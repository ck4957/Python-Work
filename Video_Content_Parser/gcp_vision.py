import os
from google.cloud import videointelligence_v1 as videointelligence
from google.cloud import speech_v1 as speech
from google.cloud import vision_v1 as vision
from google.cloud import language_v1 as language
import json

def analyze_video_content(video_path):
    """Analyzes video content using Google Cloud Video Intelligence API"""
    client = videointelligence.VideoIntelligenceServiceClient()

    with open(video_path, "rb") as file:
        input_content = file.read()

    features = [
        videointelligence.Feature.LABEL_DETECTION,
        videointelligence.Feature.SHOT_CHANGE_DETECTION,
        videointelligence.Feature.TEXT_DETECTION,
    ]

    operation = client.annotate_video(
        request={"features": features, "input_content": input_content}
    )
    
    print("Processing video...")
    result = operation.result(timeout=180)
    
    return result

def transcribe_audio(audio_path):
    """Transcribes audio using Google Cloud Speech-to-Text API"""
    client = speech.SpeechClient()

    with open(audio_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    response = client.recognize(config=config, audio=audio)
    
    return response

def analyze_text(text):
    """Analyzes text using Google Cloud Natural Language API"""
    client = language.LanguageServiceClient()

    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)
    
    response = client.analyze_entities(request={'document': document})
    
    return response

def extract_code_snippets(text):
    """
    A simple function to extract potential code snippets.
    This is a basic implementation and might need to be refined.
    """
    # This is a very simplistic approach. In reality, you'd need a more sophisticated method.
    code_snippets = []
    lines = text.split('\n')
    in_code_block = False
    current_snippet = []
    
    for line in lines:
        if line.strip().startswith('```') or line.strip().startswith('def ') or line.strip().startswith('class '):
            if in_code_block:
                code_snippets.append('\n'.join(current_snippet))
                current_snippet = []
            in_code_block = not in_code_block
        elif in_code_block:
            current_snippet.append(line)
    
    if current_snippet:
        code_snippets.append('\n'.join(current_snippet))
    
    return code_snippets

def process_video(video_path, audio_path):
    # Analyze video content
    video_result = analyze_video_content(video_path)
    
    # Transcribe audio
    audio_result = transcribe_audio(audio_path)
    
    # Combine transcribed text
    full_text = ' '.join([result.alternatives[0].transcript for result in audio_result.results])
    
    # Analyze the full text
    text_analysis = analyze_text(full_text)
    
    # Extract potential code snippets
    code_snippets = extract_code_snippets(full_text)
    
    # Prepare results
    results = {
        'video_labels': [label.entity.description for label in video_result.annotation_results[0].shot_label_annotations],
        'detected_text': [text.text for text in video_result.annotation_results[0].text_annotations],
        'transcribed_text': full_text,
        'entities': [{'name': entity.name, 'type': language.Entity.Type(entity.type_).name} for entity in text_analysis.entities],
        'code_snippets': code_snippets
    }
    
    return results

def save_results(results, output_file):
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)

# Example usage
video_path = "path/to/your/video.mp4"
audio_path = "path/to/your/audio.wav"
output_file = "video_analysis_results.json"

results = process_video(video_path, audio_path)
save_results(results, output_file)

print(f"Video content has been processed and saved to {output_file}")
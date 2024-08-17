import cv2
import pytesseract
from PIL import Image
import numpy as np
from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch

def extract_frames(video_path, interval=1):
    print('Extracting Frames')
    video = cv2.VideoCapture(video_path)
    frames = []
    count = 0
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        if count % interval == 0:
            frames.append(frame)
        count += 1
    video.release()
    return frames

def ocr_frame(frame):
    print('Performing OCR')
    img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    text = pytesseract.image_to_string(img)
    return text

def describe_image(frame, model, feature_extractor, tokenizer):
    print('Describe Image')
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values
    generated_ids = model.generate(pixel_values)
    generated_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return generated_text

def process_video(video_path):
    print('Process Video')
    frames = extract_frames(video_path)
    
    # Load models for image captioning
    model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    feature_extractor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
    
    results = []
    for frame in frames:
        ocr_text = ocr_frame(frame)
        description = describe_image(frame, model, feature_extractor, tokenizer)
        results.append({
            "ocr_text": ocr_text,
            "description": description
        })
    
    return results

def save_to_file(results, output_file):
    with open(output_file, 'w') as f:
        for result in results:
            f.write(f"OCR Text: {result['ocr_text']}\n")
            f.write(f"Description: {result['description']}\n\n")

# Example usage
video_path = "coding_video_sample.mp4"
output_file = "video_content.txt"

results = process_video(video_path)
save_to_file(results, output_file)

print(f"Video content has been processed and saved to {output_file}")

# Note: To store in a vector database, you would need to add code here to
# convert the text results into vectors (e.g., using a sentence transformer)
# and then store those vectors in your chosen vector database.
import os
import cv2
import numpy as np
from utils import get_face_landmarks

# Data directory
data_dir = './data'

print("Current Working Directory:", os.getcwd())
print("Data Directory:", os.path.abspath(data_dir))

output = []
image_count = 0
total_processed = 0

# Enhanced logging for debugging
print(f"Scanning directory: {data_dir}")

for emotion_indx, emotion in enumerate(sorted(os.listdir(data_dir))):
    emotion_path = os.path.join(data_dir, emotion)
    
    # Check if the path is a directory
    if not os.path.isdir(emotion_path):
        print(f"Skipping non-directory: {emotion_path}")
        continue

    print(f"Processing emotion: {emotion} (Index: {emotion_indx})")

    for image_path_ in os.listdir(emotion_path):
        image_path = os.path.join(emotion_path, image_path_)

        # Try reading the image
        image = cv2.imread(image_path)
        if image is None:
            print(f"Failed to read image: {image_path}")
            continue

        try:
            face_landmarks = get_face_landmarks(image)
        except Exception as e:
            print(f"Error in get_face_landmarks for image {image_path}: {e}")
            continue

        # Log the number of landmarks detected
        print(f"Image: {image_path}, Landmarks detected: {len(face_landmarks)}")

        if len(face_landmarks) == 1404:
            face_landmarks.append(int(emotion_indx))
            output.append(face_landmarks)
            image_count += 1

        total_processed += 1

# Save the final output in one file 'data.txt'
if len(output) > 0:
    output_file = os.path.abspath('data.txt')
    np.savetxt(output_file, np.asarray(output), fmt='%f')
    print(f"Data successfully saved to {output_file}")
else:
    print("No valid landmarks were found.")

# Log the number of images processed
print(f"Total images processed: {total_processed}")
print(f"Images that matched landmark criteria: {image_count}")

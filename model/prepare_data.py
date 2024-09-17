# import os
# import cv2
# import numpy as np
# from utils import get_face_landmarks

# # data directory
# data_dir = './data'

# print("Current Working Directory:", os.getcwd())
# print(os.path.abspath(data_dir))


# output = []
# for emotion_indx, emotion in enumerate(sorted(os.listdir(data_dir))):
#     for image_path_ in os.listdir(os.path.join(data_dir, emotion)):
#         image_path = os.path.join(data_dir, emotion, image_path_)

#         image = cv2.imread(image_path)
#         face_landmarks = get_face_landmarks(image)

#         if len(face_landmarks) == 1404: 
#             face_landmarks.append(int(emotion_indx))
#             output.append(face_landmarks)

# np.savetxt('data.txt', np.asarray(output))


# import os
# import cv2
# import numpy as np
# from utils import get_face_landmarks

# # data directory
# data_dir = './data'

# print("Current Working Directory:", os.getcwd())
# print(os.path.abspath(data_dir))

# output = []
# for emotion_indx, emotion in enumerate(sorted(os.listdir(data_dir))):
#     emotion_path = os.path.join(data_dir, emotion)
#     # Check if the path is a directory
#     if not os.path.isdir(emotion_path):
#         print(f"Skipping non-directory: {emotion_path}")
#         continue

#     for image_path_ in os.listdir(emotion_path):
#         image_path = os.path.join(emotion_path, image_path_)

#         # Try reading the image
#         image = cv2.imread(image_path)
#         if image is None:
#             print(f"Failed to read image: {image_path}")
#             continue

#         face_landmarks = get_face_landmarks(image)

#         if len(face_landmarks) == 1404: 
#             face_landmarks.append(int(emotion_indx))
#             output.append(face_landmarks)

# np.savetxt('data.txt', np.asarray(output))
import os
import cv2
import numpy as np
from utils import get_face_landmarks

# Data directory
data_dir = './data'

print("Current Working Directory:", os.getcwd())
print("Data Directory:", os.path.abspath(data_dir))

output = []

for emotion_indx, emotion in enumerate(sorted(os.listdir(data_dir))):
    emotion_path = os.path.join(data_dir, emotion)
    
    # Check if the path is a directory
    if not os.path.isdir(emotion_path):
        print(f"Skipping non-directory: {emotion_path}")
        continue

    for image_path_ in os.listdir(emotion_path):
        image_path = os.path.join(emotion_path, image_path_)

        # Try reading the image
        image = cv2.imread(image_path)
        if image is None:
            print(f"Failed to read image: {image_path}")
            continue

        face_landmarks = get_face_landmarks(image)

        if len(face_landmarks) == 1404:
            face_landmarks.append(int(emotion_indx))
            output.append(face_landmarks)

# Check if the output has data before saving
if len(output) > 0:
    output_file = 'data.txt'
    try:
        np.savetxt(output_file, np.asarray(output))
        print(f"Data saved to {output_file}")
    except Exception as e:
        print(f"Failed to save file: {e}")
else:
    print("No data to save.")

# Fruits Ripeness or Rottenness Detection Using YOLOv11

## Authors
- **Name:** Velman Noeli Harefa  
  **Student ID:** 1301213178  
- **Name:** Benaya Obed Sinaga  
  **Student ID:** 1301213264  

## Project Description
This project aims to detect and classify fruits into eight categories based on their condition: **good** and **bad**. The model used is **YOLOv11**, implemented in a web-based application using **Streamlit** to support automated quality assessment and sorting processes in the agricultural and retail sectors.

## Dataset
The dataset consists of 4,399 images divided into:
- **70%** for training data
- **20%** for validation data
- **10%** for testing data

The dataset includes 8 categories:
1. Apple (good and bad)
2. Banana (good and bad)
3. Orange (good and bad)
4. Pomegranate (good and bad)

## Model and Experiments
The YOLOv11 model was trained using the **SGD optimizer** with the following hyperparameter configurations:
- **Learning Rate (lr0):** 0.01
- **Momentum:** 0.9
- **Weight Decay:** 0.0005
- **Image Size:** 640x640 pixels

### Epochs Used
The model was tested with three different numbers of epochs:
1. **50 epochs:** Provided initial results with precision and recall above 0.98.
2. **100 epochs:** Achieved the best balance between accuracy and efficiency with:
   - Precision: **0.988**
   - Recall: **0.993**
   - mAP50: **0.993**
3. **150 epochs:** Showed high performance with a slight improvement in mAP50:95.

## Implementation
The trained YOLOv11 model was implemented in a web-based application that allows users to upload fruit images and obtain real-time detection results, including:
- Bounding boxes
- Category labels
- Prediction confidence levels

The application is designed to facilitate the sorting and quality assessment of fruits in the agricultural and retail industries.

## Technologies Used
- **Model Framework:** YOLOv11
- **Application Framework:** Streamlit
- **Programming Language:** Python

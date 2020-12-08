from keras.models import load_model
from keras_preprocessing import image
import numpy as np

print("Enter 1 for Skin Cancer Diagnosis \n"
      "Enter 2 for Brain Tumor Diagnosis \n"
      "Enter 3 for Diabetes Diagnosis \n"
      "Enter 4 for Heart Disease Diagnosis \n"
      "Enter 5 for Breast Cancer Diagnosis \n"
      "Enter 6 for COVID 19 Diagnosis")
selected = input("Enter choice(1/2/3/4/5/6): ")

if selected == '1':
      model = load_model('SCC.hdf5')
      test_image = image.load_img('D:/Documents/SKIN CANCER/skin-cancer-detection/testing model/Negative/divya.jpeg',
                                  target_size=(32, 32))
      test_image = image.img_to_array(test_image)
      test_image = np.expand_dims(test_image, axis=0)
      prediction = model.predict(test_image)
      print(prediction)
      print(prediction.shape)
      if (prediction[0][0] == 1):
            print("Basal Cell Carcinoma,NON MELANOMA SKIN CANCER, POSITIVE")
      elif (prediction[0][1] == 1):
            print("Benign,NEGATIVE")
      elif (prediction[0][2] == 1):
            print("Melanoma,POSITIVE")
      else:
            print("Squamous cell carcinoma,NON MELANOMA SKIN CANCER,POSITVE")
elif selected =='2':
      model = load_model('brain_tumor.hdf5')

elif selected =='3':
      model = load_model('diabetes.hdf5')

elif selected =='4':
      model = load_model('heart_disease.sav')

elif selected =='5':
      model = load_model('breast_cancer.hdf5')
elif selected =='6':
      model = load_model('Covid19.hdf5')

else:
      print("invalid response")

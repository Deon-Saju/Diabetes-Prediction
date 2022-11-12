import numpy as np
import pickle
import streamlit as st
import base64


#Add an image from local
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local(r"C:\Users\LENOVO\Dropbox\PC\Downloads\syringe.jpg")

#Add image using URL 
#def add_bg_from_url():
    
#    st.markdown(
#          f"""
#          <style>
#          .stApp {{
#              background-image: url("https://cdn.pixabay.com/photo/2016/12/05/19/49/syringe-1884784_960_720.jpg");
#              background-attachment: fixed;
#              background-size: cover;

#          }}
#          </style>
#          """,
#          unsafe_allow_html=True
#      )

# add_bg_from_url() 


# loading the saved model
loaded_model = pickle.load(open('C:/Users/LENOVO/Documents/SEMESTER 3/trained_model_1.sav', 'rb'))


# creating a function for Prediction

def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'
  
    
  
def main():
    
    
    # giving a title
    
    st.markdown("""
    <style>
    .big-font {
        font-size:70px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<p class="big-font">Diabetes Prediction </p>', unsafe_allow_html=True)
    

    Pregnancies = st.text_input('Number of Pregnancies', )
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure value')
    SkinThickness = st.text_input('Skin Thickness value')
    Insulin = st.text_input('Insulin Level')
    BMI = st.text_input('BMI value')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    Age = st.text_input('Age of the Person')
    
    # Add css to make text bigger
    st.markdown(
        """
        <style>
        textarea {
            font-size: 0.5rem !important;
        }
        input {
            font-size: 1rem !important;
        }
        .css-81oif8  {
            font-size: 20px;
        }
        .css-81oif8 {
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
    
    #code for Prediction
    diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
    st.success(diagnosis)
       
    
if __name__ == '__main__':
    main()
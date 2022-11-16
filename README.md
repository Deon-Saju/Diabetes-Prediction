# Diabetes-Prediction

### About Diabetes
Diabetes is a chronic condition brought on by either insufficient insulin production by the pancreas or inefficient insulin utilisation by the body. A hormone called insulin controls blood sugar levels. Uncontrolled diabetes frequently causes hyperglycemia, also known as raised blood glucose or raised blood sugar, which over time can seriously harm many different bodily systems, particularly the nerves and blood vessels.

Diabetes can pose issues for pregnant women and their unborn children. Poor diabetes management during pregnancy raises the baby's risk for birth abnormalities and other issues. For the woman, it may also result in major difficulties. Birth abnormalities and other health issues can be prevented with proper prenatal and postpartum treatment.

### Dataset
This dataset is originally from the National Institute of Diabetes and Digestive and Kidney Diseases. The objective is to predict based on diagnostic measurements whether a patient has diabetes.

https://www.dropbox.com/s/uh7o7uyeghqkhoy/diabetes.csv?dl=0

#### Variables
Several constraints were placed on the selection of these instances from a larger database. In particular, all patients here are females at least 21 years old of Pima Indian heritage.

- Pregnancies: Number of times pregnant
- Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
- BloodPressure: Diastolic blood pressure (mm Hg)
- SkinThickness: Triceps skin fold thickness (mm)
- Insulin: 2-Hour serum insulin (mu U/ml)
- BMI: Body mass index (weight in kg/(height in m)^2)
- DiabetesPedigreeFunction: Diabetes pedigree function
- Age: Age (years)
- Outcome: Class variable (0 or 1)

![image](https://user-images.githubusercontent.com/85385312/202089997-85b6b3a7-6e9f-4f78-9d29-b3ba3a882494.png)


Sources:

(a) Original owners: National Institute of Diabetes and Digestive and Kidney Diseases

(b) Donor of database: Vincent Sigillito (vgs@aplcen.apl.jhu.edu)
Research Center, RMI Group Leader
Applied Physics Laboratory
The Johns Hopkins University
Johns Hopkins Road
Laurel, MD 20707
(301) 953-6231

(c) Date received: 9 May 1990

### Aim of the project
To develop a system which can perform early prediction of diabetes for a patient with a higher accuracy by combining the results of different machine learning techniques.This project aims to predict diabetes via various different supervised machine learning methods. A UI is developed using streamlit so that users can check if they have diabetes or not.

### Modelling and Analysis
Various models were used to find the best results. Among the models used, Logistic Regression and Decision Tree gave the best result with a accuracy of 0.786458

![image](https://user-images.githubusercontent.com/85385312/202093247-a858ce29-1ba0-4b84-89b4-7a6c4345c1a5.png)

### Creating a User Interface
The last  part  of   the  project  is   the  creation  of  a  user   interface for   the  model. This   user-interface is used to enter unseen data for the model to read and then make a prediction.The UI was created using Streamlit with some CSS elements.

![image](https://user-images.githubusercontent.com/85385312/202097253-4c8def8b-f2ae-4ca8-8a33-f00c0bbe97b1.png)

### Conclusion
The goal of the study was to create a model that could identify diabetic individuals who are most likely to be admitted to the hospital. Prediction of risk of hospital admissionis a  fairly complex task. This procedure and its result are influenced by numerous factors. Methods to improve healthcare institutions' understanding of what matters in predicting the probability of hospital admission are urgently needed right now. By suggesting a system that can be used as an aid in identifying the patients who are most at risk of developing diabetes, this project makes a small contribution to currently used methods of diabetes detection. It does this by examining a number of important factors, including the patient's blood glucose level, body mass index, etc. Based on the pertinent medical data that is gathered through a Web application, the project forecasts the onset of diabetes in a person. The user's complete set of required medical information is entered into the online Web application, and this information is then sent to the trained model so it can determine if the user has diabetes or not.

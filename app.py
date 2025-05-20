import streamlit as st
import pandas as pd
import joblib
import numpy as np
from preprocessing import (
    encoder_Course,
    encoder_Daytime_evening_attendance,
    encoder_Gender,
    encoder_Marital_status,
    encoder_Fathers_occupation,
    encoder_Mothers_occupation,
    encoder_Nacionality,
    encoder_Previous_qualification,
    encoder_Scholarship_holder,
    encoder_Tuition_fees_up_to_date
)
from preprocessing import data_preprocessing
from prediction import prediction 

# Streamlit app
st.title("Student Status Prediction App")

data = pd.DataFrame()

# Inputan pengguna
col1, col2 = st.columns(2)

with col1:
    Course = st.selectbox("Course", options=encoder_Course.classes_)
    Daytime_evening_attendance = st.selectbox("Attendance", options=encoder_Daytime_evening_attendance.classes_)
    Gender = st.selectbox("Gender", options=encoder_Gender.classes_)
    Marital_status = st.selectbox("Marital Status", options=encoder_Marital_status.classes_)
    Fathers_occupation = st.selectbox("Father's Occupation", options=encoder_Fathers_occupation.classes_)

with col2:
    Mothers_occupation = st.selectbox("Mother's Occupation", options=encoder_Mothers_occupation.classes_)
    Nacionality = st.selectbox("Nationality", options=encoder_Nacionality.classes_)
    Previous_qualification = st.selectbox("Previous Qualification", options=encoder_Previous_qualification.classes_)
    Scholarship_holder = st.selectbox("Scholarship Holder", options=encoder_Scholarship_holder.classes_)
    Tuition_fees_up_to_date = st.selectbox("Tuition Fees Up To Date", options=encoder_Tuition_fees_up_to_date.classes_)

# Input nilai numerik
Admission_grade = st.number_input("Admission Grade", min_value=0.0, max_value=200.0, value=120.0)
Previous_qualification_grade = st.number_input("Previous Qualification Grade", min_value=0.0, max_value=200.0, value=150.0)
Curricular_units_1st_sem_grade = st.number_input("1st Sem Curricular Grade", min_value=0.0, max_value=20.0, value=10.0)
Curricular_units_2nd_sem_grade = st.number_input("2nd Sem Curricular Grade", min_value=0.0, max_value=20.0, value=12.0)

# Susun ke dataframe
data["Course"] = [Course]
data["Daytime_evening_attendance"] = [Daytime_evening_attendance]
data["Gender"] = [Gender]
data["Marital_status"] = [Marital_status]
data["Fathers_occupation"] = [Fathers_occupation]
data["Mothers_occupation"] = [Mothers_occupation]
data["Nacionality"] = [Nacionality]
data["Previous_qualification"] = [Previous_qualification]
data["Scholarship_holder"] = [Scholarship_holder]
data["Tuition_fees_up_to_date"] = [Tuition_fees_up_to_date]
data["Admission_grade"] = [Admission_grade]
data["Previous_qualification_grade"] = [Previous_qualification_grade]
data["Curricular_units_1st_sem_grade"] = [Curricular_units_1st_sem_grade]
data["Curricular_units_2nd_sem_grade"] = [Curricular_units_2nd_sem_grade]

with st.expander("View Raw Input"):
    st.dataframe(data)

if st.button("Predict"):
    new_data = data_preprocessing(data)
    
        # URUTKAN sesuai urutan saat training
    expected_columns = [
        'Marital_status',
        'Course',
        'Daytime_evening_attendance',
        'Previous_qualification',
        'Previous_qualification_grade',
        'Nacionality',
        'Mothers_occupation',
        'Fathers_occupation',
        'Admission_grade',
        'Tuition_fees_up_to_date',
        'Gender',
        'Scholarship_holder',
        'Curricular_units_1st_sem_grade',
        'Curricular_units_2nd_sem_grade'
    ]
    new_data = new_data[expected_columns]
    
    with st.expander("View Preprocessed Data"):
        st.dataframe(new_data)

    # y_pred_encoded = model.predict(new_data)
    # prediction_label = encoder_target.inverse_transform(y_pred_encoded)[0]
    prediction_label = prediction(new_data)

    st.subheader(f"Predicted Status: {prediction_label}")

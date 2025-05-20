import joblib
import numpy as np
import pandas as pd

encoder_Course = joblib.load("models/encoder_Course.joblib")
encoder_Daytime_evening_attendance = joblib.load("models/encoder_Daytime_evening_attendance.joblib")
encoder_Gender = joblib.load("models/encoder_Gender.joblib")
encoder_Marital_status = joblib.load("models/encoder_Marital_status.joblib")
encoder_Fathers_occupation = joblib.load("models/encoder_Fathers_occupation.joblib")
encoder_Mothers_occupation = joblib.load("models/encoder_Mothers_occupation.joblib")
encoder_Nacionality = joblib.load("models/encoder_Nacionality.joblib")
encoder_Previous_qualification = joblib.load("models/encoder_Previous_qualification.joblib")
encoder_Scholarship_holder = joblib.load("models/encoder_Scholarship_holder.joblib")
encoder_Tuition_fees_up_to_date = joblib.load("models/encoder_Tuition_fees_up_to_date.joblib")


scaler_Admission_grade = joblib.load("models/scaler_Admission_grade.joblib")
scaler_Previous_qualification_grade = joblib.load("models/scaler_Previous_qualification_grade.joblib")
scaler_Curricular_units_1st_sem_grade = joblib.load("models/scaler_Curricular_units_1st_sem_grade.joblib")
scaler_Curricular_units_2nd_sem_grade = joblib.load("models/scaler_Curricular_units_2nd_sem_grade.joblib")


def data_preprocessing(data):
  
    data = data.copy()
    df = pd.DataFrame()

    # Encoding categorical features
    df["Course"] = encoder_Course.transform(data["Course"])
    df["Daytime_evening_attendance"] = encoder_Daytime_evening_attendance.transform(data["Daytime_evening_attendance"])
    df["Gender"] = encoder_Gender.transform(data["Gender"])
    df["Marital_status"] = encoder_Marital_status.transform(data["Marital_status"])
    df["Fathers_occupation"] = encoder_Fathers_occupation.transform(data["Fathers_occupation"])
    df["Mothers_occupation"] = encoder_Mothers_occupation.transform(data["Mothers_occupation"])
    df["Nacionality"] = encoder_Nacionality.transform(data["Nacionality"])
    df["Previous_qualification"] = encoder_Previous_qualification.transform(data["Previous_qualification"])
    df["Scholarship_holder"] = encoder_Scholarship_holder.transform(data["Scholarship_holder"])
    df["Tuition_fees_up_to_date"] = encoder_Tuition_fees_up_to_date.transform(data["Tuition_fees_up_to_date"])

    # Scaling numerical features
    df["Admission_grade"] = scaler_Admission_grade.transform(np.asarray(data["Admission_grade"]).reshape(-1, 1)).flatten()
    df["Previous_qualification_grade"] = scaler_Previous_qualification_grade.transform(np.asarray(data["Previous_qualification_grade"]).reshape(-1, 1)).flatten()
    df["Curricular_units_1st_sem_grade"] = scaler_Curricular_units_1st_sem_grade.transform(np.asarray(data["Curricular_units_1st_sem_grade"]).reshape(-1, 1)).flatten()
    df["Curricular_units_2nd_sem_grade"] = scaler_Curricular_units_2nd_sem_grade.transform(np.asarray(data["Curricular_units_2nd_sem_grade"]).reshape(-1, 1)).flatten()

    return df
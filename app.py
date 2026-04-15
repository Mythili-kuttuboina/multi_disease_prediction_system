import streamlit as st
import pickle
import numpy as np

# Load the saved models from the current directory
heart_model = pickle.load(open('heart_disease_model.sav','rb'))
diabetes_model = pickle.load(open('diabetes_disease_model.sav','rb'))
parkinsons_model = pickle.load(open('parkinson_disease_model.sav','rb'))

st.title("Multi Disease Prediction System")

disease = st.selectbox("Select Disease", ("Heart Disease", "Diabetes", "Parkinsons"))
if disease == "Heart Disease":

    st.title("❤️ Heart Disease Prediction")

    age = st.number_input("age")
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type", [0,1,2,3])
    trestbps = st.number_input("Resting Blood Pressure")
    chol = st.number_input("Cholesterol")
    fbs = st.selectbox("Fasting Blood Sugar > 120", ["Yes", "No"])
    restecg = st.selectbox("Rest ECG", [0,1,2])
    thalach = st.number_input("Max Heart Rate")
    exang = st.selectbox("Exercise Induced Angina", ["Yes", "No"])
    oldpeak = st.number_input("Oldpeak")
    slope = st.selectbox("Slope", [0,1,2])
    ca = st.selectbox("Major Vessels", [0,1,2,3])
    thal = st.selectbox("Thal", [1,2,3])

    # Encoding
    sex = 1 if sex == "Male" else 0
    fbs = 1 if fbs == "Yes" else 0
    exang = 1 if exang == "Yes" else 0

    if st.button("Predict Heart Disease"):
        data = np.array([[age, sex, cp, trestbps, chol, fbs,
                          restecg, thalach, exang, oldpeak,
                          slope, ca, thal]])

        result = heart_model.predict(data)

        if result[0] == 1:
            st.error("⚠️ Heart Disease Detected")
        else:
            st.success("✅ No Heart Disease")


# ================= DIABETES =================
elif disease == "Diabetes":

    st.title("🩸 Diabetes Prediction")

    # -------- INPUTS --------
    age = st.number_input("Age")
    gender = st.selectbox("Gender", ["Male", "Female"])
    bmi = st.number_input("BMI")
    bp = st.number_input("Blood Pressure")
    glucose = st.number_input("Glucose")
    insulin = st.number_input("Insulin")
    hba1c = st.number_input("HbA1c")
    chol = st.number_input("Cholesterol")
    trig = st.number_input("Triglycerides")

    smoking = st.selectbox("Smoking", ["Yes", "No"])
    activity = st.selectbox("Physical Activity", ["Low", "Medium", "High"])
    family = st.selectbox("Family History", ["Yes", "No"])

    bmi_cat = st.selectbox("BMI Category", ["Normal", "Overweight", "Obese"])
    bp_cat = st.selectbox("BP Category", ["Normal", "High"])
    chol_risk = st.selectbox("Cholesterol Risk", ["Low", "Medium", "High"])

    # -------- ENCODING --------
    gender = 1 if gender == "Male" else 0
    smoking = 1 if smoking == "Yes" else 0
    family = 1 if family == "Yes" else 0

    activity = {"Low":0, "Medium":1, "High":2}[activity]
    bmi_cat = {"Normal":0, "Overweight":1, "Obese":2}[bmi_cat]
    bp_cat = {"Normal":0, "High":1}[bp_cat]
    chol_risk = {"Low":0, "Medium":1, "High":2}[chol_risk]

    # -------- PREDICT --------
    if st.button("Predict Diabetes"):

        data = np.array([[age, gender, bmi, bp, glucose, insulin,
                          hba1c, chol, trig,
                          smoking, activity, family,
                          bmi_cat, bp_cat, chol_risk]])

        result = diabetes_model.predict(data)

        if result[0] == 1:
            st.error("⚠️ Diabetes Detected")
        else:
            st.success("✅ No Diabetes")

# ================= PARKINSON'S =================


elif disease == "Parkinsons":
     st.title("🧠 Parkinson’s Disease Prediction")

# -------- INPUTS --------
     age = st.number_input("Age", min_value=0)

     gender = st.selectbox("Gender", ["Male", "Female"])
     ethnicity = st.selectbox("Ethnicity", ["Asian", "African", "Caucasian", "Other"])
     education = st.selectbox("Education Level", ["Primary", "Secondary", "Graduate", "Postgraduate"])

     bmi = st.number_input("BMI")

     smoking = st.selectbox("Smoking", ["Yes", "No"])
     alcohol = st.number_input("Alcohol Consumption")
     activity = st.number_input("Physical Activity")
     diet = st.number_input("Diet Quality")
     sleep_quality = st.number_input("Sleep Quality")

     family_history = st.selectbox("Family History Parkinsons", ["Yes", "No"])
     tbi = st.selectbox("Traumatic Brain Injury", ["Yes", "No"])
     hypertension = st.selectbox("Hypertension", ["Yes", "No"])
     diabetes_p = st.selectbox("Diabetes", ["Yes", "No"])
     depression = st.selectbox("Depression", ["Yes", "No"])
     stroke = st.selectbox("Stroke", ["Yes", "No"])

     sys_bp = st.number_input("Systolic BP")
     dia_bp = st.number_input("Diastolic BP")

     chol_total = st.number_input("Cholesterol Total")
     chol_ldl = st.number_input("Cholesterol LDL")
     chol_hdl = st.number_input("Cholesterol HDL")
     chol_trig = st.number_input("Cholesterol Triglycerides")

     updrs = st.number_input("UPDRS")
     moca = st.number_input("MoCA")
     functional = st.number_input("Functional Assessment")

# 🔥 NEW COLUMNS
     motor_score = st.number_input("Motor Score")
     early_symptoms = st.selectbox("Early Symptoms", ["Yes", "No"])

     tremor = st.selectbox("Tremor", ["Yes", "No"])
     rigidity = st.selectbox("Rigidity", ["Yes", "No"])
     brady = st.selectbox("Bradykinesia", ["Yes", "No"])
     postural = st.selectbox("Postural Instability", ["Yes", "No"])
     speech = st.selectbox("Speech Problems", ["Yes", "No"])
     sleep_dis = st.selectbox("Sleep Disorders", ["Yes", "No"])
     constipation = st.selectbox("Constipation", ["Yes", "No"])

# -------- ENCODING --------
     gender = 1 if gender == "Male" else 0

     ethnicity = {"Asian":0, "African":1, "Caucasian":2, "Other":3}[ethnicity]
     education = {"Primary":0, "Secondary":1, "Graduate":2, "Postgraduate":3}[education]

     def yn(x): return 1 if x == "Yes" else 0

     smoking = yn(smoking)
     family_history = yn(family_history)
     tbi = yn(tbi)
     hypertension = yn(hypertension)
     diabetes_p = yn(diabetes_p)
     depression = yn(depression)
     stroke = yn(stroke)

     early_symptoms = yn(early_symptoms)

     tremor = yn(tremor)
     rigidity = yn(rigidity)
     brady = yn(brady)
     postural = yn(postural)
     speech = yn(speech)
     sleep_dis = yn(sleep_dis)
     constipation = yn(constipation)

# -------- PREDICTION --------
     if st.button("Predict Parkinsons"):

         input_data = np.array([[
                    age, gender, ethnicity, education, bmi,
                    smoking, alcohol, activity, diet, sleep_quality,
                    family_history, tbi, hypertension, diabetes_p,
                    depression, stroke,
                    sys_bp, dia_bp,
                    chol_total, chol_ldl, chol_hdl, chol_trig,
                    updrs, moca, functional,
                    motor_score, early_symptoms,   # 🔥 NEW FEATURES
                    tremor, rigidity, brady, postural,
                    speech, sleep_dis, constipation
    ]])

         prediction = parkinsons_model.predict(input_data)

    # -------- OUTPUT --------
         if prediction[0] == 1:
            st.error("⚠️ Parkinson’s Disease Detected")
         else:
            st.success("✅ No Parkinson’s Disease")
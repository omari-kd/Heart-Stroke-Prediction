# Heart-Stroke-Prediction

This data science project aims to predict the likelihood of a patient experiencing a stroke based on various input parameters such as gender, age, presence of diseases and smoking status. The dataset provides relevant information about each patient, enabling the development of a predictive model.

According to the World Health Organization (WHO), stroke is the second leading cause of death worldwide, responsible for approximately 11% of total deaths. This project aims to leverage machine learning techniques to build a predictive model that can identify individuals at risk of stroke based on their demographic and health-related features. By detecting high-risk individuals early, appropriate preventive measures can be taken to reduce the incidence and impact of stroke.

# About the dataset

The dataset used in this project contains information necessary to predict the occurrence of a stroke. Each row in the dataset represents a patient, and the dataset includes the following attributes:

- id: Unique identifier
- gender: "Male", "Female" or "Other"
- age: Age of the patient
- hypertension: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension
- heart_disease: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease
- ever_married: "No" or "Yes"
- work_type: "Children", "Govt_job", "Never_worked", "Private" or "Self-employed"
- Residence_type: "Rural" or "Urban"
- avg_glucose_level: Average glucose level in the blood
- bmi: Body mass index
- smoking_status: "Formerly smoked", "Never smoked", "Smokes" or "Unknown"
- stroke: 1 if the patient had a stroke, 0 if not

# Data Visualisation

![Image](https://github.com/user-attachments/assets/1f7a9a4e-6d27-4273-b7fc-1ec61e6e9c12)

# Running the Streamlit App

This project includes an interactive web app for predicting stroke risk using a trained machine learning model.

### Requirements

Make sure you have installed the required packages:

```bash
pip install -r requirements.txt
```

### Running the App

```bash
streamlit run app.py
```

App is available at `https://omari-heartstrokeprediction.streamlit.app/`.

# Tools & Technologies

- **Python**: Core language for data analysis and modeling
  - `pandas`, `NumPy` — for data manipulation and numerical operations
  - `Matplotlib`, `Seaborn` — for data visualization
  - `scikit-learn` — for machine learning modeling and evaluation
- **Jupyter Notebook**: For interactive development, analysis and documentation of the data science workflow
- **Streamlit**: For deploying the model as a simple web app
- **VS Code**: Code editing and project management
- **Git & GitHub**: Version control and collaboration

# Contribution

Open to suggestions and improvements! Submit issues or pull requests.

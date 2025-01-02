# **Medicine Recommendation ML Project**

![Project Banner](path/to/your/image.png)  
*A Machine Learning-based solution for personalized medicine recommendations.*

---

## **Description**
The **Medicine Recommendation System** uses Machine Learning to predict diseases based on symptoms and recommend medicines, diets, and precautions. Built with Django, it features trained models and comprehensive datasets, offering a user-friendly interface for patients and doctors to enhance healthcare accessibility and decision-making.

---

## **Objectives**
- **Symptom Analysis**: Identify and interpret symptoms provided by the user.
- **Disease Prediction**: Predict possible diseases based on symptoms using trained ML models.
- **Medicine Suggestion**: Recommend medicines, diets, and precautions tailored to the predicted disease.
- **Ease of Use**: Offer a user-friendly interface for both patients and doctors to interact with the system efficiently.

---

## **Features**

### **Data-Driven Recommendations**
- Utilizes preprocessed datasets (`Symptom-severity.csv`, `Training.csv`) to analyze symptoms and their severity.
- Suggests medicines and treatments using trained models (e.g., Random Forest and Support Vector Classifier).

### **Machine Learning Models**
- **Disease Classification**: Models are trained on labeled datasets to classify diseases based on input symptoms.
- **Customizable Predictions**: Predictions can be mapped to disease names using a mapping function (`get_predicted_value`).

### **Comprehensive Datasets**
- **Symptom-Severity Dataset**: Maps symptoms to severity levels.
- **Medication Dataset**: Contains detailed information about medicines.
- **Precaution Dataset**: Provides precautions for various diseases.
- **Workout and Diet Data**: Recommends activities and nutritional guidelines.

### **Dynamic User Interaction**
- Patients can input their symptoms to receive tailored medical advice.
- Doctors can use the system for reference or as a decision-support tool.

### **Web-Based Interface**
- Built using **Django**, ensuring a modular and scalable backend.
- Frontend allows seamless interaction, including:
  - Input fields for symptoms.
  - Display of predicted diseases and recommended medicines.
  - Easy navigation through related medical advice (e.g., diets, precautions).

---

## **Project Structure**

### **Datasets**
- `symptoms_df.csv`, `description.csv`, `medications.csv`, `precautions_df.csv`, etc.
- Serve as the foundation for training and making predictions.

### **Models**
- Implemented in `medical recommendation system.ipynb`.
- Trained models (`rf.pkl`, `svc.pkl`) integrated for efficient predictions.

### **Backend (Django)**
- **Model Management**: Encapsulates business logic and database operations.
- **Views**: Handles user requests and processes responses.
- **Templates**: Renders web pages for user interaction.

### **User Interface**
- Dynamic HTML templates in the `templates` folder.
- Allows users to view and interact with predictions and recommendations.

---

## **Use Cases**

### **Patients**
- Obtain quick medical advice based on symptoms.
- Access information about medicines, diets, and precautions.

### **Doctors**
- Use the tool to verify diagnoses or recommend medicines.
- Enhance clinical decision-making with a data-backed system.

---

## **Image Examples**
- **Homepage**  
  ![Homepage](path/to/homepage_image.png)

- **Disease Prediction Results**  
  ![Prediction Results](path/to/results_image.png)

---

## **Setup Instructions**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/medicine-recommendation-ml-project.git

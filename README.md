# 🔥 AI-Powered Employee Performance Analyzer

An advanced **Streamlit-based** web application designed to predict and analyze employee performance trends using machine learning. This tool helps HR teams and managers make data-driven decisions by visualizing employee performance metrics and forecasting future trends.

## 🚀 Key Features

### 📈 Performance Trend Analysis
- Visualizes an employee’s past performance (productivity, satisfaction, projects completed) using interactive charts.
- Helps identify whether an employee is improving or declining over time.
- **Implementation**: Stores performance records over months & uses **Matplotlib/Plotly** for dynamic visualization.

### 🤖 Employee Performance Prediction
- Employs machine learning to forecast future employee performance based on historical data.
- Displays predictive insights with confidence scores.
- **Implementation**: Trained using **Scikit-Learn**, leveraging preprocessing, feature engineering, and model optimization.

### 🌐 Interactive Web Interface
- Built with **Streamlit** for an intuitive and engaging user experience.
- Enables selection of employees by department.
- Provides real-time performance trends, comparisons, and insights.

### 📊 Dataset Information

This project uses the Employee Productivity and Satisfaction HR Data dataset from Kaggle:

- **Source**: Kaggle - [Employee Productivity and Satisfaction HR Data](https://www.kaggle.com/datasets/adityaab1407/employee-productivity-and-satisfaction-hr-data)
- **Attributes**:
  - Name
  - Age
  - Gender
  - Projects Completed
  - Productivity(%)
  - Satisfaction Rate(%)
  - Feedback Score
  - Department
  - Position
  - Joining Data
  - Salary

## 📂 Project Structure
```
📂 employee_performance_app
│── 📂 data
│   ├── hr_dashboard_data.csv            # Dataset containing employee performance records
│
│── 📂 models
│   ├── performance_model.pkl            # Trained machine learning model
│
│── 📂 app
│   ├── app.py                           # Streamlit web app
│
│── 📂 notebooks
│   ├── employee_analysis.ipynb          # Data analysis, visualization & model training
│   ├── comprehensiv_analysis.ipynb      # for analysing data
│   ├── model_train.ipynb                # model training and saving into ../models/performance_model.pkl.
│   ├── predict.ipynb                    # predicting the data using trained model
│
│
│── requirements.txt                     # Dependencies
│── README.md                            # Project overview & instructions
```

## ⚙️ Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/ranjithsurineni/employee_performance_app.git
cd employee_performance_app
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit Web App
```sh
streamlit run app/app.py
```

## 📊 Data & Model
- The dataset includes **employee performance metrics**, such as productivity scores, project completion rates, and job satisfaction levels.
- A **Random Forest model** is trained for performance trend prediction.
- The model is saved in **PKL format** and loaded dynamically for real-time insights.

## 🚀 Future Enhancements
- **Advanced AI Models** (e.g., Deep Learning for more accurate predictions).
- **Interactive Dashboards** for enhanced visualization and filtering.
- **HR System Integration** for real-time employee data updates.

## 🤝 Contributing
1. **Fork** the repo.
2. **Clone** your forked repo.
3. Create a **new branch** (`git checkout -b feature-branch`).
4. **Commit changes** (`git commit -m "Added new feature"`).
5. **Push to GitHub** (`git push origin feature-branch`).
6. **Create a Pull Request**.

---
### 🖼️ Screenshots & Visualizations
Here are some screenshots of the application in action:

**🔍 Employee Performance Dashboard**
![Screenshot (34)](https://github.com/user-attachments/assets/0b22c654-59b3-4570-ac17-757f7ad59b49)

**📈 Performance v/s Department Average**
![Screenshot (37)](https://github.com/user-attachments/assets/2d2ec0fc-18c9-4e52-abee-dc560c1401d9)

**📈Predicted Performance Score, 👨‍💻Employee Details, 💰Salary Details**
![Screenshot (38)](https://github.com/user-attachments/assets/a8bdda22-db3e-4a51-993f-327769715e52)


## 📜 License
This project is licensed under the **MIT License**.

## 📞 Contact
For any queries, feel free to reach out:
- **Email**: ranjithranji1903@gmail.com
- **GitHub**: [ranjithsurineni](https://github.com/ranjithsurineni/)


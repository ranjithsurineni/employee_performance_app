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
git clone https://github.com/your-username/employee_performance_app.git
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

## 📜 License
This project is licensed under the **MIT License**.

## 📞 Contact
For any queries, feel free to reach out:
- **Email**: ranjithranji1903@gmail.com
- **GitHub**: [ranjithsurineni](https://github.com/ranjithsurineni/)


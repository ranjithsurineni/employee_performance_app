import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset and trained model
df = pd.read_csv("data/hr_dashboard_data.csv")
with open("models/performance_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Streamlit App Title
st.title("📊 Employee Performance Dashboard")

# Sidebar for Department Selection
department = st.sidebar.selectbox("Select Department", df["Department"].unique())

# Function to get employees by department
def get_employees(department):
    return df[df["Department"] == department]["Name"].tolist()

# Dropdown for Employee Selection
employees = get_employees(department)
employee_name = st.sidebar.selectbox("Select Employee", employees)


#------------------ barplot ------------------#

# Function to generate employee performance bar chart
def plot_employee_data(employee_name):
    employee = df[df["Name"] == employee_name].iloc[0]
    
    # Define performance metrics
    metrics = ["Productivity (%)", "Satisfaction Rate (%)", "Projects Completed", "Salary"]
    values = [employee[metric] for metric in metrics]

    # Convert percentage metrics to decimal percentage format
    formatted_values = [f"{v:.1f}%" if "%" in metric else f"{v}" for v, metric in zip(values, metrics)]
    
    # Create bar chart
    fig, ax = plt.subplots(figsize=(8, 5))
    barplot = sns.barplot(x=metrics, y=values, palette="viridis", ax=ax)
    

    # Add values on top of bars
    for bar, value, label in zip(barplot.patches, values, formatted_values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, label, ha='center', fontsize=12, fontweight='bold')

    ax.set_title(f"Performance Metrics: {employee_name}", fontsize=14)
    ax.set_ylabel("Value")
    ax.set_xlabel("Metrics")
    plt.xticks(rotation=30)

    return fig



#------------------ piechart ------------------#
# Function to generate overall performance pie chart
def plot_performance_pie(employee_name):
    employee = df[df["Name"] == employee_name].iloc[0]
    labels = ["Productivity (%)", "Satisfaction Rate (%)", "Feedback Score"]
    values = [employee["Productivity (%)"], employee["Satisfaction Rate (%)"], employee["Feedback Score"]]
    
    # Convert values to percentages
    values_percentage = [v for v in values]  

    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie(
        values_percentage, labels=labels, autopct='%1.1f%%',
        colors=["#ff9999", "#66b3ff", "#99ff99"], startangle=90,
        textprops={'fontsize': 12}  # Improve text readability
    )
    ax.set_title(f"Overall Performance: {employee_name}")

    # Add legend & formatting
    plt.legend(wedges, labels, title="Metrics", loc="upper right", bbox_to_anchor=(1, 0, 0.5, 1))

    return fig


#------------------ Employee Performance Analysis ------------------#

# Function to analyze Salary vs Projects Completed
def plot_salary_vs_projects(employee_name):
    employee = df[df["Name"] == employee_name].iloc[0]
    
    # Normalize values for better comparison
    max_salary = df["Salary"].max()
    max_projects = df["Projects Completed"].max()
    
    salary_percentage = (employee["Salary"] / max_salary) * 100
    projects_percentage = (employee["Projects Completed"] / max_projects) * 100
    
    categories = ["Salary (%)", "Projects Completed (%)"]
    values = [salary_percentage, projects_percentage]
    
    # Create bar chart
    fig, ax = plt.subplots()
    sns.barplot(x=categories, y=values, palette="coolwarm", ax=ax)
    
    # Annotate bars with actual values
    for i, v in enumerate(values):
        ax.text(i, v + 2, f"{v:.1f}%", ha='center', fontsize=10, fontweight='bold')
    
    ax.set_title(f"Salary vs. Projects Completed: {employee_name}")
    ax.set_ylabel("Percentage of Max Value")
    
    return fig

#------------------ Peer Benchmarking------------------#

# Function to compare employee with department average
def plot_peer_comparison(employee_name):
    employee = df[df["Name"] == employee_name].iloc[0]
    department = employee["Department"]
    
    avg_productivity = df[df["Department"] == department]["Productivity (%)"].mean()
    avg_satisfaction = df[df["Department"] == department]["Satisfaction Rate (%)"].mean()
    
    metrics = ["Productivity (%)", "Satisfaction Rate (%)"]
    values = [employee["Productivity (%)"], employee["Satisfaction Rate (%)"]]
    avg_values = [avg_productivity, avg_satisfaction]

    fig, ax = plt.subplots()
    sns.barplot(x=metrics, y=values, color="blue", label="Employee")
    sns.barplot(x=metrics, y=avg_values, color="red", alpha=0.6, label="Department Average")

    ax.legend()
    ax.set_title(f"Performance vs. Department Average: {employee_name}")
    
    return fig



#------------------ Prediction ------------------#

# Function to predict performance (converted to percentage)
def predict_performance(employee_name):
    employee = df[df["Name"] == employee_name].iloc[0]
    features = employee[["Productivity (%)", "Satisfaction Rate (%)", "Salary", "Projects Completed", "Age"]].values.reshape(1, -1)
    prediction = model.predict(features)[0]

    # Convert prediction to percentage (assuming max score is 100)
    prediction_percentage = min(max(prediction, 0), 100)  # Ensures it's within 0-100 range

    return f"Predicted Performance Score: {prediction_percentage:.2f}"


#------------------ salary details ------------------#

# Function to calculate monthly and annual salary
def calculate_salary(employee_name):
    employee = df[df["Name"] == employee_name].iloc[0]
    monthly_salary = employee["Salary"]
    annual_salary = monthly_salary * 12
    return monthly_salary, annual_salary

# Display Employee Performance
if employee_name:
    st.subheader(f"Performance Insights for {employee_name}")
    
    # Show Performance Pie Chart
    st.pyplot(plot_performance_pie(employee_name))
    
    # Show Performance Bar Chart
    st.pyplot(plot_employee_data(employee_name))
    
    # Show Salary vs Projects Completed
    st.pyplot(plot_salary_vs_projects(employee_name))

    # Show Peer Comparison
    st.pyplot(plot_peer_comparison(employee_name))  # Add this in Streamlit UI

    
    # Show Prediction
    st.success(predict_performance(employee_name))

    
    
    # Show Employee Details
    employee = df[df["Name"] == employee_name].iloc[0]
    st.markdown(f"### Employee Details:")
    st.text(f"Name: {employee_name}")
    st.text(f"Department: {employee['Department']}")
    st.text(f"Position: {employee['Position']}")
    st.text(f"Joining Date: {employee['Joining Date']}")
    st.text(f"Age: {employee['Age']}")
    
    # Show Salary Details
    monthly_salary, annual_salary = calculate_salary(employee_name)
    st.markdown(f"### Salary Details:")
    st.text(f"Monthly Salary: ${monthly_salary}")
    st.text(f"Annual Salary: ${annual_salary}")

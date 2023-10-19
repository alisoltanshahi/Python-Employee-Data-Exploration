import pandas as pd

### First we need to load the dataset
df = pd.read_csv('employees_dataset.csv')

#### Then we need to display basic information about the dataset
print("Dataset Information:")
print(df.info())

# Now it's time for statistical summary of the dataset
print("\nStatistical Summary:")
print(df.describe())

# Group data by department and calculate the average salary per department
average_salary_per_dept = df.groupby('Department')['Salary'].mean().sort_values(ascending=False)
print("\nAverage Salary by Department:")
print(average_salary_per_dept)

# Analyze the relationship between Age and Salary
age_salary_correlation = df['Age'].corr(df['Salary'])
print(f"\nCorrelation between Age and Salary: {age_salary_correlation:.2f}")

# Research Question: Does age have a significant impact on salary?

# Hypothesis Test (t-test) to determine if there's a significant difference in average salary between employees under and over 30 years old
under_30 = df[df['Age'] < 30]['Salary']
over_30 = df[df['Age'] >= 30]['Salary']

from scipy.stats import ttest_ind

t_stat, p_value = ttest_ind(under_30, over_30)
print(f"\nHypothesis Test Results:")
print(f"T-statistic: {t_stat:.2f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("There is a significant difference in average salary between employees under and over 30 years old.")
else:
    print("There is no significant difference in average salary based on age.")

# Streamlit App for Data Science Salaries Visualization

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set seaborn style
sns.set(style="whitegrid")

# Load data
df = pd.read_csv('ds_salaries.csv')

st.title("Data Science Salaries Dashboard")

# 1. Salary Trend Over Years (Line Chart)
st.subheader("Average Salary Over Years")
avg_salary_per_year = df.groupby('work_year')['salary_in_usd'].mean().reset_index()
fig1, ax1 = plt.subplots()
sns.lineplot(data=avg_salary_per_year, x='work_year', y='salary_in_usd', marker='o', ax=ax1)
ax1.set_xlabel('Year')
ax1.set_ylabel('Average Salary (USD)')
ax1.set_title('Average Salary Over Years')
st.pyplot(fig1)

# 2. Top 5 Job Titles by Average Salary (Bar Chart)
st.subheader("Top 5 Job Titles by Average Salary")
top_jobs = df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False).head(5)
fig2, ax2 = plt.subplots()
sns.barplot(x=top_jobs.values, y=top_jobs.index, palette='viridis', ax=ax2)
ax2.set_xlabel('Average Salary (USD)')
ax2.set_ylabel('Job Title')
ax2.set_title('Top 5 Job Titles by Average Salary')
st.pyplot(fig2)

# 3. Salary Distribution by Company Size (Box Plot)
st.subheader("Salary Distribution by Company Size")
fig3, ax3 = plt.subplots()
sns.boxplot(data=df, x='company_size', y='salary_in_usd', palette='Set2', ax=ax3)
ax3.set_xlabel('Company Size (S=Small, M=Medium, L=Large)')
ax3.set_ylabel('Salary (USD)')
ax3.set_title('Salary Distribution by Company Size')
st.pyplot(fig3)

# 4. Countries Offering Most Jobs (Bar Chart)
st.subheader("Top 10 Countries Offering Most Jobs")
jobs_by_country = df['company_location'].value_counts().head(10)
fig4, ax4 = plt.subplots()
sns.barplot(x=jobs_by_country.values, y=jobs_by_country.index, palette='mako', ax=ax4)
ax4.set_xlabel('Number of Jobs')
ax4.set_ylabel('Country')
ax4.set_title('Top 10 Countries Offering Most Data Science Jobs')
st.pyplot(fig4)

# 5. Most Popular Job Titles in the US (Bar Chart)
st.subheader("Most Popular Job Titles in the US")
us_jobs = df[df['company_location'] == 'US']
us_job_counts = us_jobs['job_title'].value_counts().head(10)
fig5, ax5 = plt.subplots()
sns.barplot(x=us_job_counts.values, y=us_job_counts.index, palette='coolwarm', ax=ax5)
ax5.set_xlabel('Number of Jobs')
ax5.set_ylabel('Job Title')
ax5.set_title('Most Popular Data Science Job Titles in the US')
st.pyplot(fig5)

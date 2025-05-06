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
st.markdown("**Takeaway:** Salaries have generally increased year over year, reflecting the rising demand for data professionals. This helps job seekers understand earning trends and time their entry into the job market more wisely.")

st.markdown("This line chart displays the trend of average data science salaries in USD over the years.")
st.markdown("- **Steady Growth:** Average salaries have generally increased year over year, showing positive growth in the field.")
st.markdown("- **Notable Jump:** There may be a significant salary jump in a specific year (e.g., 2021 or 2022), indicating industry-wide demand or inflation adjustment.")
st.markdown("- **Recent Plateau or Dip:** In the latest year, salary growth may have slowed or slightly declined, which could reflect market stabilization or hiring shifts.")

avg_salary_per_year = df.groupby('work_year')['salary_in_usd'].mean().reset_index()

fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.lineplot(data=avg_salary_per_year, x='work_year', y='salary_in_usd', marker='o', ax=ax1)

ax1.set_xlabel('Year')
ax1.set_ylabel('Average Salary (USD)')
ax1.set_title('Average Salary Over Years')

# Ensure each year label appears only once
ax1.set_xticks(avg_salary_per_year['work_year'].unique())

st.pyplot(fig1)


# 2. Top 5 Job Titles by Average Salary (Bar Chart)
st.subheader("Top 5 Job Titles by Average Salary")
st.markdown("**Takeaway:** Specialized roles like ML Engineers and Data Science Managers earn the most, showing that advanced skills and experience are rewarded. Job seekers can use this to guide their career focus or skill-building path.")

st.markdown("This bar chart shows the top 5 job titles with the highest average salaries.")
st.markdown("It helps identify which roles tend to be the most financially rewarding in the dataset.")
st.markdown("- **Highest Paying Role:** The top-paying job is likely a senior or specialized role, such as Machine Learning Researcher or Data Science Manager.")
st.markdown("- **Specialized Skills Pay More:** Roles that involve advanced modeling or infrastructure, like ML Engineer, typically earn more than generalist roles.")
st.markdown("- **Clear Salary Gaps:** There is a noticeable salary gap between the top role and the 4th or 5th ranked roles, highlighting value placed on expertise.")

top_jobs = df.groupby('job_title')['salary_in_usd'].mean().sort_values(ascending=False).head(5)

fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.barplot(x=top_jobs.values, y=top_jobs.index, palette='viridis', ax=ax2)

ax2.set_xlabel('Average Salary (USD)')
ax2.set_ylabel('Job Title')
ax2.set_title('Top 5 Job Titles by Average Salary')

st.pyplot(fig2)


# 3. Salary Distribution by Company Size (Box Plot)
st.subheader("Salary Distribution by Company Size")
st.markdown("**Takeaway:** Large companies tend to pay higher, but with wider variation. Smaller companies offer more consistent (but lower) pay. This helps job seekers choose the right environment based on income expectations and risk tolerance.")

st.markdown("This box plot compares salary distributions across company sizes, highlighting medians and variation.")
st.markdown("- **Large Companies Offer Higher Median Salaries:** On average, large companies (L) tend to offer higher median salaries than small (S) or medium (M) ones.")
st.markdown("- **Greater Salary Variation in Large Companies:** The range (min to max) is much wider for large companies, suggesting both high-paying executive roles and entry-level positions exist.")
st.markdown("- **More Consistent Salaries in Small Companies:** Small companies show a tighter interquartile range, indicating more consistent (but often lower) pay.")

fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.boxplot(data=df, x='company_size', y='salary_in_usd', palette='Set2', ax=ax3)

ax3.set_xlabel('Company Size (S = Small, M = Medium, L = Large)')
ax3.set_ylabel('Salary (USD)')
ax3.set_title('Salary Distribution by Company Size')

st.pyplot(fig3)



 # 4. Countries Offering Most Jobs (Bar Chart)
st.subheader("Top 10 Countries Offering Most Jobs")
st.markdown("**Takeaway:** The US leads in job offerings, followed by key European countries. This helps job seekers target regions with more opportunities, and helps governments understand where talent pipelines are needed.")

st.markdown("This bar chart shows the top 10 countries offering the most data science jobs.")
st.markdown("- The United States leads by a significant margin in job offerings.")
st.markdown("- European countries like Germany and the UK are also strong contributors.")
st.markdown("- The distribution suggests that opportunities are concentrated in a few key countries.")

jobs_by_country = df['company_location'].value_counts().head(10)

fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.barplot(x=jobs_by_country.values, y=jobs_by_country.index, palette='mako', ax=ax4)

ax4.set_xlabel('Number of Jobs')
ax4.set_ylabel('Country')
ax4.set_title('Top 10 Countries Offering Most Data Science Jobs')

st.pyplot(fig4)



# 5. Most Popular Job Titles in the US (Bar Chart)
st.subheader("Most Popular Job Titles in the US")
st.markdown("**Takeaway:** Data Scientist remains the most in-demand title, followed by Data Engineer and ML Engineer. Job seekers can align their training with the most marketable roles in the US job market.")

st.markdown("This bar chart highlights the most common data science-related job titles in the US.")
st.markdown("- Data Scientist is the most frequently listed job title.")
st.markdown("- Roles like Data Engineer and Machine Learning Engineer also appear prominently.")
st.markdown("- The distribution reflects the high demand for core data science and engineering skills.")

us_jobs = df[df['company_location'] == 'US']
us_job_counts = us_jobs['job_title'].value_counts().head(10)

fig5, ax5 = plt.subplots(figsize=(10, 6))
sns.barplot(x=us_job_counts.values, y=us_job_counts.index, palette='coolwarm', ax=ax5)

ax5.set_xlabel('Number of Jobs')
ax5.set_ylabel('Job Title')
ax5.set_title('Most Popular Data Science Job Titles in the US')

st.pyplot(fig5)

# 6. Experience Level Breakdown (Pie Chart)
st.subheader("Experience Level Breakdown")
st.markdown("**Takeaway:** Mid- and senior-level professionals make up the largest share, but there's room for entry-level talent too. This helps newcomers understand they’re entering a competitive but accessible market.")

st.markdown("This pie chart shows the distribution of experience levels among data science professionals.")
st.markdown("- **Entry-level (EN):** Represents those just starting their careers.")
st.markdown("- **Mid-level (MI):** Typically professionals with a few years of experience.")
st.markdown("- **Senior-level (SE):** Experienced practitioners with leadership or specialized roles.")
st.markdown("- **Executive-level (EX):** Top-level positions such as Heads of Data or CTOs.")

# Count each experience level
experience_counts = df['experience_level'].value_counts()

# Create the pie chart
fig6, ax6 = plt.subplots(figsize=(8, 8))
ax6.pie(experience_counts.values, labels=experience_counts.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette("pastel"))
ax6.set_title("Experience Level Distribution")
ax6.axis('equal')  # Equal aspect ratio ensures the pie chart is circular

st.pyplot(fig6)


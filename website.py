import streamlit as st
import pandas as pd
import numpy as np
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url('https://employsure.com.au/wp-content/uploads/2019/02/200624-Job-Descriptions.jpg');
    background-size: cover;
}
[data-testid="stSidebar"] {
    background-color: rgba(0,0,0,0.0);
}
h1{
    color: indianred;
}
table{
    background-color: #00425A;
    text-align: center;
}

</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)
st.title("JOB SKILLS RECOMMENDATION SYSTEM")
l=['Data Analysis', 'SQL Server', 'Data Analytics', 'powerbi', 'SQL', 'MSBI', 'Oracle', 'Training', 'tableau', 'Time management', 'Analytical', 'Data collection', 'Data analytics', 'Data Analyst', 'data visualization', 'SQL', 'Data analysis', 'Environmental science', 'Business analytics', 'Diversity and Inclusion', 'Finance', 'Corporate', 'ISS', 'Data Analyst', 'Data analytics', 'Data mining', 'Excel', 'Pivot Table', 'VLOOKUP', 'Formulas', 'Advanced Excel', 'HLOOKUP', 'BPO', 'Report Automation', 'SQL Database', 'Data Analytics', 'Data Reporting', 'excel', 'Excel', 'data visualization', 'Tableau', 'SQL', 'Python', 'Data Analytics', 'SQL', 'Excel', 'Data Analytics', 'Python', 'Data analyst', 'Engineering', 'Power Plant', 'Administration', 'Automation', 'Electronics', 'Educational', 'Engineering Maintenance', 'Quarry', 'Electrical', 'Hospital', 'mis reporting', 'Data Management', 'HLOOKUP', 'VLOOKUP', 'Data Analysis', 'report generation', 'Data Extraction', 'Advanced Excel', 'sales', 'Pivot Table', 'data monitoring', 'Data Analytics', 'Data Reporting', 'Advanced Excel', 'Pivot Table', 'MS Excel', 'VLOOKUP', 'Formulas', 'HLOOKUP', 'Informatica', 'Data Quality', 'Data Management', 'Data Mining', 'Data Analyst', 'Data Modeling', 'Solution Design', 'ETL', 'Talend', 'Data Analytics', 'SQL', 'SQL', 'Business Intelligence', 'SAS', 'Data Visualization', 'Tableau', 'Data Analytics', 'Statistics', 'Analytics', 'Python', 'Diversity and Inclusion', 'Focus', 'Banking', 'SCALA', 'Agile', 'Data Analyst', 'Asset management', 'Financial services', 'Core banking', 'Python', 'excel', 'Financial Reporting', 'advance excel', 'Finance', 'Data Analysis', 'data analyst', 'data analytics', 'performing analysis', 'report preparation', 'data governance', 'mysql', 'Performance tuning', 'Coding', 'Artificial Intelligence', 'Machine learning', 'Data Analyst', 'Data analytics', 'Analyst 3', 'Statistics', 'Analytics', 'Data extraction', 'Performance tuning', 'Data analysis', 'SAP', 'spark', 'Data structures', 'big data', 'Monitoring', 'SQL', 'Data architecture', 'Python', 'Data Quality', 'data analysis', 'Data Management', 'Data Modeling', 'Data Governance']
option1 = st.selectbox('Select Job Title', l)
if st.button('Search'):
    st.write("Skills required for ",option1," are:")
    #Print List of skills in table format
    st.table(pd.DataFrame(l))

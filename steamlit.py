import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Title of Streamlit App")
# Load the dataset
#df1 = pd.read_excel("1.Manufac Estimation.xlsx", sheet_name="manufac_to_csv")
df1 = pd.read_csv("data.csv")
#df1["EYM_YearMonth"] = pd.to_numeric(df1["EYM_YearMonth"])
df1["EYM_YearMonth"] = df1['EYM_YearMonth'].astype("category")
df1["EYM_YearMonth"] = df1['EYM_YearMonth'].apply(lambda x:str(x)+" YM")
print(df1.dtypes)# Title of the app

# Dropdown for selecting the EMC Column Name
emc_column_name = st.selectbox(
    'Select EMC Column Name:',
    options=df1['EMC_Column_Name'].unique(),
    index=df1['EMC_Column_Name'].unique().tolist().index('Direct_Labor')
)

# Filter the dataframe based on the selected EMC Column Name
dff = df1[df1['EMC_Column_Name'] == emc_column_name].copy()

# Create the Plotly line plot
fig = px.line(dff, x='EYM_YearMonth', y='ME_Value', title=f'ME_Value of {emc_column_name} per YM')

# Display the figure
print(dff.dtypes)
st.plotly_chart(fig)

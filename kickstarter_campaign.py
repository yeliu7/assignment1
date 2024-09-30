# kickstarter_campaign.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title of the app
st.title('kickstarter campaign overview')

# Load some data
df = pd.read_csv("https://raw.githubusercontent.com/yeliu7/assignment1/main/kickstarter_2016.csv")

# Show the dataset
st.write(df)

# =================Qeustion 3=====================

fig, ax = plt.subplots(figsize=(6.4, 2.4))
# Count the number of campaigns by state
campaign_counts = df['State'].value_counts()

# Create a bar plot
campaign_counts.plot(kind='bar', ax=ax)

# Add title and labels
ax.set_title('Number of Campaigns by State')
ax.set_xlabel('Campaign State')
ax.set_ylabel('Number of Campaigns')

# Show the plot
st.pyplot(fig)

# =================Qeustion 4.1======================

# Count the top 3 number of successful campaign by category
successful_categories = df[df['State'] == 'Successful']['Category'].value_counts().head(3)
# Count the top 3 number of unsuccessful campaign by category
unsuccessful_categories = df[df['State'] != 'Successful']['Category'].value_counts().head(3)

# Create a bar plot. Green bar shows the successful campaign, while red shows the unsuccessful
# alpha sets some transparency of the bar where there is overlap between successful/unsuccessful
fig, ax = plt.subplots(figsize=(6.4, 2.4))
successful_categories.plot(kind='bar', ax=ax, color='green', label='Successful')
unsuccessful_categories.plot(kind='bar', ax=ax, color='red', label='Unsuccessful', alpha=0.7)

# Add title and labels
ax.set_title('Top 3 Categories for Successful and Unsuccessful Campaigns')
ax.set_xlabel('Category')
ax.set_ylabel('Number of Campaigns')
ax.legend()

# Show the plot
st.pyplot(fig)

# =================Question 4.2=======================

# Count the top 3 number of successful campaign by category
successful_categories = df[df['State'] == 'Successful']['Category'].value_counts().head(3)
# Count the top 3 number of unsuccessful campaign by category
unsuccessful_categories = df[df['State'] != 'Successful']['Category'].value_counts().head(3)

# Combine the two Series (successful and unsuccessful) into a DataFrame
df_combined = pd.DataFrame({
    'Successful': successful_categories,
    'Unsuccessful': unsuccessful_categories
})

# Create a bar plot of the DataFrame with side-by-side bars
fig, ax = plt.subplots(figsize=(6.4, 2.4))
df_combined.plot(kind='bar', ax=ax, color=['green', 'red'], width=0.8)

# Add title and labels
ax.set_xlabel('Category')
ax.set_ylabel('Number of Campaigns')
ax.set_title('Top 3 Categories for Successful and Unsuccessful Campaigns')

# Rotate the x-axis labels for better readability
plt.xticks(rotation=45)

# Add legend
plt.legend()

# Display the plot using Streamlit
st.pyplot(fig)

# ==================Question 5==========================
import numpy as np

# filter Goal amount to avoid log transformation error
df_filtered = df[df['Goal'] > 0]

# Apply log base 10 to the 'Goal' column
df_filtered['Log_Goal'] = np.log10(df_filtered['Goal'])

# Create the histogram plot
fig, ax = plt.subplots(figsize=(6.4, 2.4))
ax.hist(df_filtered['Log_Goal'], bins=30, edgecolor='black')

# Add title and labels
ax.set_xlabel('Log10(Goal Amount)')
ax.set_ylabel('Number of Campaigns')
ax.set_title('Distribution of Campaigns by Goal Amount (on scale of Log10)')

# Adjust layout
plt.tight_layout()

# Display the plot in Streamlit
st.pyplot(fig)

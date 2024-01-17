import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import Tk, Frame, Label, Button, ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load the dataset
df = pd.read_csv("Financial Analytics data.csv", encoding='unicode_escape')

# Drop unnamed columns with all NaN values
df_cleaned = df.dropna(axis=1, how='all')

# Convert to numeric
df_cleaned['Mar Cap - Crore'] = pd.to_numeric(df_cleaned['Mar Cap - Crore'], errors='coerce')
df_cleaned['Sales Qtr - Crore'] = pd.to_numeric(df_cleaned['Sales Qtr - Crore'], errors='coerce')

# Create the main window
root = Tk()
root.title("Financial Analytics Dashboard")

# Define functions for different visualizations
def plot_histogram(column, color, title, xlabel, ylabel):
    plt.figure(figsize=(10, 6))
    sns.histplot(df_cleaned[column], bins=30, kde=True, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def plot_bar_chart(x, y, color, title, xlabel, ylabel):
    plt.figure(figsize=(12, 6))
    sns.barplot(x=x, y=y, data=df_cleaned.nlargest(10, 'Mar Cap - Crore'), palette=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Create tabs
tab_parent = ttk.Notebook(root)

# Tab 1
tab1 = ttk.Frame(tab_parent)
tab_parent.add(tab1, text="Mar Cap Histogram")
Button(tab1, text="Plot", command=lambda: plot_histogram('Mar Cap - Crore', 'blue', 'Distribution of Mar Cap - Crore', 'Mar Cap - Crore', 'Frequency')).pack()

# Tab 2
tab2 = ttk.Frame(tab_parent)
tab_parent.add(tab2, text="Sales Histogram")
Button(tab2, text="Plot", command=lambda: plot_histogram('Sales Qtr - Crore', 'green', 'Distribution of Quarterly Sales', 'Sales (Crore)', 'Frequency')).pack()

# Tab 3
tab3 = ttk.Frame(tab_parent)
tab_parent.add(tab3, text="Top N Companies Bar Chart")
Button(tab3, text="Plot", command=lambda: plot_bar_chart('Mar Cap - Crore', 'Name', 'viridis', 'Top 10 Companies by Market Capitalization', 'Market Capitalization (Crore)', 'Company Name')).pack()

# Tab 4
tab4 = ttk.Frame(tab_parent)
tab_parent.add(tab4, text="Correlation Heatmap")
Button(tab4, text="Plot", command=lambda: sns.heatmap(df_cleaned[['Mar Cap - Crore', 'Sales Qtr - Crore']].corr(), annot=True, cmap='coolwarm', linewidths=.5)).pack()

tab_parent.pack(expand=1, fill="both")

# Run the main loop
root.mainloop()

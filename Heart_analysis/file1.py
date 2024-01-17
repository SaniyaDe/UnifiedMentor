import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file_path="Heart Disease data/Heart Disease data.csv"
df=pd.read_csv(file_path)

# print(df)
print(df.describe())

# #vizualising the distribution of target variable
sns.countplot(x='target',data=df)
plt.title("distribution of target variable")
plt.show()

#explore distribution of numerical features
column_names=df.columns.tolist()
print(column_names)

numerical_columns=df.select_dtypes(include=['int64','float64']).columns.tolist()
print(numerical_columns)

num_features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']
df[num_features].hist(bins=20, figsize=(15, 10))
plt.suptitle('Distribution of Numerical Features')
plt.show()


# Scatterplots for individual features against the target
num_features = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak']

for feature in num_features:
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x=feature, y='target', data=df, hue='target', marker='o', s=50)
    plt.title(f'Scatterplot of {feature} against Target')
    plt.show()

# Using box plots for categorical features
cat_features = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal']
for feature in cat_features:
    sns.countplot(x=feature, hue='target', data=df)
    plt.title(f'Distribution of {feature} colored by Target')
    plt.show()

# Correlation heatmap
correlation_matrix = df.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
import numpy
import pandas
import matplotlib.pyplot as plt
import sklearn
import nltk

df_attributes = pandas.read_csv('DATA/attributes.csv')
df_products = pandas.read_csv('DATA/product_descriptions.csv')
df_train = pandas.read_csv('DATA/train.csv', encoding='latin1')
df_test = pandas.read_csv('DATA/test.csv', encoding='latin1')

# print(df_train.info())
# print(df_train.shape)
# print(len(df_train['product_title'].unique()))
# print(df_train['product_title'].value_counts().head(10))
# print(df_train['relevance'].mean(), df_train['relevance'].median(), df_train['relevance'].std())

# plt.hist(df_train['relevance'], bins=50, color='blue', alpha=0.7)
# plt.title('Histogram of Relevance Values')
# plt.xlabel('Relevance')
# plt.ylabel('Frequency')
# plt.show()

# print(df_attributes['product_uid'].value_counts().head(5))

filtered_df = df_attributes[df_attributes["name"].str.contains('Brand Name', na=False)]
print(filtered_df["value"].unique())
print(filtered_df["value"].value_counts().head(10))
import pandas as pd
import matplotlib.pyplot as plt
import zipfile
import os

dataset_path = r"C:\Users\kakil\OneDrive\Desktop\prodigy\API_SP.POP.TOTL_DS2_en_csv_v2_1360681.zip"

with zipfile.ZipFile(dataset_path, 'r') as zip_ref:

    zip_ref.extract('API_SP.POP.TOTL_DS2_en_csv_v2_1360681.csv', "C:\\Users\\kakil\\OneDrive\\Desktop\\prodigy\\task1\\unzip")

extracted_csv_path = "C:\\Users\\kakil\\OneDrive\\Desktop\\prodigy\\task1\\unzip\\API_SP.POP.TOTL_DS2_en_csv_v2_1360681.csv"

df = pd.read_csv(extracted_csv_path, skiprows=4)  

print(df.head())

years = df.columns[4:-1]  

country_data = df[df['Country Name'] == 'World']


population_data = country_data[years].transpose()
population_data.columns = ['Population']
population_data.index.name = 'Year'
population_data.reset_index(inplace=True)


population_data['Year'] = population_data['Year'].astype(int)


plt.figure(figsize=(12, 6))
plt.bar(population_data['Year'], population_data['Population'], color='skyblue')
plt.xlabel('Year')
plt.ylabel('Population')
plt.title('World Population Distribution Over Years')
plt.xticks(rotation=45)
plt.tight_layout()

plt.show()

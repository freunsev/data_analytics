import pandas as pd;

df = pd.read_csv('Week_02/GK/BigmacPrice.csv');
cd = pd.read_excel('Week_02/GK/ChickenData.xlsx');

print(cd.to_string());

# Create a dictionary from the DataFrame
breed_eggs_dict = cd.set_index('breed')['eggs_per_year'].to_dict()

# Print the resulting dictionary
print(breed_eggs_dict)


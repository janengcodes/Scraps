import pandas as pd


recipeDetails = pd.read_csv('01_Recipe_Details.csv')
ingredients = pd.read_csv('02_Ingredients.csv')
Compound = pd.read_csv('03_Compound_Ingredients.csv')
ingredientAliases = pd.read_csv('04_Recipe-Ingredients_Aliases.csv')



# sort the data into categories with recipeDetails
# meat produce dairy grain
# print out the categories

meat = ingredients['Meat', 'Fish', 'Seafood']
dairy = ingredients['Dairy']
produce = ingredients['Fruit', 'Herb', 'Vegetable', 'Fungus']
grain = ingredients['Cereal', 'Legume']

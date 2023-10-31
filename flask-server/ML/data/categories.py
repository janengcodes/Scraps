import pandas as pd


recipeDetails = pd.read_csv('01_Recipe_Details.csv')
ingredients = pd.read_csv('02_Ingredients.csv')
Compound = pd.read_csv('03_Compound_Ingredients.csv')
ingredientAliases = pd.read_csv('04_Recipe-Ingredients_Aliases.csv')
# O4 contains ingredients measurements for recipes


# sort the data into categories with recipeDetails
# meat produce dairy grain
# print out the categories
# Assuming your index columns are named 'Category' and 'Subcategory', you can access data like this:

# # Then, you can access specific columns in the resulting Series if needed:
# column_name = 'YourColumnName'
# specific_value = meat_fish_seafood_data[column_name]
meat = ingredients[(ingredients['Category'] == 'Meat') |
                   (ingredients['Category'] == 'Fish') |
                   (ingredients['Category'] == 'Seafood')]
# print("Meat", meat)


dairy = ingredients[(ingredients['Category'] == 'Dairy')]
# print("Dairy",  dairy)

produce = ingredients[(ingredients['Category'] == 'Fruit') |
                      (ingredients['Category'] == 'Vegetable') |
                      (ingredients['Category'] == 'Herb') |
                      (ingredients['Category'] == 'Fungus')]
print("Produce", produce)

grain = ingredients[((ingredients['Category'] == 'Cereal') |
                     (ingredients['Category'] == 'Legume'))]
# print("Grain", grain)

print("size", len(meat) + len(dairy) + len(produce) + len(grain))

allIngred = ingredientAliases['Original Ingredient Name']
# count the unique ingredients 
unique_ingred = set(allIngred)

unique_ingred_count = len(unique_ingred)

print("unique", unique_ingred_count)

# cross reference with the ingredients in each category





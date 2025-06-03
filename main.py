import parser
import create_docs

# create list of Recipes
recipes = parser.recipe_list()

for item in recipes:
    create_docs.docx_template(item)
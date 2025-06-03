import docx
from docx.shared import Inches

def docx_template(recipe):

    # Create document
    doc = docx.Document()

    # Add heading
    doc.add_heading(f'{recipe.title_info['title']}', 0)

    # add yield
    doc.add_heading(f'Yield: {recipe.title_info['yield']}', 4)

    # add Ingredients heading
    doc.add_heading('INGREDIENTS', 3)

    # add ingredient list
    for item in recipe.ingred:
        p = doc.add_paragraph(f'   - {item}')
        p.paragraph_format.space_after = Inches(0.1)
    
    # add Preparation heading
    doc.add_heading('PREPARATION', 3)

    # add prep steps list
    index = 1
    for item in recipe.steps:
        p = doc.add_paragraph(f'{index}. {item}')
        p.paragraph_format.space_after = Inches(0.1)
    
    doc.save(f'./docs/{recipe.title_info['list_name']}.docx')




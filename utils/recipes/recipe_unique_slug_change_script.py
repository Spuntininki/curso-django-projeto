from recipes.models import Recipe

recipes = Recipe.objects.all()

for recipe in recipes:
    splited_title = recipe.title.split()
    index = len(splited_title)
    new_slug = ''
    for c in range(0, index):
        if c >= 1:
            new_slug += f'-{splited_title[c]}'
        else:
            new_slug += splited_title[c]
    recipe.slug = new_slug
    recipe.save()

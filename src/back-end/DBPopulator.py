import json
import psycopg2
import DBAccess as DBA

def populate_db():
    # Connect to the database
    conn = DBA.connect_to_db()
    cursor = conn.cursor()

    # Read the JSON file
    with open('../../data/recipes.json', 'r') as file:
        recipes = json.load(file)

    # Assuming the file contains a list of recipes
    for recipe in recipes:
        # Insert the recipe into the recipes table
        recipe_query = """
        INSERT INTO public.recipes (hf_id, image_link, name, skill)
        VALUES (%s, %s, %s, %s) RETURNING id;
        """
        cursor.execute(recipe_query, (recipe['id'], recipe['imageLink'], recipe['name'], recipe['difficulty']))
        recipe_id = cursor.fetchone()[0]

        # Insert ingredients and their relationship with recipes
        for ingredient in recipe['ingredients']:
            ingredient_query = """
            INSERT INTO public.ingredients (hf_id, name)
            VALUES (%s, %s) ON CONFLICT (hf_id) DO NOTHING RETURNING id;
            """
            cursor.execute(ingredient_query, (ingredient['id'], ingredient['name']))
            ingredient_id = cursor.fetchone()[0]

            recipe_ingredients_query = """
            INSERT INTO public.recipe_ingredients (recipe_id, ingredient_id, amount, unit)
            VALUES (%s, %s, %s, %s);
            """
            cursor.execute(recipe_ingredients_query, (recipe_id, ingredient_id, ingredient['amount'], ingredient['unit']))

        # Commit the transaction
        conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()

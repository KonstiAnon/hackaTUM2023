import json
import psycopg2
import DBAccess as DBA


def make_list_unique(json_list, key):
    unique_ids = set()
    unique_json_list = []

    for item in json_list:
        # Check if the key is already in the set
        if item[key] not in unique_ids:
            # Add the key to the set to mark it as seen
            unique_ids.add(item[key])
            # Add the JSON object to the unique list
            unique_json_list.append(item)

    return unique_json_list


def flatten_list(nested_list):
    return [item for sublist in nested_list for item in
            (flatten_list(sublist) if isinstance(sublist, list) else [sublist])]


def populate_db():
    # Connect to the database
    conn = DBA.connect_to_db()
    cursor = conn.cursor()

    # Read the JSON file
    with open('../../data/recipes.json', 'r') as file:
        recipes = json.load(file)

    allergens = make_list_unique(flatten_list([r['allergens'] for r in recipes]), 'id')
    for allergen in allergens:
        recipe_query = """
                INSERT INTO public.allergies (hf_id, name)
                VALUES (%s, %s);
                """
        cursor.execute(recipe_query, (allergen['id'], allergen['name']))
    conn.commit()
    allg_id_2_hf_id = dict(DBA.fetch_data(conn, """
        SELECT a.id, a.hf_id
        FROM public.allergies a
    """))
    ingredients = make_list_unique(flatten_list([r['ingredients'] for r in recipes]), 'id')
    for ing in ingredients:
        recipe_query = """
                INSERT INTO public.allergy_ingredients (hf_id, image_link, name, skill)
                VALUES (%s, %s, %s, %s) RETURNING id;
                """
        cursor.execute(recipe_query, (recipe['id'], recipe['imageLink'], recipe['name'], recipe['difficulty']))
        recipe_id = cursor.fetchone()[0]
    ingredients = [item for item in ingredients if item.get("allergens") != []]
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
            VALUES (%s, %s) RETURNING id;
            """
            cursor.execute(ingredient_query, (ingredient['id'], ingredient['name']))
            ingredient_id = cursor.fetchone()[0]

            recipe_ingredients_query = """
            INSERT INTO public.recipe_ingredients (recipe_id, ingredient_id, amount, unit)
            VALUES (%s, %s, %s, %s);
            """
            cursor.execute(recipe_ingredients_query,
                           (recipe_id, ingredient_id, ingredient.get('amount', 1), ingredient.get('unit', ' ')))

        # Commit the transaction
        conn.commit()

    # Close the database connection
    cursor.close()
    conn.close()


if __name__ == '__main__':
    populate_db()
    print("foo")

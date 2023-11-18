import psycopg2

import DBAccess as DBA


def get_recipes_for_user(conn, user_id):
    try:
        user_liked_tags_query = f"SELECT tag_id FROM public.likedtags WHERE user_id = {user_id};"
        user_liked_tags = DBA.fetch_data(conn, user_liked_tags_query)

        # Fetch recipes based on user's allergies and liked tags
        recipe_query = f"""
                SELECT DISTINCT r.id, r.image_link, r.name, r.skill
                FROM public.recipes r
                WHERE NOT exists(
                    SELECT *
                    FROM public.user_allergies ua
                    JOIN public.allergy_ingredients ai on ai.allergy_id = ua.allergy_id
                    JOIN public.recipe_ingredients ri on ri.ingredient_id = ai.ingredient_id
                    WHERE ua.user_id = {user_id} and r.id = ri.recipe_id
                )
                {"AND exists(select * FROM public.tags t JOIN public.recipe_tags rt on rt.tag_id = t.id WHERE t.name = 'Vegan' and rt.recipe_id = r.id)" if ('Vegan',) in user_liked_tags else ""}
                ORDER BY r.id;
            """
        recipes = DBA.fetch_data(conn, recipe_query)
        return recipes

    except psycopg2.Error as e:
        print("Error fetching recipes:", e)
    return None

if __name__ == '__main__':
    conn = DBA.connect_to_db()
    get_recipes_for_user(conn, 2)

import psycopg2

import DBAccess as DBA


def get_recipes_for_user(conn, user_id):
    try:
        # Fetch the user's allergies
        user_allergies_query = f"SELECT allergy_id FROM public.user_allergies WHERE user_id = {user_id};"
        user_allergies = DBA.fetch_data(conn, user_allergies_query)

        # Fetch user's liked tags
        user_liked_tags_query = f"SELECT tag_id FROM public.likedtags WHERE user_id = {user_id};"
        user_liked_tags = DBA.fetch_data(conn, user_liked_tags_query)

        # Fetch recipes based on user's allergies and liked tags
        recipe_query = f"""
                SELECT DISTINCT r.id, r.image_link, r.name, r.skill
                FROM public.recipes r
                JOIN public.recipe_ingredients ri ON r.id = ri.recipe_id
                JOIN public.recipe_tags rt ON r.id = rt.recipe_id
                WHERE NOT EXISTS (
                    SELECT 1
                    FROM public.user_allergies ua
                    WHERE ua.user_id = {user_id}
                    AND ua.allergy_id = ANY(ARRAY(SELECT ingredient_id FROM public.recipe_ingredients WHERE recipe_id = r.id))
                )
                AND (rt.tag_id = ANY(ARRAY(SELECT tag_id FROM public.likedtags WHERE user_id = {user_id})) OR rt.tag_id IS NULL)
                {"AND rt.tag_id = 'Vegan'" if ('Vegan',) in user_liked_tags else ""}
                ;
            """
        recipes = DBA.fetch_data(conn, recipe_query)
        return recipes

    except psycopg2.Error as e:
        print("Error fetching recipes:", e)
    return None

def set_allergies_for_user(user_id, allergies):
    conn = DBA.connect_to_db()
    try:
        # Delete user's allergies
        delete_query = f"DELETE FROM public.user_allergies WHERE user_id = {user_id};"
        DBA.execute_query(conn, delete_query)

        # Insert new allergies
        insert_query = f"INSERT INTO public.user_allergies (user_id, allergy_id) VALUES "
        for i, allergy in enumerate(allergies):
            insert_query += f"({user_id}, {allergy})"
            if i < len(allergies) - 1:
                insert_query += ", "
        insert_query += ";"
        DBA.execute_query(conn, insert_query)

    except psycopg2.Error as e:
        print("Error setting allergies:", e)
        return False
    finally:
        DBA.close_connection(conn)
    return True

if __name__ == '__main__':
    conn = DBA.connect_to_db()
    get_recipes_for_user(conn, 2)

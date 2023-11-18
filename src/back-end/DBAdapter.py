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


def set_allergies_for_user(conn, user_id, allergies):
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
    return True


def insert_user(conn, name, pw):
    try:
        query = f"INSERT INTO public.users (name, pw) VALUES ('{name}', '{pw}')"
        DBA.execute_query(conn, query)
        print(f"User '{name}' inserted successfully")
    except Exception as error:
        print(f"Error inserting user: {error}")


def load_all_users(conn):
    try:
        query = "SELECT * FROM public.users"
        users = DBA.fetch_data(conn, query)
        return users
    except Exception as error:
        print(f"Error loading users: {error}")
        return None


def get_user_id(conn, name, pw):
    try:
        query = f"SELECT id FROM public.users WHERE name = '{name}' AND pw = '{pw}'"
        result = DBA.fetch_data(conn, query)
        if result:
            return result[0][0]  # Assuming the first column is the user ID
        else:
            print(f"No user found with name '{name}' and password '{pw}'")
            return None
    except Exception as error:
        print(f"Error getting user ID: {error}")
        return None


def user_add_like(conn, user_id, recipe_id):
    try:
        query = f"INSERT INTO public.liked_recipes (user_id, recipe_id) VALUES ({user_id}, {recipe_id})"
        DBA.execute_query(conn, query)
        print(f"User '{user_id}' liked recipe '{recipe_id}'")
    except Exception as error:
        print(f"Error inserting like: {error}")


def get_tags(conn):
    try:
        query = f"SELECT t.id, t.name FROM public.tags t"
        data = DBA.fetch_data(conn, query)
        return data
    except Exception as error:
        print(f"Error inserting like: {error}")
        return None


def user_add_tag(conn, user_id, tag_id):
    try:
        query = f"INSERT INTO public.user_tags (user_id, tag_id) VALUES ({user_id}, {tag_id})"
        DBA.execute_query(conn, query)
        print(f"User '{user_id}' liked recipe '{tag_id}'")
    except Exception as error:
        print(f"Error inserting like: {error}")


if __name__ == '__main__':
    conn = DBA.connect_to_db()
    get_recipes_for_user(conn, 2)

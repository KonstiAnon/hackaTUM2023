import psycopg2


def connect_to_db():
    try:
        # Modify these parameters according to your PostgreSQL setup
        conn = psycopg2.connect(
            user="postgres",
            password="hellofresh",
            host="localhost",
            port="5432",
            database="hellofresh"
        )
        return conn
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)
        return None


def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except (Exception, psycopg2.Error) as error:
        print("Error executing query:", error)
    finally:
        if cursor:
            cursor.close()


def fetch_data(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        rec = cursor.fetchall()
        return rec
    except (Exception, psycopg2.Error) as error:
        print("Error fetching data:", error)
        return None
    finally:
        if cursor:
            cursor.close()


def close_connection(conn):
    if conn:
        conn.close()
        print("PostgreSQL connection is closed")


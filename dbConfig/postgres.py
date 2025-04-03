import psycopg2

def connect_to_db():
    """Intenta conectarse a PostgreSQL usando valores fijos."""
    try:
    
        dbname = "test_db"
        user = "postgres"
        password = "1234"
        host = "localhost"
        port = "5432"


        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        print("✅ Conexión exitosa a PostgreSQL")
        return conn

    except Exception as e:
        print(f"❌ Error de conexión: {e}")
        return None
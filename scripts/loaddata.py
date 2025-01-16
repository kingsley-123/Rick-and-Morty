import psycopg2 #type: ignore
from psycopg2.extras import execute_batch #type: ignore
from fetchdata import fetch_location_data, fetch_character_data, fetch_episode_data

# PostgreSQL Connection Parameters
host = "data-postgres"
port = "5432"
dbname = "datahub"
user = "airflow"
password = "airflow"

# Function to load episode data
def load_episode_data():
    """Load episode data into the PostgreSQL database."""
    # Establish database connection
    conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
    cursor = conn.cursor()

    # Fetch episode data
    episode_df = fetch_episode_data()
    episode_data = [
        (row['id'], row['name'], row['air_date'], row['no_of_character'], row['created_at'])
        for _, row in episode_df.iterrows()
    ]

    # Insert query with conflict handling
    query = """
        INSERT INTO rickmorty.episode (id, name, air_date, no_of_character, created_at)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (id) DO UPDATE SET
            name = EXCLUDED.name,
            air_date = EXCLUDED.air_date,
            no_of_character = EXCLUDED.no_of_character,
            created_at = EXCLUDED.created_at;
    """

    # Execute batch insert
    execute_batch(cursor, query, episode_data)
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

# Function to load location data
def load_location_data():
    conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
    cursor = conn.cursor()

    # Fetch the location data
    location_df = fetch_location_data()

    # Prepare location data for insertion
    location_data = [
        (row['id'], row['name'], row['type'], row['dimension'], row['created_at'])
        for _, row in location_df.iterrows()
    ]

    # SQL query for insertion
    query = """
        INSERT INTO rickmorty.location (id, name, type, dimension, created_at)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (id) DO UPDATE SET
            name = EXCLUDED.name,
            type = EXCLUDED.type,
            dimension = EXCLUDED.dimension,
            created_at = EXCLUDED.created_at;
    """

    # Execute batch insert for location data
    execute_batch(cursor, query, location_data)
    conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()


# Function to load character data
def load_character_data():
    conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=password)
    cursor = conn.cursor()

    # Fetch the character data
    character_df = fetch_character_data()

    # Fetch existing locations to map names to IDs
    cursor.execute("SELECT id, name FROM rickmorty.location")
    location_mapping = {row[1]: row[0] for row in cursor.fetchall()}  # Map location names to IDs

    # Fetch existing episodes to map names to IDs
    cursor.execute("SELECT id, name FROM rickmorty.episode")
    episode_mapping = {row[1]: row[0] for row in cursor.fetchall()}  # Map episode names to IDs

    # Transform character data
    character_data = []
    for _, row in character_df.iterrows():
        location_id = location_mapping.get(row['location'], None)  # Map location name to ID
        episode_id = episode_mapping.get(row['episode'], None)  # Map episode name to ID
        character_data.append((
            row['id'], row['name'], row['status'], row['species'], row['type'],
            row['gender'], row['origin'], location_id, row['image'], episode_id,
            row['no_of_episode'], row['created_at']
        ))

    # SQL query for insertion
    query = """
        INSERT INTO rickmorty.character (
            id, name, status, species, type, gender, origin, location, image, episode, no_of_episode, created_at
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO UPDATE SET
            status = EXCLUDED.status,
            species = EXCLUDED.species,
            type = EXCLUDED.type,
            gender = EXCLUDED.gender,
            origin = EXCLUDED.origin,
            location = EXCLUDED.location,
            image = EXCLUDED.image,
            episode = EXCLUDED.episode,
            no_of_episode = EXCLUDED.no_of_episode,
            created_at = EXCLUDED.created_at;
    """

    execute_batch(cursor, query, character_data)
    conn.commit()
    cursor.close()
    conn.close()


# Call the functions to load data
load_episode_data()
load_location_data()
load_character_data()


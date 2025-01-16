import requests #type: ignore
import pandas as pd #type: ignore

def fetch_episode_data():
    """Fetch episode data from the Rick and Morty API and return it as a Pandas DataFrame."""
    base_url = "https://rickandmortyapi.com/api/episode"
    data = requests.get(base_url).json()
    
    episode_list = []
    total_pages = data["info"]["pages"]

    for page_num in range(1, total_pages + 1):
        page_url = f"{base_url}?page={page_num}"
        episode = requests.get(page_url).json()
        
        for epi in episode["results"]:
            episode_list.append({
                "id": epi["id"],
                "name": epi["name"],
                "air_date": pd.to_datetime(epi["air_date"], format="%B %d, %Y").strftime("%Y-%m-%d"),
                "no_of_character": len(epi["characters"]),
                "created_at": pd.to_datetime(epi["created"]).date()
            })

    episode_df = pd.DataFrame(episode_list)
    return episode_df

def fetch_location_data():
    """Fetch location data from the Rick and Morty API and return it as a Pandas DataFrame."""
    base_url = "https://rickandmortyapi.com/api/location"
    response = requests.get(base_url)
    data = response.json()

    location_list = []
    total_pages = data["info"]["pages"]

    for page_num in range(1, total_pages + 1):
        page_url = f"{base_url}?page={page_num}"
        response = requests.get(page_url)
        locations = response.json()

        for loc in locations["results"]:
            location_list.append({
                "id": loc["id"],
                "name": loc["name"],
                "type": loc["type"],
                "dimension": loc["dimension"],
                "created_at": pd.to_datetime(loc["created"]).date()
            })

    location_df = pd.DataFrame(location_list)
    return location_df

def fetch_character_data():
    character_list = []

    # Fetch first page to get total number of pages
    first_page_response = "https://rickandmortyapi.com/api/character?page=1"
    response = requests.get(first_page_response)
    data = response.json()
    total_pages = data["info"]["pages"]

    # Loop through pages and gather character data
    for page_num in range(1, total_pages + 1):
        page_response = f"https://rickandmortyapi.com/api/character?page={page_num}"
        response = requests.get(page_response)
        data = response.json()

        for character in data["results"]:
            # Extracting episode names
            episode_names = []
            for episode_url in character["episode"]:
                episode_response = requests.get(episode_url)
                episode_data = episode_response.json()
                episode_names.append(episode_data["name"])  # Collect the episode name

            # For each episode, repeat the character's data
            for episode_name in episode_names:
                character_dic = {
                    "id": character["id"],
                    "name": character["name"],
                    "status": character["status"],
                    "species": character["species"],
                    "type": character["type"],
                    "gender": character["gender"],
                    "origin": character["origin"]["name"].replace("(", "").replace(")", ""),
                    "location": character["location"]["name"].replace("(", "").replace(")", ""),
                    "image": character["image"],
                    "episode": episode_name,  # Add episode name for the current row
                    "no_of_episode": 1,  # Set to 1 since this row corresponds to a single episode
                    "created_at": pd.to_datetime(character["created"], errors="coerce").date() if character["created"] else None
                }
                character_list.append(character_dic)

    # Return the DataFrame
    character_df = pd.DataFrame(character_list)
    return character_df


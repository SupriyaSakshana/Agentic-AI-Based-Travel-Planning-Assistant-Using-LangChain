import json

def recommend_places(query):

    with open("data/places.json", "r") as file:
        places = json.load(file)

    query = query.lower()

    matched_places = []

    # Mapping interests → place types
    interest_mapping = {
        "beaches": "beach",
        "historical places": "fort",
        "shopping": "market",
        "nature": "park",
        "food": "market",
        "adventure": "park",
        "water sports": "beach",
        "nightlife": "market"
    }

    for place in places:

        place_type = place["type"].lower()

        # Check if interest matches place type
        for interest, mapped_type in interest_mapping.items():

            if interest in query and mapped_type == place_type:

                matched_places.append(
                    f"{place['name']} "
                    f"({place['type']}) "
                    f"⭐ {place['rating']}"
                )

    # Top rated places
    matched_places = matched_places[:5]

    if matched_places:
        return "\n".join(matched_places)

    return "No matching places found."
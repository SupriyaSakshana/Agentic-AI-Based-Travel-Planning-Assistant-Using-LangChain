import json

def recommend_hotels(query):

    # -----------------------------------
    # HANDLE DICTIONARY INPUT
    # -----------------------------------

    if isinstance(query, dict):

        city = query.get("city", "")
        max_price = query.get("max_price", 10000)

    # -----------------------------------
    # HANDLE STRING INPUT
    # -----------------------------------

    elif isinstance(query, str):

        city = query
        max_price = 10000

    else:
        return "Invalid hotel input."


    # -----------------------------------
    # LOAD HOTEL DATA
    # -----------------------------------

    with open("data/hotels.json", "r") as file:

        hotels = json.load(file)


    # -----------------------------------
    # FILTER HOTELS
    # -----------------------------------

    results = []

    for hotel in hotels:

        if (
            hotel["city"].lower() == city.lower()
            and
            hotel["price"] <= max_price
        ):

            results.append(
                f"""
🏨 Hotel: {hotel['name']}

📍 City: {hotel['city']}
💰 Price: ₹{hotel['price']}
⭐ Rating: {hotel['rating']}
"""
            )


    # -----------------------------------
    # RETURN RESULTS
    # -----------------------------------

    if results:

        return "\n".join(results)

    return "No hotels found within budget."
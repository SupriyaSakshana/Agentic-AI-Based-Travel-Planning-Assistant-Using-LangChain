import json

def recommend_hotels(query):

    # -----------------------------------
    # HANDLE DICTIONARY INPUT
    # -----------------------------------

    if isinstance(query, dict):

        city = query.get("city", "").strip()

        # User can send any budget
        max_price = query.get("max_price")

        # If budget not provided
        if max_price is None:
            max_price = float("inf")

    # -----------------------------------
    # HANDLE STRING INPUT
    # Example: "Goa"
    # -----------------------------------

    elif isinstance(query, str):

        city = query.strip()

        # No budget limit
        max_price = float("inf")

    else:
        return "Invalid hotel input."


    # -----------------------------------
    # VALIDATION
    # -----------------------------------

    if not city:
        return "Please provide city name."


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

    return f"No hotels found in {city} within the given budget."
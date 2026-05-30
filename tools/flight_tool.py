import json

def search_flights(query):

    # -----------------------------------
    # HANDLE DICTIONARY INPUT
    # -----------------------------------

    if isinstance(query, dict):

        source = query.get("source_city", "")
        destination = query.get("destination_city", "")

        # Handle multiple possible keys
        date = query.get("travel_date", query.get("date", "Not Provided"))

        preference = query.get(
            "flight_preference",
            query.get("preference", "Cheapest")
        )

    # -----------------------------------
    # HANDLE STRING INPUT
    # Example: "Delhi to Goa"
    # -----------------------------------

    elif isinstance(query, str):

        parts = query.split("to")

        if len(parts) < 2:
            return "Please provide source and destination."

        source = parts[0].strip()
        destination = parts[1].strip()

        date = "Not Provided"
        preference = "Cheapest"

    else:
        return "Invalid flight input format."

    # -----------------------------------
    # VALIDATION
    # -----------------------------------

    if not source or not destination:
        return "Please provide source and destination."

    # -----------------------------------
    # LOAD FLIGHTS DATA
    # -----------------------------------

    with open("data/flights.json", "r") as file:
        flights = json.load(file)

    matched_flights = []

    # -----------------------------------
    # FIND MATCHING FLIGHTS
    # -----------------------------------

    for flight in flights:

        if (
            flight["from"].lower() == source.lower()
            and
            flight["to"].lower() == destination.lower()
        ):

            matched_flights.append(flight)

    # -----------------------------------
    # NO FLIGHTS FOUND
    # -----------------------------------

    if not matched_flights:
        return f"No flights found from {source} to {destination}."

    # -----------------------------------
    # SORT BY PRICE
    # -----------------------------------

    matched_flights = sorted(
        matched_flights,
        key=lambda x: x["price"]
    )

    # -----------------------------------
    # BUILD RESPONSE
    # -----------------------------------

    result = f"""
✈ Flights Found

Source: {source}
Destination: {destination}
Date: {date}
Preference: {preference}

"""

    for i, flight in enumerate(matched_flights[:5], start=1):

        result += f"""
{i}. {flight['airline']}
   Flight ID: {flight['flight_id']}
   Price: ₹{flight['price']}
   Departure: {flight['departure_time']}
   Arrival: {flight['arrival_time']}

"""

    return result
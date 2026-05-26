import json

def search_flights(query):

    # -----------------------------
    # HANDLE DICTIONARY INPUT
    # -----------------------------
    
    if isinstance(query, dict):

        source = query.get("source_city", "")
        destination = query.get("destination_city", "")
        date = query.get("travel_date", "")
        preference = query.get("flight_preference", "")

    # -----------------------------
    # HANDLE STRING INPUT
    # Example: "Delhi to Goa"
    # -----------------------------

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


    # -----------------------------
    # VALIDATION
    # -----------------------------

    if not source or not destination:
        return "Please provide source and destination."


    # -----------------------------
    # RETURN RESPONSE
    # -----------------------------

    return f"""
    ✈ Flights Found

    Source: {source}
    Destination: {destination}
    Date: {date}
    Preference: {preference}

    1. IndiGo - ₹4500
    2. Air India - ₹5200
    3. Vistara - ₹6100
    """
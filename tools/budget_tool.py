def calculate_budget(query):

    # Sample logic
    flight_cost = 5000
    hotel_cost = 6000
    food_cost = 2000
    transport_cost = 1500

    total = (
        flight_cost
        + hotel_cost
        + food_cost
        + transport_cost
    )

    return f"""
    Budget Breakdown:

    Flight Cost: ₹{flight_cost}
    Hotel Cost: ₹{hotel_cost}
    Food Cost: ₹{food_cost}
    Transport Cost: ₹{transport_cost}

    Total Estimated Budget: ₹{total}
    """
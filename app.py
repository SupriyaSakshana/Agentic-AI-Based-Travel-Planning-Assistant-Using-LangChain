import streamlit as st
from dotenv import load_dotenv
from agent import agent

# Load Environment Variables
load_dotenv()

# -----------------------------------
# PAGE CONFIG
# -----------------------------------

st.set_page_config(
    page_title="AI Travel Planner",
    page_icon="✈️",
    layout="wide"
)

# -----------------------------------
# CUSTOM CSS
# -----------------------------------

st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.stButton button {
    width: 100%;
    height: 3rem;
    font-size: 18px;
    border-radius: 10px;
}

.trip-card {
    padding: 20px;
    border-radius: 12px;
    background-color: #f7f7f7;
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------------
# HEADER
# -----------------------------------

st.title("✈️ Agentic AI Travel Planning Assistant")

st.markdown("""
Plan smart trips using AI-powered recommendations for:

✅ Flights  
✅ Hotels  
✅ Tourist Attractions  
✅ Weather Forecast  
✅ Budget Estimation  
✅ Day-wise Itinerary  
""")

# -----------------------------------
# SIDEBAR
# -----------------------------------

st.sidebar.header("⚙️ Travel Preferences")

budget = st.sidebar.slider(
    "💰 Total Budget (₹)",
    min_value=5000,
    max_value=200000,
    value=20000,
    step=1000
)

days = st.sidebar.slider(
    "📅 Trip Duration (Days)",
    min_value=1,
    max_value=15,
    value=3
)

hotel_type = st.sidebar.selectbox(
    "🏨 Hotel Preference",
    ["Budget", "Standard", "Luxury"]
)

flight_pref = st.sidebar.selectbox(
    "🛫 Flight Preference",
    ["Cheapest", "Fastest", "Business Class"]
)

travel_type = st.sidebar.selectbox(
    "👨‍👩‍👧 Travel Type",
    [
        "Solo",
        "Family",
        "Friends",
        "Couple",
        "Business"
    ]
)

# -----------------------------------
# MAIN FORM
# -----------------------------------

st.markdown("## 🌍 Enter Trip Details")

col1, col2 = st.columns(2)

with col1:
    source = st.text_input(
        "🛫 Source City",
        placeholder="Example: Delhi"
    )

with col2:
    destination = st.text_input(
        "📍 Destination City",
        placeholder="Example: Goa"
    )

travel_date = st.date_input("📅 Travel Date")

# -----------------------------------
# INTERESTS
# -----------------------------------

interests = st.multiselect(
    "🎯 Select Your Interests",
    [
        "Beaches",
        "Adventure",
        "Food",
        "Shopping",
        "Nature",
        "Nightlife",
        "Historical Places",
        "Water Sports",
        "Mountains",
        "Photography",
        "Temple Visits",
        "Wildlife",
        "Local Culture"
    ]
)

# -----------------------------------
# FOOD PREFERENCE
# -----------------------------------

food_pref = st.selectbox(
    "🍴 Food Preference",
    [
        "Veg",
        "Non-Veg",
        "Both"
    ]
)

# -----------------------------------
# TRANSPORT
# -----------------------------------

local_transport = st.selectbox(
    "🚕 Preferred Local Transport",
    [
        "Cab",
        "Bike Rental",
        "Public Transport",
        "Private Car"
    ]
)

# -----------------------------------
# SPECIAL REQUEST
# -----------------------------------

special_request = st.text_area(
    "📝 Additional Preferences",
    placeholder="""
Example:
- Honeymoon trip
- Family-friendly places
- Avoid crowded areas
- Include nightlife
- Low-budget trip
"""
)

# -----------------------------------
# GENERATE BUTTON
# -----------------------------------

if st.button("🚀 Generate AI Travel Plan"):

    # Validation
    if source == "" or destination == "":
        st.warning("⚠️ Please enter source and destination cities.")
    
    else:

        with st.spinner("Generating your personalized itinerary..."):

            query = f"""
            Create a complete {days}-day travel itinerary.

            USER DETAILS:
            - Source City: {source}
            - Destination City: {destination}
            - Budget: ₹{budget}
            - Travel Date: {travel_date}

            PREFERENCES:
            - Hotel Type: {hotel_type}
            - Flight Preference: {flight_pref}
            - Travel Type: {travel_type}
            - Interests: {', '.join(interests)}
            - Food Preference: {food_pref}
            - Local Transport: {local_transport}

            SPECIAL REQUEST:
            {special_request}

            IMPORTANT:
            Recommend places according to user interests.

            Generate:
            1. Best Flight Recommendation
            2. Hotel Recommendation
            3. Weather Forecast
            4. Best Tourist Places
            5. Day-wise Itinerary
            6. Food Suggestions
            7. Local Transport Suggestions
            8. Budget Breakdown
            9. Travel Tips
            10. Total Estimated Cost

            Make the output clean, structured, and user-friendly.
            """
            print("")
            result = agent.run(query)

        # -----------------------------------
        # OUTPUT SECTION
        # -----------------------------------

        st.success("✅ Trip Plan Generated Successfully!")

        st.markdown("## 🌴 Your Personalized Travel Itinerary")

        st.markdown(result)

        # -----------------------------------
        # DOWNLOAD BUTTON
        # -----------------------------------

        st.download_button(
            label="📥 Download Trip Plan",
            data=result,
            file_name="travel_itinerary.txt",
            mime="text/plain"
        )   
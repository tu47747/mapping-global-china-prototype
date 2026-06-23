import streamlit as st

st.set_page_config(
    page_title="Mapping Global China Prototype V0.2",
    layout="wide"
)

# -----------------------------
# Data
# -----------------------------

GLOBAL_ELEMENTS = [
    "Diplomacy", "Trade", "Investment", "Infrastructure",
    "Technology", "Education Exchange", "Sport", "Media", "Migration"
]

NATIONAL_ELEMENTS = [
    "Governance", "Economy", "Education", "Technology",
    "Culture", "Environment", "Sport", "Media", "Security"
]

PROVINCIAL_ELEMENTS = [
    "Local Governance", "Economic Development", "Industry", "Education",
    "Urbanisation", "Transport", "Tourism", "Public Health", "Sport"
]

CITY_ELEMENTS = [
    "Community", "Schools", "Universities", "Transport",
    "Housing", "Culture", "Sport", "Local Economy"
]

PROVINCES = [
    "Beijing", "Shanghai", "Guangdong", "Hubei",
    "Sichuan", "Yunnan", "Xinjiang", "Liaoning", "Zhejiang"
]

CITIES = [
    "Beijing", "Shanghai", "Wuhan", "Shenzhen",
    "Guangzhou", "Chengdu", "Kunming"
]

MAJOR_EVENTS = {
    1990: ["Reform and opening-up continues", "Market transition deepens"],
    2000: ["Pre-WTO transformation", "Urbanisation accelerates"],
    2005: ["Post-WTO global integration", "Manufacturing expansion"],
    2010: ["Post-Olympic development", "High-speed rail expansion"],
    2015: ["Belt and Road expansion", "Policy-driven industrial upgrading"],
    2020: ["COVID-19 pandemic", "Digital governance expansion"],
    2025: ["AI and digital economy expansion", "Green transition"],
    2030: ["Future projection", "Long-term development scenarios"]
}

# -----------------------------
# Style
# -----------------------------

st.markdown(
    """
    <style>
    .stApp {
        background: radial-gradient(circle at top, #1b2a4a 0%, #08111f 45%, #03060c 100%);
        color: #f3f6ff;
    }

    .title {
        text-align: center;
        font-size: 46px;
        font-weight: 700;
        margin-top: 20px;
        color: #f3f6ff;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #b8c7e6;
        margin-bottom: 30px;
    }

    .china-node {
        text-align: center;
        border: 2px solid rgba(220, 235, 255, 0.85);
        border-radius: 160px;
        width: 260px;
        height: 260px;
        margin: 25px auto;
        background: radial-gradient(circle, rgba(85,130,190,0.95), rgba(20,42,78,0.82));
        box-shadow: 0 0 45px rgba(130, 180, 255, 0.35);
        font-size: 36px;
        font-weight: 700;
        color: white;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .event-card {
        border-left: 3px solid #9bbcff;
        padding: 10px 14px;
        margin: 8px 0;
        background: rgba(255,255,255,0.06);
        border-radius: 8px;
    }

    div.stButton > button {
        color: #ffffff !important;
        background: rgba(40, 80, 140, 0.85) !important;
        border: 1px solid rgba(180, 210, 255, 0.7) !important;
        border-radius: 12px !important;
        font-weight: 600 !important;
    }

    div.stButton > button:hover {
        background: rgba(80, 130, 210, 0.95) !important;
        color: #ffffff !important;
        border: 1px solid #ffffff !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Welcome Page
# -----------------------------

if "entered" not in st.session_state:
    st.session_state.entered = False

if not st.session_state.entered:
    st.markdown('<div class="title">Welcome to Mapping Global China</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Mapping China through space, theme, connection, and time.</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.info(
            "This V0.2 prototype focuses on information architecture. "
            "The story layer is intentionally deferred."
        )

        if st.button("Enter Prototype", use_container_width=True):
            st.session_state.entered = True
            st.rerun()

    st.stop()

# -----------------------------
# Main Interface
# -----------------------------

st.markdown('<div class="title">Mapping Global China</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Space · Theme · Global Connection · Time Range</div>',
    unsafe_allow_html=True
)

top1, top2, top3 = st.columns([1, 1, 1])

with top1:
    portal = st.radio(
        "Entry Portal",
        ["User Portal", "Admin Portal"]
    )

with top2:
    spatial_layer = st.selectbox(
        "Spatial Layer",
        [
            "Global Layer",
            "National Layer",
            "Provincial Layer",
            "City Layer"
        ]
    )

with top3:
    year_range = st.slider(
        "Timeline Range",
        min_value=1990,
        max_value=2030,
        value=(2000, 2020),
        step=5
    )

start_year, end_year = year_range

left, centre, right = st.columns([1.2, 2.6, 1.2])

# -----------------------------
# Left Panel
# -----------------------------

with left:
    st.subheader("Thematic Elements")

    if spatial_layer == "Global Layer":
        current_elements = GLOBAL_ELEMENTS
    elif spatial_layer == "National Layer":
        current_elements = NATIONAL_ELEMENTS
    elif spatial_layer == "Provincial Layer":
        current_elements = PROVINCIAL_ELEMENTS
    else:
        current_elements = CITY_ELEMENTS

    selected_element = st.selectbox(
        "Select an element",
        current_elements
    )

    st.write(
        f"You are viewing **{selected_element}** within the selected spatial layer and time range."
    )

    st.caption(
        "Future version: each thematic element can contain sub-elements, actors, datasets, relationships, and narratives."
    )

# -----------------------------
# Centre Panel
# -----------------------------

with centre:
    if portal == "User Portal":

        if spatial_layer == "Global Layer":
            st.subheader("Global Connection Layer")

            st.markdown(
                '<div class="china-node">China</div>',
                unsafe_allow_html=True
            )

            st.write(
                "This layer maps China through its external relations, movements, and global connections. "
                "Other countries are treated as connected nodes, not as equal centres."
            )

            st.write("Connection pathways:")

            rows = [
                ["China → United Kingdom", "China → Sri Lanka"],
                ["China → Brazil", "China → Kenya"],
                ["China → Other Regions"]
            ]

            for row in rows:
                cols = st.columns(2)
                for col, item in zip(cols, row):
                    with col:
                        st.button(item, use_container_width=True)

        elif spatial_layer == "National Layer":
            st.subheader("National Hub")

            st.markdown(
                '<div class="china-node">China</div>',
                unsafe_allow_html=True
            )

            st.write("Click a thematic element to focus the national-level network:")

            rows = [
                ["Governance", "Economy", "Education"],
                ["Technology", "Culture", "Environment"],
                ["Sport", "Media", "Security"]
            ]

            for row in rows:
                cols = st.columns(3)
                for col, element in zip(cols, row):
                    with col:
                        if st.button(element, use_container_width=True):
                            st.success(f"Focused on China’s {element} network.")

        elif spatial_layer == "Provincial Layer":
            st.subheader("Provincial Layer")

            province = st.selectbox(
                "Select a province or municipality",
                PROVINCES
            )

            st.markdown(
                f'<div class="china-node">{province}</div>',
                unsafe_allow_html=True
            )

            st.write(
                "This layer shows how national-level themes are interpreted, implemented, or transformed at provincial level."
            )

        elif spatial_layer == "City Layer":
            st.subheader("City Layer")

            city = st.selectbox(
                "Select a city",
                CITIES
            )

            st.markdown(
                f'<div class="china-node">{city}</div>',
                unsafe_allow_html=True
            )

            st.write(
                "This layer is designed for city-level institutions, local networks, and future narrative case studies."
            )

    else:
        st.subheader("Admin Portal")

        st.write(
            "This is a placeholder administrative interface for future data entry and maintenance."
        )

        tab1, tab2, tab3 = st.tabs(
            ["Add Spatial Unit", "Add Thematic Element", "Add Event / Narrative"]
        )

        with tab1:
            st.text_input("Spatial unit name")
            st.selectbox(
                "Spatial level",
                ["Global Connection", "National", "Provincial", "City"]
            )
            st.text_input("Parent spatial unit")
            st.text_input("Latitude")
            st.text_input("Longitude")
            st.button("Save spatial unit")

        with tab2:
            st.text_input("Element name")
            st.selectbox(
                "Applicable layer",
                ["Global", "National", "Provincial", "City", "All"]
            )
            st.text_area("Description")
            st.button("Save thematic element")

        with tab3:
            st.text_input("Event title")
            st.number_input("Year", min_value=1990, max_value=2030, value=2020)
            st.text_area("Narrative text")
            st.button("Save event / narrative")

# -----------------------------
# Right Panel
# -----------------------------

with right:
    st.subheader("Historical Context")

    st.write(f"Selected timeline range: **{start_year}–{end_year}**")

    selected_events = {
        y: events
        for y, events in MAJOR_EVENTS.items()
        if start_year <= y <= end_year
    }

    if selected_events:
        for event_year, events in selected_events.items():
            st.write(f"**{event_year}**")

            for event in events:
                st.markdown(
                    f"""
                    <div class="event-card">
                        {event}
                    </div>
                    """,
                    unsafe_allow_html=True
                )
    else:
        st.info("No major events in this selected period.")

    st.caption(
        "Future version: major events can reshape the visibility, weight, and relationships of thematic elements."
    )

# -----------------------------
# Bottom Note
# -----------------------------

st.markdown("---")
st.write(
    "**V0.2 Information Architecture:** China remains the central hub; each spatial layer has its own thematic elements."
)
st.caption(
    "Story Layer is intentionally deferred. This version focuses on Space, Theme, Global Connection, and Time Range."
)
import streamlit as st

st.set_page_config(
    page_title="Mapping Global China Prototype V0.4",
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

GLOBAL_CONNECTIONS = [
    "United Kingdom", "Sri Lanka", "Brazil", "Kenya", "Other Regions"
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

    .story-card {
        border: 1px solid rgba(180, 210, 255, 0.45);
        border-radius: 16px;
        padding: 20px;
        margin: 15px 0;
        background: rgba(255,255,255,0.07);
        box-shadow: 0 0 25px rgba(80, 130, 210, 0.20);
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
# Session State
# -----------------------------

if "entered" not in st.session_state:
    st.session_state.entered = False

if "admin_entries" not in st.session_state:
    st.session_state.admin_entries = []

if "selected_story_index" not in st.session_state:
    st.session_state.selected_story_index = None

# -----------------------------
# Helper Functions
# -----------------------------

def get_elements_for_layer(layer):
    if layer == "Global Layer":
        return GLOBAL_ELEMENTS
    elif layer == "National Layer":
        return NATIONAL_ELEMENTS
    elif layer == "Provincial Layer":
        return PROVINCIAL_ELEMENTS
    else:
        return CITY_ELEMENTS


def get_places_for_layer(layer):
    if layer == "Global Layer":
        return GLOBAL_CONNECTIONS
    elif layer == "National Layer":
        return ["China"]
    elif layer == "Provincial Layer":
        return PROVINCES
    else:
        return CITIES


def time_overlaps(entry_start, entry_end, selected_start, selected_end):
    return not (entry_end < selected_start or entry_start > selected_end)

# -----------------------------
# Welcome Page
# -----------------------------

if not st.session_state.entered:
    st.markdown('<div class="title">Welcome to Mapping Global China</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Mapping China through space, theme, connection, and time.</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns([1, 2, 1])

    with col2:
        st.info(
            "This V0.4 prototype introduces a preliminary Story View. "
            "Admin entries can now be opened as provisional research story cards."
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
    '<div class="subtitle">Space · Theme · Global Connection · Time Range · Story</div>',
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

    current_elements = get_elements_for_layer(spatial_layer)

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

        # -----------------------------
        # Related Entries from Admin Portal
        # -----------------------------

        st.markdown("---")
        st.subheader("Related Added Entries")

        related_entries = []

        for index, entry in enumerate(st.session_state.admin_entries):
            same_layer = entry["layer"] == spatial_layer
            same_theme = selected_element in entry["themes"]
            overlap_time = time_overlaps(
                entry["start_year"],
                entry["end_year"],
                start_year,
                end_year
            )

            if same_layer and same_theme and overlap_time:
                related_entries.append((index, entry))

        if related_entries:
            for index, entry in related_entries:
                st.markdown(
                    f"""
                    <div class="event-card">
                        <strong>{entry['title']}</strong><br>
                        Layer: {entry['layer']}<br>
                        Place / connection: {', '.join(entry['places'])}<br>
                        Themes: {', '.join(entry['themes'])}<br>
                        Time range: {entry['start_year']}–{entry['end_year']}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                if st.button("View Story", key=f"view_story_{index}"):
                    st.session_state.selected_story_index = index

            if st.session_state.selected_story_index is not None:
                selected_index = st.session_state.selected_story_index

                if selected_index < len(st.session_state.admin_entries):
                    story = st.session_state.admin_entries[selected_index]

                    st.markdown("---")
                    st.subheader("Story View")

                    st.markdown(
                        f"""
                        <div class="story-card">
                            <h3>{story['title']}</h3>
                            <p><strong>Layer:</strong> {story['layer']}</p>
                            <p><strong>Place / connection:</strong> {', '.join(story['places'])}</p>
                            <p><strong>Themes:</strong> {', '.join(story['themes'])}</p>
                            <p><strong>Period:</strong> {story['start_year']}–{story['end_year']}</p>
                            <hr>
                            <p>{story['summary']}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    if st.button("Close Story"):
                        st.session_state.selected_story_index = None
                        st.rerun()

        else:
            st.info("No added entries match the current layer, theme, and time range.")

    else:
        st.subheader("Admin Portal")

        st.write(
            "Use this interface to add provisional research entries using controlled spatial and thematic categories."
        )

        entry_title = st.text_input("Entry title")

        entry_layer = st.selectbox(
            "Spatial layer",
            ["Global Layer", "National Layer", "Provincial Layer", "City Layer"]
        )

        admin_places = get_places_for_layer(entry_layer)
        admin_elements = get_elements_for_layer(entry_layer)

        entry_places = st.multiselect(
            "Place / connection",
            admin_places
        )

        entry_themes = st.multiselect(
            "Themes",
            admin_elements
        )

        entry_year_range = st.slider(
            "Entry time range",
            min_value=1990,
            max_value=2030,
            value=(2000, 2020),
            step=5
        )

        entry_start_year, entry_end_year = entry_year_range

        entry_summary = st.text_area("Research summary")

        if st.button("Save entry"):
            if not entry_title:
                st.warning("Please enter a title.")
            elif not entry_places:
                st.warning("Please select at least one place or connection.")
            elif not entry_themes:
                st.warning("Please select at least one theme.")
            elif not entry_summary:
                st.warning("Please enter a research summary.")
            else:
                new_entry = {
                    "title": entry_title,
                    "layer": entry_layer,
                    "places": entry_places,
                    "themes": entry_themes,
                    "start_year": entry_start_year,
                    "end_year": entry_end_year,
                    "summary": entry_summary
                }

                st.session_state.admin_entries.append(new_entry)
                st.success("Entry saved to this session.")

        st.markdown("---")
        st.subheader("Current saved entries")

        if st.session_state.admin_entries:
            for entry in st.session_state.admin_entries:
                st.write(f"**{entry['title']}**")
                st.write(f"Layer: {entry['layer']}")
                st.write(f"Place / connection: {', '.join(entry['places'])}")
                st.write(f"Themes: {', '.join(entry['themes'])}")
                st.write(f"Time range: {entry['start_year']}–{entry['end_year']}")
                st.write(entry["summary"])
                st.markdown("---")
        else:
            st.info("No entries have been added yet.")

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
    "**V0.4 Information Architecture:** Admin entries now appear as story-accessible research cards in the User Portal."
)
st.caption(
    "Entries are saved only within the current browser session. Persistent storage will require CSV, JSON, or database support in a later version."
)

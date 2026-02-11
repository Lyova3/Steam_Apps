import os
import sys

CURRENT_DIR = os.path.dirname(__file__)          # .../src/ui
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, "..", ".."))  # .../DSA-Project-Group-5
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

import streamlit as st

from src.utils.data_loader import DataLoader
from src.utils.schemas import SCHEMAS

# Our “React-style components” for each section
from src.analytics.dataset_status import show_dataset_status
from src.analytics.indexed_engine import build_indexed_engine_section
from src.analytics.search_by_appid import search_by_appid_section
from src.analytics.search_by_name import search_by_name_section
from src.analytics.price_range import price_range_section
from src.analytics.basic_analytics import basic_analytics_section
from src.analytics.graph_explorer import render_graph_explorer



# === Cached helpers ===
@st.cache_data
def load_clean_data():
    """
    Load and clean all CSVs using DataLoader + SCHEMAS.

    This is the *expensive* CSV loading step (reading all CSV files, typing
    columns, lowercasing strings, etc.). Streamlit's @st.cache_data makes
    sure we only do it once per code change.
    """
    loader = DataLoader(SCHEMAS)
    cleaned = loader.load_all("data")  # assumes /data folder in project root
    return cleaned


# === Streamlit UI entrypoint ===
st.set_page_config(
    page_title="DSA Project – Steam Apps Explorer",
    layout="wide",
)

st.title("DSA Project – Steam Apps Explorer")
st.subheader("UI Phase 🚀")

st.write(
    """
    If you can see this message in the browser, then:
    - Python ✅
    - Streamlit ✅
    - app.py wired correctly ✅
    """
)

# 1) Load data once (cached)
with st.spinner("Loading and cleaning CSV files..."):
    cleaned_data = load_clean_data()

st.success("Data loaded successfully! 🎉")

# 2) Section 1 – dataset status
show_dataset_status(cleaned_data)

# 3) Section 2 – build indexed engine (and get objects for later sections)
app_engine, indexed_apps = build_indexed_engine_section(cleaned_data)

# 4) Section 3 – search by appid
search_by_appid_section(app_engine)

# 5) Section 4 – search by name
search_by_name_section(indexed_apps)

# 6) Section 5 – price range query
price_range_section(app_engine)

# 7) Section 6 – basic analytics
basic_analytics_section(indexed_apps)


render_graph_explorer(cleaned_data)

import streamlit as st
from settings import Settings


def initialize() -> None:
    """Initialize session state default values."""
    if not Settings.message in st.session_state:
        st.session_state[Settings.message] = ""
    if not Settings.selected_sample_index in st.session_state:
        st.session_state[Settings.selected_sample_index] = 0

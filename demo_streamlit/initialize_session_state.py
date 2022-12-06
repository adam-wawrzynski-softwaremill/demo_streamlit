"""Initialize session state keys with default values."""

import streamlit as st

from demo_streamlit.settings import Settings


def initialize() -> None:
    """Initialize session state default values."""
    if Settings.message not in st.session_state:
        st.session_state[Settings.message] = ""
    if Settings.selected_sample_index not in st.session_state:
        st.session_state[Settings.selected_sample_index] = 0

"""Callbacks from widget events."""

import streamlit as st

from demo_streamlit.query_params import update_query_params
from demo_streamlit.settings import Settings


@update_query_params
def sample_index_callback() -> None:
    """Selectbox state change callback."""
    index: str = st.session_state[Settings.selected_sample_index]
    st.session_state[Settings.message] = f"You have selected sample: {index}"

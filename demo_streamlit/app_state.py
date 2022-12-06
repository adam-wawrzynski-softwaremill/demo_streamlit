"""Script to load/save keys from session state into dataclass."""
from dataclasses import dataclass

import streamlit as st

from demo_streamlit.settings import Settings


@dataclass
class AppState:
    """An app state model."""

    selected_sample_index: int
    """Selected sample index."""

    message: str
    """UI message."""


def get_app_state() -> AppState:
    """Get AppState dataclass from session state."""
    return AppState(
        selected_sample_index=int(
            st.session_state.get(Settings.selected_sample_index, 0)
        ),
        message=st.session_state.get(Settings.message, ""),
    )


def save_app_state(app_state: AppState) -> None:
    """Save AppState dataclass to session state."""
    st.session_state[Settings.selected_sample_index] = app_state.selected_sample_index
    st.session_state[Settings.message] = app_state.message

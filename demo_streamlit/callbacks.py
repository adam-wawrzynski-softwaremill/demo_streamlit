"""Callbacks from widget events."""

import logging
from typing import Any

import streamlit as st

from demo_streamlit.query_params import update_query_params
from demo_streamlit.settings import Settings

logger = logging.getLogger(__name__)


@update_query_params
def sample_index_callback() -> None:
    """Selectbox state change callback."""
    index: str = st.session_state[Settings.selected_sample_index]
    st.session_state[Settings.message] = f"You have selected sample: {index}"


def button_callback(index: str, headers: dict[str, Any] | None) -> None:
    """Button on_click callback."""
    logger.info(  # pylint: disable = (logging-fstring-interpolation)
        f"Passed arguments: ({index}, {headers})."
    )

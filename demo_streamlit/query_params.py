"""Functions to update URL query params based on session state."""
from functools import wraps

import streamlit as st

from demo_streamlit.app_state import AppState, get_app_state, save_app_state
from demo_streamlit.settings import Settings


def _update_query_params() -> None:
    """Updates the URL query params."""
    app_state: AppState = get_app_state()
    query_params: dict[str, list[str]] = {}
    query_params[Settings.message] = [app_state.message]
    query_params[Settings.selected_sample_index] = [
        str(app_state.selected_sample_index)
    ]
    st.experimental_set_query_params(**query_params)


def update_query_params(function):
    """Updates the URL query params after every app state change."""

    @wraps(function)
    def wrapper(*args, **kwargs):
        retval = function(*args, **kwargs)
        _update_query_params()
        return retval

    return wrapper


def load_query_params() -> None:
    """Loads the URL query params."""
    app_state: AppState = get_app_state()
    query_params: dict[str, list[str]] = st.experimental_get_query_params()
    force_update: bool = False
    if Settings.message in query_params:
        app_state.message = query_params[Settings.message][0]
        force_update = True
    if Settings.selected_sample_index in query_params:
        app_state.selected_sample_index = int(
            query_params[Settings.selected_sample_index][0]
        )
        force_update = True

    if force_update:
        save_app_state(app_state=app_state)

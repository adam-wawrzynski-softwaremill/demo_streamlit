import matplotlib
import streamlit as st
from settings import Settings
from load_data import load_dataset, generate_plot
from app_state import AppState, get_app_state
from callbacks import sample_index_callback

from streamlit.web.server.websocket_headers import _get_websocket_headers


def sidebar_view() -> None:
    """Draw side bar."""
    samples = load_dataset()
    st.sidebar.selectbox(
        "Select sample index:",
        options=[val for val in range(0, len(samples))],
        key=Settings.selected_sample_index,
        on_change=sample_index_callback,
    )

    headers: dict[str, str] = _get_websocket_headers()
    with st.sidebar.expander("HTTP header"):
        st.json(headers)


def main_view() -> None:
    """Draw main view."""
    app_state: AppState = get_app_state()
    samples = load_dataset()
    st.markdown(app_state.message)

    figure: matplotlib.figure.Figure = generate_plot(samples, app_state.selected_sample_index)
    st.pyplot(figure)

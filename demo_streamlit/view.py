"""Script to draw Streamlit UI views."""
import matplotlib
import streamlit as st
from streamlit.web.server.websocket_headers import _get_websocket_headers

from demo_streamlit.app_state import AppState, get_app_state
from demo_streamlit.callbacks import sample_index_callback
from demo_streamlit.load_data import load_dataset
from demo_streamlit.plot import generate_plot
from demo_streamlit.settings import Settings


def sidebar_view() -> None:
    """Draw side bar."""
    samples = load_dataset()
    st.sidebar.selectbox(
        "Select sample index:",
        options=list(range(0, len(samples))),
        key=Settings.selected_sample_index,
        on_change=sample_index_callback,
    )

    headers: dict[str, str] | None = _get_websocket_headers()
    if headers:
        with st.sidebar.expander("HTTP header"):
            st.json(headers)


def main_view() -> None:
    """Draw main view."""
    app_state: AppState = get_app_state()
    samples = load_dataset()
    st.markdown(app_state.message)

    figure: matplotlib.figure.Figure = generate_plot(
        samples, app_state.selected_sample_index
    )
    st.pyplot(figure)

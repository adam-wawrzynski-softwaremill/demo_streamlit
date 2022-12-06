"""Entry point for Streamlit app."""
import streamlit as st

from demo_streamlit.initialize_session_state import initialize
from demo_streamlit.query_params import load_query_params
from demo_streamlit.view import main_view, sidebar_view


def main() -> None:
    """Entry point of Streamlit app."""
    st.title("MNIST dataset visualization")
    initialize()
    load_query_params()
    sidebar_view()
    main_view()


if __name__ == "__main__":
    main()

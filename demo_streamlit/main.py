import streamlit as st
from initialize_session_state import initialize
from view import sidebar_view, main_view
from query_params import load_query_params


def main() -> None:
    """Entry point of Streamlit app."""
    st.title("MNIST dataset visualization")
    initialize()
    load_query_params()
    sidebar_view()
    main_view()

if __name__ == "__main__":
    main()

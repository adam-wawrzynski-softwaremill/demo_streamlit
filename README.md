# Demo Streamlit app

## Requirements

To separate runtime environments for different services and repositories, it is
recommended to use a virtual Python environment, e.g. `virtualenv`. After
installing it, create a new environment and activate it. The project uses Python
version `3.10`.

In the example below, the `-p` parameter specifies the Python version
and the second parameter the name of the virtual environment, for
example `env`.

```bash
virtualenv -p python3.10 .venv
source .venv/bin/activate
```

The project uses the `poetry` package, which manages the dependencies in the
project. To install it first update the `pip` package and then install `poetry`
version `1.2.1`.

```bash
python -m pip install --upgrade pip
```

Instructions for installation of `poetry`:
https://python-poetry.org/docs/#installing-with-the-official-installer.

The final step is to install all the dependencies defined in the
`pyproject.toml` file.

```bash
poetry install
```

Once all the steps have been completed, the environment is ready to go.

# Run

To run the application type:

```bash
poetry run streamlit run demo_streamlit/main.py
```

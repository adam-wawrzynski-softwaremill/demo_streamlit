"""Functions used to load MNIST dataset."""
import logging

import streamlit as st
import torch
import torchvision

logger = logging.getLogger(__name__)


@st.cache(allow_output_mutation=True)
def load_dataset() -> list[tuple[torch.Tensor, torch.Tensor]]:
    """Load MNIST dataset.

    Returns:
        List of pairs: image and target label.
    """
    logger.info("Load dataset")
    data = torchvision.datasets.MNIST(
        "files/",
        train=False,
        download=True,
        transform=torchvision.transforms.Compose(
            [
                torchvision.transforms.ToTensor(),
                torchvision.transforms.Normalize((0.1307,), (0.3081,)),
            ]
        ),
    )
    return list(zip(data.data, data.targets))

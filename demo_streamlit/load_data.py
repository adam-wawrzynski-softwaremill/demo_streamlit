
import torch
import torchvision
import matplotlib
import matplotlib.pyplot as plt
import streamlit as st
import logging

logger = logging.getLogger(__name__)

def generate_plot(
    samples: list[tuple[torch.Tensor, torch.Tensor]],
    index: int,
) -> matplotlib.figure.Figure:
    """Generate matplot Figure from image and target label.

    Args:
        samples : List of images.
        index: Index of sample to display.

    Returns:
        Figure with selected image.
    """
    fig = plt.figure()
    plt.plot()
    plt.imshow(samples[index][0], cmap='gray', interpolation='none')
    plt.title("Ground Truth: {}".format(samples[index][1]))
    plt.xticks([])
    plt.yticks([])
    return fig


@st.cache(allow_output_mutation=True)
def load_dataset() -> list[tuple[torch.Tensor, torch.Tensor]]:
    """Load MNIST dataset.

    Returns:
        List of pairs: image and target label.
    """
    logger.info("Load dataset")
    data = torchvision.datasets.MNIST(
        'files/',
        train=False,
        download=True,
        transform=torchvision.transforms.Compose(
            [
                torchvision.transforms.ToTensor(),
                torchvision.transforms.Normalize((0.1307,), (0.3081,))
            ]
        )
    )
    return [(img, label) for img, label in zip(data.data, data.targets)]

"""Functions used to load figure."""
import matplotlib
import matplotlib.pyplot as plt
import torch


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
    plt.imshow(samples[index][0], cmap="gray", interpolation="none")
    plt.title(f"Ground Truth: {samples[index][1]}")
    plt.xticks([])
    plt.yticks([])
    return fig

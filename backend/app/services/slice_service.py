import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

def generate_slice_png(
    image,
    output_path
):

    plt.figure(figsize=(5,5))

    plt.imshow(image, cmap="gray")

    plt.axis("off")

    plt.savefig(
        output_path,
        bbox_inches="tight",
        pad_inches=0
    )

    plt.close()
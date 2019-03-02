import matplotlib.pyplot as plt
from matplotlib import patheffects
import numpy as np
data = np.random.random(70)


def main():
    fontsize = 18
    plt.plot(data)

    title = "This is figure title"
    x_label = "This is x axis label"
    y_label = "This is y axis label"

    title_text_obj = plt.title(title, fontsize=fontsize, verticalalignment='bottom')
    title_text_obj.set_path_effects([patheffects.withSimplePatchShadow()])

    # offset_xy -- set the 'angle' of the shadow
    # shadow_rgbFace == set the color of the shadow
    # patch_alpha == setup the transparency of the shadow

    offset_xy = (1, -1)
    rgbRed = (1.0, 0.0, 0.0)
    alpha = 0.8

    # customize shadow properties
    pe = patheffects.withSimplePatchShadow( shadow_rgbFace=rgbRed)

    # apply them to the xaxis anf yaxis labels
    xlabel_obj = plt.xlabel(x_label, fontsize=fontsize, alpha=0.5)
    xlabel_obj.set_path_effects([pe])
    #
    ylabel_obj = plt.ylabel(y_label, fontsize=fontsize, alpha=0.5)
    ylabel_obj.set_path_effects([pe])

    plt.show()


if __name__ == '__main__':
    main()


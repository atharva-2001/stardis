import numpy as np


class Opacities:
    """
    Holds opacity information.

    Paramaters
    ----------
    opacities_dict : dict
        Python dictionary to contain each of the sources of opacity by name as well as their contribution at each frequency specified in the radiation field.
    total_alphas : numpy.ndarray
        Array of the total opacity at each frequency specified in the radiation field at each depth points.
        Added as an attribute when calc_total_alphas() is called.
    """

    def __init__(self, frequencies, stellar_model):
        self.opacities_dict = {}
        self.total_alphas = np.zeros(
            (stellar_model.no_of_depth_points, len(frequencies))
        )

    ###TODO: Better implementation for this
    def calc_total_alphas(self):
        for item in self.opacities_dict.items():
            if "gammas" not in item[0] and "doppler" not in item[0]:
                self.total_alphas += item[1]
        return self.total_alphas

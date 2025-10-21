# Configuration data
class configData:
    """
    This class stores the parameters for the experiment.
    The parameters are fixed parameters.
    If necessary, the parameters can be modified as class inputs.
    """

    def __init__(self):
        self.L = 100  # Reservoir length (in meter)
        self.nx = 21  # Number of grid points
        self.T0 = 200  # Reservoir temperature (in celsius)
        self.T_inj = 60  # Injection temperature (in celsius)
        self.alpha = 9 * (10 ** -7)  # Thermal diffusivity
        self.v = 1.5 * (10 ** -5)  # Flow velocity

        self.dt = 86400  # in seconds
        self.dx = self.L / (self.nx - 1)
        self.time_step = 1  # in days
        self.simTime = 365 * self.time_step  # Total time duration
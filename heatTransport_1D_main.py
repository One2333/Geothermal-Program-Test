from heatTransport_configData import configData
from heatTransport_plot import generatePlots


class heatTransportModel:
    """
    This class is the main function of the experiment.
    The function runExp() is used for calculating the temperature updates.
    The function genPlot() is used for generating the experiment plot based on the experiment output.
    """
    def __init__(self):
        self.T_outlet = []
        self.simData = configData()  # initialize the experiment parameters

    def runExp(self):

        # initialization
        T = [self.simData.T0] * self.simData.nx  # initial condition
        T[0] = self.simData.T_inj  # left boundary condition
        T[-1] = T[-2]  # right boundary condition
        self.T_outlet = [T[-1]]  # record the outlet temperature

        # Update temperature
        for curTime in range(1, self.simData.simTime + 1, self.simData.time_step):
            T_new = [0] * self.simData.nx  # re-initialize T_new list every time step
            T_new[0] = self.simData.T_inj

            for i in range(1, self.simData.nx - 1):
                T_new[i] = T[i] + self.simData.dt * (
                        self.simData.alpha * (T[i + 1] - 2.0 * T[i] + T[i - 1]) / self.simData.dx ** 2 - self.simData.v * (
                        T[i] - T[i - 1]) / self.simData.dx)

            T_new[-1] = T_new[-2]
            self.T_outlet.append(T_new[-1])
            T = T_new.copy()

    def genPlot(self):
        simPlot = generatePlots(self.simData.simTime, self.simData.time_step, self.T_outlet)
        simPlot.plot_Temp_VS_Time()


expModel = heatTransportModel()
expModel.runExp()
expModel.genPlot()

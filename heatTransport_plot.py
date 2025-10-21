import matplotlib.pyplot as plt
import numpy as np


class generatePlots:
    """
    This class is used for generate the experiment plots.
    The class can be modified based on what data is used from the experiment output.
    """

    def __init__(self, simTime, timeStep, output_lst):
        self.simTime = simTime
        self.time_step = timeStep
        self.T_outlet = output_lst

    def plot_Temp_VS_Time(self):
        simPlot = generatePlots(self.simTime, self.time_step, self.T_outlet)
        # Plot for output
        plt.plot(np.arange(0, simPlot.simTime + 1, simPlot.time_step), simPlot.T_outlet, label='Outlet Temp VS. Days')
        plt.xlim(0, simPlot.simTime)
        plt.xlabel('Time (days)')
        plt.ylabel('Outlet Temperature (celsius)')
        plt.title('1D Heat Transport')
        plt.grid()
        plt.legend()
        plt.show()

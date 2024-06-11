import nidaqmx # import module nidaqmx
from nidaqmx.constants import TerminalConfiguration # import constant file to change terminal configuration
import matplotlib.pyplot as plt # import plotting package

plt.ylim((0, 2)) # limit y axis on plot
plt.ion() # keep plot from clearing each run 

i = 0
with nidaqmx.Task() as task:
  task.ai_channels.add_ai_voltage_chan("Dev1/ai1", terminal_config= TerminalConfiguration.NRSE) # initialize the acquisition task
  while i<100:
    data = task.read(number_of_samples_per_channel=1) # reads from channel every loop
    plt.scatter(i, data[0], c='r')
    plt.pause(0.05)

    i = i + 1

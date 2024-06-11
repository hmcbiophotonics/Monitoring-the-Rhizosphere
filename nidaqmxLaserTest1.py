import nidaqmx
from nidaqmx.constants import TerminalConfiguration
import matplotlib.pyplot as plt
import csv

plt.ylim((0.5, 0.95))
plt.ion()
plt.xlabel("Sample Number")
plt.ylabel("Voltage (V)")
plt.title("No Ambient Light, Laser On Voltage for no Stem")

# set up csv file

# field names
fields = ['Sample Number', 'Voltage']

# data rows of csv file
rows = []

# csv filename
filename = "lasernobeanENDOFDAY.csv"

i = 0
with nidaqmx.Task() as task:
  task.ai_channels.add_ai_voltage_chan("Dev1/ai1", terminal_config= TerminalConfiguration.NRSE)
  while i<250:
    data = task.read(number_of_samples_per_channel=1)
    rows.append([i, data[0]])
    plt.scatter(i, data[0], c='r')
    plt.pause(0.05)
    

    i = i + 1

plt.show(block=True) #keep the graph on the screen once data collection is finished

with open(filename, 'w') as csvfile:
  # create csv writer object
  csvwriter = csv.writer(csvfile)

  # writing the fields
  csvwriter.writerow(fields)

  # writing the data rows
  csvwriter.writerows(rows)



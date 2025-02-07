import pandas as pd
import matplotlib.pyplot as plt
import mplcursors

# Load the CSV file
file_path = r'C:\Users\civig\Desktop\SiPM\Cristalli\Probabilities\new-na-0cm.CSV'
data = pd.read_csv(file_path, delimiter=';')

# Plot the data
fig, ax = plt.subplots()
ax.plot(data['Channel'], data['BGO'], label='BGO')
ax.plot(data['Channel'], data['CSI'], label='CSI')
ax.plot(data['Channel'], data['LYSO'], label='LYSO')

# Add labels and title
ax.set_xlabel('Channel')
ax.set_ylabel('Counts')
ax.set_title('Counts vs Channel')
ax.legend()
ax.grid()

# Enable interactive cursor
mplcursors.cursor(hover=True)

# Show the plot
plt.show()

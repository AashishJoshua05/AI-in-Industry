import pandas as pd

# Define the data in a DataFrame
data = pd.DataFrame({
    'Process': ['P1', 'P2', 'P3', 'P4'],
    'Arrival Time': [0, 4, 5, 6],
    'Burst Time': [23, 3, 3, 12],
    'Priority': [3, 1, 4, 2]
})

# Calculate waiting time and turnaround time for FCFS
data_fcfs = data.sort_values(by='Arrival Time')
data_fcfs['Waiting Time'] = [0] + [max(0, data_fcfs['Burst Time'].values[i-1] - data_fcfs['Arrival Time'].values[i]) for i in range(1, len(data_fcfs))]
data_fcfs['Turnaround Time'] = data_fcfs['Waiting Time'] + data_fcfs['Burst Time']
avg_waiting_time_fcfs = data_fcfs['Waiting Time'].mean()
avg_turnaround_time_fcfs = data_fcfs['Turnaround Time'].mean()

# Calculate waiting time and turnaround time for SJF
data_sjf = data.sort_values(by='Burst Time')
data_sjf['Waiting Time'] = [0] + [max(0, data_sjf['Burst Time'].values[i-1] - data_sjf['Arrival Time'].values[i]) for i in range(1, len(data_sjf))]
data_sjf['Turnaround Time'] = data_sjf['Waiting Time'] + data_sjf['Burst Time']
avg_waiting_time_sjf = data_sjf['Waiting Time'].mean()
avg_turnaround_time_sjf = data_sjf['Turnaround Time'].mean()

# Calculate waiting time and turnaround time for Priority Scheduling
data_ps = data.sort_values(by='Priority')
data_ps['Waiting Time'] = [0] + [sum(data_ps['Burst Time'][:i]) - data_ps['Arrival Time'].values[i] for i in range(1, len(data_ps))]
data_ps['Turnaround Time'] = data_ps['Waiting Time'] + data_ps['Burst Time']
avg_waiting_time_ps = data_ps['Waiting Time'].mean()
avg_turnaround_time_ps = data_ps['Turnaround Time'].mean()

# Calculate waiting time and turnaround time for Round Robin (RR)
time_quantum = 4
data_rr = data.copy()
data_rr['Waiting Time'] = [0] * len(data_rr)
data_rr['Turnaround Time'] = [0] * len(data_rr)

while data_rr['Burst Time'].sum() > 0:
    for i in range(len(data_rr)):
        if data_rr['Burst Time'][i] > 0:
            if data_rr['Burst Time'][i] > time_quantum:
                data_rr['Waiting Time'][i] += sum(data_rr['Burst Time'][:i]) - data_rr['Arrival Time'][i]
                data_rr['Burst Time'][i] -= time_quantum
            else:
                data_rr['Waiting Time'][i] += sum(data_rr['Burst Time'][:i]) - data_rr['Arrival Time'][i]
                data_rr['Burst Time'][i] = 0
                data_rr['Turnaround Time'][i] = data_rr['Waiting Time'][i] + data_rr['Arrival Time'][i]

avg_waiting_time_rr = data_rr['Waiting Time'].mean()
avg_turnaround_time_rr = data_rr['Turnaround Time'].mean()

# Print the results
print("Average Waiting Time and Turnaround Time for FCFS:")
print("Average Waiting Time:", avg_waiting_time_fcfs)
print("Average Turnaround Time:", avg_turnaround_time_fcfs)

print("\nAverage Waiting Time and Turnaround Time for SJF:")
print("Average Waiting Time:", avg_waiting_time_sjf)
print("Average Turnaround Time:", avg_turnaround_time_sjf)

print("\nAverage Waiting Time and Turnaround Time for Priority Scheduling:")
print("Average Waiting Time:", avg_waiting_time_ps)
print("Average Turnaround Time:", avg_turnaround_time_ps)

print("\nAverage Waiting Time and Turnaround Time for Round Robin (RR):")
print("Average Waiting Time:", avg_waiting_time_rr)
print("Average Turnaround Time:", avg_turnaround_time_rr)

import csv

filename = 'train_iteration.csv'

data_list = []

with open(filename, 'r', newline='') as file:
    reader = csv.reader(file)
    
    for row in reader:
        # Check if the row is not empty
        if row:
            # Append only the first 2 items (slicing handles rows with <2 items safely)
            data_list.append([int(row[0]),int(row[0])+int(row[1])])

end_time = data_list[0][1]
cpu_overhead = 0
run_time = (data_list[0][1] - data_list[0][0])/1000
start_time = data_list[0][0]
for data in data_list:
    if data[0] > end_time:
        launch_overhead = data[0] - end_time
        cpu_overhead = cpu_overhead + (launch_overhead/1000)
        run_time = run_time + ((data[1] - data[0])/1000)
        end_time = data[1]
    else:
        if data[1] > end_time:
            run_time = run_time + ((data[1] - end_time)/1000)
            end_time = data[1]
    finish_time = data[1]

print("Kernel Run Time: ", run_time)
print("CPU Overhead Time: ", cpu_overhead)
print("Sum of calculated Kernel and CPU overhead: ", run_time+cpu_overhead)
print("Runtime from profile: ", (finish_time-start_time)/1000)

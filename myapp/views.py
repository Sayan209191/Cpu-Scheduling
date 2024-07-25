from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        algorithm = request.POST.get('algorithm')
        processes = request.POST.get('processes')
        
        if algorithm and processes:
            request.session['algorithm'] = algorithm
            request.session['processes'] = processes
            return redirect('/process-details/')  # Direct path

    return render(request, 'index.html')

def process_details(request):
    algorithm = request.session.get('algorithm')
    processes = request.session.get('processes')
    
    if not algorithm or not processes:
        return redirect('/')  # Direct path
    
    processes = int(processes)
    
    if request.method == 'POST':
        process_data = []
        for i in range(processes):
            process_data.append({
                'id': i,  # Change to an index for array referencing
                'arrival_time': int(request.POST.get(f'arrival_time_{i}')),
                'burst_time': int(request.POST.get(f'burst_time_{i}')),
                'priority': int(request.POST.get(f'priority_{i}', 0))  # Default priority to 0 if not provided
            })
        
        if algorithm.lower() == 'fcfs':
            total_waiting_time, average_waiting_time, total_turnaround_time = fcfs(process_data)
        elif algorithm.lower() == 'sjf':
            total_waiting_time, average_waiting_time, total_turnaround_time = sjf(process_data)
        elif algorithm.lower() == 'round_robin':
            time_quantum = int(request.POST.get('time_quantum'))
            total_waiting_time, average_waiting_time, total_turnaround_time = round_robin(process_data, time_quantum)
        elif algorithm.lower() == 'priority':
            total_waiting_time, average_waiting_time, total_turnaround_time = priority_scheduling(process_data)
        else:
            return HttpResponse("Algorithm not supported.")
        
        context = {
            'process_data': process_data,
            'total_waiting_time': total_waiting_time,
            'average_waiting_time': average_waiting_time,
            'total_turnaround_time': total_turnaround_time,
            'algorithm': algorithm,
        }
        return render(request, 'results.html', context)
    
    return render(request, 'process_details.html', {'algorithm': algorithm, 'processes': range(processes)})


# calculate total waiting time & turn around time 

def fcfs(process_data):
    for process in process_data:
        process['id'] = int(process['id'])
        process['arrival_time'] = int(process['arrival_time'])
        process['burst_time'] = int(process['burst_time'])
    
    # Sort the process data by arrival time
    sorted_process_data = sorted(process_data, key=lambda x: x['arrival_time'])
    
    n = len(sorted_process_data)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    waiting_time[0] = 0
    turnaround_time[0] = sorted_process_data[0]['burst_time']
    
    total_processing_time = sorted_process_data[0]['burst_time']
    # Calculate waiting time
    for i in range(1, n):
        
        if total_processing_time - sorted_process_data[i]['arrival_time'] < 0:
            waiting_time[i] = 0
        else :
            waiting_time[i] = total_processing_time - sorted_process_data[i]['arrival_time'] 
        
        turnaround_time[i] = waiting_time[i] + sorted_process_data[i]['burst_time']
        
        total_processing_time += sorted_process_data[i]['burst_time']
        
    
   
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)
    average_waiting_time = total_waiting_time / n
    
    return [total_waiting_time, average_waiting_time, total_turnaround_time]



# SJF

def sjf(process_data):
    # Convert arrival and burst times to integers
    for process in process_data:
        process['arrival_time'] = int(process['arrival_time'])
        process['burst_time'] = int(process['burst_time'])
    
    # Sort processes by arrival time
    sorted_process_data = sorted(process_data, key=lambda x: x['arrival_time'])
    
    n = len(sorted_process_data)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    completed = [False] * n
    
    current_time = 0
    completed_processes = 0
    
    while completed_processes < n:
        # Find the process with the shortest burst time that has arrived
        shortest = None
        for i in range(n):
            if (not completed[i]) and (sorted_process_data[i]['arrival_time'] <= current_time):
                if (shortest is None) or (sorted_process_data[i]['burst_time'] < sorted_process_data[shortest]['burst_time']):
                    shortest = i
        
        if shortest is not None:
            # Process the selected shortest job
            current_time += sorted_process_data[shortest]['burst_time']
            waiting_time[shortest] = current_time - sorted_process_data[shortest]['arrival_time'] - sorted_process_data[shortest]['burst_time']
            turnaround_time[shortest] = current_time - sorted_process_data[shortest]['arrival_time']
            completed[shortest] = True
            completed_processes += 1
        else:
            # If no process is ready, move time forward
            current_time += 1
    
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)
    average_waiting_time = total_waiting_time / n
    
    return [total_waiting_time, average_waiting_time, total_turnaround_time]

def round_robin(process_data, time_quantum):
    # Convert arrival and burst times to integers
    for process in process_data:
        process['arrival_time'] = int(process['arrival_time'])
        process['burst_time'] = int(process['burst_time'])
    
    # Sort processes by arrival time
    sorted_process_data = sorted(process_data, key=lambda x: x['arrival_time'])
    
    n = len(sorted_process_data)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    remaining_burst_time = [process['burst_time'] for process in sorted_process_data]
    
    current_time = 0
    completed_processes = 0
    
    # Queue for Round Robin scheduling
    queue = []
    for i in range(n):
        queue.append(i)
    
    while completed_processes < n:
        i = queue.pop(0)
        if remaining_burst_time[i] > 0:
            arrival = sorted_process_data[i]['arrival_time']
            
            if remaining_burst_time[i] > time_quantum:
                current_time += time_quantum
                remaining_burst_time[i] -= time_quantum
                # Re-add process to the queue
                queue.append(i)
            else:
                current_time += remaining_burst_time[i]
                waiting_time[i] = current_time - sorted_process_data[i]['arrival_time'] - sorted_process_data[i]['burst_time']
                turnaround_time[i] = current_time - sorted_process_data[i]['arrival_time']
                remaining_burst_time[i] = 0
                completed_processes += 1
    
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)
    average_waiting_time = total_waiting_time / n
    
    print(waiting_time)
    print(turnaround_time)
    
    return [total_waiting_time, average_waiting_time, total_turnaround_time]

def priority_scheduling(process_data):
    n = len(process_data)
    waiting_time = [0] * n
    turnaround_time = [0] * n
    
    # Sort processes by arrival time, then by priority (lower number means higher priority)
    process_data.sort(key=lambda x: (x['arrival_time'], x['priority']))
    
    current_time = 0
    completed_processes = 0
    ready_queue = []

    while completed_processes < n:
        # Add all processes that have arrived by current_time to the ready queue
        for process in process_data:
            if process['arrival_time'] <= current_time and process not in ready_queue:
                ready_queue.append(process)
        
        # Sort the ready queue by priority (lower number means higher priority)
        ready_queue.sort(key=lambda x: x['priority'])
        
        if ready_queue:
            # Select the highest priority process
            current_process = ready_queue.pop(0)
            process_id = current_process['id']
            arrival_time = current_process['arrival_time']
            burst_time = current_process['burst_time']
            priority = current_process['priority']
            
            # Calculate waiting time and turnaround time
            waiting_time[process_id] = current_time - arrival_time
            if waiting_time[process_id] < 0:
                waiting_time[process_id] = 0
            turnaround_time[process_id] = waiting_time[process_id] + burst_time
            
            # Update current time
            current_time += burst_time
            completed_processes += 1
            
            # Remove the process from process_data
            process_data = [p for p in process_data if p['id'] != process_id]
        else:
            # If no process is ready, move the current time forward
            current_time += 1
    
    total_waiting_time = sum(waiting_time)
    total_turnaround_time = sum(turnaround_time)
    average_waiting_time = total_waiting_time / n
    
    return total_waiting_time, average_waiting_time, total_turnaround_time


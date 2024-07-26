CPU Scheduling Algorithm Visualizer
Overview
This project is a web-based CPU scheduling algorithm visualizer built using Django. It allows users to input process details and visualize the scheduling of processes using various algorithms. The implemented algorithms include First-Come, First-Served (FCFS), Shortest Job First (SJF), Round Robin, and Priority Scheduling.

Features
Process Input Forms: Users can input process details including process ID, arrival time, burst time, and priority (for Priority Scheduling).
Session Management: User inputs are managed through Django sessions to ensure smooth data transfer between views.
Algorithm Selection: Users can select from FCFS, SJF, Round Robin, and Priority Scheduling algorithms.
Results Display: The application calculates and displays total waiting time, average waiting time, and total turnaround time for the selected scheduling algorithm.
Round Robin Time Quantum: For the Round Robin algorithm, users can input the time quantum.
Installation
Clone the repository:

sh
Copy code
git clone https://github.com/Sayan209191/Cpu-Scheduling.git
cd Cpu-Scheduling
Install dependencies:

sh
Copy code
pip install django
pip install pymysql
Setup the database:
Make sure you have MySQL installed and running. Update the DATABASES setting in settings.py with your MySQL credentials.

python
code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cpuscheduling',
        'USER' : 'root',
        'PASSWORD' : 'Sayan@2091@',
        'HOST' : '127.0.0.1',
        'PORT' : '3306',
    }
}

Run migrations:

sh
Copy code
python manage.py migrate
Start the development server:

sh
Copy code
python manage.py runserver
Access the application:
Open your web browser and go to http://127.0.0.1:8000/.

Usage
Home Page:

Select the desired scheduling algorithm.
Enter the number of processes.
Click "Submit".
Process Details Page:

Input the process ID, arrival time, burst time, and priority (if applicable) for each process.
For Round Robin, input the time quantum.
Click "Submit".
Results Page:

View the total waiting time, average waiting time, and total turnaround time for the selected algorithm.
Algorithms Implemented
FCFS (First-Come, First-Served)
The FCFS algorithm schedules processes in the order they arrive. It calculates the waiting time and turnaround time based on the arrival time and burst time of each process.

SJF (Shortest Job First)
The SJF algorithm selects the process with the shortest burst time next. If two processes have the same burst time, it selects based on arrival time.

Round Robin
The Round Robin algorithm assigns a fixed time quantum to each process in the ready queue in a cyclic order. It continues until all processes are completed.

Priority Scheduling
The Priority Scheduling algorithm selects the process with the highest priority (lowest priority number) next. If two processes have the same priority, it selects based on arrival time.

Acknowledgements
Django Documentation
CPU Scheduling Algorithms and their implementation
Contact
For any queries or issues, please contact sayanghorui747@gmail.com

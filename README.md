<p align="center">
  <img src="https://cdn-icons-png.flaticon.com/512/6295/6295417.png" width="100" />
</p>
<p align="center">
    <h1 align="center">CPU-SCHEDULING</h1>
</p>


<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/HTML5-E34F26.svg?style=flat&logo=HTML5&logoColor=white" alt="HTML5">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
</p>
<hr>

---

##  Overview


---

##  Features

Process Input Forms: Users can input process details including process ID, arrival time, burst time, and priority (for Priority Scheduling).

Session Management: User inputs are managed through Django sessions to ensure smooth data transfer between views.

Algorithm Selection: Users can select from FCFS, SJF, Round Robin, and Priority Scheduling algorithms.

Results Display: The application calculates and displays total waiting time, average waiting time, and total turnaround time for the selected scheduling algorithm.

Round Robin Time Quantum: For the Round Robin algorithm, users can input the time quantum.

---

##  Repository Structure

```sh
└── Cpu-Scheduling/
    ├── README.md
    ├── cpuseduling
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-311.pyc
    │   │   ├── settings.cpython-311.pyc
    │   │   ├── urls.cpython-311.pyc
    │   │   └── wsgi.cpython-311.pyc
    │   ├── asgi.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    ├── db.sqlite3
    ├── manage.py
    ├── myapp
    │   ├── __init__.py
    │   ├── __pycache__
    │   │   ├── __init__.cpython-311.pyc
    │   │   ├── admin.cpython-311.pyc
    │   │   ├── apps.cpython-311.pyc
    │   │   ├── models.cpython-311.pyc
    │   │   ├── urls.cpython-311.pyc
    │   │   └── views.cpython-311.pyc
    │   ├── admin.py
    │   ├── apps.py
    │   ├── migrations
    │   │   ├── __init__.py
    │   │   └── __pycache__
    │   │       └── __init__.cpython-311.pyc
    │   ├── models.py
    │   ├── tests.py
    │   ├── urls.py
    │   └── views.py
    ├── static
    │   └── style
    │       └── style.css
    └── template
        ├── index.html
        ├── process_details.html
        └── results.html
```

---


</details>

---

##  Getting Started

***Requirements***

Ensure you have the following dependencies installed on your system:

* **Python**: `version 3.9`

###  Installation

1. Clone the Cpu-Scheduling repository:

```sh
git clone https://github.com/Sayan209191/Cpu-Scheduling
```

2. Change to the project directory:

```sh
cd Cpu-Scheduling
```

3. Install the dependencies:

```sh
pip install django
pip install pymqsql
```
###  Set up DataBase
Setup the database:
Make sure you have MySQL installed and running. Update the DATABASES setting in settings.py with your MySQL credentials.

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
###  Run Migration
```sh
python manage.py makemigrations
python manage.py migrate
```
###  Running Cpu-Scheduling

Use the following command to run Cpu-Scheduling:

```sh
python manage.py runserver
```

###  Access the application

Open your web browser and go to http://127.0.0.1:8000/.

###  Usage

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

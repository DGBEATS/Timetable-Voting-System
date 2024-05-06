# Timetable Generator

This README provides instructions on how to run the Timetable Generator website locally.

## Running the Website locally

### Prerequisites

1. The most up-to-date Python version must be installed on your system. That can be downloaded [here](https://www.python.org/downloads/).
2. The most up-to-date pip or pip3 version.
3. Python file/folder must have been added to [PATH](https://realpython.com/add-python-to-path/). (Follow terminal instructions as needed when setting up the virtual environment).

### Steps

1. Clone the repository:

```bash
   git clone https://github.com/DGBEATS/Timetable-Voting-System.git
```

2. Move into the directory where the files are located

```bash
   cd Timetable-Voting-System
```

3. Create a virtual environment:

```bash
   # (Install virtualenv first)
   pip install virtualenv
   # (Create virtualenv)
   virtualenv envname
```

4. Activate the virtual environment:

```bash
   envname\Scripts\activate
```

5. Inside the virtual environment install django

```bash
   pip install django
```

## Starting the local server

1. Change your directory into the ttss_assignment folder

```bash
   cd ttss_assignment
```

2. Start the server:

```django
    python manage.py runserver
```

Then the development server will be started at http://127.0.0.1:8000/

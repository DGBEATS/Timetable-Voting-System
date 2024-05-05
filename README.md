# Timetable Generator

This README provides instructions on how to run the Timetable Generator website locally.

## Running the Website locally

### Prerequisites

1. The most up-to-date Python version must be install on your system. That can be downloaded [here](https://www.python.org/downloads/).

### Steps

1. Clone the repository:

```bash
   git clone https://github.com/DGBEATS/Timetable-Voting-System.git
```

2. Move into the directory where the files are located

```bash
   cd ttss_assignment
```

3. Create a virtual environment:

```bash
   [//]: # (Install virtualenv first)
   pip install virtualenv
   [//]: # (Create virtualenv)
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

1. Inside your IDE, create a new terminal.

2. Start the server:

```django
    python manage.py runserver
```

Then the development server will be started at http://127.0.0.1:8000/

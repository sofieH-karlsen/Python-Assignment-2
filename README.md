# ACIT_StudyReminder
Using Python to automate personalized study reminders for students

## Overview
The 'ACIT_StudyReminder' package automates sending students personalised study reminders.\
I manages the students data, generated reminders, simulates delivery by email, logs the activity, and automatically schedules reminders.

The package was developed as part of the second mandatory assignment for the course **ACIT4420: Problem-solving with Scripting** at OsloMet.

## Features
- Manage student information (add, remove, list)
- Generate personalised reminders
- Simulate sending reminder via console output
- Log the details of the reminders with timestamps
- Schedule reminders based on preferred time

## Structure


```bash
SHK-ACIT_StudyReminder
├── modules
│   ├── __init__.py
│   ├── logger.py
│   ├── reminder_generator.py
│   ├── reminder_sender.py
│   ├── scheduler.py
│   └── students_manager.py
├── README.md
├── main.py
├── requirements.txt
├── setup.py
└── .gitignore
```
## Installation
The package can simply be installed by running\
`pip install git+https://gitlab.com/Soso2509/shk-assignment2.git`\
Together with the package this wil also install the requirements noted in `requirements.txt`.

## Usage
Once the package is installed it can be run with the command `study_reminders` followed by one of four sub-commands.

### `study_reminders list`
This will output a list of all the students
```bash
# Example
Name: Amalie, Email: amalie@example.com, Course: Computer Science, Preferred Time: 08:00
Name: Benny, Email: benny@example.com, Course: Mathematics, Preferred Time: 09:00
Name: Charlotte, Email: charlotte@example.com, Course: Physics, Preferred Time: 07:30

```

It should be noted that the package does not come with an `students.json` file with dummy data, and the output of this command without one will be a single dummy student.\
Such a file can be manually created or it will be automatically created the first time the `add` subcommand(see below) is used without one.

### `study_reminders add <name> <email> <course> <preferred time>`
Modifies the list of students by adding one.\
Example if running `study_reminders add Ola ola@example.no "python scripting" 08:00`
```bash
Added student: Ola
```
And "Ola" is added to the *students.json* file
```JSON
{
    "name": "Ola",
    "email": "ola@example.no",
    "course": "python scripting",
    "preferred_time": "08:00"
    }
```
### `study_reminders remove <name>`
Modifies the list of students by removing a student by the given name
```bash
# Example Output
Removed student: Ola
```
Said student is then removed from the JSON file\

### `study_reminders schedule`
This command runs the automation process, and will
- Load students from `students.json`(or the test student if the file does not exist)
- Generate personalised reminders
- Print a list of current students
- Simulate sending them to each student email
- Log the actions to `reminder_log.txt`(said file will be created if it does not exist)
- Schedule future reminders based on preferred times

```bash
# Example output
Current students:
  Amalie - amalie@example.com (Computer Science) at 08:00
  Benny - benny@example.com (Mathematics) at 09:00
  Charlotte - charlotte@example.com (Physics) at 07:30

Simulating reminder sending...
Sending reminder to amalie@example.com: Amalie, remember to review the materials for Computer Science before the deadline!
Sending reminder to benny@example.com: Benny, remember to review the materials for Mathematics before the deadline!
Sending reminder to charlotte@example.com: Charlotte, remember to review the materials for Physics before the deadline!

Scheduling daily reminders (Ctrl+C to stop)...

```
### `study_reminders`
Running only the main command will output the help message shown below

```bash
usage: study_reminders [-h] {list,add,remove,schedule} ...

study_reminders CLI tool

positional arguments:
  {list,add,remove,schedule}
    list                List all students
    add                 Add a new student (name, email,course, preferred reminder time)(For arguments with multiple words use "")
    remove              Remove a student (name)
    schedule            Runs simulation of scheduled reminder sending

options:
  -h, --help            show this help message and exit
```
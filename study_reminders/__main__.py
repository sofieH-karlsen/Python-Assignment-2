import argparse

from modules.students_manager import StudentsManager
from modules.reminder_generator import generate_reminder
from modules.reminder_sender import send_reminder
from modules.logger import log_reminder
from modules.scheduler import schedule_reminders

def list_students(manager: StudentsManager):
    manager.list_students()


def add_student(manager: StudentsManager, name: str, email: str, course: str, preferred_time: str):
    manager.add_student(name, email, course, preferred_time)
    print(f"Added student: {name}")

def remove_student(manager: StudentsManager, name: str):
    manager.remove_student(name)
    print(f"Removed student: {name}")

def run_scheduler(manager: StudentsManager):
    students = manager.get_students()

    # Display current students
    print("Loaded students:")
    for s in students:
        print(f"  {s['name']} - {s['email']} ({s['course']}) at {s['preferred_time']}")

    # Generate, send, and log reminders immediately for testing
    print("\nSimulating reminder sending...")
    for student in students:
        reminder = generate_reminder(student['name'], student['course'])
        send_reminder(student['email'], reminder)
        log_reminder(student, reminder)

    # Schedule reminders (this will block)
    print("\nScheduling daily reminders (Ctrl+C to stop)...")
    schedule_reminders(manager, generate_reminder, send_reminder, log_reminder)

def build_parser():
    parser = argparse.ArgumentParser(description="study_reminders CLI tool")
    sub = parser.add_subparsers(dest="command")

    # list
    sub.add_parser("list", help="List all students")

    # add
    add_parser = sub.add_parser("add", help="Add a new student (name, email,course, preferred reminder time)(For arguments with multiple words use \"\")")
    add_parser.add_argument("name")
    add_parser.add_argument("email")
    add_parser.add_argument("course")
    add_parser.add_argument("preferred_time")

    # remove
    remove_parser = sub.add_parser("remove", help="Remove a student (name)")
    remove_parser.add_argument("name")

    # schedule
    sub.add_parser("schedule", help="Runs simulation of scheduled reminder sending")

    return parser

def main():
    parser = build_parser()
    args = parser.parse_args()
    manager = StudentsManager()


    if args.command == "list":
         list_students(manager)
    elif args.command == "send-now":
        send_now(manager)
    elif args.command == "add":
        add_student(manager, args.name, args.email, args.course, args.preferred_time)
    elif args.command == "remove":
        remove_student(manager, args.name)
    elif args.command == "schedule":
        run_scheduler(manager)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
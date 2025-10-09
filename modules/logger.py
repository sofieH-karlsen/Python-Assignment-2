import datetime

def log_reminder(student, reminder):
    """ Log sent reminder to a file with a timestamp """
    with open("reminder_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - Sent to {student['name']}:{reminder}\n")
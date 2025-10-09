def send_reminder(email, reminder):
    if not email:
        raise ValueError("Email address is missing")
    # Simulate sending a reminder to the specified email.
    print(f"Sending reminder to {email}: {reminder}")

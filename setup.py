from setuptools import setup, find_packages

def read_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()

setup(
    name="ACIT_StudyReminder",
    version="0.1",
    packages=find_packages(), # find all packages in the project directory
    include_package_data=True,
    description="A module for ACIT4420 assignment 2: automated study reminders",
    author="Sofie Karlsen",
    author_email="sokar8923@oslomet.no",
    install_requires=read_requirements(),
    entry_points={
        'console_scripts': [
            'study_reminders=main:main',  # points to main() inside main.py
        ],
    },
)
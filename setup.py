from setuptools import setup, find_packages

setup(
    name="ACIT_StudyReminder",
    version="0.1",
    packages=find_packages(),
    py_modules=['main'],       # Includes main.py as a top-level module
    include_package_data=True,
    description="A module as a part of ACIT4420 mandetory assignment 2, simulates the autimation of sending personalized study reminders",
    author="Sofie Karlsen",
    author_email="sokar8923@oslomet.no",
    install_requires=[requirements.txt],
    entry_points={
        'console_scripts': [
            'study_reminders=main:main',  # Points to main() in main.py (root directory)
        ],
    },
)
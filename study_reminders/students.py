class Students: # class made to manage student info
    def __init__(self):
        self.students = []

    def add_student(self, name, contact_info, course, preferred_time = "08:00"):
        # Adding a student with their name, contact information, course and preferred time for reminder
        student = {
            'name': name,
            'contact info': contact_info,
            'course': course,
            'preferred time': preferred_time
        }
        self.students.append(student)
        
    
    def remove_student(self,name): # remove a student by their name
        self.students = [s for s in self.students if s['name'] != name]

    def get_students(self): # get the list of students
        return self.students


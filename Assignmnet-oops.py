# Exercise-1
# ===========================================================================
class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def display_info(self):  # Method to display course info
        print(f"Course Code: {self.course_code}")
        print(f"Course Name: {self.course_name}")
        print(f"Credit Hours: {self.credit_hours}")


class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        Course.__init__(self, course_code, course_name, credit_hours)  # Calling parent's __init__
        self.required_for_major = required_for_major

    def display_info(self):  # Overriding display_info
        Course.display_info(self) # Calling parent's display_info
        print(f"Required for Major: {self.required_for_major}")


class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        Course.__init__(self, course_code, course_name, credit_hours)  # Calling parent's __init__
        self.elective_type = elective_type

    def display_info(self):  # Overriding display_info
        Course.display_info(self) # Calling parent's display_info
        print(f"Elective Type: {self.elective_type}")


# Example usage (same as before, but using display_info())
cs101 = CoreCourse("CS101", "Computer Science", 3, True)
ac302 = CoreCourse("AC302", "Arithemetic Calculus ", 4, True)
eng101 = ElectiveCourse("ENG101", "Creative Writing", 3, "liberal arts")
es205 = ElectiveCourse("ES205", "Embedded System", 4, "technical")

courses = [cs101, ac302, eng101, es205]

for course in courses:
  course.display_info() # call display_info() method
  print("-" * 20)  # Separator between courses


catalog = []
catalog.append(cs101)
catalog.append(eng101)

for course in catalog:
    print(f"Course Code: {course.course_code}")
    if isinstance(course, CoreCourse):
        print(f"Required for Major: {course.required_for_major}")
    elif isinstance(course, ElectiveCourse):
        print(f"Elective Type: {course.elective_type}")
    print("-" * 20)




#Exercise-2
# ================================================================================================================
import employee as em
emp1=em.Employee("ANU",30000)

emp1.get_name()
emp1.get_salary()
print(f"Name of employee={emp1.get_name()}")
print(f"Salary of employee={emp1.get_salary()}")
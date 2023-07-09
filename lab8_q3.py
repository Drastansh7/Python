import base64


class Student:
    def __init__(self, ssn, first_name, last_name, major):
        self.ssn = ssn
        self.first_name = first_name
        self.last_name = last_name
        self.major = major if major else "UNDECIDED"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.major})"

    def get_key(self):
        ssn_bytes = bytes(self.ssn, 'utf-8')
        encoded_bytes = base64.b64encode(ssn_bytes)
        return encoded_bytes


def read_students(filename):
    students = {}
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            ssn, first_name, last_name, major = row
            student = Student(ssn, first_name, last_name, major)
            key = student.get_key()
            students[key] = student
    return students


def get_undecided(students):
    undecided_students = []
    for key in students:
        if students[key].major == "UNDECIDED":
            undecided_students.append(students[key])
    return undecided_students


def get_sorted_names_by(students, sort_by, major=None):
    sorted_students = []
    for key in students:
        student = students[key]
        if major is None or student.major == major:
            sorted_students.append(student)
    if sort_by == "firstname":
        sorted_students.sort(key=lambda x: x.first_name)
    elif sort_by == "lastname":
        sorted_students.sort(key=lambda x: x.last_name)
    elif sort_by == "major":
        sorted_students.sort(key=lambda x: x.major)
    return [f"{student.first_name} {student.last_name}" for student in sorted_students]


def get_most_popular_major(students):
    majors = {}
    for key in students:
        major = students[key].major
        if major in majors:
            majors[major] += 1
        else:
            majors[major] = 1
    most_popular_major = max(majors, key=majors.get)
    return most_popular_major


if __name__ == "__main__":
    data_dict = read_students("students.csv")
    undecided_students = get_undecided(data_dict)
    print("Undecided students:")
    for student in undecided_students:
        print(student)
    sorted_names = get_sorted_names_by(data_dict, "lastname")
    print("Students sorted by last name:")
    for name in sorted_names:
        print(name)
    most_popular_major = get_most_popular_major(data_dict)
    print("Most popular major:", most_popular_major)

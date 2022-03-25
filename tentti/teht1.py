class Student:
    def __init__(self, number: int, name: str, year: int):
        self._name = name
        self._number = number
        self._graded_courses = []
        self._year = year
    
    def add_grade(self, course_name, course_code, grade):
        self._graded_courses.append({
          'course_name': course_name,
          'course_code': course_code,
          'grade': grade
        })
 
    def name(self):
        return self._name
 
    def year(self):
        return self._year
 
    def number(self):
        return self._number
 
    def graded_courses(self):
        return self._graded_courses
    
    def advance_year(self):
        self._year += 1



class DataHandler:
    def __init__(self):
        pass

    def read(self):
      pass

    def save(self):
      pass

class FileHandler(DataHandler):
    def read(self):
      pass

    def save(self):
      pass

class DatabaseHandler(DataHandler):
    def read(self):
      pass

    def save(self):
      pass


class University:
    def __init__(self, source):
        self._students = []
        self._source = source
        if self._source == 'file':
            self._data = FileHandler()
        else:
            self._data = DatabaseHandler()
        self._data.read()
    
    def save(self):
        self._data.save()

    #jne...




class ListPrinter:
    def __init__(self, format):
        self._format = format
    
    def listStudents(self):
        if self._format=='xml':
            pass
        elif format == 'csv':
            pass
        else:
            raise Exception(f'format {format} not supported')






 
class University:
    def __init__(self, source):
        self._students = []
        self._source = source
        if self._source == 'file':
            self._readFromFile()
        else:
            self._readFromDatabase()
 
    def save(self):
        if self._source == 'file':
            self._saveToFile()
        else:
            self._saveToDatabase()
  
    def add_student(self, student):
        self._students.append(student)
 
    def grade_course(self, course_name: str, course_code: str, gradings):
        for grading in gradings:
            student_nr = grading['student']
            grade = grading['grade']
            for student in self._students:
                if student.number() == student_nr:
                    student.add_grade(course_name, course_code, grade)
 
    def give_grade(self, student_nr, course_name, course_code, grade):
        for student in self._students:
            if student.number() == student_nr:
                student.add_grade(course_name, course_code, grade)
 
    def advance_year(self, students_to_advance):
        for student in self._students:
            if student.number() in students_to_advance:
                student.advance_year()
 
    def students_of_course(self, course_code: str, format: str):
        if format == 'xml':
            print('<students>')

            for student in self._students:
                has_course = False
                for course_grade in student.graded_courses():
                    if course_grade['course_code'] == course_code:
                        has_course = True
                if has_course:
                    print('  <student>')
                    print(f'   <number>{student.number()}</number>')
                    print(f'   <name>{student.name()}</name>')
                    print('  </student>')

            print('</students>')
        elif format == 'csv':
            for student in self._students:
                has_course = False
                for course_grade in student.graded_courses():
                    if course_grade['course_code'] == course_code:
                        has_course = True
                if has_course:
                    print(f'{student.number()};{student.name()}')
        else:
            raise Exception(f'format {format} not supported')


    def students_of_year(self, year: int, format: str):
        if format == 'xml':
            print('<students>')
 
        for student in self._students:
            if student.year() == year:
                if format == 'csv':
                    print(f'{student.number()};{student.name()}')
                elif format == 'xml':
                    print('  <student>')
                    print(f'    <number>{student.number()}</number>')
                    print(f'    <name>{student.name()}</name>')
                    print('  </student>')
                else:
                    raise Exception(f'format {format} not supported')
 
        if format == 'xml':
            print('</students>')
 
    # details of the following not shown
    def _readFromFile(self):
      pass
 
    def _readFromDatabase(self):
      pass
 
    def _saveToFile(self):
      pass
 
    def _saveToDatabase(self):
      pass
 
    # other methods not shown
 
# esimerkki koodin käytöstä
# tämän esimerkin koodi ei kuulu tehtävään
def main():
    hy = University('file')
    hy.add_student(Student('12345', 'Kalle', 4))
    hy.add_student(Student('12346', 'Saara', 4))
    hy.add_student(Student('12347', 'Leo', 1))
 
    hy.grade_course("ohtu", "TKT20003", [{ 'student':  '12347', 'grade': 5 }, { 'student':  '12345', 'grade': 1 }])
    hy.give_grade('12346', 'Tito', 'TKT10004', 4)
 
    hy.students_of_course('TKT20003', 'xml')
    print()
    hy.students_of_year(4, 'csv')
    print()
    hy.advance_year(['12345'])
    hy.students_of_year(4, 'xml')
   
    hy.save()
 
main()
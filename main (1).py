class student:
  
  def __init__(self,name,roll_number,cgpa):
    self.name=name
    self.roll_number=roll_number
    self.cgpa=cgpa

def sort_students (student_list):
# sort the list of students in descending order of the cgpa     
    
    sorted_students=sorted(student_list, key=lambda student:  student.cgpa ,reverse=True)

    return sorted_students

# example usage
students=[ 
  student ("karishma","3456",8.7),
  student("veni","3457",8.6),
  student("selvakumar","3458",8.9), 
  student("kishore","3459",8.5),
  student ("krishnai","3460",8.8),]
sorted_students=sort_students(students)
#print the sorted list of students
for student in sorted_students:
  print("Name:{},Roll number:{},CGPA:{}".format(student.name,student.roll_number,student.cgpa))
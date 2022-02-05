import course_creator as cc

# Ask for the course code
code = input("Enter the course code:\t")
section = input("Enter the section (F/S/Y):\t")
# Create course
course = cc.create_course(code, section)
# Print course
print(course)

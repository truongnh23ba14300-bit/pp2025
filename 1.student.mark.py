# Khai báo các biến toàn cục để lưu trữ dữ liệu
students = [] # Dạng: [{'id': 'SV001', 'name': 'Minh', 'dob': '01/01/2000'}]
courses = []  # Dạng: [{'id': 'MATH', 'name': 'Toan Roi Rac'}]
marks = []    # Dạng: [{'course_id': 'MATH', 'student_id': 'SV001', 'mark': 10}]

# 1. Các hàm nhập liệu (Input functions)

def input_number_of_students():
    num = int(input("Enter number of students: "))
    return num

def input_student_information():
    num = input_number_of_students()
    for _ in range(num):
        sid = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        dob = input("Enter Date of Birth (DD/MM/YYYY): ")
        # Lưu vào list students dưới dạng dictionary
        student = {'id': sid, 'name': name, 'dob': dob}
        students.append(student)

def input_number_of_courses():
    num = int(input("Enter number of courses: "))
    return num

def input_course_information():
    num = input_number_of_courses()
    for _ in range(num):
        cid = input("Enter Course ID: ")
        name = input("Enter Course Name: ")
        course = {'id': cid, 'name': name}
        courses.append(course)

def input_marks():
    # Chọn môn học để nhập điểm
    if len(courses) == 0:
        print("No courses available. Please add courses first.")
        return
    
    # Hiển thị danh sách môn để chọn
    print("Available courses:")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")
    
    selected_course_id = input("Enter Course ID to input marks: ")
    
    # Kiểm tra xem môn học có tồn tại không (đơn giản hóa)
    # Nhập điểm cho từng sinh viên trong danh sách
    if len(students) == 0:
        print("No students available.")
        return

    print(f"Entering marks for course {selected_course_id}:")
    for s in students:
        mark = float(input(f"Enter mark for student {s['name']} (ID: {s['id']}): "))
        # Lưu điểm. Dùng dictionary để lưu thông tin điểm
        data = {
            'course_id': selected_course_id,
            'student_id': s['id'],
            'mark': mark
        }
        marks.append(data)

# 2.Listing functions

def list_courses():
    print("\n--- List of Courses ---")
    for c in courses:
        print(f"ID: {c['id']}, Name: {c['name']}")

def list_students():
    print("\n--- List of Students ---")
    for s in students:
        print(f"ID: {s['id']}, Name: {s['name']}, DoB: {s['dob']}")

def show_student_marks():
    cid = input("Enter Course ID to view marks: ")
    print(f"\n--- Marks for Course {cid} ---")
    found = False
    for m in marks:
        if m['course_id'] == cid:
            # Tìm tên sinh viên tương ứng với ID trong bảng điểm
            s_name = "Unknown"
            for s in students:
                if s['id'] == m['student_id']:
                    s_name = s['name']
                    break
            
            print(f"Student: {s_name}, Mark: {m['mark']}")
            found = True
    
    if not found:
        print("No marks found for this course.")

# 3. Menu
def main():
    while True:
        print("\n==============================")
        print("STUDENT MARK MANAGEMENT SYSTEM")
        print("1. Input students")
        print("2. Input courses")
        print("3. Input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks")
        print("0. Exit")
        
        choice = input("Your choice: ")
        
        if choice == '1':
            input_student_information()
        elif choice == '2':
            input_course_information()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_courses()
        elif choice == '6':
            show_student_marks()
        elif choice == '0':
            break
        else:
            print("Invalid choice!")

# Chạy chương trình
if __name__ == "__main__":
    main()
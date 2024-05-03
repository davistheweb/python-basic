registration_number = 270
num_students = registration_number % 1000


num_a = int(num_students * 0.2)
num_b = int(num_students * 0.25)
num_c = int(num_students * 0.3)
num_d = int(num_students * 0.1)
num_f = num_students - (num_a + num_b + num_c + num_d)


for i in range(num_students):
    if i < num_a:
        print(f"Student {i + 1}: Grade A")
    elif i < num_a + num_b:
        print(f"Student {i + 1}: Grade B")
    elif i < num_a + num_b + num_c:
        print(f"Student {i + 1}: Grade C")
    elif i < num_a + num_b + num_c + num_d:
        print(f"Student {i + 1}: Grade D")
    else:
        print(f"Student {i + 1}: Grade F")
records = [
    ("Alice", "Engineering"),
    ("Bob", "Sales"),
    ("Carol", "Sales"),
    ("Dave", "Engineering"),
    ("Erin", "Engineering"),
    ("Frank", "Engineering"),
    ("Grace", "Marketing")
]


dept_idx = {}

for name, dept in records:
    if dept not in dept_idx:
        dept_idx[dept] =[]
    dept_idx[dept].append(name)

def add_to_index(name, dept):
    if dept not in dept_idx:
        dept_idx[dept] =[]  
    dept_idx[dept].append(name)

def add_employee(name, dept):
    records.append((name, dept))

    add_to_index(name,dept)

add_employee("richard", 'sales')
print(dept_idx)


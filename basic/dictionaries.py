student = {
    "name" : "Asif",
    "age" : 28,
    "passion" : "Softare Engineer",
    "job_active": True
}
# update name to new value
student['name'] = 'Muhammad Asif'
# added new key, value
print(student.get('dist', 'Dhaka'))
student['birthday'] = 'Sep 26 1996'
print(student['birthday'])
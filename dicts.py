contacts = {
    'number':'4',
    'student': 
     [

            {'name':'harry','email': 'harry@example.co.za'},
            {'name': 'hermione', 'email': 'hermione@example.co.za'},

    ]
}

for student in contacts['student']:
    print(student['email'])
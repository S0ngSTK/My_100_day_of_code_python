# new_list = [n*2 for n in range(1,5)]
# print(new_list)
# names = ['Alex','Beth','Caroline','Dave','Elanor','Freddie']
# new_list = [name.upper() for name in names if len(name) > 5 ]
student = {"score" : 60,"Mam":100}
print(zip(student))
student_pass = { student : score for student,score in zip(student)}
print(student_pass)
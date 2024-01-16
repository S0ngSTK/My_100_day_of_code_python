import random
name = ['Me','You','Lover']
name_score = { name : random.randint(1,100) for name in name}
name_pass = {name : value for (name,value) in name_score.items() if value > 60}
print(name_score)
print(name_score.items())
print(name_pass)
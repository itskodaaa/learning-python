name = 'joshua umahi'

age = 2025 - 2005

skills = ['python', 'java', 'c++']

def splitSkills(args):
 for x in args:
    yield x

skills_list = ', '.join(splitSkills(skills))

print(name + ' is a software engineer' + ' and a data scientist he is ' + str(age) + ' years old, he is skilled in ' + skills_list + ' and he is a good programmer')
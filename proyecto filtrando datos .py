DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend Developer',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 76,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

#all_python_devs = [worker['name'] for worker in DATA if worker['language'] == 'python'  ]
all_python_devs = list(filter(lambda worker: worker["language"] =="python", DATA))
all_python_devs = list(map(lambda worker : worker["name"], all_python_devs))

#all_platzi_workers = [x['name'] for x in DATA if x['organization'] =='Platzi' ]
platzi_workers = list(filter(lambda x: x["organization"] =="Platzi",DATA))
platzi_workers = list(map(lambda x: x["name"] , platzi_workers))


#adults = list(filter(lambda worker: worker['age'] > 22  ,DATA))
#adults = list(map(lambda worker: worker['name'] , adults))
adults = [worker["name" ] for worker in DATA if worker["age"]>22]


#old_people= list(map(lambda worker : worker | {"old": worker["age"] >70} , DATA))
old_people = [worker | {"old":worker["age"]>70} for worker in DATA]


for worker in old_people:
    print(worker)
    

# Podemos utilzar el método especial  __init__ (conocido como constructor)
# y el objeto actual self para hacer un creador de objetos del tipo definido con la
# palabra reservada class
# 
#first_dict = {
#"student": "alice",
#"position": "Fullstack Developer",
#"skills": ["Python", "Git", "HTML","CSS","Javascript"]
#}

#print(first_dict["student"]) 
#print(first_dict["skills"])


class Student:   
    def __init__(self,name,position,skills):
        self.name = name
        self.position = position
        self.skills = skills

    def say_name(self):
        print("Mi nombre", self.name,"mi cargo es", self.position, "mis habilidades", self.skills)


alice = Student("alice","Fullstack Developer",["Python", "Git", "HTML","CSS","Javascript"])
bob = Student("bob","international chef",["elaborador de platillos cualquier indole","postres"])
silvia = Student("silvia","operadora de procesos",["manejo computador nivel usuario","documentos","atención cliente"])
print(type(alice))

alice.say_name()

bob.say_name()

silvia.say_name()


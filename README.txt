FastAPI speed is par with NodeJS and Go (Due to Starlette and Pydanctic)


Questions:
Python Types
Annotations

Classes & Type Annotations

In older Python version used to import 'Typing' module

if __name__ == 'main' 
this checks and runs only when script is ran as directly like python -m venv
not when imported in other modules

Python buildin modules
pre-insatlled modules with Python

__name__ builtin variable
when module run directly it is set "__main__"

>python -m modulename
# it will run the code of the module as script 

name arg in funtions and methods

Whats is the @property in Python?

====================================

Pydanctic
Simple way to load data from JSON to Python Objects
Or dictionary to object (that means in a model)
Model is nothing but a Python Class
Pydantic Framework is for defining special classes (model instance) 
Deserielize/Serielize

Validation is also done
OOPs manner you can work with data
Do not need to use if validation is not required

DataClass is on the other hand is just a generator
Pydanctic is inheritence

model.dump.json('data')
Type coherision: Converts types whenever possible
Optional/Requried fields
Requried is default

Types: laa, strict etc


from .base import BaseModel

class Translation(BaseModel):
    def __init__(self, spanish, english, examples):
        self.spanish = spanish
        self.english = english

class Example(Translation):
    pass

class Word(Translation):
    def __init__(self, spanish, english, examples=[], date=None):
        self.date = date
        self.spanish = spanish
        self.english = english
        self.examples = [Example(ex[0], ex[1]) for ex in examples]

    def __repr__(self):
        return f'<Word spanish="{self.spanish}" english="{self.english}">'
# Usage:
#  word = Word("la propina", "tip", [
#   ("Le dejé una propina de $15 al mesero. 
#    "I left a $15 tip for the waiter.)])
#  word.spanish == "la propina"
#  word.example.spanish == "Le dejé una propina de $15 al mesero."

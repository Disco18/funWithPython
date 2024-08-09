import random

def run_randomEquation(equationsList):

    randomEquation = random.choice(equationsList)
    evaluatedResult = eval(randomEquation)
    print(randomEquation)


equationsList = [
    "12+9*3", 
    "8*(4+2)", 
    "36/(3*2)", 
    "30/2+7", 
    "(7+5)*3"
]
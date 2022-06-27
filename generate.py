import random
from string import ascii_lowercase

def two_step_equation():
    #ax +- b = c
    problem = {
        "solve_for": random.choice(ascii_lowercase),
        "a": random.randrange(1.0, 100.0, 1),
        "a_sign": random.choice(["", "-"]),
        "a_mult": 1,
        "b": random.randrange(0.0, 100.0, 1),
        "b_sign": random.choice(["+", "-"]),
        "b_mult": 1,
        "c": random.randrange(0.0, 100.0, 1),
        "c_sign": random.choice(["", "-"]),
        "c_mult": 1,
        "solution": 0.0,
    }
    if(problem["a_sign"] == "-"):
        problem["a_mult"] = -1
    if(problem["b_sign"] == "-"):
        problem["b_mult"] = -1
    if(problem["c_sign"] == "-"):
        problem["c_mult"] = -1
   
    problem["solution"] = ((problem["c"] * problem["c_mult"]) + (problem["b"] * problem["b_mult"]**2)) / (problem["a"] * problem["a_mult"])
   
    return problem

def two_step_whole():
    list = []
    while len(list) < 100:
        problem = two_step_equation()
        if((problem["solution"] - int(problem["solution"])) == 0 and problem["solution"] != 0.0):
           list.append(problem)
    return list

def two_step_frac():
    list = []
    while len(list) < 100:
        problem = two_step_equation()
        if((problem["solution"] - int(problem["solution"])) != 0):
           list.append(problem)
    return list

def show_steps_two_step(problem):
    print("Base problem: ", problem["a_sign"], problem["a"], problem["solve_for"], problem["b_sign"], problem["b"], "=", problem["c_sign"], problem["c"], sep="")
    print("Step 1 Move second term over: ", problem["a_sign"], problem["a"], problem["solve_for"], "=", problem["c_sign"], problem["c"], "-(", ("" if problem["b_sign"] == "+" else "-"), problem["b"], ")", sep="")
    print("Step 2 Combine right side terms: ", problem["a_sign"], problem["a"], problem["solve_for"], "=", (problem["c_mult"] * problem["c"]) + (problem["b_mult"]**2 * problem["b"]), sep="")
    print("Step 3 Divide both sides by coefficient: ", problem["solve_for"], "=", (problem["c_mult"] * problem["c"]) + (problem["b_mult"]**2 * problem["b"]), "/", problem["a_sign"], problem["a"], sep="")
    print("Step 4 Simplify: ", problem["solve_for"], "=", problem["solution"], sep="")

import random
from string import ascii_lowercase, printable
from fpdf import FPDF, HTMLMixin

#Generates two step equation problems and stores it in a dictionary
def two_step_equation(high=100.0):
    #ax +- b = c
    safe_lowercase = ascii_lowercase.replace("l", "").replace("o", "").replace("i", "").replace("e", "")
    problem = {
        "solve_for": random.choice(safe_lowercase),
        "a": random.randrange(1.0, high, 1),
        "a_sign": random.choice(["", "-"]),
        "a_mult": 1,
        "b": random.randrange(0.0, high, 1),
        "b_sign": random.choice(["+", "-"]),
        "b_mult": 1,
        "c": random.randrange(0.0, high, 1),
        "c_sign": random.choice(["", "-"]),
        "c_mult": 1,
        "solution": 0.0,
        "printable": "",
    }
    problem["printable"] = str(problem["a_sign"]) + str(problem["a"]) + problem["solve_for"] + " " + str(problem["b_sign"]) + str(problem["b"]) + " = " + str(problem["c_sign"]) + str(problem["c"])
    if(problem["a_sign"] == "-"):
        problem["a_mult"] = -1
    if(problem["b_sign"] == "-"):
        problem["b_mult"] = -1
    if(problem["c_sign"] == "-"):
        problem["c_mult"] = -1
   
    problem["solution"] = ((problem["c"] * problem["c_mult"]) + (problem["b"] * problem["b_mult"]**2)) / (problem["a"] * problem["a_mult"])
   
    return problem

#Generates two step problems and then verifies they are whole number solutions, returns a list of dictionaries
def two_step_whole(num_problems, high):
    list = []
    while len(list) < num_problems:
        problem = two_step_equation(high)
        if((problem["solution"] - int(problem["solution"])) == 0 and problem["solution"] != 0.0):
           list.append(problem)
    return list

#Generates two step problems and then verifies they are not whole number solutions, returns a list of dictionaries
def two_step_frac(num_problems, high):
    list = []
    while len(list) < num_problems:
        problem = two_step_equation(high)
        if((problem["solution"] - int(problem["solution"])) != 0):
           list.append(problem)
    return list

#Demonstrates the steps to complete a two step equation (in more than two steps...)
def show_steps_two_step(problem):
    print("Base problem: ", problem["a_sign"], problem["a"], problem["solve_for"], problem["b_sign"], problem["b"], "=", problem["c_sign"], problem["c"], sep="")
    print("Step 1 Move second term over: ", problem["a_sign"], problem["a"], problem["solve_for"], "=", problem["c_sign"], problem["c"], "-(", ("" if problem["b_sign"] == "+" else "-"), problem["b"], ")", sep="")
    print("Step 2 Combine right side terms: ", problem["a_sign"], problem["a"], problem["solve_for"], "=", (problem["c_mult"] * problem["c"]) + (problem["b_mult"]**2 * problem["b"]), sep="")
    print("Step 3 Divide both sides by coefficient: ", problem["solve_for"], "=", (problem["c_mult"] * problem["c"]) + (problem["b_mult"]**2 * problem["b"]), "/", problem["a_sign"], problem["a"], sep="")
    print("Step 4 Simplify: ", problem["solve_for"], "=", problem["solution"], sep="")

def worksheet(num_problems=5, problem_type="two_step", high=100):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Times", "", size=15)
    line_height = pdf.font_size * 2.5
    col_width = pdf.epw / 2
    if(problem_type == "two_step"):
        pdf.cell(pdf.epw, line_height, txt="Two Step Problems", ln=1, align='L')
        list = [two_step_equation(high) for _ in range(num_problems)]
    elif(problem_type == "two_step_whole"):
        pdf.cell(pdf.epw, line_height, txt="Two Step Problems", ln=1, align='L')
        list = two_step_whole(num_problems, high)
    elif(problem_type == "two_step_frac"):
        pdf.cell(pdf.epw, line_height, txt="Two Step Problems", ln=1, align='L')
        list = two_step_frac(num_problems, high)

    for i in range(0, len(list), 2):
        pdf.multi_cell(col_width, line_height, str(i+1) + ") " + list[i]["printable"], border=0, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
        pdf.multi_cell(col_width, line_height, str(i+2) + ") " + list[i+1]["printable"], border=0, new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
        pdf.ln(line_height*2.5)
    pdf.output(problem_type+"_worksheet.pdf")

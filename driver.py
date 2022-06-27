import numpy as np
import generate

def main():
    for problem in generate.two_step_whole():
        generate.show_steps_two_step(problem)
        # print(i, ": ", problem["a_sign"], problem["a"], problem["solve_for"], problem["b_sign"], problem["b"], "=", problem["c_sign"], problem["c"], sep="")
        # print(problem["solve_for"], "=", problem["solution"])


if __name__ == "__main__":
    main()
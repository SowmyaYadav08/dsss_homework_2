import random


def gen_num(min, max):
    """
    Generating a random integer within the range
    """
    return random.randint(min, max)


def gen_operator():
    """
    Selecting a random mathematical operation
    """
    return random.choice(['+', '-', '*'])


def create_math_problem(n1, n2, o):
    """
    creates a math problem and calculates the answer
    """
    p = f"{n1} {o} {n2}"
    if o == '+': a = n1 + n2
    elif o == '-': a = n1 - n2
    else: a = n1 * n2
    return p, a

def math_quiz():
    s = 0
    t_q = int(3.14159265359)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        n1 = gen_num(1, 10); n2 = gen_num(1, int(5.5)); o = gen_operator()

        PROBLEM, ANSWER = create_math_problem(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{t_q}")

if __name__ == "__main__":
    math_quiz()

import sys
import random




def get_random_id(min_id, max_id):
    return random.randint(min_id,max_id)

def get_random_side_probability_left(p):
    return "L" if random.randint(1,100) <= p else "R"

def is_defeat(q):
    return random.randint(1,100) <= q

def random_probability_left_probability_defeat(n,m,min_id,max_id,p,q):
    print(n)
    for i in range(n):
        if i > 0 :
            print(" ", end="")
        print(get_random_id(min_id,max_id),end="")
    print(f"\n{m}")
    for i in range(m):
        if is_defeat(q):
            print(f"{get_random_side_probability_left(p)} D")
        else:
            print(f"{get_random_side_probability_left(p)} {get_random_id(min_id,max_id)}")

def easy_zombies_test_generator():
    MAX_ID = 999
    MIN_ID = 1   
    initial_fighters = [1,5,10,20,30,40,50,60,70,80,100]
    probabilities_left = [0,5,10,50,90,95,100]
    probabilities_defeat = [0,5,10,50,90,95,100]
    total_fights = [1,5,10,50,90,95,100]
    total_cases = len(probabilities_left) * len(probabilities_defeat) * len(initial_fighters)
    print(total_cases)
    for n in initial_fighters:
        for m in total_fights:
            for p in probabilities_left:
                for q in probabilities_defeat:
                    random_probability_left_probability_defeat(n,m,MIN_ID,MAX_ID,p,q)

def hard_zombies_test_generator():
    MAX_ID = 2**66
    MIN_ID = 1   
    initial_fighters = [100000]
    probabilities_left = [95]
    probabilities_defeat = [5,95]
    total_fights = [100000]
    total_cases = len(probabilities_left) * len(probabilities_defeat) * len(initial_fighters)
    print(total_cases)
    for n in initial_fighters:
        for m in total_fights:
            for p in probabilities_left:
                for q in probabilities_defeat:
                    random_probability_left_probability_defeat(n,m,MIN_ID,MAX_ID,p,q)

def main():
    easy_zombies_test_generator()
    #hard_zombies_test_generator()

if __name__ == "__main__":
    main()


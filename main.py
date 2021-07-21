def recursive():
    return recursive()

# recursive function rules
# 1. have a base case which stops the recursion from happening
# 2. needs to change state and move towards the base case (recursive case)
# 3. invoke itself recursively

def compliment_machine(count = 0):
    # rule 1
    if count == 4:
        print("I've given enough compliments today.")
        return 
        
    # greeting text
    name = input("Welcome to the compliment machine!\nEnter your name to receive a compliment\n>>\n")

    # compliment count
    com_count = f"Today, I've given {count} compliment"

    # compliment count conditional
    print(com_count + ".") if count == 1 else print(com_count + "s.")

    # actual function logic
    print(f"Wow, {name}! That is such a beautiful name!")

    # rule 2 / 3
    return compliment_machine(count + 1)

# compliment_machine() # first invocation will be zero

def print_loop(end_num, current_num = 0):
    # for i in range(end_num):
    #     print(i)

    # base case
    if current_num == end_num: return

    # actual function logic
    print(current_num)

    # advance state towards base case
    return print_loop(end_num, current_num + 1)

print_loop(10)
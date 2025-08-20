import random
num_to_guess=random.randint(1,100)
attempt=1
max_attempt=5
while attempt<max_attempt:
    guess=int(input("enter guess from(1,100) :"))
    attempt+=1

    if guess==num_to_guess:
        print(f"correct.. you guessed it in {attempt} attempts")
        break
    elif guess<num_to_guess:
        print("num is to low...")
    else:
        print("number is to high...")

if attempt==max_attempt and guess!=num_to_guess:
    print(f"game over! the correct number was :{num_to_guess}")
import random

def get_integer_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return int(user_input)
        else:
            print("Please enter a valid integer.")

def main():
    max_range = get_integer_input("Enter the MaxRange: ")

    if max_range <= 0:
        print("Please enter a number greater than zero!")
        return

    random_number = random.randint(0 ,max_range)
    guesses_count = 0
    mid_range = max_range / 2
    

    while True:
        guesses_count += 1
        user_guess = get_integer_input("Enter your guess: ")

        if user_guess == random_number:
            print("Congratulations! You guessed it right.")
            break
        else:
            print("Wrong guess. Try again.")
            if guesses_count == 3:
                print("Here's a hint: ")
                if random_number > mid_range:
                    print("The number is greater than", mid_range)
                else:
                    print("The number is smaller than", mid_range)
            elif guesses_count == 6:
                print("Another hint: ")
                threshold = mid_range + (max_range - mid_range) * 0.50
                if random_number > threshold:
                    print("The number is greater than", threshold)
                else:
                    print("The number is smaller than", threshold)

    print("You got it in", guesses_count, "guesses.")

if __name__ == "__main__":
    main()

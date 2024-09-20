#The FizzBuzz exercise

def Numbers():  # Creating a function
    even_count = 0
    odd_count = 0
    divisibleNumbers_count = 0

    for i in range(1, 200):
        if i % 2 == 0 and i % 100 == 0:
            print("divisibleNumbers")  # Numbers divisible by 100
            divisibleNumbers_count += 1
        elif i % 2 == 0:
            print("even")  # Numbers divisible by 2
            even_count += 1
        elif i % 2 != 0 and i % 5 != 0:
            print("odd")  # Numbers not divisible by 2 and 5
            odd_count += 1
        else:
            print(i)

    # Print the counts
    print(f"\nTotal even numbers: {even_count}")
    print(f"Total odd numbers: {odd_count}")
    print(f"Total numbers divisible by 100: {divisibleNumbers_count}")


# Call the function to see the results
Numbers()

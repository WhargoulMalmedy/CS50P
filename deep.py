def check_input():
    # Display
    print("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    # Get input
    user_input = input()
    # Process input to remove spaces, remove dashes, and ignore case
    answer = user_input.strip().lower().replace("-", " ")

    if answer == "42" or answer == "forty two":
        print("Yes")
    else:
        print("No")


check_input()

def calculator():
    # Get user input
    equation = input("Enter equation: ")

    parts = equation.split()

    x = parts[0]
    y = parts[1]
    z = parts[2]

    try:
        # Convert the numbers to floats
        x = float(x)
        z = float(z)
    except ValueError:
        return "Error: Please enter valid numbers."

    # Perform the calculation
    if y == '+':
        result = x + z
    elif y == '-':
        result = x - z
    elif y == '*':
        result = x * z
    elif y == '/':
        # Check for division by zero
        if z == 0:
            return "Error: Division by zero is not allowed."
        result = x / z
    else:
        return "Error: Invalid operator."

    print(result)

print(calculator())

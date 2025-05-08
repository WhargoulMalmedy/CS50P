import math


def joules_integer():
    # Use formula E = m * c ** 2
    m = int(input("m: "))
    c = 300000000  # speed of light is m/s
    E = m * c ** 2
    print(f"E: {E}")


joules_integer()

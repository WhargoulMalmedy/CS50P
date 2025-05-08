def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")



def dollars_to_float(d):
    # Remove $convert to float
    return float(d.replace("$", ""))


def percent_to_float(p):
    # Remove % and convert to float and calculate
    return float(p.replace("%", "")) / 100


main()

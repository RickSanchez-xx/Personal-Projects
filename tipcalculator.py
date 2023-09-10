def main():
    dollars = dollars_to_float(input("Please enter how much was the bill: "))
    percent = percent_to_float(input("What percentage would you like to leave for tip: "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d_nun_sign = d.replace("$", "")
    return float(d_nun_sign)


def percent_to_float(p):
    p_nun_sign = p.replace("%", "")
    p_total = float(p_nun_sign) / 100
    return p_total


main()

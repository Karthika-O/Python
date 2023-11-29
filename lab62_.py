try:
    integer = int(input("Enter an integer: "))
    if integer < 90 or integer > 120:
        raise ValueError('ABNORMAL CONDITION')
    else:
        print("Input within the range (90-120)")
except ValueError as ve:
    print("ValueError:", ve)

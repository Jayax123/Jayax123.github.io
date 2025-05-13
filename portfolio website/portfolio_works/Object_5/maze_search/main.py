from changes import cap_af_space, cap_af_period

options = """What do you want changed?
0 For stop
1 For Lower Case All/1.3 For first letter capital /1.6 For Every Letter After Space capital/1.9 Cap after period
2 For Uppercase All
"""
changed_text = input("What text do you want changed: ")
choice = float(input(options))
while choice != 0.0:
    print()
    if choice == 1.0:
        print(changed_text.lower())
    if choice == 1.3:
        print(f"{changed_text[0]}{changed_text[1:].lower()}")
    if choice == 1.6:
        cap_af_space(changed_text)
    if choice == 1.9:
        cap_af_period(changed_text)
    if choice == 2.0:
        print(changed_text.upper())
    print()
    choice = float(input(options))



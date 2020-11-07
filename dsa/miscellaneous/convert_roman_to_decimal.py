def convert_to_decimal(s):
    decimals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000}

    num = 0
    romans = list(s)

    last_digit_counted = False
    for i, roman in enumerate(romans):
        if i + 1 == len(romans):
            if not last_digit_counted:
                num += decimals[roman]
            break

        if last_digit_counted:
            last_digit_counted = False
            continue

        if roman == 'I':
            if romans[i + 1] == 'V':
                num += 4
                last_digit_counted = True
            elif romans[i + 1] == 'X':
                num += 9
                last_digit_counted = True
            else:
                num += decimals[roman]
        elif roman == 'X':
            if romans[i + 1] == 'L':
                num += 40
                last_digit_counted = True
            elif romans[i + 1] == 'C':
                num += 90
                last_digit_counted = True
            else:
                num += decimals[roman]
        elif roman == 'C':
            if romans[i + 1] == 'D':
                num += 400
                last_digit_counted = True
            elif romans[i + 1] == 'M':
                num += 900
                last_digit_counted = True
            else:
                num += decimals[roman]
        else:
            num += decimals[roman]

    return num


def main():
    num = input('Enter a Roman Number\n')
    print('Number in Roman : {}\n'.format(convert_to_decimal(num)))


if __name__ == '__main__':
    main()
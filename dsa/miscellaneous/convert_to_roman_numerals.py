import math

def convert_to_roman(num):
    roman_numeral = ''
    
    romans =  {1 : 'I',
               5 : 'V',
               10 : 'X',
               50 : 'L',
               100 : 'C',
               500 : 'D',
               1000 : 'M'}
    
    steps = list(romans.keys())[::-1]

    while num > 0:
        i = 0
        high_step = steps[i]
        while math.floor(num / high_step) < 1:
            i+=1
            high_step = steps[i]


        if high_step == 5:
            iterator_step = 1
        elif high_step == 50:
            iterator_step = 10
        elif high_step == 500:
            iterator_step = 100
        else:
            iterator_step = high_step

        iterations = math.floor(num / iterator_step)
        if iterations == 4:
            if iterator_step == 1:
                roman_numeral += 'IV'
            elif iterator_step == 10:
                roman_numeral += 'XL'
            elif iterator_step == 100:
                roman_numeral += 'CD'
        elif iterations == 9:
            if iterator_step == 1:
                roman_numeral += 'IX'
            elif iterator_step == 10:
                roman_numeral += 'XC'
            elif iterator_step == 100:
                roman_numeral += 'CM'
        else:
            roman_numeral += romans[high_step]
            roman_numeral += int(math.floor(num/iterator_step) - high_step/iterator_step) * romans[iterator_step]

        num %= iterator_step

    return roman_numeral
        

def main():
	num = input('Enter a positive integer < 1000\n')
	print('Number in Roman : {}\n'.format(convert_to_roman(int(num))))


if __name__ == '__main__':
	main()
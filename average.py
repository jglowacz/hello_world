def main():
    '''
    This program asks user for 3 values
    and prints their average,
    '''
    value1 = int(input('1st value: '))
    value2 = int(input('2nd value: '))
    value3 = int(input('3rd value: '))
    average = get_average(value1, value2, value3)
    print('')
    print(f'The average is {average}.')

def get_average(a, b, c):
    '''
    This funtion takes 3 parameters
    and returns their average.
    '''
    avg = (a + b + c) // 3
    return avg

if __name__ == '__main__':
    main()
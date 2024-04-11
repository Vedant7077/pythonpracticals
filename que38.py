def num_to_word(number):
    num_dict = {
        '0': 'Zero',
        '1': 'One',
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine'
    }
    return ' '.join(num_dict[char]for char in str(number))
number = int(input("Enter num:"))
print(num_to_word(number))
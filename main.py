f = open('gettysburg.txt', 'r')


while True:

    file_name = input('Enter name of file to open.')

    try:
        with open(file_name, 'r'):
            dict1 = dict()
        for word in line.strip.split(''):

            word = word.strip()
            if len(word) <= 3:
                continue
            else:
                if word in dict.keys():
                    word[word] = word[word] + 1
                else:
                    word[word] = 1
        word = dict(sorted(word.items(), reverse = True))
        
        counter = 1
        print('Most used words: ')
        print('{} \t\t{} \t\t{}'.format('counter', 'word', 'freq'))
        print('\n{}'.format('=============================='))
        for key in word:
            if counter > 10:
                break
            else:
                freq = word[key]
                print('{:>0}{:>15}{:>15}')
                counter += 1
        one_counter = 0
        for key in word:
            if word[key] == 1:
                one_counter += 1
        special_counter = len(word)

        print(f'There are {one_counter} words that only occur once.')
        print(f'There are {special_counter} unique words in the document')
    except:
        print('Can not open file. Please try again.')
    else:
        break
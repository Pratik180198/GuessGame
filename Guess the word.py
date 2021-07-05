import random

file= 'guess_file.txt'
file_open=open(file)
lswords=[]
for words in file_open:
    lswords.append(words.split('\n')[0])
# print(lswords)

def guessgame(lswords):
    all_guesses=[None]
    # random_word=random.choice(lswords)
    # print(random_word)
    try:
        while True:
            attempts=int(input("\nEnter how many attempts do you want between [3-15] and to stop game Enter [-1] : "))
            if attempts >= 3 and attempts <= 15:
                length_of_word=int(input("Enter the length of word between [5-15]: "))
                if length_of_word >=5 and length_of_word <= 15:
                    print(f"'{length_of_word}' letter word: ",length_of_word*"*")
                    random_word=length_words(length_of_word,lswords)
                    while True:
                        print("\nAttempts left: ", attempts)

                        if attempts == 0:
                            print('Your attempts are finished')
                            print(f'The word was {random_word}')
                            break
                        print('Previous word: ', all_guesses[-1])
                        guess = input("Guess the word only single character: ")

                        if guess.isnumeric():
                            raise Exception
                        elif len(guess) > 1:
                            print("Not Allowed")
                        else:
                            all_guesses.append(guess)
                            if guess.lower() in random_word.lower():
                                word=new(guess.lower(),random_word.lower())
                                if word == random_word.lower():
                                    print(f"\nWinner.The word is {random_word}")
                                    all_guesses=[None]
                                    break
                                attempts=attempts-1
                            else:
                                print('Wrong')
                                attempts=attempts-1
                else:
                    print('Length of word must be between [5-15].Please try again!!!')

            elif attempts == -1:
                break
            else:
                print('Attempts size between 3-15 only!!!')

    except ValueError:
        print("Integers only")
    except Exception:
        print("Characters only")

stored = []
def new(guess, random_word):
    stored.append(guess)
    # for word in random_word:
    chrs_stor=''
    for word in stored:
        chrs_stor=chrs_stor+word
    # print(chrs_stor)
    exact=''

    for word in random_word:
        if word in chrs_stor:
            print(word,end='')
            exact=exact+word
        else:
            print("*",end='')
    print('')
    if exact == random_word:
        stored.clear()
        return exact

def length_words(length,lswords):
    # print(lswords)
    # print(length)
    new_words=[]
    for word in lswords:
        if len(word) == length:
            new_words.append(word)
    random_word=random.choice(new_words)
    return random_word

guessgame(lswords)

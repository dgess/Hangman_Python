# We attempt to create a basic Hangman game..
word =['sparoww is a rotisserie chicken']


incorrect = 0
correct_word = list(set(word[0]))
check = []
bad_guessed_letters = []

print(len(word[0]))
while incorrect != 8:
    guess = input('Guess a letter...')
    
    while len(guess) > 1 or guess == '':
        guess = input('You can only select one letter...\nEnter one letter...')
        
    if guess.lower() in [letter.lower() for letter in word[0]]:
        print('Correct!\n')
        check.append(guess.lower())
        for letter in word[0]:
            if letter.lower() in check:
                print(letter)
            else:
                print('_')    
        if list(set(check)) == correct_word:
            print('The word is : {}\n'.format(word[0]))
            break
        else:
            for letter in bad_guessed_letters:
                print('You have incorrectly guessed... {}\n'.format(letter.lower()))                
            
    else:
        print('Incorrect\n')
        for letter in word[0]:
            if letter.lower() in check:
                print(letter)
            else:
                print('_')
        bad_guessed_letters.append(guess.lower())
        incorrect += 1

        for letter in bad_guessed_letters:
            print('You have incorrectly guessed... {}\n'.format(letter.lower()))
            
if incorrect == 8:    
    print("You couldn't get it!!!")
    
else:
    print('You did it!!!')
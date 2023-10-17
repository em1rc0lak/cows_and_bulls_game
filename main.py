import random

number_to_guess = str(random.randint(1000,9999))

while(True):
    bulls = 0
    cows = 0
    
    guess = input("What is your 4-digit guess? ")

    if(int(guess)<1000 or int(guess)>9999):
        print("Your guess must be between 1000 and 9999 !!!")
        continue
    
    matches = set(number_to_guess) & set(guess)

    if (guess != number_to_guess):
        
        for i in range(4):
            if guess[i] == number_to_guess[i]:
                bulls += 1
            if guess[i] in number_to_guess:
                cows += 1
        cows -= bulls
    
    elif(guess == number_to_guess):
        print("Excelent! The number was:" , number_to_guess)
        break
    
    print("Bulls:" , bulls , "|" , "Cows:" , cows)


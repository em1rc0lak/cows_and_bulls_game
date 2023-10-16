import random

number_to_guess = str(random.randint(1000,9999))
print(number_to_guess)

while(True):
    bulls = 0
    cows = 0
    
    guess = input("What is your 4-digit guess? ")

    if(int(guess)<1000 or int(guess)>9999):
        print("Your guess must be between 1000 and 9999 !!!")
        continue
    
    type(guess)

    if (guess != number_to_guess):
        
        for i in range(4):
            if(guess[i] == number_to_guess[i]):
                bulls += 1

        for i in range(4):
            for j in range(4):
                if(i != j and guess[i] == number_to_guess[j]):
                    cows += 1

    elif(guess == number_to_guess):
        print("Excelent! The number was:" , number_to_guess)
        break

    print("Bulls:" , bulls , "|" , "Cows:" , cows)


import random

def guess_number():
    
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = int(input("Devinez le nombre entre 1 et 100 : "))

        if guess == number:
            print("Bravo ! Vous avez trouvé le nombre en", attempts, "essais.")
            break
        elif guess < number:
            print("Trop petit !")
        else:
            print("Trop grand !")

        attempts += 1

guess_number()
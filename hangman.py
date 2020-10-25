#Se da la bienvenida al jugador
def name():
    name = str(input("Enter your name: "))
    print("Hello " + str(name) + ", let's play and try to solve the hangman game!")
    return

name()


#Importo random para escoger palabras de las listas predeterminadas
#Importo time para dar un tiempo predeterminado al jugador
import random, time

#Creo las variables
paises_europeos = ["albania", "alemania", "andorra", "armenia", "austria", "azerbaiyan", "belgica", "bielorrusia", "bosnia", "bulgaria", "chipre", "croacia", "dinamarca", "eslovaquia", "eslovenia", "españa", "estonia", "rusia", "finlandia", "francia", "grecia", "hungria", "irlanda", "islandia", "italia", "letonia", "lituania", "luxemburgo", "macedonia", "malta", "moldavia", "monaco", "montenegro", "noruega", "paises bajos", "polonia", "portugal", "reino unido", "republica checa", "rumania", "serbia", "suecia", "suiza", "turquia", "ucrania"]
frutas = ["platano", "fresa", "manzana", "piña", "coco", "frambuesa", "mora", "uva", "melocoton", "pera", "melon", "sandia"]

player_guess_list = []
player_guesses = []
play_game = True
category = ""
continue_game = "Y"

#Comienza el juego: se adivina la palabra
time.sleep(3)
print("The objective of the game is to guess the secret word chosen by the computer.")
time.sleep(3)
print("You can only gues one letter at a time. Don't forget to press the 'enter' key after each guess!")
time.sleep(4)
print("Let the fun begin!")
time.sleep(2)


#Se escoge la palabra para adivinar de las categorias predeterminadas
while True:
    if category.upper() == 'P':
        secret_word = random.choice(paises_europeos)
        break
    elif category.upper() == 'F':
        secret_word = random.choice(frutas)
        break
    else:
        category = input("Please select a category: P for Paises Europeos, F for Frutas, X to Exit")
    
    if category.upper() == 'X':
        print("You're leaving already? See you next time!")
        play_game = False
        break

if play_game:
    secret_word_list = list(secret_word)
    attempts = (len(secret_word) + 3)

    #Creo una función para ir almacenando las letras que adivina el jugador
    def guessed_letter():
        print("Your secret word is: " + ''.join(player_guess_list))

    #Creo una función para añadir espacios entre las letras
    for char in secret_word_list:
        player_guess_list.append('_')
    guessed_letter()

    print("The number of guesses for this word is: ", attempts)

    #Empieza el juego
    while True:
        print("Start guessing the word... Please enter a letter: ")
        time.sleep(3)
        letter = input()

        #Si ya ha adivinado la misma letra antes
        if letter in player_guesses:
            print("Oops! Looks like you already guessed this letter... try something else!")

        else:
            attempts -= 1
            player_guesses.append(letter)
            if letter in secret_word_list:
                print("Nice guess! Keep going.")
                if attempts > 0:
                    print("You have ", attempts, "guesses left.")
                
                for x in range(len(secret_word_list)):
                    if letter == secret_word_list[x]:
                        letter_index = x
                        player_guess_list[letter_index] = letter.upper()
                guessed_letter()

                #Si se equivoca de letra
            else:
                print("Oops! Wrong letter. Try again.")
                if attempts > 0:
                    print("You have ", attempts, "guesses left.")
                guessed_letter()
        
        #Bucle ganar o perder
        list_joined = ''.join(player_guess_list)
        if list_joined.upper() == secret_word.upper():
            print("Congratulations! You win ", name, " !")
            break
        elif attempts == 0:
            print("Too many guesses... Sorry, try next time!")
            print("The secret word was: ", secret_word.upper())
            break

    


                



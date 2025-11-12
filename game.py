##def start():
##    print(get_number())
##
##def get_number():
##    number = 12
##    return number


##def start():
##    print("Hello {}".format(get_name()))
##
##def get_name():
##    name = input("What is your name?")
##    return name


##def start():
##    f_name = "Sarah"
##    l_name = "Connor"
##    age = 28
##    gender = "Female"
##    get_info(f_name, l_name, age, gender)
##
##def get_info(f_name, l_name, age, gender):
##    print("My Name is {} {}. I am a {} year old {}.".format(f_name, l_name, age, gender))
##
##    


# How we are passing information into our function and getting information out of
# our function

def start(nice= 0, mean=0, name=""):
    #start function needs to know the name of plsyer.
    name = describe_game(name)# gets and returns the users name
    nice,mean,name = nice_mean(nice,mean,name) #uses the "name" in the game

def describe_game(name):
    """
    Check if this is a new game or not.
    If it is new, get the users name.
    if it is not new thank the player
    for playing again and continue with the game.
    """

    if name != "":
        print("\nThank you for playing again".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name?\n>>>").capitalize()
                if name != "":
                    print("\nWelcome, {} !".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \n will be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a conversation. Will you be nice or mean? (N/M)\n ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
        stop = False
    score(nice, mean, name) # pass the 3 variables to the score()

def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and ({}, Mean)".format(name,nice,mean))

    
def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2: # if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else: # else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    # Substitute the {} wildcards with our variable values
    print("Nice job {}, you win! \nEveryone loves you and \nyou've made tons of friends along the way!".format(name))
    # Call again function and pass in our variables
    again(name,name,name)
    
def lose(nice, mean, name):
    # Substitute the {} placeholders with our variable values
    print("\nAhhh too bad, game over! \n{}, you live in a dirty beat-up van by the river, wretched and alone!".format(name))
    # Call again function and pass in our variables
    again(nice,mean,name)


def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>> ").lower()
        if choice == "y":
            stop = False
            reset(nice, mean, name)
        if choice == "n":
            print("\nOh sad, sorry to see you go!\n")
            stop = True
            quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO'\n")


def reset(nice,mean,name):
    nice = 0
    mean = 0
    #Notice, I do not reset the name variable as that same user has elected to play again
    start(nice,mean,name)



if __name__ == "__main__":
    start()


    
    

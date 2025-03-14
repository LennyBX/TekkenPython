import random
from faker import Faker

def rock_paper():
    print("Welcome to Rock Paper Scissors!")
    print("Write on the following possibility :")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    user_input = int(input("Votre choix : "))
    if user_input not in [1, 2, 3]:
        print("Veuillez entrer un nombre valide (1, 2 ou 3).")
        return rock_paper()

    choices = {1: "Rock", 2: "Paper", 3: "Scissors"}
    master_of_rock_paper_scissors = random.choice([1, 2, 3])

    print(f"Votre choix: {choices[user_input]}")
    print(f"Ordinateur: {choices[master_of_rock_paper_scissors]}")

    if master_of_rock_paper_scissors == user_input:
        print("No Winners sorry !")
        rock_paper()
    elif (
         (master_of_rock_paper_scissors == 1 and user_input == 2) or
         (master_of_rock_paper_scissors == 2 and user_input == 3) or
         (master_of_rock_paper_scissors == 3 and user_input == 1)
    ):
        print("You Win!")
    else:
        print("You lose!")

def rock_paper_for_test(choices_user, master_of_rock_paper_scissors):
    print("Welcome to Rock Paper Scissors!")
    print("Write on the following possibility :")
    print("1 - Rock")
    print("2 - Paper")
    print("3 - Scissors")
    if choices_user not in [1, 2, 3]:
        print("Veuillez entrer un nombre valide (1, 2 ou 3).")
        return rock_paper()

    if master_of_rock_paper_scissors is None:
        master_of_rock_paper_scissors = random.choice([1, 2, 3])

    if master_of_rock_paper_scissors == choices_user:
        return "No Winners sorry !"
        rock_paper()
    elif (
         (master_of_rock_paper_scissors == 1 and choices_user == 2) or
         (master_of_rock_paper_scissors == 2 and choices_user == 3) or
         (master_of_rock_paper_scissors == 3 and choices_user == 1)
    ):
        return "You Win!"
    else:
        return "You lose!"


def game_personage():
    faker = Faker()

    races = {
        1: "Humaine",
        2: "Alien",
        3: "Florian",
    }
    character1 = {
        "id": 1,
        "name": "Gedeon",
        "city": "Lyon",
        "country": "France",
        "attacks" : [
            {
                "name": "Hurlement",
                "dammage": 30
            },
            {
                "name": "Bain d'eau chaude",
                "dammage": 15
            },
            {
                "name": "Boulette de lave",
                "dammage": 5
            }
        ],
        "hp": random.randint(10, 25),
        "race": races[random.choice(list(races.keys())) ],
    }
    character2 = {
        "id": 2,
        "name": "Gaspar",
        "city": faker.city(),
        "country": faker.country(),
        "hp": random.randint(10, 10),
        "race": races[random.choice(list(races.keys())) ],
    }

    print("Bienvenue dans le case depart")
    print('---------------------------------')

    print(f"Vous - "
          f"Nom : { character1['name']} "
          f"Pays : { character1['country']} "
          f"Ville : { character1['city']} "
          f"Race : { character1['race']} "
          )
    print(f"Adversaire - "
          f"Nom : {character2['name']} "
          f"Pays : {character2['country']}  "
          f"Ville : {character2['city']} "
          f"Race : {character2['race']} "
          )

    print('---------------------------------')

    print("Le combat va commencer prepare toi")

    print('---------------------------------')

    while character2['hp'] > 0 and character1['hp'] > 0:
        print(f"Ton perssonage va attaquer le perssonage adverse")
        print(f"Attaque de {character1['name']} sur {character2['name']}")

        print('---------------------------------')

        try:
            attack_user = int(input(f"Choisisez une attack ?"))
        except ValueError:
            print("Veuillez entrer un nombre valide.")
            continue

        print(f"{character1['name']} a infliger - {attack_user} point de vie  a  {character2['name']}")
        character2['hp'] -= attack_user
        print(f"{character2['name']} a désormais que {character2['hp']} point de vie")

        print('---------------------------------')

        attack_adversaire = random.randint(1,10)
        print(f"{character2['name']} a infliger - {attack_adversaire} point de vie  a  {character1['name']}")
        character2['hp'] -= attack_adversaire
        print(f"{character1['name']} a désormais que {character1['hp']} point de vie")

    if character2['hp'] <= 0:
        print("You Win")
    else:
        print("You Lose")


# rock_paper()
# game_personage()
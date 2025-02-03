from django.shortcuts import render
import random

def index(request):
    character1 = {
        "name": "Bryan",
        "city": "Lyon",
        "country": "France",
        "hp": random.randint(10, 25),
        "race": "Humaine",
        "attacks": [
            {"name": "Fouet", "damage": 30},
            {"name": "Marque sur le torse", "damage": 15},
            {"name": "Torture", "damage": 5},
        ]
    }

    character2 = {
        "name": "Raven",
        "city": "Paris",
        "country": "France",
        "hp": random.randint(10, 25),
        "race": "Alien"
    }

    context = {
        "character1": character1,
        "character2": character2
    }
    return render(request, "jeux1/index.html", context)

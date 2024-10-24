#vos fonctions

#variables
pokemons = [{"nom":"pikachu", "hp" : 120,"attaque_1":"attaque éclaire", "attaque_2" : "vive attaque"},
            {"nom":"salameche", "hp" : 110,"attaque_1":"flameche", "attaque_2" : "charge"}
            ]

programme = True

#programme principale
while programme:
    choix = int(input("voulez-vous (1) afficher les pokémons (2) ajouter (3)supprimer (4) modifier un pokémon : "))
    print("--------------------------------------------------------------------------------------")
    match choix:
        case 1:
            #afficher les pokemons
            pass
        case 2:
            #ajouter un pokemon
            pass
        case 3:
            #retirer un pokemon
            pass
        case 4: 
            #modifier un pokemon
            pass
        case _ : 
            print("erreur lors du choix")
    print("--------------------------------------------------------------------------------------")
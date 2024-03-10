import pandas as pd
from planification import Infrastructure
from planification import Building


# Etape de preparation des données
def prepare_data(path_to_csv):
    path_to_csv= "C:/Users/blond/OneDrive/Bureau/MASTERE/MD4/Machine_learning/Projet_fin_de_module/projet_de_math/Raccordement-Fibre/reseau_en_arbre.csv"
    data_set = pd.read_csv(path_to_csv)

    duplicated_data = data_set[data_set.duplicated()]  # idendetification des doublons
    print(duplicated_data)

    data_set = pd.read_csv(path_to_csv).drop_duplicates()  # Suppression des doublons
    print(data_set)

    
    data_set = data_set[data_set["infra_type"] != "infra_intacte"] # Sciller les infrastructure à reparer
    print(data_set)

    # Regrouper selon les infra_id
    data_set_infra = data_set.groupby(by="infra_id")
    print(data_set_infra)
    dict_infra = {}

    for infra_id, infra_set in data_set_infra:
        length = infra_set["longueur"].iloc[0]
        infra_type = infra_set["infra_type"].iloc[0]
        nb_houses = infra_set["nb_maisons"].sum()
        infra = Infrastructure(infra_id, length, infra_type, nb_houses)
        dict_infra[infra_id] = infra

     # Regrouper selon les id_batiment
    data_set_buld = data_set.groupby(by="id_batiment")
    print(data_set_buld)
    list_buildings = []

    for id_bat, bat_set in data_set_buld:
        list_infra = []
        for infra_id in bat_set["infra_id"]:
            infra = dict_infra[infra_id]
            list_infra.append(infra)
        building = Building(id_bat, list_infra)
        list_buildings.append(building)

    return dict_infra, list_buildings


# Fonction de trie selon la difficulté
def sorted_build_difficulty(list_building):
    """ Cette fonction permet dans un premier temps de trier les bâtiments en fonction de leur difficulté à l'aide 
    de la méthode __lt__ définie dans la classe Building. Puis retourne la liste des bâtiments triés selon leur difficulté.
    """
    sorted_buildings = sorted(list_building)
    return sorted_buildings


path_to_csv = "C:/Users/blond/OneDrive/Bureau/MASTERE/MD4/Machine_learning/Projet_fin_de_module/projet_de_math/Raccordement-Fibre/reseau_en_arbre.csv"
dict_infra, list_buildings = prepare_data(path_to_csv)
sorted_buildings = sorted_build_difficulty(list_buildings)

# Renvoie les batiment triés déjà selon le niveau de difficultés
for building in sorted_buildings:
    print("Building ID:", building.id_building, "| Difficulty:", building.get_building_difficulty())




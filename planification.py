# Définition de la classe Infrastructure
class Infrastructure:
    def __init__(self, infra_id, length, infra_type, nb_houses):
        self.infra_id = infra_id
        self.length = length
        self.infra_type = infra_type
        self.nb_houses = nb_houses

    def get_repair_infra(self):
        if self.infra_type == "infra_intact":
            return None
        
    def get_infra_difficulty(self):
        """ Cette méthode calcule la difficulté de l'infrastructure. Si le type d'infrastructure est "infra_intact", la difficulté est définie à 0.
          Sinon, la difficulté est calculée en fonction de la longueur de l'infrastructure divisée par le nombre de maisons associées.
        """
        if self.infra_type == "infra_intact":
            return 0
        else:
            return self.length / self.nb_houses

    def __radd__(self, other_infra):
        """ Cette methode permet de sommer les infrastructures déjà reparer, radd (pour a droite).
        """
        return self.get_repair_infra + other_infra
    
    def __add__(self, other_infra):
        """ Cette methode est utilisée comme pour l'addition (add). 
        """
        return self.get_repair_infra + other_infra.get_repair_infra()

# Définition de la classe Building
class Building:
    def __init__(self, id_building, list_infras):
        self.id_building = id_building
        self.list_infras = list_infras

    def get_building_difficulty(self):
        """ Cette méthode calcule la difficulté du bâtiment. 
        Elle somme les difficultés de toutes les infrastructures contenues dans la liste list_infras.
        """
        return sum(infra.get_infra_difficulty() for infra in self.list_infras)

    def __lt__(self, other_building):
        """ cette une méthode de comparaison. 
        Elle compare la difficulté d'un bâtiment  donné avec la difficulté d'un autre bâtiment pour déterminer s'il est inférieur.
        """
        return self.get_building_difficulty() < other_building.get_building_difficulty()

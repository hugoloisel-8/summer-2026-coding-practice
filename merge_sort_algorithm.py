```python
def merge_sort(array):
    """
    Trie une liste d'entiers avec l'algorithme Merge Sort.

    L'algorithme divise récursivement la liste en deux parties,
    trie chaque partie, puis fusionne les deux parties triées.
    """

    # Une liste de 0 ou 1 élément est déjà triée.
    if len(array) <= 1:
        return

    # On trouve le milieu de la liste.
    middle_point = len(array) // 2

    # On divise la liste en deux parties.
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # On trie récursivement les deux parties.
    merge_sort(left_part)
    merge_sort(right_part)

    # Indices permettant de parcourir les deux parties.
    left_array_index = 0
    right_array_index = 0

    # Indice permettant de remplir le tableau final.
    sorted_index = 0

    # On compare les éléments des deux parties
    # et on place le plus petit dans le tableau original.
    while (
        left_array_index < len(left_part)
        and right_array_index < len(right_part)
    ):
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1

        sorted_index += 1

    # S'il reste des éléments dans la partie gauche,
    # on les ajoute au tableau.
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1

    # S'il reste des éléments dans la partie droite,
    # on les ajoute au tableau.
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


# Permet d'exécuter cette partie uniquement
# lorsque le fichier est lancé directement.
if __name__ == "__main__":
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]

    print("Unsorted array:")
    print(numbers)

    merge_sort(numbers)

    print("Sorted array:")
    print(numbers)
```

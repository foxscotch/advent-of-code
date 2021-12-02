# Python 3.8.3

from collections import defaultdict


def get_input():
    with open("input.txt", "r") as f:
        for line in f.read().splitlines():
            ingredients, allergens = line.split(" (contains ")
            ingredients = set(ingredients.split())
            allergens = set(allergens[:-1].split(", "))
            yield ingredients, allergens


def main():
    items = list(get_input())
    allergen_names = defaultdict(set)
    safe_ingredients = set()

    for ingredients, allergens in items:
        for allergen in allergens:
            safe_ingredients.update(ingredients)
            allergen_set = allergen_names[allergen]
            if len(allergen_set) == 0:
                allergen_set.update(ingredients)
            allergen_set.intersection_update(ingredients)

    safe_count = 0
    for ingredients in allergen_names.values():
        for ingr in safe_ingredients:
            if ingr in ingredients:
                safe_count += 1

    print(safe_count)


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(main())
    print(time.perf_counter() - start)

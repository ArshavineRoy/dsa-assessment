def remove_duplicates(sequence):
    container = []
    for num in sequence:
        if num not in container:
            container.append(num)

    return container

print(remove_duplicates([2, 3, 2, 4, 5, 3, 6, 7, 5]))  # [2, 3, 4, 5, 6, 7]
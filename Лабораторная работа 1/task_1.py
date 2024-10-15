numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_missing = 4
numbers[index_missing] = 0
numbers[index_missing] = sum(numbers) / len(numbers)

print("Измененный список:", numbers)

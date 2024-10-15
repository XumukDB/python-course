BYTES_FOR_ONE_CHAR = 4

available_space_mb = 1.44
available_space_bytes = available_space_mb * 1024 * 1024
number_of_pages = 100
strings_per_page = 50
strings_length = 25
book_size = number_of_pages * strings_per_page * strings_length * BYTES_FOR_ONE_CHAR

books_fit = int(available_space_bytes // book_size)
print("Количество книг, помещающихся на дискету:", books_fit)

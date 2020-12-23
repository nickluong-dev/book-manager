"""
Book collection manager.
Nick Luong
A00972523
"""


import doctest


def PRINT_ERROR():
    """
    Print warning to user.

    Prints an error message to user if they make a wrong choice in any point of the program.

    :postcondition: prints a warning message to user if wrong choice is made

    >>> PRINT_ERROR()
    That is not a valid option. Please try again.
    <BLANKLINE>
    """

    print("That is not a valid option. Please try again.\n")


def get_info(filename) -> tuple:
    """
    Read the books.txt file and creates a dictionary.

    Reads the books.txt and creates a tuple of dictionaries with each dictionary representing a book. Keys are organized
    by book information (Title, Author, etc). Anything value that is missing is given a string value of 'None'.

    :precondition: file must be plaintext file with data separated by tabs
    :postcondition: generate a collection of books represented by a tuple of dictionaries
    :return: a tuple of dictionaries

    >>> get_info('books_short_test.txt') # doctest: +NORMALIZE_WHITESPACE
     ({'Author': 'Dupre', 'Title': 'Skyscrapers', 'Publisher': 'BD&L', 'Shelf': '12', 'Category': 'Architecture', \
     'Subject': '20th Century'}, {'Author': 'Hollingsworth', 'Title': 'Architecture of the 20th Century', \
     'Publisher': 'Exeter', 'Shelf': '6', 'Category': 'Architecture', 'Subject': '20th Century'}, \
     {'Author': 'Johnson Burgee', 'Title': 'Architecture 1979-1985', 'Publisher': 'Rizzoli', 'Shelf': '6', \
     'Category': 'Architecture', 'Subject': '20th Century'})
    """

    # Reads file, splits by tab, and replaces empty values with 'None'.
    try:
        with open(filename, encoding='UTF-16') as books_file:
            headers = books_file.readline().split()
            book_collection = []
            for line in books_file:
                book_info = line.strip('\n').split('\t')

                for item in range(len(book_info)):
                    # if book_info[item] == '':
                    book_info[item] = 'None' if book_info[item] == '' else book_info[item]

                # Take the header and book value to form a dictionary.
                book = dict(zip(headers, book_info))
                book_collection.append(book)

            return tuple(book_collection)

    except FileNotFoundError:
        print("There's no file in the directory!")


def menu() -> str:
    """
    Display a menu with different options to the user.

    The menu displays helpful information for the user and give different options to choose from. The user is asked what
    they want to do (move, search, quit).

    :precondition: user must input valid menu choice
    :postcondition: display a text menu for user to navigate and choose from
    :return: a string representing the user choice
    """

    print("Welcome to your virtual book shelf. Please select an option. You can type in lowercase.")

    user_choice = input("1. Type '1' to search for a book.\n"
                        "2. Type '2' to move a book.\n"
                        "3. Type '3' to exit the program.\n")

    # Only accept valid options. Considers input errors.
    if user_choice in ['1', '2', '3']:
        return user_choice
    else:
        PRINT_ERROR()


def ask_search(book_collection: tuple) -> list:
    """
    Ask user how they would like to search for a book.

    Asks user for input on which search method they would like to search by. Then asks what is the value of their
    search. The values of both inputs are returned as a list to be used by search_book().

    :param book_collection: a tuple of dictionaries representing the collection of books
    :precondition: user must enter a valid option
    :postcondition: will return the search_parameters to search_book() which displays the results
    :return: a list of search parameters
    """

    options = create_options(book_collection)
    # print(options)

    print("How do you want to search for the book?")
    search_method = input(get_search_methods(options)).strip()

    # If valid option, ask the next question.
    if search_method in options.keys():
        search_query = input(f"Search by {options[search_method]} (you can partial search):")

        if search_query != '':
            # Returns list of search method and search query.
            search_parameters = [options[search_method], search_query.lower()]
            return search_parameters


def get_search_methods(options):
    """
    Format and print dynamic search methods.

    Takes the book and list of results to create a neatly formatted string to be printed when a book is searched.

    :param options: a dictionary of numbered options
    :precondition: options must be a dictionary
    :postcondition: displays the search method options
    :return: a string of the search method options

    >>> option = {'1': 'Element', '2': 'Class', '3': 'Race', '4': 'Weapon'}
    >>> get_search_methods(option) # doctest: +NORMALIZE_WHITESPACE
    "1. Type '1' to search by Element\\n2. Type '2' to search by Class\\n3. Type '3' to search by Race\\n4. Type '4' to
    search by Weapon\\n"

    >>> option = {'1': 'Author', '2': 'Title', '3': 'Publisher'}
    >>> get_search_methods(option)
    "1. Type '1' to search by Author\\n2. Type '2' to search by Title\\n3. Type '3' to search by Publisher\\n"
    """

    search = ""
    values = [val for val in options.values()]
    for seq, options in enumerate(options, 1):
        search += f"{seq}. Type '{seq}' to search by {values[seq-1]}\n"
    return search


def create_options(book_collection: tuple) -> dict:
    """
    Generate a dynamic dictionary of numbered options.

    Creates a dynamic dictionary of numbered options to be used in ask_search().

    :precondition: book collection must be a tuple
    :postcondition: generate a dictionary
    :param book_collection: a collection of books as a tuple
    :return: a dictionary of numbered options

    >>> collection = ({'Author': '', 'Title': '', 'Publisher': '', 'Shelf': '', 'Category': '', \
    'Subject': ''}, {'Author': '1', 'Title': '1', 'Publisher': '1', 'Shelf': '1', 'Category': '1', 'Subject': '1'})
    >>> create_options(collection)
    {'1': 'Author', '2': 'Title', '3': 'Publisher', '4': 'Shelf', '5': 'Category', '6': 'Subject'}

    >>> collection = ({'Damage': '', 'Health': '', 'Resistance': '', 'Dexterity': '', 'Mana': '', 'Class': ''}, \
    {'Damage': '1', 'Health': '1', 'Resistance': '1', 'Dexterity': '1', 'Mana': '1', 'Class': '1'})
    >>> create_options(collection)
    {'1': 'Damage', '2': 'Health', '3': 'Resistance', '4': 'Dexterity', '5': 'Mana', '6': 'Class'}
    """

    options = list([keys for keys in book_collection[0].keys()])
    numbers = [str(num + 1) for num in range(len(options) + 1)]
    result = dict(zip(numbers, options))
    return result


def search_book(search_parameters: list, book_collection: tuple) -> list:
    """
    Display the books searched from ask_search().

    Takes the values from ask_search() and get_info() to store matching searches to a new list. Prints the search
    results for user to read.

    :param search_parameters: a list of strings representing search method and search query
    :param book_collection: a tuple of dictionaries representing all books
    :precondition: search parameters must be valid choices
    :postcondition: will print the search results and return a list of those results
    :return: a list of dictionaries, the searched books

    >>> search_book(['Title', 'unbuilding'], get_info('Books UTF-16.txt')) # doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
    There are 1 results matching 'unbuilding':
    <BLANKLINE>
    1	Author: Macaulay
        Title: Unbuilding
        Publisher: HMCo
        Shelf: 6
        Category: Architecture
        Subject: American Architecture
    <BLANKLINE>
    [{'Author': 'Macaulay', 'Title': 'Unbuilding', 'Publisher': 'HMCo', 'Shelf': '6',
    'Category': 'Architecture', 'Subject': 'American Architecture'}]

    >>> search_book(['Author', 'hello world'], get_info('Books UTF-16.txt')) # doctest: +NORMALIZE_WHITESPACE
    <BLANKLINE>
    There are 0 results matching 'hello world':
    <BLANKLINE>
    []
    """

    # Takes search parameters from ask search() and append to list.
    results = []
    number_of_books = 0
    search_method, search_query = search_parameters[0], search_parameters[1]
    for book in book_collection:

        for keys, values in book.items():

            if search_method == keys:

                if search_query.isdigit() and search_query == values:
                    number_of_books += 1
                    results.append(book)

                elif not search_query.isdigit() and search_query in values.lower():
                    number_of_books += 1
                    results.append(book)

    print(f"\nThere are {number_of_books} results matching '{search_query}':\n")

    # Formats and prints the search results.
    for book in results:
        print_search(book, results)

    return results


def print_search(book: dict, results: list):
    """
    Format and print the search results.

    Takes the book and list of results to create a neatly formatted string to be printed when a book is searched.

    :param book: a dictionary representing a book in the book collection
    :param results: a list representing all the searched books found
    :precondition: book must be a dictionary and results must have at least one dictionary
    :postcondition: displays the search results

    >>> book_example = {'Author': 'Nick Luong', 'Title': 'How to Not Code 101', 'Publisher': 'Janky Coders 2020'}
    >>> results_example = [{'Author': 'Nick Luong', 'Title': 'How to Not Code 101', 'Publisher': 'Janky Coders 2020'}]
    >>> print_search(book_example, results_example) # doctest: +NORMALIZE_WHITESPACE
    1	Author: Nick Luong
        Title: How to Not Code 101
        Publisher: Janky Coders 2020
    <BLANKLINE>
    """

    search = ""
    search += f'{results.index(book) + 1}'
    for key, val in book.items():
        search += f'\t{key}: {val}\n'
    print(search)


def create_ordered_shelves() -> list:
    """
    Generate the virtual shelves.

    Creates a list of all the shelf values. Sorts it and returns theshelves as a list for for display_shelves() to use.

    :postcondition: returns a list of shelves
    :return: a list of shelf values

    >>> create_ordered_shelves() # doctest: +NORMALIZE_WHITESPACE
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31,
    32, 33, 34, 35, 36, 37, 38, 'Gaby', 'Island', 'Lego', 'Noguchi', 'Reading', 'Students']
    """

    # Get unique shelves. Converts numeric strings into ints for sorting.
    book_collection = get_info('Books UTF-16.txt')
    shelves = set()
    for dicts in book_collection:
        for _ in dicts.values():
            if dicts['Shelf'].isdigit():
                shelves.add(int(dicts['Shelf']))
            else:
                shelves.add(dicts['Shelf'])

    # Sorts ints and strings separately and combine into one list.
    shelves = sorted([item for item in shelves if str(item).isdigit()]) + sorted(
        [item for item in shelves if not str(item).isdigit()])

    return shelves


def display_shelves():
    """
    Display shelves.

    Formats the shelves available to the user before moving a book. Prints the books in two rows.

    :postcondition: prints shelves available to move books to

    >>> display_shelves() # doctest: +NORMALIZE_WHITESPACE
    Shelves:
    1|2|3|4|5|6|7|8|9|10|11|12|13|14|15|16|17|18|19|20|21|22|
    23|24|25|26|27|28|29|30|31|32|33|34|35|36|37|38|Gaby|Island|Lego|Noguchi|Reading|Students|
    """

    shelves = create_ordered_shelves()

    # Formats and prints the shelves. Split into half.
    print('Shelves:')
    for index in range(0, len(shelves) // 2):
        print(shelves[index], end='|')
    print('')

    for index in range(len(shelves) // 2, len(shelves)):
        print(shelves[index], sep='|', end='|')
    print('\n')


def ask_move(results: list) -> list or None:
    """
    Ask user what book they want to move and what shelf to move it to.

    Takes the search results and asks the user what book it wants to move. Then the user is presented the shelf options
    from make_ordered_shelf() and is asked where they want to put the book. The results of these questions are returned
    to be used by move().

    :param results: a list of dictionaries representing the search results from search_book()
    :precondition: results must have at least one book dictionary in it
    :postcondition: outputs the move parameters for move() to use
    :return: a list of one int and one string
    """

    move_parameters = []

    book_choice = get_book(results)
    shelf_choice = get_shelf()

    # Breaks out of try except block in books() if invalid choices
    if book_choice is None:
        return

    elif shelf_choice is None:
        return

    move_parameters.append(book_choice)
    move_parameters.append(shelf_choice)

    return move_parameters


def get_shelf() -> str:
    """
    Get the shelf choice from the user input.

    Asks user what shelf they want to move the chosen book to and returns a list.

    :postcondition: generates a list
    :return: a string, representing the shelf choice
    """

    # Displays shelf and asks what shelf to put the book on. Considers input errors.
    display_shelves()
    shelf = create_ordered_shelves()
    shelf_choice = input('Please choose which shelf you want to move the book to:')

    # If the numeric choice or string choice (eg. Island) is valid.
    if shelf_choice.isdigit() and int(shelf_choice) in shelf or shelf_choice.capitalize() in shelf:
        return shelf_choice


def get_book(results: list) -> int:
    """
    Get the book choice from the user input.

    Asks user what book they want to move and returns an int.

    :postcondition: generates an int
    :return: an int
    """

    # Asks what book to move. Considers input errors.
    book_choice = input('Please choose the number of which book you want to move:')

    # If not a digit, not in list, or zero.
    if book_choice.isdigit() and len(results) >= int(book_choice) > 0:
        return int(book_choice)


def move(results: list or dict, move_parameters: list):
    """
    Update the chosen book with the new shelf.

    Takes the search results and move parameters to update the chosen book. The update is visible in future searches and
    the update result is printed to the user.

    :param results: a list of dictionaries representing the searched book results
    :param move_parameters: a list of one int and one string representing the move parameters
    :precondition: results must be a dictionary with at least one book in it. Move_parameters must be a list with the
    book choice as an int and shelf choice a string.
    :postcondition: updates the chosen book with the new shelf

    >>> test_results = [{'Author': 'Macaulay', 'Title': 'Unbuilding', 'Publisher': 'HMCo', 'Shelf': '6', \
    'Category': 'Architecture', 'Subject': 'American Architecture'}]
    >>> test_move_parameters = [1, 'Island']
    >>> move(test_results, test_move_parameters) # doctest: +NORMALIZE_WHITESPACE
    You successfully moved 'Unbuilding' by 'Macaulay' to shelf: 'Island'
    <BLANKLINE>
    """

    # Updates the book with new shelf.
    chosen_book = move_parameters[0] - 1
    chosen_shelf = move_parameters[1]
    updated_book = results[chosen_book]

    # Capitalizes shelf choice if it is a string name (eg. Island) otherwise it is a numeric string
    updated_book['Shelf'] = chosen_shelf.capitalize() if chosen_shelf.isalpha() else chosen_shelf

    # updated_book is a dictionary when print(type(updated_book)) but hovering over it shows that it is a list. Bug?
    print(f"You successfully moved '{updated_book['Title']}' by '{updated_book['Author']}' to shelf: "
          f"'{updated_book['Shelf']}'\n")


def end_program(book_collection: tuple):
    """
    Export updated book collection to plaintext file and end program.

    Exports books in a plaintext file separated by tabs. Each row represents a new book. Then the program quits.

    :param book_collection: a tuple of dictionaries representing the book collection
    :precondition: book_collection must be a tuple of dictionaries
    :postcondition: writes new plaintext file with new book collection and ends program
    """

    filename = 'Books UTF-16.txt'
    with open(filename, 'w', encoding='UTF-16') as file_object:
        file_object.write(quit_headers(book_collection) + '\n')
        for book in book_collection:
            new_book = quit_lines(book)
            file_object.write(new_book + '\n')

    quit()


def quit_lines(book: dict) -> str:
    """
    Generate the new lines for overwriting original plaintext file.

    Gets the values from each dictionary in the book collection. Creates a string and strips the last tab from the
    right.

    :param book: a dictionary, representing the books in the collection
    :postcondition: generate a string of book values spaced by tabs except for the last header
    :return: a string of book values

    >>> example_book = {'Author': 'Nick Luong', 'Title': 'How to Not Code 101', 'Publisher': 'Janky Coders 2020'}
    >>> quit_lines(example_book)
    'Nick Luong\\tHow to Not Code 101\\tJanky Coders 2020'

    >>> example_book = {'Author': 'Macaulay', 'Title': 'Unbuilding', 'Publisher': 'HMCo', 'Shelf': '6', \
    'Category': 'Architecture', 'Subject': 'American Architecture'}
    >>> quit_lines(example_book)
    'Macaulay\\tUnbuilding\\tHMCo\\t6\\tArchitecture\\tAmerican Architecture'
    """

    lines = ""
    for value in book.values():
        lines = lines + value + '\t'
    stripped = lines.rstrip('\t')
    return stripped


def quit_headers(book_collection) -> str:
    """
    Generate dynamic headers for overwriting original plaintext file.

    Gets the keys from any dictionary in the book collection. It doesn't matter which. Creates a string and strips
    the last tab from the right.

    :param book_collection: a tuple of dictionaries
    :precondition: book collection must be a tuple of dictionaries
    :postcondition: generate a string of headers spaced by tabs except for the last header
    :return: a string of headers

    >>> collection = ({'Author': '', 'Title': '', 'Publisher': '', 'Shelf': '', 'Category': '', \
    'Subject': ''}, {'Author': '1', 'Title': '1', 'Publisher': '1', 'Shelf': '1', 'Category': '1', 'Subject': '1'})
    >>> quit_headers(collection)
    'Author\\tTitle\\tPublisher\\tShelf\\tCategory\\tSubject'

    >>> collection = ({'Damage': '', 'Health': '', 'Resistance': '', 'Dexterity': '', 'Mana': '', 'Class': ''}, \
    {'Damage': '1', 'Health': '1', 'Resistance': '1', 'Dexterity': '1', 'Mana': '1', 'Class': '1'})
    >>> quit_headers(collection)
    'Damage\\tHealth\\tResistance\\tDexterity\\tMana\\tClass'
    """

    headers = ""
    for key in book_collection[0].keys():
        headers = headers + key + '\t'
    stripped = headers.rstrip('\t')
    return stripped


def books():
    """
    Drive the flow of the program.

    Organizes the flow and structure of the program through while loops and if statements.

    :postcondition: runs the functionality of the program
    """

    book_collection = get_info('Books UTF-16.txt')

    # Loops main functions and brings up main menu.
    while True:
        user_choice = menu()

        try:
            if user_choice == '1':  # Search
                search_parameters = ask_search(book_collection)
                search_book(search_parameters, book_collection)

            elif user_choice == '2':  # Move
                search_parameters = ask_search(book_collection)
                search_results = search_book(search_parameters, book_collection)

                if len(search_results) > 0:
                    move_parameters = ask_move(search_results)
                    move(search_results, move_parameters)

            elif user_choice == '3':  # Quit
                end_program(book_collection)

        except (TypeError, AttributeError):
            PRINT_ERROR()


def main():
    """
    Executes the program.
    """

    books()
    doctest.testmod(verbose=True)


if __name__ == "__main__":
    main()

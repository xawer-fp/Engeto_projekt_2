"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Roman Brixí
email: roman.brixi@seznam.com
"""

import random
import time

# nastavení šířky výpisu hry
WINDOW_WITH = 65
# nastavení proměnné pro výpis řádku
PRINT_LINE = "-" * WINDOW_WITH
# nastavení proměnné pro TOP3 tabulku
top_results: list[dict[str, int]] = []

def start_the_game() -> None:
    """
    Displays the game introduction and prompts the user to start or view help.

    This function:
    - Prints a welcome message and basic game description
    - Asks the player to press 'H' for help or 'S' to start the game
    - Handles input validation (length, type, allowed characters)
    - Instructions will be displayed if the "H" key is pressed
    - Calls play_game() if 'S' is pressed

    Returns:
        None
    """
    print(PRINT_LINE)
    # pozdrav hráče a napiš to velkým písmem
    text = "Hello player!"
    print(f"{text.upper():^{WINDOW_WITH}}")
    print(PRINT_LINE)
    # vypiš krátké info o hře
    row = (
        "Welcome to the game Bulls and Cows.\n"
        "Your task, if you accept it,\n"
        "will be to guess a 4-digits number."
    )
    for line in row.splitlines():
        print(f"{line:^{WINDOW_WITH}}")
    # čeká na hráče, aby stiskl H pro pomoc nebo S pro začátek hry
    # a kontroluje, zda je vstup správný
    while True:
        print(PRINT_LINE)
        game = input("Press 'H' for help or 'S' for start: ").strip().upper()
        print()
        if len(game) == 0:
            # pokud je vstup prázdný, tak vrátí chybu
            print(f"{"❌ ERROR: No character entered.":>{WINDOW_WITH-1}}")
        elif len(game) > 1:
            # pokud je vstup delší než 1 znak, tak vrátí chybu
            print(f"{"❌ ERROR: Please enter only one character.":>{WINDOW_WITH-1}}")
        elif game.isdigit():
            # pokud je vstup číslo, tak vrátí chybu
            print(
                f"{"❌ ERROR: Please enter a character not a number.":>{WINDOW_WITH-1}}"
            )
        elif game.isalpha():
            # pokud je vstup písmeno, tak zkontroluje, zda je to H nebo S
            if game == "H":
                print(PRINT_LINE)
                text = "Rules of the game"
                print(f"{text.upper():^{WINDOW_WITH}}")
                print(PRINT_LINE)
                # vypiš pravidla hry
                # rozděleno do více řádků pro lepší čitelnost
                row = (
                    "The game is played with a 4-digit number.\n"
                    "The first digit must not be zero.\n"
                    "The digits must be unique. Without repeating the same numbers.\n"
                    "The player has to guess the number.\n"
                    "For each guess, the player receives feedback:\n"
                    "Bulls (🐂) - correct digit in the correct position\n"
                    "Cows (🐄) - correct digit in the wrong position\n"
                    "The game ends when the player guesses the number or types 'quit'."
                )
                for line in row.splitlines():
                    print(f"{line:^{WINDOW_WITH}}")
                print(PRINT_LINE)
                ## čeká na hráče, aby stiskl Enter pro začátek hry
                input("\nPress Enter to start the game...")
                print()
                break
            elif game == "S":
                break
            else:
                # pokud je vstup jiný znak než H nebo S, tak vrátí chybu
                print(f"{"❌ ERROR: Invalid character.":>{WINDOW_WITH-1}}")
        else:
            # pokud je vstup jiný než předchozí podmínky, tak vrátí chybu
            print(f"{"❌ ERROR: Invalid character.":>{WINDOW_WITH-1}}")
    print(PRINT_LINE)
    play_game()


def generate_a_number() -> str:
    """
    Generates a random 4-digit number as a string, with non-repeating digits.
    The first digit is guaranteed to be non-zero.
    Returns:
        str: A 4-digit number with unique digits (first digit is 1–9).
    """
    # alternativně lze numbers = list("0123456789")
    numbers = list(map(str, range(10)))
    # první číslice nesmí být 0
    first_number = random.choice(numbers[1:])
    # odstraň první číslo z výběrové monožiny
    numbers.remove(first_number)
    # vygeneruj unikátní zbylá 3 čísla
    last_three_numbers = random.sample(numbers, 3)
    # spoj dohromady a vrať
    return first_number + "".join(last_three_numbers)


def play_game() -> None:
    """
    Runs a single round of the Bulls and Cows game.

    This function:
    - Generates a secret 4-digit number with unique digits (first digit ≠ 0)
    - Starts a timer to measure game duration
    - Prompts the user repeatedly to guess the number
    - Provides feedback (bulls & cows) for each guess
    - Displays input errors (length, uniqueness, non-digit characters)
    - Ends the game if the user guesses the number or types 'quit'
    - Calls `end_game()` to display final results upon success

    Returns:
        None
    """
    number = generate_a_number()
    start_time = time.time()
    text = "The game is started"
    print(f"{text.upper():^{WINDOW_WITH}}")
    print(f"{"(to end the game enter 'quit')":^{WINDOW_WITH}}")
    # zde lze zobrazit číslo pro testování
    print(PRINT_LINE)
    print(f"{f"Only for testing, the number is: {number}":^{WINDOW_WITH}}")
    round_of_the_game = 0
    # horní a dolní část tabulky pro výpis kol
    print_top = f"{"┌───┬───┬───┬───┐":>{WINDOW_WITH}}"
    print_bottom = f"{"└───┴───┴───┴───┘":>{WINDOW_WITH}}"

    # hlavní cyklus hry, který se opakuje, dokud hráč neuhodne číslo nebo nezadá quit
    while True:
        print(PRINT_LINE)
        user_number = input("Enter a 4-digit unique number: ").strip().lower()
        print()

        if user_number.isdigit():
            if len(user_number) != 4:
                # pokud není zadáno 4 čísla, tak vrátí chybu
                print(f"{"❌ ERROR: Enter exactly 4 numbers":>{WINDOW_WITH-1}}")
            elif len(set(user_number)) != 4:
                # pokud není zadáno 4 unikátní čísla, tak vrátí chybu
                print(f"{"❌ ERROR: Enter 4 unique numbers":>{WINDOW_WITH-1}}")
            elif user_number[0] == "0":
                # pokud je první číslo 0, tak vrátí chybu
                print(
                    f"{"❌ ERROR: The first digit must not be zero":>{WINDOW_WITH-1}}"
                )
            else:
                # pokud je zadáno 4 unikátní číslo, tak pokračuje ve hře
                # a spočítá bulls a cows
                print(f"{"✅ You entered a valid number!":>{WINDOW_WITH-1}}")
                bulls = sum(1 for i, j in zip(user_number, number) if i == j)
                cows = len(set(user_number) & set(number)) - bulls
                round_of_the_game += 1
                print(print_top)
                row = (
                    f"Round: {round_of_the_game} ->"
                    f" 🐂 bulls = {bulls} | 🐄 cows = {cows}  "
                    f"│ {user_number[0].upper()} "
                    f"│ {user_number[1].upper()} "
                    f"│ {user_number[2].upper()} "
                    f"│ {user_number[3].upper()} │"
                )
                print(f"{row:>{WINDOW_WITH-2}}")
                print(print_bottom)
                if user_number == number:
                    # pokud hráč uhodl číslo, tak zavolá funkci end_game
                    # a předá jí čas začátku hry a počet kol
                    end_game(start_time, round_of_the_game)
                    break
        elif len(user_number) == 0:
            # pokud není zadáno nic, tak vrátí chybu
            print(f"{"❌ ERROR: No character entered.":>{WINDOW_WITH-1}}")
        elif user_number == "quit":
            # pokud hráč zadá quit, tak ukončí hru
            print(f"{"You chose to quit the game.":^{WINDOW_WITH}}")
            print(f"{"The game is over.":^{WINDOW_WITH-1}}")
            print(PRINT_LINE)
            # zavolání funkce play_again pro dotaz na další hru
            play_again()
            break
        elif user_number.isalpha():
            # pokud je zadáno písmeno, tak vrátí chybu
            print(f"{"❌ ERROR: Enter only numbers":>{WINDOW_WITH-1}}")
        else:
            print(f"{"❌ ERROR: Invalid character.":>{WINDOW_WITH-1}}")


def end_game(start_time, round_of_the_game):
    """
    Displays the end game message and thanks the player for playing.

    This function:
    - Prints a thank you message
    - Displays the total time taken to play the game

    Returns:
        None
    """
    # gratulace hráči za uhodnutí čísla
    print(f"{"👍 Congratulations! 👍":^{WINDOW_WITH-2}}")
    print(f"{"You guessed the number you were looking for!":^{WINDOW_WITH}}")
    # výpis počtu pokusů
    print(f"{f'Number of attempts: {round_of_the_game}':^{WINDOW_WITH}}")
    # výpis času hry
    minutes, seconds = time_counter(start_time)
    print(f"{f"⌛ Game duration: {minutes} min {seconds} sec":^{WINDOW_WITH - 1}}")
    top_scores(round_of_the_game, minutes, seconds)
    # zavolání funkce play_again pro dotaz na další hru
    print()
    play_again()


def top_scores(round_of_the_game: int, minutes: int, seconds: int) -> None:
    """
    Displays the top 3 results of the game in a formatted table.

    This function:
    - Appends the current game results (rounds, minutes, seconds) to the top results list.
    - Sorts the top results based on the number of rounds, minutes, and seconds in ascending order.
    - Trims the list to only include the top 3 results.
    - Prints the results in a visually formatted ASCII table with columns for Rank, 
    Rounds, and Time.

    Args:
        round_of_the_game (int): The number of rounds it took the player to guess the number.
        minutes (int): The number of minutes taken to complete the game.
        seconds (int): The number of seconds taken to complete the game.

    Returns:
        None: This function does not return anything, but prints the top 3 results table.
    """
    top_results.append({
        "rounds": round_of_the_game,
        "minutes": minutes,
        "seconds": seconds
    })
    # seřadit výsledky podle počtu kol, minut a sekund
    # a ponechat pouze 3 nejlepší výsledky
    # seřadí výsledky podle počtu kol, minut a sekund
    top_results[:] = sorted(
        top_results,
        key=lambda x: (x["rounds"], x["minutes"], x["seconds"])
    )[:3]

    # Vykreslení tabulky
    table_width = 43
    border = "=" * table_width
    print(f"\n{border:^{WINDOW_WITH}}")
    print(f"{' TOP 3 RESULTS ':^{table_width}}".center(WINDOW_WITH))
    print(f"{border:^{WINDOW_WITH}}")
    print(f"| {'RANK':^6} | {'ROUNDS':^10} | {'TIME':^15} |".center(WINDOW_WITH))
    print(f"|{'-' * 6:^8}|{'-' * 10:^12}|{'-' * 15:^17}|".center(WINDOW_WITH))
    for i, result in enumerate(top_results, start=1):
        time_str = f"{result['minutes']}m {result['seconds']}s"
        row = f"| {i:^6} | {result['rounds']:^10} | {time_str:^15} |"
        print(f"{row:^{WINDOW_WITH}}")
    print(f"{'=' * table_width:^{WINDOW_WITH}}")


def play_again() -> None:
    """
    Asks the player whether they want to play another round.

    - Prompts the user with a Yes/No question.
    - If the answer is 'Y', starts a new game by calling play_game().
    - Otherwise, prints a goodbye message and ends the program loop.

    Returns:
        None
    """
    # čeká na hráče, aby stiskl Y pro další hru nebo N pro konec
    answer = input("Do you want to play again? (Y/N): ").strip().upper()
    if answer != "Y":
        print(f"\n{"Thanks for playing! Goodbye.":^{WINDOW_WITH}}")
        print(PRINT_LINE)
    else:
        print()
        print(PRINT_LINE)
        play_game()


def time_counter(start_time: float) -> tuple[int, int]:
    """
    Calculates the elapsed time in minutes and seconds.

    Args:
        start_time (float): The start time in seconds (typically from time.time()).

    Returns:
        tuple[int, int]: A tuple containing the elapsed time as (minutes, seconds).
    """
    # výpočet času hry
    end_time = time.time()
    elapsed_time = end_time - start_time
    minutes = int(elapsed_time // 60)
    seconds = int(elapsed_time % 60)
    return minutes, seconds


if __name__ == "__main__":
    start_the_game()

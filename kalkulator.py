def _get_input() -> list:
    a = float(input("Wpisz pierwsza liczbe:"))
    b = float(input("Wpisz druga liczbe:"))

    return [a, b]


def addition(x: float, y: float) -> float:
    print(f"Rozpoczeto dodawanie liczby {x} do liczby {y}")
    return x + y


def subtraction(x: float, y: float) -> float:
    print(f"Rozpoczeto odejmowanie liczby {x} od liczby {y}")
    return x - y


def multiplication(x: float, y: float) -> float:
    print(f"Rozpoczeto mnozenie liczby {x} przez liczbe {y}")
    return x * y


def division(x: float, y: float) -> float:
    print(f"Rozpoczeto dzielenie liczby {x} przez liczbe {y}")
    return x / y


def involution(x: float, y: float) -> float:
    print(f"Rozpoczeto potegowanie liczby {x} do liczby {y}")
    return x ** y


def main():
    while True:
        print("""
        KALKULATOR
        1) Dodawanie
        2) Odejmowanie
        3) Mnozenie
        4) Dzielenie
        5) Potegowanie
        6) Exit 
        """)
        option = float(input("Wybierz pozycje:"))

        x, y = _get_input()

        if option == 1:
            result = addition(x=x, y=y)

        elif option == 2:
            result = subtraction(x=x, y=y)

        elif option == 3:
            result = multiplication(x=x, y=y)

        elif option == 4:
            result = division(x=x, y=y)

        elif option == 5:
            result = involution(x=x, y=y)
    
        elif option == 6:
            break

        else:
            print("Niepoprawna odpowiedz")

        if option in range(1,6):
            print(f"Wynik to: {result}") 

        input("Kliknij aby kontynuowac")


if __name__ == "__main__":
    main()

def main():
    print("Taschenrechner")
    print("1 fuer Addition")
    print("2 fuer Subtraktion")
    print("3 fuer Multiplikation")
    print("4 fuer Division")

    wahl = input("Wahl eingeben: ")
    a, b = (input("a: "), input("b: "))
    
    if not a.isnumeric():
        print(f"a: {a} is not a valid number!")
        return
    if not b.isnumeric():
        print(f"b: {b} is not a valid number!")
        return

    match wahl:
        case "1":
            print("Gruppenmitglied 1 kann hier die Addition implementieren.")
            # Hier Funktion für Addition einfügen
        case "2":
            print("Gruppenmitglied 1 kann hier die Subtraktion implementieren.")
            # Hier Funktion für die Subtraktion einfügen
        case "3":
            print(f"{a} * {b} = {a * b}")
        case "4":
            print(f"{a} / {b} = {a / b}")
        case _:
            print("Falsche Auswahl, das Programm wird beendet.")

if __name__ == "__main__":
    main()

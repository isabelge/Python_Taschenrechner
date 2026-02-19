def main():
    print("Taschenrechner")
    print("1 fuer Addition")
    print("2 fuer Subtraktion")
    print("3 fuer Multiplikation")
    print("4 fuer Division")

    wahl = input("Wahl eingeben: ")

    match wahl:
        case "1":
            print("Gruppenmitglied 1 kann hier die Addition implementieren.")
            # Hier Funktion für Addition einfügen
        case "2":
            print("Gruppenmitglied 1 kann hier die Subtraktion implementieren.")
            # Hier Funktion für die Subtraktion einfügen
        case "3":
            print("Gruppenmitglied 2 kann hier die Multiplikation implementieren.")
            # Hier die Funktion für die Multiplikation einfügen
        case "4":
            print("Gruppenmitglied 2 kann hier die Division implementieren.")
            # Hier die Funktion für die Division einfügen
        case _:
            print("Falsche Auswahl, das Programm wird beendet.")

if __name__ == "__main__":
    main()
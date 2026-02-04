from pprint import pprint


def beolvasas(fajlnev):
    cipok = []
    with open(fajlnev, encoding="utf-8") as fajl:
        sorok = fajl.readlines()
        i = 1  # 0. sor = fejléc
        while i < len(sorok):
            sor = sorok[i]
            adat = sor.strip().split(",")

            cipo = {
                'title': adat[1],
                'color': adat[4],
                'full price': float(adat[5]),
                'current price': float(adat[6]),
                'publish date': adat[9].split('T')[0]
            }

            cipok.append(cipo)
            i += 1
    return cipok


def rendezes(cipok):
    print("1 - title")
    print("2 - color")
    print("3 - full price")
    print("4 - current price")
    print("5 - publish date")
    valasztas = int(input("Add meg a lehetőség számát: "))
    kulcsok = {
        1: 'title',
        2: 'color',
        3: 'full price',
        4: 'current price',
        5: 'publish date'
    }
    cipok.sort(key=lambda szam: szam[kulcsok[valasztas]])
    pprint(cipok)


def main():
    cipok = beolvasas("Nike_shoes_2023-04-16.csv")
    rendezes(cipok)


main()

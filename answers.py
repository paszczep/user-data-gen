from random import randint, choice, sample
from const import ZIP_CODES


def question_5(profile):
    """Ile srednio kilometrow przemierzasz autem w skali roku ?"""

    mapping = {
        "STUDENT": ["Do 10 tys."],
        "BUSINESS": [
            "10 - 25 tys.",
            "25 - 50 tys."],
        "FAMILY": ["powyzej 50 tys."],
        "OFFICE": ["Do 10 tys."],
        "SPORT": ["powyzej 50 tys."],
        "RANDOM": [
            "Do 10 tys.",
            "10 - 25 tys.",
            "25 - 50 tys.",
            "powyzej 50 tys."]}

    answer = choice(mapping[profile])

    return answer


def question_6(profile):
    """Jaki jest twoj przewazajacy tryb jazdy samochodem ?"""

    mapping = {
        "STUDENT": ["miejski"],
        "BUSINESS": [
            "mieszany",
            "miejski",
            "pozamiejski - dlugie trasy"],
        "FAMILY": ["pozamiejski - dlugie trasy"],
        "OFFICE": ["miejski"],
        "SPORT": [
            "mieszany",
            "miejski",
            "pozamiejski - dlugie trasy"],
        "RANDOM": [
            "miejski",
            "mieszany",
            "pozamiejski - dlugie trasy"]}

    answer = choice(mapping[profile])

    return answer


def question_7(profile):
    """Jaki jest typ drog uczeszczanych w dlugich trasach ?"""

    mapping = {"STUDENT": [],
               "BUSINESS": ["drogi krajowe"],
               "FAMILY": ["drogi ekspresowe i autostrady"],
               "OFFICE": ["drogi krajowe"],
               "SPORT": ["drogi ekspresowe i autostrady"],
               "RANDOM": ["drogi krajowe", "drogi ekspresowe i autostrady"]}

    if not mapping[profile]:
        answer = str()
    else:
        answer = mapping[profile].pop(randint(0, len(mapping[profile]) - 1))

    return answer


def question_8(profile):
    """Poszukujesz samochodu przeznaczonego dla ... ?"""

    mapping = {
        "STUDENT": [
            'jednej osoby',
            'pary bez dzieci'],
        "BUSINESS": [
            'rodziny 2+1',
            'rodziny 2+2'],
        "FAMILY": [
            'rodziny 2+3',
            'wiekszej liczby osob'],
        "OFFICE": ['jednej osoby'],
        "SPORT": [
            'jednej osoby',
            'pary bez dzieci'],
        "RANDOM": [
            'jednej osoby',
            'pary bez dzieci',
            'rodziny 2+1',
            'rodziny 2+2',
            'rodziny 2+3',
            'wiekszej liczby osob']}

    answer = choice(mapping[profile])

    return answer


def question_9(profile):
    """Jak czesto jedziesz samochodem na wycieczke lub wakacje ?"""

    mapping = {
        "STUDENT": ['raz w roku'],
        "BUSINESS": [
            'kilka razy w roku',
            "kilkanascie razy w roku"],
        "FAMILY": ["wiecej niz kilkanascie razy w roku"],
        "OFFICE": ['raz w roku'],
        "SPORT": ["wiecej niz kilkanascie razy w roku"],
        "RANDOM": [
            'raz w roku',
            'kilka razy w roku',
            "kilkanascie razy w roku",
            "wiecej niz kilkanascie razy w roku"]}

    answer = choice(mapping[profile])

    return answer


def question_10(profile):
    """Jaki budzet zamierzasz przeznaczyc na zakup nowego samochodu ?"""

    mapping = {
        "STUDENT": ['do 50 tys.'],
        "BUSINESS": [
            '200 - 250 tys.',
            'powyzej 250 tys.'],
        "FAMILY": [
            '75 - 100 tys.',
            '100 - 150 tys.',
            '150 - 200 tys.',
            '200 - 250 tys.'],
        "OFFICE": [
            'do 50 tys.',
            '50 - 75 tys.'],
        "SPORT": [
            '50 - 75 tys.',
            '75 - 100 tys.',
            '100 - 150 tys.',
            '150 - 200 tys.'],
        "RANDOM": [
            'do 50 tys.',
            '50 - 75 tys.',
            '75 - 100 tys.',
            '100 - 150 tys.',
            '150 - 200 tys.',
            '200 - 250 tys.',
            'powyzej 250 tys.']}

    answer = choice(mapping[profile])

    return answer


def question_11(profile):
    """Jak dlugo planujesz posiadac zakupiony samochod ?"""

    mapping = {
        "STUDENT": [
            'do 1 roku',
            '2 - 3 lata'],
        "BUSINESS": [
            '1 - 2 lata',
            '2 - 3 lata',
            '3 - 4 lata'],
        "FAMILY": [
            '3 - 4 lata',
            '4 - 5 lat',
            '5 - 6 lat',
            '6 - 8 lat',
            'powyzej 8 lat'],
        "OFFICE": [
            '1 - 2 lata',
            '2 - 3 lata',
            '3 - 4 lata'],
        "SPORT": [
            '3 - 4 lata',
            '4 - 5 lat',
            '5 - 6 lat',
            '6 - 8 lat'],
        "RANDOM": [
            'do 1 roku',
            '1 - 2 lata',
            '2 - 3 lata',
            '3 - 4 lata',
            '4 - 5 lat',
            '5 - 6 lat',
            '6 - 8 lat',
            'powyzej 8 lat']}

    answer = choice(mapping[profile])

    return answer


def question_12(profile):
    """Podaj kod pocztowy twojego miejsca zamieszkania."""

    mapping = {"STUDENT": ['mokotow', 'srodmiescie', 'bemowo'],
               "BUSINESS": ['jozefow', 'srodmiescie', 'mokotow'],
               "FAMILY": ['rembertow', 'bielany', 'bemowo', 'ursynow'],
               "OFFICE": ['praga', 'ursynow', 'ochota'],
               "SPORT": ['ursynow', 'bielany', 'bemowo'],
               "RANDOM": ['mokotow', 'rembertow', 'bielany', 'bemowo', 'srodmiescie', 'wlochy', 'ursynow',
                          'jozefow', 'ochota', 'praga']}

    district = choice(mapping[profile])
    answer = choice(ZIP_CODES[district])

    return answer


def question_13(profile):
    """Czy wystepuja u ciebie problemy ze zdrowiem mogace miec wplyw na komfort jazdy ?"""

    mapping = {"STUDENT": ['nie', 'tak'],
               "BUSINESS": ['tak'],
               "FAMILY": ['nie', 'tak'],
               "OFFICE": ['nie'],
               "SPORT": ['nie'],
               "RANDOM": ['nie', 'tak']}

    answer = choice(mapping[profile])

    return answer


def question_14(profile):
    """Zaznacz jakie problemy zdrowotne Cie dotycza :"""

    pool = ['problemy z kregoslupem', 'problemy z kolanami',
            'cukrzyca', 'alergie / choroby ukladu oddechowego']

    mapping = {"STUDENT": 0,
               "BUSINESS": 2,
               "FAMILY": 1,
               "OFFICE": 0,
               "SPORT": 0,
               "RANDOM": randint(0, len(pool))}

    answer = []
    for i in range(mapping[profile]):
        answer.append(pool.pop(randint(0, len(pool) - 1)))

    return answer


def question_15(profile):
    """Podaj swoj wzrost :"""

    mapping = {"STUDENT": [160, 195],
               "BUSINESS": [165, 193],
               "FAMILY": [175, 200],
               "OFFICE": [155, 180],
               "SPORT": [178, 192],
               "RANDOM": [150, 191]}

    answer = randint(mapping[profile][0], mapping[profile][1])

    return answer


def question_16(profile):
    """Czy zamierzasz przewozic zwierzeta ?"""

    mapping = {"STUDENT": ['nie', 'nie wiem'],
               "BUSINESS": ['nie'],
               "FAMILY": ['tak'],
               "OFFICE": ['nie'],
               "SPORT": ['tak', 'nie wiem'],
               "RANDOM": ['nie', 'tak', 'nie wiem']}

    answer = choice(mapping[profile])

    return answer


def question_17(profile):
    """W jaki sposob zamierzasz przewozic zwierzeta ?"""
    pool = [
        "w transporterze",
        "w przestrzeni bagazowej",
        "w przestrzeni pasazerskiej"]
    mapping = {"STUDENT": 0,
               "BUSINESS": 1,
               "FAMILY": 2,
               "OFFICE": 0,
               "SPORT": 1,
               "RANDOM": randint(0, len(pool))}
    answer = []
    for i in range(mapping[profile]):
        answer.append(pool.pop(randint(0, len(pool) - 1)))
    return answer


def question_18(profile):
    """Czy zamierzasz przewozic rowery ?"""
    mapping = {"STUDENT": ['nie', 'nie wiem'],
               "BUSINESS": ['nie', 'tak'],
               "FAMILY": ['tak'],
               "OFFICE": ['nie'],
               "SPORT": ['tak'],
               "RANDOM": ['tak', 'nie', 'nie wiem']}
    answer = choice(mapping[profile])
    return answer


def question_19(profile):
    """Na jakie sposoby chcialbys miec mozliwosc transportu rowerow ?"""
    pool = ['wewnatrz', 'bagaznik tylny', 'bagaznik dachowy']
    mapping = {"STUDENT": 0,
               "BUSINESS": 1,
               "FAMILY": 2,
               "OFFICE": 0,
               "SPORT": 2,
               "RANDOM": randint(0, len(pool))}
    answer = []
    for i in range(mapping[profile]):
        answer.append(pool.pop(randint(0, len(pool) - 1)))
    return answer


def question_20(profile):
    """Czy zamierzasz przewozic narty lub snowboard ?"""

    mapping = {"STUDENT": ['nie'],
               "BUSINESS": ['nie', 'tak'],
               "FAMILY": ['tak', 'nie wiem'],
               "OFFICE": ['nie', 'nie wiem'],
               "SPORT": ['tak'],
               "RANDOM": ['tak', 'nie', 'nie wiem']}

    answer = choice(mapping[profile])

    return answer


def question_21(profile):
    """Na jakie sposoby chcialbys miec mozliwosc transportu nart lub snowboardu ?"""
    pool = ["bagaznik dachowy", "wewnatrz", "bagaznik tylny"]
    mapping = {"STUDENT": 0,
               "BUSINESS": 1,
               "FAMILY": 2,
               "OFFICE": 0,
               "SPORT": 2,
               "RANDOM": randint(0, len(pool) - 1)}
    answer = []
    for i in range(mapping[profile]):
        answer.append(pool.pop(randint(0, len(pool) - 1)))
    return answer


def question_22(profile):
    """Jakie inne rzeczy bedziesz przewozic?"""

    mapping = {"STUDENT": [],
               "BUSINESS": [],
               "FAMILY": ['sprzet campingowy', 'meble / gabaryty'],
               "OFFICE": ['wyposazenie biurowe'],
               "SPORT": ['sprzet campingowy',
                         'lekki sprzet sportowy (np. kite)'],
               "RANDOM": ['sprzet campingowy',
                          'lekki sprzet sportowy (np. kite, bron mysliwska)',
                          'meble / gabaryty',
                          'wyposazenie biurowe']}
    answer = []
    how_many = randint(0, len(mapping[profile]))
    for i in range(1, how_many):
        answer.append(mapping[profile].pop(randint(0, how_many - i)))

    return answer


def question_23(profile):
    """Jesli zamierzasz holowac przyczepe prosze zaznacz jakie rodzaje przyczep to beda ?"""

    mapping = {"STUDENT": [],
               "BUSINESS": [],
               "FAMILY": [],
               "OFFICE": [],
               "SPORT": ["rekreacyjna"],
               "RANDOM": ["towarowa lekka",
                          "rekreacyjna",
                          "towarowa ciezka / laweta"]}

    answer = []
    how_many = randint(0, len(mapping[profile]))
    for i in range(0, how_many):
        answer.append(mapping[profile].pop(randint(0, how_many - i - 1)))

    return answer


def question_24(profile):
    """Jak istotny jest dla Ciebie koszt paliwa ?"""

    mapping = {"STUDENT": [7, 10],
               "BUSINESS": [0, 5],
               "FAMILY": [5, 10],
               "OFFICE": [4, 10],
               "SPORT": [3, 8],
               "RANDOM": [0, 10]}

    answer = randint(mapping[profile][0], mapping[profile][1])

    return answer


def question_25(profile):
    """Jak wazne jest dla Ciebie bezpieczenstwo ?"""

    mapping = {"STUDENT": [0, 5],
               "BUSINESS": [2, 7],
               "FAMILY": [7, 10],
               "OFFICE": [4, 10],
               "SPORT": [3, 8],
               "RANDOM": [0, 10]}

    answer = randint(mapping[profile][0], mapping[profile][1])

    return answer


def question_26(profile):
    """Jak wazny jest dla Ciebie komfort jazdy?"""

    mapping = {"STUDENT": [0, 5],
               "BUSINESS": [5, 10],
               "FAMILY": [7, 10],
               "OFFICE": [4, 10],
               "SPORT": [3, 8],
               "RANDOM": [0, 10]}

    answer = randint(mapping[profile][0], mapping[profile][1])

    return answer


def question_27(profile):
    """Jak wazna jest dla Ciebie latwosc parkowania?"""

    mapping = {"STUDENT": [0, 5],
               "BUSINESS": [2, 7],
               "FAMILY": [7, 10],
               "OFFICE": [6, 10],
               "SPORT": [3, 8],
               "RANDOM": [0, 10]}

    answer = randint(mapping[profile][0], mapping[profile][1])

    return answer


def question_28(profile):
    """Jak wazna jest dla Ciebie dynamika jazdy?"""

    mapping = {"STUDENT": [0, 5],
               "BUSINESS": [2, 7],
               "FAMILY": [7, 10],
               "OFFICE": [4, 10],
               "SPORT": [3, 8],
               "RANDOM": [0, 10]}

    answer = randint(mapping[profile][0], mapping[profile][1])

    return answer


def question_29(profile):
    """Jaki rodzaj nadwozia preferujesz ?"""

    mapping = {
        "STUDENT": [
            "hatchback",
            "sedan"],
        "BUSINESS": [
            "sedan",
            "SUV",
            "coupe"],
        "FAMILY": [
            "kombi",
            "minivan",
            "SUV"],
        "OFFICE": [
            "hatchback",
            "crossover",
            "coupe"],
        "SPORT": [
            "SUV",
            "crossover",
            "kombi"],
        "RANDOM": [
            "hatchback",
            "sedan",
            "kombi",
            "minivan",
            "SUV",
            "crossover",
            "coupe",
            "cabrio",
            "dostawczy",
            "pickup"]}

    answer = choice(mapping[profile])

    return answer


def question_30(profile):
    """Jaki rodzaj silnika preferujesz ?"""

    mapping = {"STUDENT": ["spalinowy"],
               "BUSINESS": ["spalinowy", "hybrydowy"],
               "FAMILY": ["hybrydowy", "spalinowy"],
               "OFFICE": ["spalinowy"],
               "SPORT": ["hybrydowy"],
               "RANDOM": ["elektryczny", "hybrydowy", "spalinowy"]}

    answer = choice(mapping[profile])

    return answer


def question_31(profile):
    """Jaki rodzaj paliwa preferujesz ?"""

    mapping = {"STUDENT": ["benzyna", "gaz"],
               "BUSINESS": ["benzyna"],
               "FAMILY": ["benzyna", "diesel"],
               "OFFICE": ["benzyna", "gaz"],
               "SPORT": ["benzyna", "diesel"],
               "RANDOM": ["benzyna", "diesel", "gaz"]}

    answer = choice(mapping[profile])

    return answer


def question_32(profile):
    """Jaki rodzaj hybrydy preferujesz ?"""

    mapping = {"STUDENT": [],
               "BUSINESS": ['mild', 'plug-in', 'full'],
               "FAMILY": ['mild', 'plug-in', 'full'],
               "OFFICE": ['mild', 'plug-in', 'full'],
               "SPORT": ['mild', 'plug-in', 'full'],
               "RANDOM": ['mild', 'plug-in', 'full']}

    if not mapping[profile]:
        answer = str()
    else:
        answer = choice(mapping[profile])
    return answer


def question_33(profile):
    """Jaki rodzaj przeniesienia napedu preferujesz ?"""

    mapping = {
        "STUDENT": ["manualne"],
        "BUSINESS": ["manualne", "automatyczne"],
        "FAMILY": ["manualne", "automatyczne"],
        "OFFICE": ["automatyczne"],
        "SPORT": ["manualne", "automatyczne"],
        "RANDOM": [
            "manualne",
            "automatyczne",
            "automatyczne bezstopniowe"]}

    answer = choice(mapping[profile])

    return answer


def question_34(profile):
    """Zaznacz preferowane marki :"""

    pool = ["Dacia", "Skoda", "Fiat", "Seat", "Kia",
            "Hyundai", "Renault", "Ford", "Suzuki",
            "Volkswagen", "Peugeot", "Opel", "Mitsubishi", "Nissan",
            "Honda", "Subaru", "Toyota", "Mazda", "Smart", "Mini",
            "Alfa Romeo", "Citroen", "Jeep", "Volvo", "Audi", "Lexus",
            "Infiniti", "Jaguar", "Land Rover", "BMW", "Mercedes", "Porsche"]

    mapping = {"STUDENT": pool[0:11],
               "BUSINESS": pool[-16:],
               "FAMILY": pool,
               "OFFICE": pool[0:-13],
               "SPORT": pool[3:-2],
               "RANDOM": pool}
    # answer = []
    how_many = randint(1, len(mapping[profile]))
    # for i in range(0, how_many):
    #     answer.append(mapping[profile].pop(randint(0, how_many - i - 1)))

    answer = sample(mapping[profile], how_many)

    return answer


def question_35(profile):
    """Podaj preferencje co do wykonczenia wnetrza:"""

    pool = ["Material", "Welur", "Czesciowo skorzane", "Alkantara", "Skora"]

    mapping = {"STUDENT": pool[:2],
               "BUSINESS": pool[-2:],
               "FAMILY": pool,
               "OFFICE": pool[:3],
               "SPORT": pool[1:],
               "RANDOM": pool}

    answer = []
    how_many = randint(1, len(mapping[profile]))
    for i in range(0, how_many):
        answer.append(mapping[profile].pop(randint(0, how_many - i - 1)))
    return answer


def question_36(profile):
    """Wybierz preferowane dodatkowe wyposazenie"""

    pool = [
        'Alufelgi',
        'Dach panoramiczny',
        'Hak',
        'HUD (wyswietlacz przezierny)',
        'ISOFIX',
        'Klimatyzacja',
        'Klimatyzacja strefowa',
        'Nawigacja GPS',
        'Ogrzewanie postojowe',
        'Podgrzewana przednia szyba',
        'Podgrzewane lusterka boczne',
        'Podgrzewane lusterka',
        'Podgrzewane siedzenia',
        'Przyciemniane szyby',
        'Wielofunkcyjna kierownica']

    mapping = {"STUDENT": 5,
               "BUSINESS": 15,
               "FAMILY": 10,
               "OFFICE": 7,
               "SPORT": 10,
               "RANDOM": randint(0, len(pool))}

    answer = []
    how_many = randint(0, mapping[profile])
    for i in range(0, how_many):
        answer.append(pool.pop(randint(0, how_many - i - 1)))
    return answer


def question_37(profile):
    """Wybierz preferowane systemy wspomagania :"""

    pool = [
        "ABS",
        "ASR (kontrola trakcji)",
        "Asystent parkowania",
        "Asystent pasa ruchu",
        "Czujnik deszczu",
        "Czujnik martwego pola",
        "Czujnik zmierzchu",
        "Czujniki parkowania przednie",
        "Czujniki parkowania tylne",
        "ESP (stabilizacja toru jazdy)",
        "Kamera cofania",
        "System Start-Stop",
        "Swiatla LED",
        "Swiatla przeciwmgielne przednie"
        "Swiatla ksenonowe"
        "Tempomat",
        "Tempomat aktywny"]

    mapping = {"STUDENT": 5,
               "BUSINESS": 15,
               "FAMILY": 10,
               "OFFICE": 7,
               "SPORT": 10,
               "RANDOM": randint(1, len(pool))}

    answer = []
    how_many = randint(0, mapping[profile])
    for i in range(0, how_many):
        answer.append(pool.pop(randint(0, how_many - i - 1)))
    return answer


def question_38(profile):
    """Wybierz marke samochodu, ktory wedlug Ciebie spelni Twoje oczekiwania:"""
    return profile


def question_39(profile):
    """Czy wazniejsza jest dla Ciebie jakosc czy cena czesci samochodowych?"""

    pool = ["Tylko cena sie liczy", "Glownie cena sie liczy", "Sa rownie istotne", "Wazniejsza jest jakosc",
            "Tylko jakosc sie liczy"]

    mapping = {
        "STUDENT": pool[0:2],
        "BUSINESS": pool[-2:],
        "FAMILY": pool[1:4],
        "OFFICE": pool[1:3],
        "SPORT": pool[2:4],
        "RANDOM": pool}

    # answer = mapping[profile].pop(randint(0, len(mapping[profile]) - 1))
    answer = choice(mapping[profile])

    return answer


def question_40(profile):
    """Czy zamienna czesc, ktora kupujesz, musi byc idealnym zamiennikiem czesci producenta?"""

    mapping = {
        "STUDENT": ["nie"],
        "BUSINESS": ["tak"],
        "FAMILY": ["tak", "nie"],
        "OFFICE": ["nie"],
        "SPORT": ["tak"],
        "RANDOM": ["tak", "nie"]}

    answer = choice(mapping[profile])
    return answer

class DbDatabase:
    def __init__(self) -> None:
        # Define the maximum number of Digimon evolutions
        max_evolutions = 404

        # Initialize the Digimon evolution array
        self.digiEvolution = [
            [["" for _ in range(8)] for _ in range(2)] for _ in range(max_evolutions)]

        # Initialize the index variable
        i = 0

        # kuramon
        # for
        self.digiEvolution[i][1][0] = "Tsumemon"
        self.digiEvolution[i][1][1] = "Pagumon"
        self.digiEvolution[i][1][2] = "Arcadiamon In-Tr"
        i += 1

        # pabumon
        # for
        self.digiEvolution[i][1][0] = "Tanemon"
        self.digiEvolution[i][1][1] = "Yokomon"
        self.digiEvolution[i][1][2] = "Motimon"
        i += 1

        # punimon
        # for
        self.digiEvolution[i][1][0] = "Tsunomon"
        self.digiEvolution[i][1][1] = "Nyaromon"
        i += 1

        # botamon
        # for
        self.digiEvolution[i][1][0] = "Koromon"
        self.digiEvolution[i][1][1] = "Wanyamon"
        i += 1

        # poyomon
        # for
        self.digiEvolution[i][1][0] = "Tokomon"
        self.digiEvolution[i][1][1] = "Bukamon"
        i += 1

        # arcadiamon In-Tr.
        # from
        self.digiEvolution[i][0][0] = "Kuramon"

        # for
        self.digiEvolution[i][1][0] = "Arcadiamon Rookie"
        i += 1

        # koromon
        # from
        self.digiEvolution[i][0][0] = "Botamon"

        # for
        self.digiEvolution[i][1][0] = "Agumon"
        self.digiEvolution[i][1][1] = "Guilmon"
        self.digiEvolution[i][1][2] = "ToyAgumon"
        self.digiEvolution[i][1][3] = "Hackmon"
        self.digiEvolution[i][1][4] = "Dracomon"
        self.digiEvolution[i][1][5] = "Shoutmon"
        i += 1

        # tanemon
        # from
        self.digiEvolution[i][0][0] = "Pabumon"

        # for
        self.digiEvolution[i][1][0] = "Lalamon"
        self.digiEvolution[i][1][1] = "Palmon"
        self.digiEvolution[i][1][2] = "Renamon"
        self.digiEvolution[i][1][3] = "FanBeemon"
        i += 1

        # tsunomon
        # from
        self.digiEvolution[i][0][0] = "Punimon"

        # for
        self.digiEvolution[i][1][0] = "Gabumon"
        self.digiEvolution[i][1][1] = "Gabumon BLK"
        self.digiEvolution[i][1][2] = "Goblimon"
        self.digiEvolution[i][1][3] = "Veemon"
        self.digiEvolution[i][1][4] = "Zubamon"
        self.digiEvolution[i][1][5] = "Monodramon"
        i += 1

        # tsumemon
        # from
        self.digiEvolution[i][0][0] = "Kuramon"

        # for
        self.digiEvolution[i][1][0] = "Agumon BLK"
        self.digiEvolution[i][1][1] = "Keramon"
        self.digiEvolution[i][1][2] = "DemiDevimon"
        self.digiEvolution[i][1][3] = "Dracmon"
        i += 1

        # tokomon
        # from
        self.digiEvolution[i][0][0] = "Poyomon"

        # for
        self.digiEvolution[i][1][0] = "Patamon"
        self.digiEvolution[i][1][1] = "Falcomon"
        self.digiEvolution[i][1][2] = "Hawkmon"
        self.digiEvolution[i][1][3] = "Lucemon"
        self.digiEvolution[i][1][4] = "Sistermon Blanc"
        i += 1

        # nyaromon
        # from
        self.digiEvolution[i][0][0] = "Punimon"

        # for
        self.digiEvolution[i][1][0] = "Armadillomon"
        self.digiEvolution[i][1][1] = "Terriermon"
        self.digiEvolution[i][1][2] = "Salamon"
        self.digiEvolution[i][1][3] = "Lunamon"
        i += 1

        # Pagumon
        # from
        self.digiEvolution[i][0][0] = "Kuramon"

        # for
        self.digiEvolution[i][1][0] = "Impmon"
        self.digiEvolution[i][1][1] = "Gazimon"
        self.digiEvolution[i][1][2] = "Lopmon"
        self.digiEvolution[i][1][3] = "Chuumon"
        i += 1

        # yokomon
        # from
        self.digiEvolution[i][0][0] = "Pabumon"

        # for
        self.digiEvolution[i][1][0] = "Elecmon"
        self.digiEvolution[i][1][1] = "Biyomon"
        self.digiEvolution[i][1][2] = "Wormmon"
        self.digiEvolution[i][1][3] = "Mushroomon"
        i += 1

        # bukamon
        # from
        self.digiEvolution[i][0][0] = "Poyomon"

        # for
        self.digiEvolution[i][1][0] = "Otamamon"
        self.digiEvolution[i][1][1] = "Gomamon"
        self.digiEvolution[i][1][2] = "Syakomon"
        self.digiEvolution[i][1][3] = "Betamon"
        i += 1

        # motimon
        # from
        self.digiEvolution[i][0][0] = "Pabumon"

        # for
        self.digiEvolution[i][1][0] = "Gotsumon"
        self.digiEvolution[i][1][1] = "Solarmon"
        self.digiEvolution[i][1][2] = "Tentomon"
        self.digiEvolution[i][1][3] = "Hagurumon"
        i += 1

        # wanyamon
        # from
        self.digiEvolution[i][0][0] = "Botamon"

        # for
        self.digiEvolution[i][1][0] = "Gaomon"
        self.digiEvolution[i][1][1] = "Kudamon"
        self.digiEvolution[i][1][2] = "Dorumon"
        self.digiEvolution[i][1][3] = "Ryudamon"
        i += 1

        # agumon
        # from
        self.digiEvolution[i][0][0] = "Koromon"

        # for
        self.digiEvolution[i][1][0] = "Greymon"
        self.digiEvolution[i][1][1] = "GeoGreymon"
        self.digiEvolution[i][1][2] = "Sukamon"
        self.digiEvolution[i][1][3] = "Tyrannomon"
        self.digiEvolution[i][1][4] = "Meramon"
        self.digiEvolution[i][1][5] = "Agunimon"
        i += 1

        # agumon blk
        # from
        self.digiEvolution[i][0][0] = "Tsumemon"

        # for
        self.digiEvolution[i][1][0] = "Growlmon"
        self.digiEvolution[i][1][1] = "Greymon(Blue)"
        self.digiEvolution[i][1][2] = "Cyclonemon"
        self.digiEvolution[i][1][3] = "Tankmon"
        self.digiEvolution[i][1][4] = "Tyrannomon"
        self.digiEvolution[i][1][5] = "Monochromon"
        i += 1

        # arcadiamon rookie
        # from
        self.digiEvolution[i][0][0] = "Arcadiamon In-Tr"

        # for
        self.digiEvolution[i][1][0] = "Arcadiamon Champion"
        self.digiEvolution[i][1][1] = "Kurisarimon"
        self.digiEvolution[i][1][2] = "Leomon"
        i += 1

        # armadillomon
        # from
        self.digiEvolution[i][0][0] = "Nyaromon"

        # for
        self.digiEvolution[i][1][0] = "Ankylomon"
        self.digiEvolution[i][1][1] = "Geremon"
        self.digiEvolution[i][1][2] = "GoldNumemon"
        self.digiEvolution[i][1][3] = "Cyclonemon"
        self.digiEvolution[i][1][4] = "Tankmon"
        self.digiEvolution[i][1][5] = "Golemon"
        i += 1

        # impmon
        # from
        self.digiEvolution[i][0][0] = "Pagumon"

        # for
        self.digiEvolution[i][1][0] = "IceDevimon"
        self.digiEvolution[i][1][1] = "Wizardmon"
        self.digiEvolution[i][1][2] = "Ogremon"
        self.digiEvolution[i][1][3] = "Socerimon"
        self.digiEvolution[i][1][4] = "Bakemon"
        self.digiEvolution[i][1][5] = "BlackGatomon"
        i += 1

        # Elecmon
        # from
        self.digiEvolution[i][0][0] = "Yokomon"

        # for
        self.digiEvolution[i][1][0] = "Garurumon"
        self.digiEvolution[i][1][1] = "Garurumon BLK"
        self.digiEvolution[i][1][2] = "Geremon"
        self.digiEvolution[i][1][3] = "Sukamon"
        self.digiEvolution[i][1][4] = "Nanimon"
        self.digiEvolution[i][1][5] = "Leomon"
        i += 1

        # Otamamon
        # from
        self.digiEvolution[i][0][0] = "Bukamon"

        # for
        self.digiEvolution[i][1][0] = "ShellNumemon"
        self.digiEvolution[i][1][1] = "Gekomon"
        self.digiEvolution[i][1][2] = "Seadramon"
        self.digiEvolution[i][1][3] = "Numemon"
        self.digiEvolution[i][1][4] = "Coelamon"
        self.digiEvolution[i][1][5] = "Raremon"
        i += 1

        # Gaomon
        # from
        self.digiEvolution[i][0][0] = "Wanyamon"

        # for
        self.digiEvolution[i][1][0] = "Ogremon"
        self.digiEvolution[i][1][1] = "GaoGamon"
        self.digiEvolution[i][1][2] = "Gargomon"
        self.digiEvolution[i][1][3] = "Togemon"
        self.digiEvolution[i][1][4] = "Leomon"
        self.digiEvolution[i][1][5] = "Sangloupmon"
        i += 1

        # Gazimon
        # from
        self.digiEvolution[i][0][0] = "Pagumon"

        # for
        self.digiEvolution[i][1][0] = "GaoGamon"
        self.digiEvolution[i][1][1] = "Garurumon BLK"
        self.digiEvolution[i][1][2] = "Kurisarimon"
        self.digiEvolution[i][1][3] = "Dorugamon"
        self.digiEvolution[i][1][4] = "Nanimon"
        self.digiEvolution[i][1][5] = "Leomon"
        i += 1

        # Gabumon
        # from
        self.digiEvolution[i][0][0] = "Tsunomon"

        # for
        self.digiEvolution[i][1][0] = "Garurumon"
        self.digiEvolution[i][1][1] = "Dorugamon"
        self.digiEvolution[i][1][2] = "Numemon"
        self.digiEvolution[i][1][3] = "Veedramon"
        self.digiEvolution[i][1][4] = "Frigimon"
        self.digiEvolution[i][1][5] = "Lobomon"
        i += 1

        # Gabumon BLK
        # from
        self.digiEvolution[i][0][0] = "Tsunomon"

        # for
        self.digiEvolution[i][1][0] = "Garurumon BLK"
        self.digiEvolution[i][1][1] = "Vegiemon"
        self.digiEvolution[i][1][2] = "Frigimon"
        self.digiEvolution[i][1][3] = "Reppamon"
        self.digiEvolution[i][1][4] = "Raremon"
        i += 1

        # Guilmon
        # from
        self.digiEvolution[i][0][0] = "Koromon"

        # for
        self.digiEvolution[i][1][0] = "GeoGreymon"
        self.digiEvolution[i][1][1] = "Growlmon"
        self.digiEvolution[i][1][2] = "Greymon(Blue)"
        self.digiEvolution[i][1][3] = "Tyrannomon"
        self.digiEvolution[i][1][4] = "Meramon"
        self.digiEvolution[i][1][5] = "Agunimon"
        i += 1

        # Kudamon
        # from
        self.digiEvolution[i][0][0] = "Wanyamon"

        # for
        self.digiEvolution[i][1][0] = "Angemon"
        self.digiEvolution[i][1][1] = "GoldNumemon"
        self.digiEvolution[i][1][2] = "Peckmon"
        self.digiEvolution[i][1][3] = "Reppamon"
        self.digiEvolution[i][1][4] = "Lobomon"
        i += 1

        # Keramon
        # from
        self.digiEvolution[i][0][0] = "Tsumemon"

        # for
        self.digiEvolution[i][1][0] = "Wizardmon"
        self.digiEvolution[i][1][1] = "Kurisarimon"
        self.digiEvolution[i][1][2] = "Bakemon"
        self.digiEvolution[i][1][3] = "PlatinumSukamon"
        self.digiEvolution[i][1][4] = "Arcadiamon Champion"
        i += 1

        # Gotsumon
        # from
        self.digiEvolution[i][0][0] = "Motimon"

        # for
        self.digiEvolution[i][1][0] = "Ankylomon"
        self.digiEvolution[i][1][1] = "Clockmon"
        self.digiEvolution[i][1][2] = "Starmon"
        self.digiEvolution[i][1][3] = "Tankmon"
        self.digiEvolution[i][1][4] = "Icemon"
        self.digiEvolution[i][1][5] = "Golemon"
        i += 1

        # Goblimon
        # from
        self.digiEvolution[i][0][0] = "Tsunomon"

        # for
        self.digiEvolution[i][1][0] = "GaoGamon"
        self.digiEvolution[i][1][1] = "Growlmon"
        self.digiEvolution[i][1][2] = "Greymon(Blue)"
        self.digiEvolution[i][1][3] = "Nanimon"
        self.digiEvolution[i][1][4] = "Coredramon(Green)"
        i += 1

        # Gomamon
        # from
        self.digiEvolution[i][0][0] = "Bukamon"

        # for
        self.digiEvolution[i][1][0] = "Ankylomon"
        self.digiEvolution[i][1][1] = "Ikkakumon"
        self.digiEvolution[i][1][2] = "Socerimon"
        self.digiEvolution[i][1][3] = "Frigimon"
        self.digiEvolution[i][1][4] = "Icemon"
        i += 1

        # Syakomon
        # from
        self.digiEvolution[i][0][0] = "Bukamon"

        # for
        self.digiEvolution[i][1][0] = "Ikkakumon"
        self.digiEvolution[i][1][1] = "ShellNumemon"
        self.digiEvolution[i][1][2] = "Gekomon"
        self.digiEvolution[i][1][3] = "Seadramon"
        self.digiEvolution[i][1][4] = "Coelamon"
        i += 1

        # Zubamon
        # from
        self.digiEvolution[i][0][0] = "Tsunomon"

        # for
        self.digiEvolution[i][1][0] = "Zubaeagermon"
        self.digiEvolution[i][1][1] = "BaoHuckmon"
        self.digiEvolution[i][1][2] = "GoldNumemon"
        self.digiEvolution[i][1][3] = "Ginryumon"
        i += 1

        # Solarmon
        # from
        self.digiEvolution[i][0][0] = "Motimon"

        # for
        self.digiEvolution[i][1][0] = "Clockmon"
        self.digiEvolution[i][1][1] = "Starmon"
        self.digiEvolution[i][1][2] = "Meramon"
        self.digiEvolution[i][1][3] = "Guardromon(Gold)"
        self.digiEvolution[i][1][4] = "Golemon"
        i += 1

        # Chuumon
        # from
        self.digiEvolution[i][0][0] = "Pagumon"

        # for
        self.digiEvolution[i][1][0] = "Raremon"
        self.digiEvolution[i][1][1] = "Sukamon"
        self.digiEvolution[i][1][2] = "BlackGatomon"
        self.digiEvolution[i][1][3] = "Nanimon"
        i += 1

        # Terriermon
        # from
        self.digiEvolution[i][0][0] = "Nyaromon"

        # for
        self.digiEvolution[i][1][0] = "Gargomon"
        self.digiEvolution[i][1][1] = "Ikkakumon"
        self.digiEvolution[i][1][2] = "Gatomon"
        self.digiEvolution[i][1][3] = "Rapidmon Armor"
        self.digiEvolution[i][1][4] = "Unimon"
        i += 1

        # Tentomon
        # from
        self.digiEvolution[i][0][0] = "Motimon"

        # for
        self.digiEvolution[i][1][0] = "Kabuterimon"
        self.digiEvolution[i][1][1] = "Kuwagamon"
        self.digiEvolution[i][1][2] = "Sunflowmon"
        self.digiEvolution[i][1][3] = "Stingmon"
        self.digiEvolution[i][1][4] = "Waspmon"
        i += 1

        # ToyAgumon
        # from
        self.digiEvolution[i][0][0] = "Koromon"

        # for
        self.digiEvolution[i][1][0] = "Clockmon"
        self.digiEvolution[i][1][1] = "Guardromon"
        self.digiEvolution[i][1][2] = "Greymon"
        self.digiEvolution[i][1][3] = "Sukamon"
        self.digiEvolution[i][1][4] = "Starmon"
        self.digiEvolution[i][1][5] = "Guardromon(Gold)"
        i += 1

        # Dracmon
        # from
        self.digiEvolution[i][0][0] = "Tsumemon"

        # for
        self.digiEvolution[i][1][0] = "Arcadiamon Champion"
        self.digiEvolution[i][1][1] = "Sangloupmon"
        self.digiEvolution[i][1][2] = "Raremon"
        self.digiEvolution[i][1][3] = "Sistermon Ciel"
        self.digiEvolution[i][1][4] = "Devimon"
        i += 1

        # Dracomon
        # from
        self.digiEvolution[i][0][0] = "Koromon"

        # for
        self.digiEvolution[i][1][0] = "Coredramon(Blue)"
        self.digiEvolution[i][1][1] = "Coredramon(Green)"
        self.digiEvolution[i][1][2] = "Veedramon"
        self.digiEvolution[i][1][3] = "Ginryumon"
        i += 1

        # Dorumon
        # from
        self.digiEvolution[i][0][0] = "Wanyamon"

        # for
        self.digiEvolution[i][1][0] = "Guardromon"
        self.digiEvolution[i][1][1] = "Cyclonemon"
        self.digiEvolution[i][1][2] = "Dorugamon"
        self.digiEvolution[i][1][3] = "Waspmon"
        self.digiEvolution[i][1][4] = "Raptordramon"
        i += 1

        # Hagurumon
        # from
        self.digiEvolution[i][0][0] = "Motimon"

        # for
        self.digiEvolution[i][1][0] = "Guardromon"
        self.digiEvolution[i][1][1] = "Clockmon"
        self.digiEvolution[i][1][2] = "GoldNumemon"
        self.digiEvolution[i][1][3] = "Starmon"
        self.digiEvolution[i][1][4] = "PlatinumSukamon"
        i += 1

        # Patamon
        # from
        self.digiEvolution[i][0][0] = "Tokomon"

        # for
        self.digiEvolution[i][1][0] = "ExVeemon"
        self.digiEvolution[i][1][1] = "Angemon"
        self.digiEvolution[i][1][2] = "Gatomon"
        self.digiEvolution[i][1][3] = "Birdramon"
        self.digiEvolution[i][1][4] = "Reppamon"
        self.digiEvolution[i][1][5] = "Unimon"
        i += 1

        # Hackmon
        # from
        self.digiEvolution[i][0][0] = "Koromon"

        # for
        self.digiEvolution[i][1][0] = "Greymon"
        self.digiEvolution[i][1][1] = "GeoGreymon"
        self.digiEvolution[i][1][2] = "PlatinumSukamon"
        self.digiEvolution[i][1][3] = "Zubaeagermon"
        self.digiEvolution[i][1][4] = "BaoHuckmon"
        self.digiEvolution[i][1][5] = "Monochromon"
        i += 1

        # Palmon
        # from
        self.digiEvolution[i][0][0] = "Tanemon"

        # for
        self.digiEvolution[i][1][0] = "Woodmon"
        self.digiEvolution[i][1][1] = "Kuwagamon"
        self.digiEvolution[i][1][2] = "Sunflowmon"
        self.digiEvolution[i][1][3] = "Togemon"
        self.digiEvolution[i][1][4] = "Vegiemon"
        self.digiEvolution[i][1][5] = "MudFrigimon"
        i += 1

        # DemiDevimon
        # from
        self.digiEvolution[i][0][0] = "Tsumemon"

        # for
        self.digiEvolution[i][1][0] = "IceDevimon"
        self.digiEvolution[i][1][1] = "Kyubimon"
        self.digiEvolution[i][1][2] = "Kurisarimon"
        self.digiEvolution[i][1][3] = "Devimon"
        self.digiEvolution[i][1][4] = "Bakemon"
        i += 1

        # Biyomon
        # from
        self.digiEvolution[i][0][0] = "Aquilamon"

        # for
        self.digiEvolution[i][1][0] = "Kabuterimon"
        self.digiEvolution[i][1][1] = "Kyubimon"
        self.digiEvolution[i][1][2] = "Birdramon"
        self.digiEvolution[i][1][3] = "Airdramon"
        i += 1

        # Falcomon
        # from
        self.digiEvolution[i][0][0] = "Tokomon"

        # for
        self.digiEvolution[i][1][0] = "Aquilamon"
        self.digiEvolution[i][1][1] = "ExVeemon"
        self.digiEvolution[i][1][2] = "Stingmon"
        self.digiEvolution[i][1][3] = "Peckmon"
        i += 1

        # FanBeemon
        # from
        self.digiEvolution[i][0][0] = "Tanemon"

        # for
        self.digiEvolution[i][1][0] = "Guardromon(Gold)"
        self.digiEvolution[i][1][1] = "Raptordramon"
        self.digiEvolution[i][1][2] = "Stingmon"
        self.digiEvolution[i][1][3] = "Waspmon"
        self.digiEvolution[i][1][4] = "Togemon"
        i += 1

        # Veemon
        # from
        self.digiEvolution[i][0][0] = "Tsunomon"

        # for
        self.digiEvolution[i][1][0] = "ExVeemon"
        self.digiEvolution[i][1][1] = "Veedramon"
        self.digiEvolution[i][1][2] = "Flamedramon"
        self.digiEvolution[i][1][3] = "Magnamon"
        self.digiEvolution[i][1][4] = "Lobomon"
        self.digiEvolution[i][1][5] = "Strikedramon"
        i += 1

        # Salamon
        # from
        self.digiEvolution[i][0][0] = "Nyaromon"

        # for
        self.digiEvolution[i][1][0] = "Socerimon"
        self.digiEvolution[i][1][1] = "Gatomon"
        self.digiEvolution[i][1][2] = "Veedramon"
        self.digiEvolution[i][1][3] = "Frigimon"
        self.digiEvolution[i][1][4] = "Reppamon"
        self.digiEvolution[i][1][5] = "BaoHuckmon"
        i += 1

        # Betamon
        # from
        self.digiEvolution[i][0][0] = "Bukamon"

        # for
        self.digiEvolution[i][1][0] = "ShellNumemon"
        self.digiEvolution[i][1][1] = "Gekomon"
        self.digiEvolution[i][1][2] = "Seadramon"
        self.digiEvolution[i][1][3] = "Numemon"
        self.digiEvolution[i][1][4] = "Vegiemon"
        self.digiEvolution[i][1][5] = "Airdramon"
        i += 1

        # Hawkmon
        # from
        self.digiEvolution[i][0][0] = "Tokomon"

        # for
        self.digiEvolution[i][1][0] = "Aquilamon"
        self.digiEvolution[i][1][1] = "Birdramon"
        self.digiEvolution[i][1][2] = "Peckmon"
        self.digiEvolution[i][1][3] = "Meramon"
        self.digiEvolution[i][1][4] = "Airdramon"
        i += 1

        # Mushroomon
        # from
        self.digiEvolution[i][0][0] = "Yokomon"

        # for
        self.digiEvolution[i][1][0] = "MudFrigimon"
        self.digiEvolution[i][1][1] = "Woodmon"
        self.digiEvolution[i][1][2] = "Sunflowmon"
        self.digiEvolution[i][1][3] = "Vegiemon"
        i += 1

        # Monodramon
        # from
        self.digiEvolution[i][0][0] = "Tsunomon"

        # for
        self.digiEvolution[i][1][0] = "Coredramon(Blue)"
        self.digiEvolution[i][1][1] = "Strikedramon"
        self.digiEvolution[i][1][2] = "Raptordramon"
        self.digiEvolution[i][1][3] = "Kurisarimon"
        self.digiEvolution[i][1][4] = "Dorugamon"
        i += 1

        # Lalamon
        # from
        self.digiEvolution[i][0][0] = "Tanemon"

        # for
        self.digiEvolution[i][1][0] = "Woodmon"
        self.digiEvolution[i][1][1] = "Sunflowmon"
        self.digiEvolution[i][1][2] = "Togemon"
        self.digiEvolution[i][1][3] = "Vegiemon"
        i += 1

        # Lucemon
        # from
        self.digiEvolution[i][0][0] = "Tokomon"

        # for
        self.digiEvolution[i][1][0] = "Angemon"
        self.digiEvolution[i][1][1] = "Devimon"
        self.digiEvolution[i][1][2] = "Lucemon FM"
        i += 1

        # Lunamon
        # from
        self.digiEvolution[i][0][0] = "Nyaromon"

        # for
        self.digiEvolution[i][1][0] = "Sangloupmon"
        self.digiEvolution[i][1][1] = "Lekismon"
        self.digiEvolution[i][1][2] = "Sistermon Ciel"
        self.digiEvolution[i][1][3] = "Gatomon"
        i += 1

        # Renamon
        # from
        self.digiEvolution[i][0][0] = "Tanemon"

        # for
        self.digiEvolution[i][1][0] = "Woodmon"
        self.digiEvolution[i][1][1] = "Garurumon"
        self.digiEvolution[i][1][2] = "Kyubimon"
        self.digiEvolution[i][1][3] = "BlackGatomon"
        self.digiEvolution[i][1][4] = "Turuiemon"
        self.digiEvolution[i][1][5] = "Lekismon"
        i += 1

        # Lopmon
        # from
        self.digiEvolution[i][0][0] = "Pagumon"

        # for
        self.digiEvolution[i][1][0] = "Wizardmon"
        self.digiEvolution[i][1][1] = "Gargomon"
        self.digiEvolution[i][1][2] = "Devimon"
        self.digiEvolution[i][1][3] = "BlackGatomon"
        self.digiEvolution[i][1][4] = "MudFrigimon"
        self.digiEvolution[i][1][5] = "Turuiemon"
        i += 1

        # Wormmon
        # from
        self.digiEvolution[i][0][0] = "Yokomon"

        # for
        self.digiEvolution[i][1][0] = "IceDevimon"
        self.digiEvolution[i][1][1] = "Kabuterimon"
        self.digiEvolution[i][1][2] = "Kuwagamon"
        self.digiEvolution[i][1][3] = "Stingmon"
        self.digiEvolution[i][1][4] = "Waspmon"
        self.digiEvolution[i][1][5] = "Hudiemon"
        i += 1

        # IceDevimon
        # from
        self.digiEvolution[i][0][0] = "Impmon"
        self.digiEvolution[i][0][1] = "DemiDevimon"
        self.digiEvolution[i][0][2] = "Wormmon"

        # for
        self.digiEvolution[i][1][0] = "Myotismon"
        self.digiEvolution[i][1][1] = "Cherrymon"
        self.digiEvolution[i][1][2] = "LadyDevimon"
        self.digiEvolution[i][1][3] = "Arcadiamon Ultimate"
        self.digiEvolution[i][1][4] = "Dragomon"
        i += 1

        # Icemon
        # from
        self.digiEvolution[i][0][0] = "Gotsumon"
        self.digiEvolution[i][0][1] = "Gomamon"

        # for
        self.digiEvolution[i][1][0] = "Meteormon"
        self.digiEvolution[i][1][1] = "Panjyamon"
        self.digiEvolution[i][1][2] = "Zudomon"
        i += 1

        # Aquilamon
        # from
        self.digiEvolution[i][0][0] = "Biyomon"
        self.digiEvolution[i][0][1] = "Falcomon"
        self.digiEvolution[i][0][2] = "Hawkmon"

        # for
        self.digiEvolution[i][1][0] = "AeroVeedramon"
        self.digiEvolution[i][1][1] = "Garudamon"
        self.digiEvolution[i][1][2] = "Silphymon"
        self.digiEvolution[i][1][3] = "Crowmon"
        self.digiEvolution[i][1][4] = "HippoGryphonmon"
        i += 1

        # Agunimon
        # from
        self.digiEvolution[i][0][0] = "Agumon"
        self.digiEvolution[i][0][1] = "Guilmon"

        # for
        self.digiEvolution[i][1][0] = "BurningGreymon"
        self.digiEvolution[i][1][1] = "Matadormon"
        self.digiEvolution[i][1][2] = "SkullMeramon"
        self.digiEvolution[i][1][3] = "RizeGreymon"
        i += 1

        # Arcadiamon Champion
        # from
        self.digiEvolution[i][0][0] = "Arcadiamon Rookie"
        self.digiEvolution[i][0][1] = "Keramon"
        self.digiEvolution[i][0][2] = "Dracmon"

        # for
        self.digiEvolution[i][1][0] = "Arcadiamon Ultimate"
        self.digiEvolution[i][1][1] = "SkullSatamon"
        self.digiEvolution[i][1][2] = "Infermon"
        i += 1

        # Ankylomon
        # from
        self.digiEvolution[i][0][0] = "Armadillomon"
        self.digiEvolution[i][0][1] = "Gotsumon"
        self.digiEvolution[i][0][2] = "Gomamon"

        # for
        self.digiEvolution[i][1][0] = "Meteormon"
        self.digiEvolution[i][1][1] = "Shakkoumon"
        self.digiEvolution[i][1][2] = "SkullGreymon"
        self.digiEvolution[i][1][3] = "MagnaAngemon"
        self.digiEvolution[i][1][4] = "Groundramon"
        i += 1

        # Ikkakumon
        # from
        self.digiEvolution[i][0][0] = "Gomamon"
        self.digiEvolution[i][0][1] = "Syakomon"
        self.digiEvolution[i][0][2] = "Terriermon"

        # for
        self.digiEvolution[i][1][0] = "Zudomon"
        self.digiEvolution[i][1][1] = "Whamon"
        self.digiEvolution[i][1][2] = "MachGaogamon"
        self.digiEvolution[i][1][3] = "Triceramon"
        i += 1

        # Wizardmon
        # from
        self.digiEvolution[i][0][0] = "Impmon"
        self.digiEvolution[i][0][1] = "Keramon"
        self.digiEvolution[i][0][2] = "Lopmon"

        # for
        self.digiEvolution[i][1][0] = "Myotismon"
        self.digiEvolution[i][1][1] = "SkullMeramon"
        self.digiEvolution[i][1][2] = "Wisemon"
        self.digiEvolution[i][1][3] = "Phantomon"
        i += 1

        # Lobomon
        # from
        self.digiEvolution[i][0][0] = "Gabumon"
        self.digiEvolution[i][0][1] = "Kudamon"
        self.digiEvolution[i][0][2] = "Veemon"

        # for
        self.digiEvolution[i][1][0] = "KendoGarurumon"
        self.digiEvolution[i][1][1] = "Knightmon"
        i += 1

        # Woodmon
        # from
        self.digiEvolution[i][0][0] = "Palmon"
        self.digiEvolution[i][0][1] = "Lalamon"
        self.digiEvolution[i][0][2] = "Renamon"
        self.digiEvolution[i][0][3] = "Mushroomon"

        # for
        self.digiEvolution[i][1][0] = "Cherrymon"
        self.digiEvolution[i][1][1] = "Taomon"
        self.digiEvolution[i][1][2] = "Pumpkinmon"
        i += 1

        # Airdramon
        # from
        self.digiEvolution[i][0][0] = "Biyomon"
        self.digiEvolution[i][0][1] = "Hawkmon"
        self.digiEvolution[i][0][2] = "Betamon"

        # for
        self.digiEvolution[i][1][0] = "Wingdramon"
        self.digiEvolution[i][1][1] = "MegaSeadramon"
        self.digiEvolution[i][1][2] = "Megadramon"
        self.digiEvolution[i][1][3] = "MetalGreymon"
        i += 1

        # ExVeemon
        # from
        self.digiEvolution[i][0][0] = "Patamon"
        self.digiEvolution[i][0][1] = "Falcomon"
        self.digiEvolution[i][0][2] = "Veemon"

        # for
        self.digiEvolution[i][1][0] = "Paildramon"
        self.digiEvolution[i][1][1] = "MagnaAngemon"
        self.digiEvolution[i][1][2] = "RizeGreymon"
        self.digiEvolution[i][1][3] = "Wingdramon"
        self.digiEvolution[i][1][4] = "Dinobeemon"
        i += 1

        # Angemon
        # from
        self.digiEvolution[i][0][0] = "Kudamon"
        self.digiEvolution[i][0][1] = "Patamon"
        self.digiEvolution[i][0][2] = "Lucemon"

        # for
        self.digiEvolution[i][1][0] = "Garudamon"
        self.digiEvolution[i][1][1] = "Shakkoumon"
        self.digiEvolution[i][1][2] = "MagnaAngemon"
        self.digiEvolution[i][1][3] = "SaviorHuckmon"
        self.digiEvolution[i][1][4] = "HippoGryphonmon"
        i += 1

        # Ogremon
        # from
        self.digiEvolution[i][0][0] = "Impmon"
        self.digiEvolution[i][0][1] = "Gaomon"
        self.digiEvolution[i][0][2] = "Goblimon"

        # for
        self.digiEvolution[i][1][0] = "Digitamamon"
        self.digiEvolution[i][1][1] = "SkullMeramon"
        self.digiEvolution[i][1][2] = "WereGarurumon"
        self.digiEvolution[i][1][3] = "SkullSatamon"
        i += 1

        # Guardromon
        # from
        self.digiEvolution[i][0][0] = "ToyAgumon"
        self.digiEvolution[i][0][1] = "Dorumon"
        self.digiEvolution[i][0][2] = "Hagurumon"

        # for
        self.digiEvolution[i][1][0] = "Andromon"
        self.digiEvolution[i][1][1] = "GrapLeomon"
        self.digiEvolution[i][1][2] = "Datamon"
        self.digiEvolution[i][1][3] = "MetalMamemon"
        self.digiEvolution[i][1][4] = "CatchMamemon"
        i += 1

        # Guardromon Gold
        # from
        self.digiEvolution[i][0][0] = "ToyAgumon"
        self.digiEvolution[i][0][1] = "Solarmon"
        self.digiEvolution[i][0][2] = "FanBeemon"

        # for
        self.digiEvolution[i][1][0] = "Grademon"
        self.digiEvolution[i][1][1] = "Duramon"
        self.digiEvolution[i][1][2] = "Andromon"
        self.digiEvolution[i][1][3] = "Rapidmon Armor"
        self.digiEvolution[i][1][4] = "Magnamon"
        i += 1

        # GaoGamon
        # from
        self.digiEvolution[i][0][0] = "Gaomon"
        self.digiEvolution[i][0][1] = "Gazimon"
        self.digiEvolution[i][0][2] = "Goblimon"

        # for
        self.digiEvolution[i][1][0] = "GrapLeomon"
        self.digiEvolution[i][1][1] = "MachGaogamon"
        self.digiEvolution[i][1][2] = "WereGarurumon"
        i += 1

        # Kabuterimon
        # from
        self.digiEvolution[i][0][0] = "Tentomon"
        self.digiEvolution[i][0][1] = "Biyomon"
        self.digiEvolution[i][0][2] = "Wormmon"

        # for
        self.digiEvolution[i][1][0] = "MegaKabuterimon"
        self.digiEvolution[i][1][1] = "Cherrymon"
        self.digiEvolution[i][1][2] = "Lilamon"
        i += 1

        # ShellNumemon
        # from
        self.digiEvolution[i][0][0] = "Otamamon"
        self.digiEvolution[i][0][1] = "Syakomon"
        self.digiEvolution[i][0][2] = "Betamon"

        # for
        self.digiEvolution[i][1][0] = "ShogunGekomon"
        self.digiEvolution[i][1][1] = "BlackKingNumemon"
        self.digiEvolution[i][1][2] = "MegaSeadramon"
        i += 1

        # Gargomon
        # from
        self.digiEvolution[i][0][0] = "Gaomon"
        self.digiEvolution[i][0][1] = "Terriermon"
        self.digiEvolution[i][0][2] = "Lopmon"
        self.digiEvolution[i][0][3] = "Sistermon Blanc"

        # for
        self.digiEvolution[i][1][0] = "Antylamon"
        self.digiEvolution[i][1][1] = "WarGrowlmon"
        self.digiEvolution[i][1][2] = "Rapidmon"
        i += 1

        # Garurumon
        # from
        self.digiEvolution[i][0][0] = "Elecmon"
        self.digiEvolution[i][0][1] = "Gabumon"
        self.digiEvolution[i][0][2] = "Renamon"

        # for
        self.digiEvolution[i][1][0] = "Zudomon"
        self.digiEvolution[i][1][1] = "DoruGreymon"
        self.digiEvolution[i][1][2] = "Panjyamon"
        self.digiEvolution[i][1][3] = "WereGarurumon"
        i += 1

        # Garurumon Black
        # from
        self.digiEvolution[i][0][0] = "Elecmon"
        self.digiEvolution[i][0][1] = "Gazimon"
        self.digiEvolution[i][0][2] = "Gabumon BLK"

        # for
        self.digiEvolution[i][1][0] = "BlueMeramon"
        self.digiEvolution[i][1][1] = "MachGaogamon"
        self.digiEvolution[i][1][2] = "WereGarurumon BLK"
        self.digiEvolution[i][1][3] = "Pandamon"
        i += 1

        # Kyubimon
        # from
        self.digiEvolution[i][0][0] = "DemiDevimon"
        self.digiEvolution[i][0][1] = "Biyomon"
        self.digiEvolution[i][0][2] = "Renamon"

        # for
        self.digiEvolution[i][1][0] = "Taomon"
        self.digiEvolution[i][1][1] = "Monzaemon"
        self.digiEvolution[i][1][2] = "LadyDevimon"
        i += 1

        # Growlmon
        # from
        self.digiEvolution[i][0][0] = "Agumon BLK"
        self.digiEvolution[i][0][1] = "Guilmon"
        self.digiEvolution[i][0][2] = "Goblimon"

        # for
        self.digiEvolution[i][1][0] = "Gigadramon"
        self.digiEvolution[i][1][1] = "WarGrowlmon"
        self.digiEvolution[i][1][2] = "MetalGreymon"
        self.digiEvolution[i][1][3] = "MetalTyrannomon"
        self.digiEvolution[i][1][4] = "BurningGreymon"
        i += 1

        # Kurisarimon
        # from
        self.digiEvolution[i][0][0] = "Gazimon"
        self.digiEvolution[i][0][1] = "Keramon"
        self.digiEvolution[i][0][2] = "DemiDevimon"
        self.digiEvolution[i][0][3] = "Arcadiamon Rookie"
        self.digiEvolution[i][0][4] = "Monodramon"

        # for
        self.digiEvolution[i][1][0] = "Infermon"
        self.digiEvolution[i][1][1] = "Cyberdramon"
        self.digiEvolution[i][1][2] = "Taomon"
        self.digiEvolution[i][1][3] = "Arcadiamon Ultimate"
        i += 1

        # Greymon
        # from
        self.digiEvolution[i][0][0] = "Agumon"
        self.digiEvolution[i][0][1] = "ToyAgumon"
        self.digiEvolution[i][0][2] = "Hackmon"

        # for
        self.digiEvolution[i][1][0] = "SkullGreymon"
        self.digiEvolution[i][1][1] = "Megadramon"
        self.digiEvolution[i][1][2] = "MetalGreymon"
        self.digiEvolution[i][1][3] = "MetalGreymon Blue"
        i += 1

        # Greymon Blue
        # from
        self.digiEvolution[i][0][0] = "Agumon BLK"
        self.digiEvolution[i][0][1] = "Guilmon"
        self.digiEvolution[i][0][2] = "Goblimon"

        # for
        self.digiEvolution[i][1][0] = "DoruGreymon"
        self.digiEvolution[i][1][1] = "Knightmon"
        self.digiEvolution[i][1][2] = "MetalGreymon Blue"
        self.digiEvolution[i][1][3] = "Triceramon"
        i += 1

        # Clockmon
        # from
        self.digiEvolution[i][0][0] = "Gotsumon"
        self.digiEvolution[i][0][1] = "Solarmon"
        self.digiEvolution[i][0][2] = "ToyAgumon"
        self.digiEvolution[i][0][3] = "Hagurumon"

        # for
        self.digiEvolution[i][1][0] = "Andromon"
        self.digiEvolution[i][1][1] = "Knightmon"
        self.digiEvolution[i][1][2] = "Datamon"
        self.digiEvolution[i][1][3] = "Wisemon"
        i += 1

        # Kuwagamon
        # from
        self.digiEvolution[i][0][0] = "Tentomon"
        self.digiEvolution[i][0][1] = "Palmon"
        self.digiEvolution[i][0][2] = "Wormmon"

        # for
        self.digiEvolution[i][1][0] = "Okuwamon"
        self.digiEvolution[i][1][1] = "CannonBeemon"
        self.digiEvolution[i][1][2] = "Cherrymon"
        i += 1

        # Gekomon
        # from
        self.digiEvolution[i][0][0] = "Otamamon"
        self.digiEvolution[i][0][1] = "Syakomon"
        self.digiEvolution[i][0][2] = "Betamon"

        # for
        self.digiEvolution[i][1][0] = "ShogunGekomon"
        self.digiEvolution[i][1][1] = "Whamon"
        self.digiEvolution[i][1][2] = "MegaSeadramon"
        i += 1

        # Geremon
        # from
        self.digiEvolution[i][0][0] = "Armadillomon"
        self.digiEvolution[i][0][1] = "Elecmon"
        self.digiEvolution[i][0][2] = "Solarmon"

        # for
        self.digiEvolution[i][1][0] = "Etemon"
        self.digiEvolution[i][1][1] = "SuperStarmon"
        self.digiEvolution[i][1][2] = "MetalMamemon"
        i += 1

        # Coredramon Blue
        # from
        self.digiEvolution[i][0][0] = "Dracomon"
        self.digiEvolution[i][0][1] = "Monodramon"

        # for
        self.digiEvolution[i][1][0] = "Wingdramon"
        self.digiEvolution[i][1][1] = "AeroVeedramon"
        self.digiEvolution[i][1][2] = "BlueMeramon"
        i += 1

        # Coredramon Green
        # from
        self.digiEvolution[i][0][0] = "Goblimon"
        self.digiEvolution[i][0][1] = "Dracomon"

        # for
        self.digiEvolution[i][1][0] = "Groundramon"
        self.digiEvolution[i][1][1] = "Triceramon"
        self.digiEvolution[i][1][2] = "WarGrowlmon"
        i += 1

        # GoldNumemon
        # from
        self.digiEvolution[i][0][0] = "Armadillomon"
        self.digiEvolution[i][0][1] = "Kudamon"
        self.digiEvolution[i][0][2] = "Hagurumon"
        self.digiEvolution[i][0][3] = "Zubamon"

        # for
        self.digiEvolution[i][1][0] = "BlackKingNumemon"
        self.digiEvolution[i][1][1] = "Vademon"
        self.digiEvolution[i][1][2] = "PlatinumNumemon"
        i += 1

        # Golemon
        # from
        self.digiEvolution[i][0][0] = "Armadillomon"
        self.digiEvolution[i][0][1] = "Gotsumon"
        self.digiEvolution[i][0][2] = "Solarmon"

        # for
        self.digiEvolution[i][1][0] = "Volcanomon"
        self.digiEvolution[i][1][1] = "Meteormon"
        self.digiEvolution[i][1][2] = "Pumpkinmon"
        i += 1

        # Cyclonemon
        # from
        self.digiEvolution[i][0][0] = "Agumon BLK"
        self.digiEvolution[i][0][1] = "Armadillomon"
        self.digiEvolution[i][0][2] = "Dorumon"

        # for
        self.digiEvolution[i][1][0] = "DoruGreymon"
        self.digiEvolution[i][1][1] = "Datamon"
        self.digiEvolution[i][1][2] = "Megadramon"
        i += 1

        # Sangloupmon
        # from
        self.digiEvolution[i][0][0] = "Gaomon"
        self.digiEvolution[i][0][1] = "Dracmon"
        self.digiEvolution[i][0][2] = "Lunamon"

        # for
        self.digiEvolution[i][1][0] = "KendoGarurumon"
        self.digiEvolution[i][1][1] = "Matadormon"
        self.digiEvolution[i][1][2] = "Myotismon"
        self.digiEvolution[i][1][3] = "WereGarurumon BLK"
        i += 1

        # Sunflowmon
        # from
        self.digiEvolution[i][0][0] = "Tentomon"
        self.digiEvolution[i][0][1] = "Palmon"
        self.digiEvolution[i][0][2] = "Lalamon"
        self.digiEvolution[i][0][3] = "Mushroomon"

        # for
        self.digiEvolution[i][1][0] = "Angemon"
        self.digiEvolution[i][1][1] = "Lilamon"
        self.digiEvolution[i][1][2] = "Lillymon"
        i += 1

        # Seadramon
        # from
        self.digiEvolution[i][0][0] = "Otamamon"
        self.digiEvolution[i][0][1] = "Syakomon"
        self.digiEvolution[i][0][2] = "Betamon"

        # for
        self.digiEvolution[i][1][0] = "ShogunGekomon"
        self.digiEvolution[i][1][1] = "Whamon"
        self.digiEvolution[i][1][2] = "MegaSeadramon"
        self.digiEvolution[i][1][3] = "Hisyaryumon"
        i += 1

        # Coelamon
        # from
        self.digiEvolution[i][0][0] = "Otamamon"
        self.digiEvolution[i][0][1] = "Syakomon"

        # for
        self.digiEvolution[i][1][0] = "Dragomon"
        self.digiEvolution[i][1][1] = "Andromon"
        self.digiEvolution[i][1][2] = "MegaSeadramon"
        self.digiEvolution[i][1][3] = "Hisyaryumon"
        i += 1

        # GeoGreymon
        # from
        self.digiEvolution[i][0][0] = "Agumon"
        self.digiEvolution[i][0][1] = "Guilmon"
        self.digiEvolution[i][0][2] = "Hackmon"

        # for
        self.digiEvolution[i][1][0] = "Gigadramon"
        self.digiEvolution[i][1][1] = "SkullGreymon"
        self.digiEvolution[i][1][2] = "RizeGreymon"
        self.digiEvolution[i][1][3] = "Groundramon"
        i += 1

        # Sukamon
        # from
        self.digiEvolution[i][0][0] = "Agumon"
        self.digiEvolution[i][0][1] = "Elecmon"
        self.digiEvolution[i][0][2] = "ToyAgumon"
        self.digiEvolution[i][0][3] = "Chuumon"

        # for
        self.digiEvolution[i][1][0] = "Etemon"
        self.digiEvolution[i][1][1] = "SuperStarmon"
        self.digiEvolution[i][1][2] = "Vademon"
        i += 1

        # Starmon
        # from
        self.digiEvolution[i][0][0] = "Gotsumon"
        self.digiEvolution[i][0][1] = "Solarmon"
        self.digiEvolution[i][0][2] = "ToyAgumon"
        self.digiEvolution[i][0][3] = "Hagurumon"

        # for
        self.digiEvolution[i][1][0] = "SuperStarmon"
        self.digiEvolution[i][1][1] = "Mamemon"
        self.digiEvolution[i][1][2] = "MetalMamemon"
        self.digiEvolution[i][1][3] = "CatchMamemon"
        self.digiEvolution[i][1][4] = "Crescemon"
        i += 1

        # Stingmon
        # from
        self.digiEvolution[i][0][0] = "Tentomon"
        self.digiEvolution[i][0][1] = "Falcomon"
        self.digiEvolution[i][0][2] = "Wormmon"
        self.digiEvolution[i][0][3] = "FanBeemon"

        # for
        self.digiEvolution[i][1][0] = "Infermon"
        self.digiEvolution[i][1][1] = "Okuwamon"
        self.digiEvolution[i][1][2] = "Paildramon"
        self.digiEvolution[i][1][3] = "Dinobeemon"
        i += 1

        # Strikedramon
        # from
        self.digiEvolution[i][0][0] = "Gomamon"
        self.digiEvolution[i][0][1] = "Veemon"
        self.digiEvolution[i][0][2] = "Monodramon"

        # for
        self.digiEvolution[i][1][0] = "SaviorHuckmon"
        self.digiEvolution[i][1][1] = "Cyberdramon"
        self.digiEvolution[i][1][2] = "WereGarurumon"
        i += 1

        # Zubaeagermon
        # from
        self.digiEvolution[i][0][0] = "Hackmon"
        self.digiEvolution[i][0][1] = "Zubamon"

        # for
        self.digiEvolution[i][1][0] = "KendoGarurumon"
        self.digiEvolution[i][1][1] = "Duramon"
        self.digiEvolution[i][1][2] = "Phantomon"
        i += 1

        # Socerimon
        # from
        self.digiEvolution[i][0][0] = "Impmon"
        self.digiEvolution[i][0][1] = "Gomamon"
        self.digiEvolution[i][0][2] = "Salamon"

        # for
        self.digiEvolution[i][1][0] = "Antylamon"
        self.digiEvolution[i][1][1] = "Piximon"
        self.digiEvolution[i][1][2] = "Wisemon"
        i += 1

        # Tankmon
        # from
        self.digiEvolution[i][0][0] = "Agumon BLK"
        self.digiEvolution[i][0][1] = "Armadillomon"
        self.digiEvolution[i][0][2] = "Gotsumon"

        # for
        self.digiEvolution[i][1][0] = "Andromon"
        self.digiEvolution[i][1][1] = "Gigadramon"
        self.digiEvolution[i][1][2] = "CannonBeemon"
        self.digiEvolution[i][1][3] = "Knightmon"
        self.digiEvolution[i][1][4] = "Volcanomon"
        i += 1

        # MudFrigimon
        # from
        self.digiEvolution[i][0][0] = "Palmon"
        self.digiEvolution[i][0][1] = "Mushroomon"
        self.digiEvolution[i][0][2] = "Lopmon"

        # for
        self.digiEvolution[i][1][0] = "Pandamon"
        self.digiEvolution[i][1][1] = "Meteormon"
        self.digiEvolution[i][1][2] = "Pumpkinmon"
        i += 1

        # Tyrannomon
        # from
        self.digiEvolution[i][0][0] = "Agumon"
        self.digiEvolution[i][0][1] = "Agumon BLK"
        self.digiEvolution[i][0][2] = "Guilmon"

        # for
        self.digiEvolution[i][1][0] = "Mamemon"
        self.digiEvolution[i][1][1] = "Megadramon"
        self.digiEvolution[i][1][2] = "MetalGreymon Blue"
        self.digiEvolution[i][1][3] = "MetalTyrannomon"
        i += 1

        # Gatomon
        # from
        self.digiEvolution[i][0][0] = "Terriermon"
        self.digiEvolution[i][0][1] = "Patamon"
        self.digiEvolution[i][0][2] = "Salamon"
        self.digiEvolution[i][0][3] = "Lunamon"

        # for
        self.digiEvolution[i][1][0] = "Angewomon"
        self.digiEvolution[i][1][1] = "Silphymon"
        self.digiEvolution[i][1][2] = "Lillymon"
        self.digiEvolution[i][1][3] = "Pandamon"
        i += 1

        # Devimon
        # from
        self.digiEvolution[i][0][0] = "DemiDevimon"
        self.digiEvolution[i][0][1] = "Lucemon"
        self.digiEvolution[i][0][2] = "Lopmon"
        self.digiEvolution[i][0][3] = "Dracmon"

        # for
        self.digiEvolution[i][1][0] = "Infermon"
        self.digiEvolution[i][1][1] = "Myotismon"
        self.digiEvolution[i][1][2] = "Meramon"
        self.digiEvolution[i][1][3] = "MetalGreymon Blue"
        self.digiEvolution[i][1][4] = "SkullSatamon"
        i += 1

        # Turuiemon
        # from
        self.digiEvolution[i][0][0] = "Renamon"
        self.digiEvolution[i][0][1] = "Lopmon"

        # for
        self.digiEvolution[i][1][0] = "Antylamon"
        self.digiEvolution[i][1][1] = "Cyberdramon"
        self.digiEvolution[i][1][2] = "Monzaemon"
        i += 1

        # Togemon
        # from
        self.digiEvolution[i][0][0] = "Gaomon"
        self.digiEvolution[i][0][1] = "Palmon"
        self.digiEvolution[i][0][2] = "Lalamon"
        self.digiEvolution[i][0][3] = "FanBeemon"

        # for
        self.digiEvolution[i][1][0] = "Pumpkinmon"
        self.digiEvolution[i][1][1] = "MachGaogamon"
        self.digiEvolution[i][1][2] = "Lillymon"
        i += 1

        # Dorugamon
        # from
        self.digiEvolution[i][0][0] = "Gazimon"
        self.digiEvolution[i][0][1] = "Gabumon"
        self.digiEvolution[i][0][2] = "Dorumon"
        self.digiEvolution[i][0][3] = "Monodramon"

        # for
        self.digiEvolution[i][1][0] = "Chirinmon"
        self.digiEvolution[i][1][1] = "DoruGreymon"
        self.digiEvolution[i][1][2] = "RizeGreymon"
        self.digiEvolution[i][1][3] = "Grademon"
        i += 1

        # Nanimon
        # from
        self.digiEvolution[i][0][0] = "Elecmon"
        self.digiEvolution[i][0][1] = "Gazimon"
        self.digiEvolution[i][0][2] = "Goblimon"
        self.digiEvolution[i][0][3] = "Chuumon"

        # for
        self.digiEvolution[i][1][0] = "Meteormon"
        self.digiEvolution[i][1][1] = "SuperStarmon"
        self.digiEvolution[i][1][2] = "Digitamamon"
        i += 1

        # Numemon
        # from
        self.digiEvolution[i][0][0] = "Otamamon"
        self.digiEvolution[i][0][1] = "Gabumon"
        self.digiEvolution[i][0][2] = "Betamon"

        # for
        self.digiEvolution[i][1][0] = "Etemon"
        self.digiEvolution[i][1][1] = "BlackKingNumemon"
        self.digiEvolution[i][1][2] = "Monzaemon"
        i += 1

        # Birdramon
        # from
        self.digiEvolution[i][0][0] = "Patamon"
        self.digiEvolution[i][0][1] = "Biyomon"
        self.digiEvolution[i][0][2] = "Hawkmon"

        # for
        self.digiEvolution[i][1][0] = "AeroVeedramon"
        self.digiEvolution[i][1][1] = "Garudamon"
        self.digiEvolution[i][1][2] = "Chirinmon"
        self.digiEvolution[i][1][3] = "Crowmon"
        self.digiEvolution[i][1][4] = "BurningGreymon"
        self.digiEvolution[i][1][5] = "HippoGryphonmon"
        i += 1

        # BaoHuckmon
        # from
        self.digiEvolution[i][0][0] = "Hackmon"
        self.digiEvolution[i][0][1] = "Zubamon"
        self.digiEvolution[i][0][2] = "Salamon"

        # for
        self.digiEvolution[i][1][0] = "KendoGarurumon"
        self.digiEvolution[i][1][1] = "SaviorHuckmon"
        self.digiEvolution[i][1][2] = "RizeGreymon"
        i += 1

        # Bakemon
        # from
        self.digiEvolution[i][0][0] = "Impmon"
        self.digiEvolution[i][0][1] = "Keramon"
        self.digiEvolution[i][0][2] = "DemiDevimon"

        # for
        self.digiEvolution[i][1][0] = "Myotismon"
        self.digiEvolution[i][1][1] = "Pumpkinmon"
        self.digiEvolution[i][1][2] = "BlueMeramon"
        self.digiEvolution[i][1][3] = "LadyDevimon"
        self.digiEvolution[i][1][4] = "Phantomon"
        self.digiEvolution[i][1][5] = "Matadormon"
        i += 1

        # Veedramon
        # from
        self.digiEvolution[i][0][0] = "Gabumon"
        self.digiEvolution[i][0][1] = "Veemon"
        self.digiEvolution[i][0][2] = "Salamon"
        self.digiEvolution[i][0][3] = "Dracomon"

        # for
        self.digiEvolution[i][1][0] = "AeroVeedramon"
        self.digiEvolution[i][1][1] = "Cyberdramon"
        self.digiEvolution[i][1][2] = "WarGrowlmon"
        self.digiEvolution[i][1][3] = "MetalTyrannomon"
        i += 1

        # Hudiemon
        # from
        self.digiEvolution[i][0][0] = "Wormmon"

        # for
        self.digiEvolution[i][1][0] = "Lillymon"
        self.digiEvolution[i][1][1] = "CannonBeemon"
        self.digiEvolution[i][1][2] = "Lilamon"
        i += 1

        # PlatinumSukamon
        # from
        self.digiEvolution[i][0][0] = "Keramon"
        self.digiEvolution[i][0][1] = "Hagurumon"
        self.digiEvolution[i][0][2] = "Hackmon"

        # for
        self.digiEvolution[i][1][0] = "Etemon"
        self.digiEvolution[i][1][1] = "Vademon"
        self.digiEvolution[i][1][2] = "MetalMamemon"
        self.digiEvolution[i][1][3] = "CatchMamemon"
        i += 1

        # BlackGatomon
        # from
        self.digiEvolution[i][0][0] = "Impmon"
        self.digiEvolution[i][0][1] = "Renamon"
        self.digiEvolution[i][0][2] = "Lopmon"
        self.digiEvolution[i][0][3] = "Chuumon"

        # for
        self.digiEvolution[i][1][0] = "Cyberdramon"
        self.digiEvolution[i][1][1] = "Knightmon"
        self.digiEvolution[i][1][2] = "LadyDevimon"
        self.digiEvolution[i][1][3] = "WereGarurumon"
        i += 1

        # Vegiemon
        # from
        self.digiEvolution[i][0][0] = "Gabumon BLK"
        self.digiEvolution[i][0][1] = "Palmon"
        self.digiEvolution[i][0][2] = "Betamon"
        self.digiEvolution[i][0][3] = "Lalamon"
        self.digiEvolution[i][0][4] = "Mushroomon"

        # for
        self.digiEvolution[i][1][0] = "MegaKabuterimon"
        self.digiEvolution[i][1][1] = "Digitamamon"
        self.digiEvolution[i][1][2] = "Lilamon"
        i += 1

        # Peckmon
        # from
        self.digiEvolution[i][0][0] = "Kudamon"
        self.digiEvolution[i][0][1] = "Falcomon"
        self.digiEvolution[i][0][2] = "Hawkmon"

        # for
        self.digiEvolution[i][1][0] = "Antylamon"
        self.digiEvolution[i][1][1] = "Piximon"
        self.digiEvolution[i][1][2] = "Crowmon"
        i += 1

        # Meramon
        # from
        self.digiEvolution[i][0][0] = "Agumon"
        self.digiEvolution[i][0][1] = "Guilmon"
        self.digiEvolution[i][0][2] = "Solarmon"
        self.digiEvolution[i][0][3] = "Hawkmon"

        # for
        self.digiEvolution[i][1][0] = "SkullMeramon"
        self.digiEvolution[i][1][1] = "Panjyamon"
        self.digiEvolution[i][1][2] = "BlueMeramon"
        self.digiEvolution[i][1][3] = "Mamemon"
        self.digiEvolution[i][1][4] = "BurningGreymon"
        self.digiEvolution[i][1][5] = "Volcanomon"
        i += 1

        # Monochromon
        # from
        self.digiEvolution[i][0][0] = "Agumon BLK"
        self.digiEvolution[i][0][1] = "Hackmon"

        # for
        self.digiEvolution[i][1][0] = "Triceramon"
        self.digiEvolution[i][1][1] = "SkullGreymon"
        self.digiEvolution[i][1][2] = "MetalTyrannomon"
        i += 1

        # Frigimon
        # from
        self.digiEvolution[i][0][0] = "Gabumon"
        self.digiEvolution[i][0][1] = "Gabumon BLK"
        self.digiEvolution[i][0][2] = "Gomamon"
        self.digiEvolution[i][0][3] = "Salamon"

        # for
        self.digiEvolution[i][1][0] = "Angewomon"
        self.digiEvolution[i][1][1] = "Zudomon"
        self.digiEvolution[i][1][2] = "Monzaemon"
        self.digiEvolution[i][1][3] = "Crescemon"
        i += 1

        # Unimon
        # from
        self.digiEvolution[i][0][0] = "Terriermon"
        self.digiEvolution[i][0][1] = "Patamon"

        # for
        self.digiEvolution[i][1][0] = "HippoGryphonmon"
        self.digiEvolution[i][1][1] = "Piximon"
        self.digiEvolution[i][1][2] = "MagnaAngemon"
        i += 1

        # Raptordramon
        # from
        self.digiEvolution[i][0][0] = "Dorumon"
        self.digiEvolution[i][0][1] = "FanBeemon"
        self.digiEvolution[i][0][2] = "Monodramon"
        self.digiEvolution[i][0][3] = "Ryudamon"

        # for
        self.digiEvolution[i][1][0] = "Grademon"
        self.digiEvolution[i][1][1] = "Duramon"
        self.digiEvolution[i][1][2] = "Gigadramon"
        self.digiEvolution[i][1][3] = "DoruGreymon"
        i += 1

        # Raremon
        # from
        self.digiEvolution[i][0][0] = "Otamamon"
        self.digiEvolution[i][0][1] = "Gabumon BLK"
        self.digiEvolution[i][0][2] = "Chuumon"
        self.digiEvolution[i][0][3] = "Dracmon"

        # for
        self.digiEvolution[i][1][0] = "SkullSatamon"
        self.digiEvolution[i][1][1] = "Dragomon"
        self.digiEvolution[i][1][2] = "Phantomon"
        self.digiEvolution[i][1][3] = "BlackKingNumemon"
        self.digiEvolution[i][1][4] = "MetalGreymon Blue"
        i += 1

        # Leomon
        # from
        self.digiEvolution[i][0][0] = "Elecmon"
        self.digiEvolution[i][0][1] = "Gaomon"
        self.digiEvolution[i][0][2] = "Gazimon"
        self.digiEvolution[i][0][3] = "Arcadiamon Rookie"

        # for
        self.digiEvolution[i][1][0] = "Meteormon"
        self.digiEvolution[i][1][1] = "GrapLeomon"
        self.digiEvolution[i][1][2] = "Panjyamon"
        self.digiEvolution[i][1][3] = "MetalGreymon"
        self.digiEvolution[i][1][4] = "Grademon"
        i += 1

        # Lekismon
        # from
        self.digiEvolution[i][0][0] = "Renamon"
        self.digiEvolution[i][0][1] = "Lunamon"
        self.digiEvolution[i][0][2] = "Sistermon Blanc"

        # for
        self.digiEvolution[i][1][0] = "Crescemon"
        self.digiEvolution[i][1][1] = "Antylamon"
        self.digiEvolution[i][1][2] = "MachGaogamon"
        i += 1

        # Reppamon
        # from
        self.digiEvolution[i][0][0] = "Gabumon BLK"
        self.digiEvolution[i][0][1] = "Kudamon"
        self.digiEvolution[i][0][2] = "Patamon"
        self.digiEvolution[i][0][3] = "Salamon"
        self.digiEvolution[i][0][4] = "Ryudamon"

        # for
        self.digiEvolution[i][1][0] = "Chirinmon"
        self.digiEvolution[i][1][1] = "Piximon"
        self.digiEvolution[i][1][2] = "Rapidmon"
        i += 1

        # Waspmon
        # from
        self.digiEvolution[i][0][0] = "Tentomon"
        self.digiEvolution[i][0][1] = "Dorumon"
        self.digiEvolution[i][0][2] = "Wormmon"
        self.digiEvolution[i][0][3] = "FanBeemon"

        # for
        self.digiEvolution[i][1][0] = "MegaKabuterimon"
        self.digiEvolution[i][1][1] = "Okuwamon"
        self.digiEvolution[i][1][2] = "CannonBeemon"
        self.digiEvolution[i][1][3] = "Rapidmon"
        i += 1

        # MegaKabuterimon
        # from
        self.digiEvolution[i][0][0] = "Kabuterimon"
        self.digiEvolution[i][0][1] = "Vegiemon"
        self.digiEvolution[i][0][2] = "Waspmon"

        # for
        self.digiEvolution[i][1][0] = "GranKuwagamon"
        self.digiEvolution[i][1][1] = "HerculesKabuterimon"
        self.digiEvolution[i][1][2] = "Magnadramon"
        i += 1

        # Arcadiamon Ultimate
        # from
        self.digiEvolution[i][0][0] = "IceDevimon"
        self.digiEvolution[i][0][1] = "Arcadiamon Champion"
        self.digiEvolution[i][0][2] = "Kurisarimon"

        # for
        self.digiEvolution[i][1][0] = "Arcadiamon Mega"
        self.digiEvolution[i][1][1] = "Diaboromon"
        self.digiEvolution[i][1][2] = "Creepymon"
        i += 1

        # Antylamon
        # from
        self.digiEvolution[i][0][0] = "Gargomon"
        self.digiEvolution[i][0][1] = "Socerimon"
        self.digiEvolution[i][0][2] = "Peckmon"
        self.digiEvolution[i][0][3] = "Turuiemon"
        self.digiEvolution[i][0][4] = "Lekismon"

        # for
        self.digiEvolution[i][1][0] = "Kerpymon Good"
        self.digiEvolution[i][1][1] = "Dianamon"
        self.digiEvolution[i][1][2] = "Diaboromon"
        self.digiEvolution[i][1][3] = "Kerpymon BLK"
        i += 1

        # Andromon
        # from
        self.digiEvolution[i][0][0] = "Guardromon"
        self.digiEvolution[i][0][1] = "Clockmon"
        self.digiEvolution[i][0][2] = "Tankmon"
        self.digiEvolution[i][0][3] = "Guardromon(Gold)"
        self.digiEvolution[i][0][4] = "Coelamon"

        # for
        self.digiEvolution[i][1][0] = "Craniamon"
        self.digiEvolution[i][1][1] = "TigerVespamon"
        self.digiEvolution[i][1][2] = "HiAndromon"
        i += 1

        # Meteormon
        # from
        self.digiEvolution[i][0][0] = "Ankylomon"
        self.digiEvolution[i][0][1] = "Nanimon"
        self.digiEvolution[i][0][2] = "Leomon"
        self.digiEvolution[i][0][3] = "Icemon"
        self.digiEvolution[i][0][4] = "Golemon"
        self.digiEvolution[i][0][5] = "MudFrigimon"

        # for
        self.digiEvolution[i][1][0] = "Ebemon"
        self.digiEvolution[i][1][1] = "Dianamon"
        self.digiEvolution[i][1][2] = "MetalEtemon"
        i += 1

        # Infermon
        # from
        self.digiEvolution[i][0][0] = "Kurisarimon"
        self.digiEvolution[i][0][1] = "Stingmon"
        self.digiEvolution[i][0][2] = "Devimon"
        self.digiEvolution[i][0][3] = "Arcadiamon Champion"

        # for
        self.digiEvolution[i][1][0] = "VenomMyotismon"
        self.digiEvolution[i][1][1] = "Diaboromon"
        self.digiEvolution[i][1][2] = "Beelzemon"
        self.digiEvolution[i][1][3] = "Arcadiamon Mega"
        i += 1

        # Myotismon
        # from
        self.digiEvolution[i][0][0] = "IceDevimon"
        self.digiEvolution[i][0][1] = "Wizardmon"
        self.digiEvolution[i][0][2] = "Devimon"
        self.digiEvolution[i][0][3] = "Bakemon"
        self.digiEvolution[i][0][4] = "Sangloupmon"

        # for
        self.digiEvolution[i][1][0] = "VenomMyotismon"
        self.digiEvolution[i][1][1] = "Barbamon"
        self.digiEvolution[i][1][2] = "Piedmon"
        self.digiEvolution[i][1][3] = "Arcadiamon Mega"
        self.digiEvolution[i][1][4] = "GranDracmon"
        i += 1

        # Wingdramon
        # from
        self.digiEvolution[i][0][0] = "Airdramon"
        self.digiEvolution[i][0][1] = "ExVeemon"
        self.digiEvolution[i][0][2] = "Coredramon(Blue)"

        # for
        self.digiEvolution[i][1][0] = "Slayerdramon"
        self.digiEvolution[i][1][1] = "UlforceVeedramon"
        self.digiEvolution[i][1][2] = "Dynasmon"
        i += 1

        # BurningGreymon
        # from
        self.digiEvolution[i][0][0] = "Agunimon"
        self.digiEvolution[i][0][1] = "Growlmon"
        self.digiEvolution[i][0][2] = "Birdramon"
        self.digiEvolution[i][0][3] = "Meramon"

        # for
        self.digiEvolution[i][1][0] = "KaiserGreymon"
        i += 1

        # AeroVeedramon
        # from
        self.digiEvolution[i][0][0] = "Aquilamon"
        self.digiEvolution[i][0][1] = "Birdramon"
        self.digiEvolution[i][0][2] = "Veedramon"
        self.digiEvolution[i][0][3] = "Coredramon(Blue)"

        # for
        self.digiEvolution[i][1][0] = "UlforceVeedramon"
        self.digiEvolution[i][1][1] = "Dynasmon"
        self.digiEvolution[i][1][2] = "Ravemon"
        self.digiEvolution[i][1][3] = "Goldramon"
        i += 1

        # Etemon
        # from
        self.digiEvolution[i][0][0] = "Geremon"
        self.digiEvolution[i][0][1] = "Sukamon"
        self.digiEvolution[i][0][2] = "Numemon"
        self.digiEvolution[i][0][3] = "PlatinumSukamon"

        # for
        self.digiEvolution[i][1][0] = "Piedmon"
        self.digiEvolution[i][1][1] = "PlatinumNumemon"
        i += 1

        # Angewomon
        # from
        self.digiEvolution[i][0][0] = "Sunflowmon"
        self.digiEvolution[i][0][1] = "Gatomon"
        self.digiEvolution[i][0][2] = "Frigimon"

        # for
        self.digiEvolution[i][1][0] = "Ophanimon"
        self.digiEvolution[i][1][1] = "Magnadramon"
        self.digiEvolution[i][1][2] = "Mastemon"
        self.digiEvolution[i][1][3] = "Valkyrimon"
        i += 1

        # Okuwamon
        # from
        self.digiEvolution[i][0][0] = "Kuwagamon"
        self.digiEvolution[i][0][1] = "Stingmon"
        self.digiEvolution[i][0][2] = "Waspmon"

        # for
        self.digiEvolution[i][1][0] = "GranKuwagamon"
        self.digiEvolution[i][1][1] = "Diaboromon"
        self.digiEvolution[i][1][2] = "HerculesKabuterimon"
        i += 1

        # Garudamon
        # from
        self.digiEvolution[i][0][0] = "Aquilamon"
        self.digiEvolution[i][0][1] = "Angemon"
        self.digiEvolution[i][0][2] = "Birdramon"

        # for
        self.digiEvolution[i][1][0] = "Justimon"
        self.digiEvolution[i][1][1] = "Hououmon"
        self.digiEvolution[i][1][2] = "Ravemon"
        self.digiEvolution[i][1][3] = "Varodurumon"
        self.digiEvolution[i][1][4] = "Gryphonmon"
        i += 1

        # KendoGarurumon
        # from
        self.digiEvolution[i][0][0] = "Lobomon"
        self.digiEvolution[i][0][1] = "Sangloupmon"
        self.digiEvolution[i][0][2] = "Zubaeagermon"
        self.digiEvolution[i][0][3] = "BaoHuckmon"

        # for
        self.digiEvolution[i][1][0] = "MagnaGarurumon"
        i += 1

        # Gigadramon
        # from
        self.digiEvolution[i][0][0] = "Growlmon"
        self.digiEvolution[i][0][1] = "GeoGreymon"
        self.digiEvolution[i][0][2] = "Tankmon"
        self.digiEvolution[i][0][3] = "Raptordramon"

        # for
        self.digiEvolution[i][1][0] = "GroundLocomon"
        self.digiEvolution[i][1][1] = "Machinedramon"
        self.digiEvolution[i][1][2] = "MetalSeadramon"
        self.digiEvolution[i][1][3] = "Darkdramon"
        self.digiEvolution[i][1][4] = "Dorugoramon"
        self.digiEvolution[i][1][5] = "Megidramon"
        i += 1

        # CatchMamemon
        # from
        self.digiEvolution[i][0][0] = "Guardromon"
        self.digiEvolution[i][0][1] = "Starmon"
        self.digiEvolution[i][0][2] = "PlatinumSukamon"

        # for
        self.digiEvolution[i][1][0] = "Justimon"
        self.digiEvolution[i][1][1] = "Puppetmon"
        self.digiEvolution[i][1][2] = "PrinceMamemon"
        i += 1

        # CannonBeemon
        # from
        self.digiEvolution[i][0][0] = "Kuwagamon"
        self.digiEvolution[i][0][1] = "Tankmon"
        self.digiEvolution[i][0][2] = "Waspmon"
        self.digiEvolution[i][0][3] = "Ginryumon"
        self.digiEvolution[i][0][4] = "Hudiemon"

        # for
        self.digiEvolution[i][1][0] = "GroundLocomon"
        self.digiEvolution[i][1][1] = "MegaGargomon"
        self.digiEvolution[i][1][2] = "TigerVespamon"
        i += 1

        # Groundramon
        # from
        self.digiEvolution[i][0][0] = "Ankylomon"
        self.digiEvolution[i][0][1] = "Coredramon(Green)"
        self.digiEvolution[i][0][2] = "GeoGreymon"

        # for
        self.digiEvolution[i][1][0] = "Breakdramon"
        self.digiEvolution[i][1][1] = "Megidramon"
        self.digiEvolution[i][1][2] = "Vikemon"
        i += 1

        # GrapLeomon
        # from
        self.digiEvolution[i][0][0] = "Guardromon"
        self.digiEvolution[i][0][1] = "GaoGamon"
        self.digiEvolution[i][0][2] = "Leomon"

        # for
        self.digiEvolution[i][1][0] = "SaberLeomon"
        self.digiEvolution[i][1][1] = "Leopardmon"
        self.digiEvolution[i][1][2] = "BanchoLeomon"
        self.digiEvolution[i][1][3] = "PileVolcamon"
        i += 1

        # Grademon
        # from
        self.digiEvolution[i][0][0] = "Guardromon(Gold)"
        self.digiEvolution[i][0][1] = "Dorugamon"
        self.digiEvolution[i][0][2] = "Raptordramon"
        self.digiEvolution[i][0][3] = "Leomon"

        # for
        self.digiEvolution[i][1][0] = "Durandamon"
        self.digiEvolution[i][1][1] = "Dorugoramon"
        self.digiEvolution[i][1][2] = "Alphamon"
        self.digiEvolution[i][1][3] = "TigerVespamon"
        self.digiEvolution[i][1][4] = "Ouryumon"
        i += 1

        # Crescemon
        # from
        self.digiEvolution[i][0][0] = "Starmon"
        self.digiEvolution[i][0][1] = "Frigimon"
        self.digiEvolution[i][0][2] = "Lekismon"

        # for
        self.digiEvolution[i][1][0] = "Kerpymon Good"
        self.digiEvolution[i][1][1] = "Kentaurosmon"
        self.digiEvolution[i][1][2] = "Dianamon"
        i += 1

        # Cyberdramon
        # from
        self.digiEvolution[i][0][0] = "Kurisarimon"
        self.digiEvolution[i][0][1] = "Veedramon"
        self.digiEvolution[i][0][2] = "BlackGatomon"
        self.digiEvolution[i][0][3] = "Strikedramon"
        self.digiEvolution[i][0][4] = "Turuiemon"

        # for
        self.digiEvolution[i][1][0] = "Alphamon"
        self.digiEvolution[i][1][1] = "Justimon"
        self.digiEvolution[i][1][2] = "Titamon"
        i += 1

        # Shakkoumon
        # from
        self.digiEvolution[i][0][0] = "Ankylomon"
        self.digiEvolution[i][0][1] = "Angemon"

        # for
        self.digiEvolution[i][1][0] = "Vikemon"
        self.digiEvolution[i][1][1] = "ChaosGallantmon"
        self.digiEvolution[i][1][2] = "Kerpymon Good"
        i += 1

        # Cherrymon
        # from
        self.digiEvolution[i][0][0] = "IceDevimon"
        self.digiEvolution[i][0][1] = "Woodmon"
        self.digiEvolution[i][0][2] = "Kabuterimon"
        self.digiEvolution[i][0][3] = "Kuwagamon"

        # for
        self.digiEvolution[i][1][0] = "Kuzuhamon"
        self.digiEvolution[i][1][1] = "GranKuwagamon"
        self.digiEvolution[i][1][2] = "Puppetmon"
        i += 1

        # Silphymon
        # from
        self.digiEvolution[i][0][0] = "Aquilamon"
        self.digiEvolution[i][0][1] = "Gatomon"

        # for
        self.digiEvolution[i][1][0] = "Sakuyamon"
        self.digiEvolution[i][1][1] = "Dynasmon"
        self.digiEvolution[i][1][2] = "Hououmon"
        self.digiEvolution[i][1][3] = "Valkyrimon"
        self.digiEvolution[i][1][4] = "Gryphonmon"
        i += 1

        # SuperStarmon
        # from
        self.digiEvolution[i][0][0] = "Geremon"
        self.digiEvolution[i][0][1] = "Sukamon"
        self.digiEvolution[i][0][2] = "Starmon"
        self.digiEvolution[i][0][3] = "Nanimon"

        # for
        self.digiEvolution[i][1][0] = "Gankoomon"
        self.digiEvolution[i][1][1] = "Justimon"
        self.digiEvolution[i][1][2] = "PlatinumNumemon"
        i += 1

        # SkullGreymon
        # from
        self.digiEvolution[i][0][0] = "Ankylomon"
        self.digiEvolution[i][0][1] = "Greymon"
        self.digiEvolution[i][0][2] = "GeoGreymon"
        self.digiEvolution[i][0][3] = "Monochromon"

        # for
        self.digiEvolution[i][1][0] = "ShineGreymon"
        self.digiEvolution[i][1][1] = "Titamon"
        self.digiEvolution[i][1][2] = "Creepymon"
        i += 1

        # SkullSatamon
        # from
        self.digiEvolution[i][0][0] = "Arcadiamon Champion"
        self.digiEvolution[i][0][1] = "Ogremon"
        self.digiEvolution[i][0][2] = "Devimon"
        self.digiEvolution[i][0][3] = "Raremon"

        # for
        self.digiEvolution[i][1][0] = "GranDracmon"
        self.digiEvolution[i][1][1] = "Diaboromon"
        self.digiEvolution[i][1][2] = "Creepymon"
        i += 1

        # Zudomon
        # from
        self.digiEvolution[i][0][0] = "Ikkakumon"
        self.digiEvolution[i][0][1] = "Garurumon"
        self.digiEvolution[i][0][2] = "Frigimon"
        self.digiEvolution[i][0][3] = "Icemon"

        # for
        self.digiEvolution[i][1][0] = "Vikemon"
        self.digiEvolution[i][1][1] = "MarineAngemon"
        self.digiEvolution[i][1][2] = "MetalGarurumon"
        self.digiEvolution[i][1][3] = "Plesiomon"
        i += 1

        # SaviorHuckmon
        # from
        self.digiEvolution[i][0][0] = "Angemon"
        self.digiEvolution[i][0][1] = "Strikedramon"
        self.digiEvolution[i][0][2] = "BaoHuckmon"

        # for
        self.digiEvolution[i][1][0] = "Slayerdramon"
        self.digiEvolution[i][1][1] = "Valkyrimon"
        self.digiEvolution[i][1][2] = "Jesmon"
        i += 1

        # Taomon
        # from
        self.digiEvolution[i][0][0] = "Woodmon"
        self.digiEvolution[i][0][1] = "Kyubimon"
        self.digiEvolution[i][0][2] = "Kurisarimon"

        # for
        self.digiEvolution[i][1][0] = "Kuzuhamon"
        self.digiEvolution[i][1][1] = "Sakuyamon"
        self.digiEvolution[i][1][2] = "Dianamon"
        i += 1

        # Dragomon
        # from
        self.digiEvolution[i][0][0] = "IceDevimon"
        self.digiEvolution[i][0][1] = "Coelamon"
        self.digiEvolution[i][0][2] = "Raremon"

        # for
        self.digiEvolution[i][1][0] = "Neptunemon"
        self.digiEvolution[i][1][1] = "Ebemon"
        self.digiEvolution[i][1][2] = "Leviamon"
        i += 1

        # Chirinmon
        # from
        self.digiEvolution[i][0][0] = "Dorugamon"
        self.digiEvolution[i][0][1] = "Birdramon"
        self.digiEvolution[i][0][2] = "Reppamon"

        # for
        self.digiEvolution[i][1][0] = "Kentaurosmon"
        self.digiEvolution[i][1][1] = "Seraphimon"
        self.digiEvolution[i][1][2] = "MetalGarurumon"
        i += 1

        # DinoBeemon
        # from
        self.digiEvolution[i][0][0] = "ExVeemon"
        self.digiEvolution[i][0][1] = "Stingmon"

        # for
        self.digiEvolution[i][1][0] = "Imperialdramon DM"
        self.digiEvolution[i][1][1] = "GranKuwagamon"
        i += 1

        # Digitamamon
        # from
        self.digiEvolution[i][0][0] = "Ogremon"
        self.digiEvolution[i][0][1] = "Nanimon"
        self.digiEvolution[i][0][2] = "Vegiemon"

        # for
        self.digiEvolution[i][1][0] = "Titamon"
        self.digiEvolution[i][1][1] = "Belphemon SM"
        self.digiEvolution[i][1][2] = "Minervamon"
        i += 1

        # SkullMeramon
        # from
        self.digiEvolution[i][0][0] = "Wizardmon"
        self.digiEvolution[i][0][1] = "Ogremon"
        self.digiEvolution[i][0][2] = "Meramon"
        self.digiEvolution[i][0][3] = "Agunimon"

        # for
        self.digiEvolution[i][1][0] = "Gankoomon"
        self.digiEvolution[i][1][1] = "Beelzemon"
        self.digiEvolution[i][1][2] = "Boltmon"
        i += 1

        # Duramon
        # from
        self.digiEvolution[i][0][0] = "Guardromon(Gold)"
        self.digiEvolution[i][0][1] = "Zubaeagermon"
        self.digiEvolution[i][0][2] = "Raptordramon"
        # for
        self.digiEvolution[i][1][0] = "Durandamon"
        self.digiEvolution[i][1][1] = "TigerVespamon"
        self.digiEvolution[i][1][2] = "Jesmon"
        i += 1

        # ShogunGekomon
        # from
        self.digiEvolution[i][0][0] = "ShellNumemon"
        self.digiEvolution[i][0][1] = "Gekomon"
        self.digiEvolution[i][0][2] = "Seadramon"

        # for
        self.digiEvolution[i][1][0] = "Vikemon"
        self.digiEvolution[i][1][1] = "Plesiomon"
        self.digiEvolution[i][1][2] = "Leviamon"
        self.digiEvolution[i][1][3] = "KingEtemon"
        i += 1

        # Triceramon
        # from
        self.digiEvolution[i][0][0] = "Ikkakumon"
        self.digiEvolution[i][0][1] = "Greymon(Blue)"
        self.digiEvolution[i][0][2] = "Coredramon(Green)"
        self.digiEvolution[i][0][3] = "Monochromon"

        # for
        self.digiEvolution[i][1][0] = "Breakdramon"
        self.digiEvolution[i][1][1] = "GranKuwagamon"
        self.digiEvolution[i][1][2] = "SaberLeomon"
        i += 1

        # DoruGreymon
        # from
        self.digiEvolution[i][0][0] = "Garurumon"
        self.digiEvolution[i][0][1] = "Greymon(Blue)"
        self.digiEvolution[i][0][2] = "Cyclonemon"
        self.digiEvolution[i][0][3] = "Dorugamon"
        self.digiEvolution[i][0][4] = "Raptordramon"

        # for
        self.digiEvolution[i][1][0] = "Alphamon"
        self.digiEvolution[i][1][1] = "Kentaurosmon"
        self.digiEvolution[i][1][2] = "Dorugoramon"
        i += 1

        # Knightmon
        # from
        self.digiEvolution[i][0][0] = "Greymon(Blue)"
        self.digiEvolution[i][0][1] = "Clockmon"
        self.digiEvolution[i][0][2] = "Tankmon"
        self.digiEvolution[i][0][3] = "BlackGatomon"
        self.digiEvolution[i][0][4] = "Lobomon"

        # for
        self.digiEvolution[i][1][0] = "Craniamon"
        self.digiEvolution[i][1][1] = "Leopardmon"
        self.digiEvolution[i][1][2] = "Crusadermon"
        self.digiEvolution[i][1][3] = "Durandamon"
        i += 1

        # Datamon
        # from
        self.digiEvolution[i][0][0] = "Guardromon"
        self.digiEvolution[i][0][1] = "Clockmon"
        self.digiEvolution[i][0][2] = "Cyclonemon"

        # for
        self.digiEvolution[i][1][0] = "GroundLocomon"
        self.digiEvolution[i][1][1] = "Machinedramon"
        self.digiEvolution[i][1][2] = "MetalGarurumon BLK"
        i += 1

        # Paildramon
        # from
        self.digiEvolution[i][0][0] = "ExVeemon"
        self.digiEvolution[i][0][1] = "Stingmon"

        # for
        self.digiEvolution[i][1][0] = "Imperialdramon DM"
        i += 1

        # Panjyamon
        # from
        self.digiEvolution[i][0][0] = "Garurumon"
        self.digiEvolution[i][0][1] = "Meramon"
        self.digiEvolution[i][0][2] = "Leomon"
        self.digiEvolution[i][0][3] = "Icemon"

        # for
        self.digiEvolution[i][1][0] = "SaberLeomon"
        self.digiEvolution[i][1][1] = "BanchoLeomon"
        self.digiEvolution[i][1][2] = "MirageGaogamon"
        i += 1

        # Pandamon
        # from
        self.digiEvolution[i][0][0] = "Garurumon BLK"
        self.digiEvolution[i][0][1] = "MudFrigimon"
        self.digiEvolution[i][0][2] = "Gatomon"
        self.digiEvolution[i][0][3] = "Sistermon Ciel"

        # for
        self.digiEvolution[i][1][0] = "KingEtemon"
        self.digiEvolution[i][1][1] = "Justimon"
        self.digiEvolution[i][1][2] = "BanchoLeomon"
        i += 1

        # Pumpkinmon
        # from
        self.digiEvolution[i][0][0] = "Woodmon"
        self.digiEvolution[i][0][1] = "Togemon"
        self.digiEvolution[i][0][2] = "Bakemon"
        self.digiEvolution[i][0][3] = "Golemon"
        self.digiEvolution[i][0][4] = "MudFrigimon"

        # for
        self.digiEvolution[i][1][0] = "Puppetmon"
        self.digiEvolution[i][1][1] = "Boltmon"
        self.digiEvolution[i][1][2] = "Rosemon"
        i += 1

        # Piximon
        # from
        self.digiEvolution[i][0][0] = "Socerimon"
        self.digiEvolution[i][0][1] = "Peckmon"
        self.digiEvolution[i][0][2] = "Reppamon"
        self.digiEvolution[i][0][3] = "Unimon"

        # for
        self.digiEvolution[i][1][0] = "Ophanimon"
        self.digiEvolution[i][1][1] = "Hououmon"
        self.digiEvolution[i][1][2] = "MarineAngemon"
        i += 1

        # HippoGryphonmon
        # from
        self.digiEvolution[i][0][0] = "Aquilamon"
        self.digiEvolution[i][0][1] = "Angemon"
        self.digiEvolution[i][0][2] = "Birdramon"
        self.digiEvolution[i][0][3] = "Unimon"

        # for
        self.digiEvolution[i][1][0] = "Varodurumon"
        self.digiEvolution[i][1][1] = "Gryphonmon"
        self.digiEvolution[i][1][2] = "Seraphimon"
        i += 1

        # Phantomon
        # from
        self.digiEvolution[i][0][0] = "Wizardmon"
        self.digiEvolution[i][0][1] = "Zubaeagermon"
        self.digiEvolution[i][0][2] = "Bakemon"
        self.digiEvolution[i][0][3] = "Raremon"

        # for
        self.digiEvolution[i][1][0] = "VenomMyotismon"
        self.digiEvolution[i][1][1] = "Titamon"
        self.digiEvolution[i][1][2] = "Barbamon"
        i += 1

        # BlackKingNumemon
        # from
        self.digiEvolution[i][0][0] = "ShellNumemon"
        self.digiEvolution[i][0][1] = "GoldNumemon"
        self.digiEvolution[i][0][2] = "Numemon"
        self.digiEvolution[i][0][3] = "Raremon"

        # for
        self.digiEvolution[i][1][0] = "PlatinumNumemon"
        self.digiEvolution[i][1][1] = "PrinceMamemon"
        self.digiEvolution[i][1][2] = "MetalEtemon"
        i += 1

        # BlueMeramon
        # from
        self.digiEvolution[i][0][0] = "Garurumon BLK"
        self.digiEvolution[i][0][1] = "Devimon"
        self.digiEvolution[i][0][2] = "Bakemon"
        self.digiEvolution[i][0][3] = "Meramon"
        self.digiEvolution[i][0][4] = "Coredramon(Blue)"

        # for
        self.digiEvolution[i][1][0] = "Creepymon"
        self.digiEvolution[i][1][1] = "Barbamon"
        self.digiEvolution[i][1][2] = "Boltmon"
        self.digiEvolution[i][1][3] = "Darkdramon"
        i += 1

        # Vademon
        # from
        self.digiEvolution[i][0][0] = "GoldNumemon"
        self.digiEvolution[i][0][1] = "Sukamon"
        self.digiEvolution[i][0][2] = "PlatinumSukamon"

        # for
        self.digiEvolution[i][1][0] = "Ebemon"
        self.digiEvolution[i][1][1] = "HiAndromon"
        self.digiEvolution[i][1][2] = "HerculesKabuterimon"
        i += 1

        # Whamon
        # from
        self.digiEvolution[i][0][0] = "Ikkakumon"
        self.digiEvolution[i][0][1] = "Gekomon"
        self.digiEvolution[i][0][2] = "Seadramon"

        # for
        self.digiEvolution[i][1][0] = "Plesiomon"
        self.digiEvolution[i][1][1] = "MarineAngemon"
        self.digiEvolution[i][1][2] = "MetalSeadramon"
        self.digiEvolution[i][1][3] = "Neptunemon"
        i += 1

        # MagnaAngemon
        # from
        self.digiEvolution[i][0][0] = "Ankylomon"
        self.digiEvolution[i][0][1] = "ExVeemon"
        self.digiEvolution[i][0][2] = "Angemon"
        self.digiEvolution[i][0][3] = "Unimon"
        # for
        self.digiEvolution[i][1][0] = "ShineGreymon"
        self.digiEvolution[i][1][1] = "Seraphimon"
        self.digiEvolution[i][1][2] = "Crusadermon"
        self.digiEvolution[i][1][3] = "Valkyrimon"
        self.digiEvolution[i][1][4] = "Goldramon"
        i += 1

        # Volcanomon
        # from
        self.digiEvolution[i][0][0] = "Golemon"
        self.digiEvolution[i][0][1] = "Tankmon"
        self.digiEvolution[i][0][2] = "Meramon"

        # for
        self.digiEvolution[i][1][0] = "PileVolcamon"
        self.digiEvolution[i][1][1] = "Gankoomon"
        self.digiEvolution[i][1][2] = "MetalEtemon"
        i += 1

        # Matadormon
        # from
        self.digiEvolution[i][0][0] = "Sangloupmon"
        self.digiEvolution[i][0][1] = "Bakemon"
        self.digiEvolution[i][0][2] = "Agunimon"

        # for
        self.digiEvolution[i][1][0] = "GranDracmon"
        self.digiEvolution[i][1][1] = "VenomMyotismon"
        self.digiEvolution[i][1][2] = "Piedmon"
        i += 1

        # MachGaogamon
        # from
        self.digiEvolution[i][0][0] = "Ikkakumon"
        self.digiEvolution[i][0][1] = "GaoGamon"
        self.digiEvolution[i][0][2] = "Garurumon BLK"
        self.digiEvolution[i][0][3] = "Togemon"
        self.digiEvolution[i][0][4] = "Lekismon"

        # for
        self.digiEvolution[i][1][0] = "MegaGargomon"
        self.digiEvolution[i][1][1] = "BanchoLeomon"
        self.digiEvolution[i][1][2] = "MirageGaogamon"
        self.digiEvolution[i][1][3] = "Merukimon"
        i += 1

        # Mamemon
        # from
        self.digiEvolution[i][0][0] = "Starmon"
        self.digiEvolution[i][0][1] = "Tyrannomon"
        self.digiEvolution[i][0][2] = "Meramon"

        # for
        self.digiEvolution[i][1][0] = "WarGreymon"
        self.digiEvolution[i][1][1] = "Puppetmon"
        self.digiEvolution[i][1][2] = "PrinceMamemon"
        i += 1

        # MegaSeadramon
        # from
        self.digiEvolution[i][0][0] = "ShellNumemon"
        self.digiEvolution[i][0][1] = "Gekomon"
        self.digiEvolution[i][0][2] = "Seadramon"
        self.digiEvolution[i][0][3] = "Airdramon"
        self.digiEvolution[i][0][4] = "Coelamon"
        self.digiEvolution[i][0][5] = "Ginryumon"

        # for
        self.digiEvolution[i][1][0] = "Plesiomon"
        self.digiEvolution[i][1][1] = "MetalSeadramon"
        self.digiEvolution[i][1][2] = "Leviamon"
        self.digiEvolution[i][1][3] = "Neptunemon"
        i += 1

        # Megadramon
        # from
        self.digiEvolution[i][0][0] = "Greymon"
        self.digiEvolution[i][0][1] = "Cyclonemon"
        self.digiEvolution[i][0][2] = "Tyrannomon"
        self.digiEvolution[i][0][3] = "Airdramon"

        # for
        self.digiEvolution[i][1][0] = "UlforceVeedramon"
        self.digiEvolution[i][1][1] = "BlackWarGreymon"
        self.digiEvolution[i][1][2] = "Machinedramon"
        self.digiEvolution[i][1][3] = "Goldramon"
        self.digiEvolution[i][1][4] = "Megidramon"
        i += 1

        # WarGrowlmon
        # from
        self.digiEvolution[i][0][0] = "Gargomon"
        self.digiEvolution[i][0][1] = "Growlmon"
        self.digiEvolution[i][0][2] = "Veedramon"
        self.digiEvolution[i][0][3] = "Coredramon(Green)"

        # for
        self.digiEvolution[i][1][0] = "ChaosGallantmon"
        self.digiEvolution[i][1][1] = "Gallantmon"
        self.digiEvolution[i][1][2] = "RustTyranomon"
        self.digiEvolution[i][1][3] = "Darkdramon"
        self.digiEvolution[i][1][4] = "Megidramon"
        i += 1

        # Metal Greymon
        # from
        self.digiEvolution[i][0][0] = "Growlmon"
        self.digiEvolution[i][0][1] = "Greymon"
        self.digiEvolution[i][0][2] = "Leomon"
        self.digiEvolution[i][0][3] = "Airdramon"

        # for
        self.digiEvolution[i][1][0] = "WarGreymon"
        self.digiEvolution[i][1][1] = "Gaiomon"
        self.digiEvolution[i][1][2] = "RustTyranomon"
        i += 1

        # MetalGreymon Blue
        # from
        self.digiEvolution[i][0][0] = "Greymon"
        self.digiEvolution[i][0][1] = "Greymon(Blue)"
        self.digiEvolution[i][0][2] = "Tyrannomon"
        self.digiEvolution[i][0][3] = "Devimon"
        self.digiEvolution[i][0][4] = "Raremon"

        # for
        self.digiEvolution[i][1][0] = "WarGreymon"
        self.digiEvolution[i][1][1] = "Gaiomon"
        self.digiEvolution[i][1][2] = "BlackWarGreymon"
        self.digiEvolution[i][1][3] = "Kerpymon BLK"
        i += 1

        # MetalTyrannomon
        # from
        self.digiEvolution[i][0][0] = "Growlmon"
        self.digiEvolution[i][0][1] = "Tyrannomon"
        self.digiEvolution[i][0][2] = "Veedramon"
        self.digiEvolution[i][0][3] = "Monochromon"

        # for
        self.digiEvolution[i][1][0] = "BlackWarGreymon"
        self.digiEvolution[i][1][1] = "Gallantmon"
        self.digiEvolution[i][1][2] = "RustTyranomon"
        self.digiEvolution[i][1][3] = "Breakdramon"
        i += 1

        # MetalMamemon
        # from
        self.digiEvolution[i][0][0] = "Guardromon"
        self.digiEvolution[i][0][1] = "Geremon"
        self.digiEvolution[i][0][2] = "Starmon"
        self.digiEvolution[i][0][3] = "PlatinumSukamon"

        # for
        self.digiEvolution[i][1][0] = "Ebemon"
        self.digiEvolution[i][1][1] = "HiAndromon"
        self.digiEvolution[i][1][2] = "PrinceMamemon"
        i += 1

        # Monzaemon
        # from
        self.digiEvolution[i][0][0] = "Kyubimon"
        self.digiEvolution[i][0][1] = "Numemon"
        self.digiEvolution[i][0][2] = "Frigimon"
        self.digiEvolution[i][0][3] = "Turuiemon"

        # for
        self.digiEvolution[i][1][0] = "SaberLeomon"
        self.digiEvolution[i][1][1] = "Sakuyamon"
        self.digiEvolution[i][1][2] = "Minervamon"
        i += 1

        # Crowmon
        # from
        self.digiEvolution[i][0][0] = "Aquilamon"
        self.digiEvolution[i][0][1] = "Birdramon"
        self.digiEvolution[i][0][2] = "Peckmon"

        # for
        self.digiEvolution[i][1][0] = "Kuzuhamon"
        self.digiEvolution[i][1][1] = "Minervamon"
        self.digiEvolution[i][1][2] = "Ravemon"
        self.digiEvolution[i][1][3] = "Varodurumon"
        self.digiEvolution[i][1][4] = "Ouryumon"
        i += 1

        # RizeGreymon
        # from
        self.digiEvolution[i][0][0] = "ExVeemon"
        self.digiEvolution[i][0][1] = "GeoGreymon"
        self.digiEvolution[i][0][2] = "Dorugamon"
        self.digiEvolution[i][0][3] = "Agunimon"
        self.digiEvolution[i][0][4] = "BaoHuckmon"

        # for
        self.digiEvolution[i][1][0] = "Gaiomon"
        self.digiEvolution[i][1][1] = "ShineGreymon"
        self.digiEvolution[i][1][2] = "Slayerdramon"
        i += 1

        # Lilamon
        # from
        self.digiEvolution[i][0][0] = "Kabuterimon"
        self.digiEvolution[i][0][1] = "Sunflowmon"
        self.digiEvolution[i][0][2] = "Vegiemon"
        self.digiEvolution[i][0][3] = "Hudiemon"

        # for
        self.digiEvolution[i][1][0] = "Lilithmon"
        self.digiEvolution[i][1][1] = "Rosemon"
        self.digiEvolution[i][1][2] = "Lotosmon"
        i += 1

        # Rapidmon
        # from
        self.digiEvolution[i][0][0] = "Gargomon"
        self.digiEvolution[i][0][1] = "Reppamon"
        self.digiEvolution[i][0][2] = "Waspmon"

        # for
        self.digiEvolution[i][1][0] = "MegaGargomon"
        self.digiEvolution[i][1][1] = "TigerVespamon"
        self.digiEvolution[i][1][2] = "MetalGarurumon BLK"
        i += 1

        # Lillymon
        # from
        self.digiEvolution[i][0][0] = "Sunflowmon"
        self.digiEvolution[i][0][1] = "Gatomon"
        self.digiEvolution[i][0][2] = "Togemon"
        self.digiEvolution[i][0][3] = "Hudiemon"

        # for
        self.digiEvolution[i][1][0] = "Magnadramon"
        self.digiEvolution[i][1][1] = "Rosemon"
        self.digiEvolution[i][1][2] = "Lotosmon"
        i += 1

        # Lucemon FM
        # from
        self.digiEvolution[i][0][0] = "Lucemon"

        # for
        self.digiEvolution[i][1][0] = "Lucemon SM"
        i += 1

        # LadyDevimon
        # from
        self.digiEvolution[i][0][0] = "IceDevimon"
        self.digiEvolution[i][0][1] = "Kyubimon"
        self.digiEvolution[i][0][2] = "Bakemon"
        self.digiEvolution[i][0][3] = "BlackGatomon"
        self.digiEvolution[i][0][4] = "Sistermon Ciel"

        # for
        self.digiEvolution[i][1][0] = "Mastemon"
        self.digiEvolution[i][1][1] = "Lilithmon"
        self.digiEvolution[i][1][2] = "Lotosmon"
        i += 1

        # WereGarurumon
        # from
        self.digiEvolution[i][0][0] = "Ogremon"
        self.digiEvolution[i][0][1] = "GaoGamon"
        self.digiEvolution[i][0][2] = "Garurumon"
        self.digiEvolution[i][0][3] = "Lobomon"
        self.digiEvolution[i][0][4] = "Strikedramon"

        # for
        self.digiEvolution[i][1][0] = "MirageGaogamon"
        self.digiEvolution[i][1][1] = "MetalGarurumon"
        self.digiEvolution[i][1][2] = "MetalGarurumon BLK"
        i += 1

        # WereGarurumon BLK
        # from
        self.digiEvolution[i][0][0] = "Garurumon BLK"
        self.digiEvolution[i][0][1] = "BlackGatomon"
        self.digiEvolution[i][0][2] = "Sangloupmon"

        # for
        self.digiEvolution[i][1][0] = "BanchoLeomon"
        self.digiEvolution[i][1][1] = "Minervamon"
        self.digiEvolution[i][1][2] = "MetalGarurumon BLK"
        self.digiEvolution[i][1][3] = "Merukimon"
        i += 1

        # Wisemon
        # from
        self.digiEvolution[i][0][0] = "Wizardmon"
        self.digiEvolution[i][0][1] = "Clockmon"
        self.digiEvolution[i][0][2] = "Socerimon"

        # for
        self.digiEvolution[i][1][0] = "VenomMyotismon"
        self.digiEvolution[i][1][1] = "Piedmon"
        self.digiEvolution[i][1][2] = "Belphemon SM"
        i += 1

        # Arcadiamon Mega
        # from
        self.digiEvolution[i][0][0] = "Arcadiamon Ultimate"
        self.digiEvolution[i][0][1] = "Infermon"
        self.digiEvolution[i][0][2] = "Myotismon"

        # for
        self.digiEvolution[i][1][0] = "Arcadiamon Ultra"
        i += 1

        # Alphamon
        # from
        self.digiEvolution[i][0][0] = "Cyberdramon"
        self.digiEvolution[i][0][1] = "DoruGreymon"
        self.digiEvolution[i][0][2] = "Grademon"

        # for
        self.digiEvolution[i][1][0] = "Alphamon Ouryuken"
        i += 1

        # UlforceVeedramon
        # from
        self.digiEvolution[i][0][0] = "AeroVeedramon"
        self.digiEvolution[i][0][1] = "Megadramon"
        self.digiEvolution[i][0][2] = "Wingdramon"
        i += 1

        # Ebemon
        # from
        self.digiEvolution[i][0][0] = "Meteormon"
        self.digiEvolution[i][0][1] = "Vademon"
        self.digiEvolution[i][0][2] = "MetalMamemon"
        self.digiEvolution[i][0][3] = "Dragomon"
        i += 1

        # Imperialdramon DM
        # from
        self.digiEvolution[i][0][0] = "Paildramon"
        self.digiEvolution[i][0][1] = "Imperialdramon FM"
        self.digiEvolution[i][0][2] = "Dinobeemon"

        # for
        self.digiEvolution[i][1][0] = "Imperialdramon PM"
        self.digiEvolution[i][1][1] = "Imperialdramon FM"
        i += 1

        # Imperialdramon FM
        # from
        self.digiEvolution[i][0][0] = "Imperialdramon DM"

        # for
        self.digiEvolution[i][1][0] = "Imperialdramon DM"
        i += 1

        # Vikemon
        # from
        self.digiEvolution[i][0][0] = "Shakkoumon"
        self.digiEvolution[i][0][1] = "Zudomon"
        self.digiEvolution[i][0][2] = "ShogunGekomon"
        self.digiEvolution[i][0][3] = "Groundramon"
        i += 1

        # Valkyrimon
        # from
        self.digiEvolution[i][0][0] = "Angewomon"
        self.digiEvolution[i][0][1] = "Silphymon"
        self.digiEvolution[i][0][2] = "MagnaAngemon"
        self.digiEvolution[i][0][3] = "SaviorHuckmon"
        i += 1

        # Varodurumon
        # from
        self.digiEvolution[i][0][0] = "Garudamon"
        self.digiEvolution[i][0][1] = "HippoGryphonmon"
        self.digiEvolution[i][0][2] = "Crowmon"

        # for
        self.digiEvolution[i][1][0] = "Chaosmon VA"
        i += 1

        # VenomMyotismon
        # from
        self.digiEvolution[i][0][0] = "Infermon"
        self.digiEvolution[i][0][1] = "Myotismon"
        self.digiEvolution[i][0][2] = "Wisemon"
        self.digiEvolution[i][0][3] = "Phantomon"
        self.digiEvolution[i][0][4] = "Matadormon"
        i += 1

        # WarGreymon
        # from
        self.digiEvolution[i][0][0] = "Mamemon"
        self.digiEvolution[i][0][1] = "MetalGreymon"
        self.digiEvolution[i][0][2] = "MetalGreymon Blue"

        # for
        self.digiEvolution[i][1][0] = "Omnimon"
        i += 1

        # Ophanimon
        # from
        self.digiEvolution[i][0][0] = "Angewomon"
        self.digiEvolution[i][0][1] = "Piximon"
        i += 1

        # Gaiomon
        # from
        self.digiEvolution[i][0][0] = "MetalGreymon"
        self.digiEvolution[i][0][1] = "MetalGreymon Blue"
        self.digiEvolution[i][0][2] = "RizeGreymon"
        self.digiEvolution[i][0][3] = "Hisyaryumon"
        i += 1

        # KaiserGreymon
        # from
        self.digiEvolution[i][0][0] = "BurningGreymon"

        # for
        self.digiEvolution[i][1][0] = "Susanomon"
        i += 1

        # ChaosGallantmon
        # from
        self.digiEvolution[i][0][0] = "Shakkoumon"
        self.digiEvolution[i][0][1] = "WarGrowlmon"
        i += 1

        # Chaosdramon
        # from
        self.digiEvolution[i][0][0] = "Machinedramon"
        i += 1

        # Gankoomon
        # from
        self.digiEvolution[i][0][0] = "SuperStarmon"
        self.digiEvolution[i][0][1] = "SkullMeramon"
        self.digiEvolution[i][0][2] = "Volcanomon"
        i += 1

        # KingEtemon
        # from
        self.digiEvolution[i][0][0] = "Etemon"
        self.digiEvolution[i][0][1] = "ShogunGekomon"
        self.digiEvolution[i][0][2] = "Pandamon"
        i += 1

        # Kuzuhamon
        # from
        self.digiEvolution[i][0][0] = "Cherrymon"
        self.digiEvolution[i][0][1] = "Taomon"
        self.digiEvolution[i][0][2] = "Crowmon"
        i += 1

        # GranKuwagamon
        # from
        self.digiEvolution[i][0][0] = "MegaKabuterimon"
        self.digiEvolution[i][0][1] = "Okuwamon"
        self.digiEvolution[i][0][2] = "Cherrymon"
        self.digiEvolution[i][0][3] = "Dinobeemon"
        self.digiEvolution[i][0][4] = "Triceramon"
        i += 1

        # GranDracmon
        # from
        self.digiEvolution[i][0][0] = "Myotismon"
        self.digiEvolution[i][0][1] = "SkullSatamon"
        self.digiEvolution[i][0][2] = "Matadormon"
        i += 1

        # GroundLocomon
        # from
        self.digiEvolution[i][0][0] = "Gigadramon"
        self.digiEvolution[i][0][1] = "CannonBeemon"
        self.digiEvolution[i][0][2] = "Datamon"
        i += 1

        # Gryphonmon
        # from
        self.digiEvolution[i][0][0] = "Garudamon"
        self.digiEvolution[i][0][1] = "Silphymon"
        self.digiEvolution[i][0][2] = "HippoGryphonmon"
        i += 1

        # Craniamon
        # from
        self.digiEvolution[i][0][0] = "Andromon"
        self.digiEvolution[i][0][1] = "Knightmon"
        i += 1

        # Kerpymon BLK
        # from
        self.digiEvolution[i][0][0] = "Antylamon"
        self.digiEvolution[i][0][1] = "MetalGreymon Blue"
        i += 1

        # kerpymon GOod
        # from
        self.digiEvolution[i][0][0] = "Antylamon"
        self.digiEvolution[i][0][1] = "Shakkoumon"
        self.digiEvolution[i][0][2] = "Crescemon"
        i += 1

        # Goldramon
        # from
        self.digiEvolution[i][0][0] = "AeroVeedramon"
        self.digiEvolution[i][0][1] = "MagnaAngemon"
        self.digiEvolution[i][0][2] = "Megadramon"
        self.digiEvolution[i][0][3] = "Hisyaryumon"
        i += 1

        # SaberLeomon
        # from
        self.digiEvolution[i][0][0] = "GrapLeomon"
        self.digiEvolution[i][0][1] = "Panjyamon"
        self.digiEvolution[i][0][2] = "Monzaemon"
        self.digiEvolution[i][0][3] = "Triceramon"
        i += 1

        # Sakuyamon
        # from
        self.digiEvolution[i][0][0] = "Silphymon"
        self.digiEvolution[i][0][1] = "Taomon"
        self.digiEvolution[i][0][2] = "Monzaemon"
        i += 1

        # Jesmon
        # from
        self.digiEvolution[i][0][0] = "SaviorHuckmon"
        self.digiEvolution[i][0][1] = "Duramon"
        i += 1

        # ShineGreymon
        # from
        self.digiEvolution[i][0][0] = "SkullGreymon"
        self.digiEvolution[i][0][1] = "MagnaAngemon"
        self.digiEvolution[i][0][2] = "RizeGreymon"

        # for
        self.digiEvolution[i][1][0] = "ShineGreymon BM"
        i += 1

        # ShineGreymon BM
        # from
        self.digiEvolution[i][0][0] = "ShineGreymon"
        i += 1

        # Justimon
        # from
        self.digiEvolution[i][0][0] = "Garudamon"
        self.digiEvolution[i][0][1] = "Cyberdramon"
        self.digiEvolution[i][0][2] = "SuperStarmon"
        self.digiEvolution[i][0][3] = "CatchMamemon"
        self.digiEvolution[i][0][4] = "Pandamon"
        i += 1

        # Kentaurosmon
        # from
        self.digiEvolution[i][0][0] = "Kentaurosmon"
        self.digiEvolution[i][0][1] = "Chirinmon"
        self.digiEvolution[i][0][2] = "DoruGreymon"
        self.digiEvolution[i][0][3] = "Crescemon"
        i += 1

        # Slayerdramon
        # from
        self.digiEvolution[i][0][0] = "Wingdramon"
        self.digiEvolution[i][0][1] = "SaviorHuckmon"
        self.digiEvolution[i][0][2] = "RizeGreymon"

        # for
        self.digiEvolution[i][1][0] = "Examon"
        i += 1

        # Seraphimon
        # from
        self.digiEvolution[i][0][0] = "Chirinmon"
        self.digiEvolution[i][0][1] = "MagnaAngemon"
        self.digiEvolution[i][0][2] = "HippoGryphonmon"
        i += 1

        # MegaGargomon
        # from
        self.digiEvolution[i][0][0] = "CannonBeemon"
        self.digiEvolution[i][0][1] = "MachGaogamon"
        self.digiEvolution[i][0][2] = "Rapidmon"
        i += 1

        # Darkdramon
        # from
        self.digiEvolution[i][0][0] = "Gigadramon"
        self.digiEvolution[i][0][1] = "BlueMeramon"
        self.digiEvolution[i][0][2] = "WarGrowlmon"

        # for
        self.digiEvolution[i][1][0] = "Chaosmon"
        i += 1

        # TigesVespamon
        # from
        self.digiEvolution[i][0][0] = "Andromon"
        self.digiEvolution[i][0][1] = "CannonBeemon"
        self.digiEvolution[i][0][2] = "Rapidmon"
        self.digiEvolution[i][0][3] = "Grademon"
        self.digiEvolution[i][0][4] = "Duramon"
        i += 1

        # Titamon
        # from
        self.digiEvolution[i][0][0] = "Cyberdramon"
        self.digiEvolution[i][0][1] = "SkullGreymon"
        self.digiEvolution[i][0][2] = "Digitamamon"
        self.digiEvolution[i][0][3] = "Phantomon"
        i += 1

        # TyrantKabuterimon
        # from
        self.digiEvolution[i][0][0] = "HerculesKabuterimon"
        i += 1

        # Dianamon
        # from
        self.digiEvolution[i][0][0] = "Antylamon"
        self.digiEvolution[i][0][1] = "Meteormon"
        self.digiEvolution[i][0][2] = "Taomon"
        self.digiEvolution[i][0][3] = "Crescemon"
        i += 1

        # Diaboromon
        # from
        self.digiEvolution[i][0][0] = "Antylamon"
        self.digiEvolution[i][0][1] = "Infermon"
        self.digiEvolution[i][0][2] = "Okuwamon"
        self.digiEvolution[i][0][3] = "Arcadiamon Ultimate"
        self.digiEvolution[i][0][4] = "SkullSatamon"

        # for
        self.digiEvolution[i][1][0] = "Armageddemon"
        i += 1

        # Creepymon
        # from
        self.digiEvolution[i][0][0] = "SkullGreymon"
        self.digiEvolution[i][0][1] = "BlueMeramon"
        self.digiEvolution[i][0][2] = "Arcadiamon Ultimate"
        self.digiEvolution[i][0][3] = "SkullSatamon"
        i += 1

        # Gallantmon
        # from
        self.digiEvolution[i][0][0] = "WarGrowlmon"
        self.digiEvolution[i][0][1] = "MetalTyrannomon"

        # for
        self.digiEvolution[i][1][0] = "Gallantmon CM"
        i += 1

        # Dynasmon
        # from
        self.digiEvolution[i][0][0] = "AeroVeedramon"
        self.digiEvolution[i][0][1] = "Silphymon"
        self.digiEvolution[i][0][2] = "Wingdramon"
        i += 1

        # Durandamon
        # from
        self.digiEvolution[i][0][0] = "Grademon"
        self.digiEvolution[i][0][1] = "Duramon"
        self.digiEvolution[i][0][2] = "Knightmon"
        i += 1

        # Leopardmon
        # from
        self.digiEvolution[i][0][0] = "GrapLeomon"
        self.digiEvolution[i][0][1] = "Knightmon"
        self.digiEvolution[i][0][2] = "Leopardmon LM"

        # for
        self.digiEvolution[i][1][0] = "Leopardmon LM"
        i += 1

        # Leopardmon LM
        # from
        self.digiEvolution[i][0][0] = "Leopardmon"

        # for
        self.digiEvolution[i][1][0] = "Leopardmon"
        i += 1

        # Dorugoramon
        # from
        self.digiEvolution[i][0][0] = "Gigadramon"
        self.digiEvolution[i][0][1] = "Grademon"
        self.digiEvolution[i][0][2] = "DoruGreymon"
        i += 1

        # Neptunemon
        # from
        self.digiEvolution[i][0][0] = "Dragomon"
        self.digiEvolution[i][0][1] = "Whamon"
        self.digiEvolution[i][0][2] = "MegaSeadramon"
        i += 1

        # HiAndromon
        # from
        self.digiEvolution[i][0][0] = "Andromon"
        self.digiEvolution[i][0][1] = "Vademon"
        self.digiEvolution[i][0][2] = "MetalMamemon"
        i += 1

        # PileVolcamon
        # from
        self.digiEvolution[i][0][0] = "Etemon"
        self.digiEvolution[i][0][1] = "GrapLeomon"
        self.digiEvolution[i][0][2] = "Volcanomon"
        i += 1

        # Barbamon
        # from
        self.digiEvolution[i][0][0] = "Myotismon"
        self.digiEvolution[i][0][1] = "BlueMeramon"
        self.digiEvolution[i][0][2] = "Phantomon"
        i += 1

        # BanchoLeomon
        # from
        self.digiEvolution[i][0][0] = "GrapLeomon"
        self.digiEvolution[i][0][1] = "Panjyamon"
        self.digiEvolution[i][0][2] = "MachGaogamon"
        self.digiEvolution[i][0][3] = "WereGarurumon BLK"
        self.digiEvolution[i][0][4] = "Pandamon"

        # for
        self.digiEvolution[i][1][0] = "Chaosmon"
        self.digiEvolution[i][1][0] = "Chaosmon VA"
        i += 1

        # Piedmon
        # from
        self.digiEvolution[i][0][0] = "Myotismon"
        self.digiEvolution[i][0][1] = "Etemon"
        self.digiEvolution[i][0][2] = "Wisemon"
        self.digiEvolution[i][0][3] = "Matadormon"

        # for
        self.digiEvolution[i][1][0] = "Apocalymon"
        i += 1

        # Puppetmon
        # from
        self.digiEvolution[i][0][0] = "Cherrymon"
        self.digiEvolution[i][0][1] = "Pumpkinmon"
        self.digiEvolution[i][0][2] = "Mamemon"
        self.digiEvolution[i][0][3] = "CatchMamemon"

        # for
        self.digiEvolution[i][1][0] = "Apocalymon"
        i += 1

        # PlatinumNumemon
        # from
        self.digiEvolution[i][0][0] = "GoldNumemon"
        self.digiEvolution[i][0][1] = "Etemon"
        self.digiEvolution[i][0][2] = "SuperStarmon"
        self.digiEvolution[i][0][3] = "BlackKingNumemon"
        i += 1

        # BlackWarGreymon
        # from
        self.digiEvolution[i][0][0] = "Megadramon"
        self.digiEvolution[i][0][1] = "MetalGreymon Blue"
        self.digiEvolution[i][0][2] = "MetalTyrannomon"

        # for
        self.digiEvolution[i][1][0] = "Omnimon Zwart"
        i += 1

        # PrinceMamemon
        # from
        self.digiEvolution[i][0][0] = "BlackKingNumemon"
        self.digiEvolution[i][0][1] = "Mamemon"
        self.digiEvolution[i][0][2] = "MetalMamemon"
        i += 1

        # Breakdramon
        # from
        self.digiEvolution[i][0][0] = "Groundramon"
        self.digiEvolution[i][0][1] = "Triceramon"
        self.digiEvolution[i][0][2] = "MetalTyrannomon"

        # for
        self.digiEvolution[i][1][0] = "Examon"
        i += 1

        # Plesiomon
        # from
        self.digiEvolution[i][0][0] = "ShogunGekomon"
        self.digiEvolution[i][0][1] = "Whamon"
        self.digiEvolution[i][0][2] = "MegaSeadramon"
        self.digiEvolution[i][0][3] = "Zudomon"
        i += 1

        # Herculeskabuterimon
        # from
        self.digiEvolution[i][0][0] = "MegaKabuterimon"
        self.digiEvolution[i][0][1] = "Okuwamon"
        self.digiEvolution[i][0][2] = "Vademon"

        # for
        self.digiEvolution[i][1][0] = "TyrantKabuterimon"
        i += 1

        # Beelzemon
        # from
        self.digiEvolution[i][0][0] = "Infermon"
        self.digiEvolution[i][0][1] = "SkullMeramon"

        # for
        self.digiEvolution[i][1][0] = "Beelzemon BM"
        i += 1

        # Beelzemon BM
        # from
        self.digiEvolution[i][0][0] = "Beelzemon"
        i += 1

        # Belphemon SM
        # from
        self.digiEvolution[i][0][0] = "Digitamamon"
        self.digiEvolution[i][0][1] = "Wisemon"
        self.digiEvolution[i][0][2] = "Belphemon RM"

        # for
        self.digiEvolution[i][1][0] = "Belphemon RM"
        i += 1

        # Hououmon
        # from
        self.digiEvolution[i][0][0] = "Garudamon"
        self.digiEvolution[i][0][1] = "Silphymon"
        self.digiEvolution[i][0][2] = "Piximon"
        i += 1

        # Magnadramon
        # from
        self.digiEvolution[i][0][0] = "MegaKabuterimon"
        self.digiEvolution[i][0][1] = "Angemon"
        self.digiEvolution[i][0][2] = "Lillymon"
        i += 1

        # Boltmon
        # from
        self.digiEvolution[i][0][0] = "SkullMeramon"
        self.digiEvolution[i][0][1] = "Pumpkinmon"
        self.digiEvolution[i][0][2] = "BlueMeramon"
        i += 1

        # MagnaGarurumon
        # from
        self.digiEvolution[i][0][0] = "KendoGarurumon"
        self.digiEvolution[i][0][1] = "MagnaGarurumon SV"

        # for
        self.digiEvolution[i][1][0] = "MagnaGarurumon SV"
        self.digiEvolution[i][1][1] = "Susanomon"
        i += 1

        # MagnaGarurumon SV
        # from
        self.digiEvolution[i][0][0] = "MagnaGarurumon"

        # for
        self.digiEvolution[i][1][0] = "MagnaGarurumon"
        i += 1

        # Mastemon
        # from
        self.digiEvolution[i][0][0] = "Angewomon"
        self.digiEvolution[i][0][1] = "LadyDevimon"
        i += 1

        # MarineAngemon
        # from
        self.digiEvolution[i][0][0] = "Zudomon"
        self.digiEvolution[i][0][1] = "Piximon"
        self.digiEvolution[i][0][2] = "Whamon"
        i += 1

        # Minervamon
        # from
        self.digiEvolution[i][0][0] = "Digitamamon"
        self.digiEvolution[i][0][1] = "Monzaemon"
        self.digiEvolution[i][0][2] = "Crowmon"
        self.digiEvolution[i][0][3] = "WereGarurumon BLK"
        self.digiEvolution[i][0][4] = "Hisyaryumon"
        i += 1

        # MirageGaogamon
        # from
        self.digiEvolution[i][0][0] = "Panjyamon"
        self.digiEvolution[i][0][1] = "MachGaogamon"
        self.digiEvolution[i][0][2] = "WereGarurumon"

        # for
        self.digiEvolution[i][1][0] = "MirageGaogamon BM"
        i += 1

        # MirageGaogamon BM
        # from
        self.digiEvolution[i][0][0] = "MirageGaogamon"
        i += 1

        # Machinedramon
        # from
        self.digiEvolution[i][0][0] = "Gigadramon"
        self.digiEvolution[i][0][1] = "Datamon"
        self.digiEvolution[i][0][2] = "Megadramon"

        # for
        self.digiEvolution[i][1][0] = "Chaosdramon"
        self.digiEvolution[i][1][1] = "Apocalymon"
        i += 1

        # Megidramon
        # from
        self.digiEvolution[i][0][0] = "GroundLocomon"
        self.digiEvolution[i][0][1] = "Megadramon"
        self.digiEvolution[i][0][2] = "WarGrowlmon"
        self.digiEvolution[i][0][3] = "Gigadramon"
        i += 1

        # MetalEtemon
        # from
        self.digiEvolution[i][0][0] = "Meteormon"
        self.digiEvolution[i][0][1] = "Etemon"
        self.digiEvolution[i][0][2] = "BlackKingNumemon"
        self.digiEvolution[i][0][3] = "Volcanomon"
        i += 1

        # MetalGarurumon
        # from
        self.digiEvolution[i][0][0] = "Zudomon"
        self.digiEvolution[i][0][1] = "Chirinmon"
        self.digiEvolution[i][0][2] = "WereGarurumon"

        # for
        self.digiEvolution[i][1][0] = "Omnimon"
        i += 1

        # MetalGarurumon BLK
        # from
        self.digiEvolution[i][0][0] = "Datamon"
        self.digiEvolution[i][0][1] = "Rapidmon"
        self.digiEvolution[i][0][2] = "WereGarurumon"
        self.digiEvolution[i][0][3] = "WereGarurumon BLK"

        # for
        self.digiEvolution[i][1][0] = "Omnimon Zwart"
        i += 1

        # MetalSeadramon
        # from
        self.digiEvolution[i][0][0] = "Gigadramon"
        self.digiEvolution[i][0][1] = "Whamon"
        self.digiEvolution[i][0][2] = "MegaSeadramon"

        # for
        self.digiEvolution[i][1][0] = "Apocalymon"
        i += 1

        # Merukimon
        # from
        self.digiEvolution[i][0][0] = "MachGaogamon"
        self.digiEvolution[i][0][1] = "WereGarurumon BLK"
        i += 1

        # RustTyranomon
        # from
        self.digiEvolution[i][0][0] = "WarGrowlmon"
        self.digiEvolution[i][0][1] = "MetalGreymon"
        self.digiEvolution[i][0][2] = "MetalTyrannomon"
        i += 1

        # Leviamon
        # from
        self.digiEvolution[i][0][0] = "ShogunGekomon"
        self.digiEvolution[i][0][1] = "MegaSeadramon"
        self.digiEvolution[i][0][2] = "Dragomon"
        i += 1

        # Lilithmon
        # from
        self.digiEvolution[i][0][0] = "Lilamon"
        self.digiEvolution[i][0][1] = "LadyDevimon"
        i += 1

        # Ravemon
        # from
        self.digiEvolution[i][0][0] = "AeroVeedramon"
        self.digiEvolution[i][0][1] = "Garudamon"
        self.digiEvolution[i][0][2] = "Crowmon"

        # for
        self.digiEvolution[i][1][0] = "Ravemon BM"
        i += 1

        # Ravemon BM
        # from
        self.digiEvolution[i][0][0] = "Ravemon"
        i += 1

        # Crusadermon
        # from
        self.digiEvolution[i][0][0] = "Knightmon"
        self.digiEvolution[i][0][1] = "MagnaAngemon"
        i += 1

        # Rosemon
        # from
        self.digiEvolution[i][0][0] = "Pumpkinmon"
        self.digiEvolution[i][0][1] = "Lilamon"
        self.digiEvolution[i][0][2] = "Lillymon"

        # for
        self.digiEvolution[i][1][0] = "Rosemon BM"
        i += 1

        # Rosemon BM
        # from
        self.digiEvolution[i][0][0] = "Rosemon"
        i += 1

        # Lotosmon
        # from
        self.digiEvolution[i][0][0] = "Lilamon"
        self.digiEvolution[i][0][1] = "Lillymon"
        self.digiEvolution[i][0][2] = "LadyDevimon"
        i += 1

        # Armageddemon
        # from
        self.digiEvolution[i][0][0] = "Diaboromon"
        i += 1

        # Arcadiamon Ultra
        # from
        self.digiEvolution[i][0][0] = "Arcadiamon Mega"
        i += 1

        # Alphamon Ouryuken
        # from
        self.digiEvolution[i][0][0] = "Alphamon"
        self.digiEvolution[i][0][1] = "Ouryumon"
        i += 1

        # Imperialdramon PM
        # from
        self.digiEvolution[i][0][0] = "Imperialdramon DM"
        i += 1

        # Examon
        # from
        self.digiEvolution[i][0][0] = "Slayerdramon"
        self.digiEvolution[i][0][1] = "Breakdramon"
        i += 1

        # Omnimon
        # from
        self.digiEvolution[i][0][0] = "WarGreymon"
        self.digiEvolution[i][0][1] = "MetalGarurumon"
        i += 1

        # Omnimon Zwart
        # from
        self.digiEvolution[i][0][0] = "BlackWarGreymon"
        self.digiEvolution[i][0][1] = "MetalGarurumon BLK"
        i += 1

        # Chaosmon
        # from
        self.digiEvolution[i][0][0] = "BanchoLeomon"
        self.digiEvolution[i][0][1] = "Darkdramon"
        i += 1

        # Chaosmon VA
        # from
        self.digiEvolution[i][0][0] = "Varodurumon"
        self.digiEvolution[i][0][1] = "BanchoLeomon"
        i += 1

        # Susanomon
        # from
        self.digiEvolution[i][0][0] = "KaiserGreymon"
        self.digiEvolution[i][0][1] = "MagnaGarurumon"
        i += 1

        # Gallantmon CM
        # from
        self.digiEvolution[i][0][0] = "Gallantmon"
        i += 1

        # Belphemon RM
        # from
        self.digiEvolution[i][0][0] = "Belphemon SM"

        # for
        self.digiEvolution[i][1][0] = "Belphemon SM"
        i += 1

        # Lucemon SM
        # from
        self.digiEvolution[i][0][0] = "Lucemon FM"
        i += 1

        # Flamedramon
        # from
        self.digiEvolution[i][0][0] = "Veemon"
        i += 1

        # Magnamon
        # from
        self.digiEvolution[i][0][0] = "Veemon"
        self.digiEvolution[i][0][1] = "Guardromon(Gold)"
        i += 1

        # Rapidmon(Armor)
        # from
        self.digiEvolution[i][0][0] = "Terriermon"
        self.digiEvolution[i][0][1] = "Guardromon(Gold)"
        i += 1

        # Shoutmon
        # from
        self.digiEvolution[i][0][0] = "Koromon"

        # for
        self.digiEvolution[i][1][0] = "OmniShoutmon"
        i += 1

        # OmniShoutmon
        # from
        self.digiEvolution[i][0][0] = "Shoutmon"
        i += 1

        # Ryudamon
        # from
        self.digiEvolution[i][0][0] = "Wanyamon"

        # for
        self.digiEvolution[i][1][0] = "Ginryumon"
        self.digiEvolution[i][1][1] = "Raptordramon"
        self.digiEvolution[i][1][2] = "Reppamon"
        i += 1

        # Ginryudamon
        # from
        self.digiEvolution[i][0][0] = "Ryudamon"
        self.digiEvolution[i][0][1] = "Zubamon"
        self.digiEvolution[i][0][2] = "Dracomon"

        # for
        self.digiEvolution[i][1][0] = "Hisyaryumon"
        self.digiEvolution[i][1][1] = "CannonBeemon"
        self.digiEvolution[i][1][2] = "MegaSeadramon"
        i += 1

        # Hisyaryumon
        # from
        self.digiEvolution[i][0][0] = "Ginryumon"
        self.digiEvolution[i][0][1] = "Seadramon"
        self.digiEvolution[i][0][2] = "Coelamon"

        # for
        self.digiEvolution[i][1][0] = "Ouryumon"
        self.digiEvolution[i][1][1] = "Gaiomon"
        self.digiEvolution[i][1][2] = "Goldramon"
        self.digiEvolution[i][1][3] = "Minervamon"
        i += 1

        # Ouryumon
        # from
        self.digiEvolution[i][0][0] = "Hisyaryumon"
        self.digiEvolution[i][0][1] = "Grademon"
        self.digiEvolution[i][0][2] = "Crowmon"

        # for
        self.digiEvolution[i][1][0] = "Alphamon Ouryuken"
        i += 1

        # Apocalymon
        # from
        self.digiEvolution[i][0][0] = "MetalSeadramon"
        self.digiEvolution[i][0][1] = "Puppetmon"
        self.digiEvolution[i][0][2] = "Machinedramon"
        self.digiEvolution[i][0][3] = "Piedmon"
        i += 1

        # Sistermon Blanc
        # from
        self.digiEvolution[i][0][0] = "Tokomon"

        # for
        self.digiEvolution[i][1][0] = "Sistermon B Awake"
        self.digiEvolution[i][1][1] = "Sistermon Ciel"
        self.digiEvolution[i][1][2] = "Gargomon"
        self.digiEvolution[i][1][3] = "Lekismon"
        i += 1

        # Sistermon B Awake
        # from
        self.digiEvolution[i][0][0] = "Sistermon Blanc"
        i += 1

        # Sistermon Ciel
        # from
        self.digiEvolution[i][0][0] = "Sistermon Blanc"
        self.digiEvolution[i][0][1] = "Dracmon"
        self.digiEvolution[i][0][2] = "Lunamon"

        # for
        self.digiEvolution[i][1][0] = "Sistermon C Awake"
        self.digiEvolution[i][1][1] = "Pandamon"
        self.digiEvolution[i][1][2] = "LadyDevimon"
        i += 1

        # Sistermon C Awake
        # from
        self.digiEvolution[i][0][0] = "Sistermon Ciel"
        i += 1

        self.Digimons = [
            "Kuramon", "Pabumon", "Punimon", "Botamon", "Poyomon",
            "Arcadiamon In-Tr", "Koromon", "Tanemon", "Tsunomon", "Tsumemon", "Tokomon", "Nyaromon", "Pagumon", "Yokomon", "Bukamon", "Motimon", "Wanyamon",
            "Agumon", "Agumon BLK", "Arcadiamon Rookie", "Armadillomon", "Impmon", "Elecmon", "Otamamon", "Gaomon", "Gazimon", "Gabumon", "Gabumon BLK",
            "Guilmon", "Kudamon", "Keramon", "Gotsumon", "Goblimon", "Gomamon", "Syakomon", "Zubamon", "Solarmon", "Chuumon", "Terriermon", "Tentomon", "ToyAgumon", "Dracmon",
            "Dracomon", "Dorumon", "Hagurumon", "Patamon", "Hackmon", "Palmon", "DemiDevimon", "Biyomon", "Falcomon", "FanBeemon", "Veemon",
            "Salamon", "Betamon", "Hawkmon", "Mushroomon", "Monodramon", "Lalamon", "Lucemon", "Lunamon", "Renamon", "Lopmon", "Wormmon", "IceDevimon", "Icemon",
            "Aquilamon", "Agunimon", "Arcadiamon Champion", "Ankylomon", "Ikkakumon", "Wizardmon", "Lobomon", "Woodmon", "Airdramon", "ExVeemon", "Angemon", "Ogremon",
            "Guardromon", "Guardromon(Gold)", "GaoGamon", "Kabuterimon", "ShellNumemon", "Gargomon", "Garurumon", "Garurumon BLK", "Kyubimon", "Growlmon", "Kurisarimon",
            "Greymon", "Greymon(Blue)", "Clockmon", "Kuwagamon", "Gekomon", "Geremon", "Coredramon(Blue)", "Coredramon(Green)", "GoldNumemon", "Golemon", "Cyclonemon",
            "Sangloupmon", "Sunflowmon", "Seadramon", "Coelamon", "GeoGreymon", "Sukamon", "Starmon", "Stingmon", "Strikedramon", "Zubaeagermon", "Socerimon", "Tankmon",
            "MudFrigimon", "Tyrannomon", "Gatomon", "Devimon", "Turuiemon", "Togemon", "Dorugamon", "Nanimon", "Numemon", "Birdramon", "BaoHuckmon", "Bakemon", "Veedramon",
            "Hudiemon", "PlatinumSukamon", "BlackGatomon", "Vegiemon", "Peckmon", "Meramon", "Monochromon", "Frigimon", "Unimon", "Raptordramon", "Raremon", "Leomon",
            "Lekismon", "Reppamon", "Waspmon", "MegaKabuterimon", "Arcadiamon Ultimate", "Antylamon", "Andromon", "Meteormon", "Infermon", "Myotismon", "Wingdramon",
            "BurningGreymon", "AeroVeedramon", "Etemon", "Angewomon", "Okuwamon", "Garudamon", "KendoGarurumon", "Gigadramon", "CatchMamemon", "CannonBeemon", "Groundramon",
            "GrapLeomon", "Grademon", "Crescemon", "Cyberdramon", "Shakkoumon", "Cherrymon", "Silphymon", "SuperStarmon", "SkullGreymon", "SkullSatamon", "Zudomon",
            "SaviorHuckmon", "Taomon", "Dragomon", "Chirinmon", "Dinobeemon", "Digitamamon", "SkullMeramon", "Duramon", "ShogunGekomon", "Triceramon", "DoruGreymon",
            "Knightmon", "Datamon", "Paildramon", "Panjyamon", "Pandamon", "Pumpkinmon", "Piximon", "HippoGryphonmon", "Phantomon", "BlackKingNumemon", "BlueMeramon",
            "Vademon", "Whamon", "MagnaAngemon", "Volcanomon", "Matadormon", "MachGaogamon", "Mamemon", "MegaSeadramon", "Megadramon", "WarGrowlmon", "MetalGreymon",
            "MetalGreymon Blue", "MetalTyrannomon", "MetalMamemon", "Monzaemon", "Crowmon", "RizeGreymon", "Lilamon", "Rapidmon", "Lillymon", "Lucemon FM", "LadyDevimon",
            "WereGarurumon", "WereGarurumon BLK", "Wisemon", "Arcadiamon Mega", "Alphamon", "UlforceVeedramon", "Ebemon", "Imperialdramon DM", "Imperialdramon FM", "Vikemon",
            "Valkyrimon", "Varodurumon", "VenomMyotismon", "WarGreymon", "Ophanimon", "Gaiomon", "KaiserGreymon", "ChaosGallantmon", "Chaosdramon", "Gankoomon", "KingEtemon",
            "Kuzuhamon", "GranKuwagamon", "GranDracmon", "GroundLocomon", "Gryphonmon", "Craniamon", "Kerpymon BLK", "Kerpymon Good", "Goldramon", "SaberLeomon", "Sakuyamon",
            "Jesmon", "ShineGreymon", "ShineGreymon BM", "Justimon", "Kentaurosmon", "Slayerdramon", "Seraphimon", "MegaGargomon", "Darkdramon", "TigerVespamon", "Titamon",
            "TyrantKabuterimon", "Dianamon", "Diaboromon", "Creepymon", "Gallantmon", "Dynasmon", "Durandamon", "Leopardmon", "Leopardmon LM", "Dorugoramon", "Neptunemon", "HiAndromon",
            "PileVolcamon", "Barbamon", "BanchoLeomon", "Piedmon", "Puppetmon", "PlatinumNumemon", "BlackWarGreymon", "PrinceMamemon", "Breakdramon", "Plesiomon", "HerculesKabuterimon",
            "Beelzemon", "Beelzemon BM", "Belphemon SM", "Hououmon", "Magnadramon", "Boltmon", "MagnaGarurumon", "MagnaGarurumon SV", "Mastemon", "MarineAngemon", "Minervamon", "MirageGaogamon", "MirageGaogamon BM",
            "Machinedramon", "Megidramon", "MetalEtemon", "MetalGarurumon", "MetalGarurumon BLK", "MetalSeadramon", "Merukimon", "RustTyranomon", "Leviamon", "Lilithmon", "Ravemon", "Ravemon BM",
            "Crusadermon", "Rosemon", "Rosemon BM", "Lotosmon", "Armageddemon", "Arcadiamon Ultra", "Alphamon Ouryuken", "Imperialdramon PM", "Examon", "Omnimon", "Omnimon Zwart", "Chaosmon",
            "Chaosmon VA", "Susanomon", "Gallantmon CM", "Belphemon RM", "Lucemon SM", "Flamedramon", "Magnamon", "Rapidmon Armor", "Shoutmon", "OmniShoutmon", "Ryudamon", "Ginryumon", "Hisyaryumon",
            "Ouryumon", "Apocalymon", "Sistermon Blanc", "Sistermon B Awake", "Sistermon Ciel", "Sistermon C Awake", "Alphamon NX", "Crusadermon NX", "Leopardmon NX", "Omnimon NX", "Gallantmon NX"
        ]

        print("DataCreated")

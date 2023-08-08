import DbDatabase
database = DbDatabase.DbDatabase()


class DPath:
    def __init__(self, initial, final):
        self.initial = initial
        self.final = final
        self.final_real = final

        self.seekCache = []
        self.path = []
        self.initPath()

    def initPath(self):
        self.path.append(self.final_real)
        id = self.getDigimonID(self.initial)
        found = self.seek(id)
        while (found == False):
            for cached in self.seekCache:
                id = self.getDigimonID(cached)
                found = self.seek(id)
                if (found):
                    break
        self.path.append(self.initial)
        print(self.path)

    def getDigimonID(self, digimon):
        try:
            return database.Digimons.index(digimon)
        except:
            pass

    def seek(self, id):
        try:
            for way in range(2):
                for digivolution in range(8):
                    if (database.digiEvolution[id][way][digivolution] == self.final):
                        print(f"Found throught {database.Digimons[id]}")
                        if (database.Digimons[id] != self.initial):
                            self.final = database.Digimons[id]
                            self.path.append(self.final)
                            self.seekCache.clear()
                            self.seekCache.append(self.initial)
                            return False
                        return True
                    else:
                        self.seekCache.append(
                            database.digiEvolution[id][way][digivolution])
        except:
            pass
        return False

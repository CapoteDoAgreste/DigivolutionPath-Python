import DbDatabase
database = DbDatabase.DbDatabase()


class DPath:
    def __init__(self, initial, final, exceptions=""):
        self.initial = initial
        self.final = final
        self.final_real = final
        self.exceptions = exceptions

        self.seekCache = []
        self.path = []
        self.initPath()

    def initPath(self):
        self.path.append(self.final_real)
        id = self.getDigimonID(self.initial)
        found = self.seek(id, self.exceptions)
        while (found == False):
            for cached in self.seekCache:
                id = self.getDigimonID(cached)
                found = self.seek(id, self.exceptions)
                if (found):
                    break
        self.path.append(self.initial)
        print(self.path)

    def getDigimonID(self, digimon):
        try:
            return database.Digimons.index(digimon)
        except:
            pass

    def seek(self, id, exceptions):
        try:
            for way in range(2):
                for digivolution in range(8):
                    if (database.digiEvolution[id][way][digivolution] == self.final and database.Digimons[id] not in exceptions):
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

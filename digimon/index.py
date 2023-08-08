import DPath


class SeekStart:
    def __init__(self):
        self.initialDigimon = "Botamon"
        self.FinalDigimon = "Renamon"
        self.path = DPath.DPath(self.initialDigimon, self.FinalDigimon)


init = SeekStart()

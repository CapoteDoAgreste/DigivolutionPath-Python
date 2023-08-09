import DPath


class SeekStart:
    def __init__(self):
        self.initialDigimon = "Omnimon"
        self.FinalDigimon = "Agumon"
        self.exceptions = ["Koromon"]
        self.path = DPath.DPath(
            self.FinalDigimon, self.initialDigimon, self.exceptions)


init = SeekStart()

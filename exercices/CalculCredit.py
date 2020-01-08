class Credit:
    def __init__(self, capital, duree):
        self.capital = capital
        self.duree = duree*12

    def taux(self):
        if (self.duree <= 7*12):
            return 0.92
        elif (self.duree <= 10*12):
            return 1.1
        elif (self.duree <= 15*12):
            return 1.38
        elif (self.duree <= 20*12):
            return 1.6
        else:
            return -1


    def mensualite(self):
        __mensualite = 0
        __taux = self.taux()
        # si le capital est nul, il n'y a rien à rembourser
        if self.capital == 0:
            __mensualite = 0
            return __mensualite
        # si l'intérêt est nul, la mensualité ne dépend plus que de C et N
        if __taux==0:
            __mensualite=self.capital/self.duree
            return __mensualite
        # calcul de la mensualité dans le cas général
        __taux=__taux/1200
        __mensualite=self.capital*__taux*(1-1/(1-(1+__taux)**self.duree))
        return round(__mensualite, 2)

    def cout_total(self):
        return round(self.mensualite()*self.duree - self.capital, 2)

credit = Credit (100000, 20)


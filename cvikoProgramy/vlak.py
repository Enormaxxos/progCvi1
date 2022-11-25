class Masina:
    def __init__(self, prvni_vagon=None):
        self.dalsi = prvni_vagon
        self.posledni = None

    def __str__(self):
        final = ""
        current = self.dalsi

        if current == None:
            final += "Vlak nema vagony."

        while current:
            final += f"Vagon vezouci {current.naklad} v mnozstvi {current.mnozstvi}\n"
            current = current.dalsi
        return final[:-1]

    def pridej_na_konec(self, vagon):

        if self.posledni:
            self.posledni.dalsi = vagon
            self.posledni = self.posledni.dalsi

        if self.dalsi == None:
            self.dalsi = vagon
            self.posledni = vagon
            return True

        current = self.dalsi
        while current.dalsi != None:
            current = current.dalsi

        current.dalsi = vagon
        self.posledni = current.dalsi
        return True

    def pridej_na_zacatek(self, vagon):
        current = self.dalsi
        self.dalsi = vagon
        self.dalsi.dalsi = current

    def odeber_nejvetsi(self):
        prev_max_vagon = None
        maximalni_vagon = None

        current = self.dalsi
        prevCurrent = self

        while current:
            if maximalni_vagon == None or maximalni_vagon.mnozstvi < current.mnozstvi:
                maximalni_vagon = current
                prev_max_vagon = prevCurrent
            prevCurrent = current
            current = current.dalsi

        prev_max_vagon.dalsi = maximalni_vagon.dalsi

    def pridej_za_nejvetsi(self,vagon):
        maximalni_vagon = None

        current = self.dalsi
        while current:
            if maximalni_vagon == None or maximalni_vagon.mnozstvi < current.mnozstvi:
                maximalni_vagon = current
            current = current.dalsi

        vagon.dalsi = maximalni_vagon.dalsi
        maximalni_vagon.dalsi = vagon

        return True

class Vagon:
    def __init__(self, ceho=None, kolik=0, dalsi=None):
        self.naklad = ceho
        self.mnozstvi = kolik
        self.dalsi = dalsi

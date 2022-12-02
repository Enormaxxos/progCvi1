class Masina:
    def __init__(self, prvni_vagon=None):
        self.dalsi = prvni_vagon
        self.posledni = None

    def __str__(self):
        final = ""
        current = self.dalsi

        while current:
            final += f"Vagon vezouci {current.naklad} v mnozstvi {current.mnozstvi}\n"
            current = current.dalsi
            
        return final[:-1]

    def pridat_na_konec(self, vagon):

        # print(vagon.naklad)

        # if self.posledni:
        #     self.posledni.dalsi = vagon
        #     self.posledni = self.posledni.dalsi
        #     print("short way")
        #     return True

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

    def pridat_za_masinu(self, vagon):
        current = self.dalsi
        vagon.dalsi = current
        self.dalsi = vagon

    def najdiNejvetsi(self,prev):
        prev_max = None
        max_vagon = None

        current = self.dalsi
        prevCurrent = self

        while current:
            if max_vagon == None or max_vagon.mnozstvi < current.mnozstvi:
                max_vagon = current
                prev_max = prevCurrent
            
            prevCurrent = current
            current = current.dalsi

        if prev:
            return (prev_max, max_vagon)
        else:
            # print(max_vagon.naklad)
            return max_vagon


    def odebrat_nejvetsi(self):
        if self.dalsi == None:
            return

        predNejvetsim, nejvetsi = self.najdiNejvetsi(True)

        # if nejvetsi.dalsi == None:
        #     self.posledni = predNejvetsim

        predNejvetsim.dalsi = nejvetsi.dalsi

    def pridat_za_nejvetsi(self,vagon):
        if self.dalsi == None:
            self.dalsi = vagon
            self.posledni = self.dalsi
            return

        nejvetsi = self.najdiNejvetsi(False)

        temp = nejvetsi.dalsi
        nejvetsi.dalsi = vagon
        # if temp == None:
        #     self.posledni = nejvetsi.dalsi
        nejvetsi.dalsi.dalsi = temp

class Vagon:
    def __init__(self, ceho=None, kolik=0, dalsi=None):
        self.naklad = ceho
        self.mnozstvi = kolik
        self.dalsi = dalsi


vlak = Masina()

def inputHandler(inputList):
    for instruction in inputList:
        whatDo = instruction[0]
        ofWhat = instruction[1]
        howMuch = instruction[2]

        try:
            if whatDo == "odebrat_nejvetsi":
                vlak.odebrat_nejvetsi()
            else:
                eval(f"vlak.{whatDo}(Vagon(ceho='{ofWhat}',kolik={howMuch}))")
        except AttributeError:
            print("ERROR")
            return

    print(vlak)

inputHandler(eval(input()))

# import random

# a = Masina()

# a.pridat_za_masinu(Vagon("zacatek",10))

# for i in range(20):

#     znak = chr(ord("a")+i)
#     mnozstvi = random.randrange(5,400)

#     print(f"adding {znak} of {mnozstvi} after",end=" ")

#     a.pridat_za_nejvetsi(Vagon(znak,mnozstvi))

# print(a)
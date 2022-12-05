import gzip
import shutil

with open("soubor.txt","rb") as inF:
    with gzip.open("soubor.txt.gz","wb") as outF:
        shutil.copyfileobj(inF,outF)
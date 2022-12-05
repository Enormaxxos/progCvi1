import gzip

with gzip.open("soubor.txt.gz","rb") as o:
    with open("vystupni_soubor.txt","wb") as out:
        out.write(o.read())
from ExtraETFParser import ExtraetfETF #Die Klasse Importieren

#Beispielhafte Anwendung des extraETF Parsers
# Als "IDs" werden die ISINs der Wertpapiere verwendet
IDs = ["IE00B5BMR087", "IE00B4L5Y983", "IE00B3XXRP09", "IE00BKM4GZ66", "LU1829221024", "IE00B1FZS350"]

ETFs = []

for id in IDs:
    etf = ExtraetfETF(id) #Objekt der Klasse ExtraetfETF erzeugen
    etf.parse() #Daten holen
    etf.print() #Daten ausgeben (optional)
    ETFs.append(etf)
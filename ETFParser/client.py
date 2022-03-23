from ExtraETFParser import ExtraetfETF

#Beispielhafte Anwendung des extraETF Parsers
IDs = ["IE00B5BMR087", "IE00B4L5Y983", "IE00B3XXRP09", "IE00BKM4GZ66", "LU1829221024", "IE00B1FZS350"]

ETFs = []

for id in IDs:
    etf = ExtraetfETF(id)
    etf.parse()
    etf.print()
    ETFs.append(etf)
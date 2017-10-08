import sys

lastKey = None
totalSales = 0.0

for line in sys.stdlin:
    mappedData = line.strip().split("\t")
    if len(mappedData) != 2:
        continue

    thisKey, thisSale = mappedData

    if lastKey and lastKey != thisKey:
        print lastKey, "\t", totalSales
        lastKey = thisKey
        totalSales = 0

    lastKey = thisKey
    totalSales += float(thisSale)

if lastKey != None:
    print lastKey, "\t", totalSales
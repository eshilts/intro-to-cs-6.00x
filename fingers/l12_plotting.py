import pylab

def loadJulyTemps():
    high = []
    low = []
    inFile = open('julyTemps.txt')

    for line in inFile:
        fields = line.split()
        if len(fields) < 3 or not fields[0].isdigit():
            continue
        high.append(int(fields[1]))
        low.append(int(fields[2]))

    return (high, low)


def producePlot(lowTemps, highTemps):
    diffTemps = []
    for low, high in zip(lowTemps, highTemps):
        diffTemps.append(high - low)

    pylab.figure(1)
    pylab.plot(range(1, 32), diffTemps)
    pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature Ranges')
    pylab.show()

high_low = loadJulyTemps()
#producePlot(high_low[1], high_low[0])

def plotHighAndLowTemps(lowTemps, highTemps):
    pylab.figure(2)
    pylab.plot(range(1, 32), lowTemps, 'b--')
    pylab.plot(range(1, 32), highTemps, 'r-')
    pylab.title('Day by Day High and Low Temperatures in Boston in July 2012')
    pylab.xlabel('Days')
    pylab.ylabel('Temperature')
    pylab.annotate('High', (31.5, highTemps[-1]), color='r')
    pylab.annotate('Low', (31.5, lowTemps[-1]), color='b')
    pylab.show()

plotHighAndLowTemps(high_low[1], high_low[0])

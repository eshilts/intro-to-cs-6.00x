# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b import *

#
# PROBLEM 1
#        

def plotHistogram(data, preTime):
    pylab.figure(1)
    pylab.hist(data, bins=10)
    pylab.xlabel("Virus Population At End of Simulation")
    pylab.ylabel("Number of Trials")
    pylab.title("{0} Time Steps Before Treatment Simulation".format(preTime))
    pylab.show()
    

def simulationDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 1.

    Runs numTrials simulations to show the relationship between delayed
    treatment and patient outcome using a histogram.

    Histograms of final total virus populations are displayed for delays of 300,
    150, 75, 0 timesteps (followed by an additional 150 timesteps of
    simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # Initialize parameters from ps8
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False}
    mutProb = 0.005


    viruses = []
    for nv in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))

    preTreatmentTimeSteps = [300, 150, 75, 0]
    postTreatmentTimeSteps = 150
    outcomeTypes = ['Total', 'Resistant']
    outcomes = {}

    finalOutcomes = {}

    # Initialize outcomes to store results
    # outcomes is a dict to store the populations of average and resistant
    # viruses. Each element stores a dict with four arrays of the total viruses
    # found at each time step, keyed by the number of steps prior to treatment.
    # Thus each array will have len() of preTreatmentSteps + 150.
    for outcomeType in outcomeTypes:
        outcomes[outcomeType] = {}
        finalOutcomes[outcomeType] = {}
        for pre in preTreatmentTimeSteps:
            outcomes[outcomeType][pre] = []
            finalOutcomes[outcomeType][pre] = []
            for preTimeStep in range(pre + postTreatmentTimeSteps):
                outcomes[outcomeType][pre].append(0.0)

    for pre in preTreatmentTimeSteps:

        for numTrial in range(numTrials):
            print "PreTreatTimeSteps {0} - Trial # {1}".format(pre, numTrial)
            patient = TreatedPatient(viruses[:], maxPop)

            for preTimeStep in range(pre):
                patient.update()
                outcomes['Total'][pre][preTimeStep] += patient.getTotalPop()
                outcomes['Resistant'][pre][preTimeStep] += patient.getResistPop(['guttagonol'])

            patient.addPrescription('guttagonol')

            for postTimeStep in range(postTreatmentTimeSteps):
                patient.update()
                outcomes['Total'][pre][postTimeStep] += patient.getTotalPop()
                outcomes['Resistant'][pre][postTimeStep] += patient.getResistPop(['guttagonol'])

            finalOutcomes['Total'][pre].append(patient.getTotalPop())
            finalOutcomes['Resistant'][pre].append(patient.getResistPop(['guttagonol']))

    for outcomeType in outcomeTypes:
        for pre in preTreatmentTimeSteps:
            for preTimeStep in range(pre + postTreatmentTimeSteps):
                outcomes[outcomeType][pre][preTimeStep] /= numTrials

    #print "Average population (length = {1}) = {0}".format(averagePopulation, len(averagePopulation))
    #print "Average resistant population (length = {1}) = {0}".format(resistantPopulation, len(resistantPopulation))

    for pre in preTreatmentTimeSteps:
        plotHistogram(finalOutcomes['Total'][pre], pre)


#simulationDelayedTreatment(125)

#
# PROBLEM 2
#
def simulationTwoDrugsDelayedTreatment(numTrials):
    """
    Runs simulations and make histograms for problem 2.

    Runs numTrials simulations to show the relationship between administration
    of multiple drugs and patient outcome.

    Histograms of final total virus populations are displayed for lag times of
    300, 150, 75, 0 timesteps between adding drugs (followed by an additional
    150 timesteps of simulation).

    numTrials: number of simulation runs to execute (an integer)
    """
    # Initialize parameters from ps8
    numViruses = 100
    maxPop = 1000
    maxBirthProb = 0.1
    clearProb = 0.05
    resistances = {'guttagonol': False, 'grimpex': False}
    mutProb = 0.005

    viruses = []
    for nv in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))

    prePreTreatmentTimeSteps = 150
    preTreatmentTimeSteps = [300, 150, 75, 0]
    postTreatmentTimeSteps = 150
    outcomeTypes = ['Total', 'Resistant']
    outcomes = {}

    finalOutcomes = {}

    # Initialize outcomes to store results
    # outcomes is a dict to store the populations of average and resistant
    # viruses. Each element stores a dict with four arrays of the total viruses
    # found at each time step, keyed by the number of steps prior to treatment.
    # Thus each array will have len() of preTreatmentSteps + 150.
    for outcomeType in outcomeTypes:
        finalOutcomes[outcomeType] = {}
        for pre in preTreatmentTimeSteps:
            finalOutcomes[outcomeType][pre] = []

    for pre in preTreatmentTimeSteps:

        for numTrial in range(numTrials):
            print "PreTreatTimeSteps {0} - Trial # {1}".format(pre, numTrial)
            patient = TreatedPatient(viruses[:], maxPop)

            for preTimeStep in range(prePreTreatmentTimeSteps):
                patient.update()

            patient.addPrescription('guttagonol')

            for preTimeStep in range(pre):
                patient.update()

            patient.addPrescription('grimpex')

            for postTimeStep in range(postTreatmentTimeSteps):
                patient.update()

            finalOutcomes['Total'][pre].append(patient.getTotalPop())
            finalOutcomes['Resistant'][pre].append(patient.getResistPop(['guttagonol', 'grimpex']))

    for pre in preTreatmentTimeSteps:
        print "Virus population - {0} time steps - mean: {1}, sd: {2}".format(
                pre, 
                round(numpy.mean(finalOutcomes['Total'][pre]), 3),
                round(numpy.std(finalOutcomes['Total'][pre]), 3))
        plotHistogram(finalOutcomes['Total'][pre], pre)

simulationTwoDrugsDelayedTreatment(250)

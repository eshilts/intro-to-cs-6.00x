# 6.00 Problem Set 9

import numpy
import random
import pylab
from ps8b import *

#
# PROBLEM 1
#        
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

    # Initialize outcomes to store results
    # outcomes is a dict to store the populations of average and resistant
    # viruses. Each element stores a dict with four arrays of the total viruses
    # found at each time step, keyed by the number of steps prior to treatment.
    # Thus each array will have len() of preTreatmentSteps + 150.
    for outcomeType in outcomeTypes:
        outcomes[outcomeType] = {}
        for pre in preTreatmentTimeSteps:
            outcomes[outcomeType][pre] = []
            for preTimeStep in range(pre + postTreatmentTimeSteps):
                outcomes[outcomeType][pre].append(0)

    for pre in preTreatmentTimeSteps:

        for numTrial in range(numTrials):
            #print "PreTreatTimeSteps {0} - Trial # {1}".format(pre, numTrial)
            patient = TreatedPatient(viruses[:], maxPop)

            for preTimeStep in range(pre):
                patient.update()
                outcomes['Total'][pre][preTimeStep] += patient.getTotalPop()
                outcomes['Resistant'][pre][preTimeStep] += patient.getResistPop(['guttagonol'])

            patient.addPrescription('guttagonol')

            for postTimeStep in range(postTimeSteps):
                patient.update()
                outcomes['Total'][pre][postTimeStep] += patient.getTotalPop()
                outcomes['Resistant'][pre][postTimeStep] += patient.getResistPop(['guttagonol'])

    for outcomeType in outcomeTypes:
        for pre in preTreatmentTimeSteps:
            for preTimeStep in range(pre + postTreatmentTimeSteps):
                outcomes[outcomeType][pre] /= numTrials

    #print "Average population (length = {1}) = {0}".format(averagePopulation, len(averagePopulation))
    #print "Average resistant population (length = {1}) = {0}".format(resistantPopulation, len(resistantPopulation))

    pylab.figure(1)
    for outcomeType in outcomeTypes:
        for pre in preTreatmentTimeSteps:
            pylab.plot(outcomes[outcomeType][pre], label="{0} population - {1} steps before treatment".format(
                outcomeType, pre)
    pylab.plot(resistantPopulation, 'g-', label='Average resistant population')
    pylab.xlabel("Time Steps")
    pylab.ylabel("Virus Population")
    pylab.title("ResistantVirus simulation")
    pylab.legend(loc='best')
    pylab.show()
    

simulationDelayedTreatment(1)




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
    # TODO

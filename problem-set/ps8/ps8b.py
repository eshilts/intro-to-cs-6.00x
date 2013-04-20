# Problem Set 8: Simulating the Spread of Disease and Virus Population Dynamics 

import numpy
import random
import pylab

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 2
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):
        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb


    def getMaxBirthProb(self):
        """
        Returns the max birth probability.
        """
        return self.maxBirthProb


    def getClearProb(self):
        """
        Returns the clear probability.
        """
        return self.clearProb


    def doesClear(self):
        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.getClearProb and otherwise returns
        False.
        """
        if random.random() < self.getClearProb():
            return True
        return False

    
    def reproduce(self, popDensity):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the Patient and
        TreatedPatient classes. The virus particle reproduces with probability
        self.getMaxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """
        if random.random() < self.getMaxBirthProb() * (1 - popDensity):
            return SimpleVirus(self.getMaxBirthProb(), self.getClearProb())
        raise NoChildException


class Patient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the maximum virus population for this patient (an integer)
        """
        self.viruses = viruses
        self.maxPop = maxPop


    def getViruses(self):
        """
        Returns the viruses in this Patient.
        """
        return self.viruses


    def getMaxPop(self):
        """
        Returns the max population.
        """
        return self.maxPop


    def getTotalPop(self):
        """
        Gets the size of the current total virus population. 
        returns: The total virus population (an integer)
        """
        return len(self.getViruses())

    def getPopDensity(self):
        """
        Gets the virus population density.
        returns: self.getTotalPop() / self.getMaxPop()
        """
        return float(self.getTotalPop()) / self.getMaxPop()


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        
        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        #print "Virus population at beginning of update: {0}".format(self.getTotalPop())
        survivingViruses = []
        for virus in self.getViruses():
            if not virus.doesClear():
                survivingViruses.append(virus)
        #print "Number of surviving viruses: {0}".format(len(survivingViruses))
        self.viruses = survivingViruses[:]

        popDensity = self.getPopDensity()
        childViruses = []
        for virus in self.getViruses():
            try:
                child = virus.reproduce(popDensity)
                childViruses.append(child)
            except NoChildException:
                next

        self.viruses += childViruses

        #print "Virus population [{0}] after adding children [{1}]: {2}".format(
        #        len(survivingViruses), len(childViruses), self.getTotalPop())

        return self.getTotalPop()
                

maxPop = 20
maxBirthProb = 0.5
clearProb = 0.05
numViruses = 10

newViruses = []
for i in range(numViruses):
    newViruses.append(SimpleVirus(maxBirthProb, clearProb))

patient = Patient(newViruses[:], maxPop)

for i in range(5):
    patient.update()

virus = SimpleVirus(1.0, 0.0)
patient = Patient([virus], 100)
for i in range(100):
    patient.update()
print "Total population: ", patient.getTotalPop()


#
# PROBLEM 3
#

random.seed(0)

def simulationWithoutDrug(numViruses, maxPop, maxBirthProb, clearProb,
                          numTrials):
    """
    Run the simulation and plot the graph for problem 3 (no drugs are used,
    viruses do not have any drug resistance).    
    For each of numTrials trial, instantiates a patient, runs a simulation
    for 300 timesteps, and plots the average virus population size as a
    function of time.

    numViruses: number of SimpleVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: Maximum clearance probability (a float between 0-1)
    numTrials: number of simulation runs to execute (an integer)
    """
    viruses = []
    for nv in range(numViruses):
        viruses.append(SimpleVirus(maxBirthProb, clearProb))

    timeSteps = 300
    outcomes = []
    for ts in range(timeSteps):
        outcomes.append([])

    for nt in range(numTrials):
        print "Trial # {0}".format(nt)
        patient = Patient(viruses[:], maxPop)

        for ts in range(timeSteps):
            patient.update()
            outcomes[ts].append(patient.getTotalPop())

    averagePopulation = []
    for ts in range(timeSteps):
        averagePopulation.append(sum(outcomes[ts]) / float(numTrials))

    #print "Average population = {0}".format(averagePopulation)

    pylab.figure(1)
    pylab.plot(range(timeSteps), averagePopulation, label='SimpleVirus population')
    pylab.xlabel("Time Steps")
    pylab.ylabel("Average Virus Population")
    pylab.title("SimpleVirus simulation")
    pylab.legend(loc='best')
    pylab.show()

#simulationWithoutDrug(100, 1000, 0.1, 0.05, 10)


#
# PROBLEM 4
#
class ResistantVirus(SimpleVirus):
    """
    Representation of a virus which can have drug resistance.
    """   

    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        """
        Initialize a ResistantVirus instance, saves all parameters as attributes
        of the instance.

        maxBirthProb: Maximum reproduction probability (a float between 0-1)       

        clearProb: Maximum clearance probability (a float between 0-1).

        resistances: A dictionary of drug names (strings) mapping to the state
        of this virus particle's resistance (either True or False) to each drug.
        e.g. {'guttagonol':False, 'srinol':False}, means that this virus
        particle is resistant to neither guttagonol nor srinol.

        mutProb: Mutation probability for this virus particle (a float). This is
        the probability of the offspring acquiring or losing resistance to a drug.
        """
        SimpleVirus.__init__(self, maxBirthProb, clearProb)
        self.resistances = resistances
        self.mutProb = mutProb


    def getResistances(self):
        """
        Returns the resistances for this virus.
        """
        return self.resistances

    def getMutProb(self):
        """
        Returns the mutation probability for this virus.
        """
        return self.mutProb

    def isResistantTo(self, drug):
        """
        Get the state of this virus particle's resistance to a drug. This method
        is called by getResistPop() in TreatedPatient to determine how many virus
        particles have resistance to a drug.       

        drug: The drug (a string)

        returns: True if this virus instance is resistant to the drug, False
        otherwise.
        """
        return self.getResistances().get(drug, False)

    def isResistantToAll(self, activeDrugs):
        """
        Gets the state of this virus particle's resistance to all drugs in the
        list of drugs given by activeDrugs.

        activeDrugs: List of drugs to check resistance

        returns: A boolean of whether the virus is resistant to all activeDrugs
        """
        resistantToAll = True
        for drug in activeDrugs:
            if not self.isResistantTo(drug):
                resistantToAll = False

        return resistantToAll

    def reproduce(self, popDensity, activeDrugs):
        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the TreatedPatient class.

        A virus particle will only reproduce if it is resistant to ALL the drugs
        in the activeDrugs list. For example, if there are 2 drugs in the
        activeDrugs list, and the virus particle is resistant to 1 or no drugs,
        then it will NOT reproduce.

        Hence, if the virus is resistant to all drugs
        in activeDrugs, then the virus reproduces with probability:      

        self.getMaxBirthProb * (1 - popDensity).                       

        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring ResistantVirus (which has the same
        maxBirthProb, clearProb, and mutProb values as its parent). The offspring virus
        will have the same maxBirthProb, clearProb, and mutProb as the parent.

        For each drug resistance trait of the virus (i.e. each key of
        self.resistances), the offspring has probability 1-mutProb of
        inheriting that resistance trait from the parent, and probability
        mutProb of switching that resistance trait in the offspring.       

        For example, if a virus particle is resistant to guttagonol but not
        srinol, and self.mutProb is 0.1, then there is a 10% chance that
        that the offspring will lose resistance to guttagonol and a 90%
        chance that the offspring will be resistant to guttagonol.
        There is also a 10% chance that the offspring will gain resistance to
        srinol and a 90% chance that the offspring will not be resistant to
        srinol.

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population       

        activeDrugs: a list of the drug names acting on this virus particle
        (a list of strings).

        returns: a new instance of the ResistantVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.
        """
        if self.isResistantToAll(activeDrugs):
            if random.random() < self.getMaxBirthProb() * (1 - popDensity):
                childResistances = self.getResistances().copy()

                for resistance in childResistances:
                    if random.random() < self.getMutProb():
                        childResistances[resistance] = not childResistances[resistance]

                return ResistantVirus(
                        self.getMaxBirthProb(), 
                        self.getClearProb(), 
                        childResistances.copy(),
                        self.getMutProb())

        raise NoChildException

virus = ResistantVirus(1.0, 0.0, {}, 0.0)


class TreatedPatient(Patient):
    """
    Representation of a patient. The patient is able to take drugs and his/her
    virus population can acquire resistance to the drugs he/she takes.
    """

    def __init__(self, viruses, maxPop):
        """
        Initialization function, saves the viruses and maxPop parameters as
        attributes. Also initializes the list of drugs being administered
        (which should initially include no drugs).              

        viruses: The list representing the virus population (a list of
        virus instances)

        maxPop: The  maximum virus population for this patient (an integer)
        """
        Patient.__init__(self, viruses, maxPop)
        self.prescriptions = []


    def getPopDensity(self):                                                    
        """                                                                     
        Gets the virus population density.                                      
        returns: self.getTotalPop() / self.getMaxPop()                          
        """                                                                     
        return float(self.getTotalPop()) / self.getMaxPop()                     


    def addPrescription(self, newDrug):
        """
        Administer a drug to this patient. After a prescription is added, the
        drug acts on the virus population for all subsequent time steps. If the
        newDrug is already prescribed to this patient, the method has no effect.

        newDrug: The name of the drug to administer to the patient (a string).

        postcondition: The list of drugs being administered to a patient is updated
        """
        if newDrug not in self.getPrescriptions():
            self.prescriptions.append(newDrug)


    def getPrescriptions(self):
        """
        Returns the drugs that are being administered to this patient.

        returns: The list of drug names (strings) being administered to this
        patient.
        """
        return self.prescriptions[:]


    def getResistPop(self, drugResist):
        """
        Get the population of virus particles resistant to the drugs listed in
        drugResist.       

        drugResist: Which drug resistances to include in the population (a list
        of strings - e.g. ['guttagonol'] or ['guttagonol', 'srinol'])

        returns: The population of viruses (an integer) with resistances to all
        drugs in the drugResist list.
        """
        resistantViruses = []
        for virus in self.getViruses():
            if virus.isResistantToAll(drugResist):
                resistantViruses.append(virus)

        return len(resistantViruses)


    def update(self):
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute these actions in order:

        - Determine whether each virus particle survives and update the list of
          virus particles accordingly

        - The current population density is calculated. This population density
          value is used until the next call to update().

        - Based on this value of population density, determine whether each 
          virus particle should reproduce and add offspring virus particles to 
          the list of viruses in this patient.
          The list of drugs being administered should be accounted for in the
          determination of whether each virus particle reproduces.

        returns: The total virus population at the end of the update (an
        integer)
        """
        survivingViruses = []

        for virus in self.getViruses():
            if not virus.doesClear():
                survivingViruses.append(virus)

        self.viruses = survivingViruses[:]
        popDensity = self.getPopDensity()
        childViruses = []

        for virus in self.getViruses():
            try:
                childVirus = virus.reproduce(popDensity, self.getPrescriptions())
                childViruses.append(childVirus)
            except NoChildException:
                next

        self.viruses += childViruses[:]

        return self.getTotalPop()


#
# PROBLEM 5
#
def simulationWithDrug(numViruses, maxPop, maxBirthProb, clearProb, resistances,
                       mutProb, numTrials):
    """
    Runs simulations and plots graphs for problem 5.

    For each of numTrials trials, instantiates a patient, runs a simulation for
    150 timesteps, adds guttagonol, and runs the simulation for an additional
    150 timesteps.  At the end plots the average virus population size
    (for both the total virus population and the guttagonol-resistant virus
    population) as a function of time.

    numViruses: number of ResistantVirus to create for patient (an integer)
    maxPop: maximum virus population for patient (an integer)
    maxBirthProb: Maximum reproduction probability (a float between 0-1)        
    clearProb: maximum clearance probability (a float between 0-1)
    resistances: a dictionary of drugs that each ResistantVirus is resistant to
                 (e.g., {'guttagonol': False})
    mutProb: mutation probability for each ResistantVirus particle
             (a float between 0-1). 
    numTrials: number of simulation runs to execute (an integer)
    
    """
    viruses = []
    for nv in range(numViruses):
        viruses.append(ResistantVirus(maxBirthProb, clearProb, resistances, mutProb))

    timeSteps = 150
    averageOutcomes = []
    resistantOutcomes = []
    for ts in range(timeSteps * 2):
        averageOutcomes.append([])
        resistantOutcomes.append([])

    for nt in range(numTrials):
        #print "Trial # {0}".format(nt)
        patient = TreatedPatient(viruses[:], maxPop)

        for ts in range(timeSteps):
            patient.update()
            averageOutcomes[ts].append(patient.getTotalPop())
            resistantOutcomes[ts].append(patient.getResistPop(['guttagonol']))

        patient.addPrescription('guttagonol')

        for ts in range(timeSteps):
            patient.update()
            averageOutcomes[ts + timeSteps].append(patient.getTotalPop())
            resistantOutcomes[ts +
                    timeSteps].append(patient.getResistPop(['guttagonol']))

    averagePopulation = []
    resistantPopulation = []
    for ts in range(timeSteps * 2):
        averagePopulation.append(sum(averageOutcomes[ts]) / float(numTrials))
        resistantPopulation.append(sum(resistantOutcomes[ts]) / float(numTrials))

    #print "Average population (length = {1}) = {0}".format(averagePopulation, len(averagePopulation))
    #print "Average resistant population (length = {1}) = {0}".format(resistantPopulation, len(resistantPopulation))

    pylab.figure(1)
    pylab.plot(range(timeSteps * 2), averagePopulation, label='Average total population')
    pylab.plot(resistantPopulation, 'g-', label='Average resistant population')
    pylab.xlabel("Time Steps")
    pylab.ylabel("Virus Population")
    pylab.title("ResistantVirus simulation")
    pylab.legend(loc='best')
    pylab.show()

simulationWithDrug(100, 1000, 0.1, 0.05, {'guttagonol': False}, 0.005, 10)

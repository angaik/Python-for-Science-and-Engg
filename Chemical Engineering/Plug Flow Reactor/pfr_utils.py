from dataclasses import dataclass
import math
from enum import Enum

Univ_Gas_Const = 8.314      # kJ/kmol-K

@dataclass
class ReactorFDMSolver:
    """Class to store solver settings to solve the finite difference equations
    Settings: Time step and length step"""
    time_step : float = 0.1
    length_step : float = 0.1

@dataclass
class Reactor:
    """Class to store reactor dimensions"""
    cooling : bool
    cross_section_area : float = 0.1
    length : float = 1
    cooling_duty_kJ : float = 0

@dataclass
class Chemical:
    name : str
    mol_wt : float
    sp_heat_cap : float

    # Added hash function to enable Chemical object to be used as dictionary
    # key. e.g. Refer Reaction object's 'stoic_cf' variable
    def __hash__(self) -> int:
        return hash(str(self))

@dataclass
class Reaction:
    """Class to store details of reaction thermodynamics & kinetics, like rate 
    equations."""
    
    # class Reaction should be composed of species & corresponding stoichiometric cf
    # too. Reaction.stoic_cf should be dict instead of tuple. Keys = species. Make
    # new dict for state from these keys using dict.fromkeys constructor.
    stoic_cf : dict[Chemical,float]
    heat_of_rxn : float     # Heat of reaction (MJ/kmol)
    arrhenius_coeff : float = 0.1
    activation_energy : float = 0.1
    
    def rate_const(self, temp)->float:
        return self.arrhenius_coeff * math.exp(-self.activation_energy/Univ_Gas_Const*temp)

    def __post_init__(self):
        """Extract the Chemical objects into species list."""
        self.species= [key for key,value in self.stoic_cf.items()]


@dataclass
class ProcessSimulationConfig:
    """Class to summarize process simulation configuration in terms of solver,
    reactor, and reaction."""
    solver : ReactorFDMSolver
    reactor : Reactor
    reaction : Reaction

    def __post_init__(self) -> None:
        """Calculate the element volume to use in respective concentration & 
        temperature profile calculation functions as soon as configuration is 
        instantiated."""
        self.element_vol = self.solver.length_step * self.reactor.cross_section_area

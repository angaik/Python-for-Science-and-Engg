from dataclasses import dataclass
import math

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
    cross_section_area : float = 0.1
    length : float = 1

@dataclass
class Reaction:
    """Class to store details of reaction kinetics, like rate equations"""
    
    # class Reaction should be composed of species & corresponding stoichiometric cf
    # too. Reaction.stoic_cf should be dict instead of tuple. Keys = species. Make
    # new dict for state from these keys using dict.fromkeys constructor.
    stoic_cf : dict[str,float]
    
    arrhenius_coeff : float = 0.1
    activation_energy : float = 0.1
    
    def rate_const(self, temp):
        return self.arrhenius_coeff * math.exp(-self.activation_energy/Univ_Gas_Const*temp)
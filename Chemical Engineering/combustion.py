# calculate combustion product composition according to given input chemical composition and air/oxygen input

import numpy as np
import chemCalc


LHV={'Carbon monoxide':10.1,'Methane':50,'Hydrogen':120} # LHV in MJ/kg
MW=np.array([28,44,2,32,28,16])   # MW in kg/kmol according to order of inlet_components list.
tot_kmol=47    # kmol

# Inlet composition in mol fraction (0-100%)
inlet_components=['Carbon monoxide','Carbon dioxide','Hydrogen','Oxygen','Nitrogen','Methane']
inlet_molFrac=np.array([38,10,40,4,4,4])
inlet_moleFlow=np.zeros(np.size(inlet_molFrac))
inlet_massFlow=np.zeros(np.size(inlet_molFrac))
# Form inlet streams as dict via dict comprehension
if abs(sum(inlet_molFrac)-100) < 5: # flows listed till 95% mol-fraction
    
    # Flow in kg
    inlet_moleFlow=[inlet_molFrac[i]*tot_kmol/100 for i in range(np.size(inlet_components))]
    inlet_massFlow=inlet_moleFlow*MW    # kg

# Emissions calculation

CO_emissions=chemCalc.combust(inlet_components[0],inlet_massFlow[0],oxyfuel=True)
print(f"Combustion of {inlet_components[0]} in inlet fuel causes {CO_emissions[0]:.2f} kg CO2 emissions.")

# Oxygen trial
chemCalc.combust(inlet_components[3],inlet_massFlow[3],oxyfuel=False)

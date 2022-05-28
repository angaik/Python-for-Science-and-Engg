
P_norm = 101.325   # kPa
R = 8.314     # kJ/kmol-K
T_norm = 273.15    # K


def norm_Density(MW: float) -> float:
    """Function to calculate density at normal conditions (101.325 kPa & 273.15 K) in kg/Nm3, given molecular weight in (g/mol) or (kg/kmol)."""
    kg_per_Nm3 = P_norm*MW/(R*T_norm)
    return kg_per_Nm3


def combust(compound: str, kg, oxyfuel=False):
    """Returns three values: CO2, H2O & N2 emissions in kg respectively. 100% combustion efficiency assumed."""
    
    # If fuel compound has x carbon atoms, y hydrogen atoms & z oxygen atoms in molecule
    # (kg_emissions/kg_fuel) are given by following three lambda functions i.e. equations
    def sp_kgCO2(x, y, z): return (44*x)/((12*x)+y+(16*z))
    def sp_kgH2O(x, y, z): return (9*y)/((12*x)+y+(16*z))
    if oxyfuel == False:
        def sp_kgN2(x, y, z): return 4*3.729*((4*x)+y-(2*z))/((12*x)+y+(16*z))
    elif oxyfuel != False:
        def sp_kgN2(x, y, z): return 0
    
    if compound.casefold() == "methane":
        kg_CO2_emit = kg*sp_kgCO2(1, 4, 0)
        kg_H2O_emit = kg*sp_kgH2O(1, 4, 0)
        kg_N2_emit = kg*sp_kgN2(1, 4, 0)
    elif compound.casefold()=="carbon monoxide":
        kg_CO2_emit = kg*sp_kgCO2(1, 0, 1)
        kg_H2O_emit = kg*sp_kgH2O(1, 0, 1)
        kg_N2_emit = kg*sp_kgN2(1, 0, 1)
    elif compound.casefold()=="hydrogen":
        kg_CO2_emit = kg*sp_kgCO2(0, 2, 0)
        kg_H2O_emit = kg*sp_kgH2O(0, 2, 0)
        kg_N2_emit = kg*sp_kgN2(0, 2, 0)
    else:
        print(f"The compound {compound} is not combustible.")
        kg_CO2_emit=0
        kg_H2O_emit=0
        kg_N2_emit=0
    
    if [kg_CO2_emit,kg_H2O_emit,kg_N2_emit]==[0,0,0]:
        return None
    else:
        return kg_CO2_emit, kg_H2O_emit, kg_N2_emit

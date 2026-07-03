from pfr_utils import *
import math

def calc_steady_profile(config:ProcessSimulationConfig,entry_mol:list,
    axial_vel:float,
    )->dict[str,dict[float,float]]:    
    
    moles_A = {0.00:entry_mol[0]} # Keys will be z-co-ordinate
    moles_B = {0.00:entry_mol[1]}
    moles_C = {0.00:entry_mol[2]}
    moles_D = {0.00:entry_mol[3]}
    Temp_kelvin = {0.00:900}

    if config.reactor.cooling is True:
        rate_const_entry = config.reaction.rate_const(Temp_kelvin[list(Temp_kelvin.keys())[0]])

    # For 10 nodes
    for i in range(10):
        z_coord = float(f"{(i*config.solver.length_step):.2f}")
        z_next = float(f"{(z_coord + config.solver.length_step):.2f}")
        
        # Calculate rate of reaction in this element w.r.t. A using temperature at 
        # entry of elemental volume
        if config.reactor.cooling is False:
            rate_A = config.reaction.rate_const(Temp_kelvin[z_coord]) * \
                (moles_A[z_coord] ** abs(config.reaction.stoic_cf[config.reaction.species[0]]))
        else:
            rate_A = rate_const_entry * (moles_A[z_coord] ** \
                                          abs(config.reaction.stoic_cf[config.reaction.species[0]]))
        
        # Calculate concentration to check for limiting reactant
        moles_reacted_A = (rate_A * (config.solver.length_step ** 2)/(axial_vel))
        next_moles_A = moles_A[z_coord] - moles_reacted_A

        next_moles_B = moles_B[z_coord] - \
                        (config.reaction.stoic_cf[config.reaction.species[1]]/\
                         config.reaction.stoic_cf[config.reaction.species[0]]) * moles_reacted_A
        
        next_moles_C = moles_C[z_coord] - \
                        (config.reaction.stoic_cf[config.reaction.species[2]]/\
                         config.reaction.stoic_cf[config.reaction.species[0]]) * moles_reacted_A
        
        next_moles_D = moles_D[z_coord] - \
                        (config.reaction.stoic_cf[config.reaction.species[3]]/\
                         config.reaction.stoic_cf[config.reaction.species[0]]) * moles_reacted_A

        # Check for limiting reactant. Only proceed if no concentration is equal to 0
        if next_moles_A > 0 and next_moles_B > 0:
            # Calculate moles for next node
            moles_A[z_next] = next_moles_A
            moles_B[z_next] = next_moles_B
            moles_C[z_next] = next_moles_C
            moles_D[z_next] = next_moles_D

            # Calculate temperature for next node & cooling duty as per settings of reactor cooling
            if config.reactor.cooling is False:
                
                # Calculate density & specific heat capacity
                moles_state = [
                    moles_A[z_coord],moles_B[z_coord],
                    moles_C[z_coord],moles_D[z_coord]
                    ]
                element_mass = sum([a*b 
                                    for a,b in zip(
                                        moles_state,[specie.mol_wt 
                                        for specie in config.reaction.species])
                                    ])
                element_sp_heat_cap = sum([
                    a*b*c*1e-3 
                    for a,b,c in zip(moles_state,
                                     [specie.sp_heat_cap 
                                        for specie in config.reaction.species],
                                     [specie.mol_wt 
                                        for specie in config.reaction.species])
                    ])/config.element_vol
                
                # Calculate temperature for next node
                Temp_kelvin[z_next] = Temp_kelvin[z_coord] + (moles_reacted_A*config.reaction.heat_of_rxn/\
                                                        (element_mass*element_sp_heat_cap))
                
            else:
                cooling_duty_kJ += moles_reacted_A*config.reaction.heat_of_rxn
                Temp_kelvin[z_next] = Temp_kelvin[z_coord]
        
        # Else if some concentration is zero
        else:
            # Determine moles and temperature for next node, as being the same as current node
            moles_A[z_next] = moles_A[z_coord]
            moles_B[z_next] = moles_B[z_coord]
            moles_C[z_next] = moles_C[z_coord]
            moles_D[z_next] = moles_D[z_coord]
            Temp_kelvin[z_next] = Temp_kelvin[z_coord]

    return {**dict.fromkeys([key.name for key in config.reaction.stoic_cf.keys()],
                            [moles_A,moles_B,moles_C,moles_D]),
                "Temperature (K)":Temp_kelvin}

def calc_transient_profile(config:ProcessSimulationConfig,time_pts:list
                           )->dict[str,dict[str,float]]:
    """Calculate transient concentrations and temperature profile for PFR.
    
    Returns:
    ------
        dict[str,dict[str,float]] : level 0 key ~ time point. level 1 key ~ 
        node location."""
    
    # Define state variables: n_i, T
    state = {}
    
    # 1st for-loop for all time-points
    for t in time_pts:
        # Inner for-loop for all nodes/positions
        for i in range(10):
            # Determine species moles at entry of element
            entry_moles = [4,5,0,0.1]   # TODO: Should this be dynamic?
            axial_vel = {t:1.2 + 0.4*math.sin(2*t) for t in time_pts}
            state[t] =calc_steady_profile(entry_moles,axial_vel)

            # # TODO: Core equation for transient energy balance
            # -config.reactor.cooling_duty_kJ - shaft_work = sum([
            #     specie[z_coord] * sp_heat_cap[idx] * \
            #         ((Temp_kelvin[t][z_coord]-\
            #             Temp_kelvin[t-config.solver.time_step][[z_coord]])/\
            #             config.solver.time_step)
            #     for idx, specie in enumerate(config.reaction.stoic_cf.keys())
            #     ], rate_A * config.element_vol * config.reaction.heat_of_rxn)
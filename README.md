# GaussianPlume
Combined with the assumption made, Gaussian Plume Model for the Nord Stream explosion is built. All the functions are packaged in a typical file. Different options for simulation is set:
1. For the plot view, we have four different choices, PLAN VIEW, HEIGHT SLICE, SURFACE TIME and NO PLOT. It will help us to compare with the satellite image in different aspect and study the environmental influence.
2. For the incoming wind, we have CONSTANT WIND which means the direction is horizontal to the sea surface and speed is a constant. The FLUCTUATING WIND corresponded to the sinuous wind propagation. The PREVAILING WIND is also simulated as its common around the sea. 
3. The leakage points according to the news are three, so the number of stacks can be set from one to three.
4. The stability of the atmosphere has two choice, the constant stability and annual cycle which means in a cycle the stability is varying from very unstable to stable by the time.
5. The aerosol properties of contaminants is the setting of methane physical and chemical properties as to study the buoyancy effect. The dry plume will then humidify as the leakage is from the sea surface, so the humidify condition are supposed to set.
6. The buoyancy of the methane is considered, as the methane is lighter than the air after humidifying. Four parameters will influence the buoyancy of the methane propagation, which are: amount of substance, density, atomic weight, and molecular weight.
7. The resolution, study time span and model size and all the variable in the Gaussian Plume model are then set in the configuration part.

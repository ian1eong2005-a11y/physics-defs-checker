"""Definitions: Kinetic particle model, Thermal processes, Internal energy, Thermal properties of matter (6091)."""
from ..marker import Pitfall, Point
from .base import BOTH, PURE, definition

P, PF = Point, Pitfall

# ================================================================= 7  Kinetic particle model
definition("d_kpm_solid", "kpm", 2, "7b",
           stem="Describe the arrangement, motion and forces between the particles in a **solid**.",
           points=[P("closely packed in a regular (orderly) arrangement", ["closely packed", "close together", "tightly packed", "regular", "orderly", "fixed pattern", "lattice"]),
                   P("vibrate about fixed positions", ["vibrate about fixed positions", "vibrate about their fixed positions", "vibrate in fixed positions", "vibrate about a fixed point", "vibrate about fixed points", "vibrate in place", "vibrate only"]),
                   P("strong forces of attraction between particles", ["strong forces", "strong attractive forces", "strong attraction", "strong intermolecular", "held strongly"])],
           pitfalls=[PF(["do not move", "particles are stationary", "not moving"], "Particles in a solid still VIBRATE about fixed positions; they are never stationary (above absolute zero).")],
           model_answer="In a solid the particles are closely packed in a regular arrangement, vibrate about fixed positions, and are held by strong forces of attraction.",
           hints=["Three things: arrangement, motion, forces.", "Can the particles move from place to place, or only vibrate?", "How strong are the forces holding them?"],
           keywords="closely packed, regular; vibrate about fixed positions; strong forces",
           sample_pass=["closely packed in a regular pattern, vibrating about fixed positions, with strong forces of attraction", "tightly packed and orderly; particles vibrate in place; strong attractive forces"],
           sample_fail=["the particles do not move and are far apart", "the particles slide past each other"])

definition("d_kpm_liquid", "kpm", 2, "7b",
           stem="Describe the arrangement, motion and forces between the particles in a **liquid**.",
           points=[P("close together but in a random (irregular) arrangement", ["close together", "closely packed", "random", "irregular", "disorderly", "no fixed pattern"]),
                   P("free to move / slide past one another throughout the liquid", ["slide past", "move past", "free to move", "move about", "move around", "flow", "not fixed"]),
                   P("forces of attraction weaker than in a solid (but still significant)", ["weaker forces", "weaker attraction", "less strong", "weaker than in a solid", "moderate forces", "fairly strong"])],
           model_answer="In a liquid the particles are close together but randomly arranged; they are free to move and slide past one another; the forces of attraction are weaker than in a solid.",
           hints=["Compare with a solid: what changes in arrangement, motion and forces?", "Are the particles still touching? Are they in a pattern?", "Can they change places?"],
           keywords="close, random; slide past each other; weaker forces",
           sample_pass=["close together but randomly arranged, sliding past each other, with weaker forces than in a solid", "particles are closely packed but irregular and free to move about; attraction is less strong"],
           sample_fail=["far apart and moving fast with no forces", "regular arrangement vibrating about fixed positions"])

definition("d_kpm_gas", "kpm", 2, "7b",
           stem="Describe the arrangement, motion and forces between the particles in a **gas**.",
           points=[P("far apart, random arrangement (occupy the whole container)", ["far apart", "very far apart", "widely spaced", "large distances", "spread out", "fill the container"]),
                   P("move freely, rapidly and randomly in all directions", ["move freely", "move rapidly", "move randomly", "moving freely", "moving rapidly", "moving randomly", "random motion", "high speed", "fast", "rapidly", "randomly", "quickly", "freely", "all directions"]),
                   P("negligible (very weak) forces of attraction", ["negligible", "very weak", "almost no", "hardly any", "no forces", "no attraction"])],
           model_answer="In a gas the particles are far apart in a random arrangement, move freely and rapidly in random directions, and the forces of attraction between them are negligible.",
           hints=["Think about why a gas fills its container.", "How far apart, how fast, how strong are the forces?", "Give all three features."],
           keywords="far apart; rapid random motion; negligible forces",
           sample_pass=["far apart, moving rapidly and randomly, with negligible forces between them", "widely spaced particles in random fast motion and almost no attraction"],
           sample_fail=["close together vibrating about fixed positions", "particles slide over each other with strong forces"])

definition("d_kpm_temperature_ke", "kpm", 2, "7c",
           stem="State how the temperature of a body is related to the motion of its particles.",
           points=[P("a rise in temperature means an increase in the average kinetic energy of the particles", ["average kinetic energy", "mean kinetic energy", "average speed", "average ke"]),
                   P("higher temperature: particles move / vibrate faster", ["increase", "higher", "faster", "more vigorously", "greater", "rises"])],
           pitfalls=[PF(["total kinetic energy", "total energy of the particles"], "Temperature is a measure of the AVERAGE kinetic energy per particle, not the total (total KE also depends on how many particles there are).")],
           model_answer="Temperature is a measure of the average kinetic energy of the particles: a rise in temperature means the particles move (or vibrate) faster, so their average kinetic energy increases.",
           hints=["Hotter particles move faster.", "Which kind of kinetic energy: total or average?", "Link 'temperature rises' to 'kinetic energy ... increases'."],
           keywords="average kinetic energy of particles increases",
           sample_pass=["higher temperature means the particles have greater average kinetic energy", "when temperature rises the average KE of the particles increases"], sample_fail=["the total kinetic energy increases", "hot things have more heat"])

definition("d_kpm_brownian", "kpm", 3, "7c",
           stem="In a Brownian motion experiment, smoke particles in air are seen to move randomly. Explain what this shows.", syllabi=PURE,
           points=[P("the smoke particles are bombarded unevenly / continuously by air molecules", ["bombarded", "hit by air molecules", "collide with the smoke", "collisions with air molecules", "struck by air molecules", "uneven bombardment", "unequal bombardment"]),
                   P("the air molecules are too small to be seen, moving fast and randomly", ["too small to be seen", "invisible", "cannot be seen", "random motion", "moving randomly", "fast moving", "random directions"]),
                   P("evidence that molecules in a gas (or liquid) are in constant random motion", ["evidence", "shows that", "proves", "constant random motion", "continuous random motion", "molecules are in random motion"])],
           min_points=2,
           pitfalls=[PF(["smoke particles are the molecules", "we see the air molecules"], "The air molecules are too small to see. The visible smoke particles jiggle because the invisible air molecules hit them unevenly.")],
           model_answer="The smoke particles are being bombarded unevenly from all sides by fast-moving air molecules that are too small to be seen. The random jerky motion of the smoke is evidence that the air molecules are in continuous random motion.",
           hints=["Why would a large smoke particle suddenly change direction?", "Something invisible is hitting it.", "What does the randomness tell you about the motion of air molecules?"],
           keywords="uneven bombardment by invisible air molecules; evidence of random molecular motion",
           sample_pass=["The smoke particles are hit unevenly by invisible air molecules, showing the molecules move randomly", "evidence that air molecules are in constant random motion, as they bombard the smoke particles"],
           sample_fail=["the smoke is moved by convection currents", "the smoke particles are too hot"])

definition("d_kpm_gas_pressure", "kpm", 3, "7e",
           stem="Explain, in terms of particles, how a gas exerts a pressure on the walls of its container.", syllabi=PURE,
           points=[P("gas particles move randomly and collide with the walls", ["collide with the walls", "hit the walls", "bombard the walls", "strike the walls", "collisions with the walls", "collide with the container"]),
                   P("each collision exerts a force on the wall (change in momentum); the total force per unit area is the pressure", ["force on the wall", "exert a force", "force per unit area", "change in momentum", "many collisions per second", "total force"])],
           pitfalls=[PF(["particles push each other", "particles repel"], "Gas pressure comes from particles hitting the WALLS, not from particles pushing one another.")],
           model_answer="The gas particles move randomly at high speed and continually collide with the walls of the container. Each collision exerts a small force on the wall; the total force from the very many collisions, acting per unit area of the wall, is the gas pressure.",
           hints=["What are the particles doing all the time?", "What do they hit?", "Force per unit area is ...?"],
           keywords="particles collide with walls; force per unit area",
           sample_pass=["particles collide with the walls, exerting a force; force per unit area is pressure", "the molecules bombard the container walls and each collision exerts a force on the wall"],
           sample_fail=["the gas is squeezed so it pushes out", "the particles push against each other"])

# ================================================================= 8  Thermal processes
definition("d_tp_direction", "thermal_proc", 1, "8a",
           stem="State the direction in which thermal energy is transferred between two bodies in contact, and when the transfer stops.",
           points=[P("from the region/body at higher temperature to the one at lower temperature", ["higher temperature to lower temperature", "higher temperature to a region of lower", "hotter to colder", "hot to cold", "hotter body to the colder", "high temperature to low temperature", "from the hotter", "hotter object to the cooler"]),
                   P("until thermal equilibrium (same temperature) is reached", ["thermal equilibrium", "same temperature", "equal temperature", "temperatures are equal", "no temperature difference"])],
           pitfalls=[PF(["cold to hot", "colder to hotter", "lower temperature to higher"], "Wrong way round: energy flows from HOT to COLD.")],
           model_answer="Thermal energy is transferred from the body at the higher temperature to the body at the lower temperature, until both reach the same temperature (thermal equilibrium).",
           hints=["Think of a hot spoon in cold water.", "Which way does the energy go?", "When does the net transfer stop?"],
           keywords="hot to cold; until thermal equilibrium",
           sample_pass=["from the hotter body to the colder body until they reach thermal equilibrium", "from higher temperature to lower temperature until the temperatures are equal"], sample_fail=["from cold to hot until equal", "heat spreads out"])

definition("d_tp_equilibrium", "thermal_proc", 2, "8a",
           stem="State what is meant by **thermal equilibrium**.",
           points=[P("two bodies are at the same temperature", ["same temperature", "equal temperature", "temperatures are equal", "no temperature difference"]),
                   P("so there is no net transfer of thermal energy between them", ["no net transfer", "no net flow", "no net heat", "no overall transfer", "no further transfer", "no more net"])],
           model_answer="Two bodies are in thermal equilibrium when they are at the same temperature, so there is no net transfer of thermal energy between them.",
           hints=["It happens after a hot and a cold body have been in contact for a while.", "Compare their temperatures.", "What then happens to the net energy transfer?"],
           keywords="same temperature; no net transfer of thermal energy",
           sample_pass=["the two bodies are at the same temperature so there is no net transfer of thermal energy", "equal temperatures, no net flow of heat"], sample_fail=["the bodies are both hot", "heat moves from hot to cold"])

definition("d_tp_conduction", "thermal_proc", 3, "8b",
           stem="Describe, in terms of particles, how thermal **conduction** occurs in a solid, and why metals conduct better than non-metals.",
           points=[P("particles at the hot end vibrate more vigorously and pass energy to neighbouring particles by collision", ["vibrate more vigorously", "vibrate faster", "vibrate with larger amplitude", "pass energy to neighbouring", "collide with neighbouring", "transfer energy to the next", "neighbouring particles", "adjacent particles", "atomic vibration", "vibration of atoms", "vibrating atoms", "vibration of particles", "vibration of molecules", "vibrating particles", "energy by collision", "transfers energy by collision", "passed on by collisions", "collisions between particles"]),
                   P("in metals, free (delocalised) electrons also move and carry energy quickly through the metal", ["free electrons", "delocalised electrons", "mobile electrons", "electrons diffuse", "electrons carry", "movement of electrons"])],
           model_answer="Particles at the hot end gain energy and vibrate more vigorously; they collide with neighbouring particles and pass energy along the solid. In metals, free electrons also gain kinetic energy and move through the metal, transferring energy much faster, so metals are better conductors.",
           hints=["Start at the hot end: what do the particles there do?", "How does energy get to the next particle?", "What extra carriers do metals have?"],
           keywords="vibrating particles pass energy to neighbours; free electrons in metals",
           sample_pass=["atoms at the hot end vibrate more and pass energy to neighbouring atoms; in metals free electrons also carry the energy", "vibration of particles transfers energy by collision; metals have mobile electrons which diffuse and carry energy"],
           sample_fail=["heat travels through the metal because it is a conductor", "hot particles move to the cold end"])

definition("d_tp_convection", "thermal_proc", 3, "8c",
           stem="Describe, in terms of density changes, how **convection** occurs in a fluid heated from below.",
           points=[P("fluid near the heat source is heated and expands, so it becomes less dense", ["expands", "less dense", "lower density", "density decreases", "decrease in density"]),
                   P("the less dense fluid rises; cooler denser fluid sinks to take its place, forming a convection current", ["rises", "denser fluid sinks", "cooler fluid sinks", "sinks to replace", "convection current", "circulates", "takes its place"])],
           pitfalls=[PF(["heat rises", "hot air rises because heat rises"], "Heat does not 'rise'. The HOT FLUID rises because it has expanded and become LESS DENSE."),
                     PF(["particles become lighter", "molecules get lighter"], "The particles do not change mass. The fluid expands, so the same mass occupies more volume: lower DENSITY.")],
           model_answer="The fluid near the heat source is heated, expands and becomes less dense, so it rises. Cooler, denser fluid sinks to take its place and is heated in turn, setting up a convection current.",
           hints=["What happens to the volume of the heated fluid?", "Density = mass / volume: so what happens to its density?", "What does less dense fluid do, and what replaces it?"],
           keywords="expands, less dense, rises; cooler denser fluid sinks; convection current",
           sample_pass=["heated fluid expands and becomes less dense so it rises, while cooler denser fluid sinks to replace it", "the warm water has lower density and rises; cold water sinks, forming a convection current"],
           sample_fail=["heat rises to the top", "the particles become lighter and float up"])

definition("d_tp_radiation", "thermal_proc", 2, "8d",
           stem="State what is meant by thermal **radiation**, and state one way it differs from conduction and convection.",
           points=[P("transfer of thermal energy by electromagnetic waves (infrared)", ["electromagnetic waves", "infrared", "infra-red", "em waves", "electromagnetic radiation"]),
                   P("does not require a medium (can travel through a vacuum)", ["does not require a medium", "no medium", "without a medium", "through a vacuum", "through vacuum", "does not need a medium", "needs no medium", "even in a vacuum"])],
           model_answer="Thermal radiation is the transfer of thermal energy by electromagnetic (infrared) waves. Unlike conduction and convection it does not need a medium, so it can travel through a vacuum (e.g. from the Sun to the Earth).",
           hints=["How does energy from the Sun reach us?", "What kind of waves carry it?", "What does this method not need, that the other two do?"],
           keywords="infrared / electromagnetic waves; no medium needed",
           sample_pass=["transfer of energy by infrared waves, which needs no medium", "energy carried by electromagnetic waves; it can travel through a vacuum"], sample_fail=["heat moving through air currents", "transfer by vibrating particles"])

definition("d_tp_radiation_factors", "thermal_proc", 3, "8d",
           stem="State **three** factors that affect the rate at which a body emits (or absorbs) thermal radiation, and say how each affects it.",
           points=[P("surface colour and texture: dull black surfaces emit/absorb faster than shiny white/silver ones", ["colour", "black", "dull", "shiny", "silver", "white", "texture", "rough"]),
                   P("surface temperature: higher temperature (difference), faster rate", ["temperature", "hotter"]),
                   P("surface area: larger area, faster rate", ["surface area", "larger area", "bigger area", "area"])],
           model_answer="(1) Surface colour and texture: dull black surfaces emit and absorb radiation faster than shiny, white or silvery ones. (2) Surface temperature: the higher the temperature, the faster the rate of emission. (3) Surface area: the larger the area, the faster the rate.",
           hints=["Think about a car radiator, a black T-shirt and a hot kettle.", "Colour/texture, temperature and size.", "Give the factor and the direction of its effect."],
           keywords="colour/texture, temperature, surface area",
           sample_pass=["dull black surfaces radiate faster than shiny ones; higher temperature radiates faster; larger surface area radiates faster", "colour and texture, surface temperature and surface area"],
           sample_fail=["mass and volume", "the colour of the object"])

# ================================================================= 9 / 7  Internal energy, change of state
definition("d_int_internal_energy", "internal", 2, "7d",
           stem="Describe what is meant by the **internal energy** of a body.",
           points=[P("the total kinetic energy of the particles due to their random motion", ["total kinetic energy", "sum of the kinetic energy", "kinetic energy of the particles", "random motion"]),
                   P("plus the total potential energy between the particles", ["total potential energy", "sum of the potential energy", "potential energy between the particles", "potential energy of the particles", "potential energy due to the forces"])],
           pitfalls=[PF(["average kinetic energy"], "Internal energy is the TOTAL (sum of) kinetic and potential energies, not the average (that is temperature).")],
           model_answer="Internal energy is the total kinetic energy associated with the random motion of the particles plus the total potential energy between the particles in the body.",
           hints=["It is a sum of two kinds of energy of the particles.", "One is about their motion.", "The other is about the forces (bonds) between them."],
           keywords="total KE of random motion + total PE between particles",
           sample_pass=["the sum of the total kinetic energy of the random motion of the particles and the total potential energy between them", "total kinetic energy plus total potential energy of all the particles"],
           sample_fail=["the heat inside a body", "the average kinetic energy of the particles"])

definition("d_int_change_of_state", "internal", 4, "7e",
           stem="A solid is being melted. State what happens to its temperature while it melts, and explain in terms of the energy of the particles.",
           points=[P("temperature stays constant during melting", ["temperature stays constant", "temperature remains constant", "temperature does not change", "constant temperature", "no change in temperature", "temperature is constant", "temperature remains the same", "temperature stays the same"]),
                   P("the energy supplied is used to break/weaken the bonds between particles (increase potential energy), not to increase kinetic energy", ["break the bonds", "breaking bonds", "weaken the bonds", "overcome the forces", "overcome the attraction", "increase the potential energy", "potential energy increases", "not the kinetic energy", "kinetic energy does not increase", "not to increase the kinetic", "separate the particles", "loosen"])],
           pitfalls=[PF(["temperature increases", "temperature rises", "temperature continues to rise"], "During a change of state the temperature stays CONSTANT: the energy goes into potential energy (breaking bonds), not kinetic energy.")],
           model_answer="The temperature stays constant while the solid melts. The thermal energy supplied is used to break the bonds between the particles, increasing their potential energy; the average kinetic energy of the particles, and hence the temperature, does not change.",
           hints=["Look at the flat part of a heating curve.", "Energy is still being supplied: which energy of the particles increases, kinetic or potential?", "Temperature depends only on the average kinetic energy."],
           keywords="temperature constant; energy breaks bonds (PE up), KE unchanged",
           sample_pass=["The temperature remains constant because the energy supplied is used to break the bonds between particles, increasing potential energy rather than kinetic energy", "temperature does not change; energy goes to overcome the forces between particles, not to raise their kinetic energy"],
           sample_fail=["the temperature rises as it melts", "the temperature stays constant because no energy is supplied"])

# ================================================================= 9  Thermal properties (6091 only)
definition("d_thp_heat_capacity", "thermal_props", 2, "9b",
           stem="Define **heat capacity**.", syllabi=PURE,
           points=[P("the amount of thermal energy required to raise the temperature of a body", ["energy required to raise the temperature", "energy needed to raise the temperature", "thermal energy required to raise", "heat required to raise the temperature", "energy needed to increase the temperature", "energy required to increase the temperature", "energy per unit temperature rise", "energy per unit rise in temperature"]),
                   P("by 1 K (1 °C)", ["1 k", "1 °c", "one kelvin", "one degree", "1 degree", "unit temperature", "per kelvin", "per degree", "1°c", "1 c"])],
           pitfalls=[PF(["unit mass", "1 kg", "per kg", "per kilogram", "per unit mass"], "That is SPECIFIC heat capacity. Heat capacity is for the whole body, with no 'per unit mass'.")],
           model_answer="Heat capacity is the amount of thermal energy required to raise the temperature of a body by 1 K (or 1 °C); unit J/K.",
           hints=["It is an amount of energy.", "Energy needed to do what to the body?", "By how much?"],
           keywords="energy to raise temperature of the body by 1 K",
           sample_pass=["the thermal energy needed to raise the temperature of the body by 1 K", "energy required to increase the temperature of an object by one degree Celsius"], sample_fail=["the energy needed to raise 1 kg by 1 K", "how much heat a body can hold"])

definition("d_thp_shc", "thermal_props", 2, "9b",
           stem="Define **specific heat capacity**.", syllabi=PURE,
           points=[P("the amount of thermal energy required to raise the temperature", ["energy required to raise the temperature", "energy needed to raise the temperature", "thermal energy required to raise", "heat required to raise the temperature", "energy needed to increase the temperature", "energy required to increase the temperature", "energy required per unit temperature rise"]),
                   P("of unit mass (1 kg) of the substance", ["unit mass", "1 kg", "one kilogram", "per kg", "per kilogram", "per unit mass", "1 kilogram"]),
                   P("by 1 K (1 °C)", ["1 k", "1 °c", "one kelvin", "one degree", "1 degree", "unit temperature", "per kelvin", "per degree", "1°c", "1 c"])],
           pitfalls=[PF(["change its state", "change of state", "without a change in temperature"], "That is specific LATENT heat. Specific heat capacity is about raising the TEMPERATURE.")],
           model_answer="Specific heat capacity is the amount of thermal energy required to raise the temperature of unit mass (1 kg) of a substance by 1 K (or 1 °C); unit J/(kg K).",
           hints=["The unit J/(kg K) tells you the three parts.", "'Specific' means per unit mass.", "Energy ... per kg ... per K."],
           keywords="energy to raise temperature of 1 kg by 1 K",
           sample_pass=["the energy needed to raise the temperature of 1 kg of the substance by 1 K", "thermal energy required per unit mass per unit temperature rise"], sample_fail=["the energy needed to raise the temperature by 1 K", "energy to change the state of 1 kg without temperature change"])

definition("d_thp_latent_heat", "thermal_props", 2, "9f",
           stem="Define **latent heat**.", syllabi=PURE,
           points=[P("the thermal energy absorbed or released during a change of state", ["change of state", "change in state", "changes state", "change its state", "change of phase", "melting", "boiling"]),
                   P("without a change in temperature", ["without a change in temperature", "without any change in temperature", "at constant temperature", "temperature remains constant", "no change in temperature", "temperature stays the same", "without changing its temperature", "no temperature change"])],
           pitfalls=[PF(["raise the temperature", "increase the temperature"], "Latent heat does NOT change the temperature: it is the energy for a change of state at constant temperature.")],
           model_answer="Latent heat is the thermal energy absorbed or released when a substance changes state, without any change in temperature.",
           hints=["'Latent' means hidden: the thermometer does not show it.", "When is energy taken in without the temperature rising?", "Mention change of state and constant temperature."],
           keywords="energy for change of state at constant temperature",
           sample_pass=["energy absorbed or released during a change of state without a change in temperature", "the heat needed to change state at constant temperature"], sample_fail=["the heat needed to raise the temperature", "hidden heat"])

definition("d_thp_slh", "thermal_props", 3, "9f",
           stem="Define **specific latent heat**.", syllabi=PURE,
           points=[P("the thermal energy required to change the state", ["energy required to change the state", "energy needed to change the state", "energy required to change state", "heat required to change the state", "thermal energy needed to change", "energy to change the state", "energy absorbed or released when", "energy required to melt", "energy required to boil", "energy needed to convert"]),
                   P("of unit mass (1 kg) of the substance", ["unit mass", "1 kg", "one kilogram", "per kg", "per kilogram", "per unit mass", "1 kilogram"]),
                   P("without a change in temperature", ["without a change in temperature", "without any change in temperature", "at constant temperature", "temperature remains constant", "no change in temperature", "temperature stays the same", "without changing its temperature", "no temperature change"])],
           pitfalls=[PF(["raise the temperature", "increase the temperature", "by 1 k", "by 1 °c"], "That is specific HEAT CAPACITY. Specific latent heat is about changing STATE with no temperature change (examiner report 2021: many gave the wrong definition).")],
           model_answer="Specific latent heat is the thermal energy required to change the state of unit mass (1 kg) of a substance without a change in temperature; unit J/kg.",
           hints=["Three parts: energy to do what, for how much substance, with what happening to the temperature.", "'Specific' means per kg.", "No temperature change is part of the definition (examiners penalise leaving it out)."],
           keywords="energy to change state of 1 kg at constant temperature",
           sample_pass=["the energy required to change the state of 1 kg of a substance without a change in temperature", "thermal energy per unit mass needed to change state at constant temperature"],
           sample_fail=["the energy needed to raise the temperature of 1 kg by 1 K", "energy needed to change state"])

definition("d_thp_fusion_vaporisation", "thermal_props", 3, "9f",
           stem="Distinguish between the specific latent heat of **fusion** and the specific latent heat of **vaporisation**.", syllabi=PURE,
           points=[P("fusion: solid ↔ liquid (melting / solidifying) at the melting point", ["solid to liquid", "melt", "solid and liquid", "liquid to solid", "freez", "solidif", "melting point"]),
                   P("vaporisation: liquid ↔ gas (boiling / condensing) at the boiling point", ["liquid to gas", "boil", "liquid and gas", "gas to liquid", "condens", "vapour", "boiling point"])],
           model_answer="Specific latent heat of fusion is the energy per kg to change a substance between solid and liquid (melting or solidifying) at its melting point. Specific latent heat of vaporisation is the energy per kg to change it between liquid and gas (boiling or condensing) at its boiling point.",
           hints=["Fusion means melting.", "Vaporisation means turning into vapour (gas).", "Name the two states involved in each."],
           keywords="fusion: solid-liquid; vaporisation: liquid-gas",
           sample_pass=["fusion is for melting (solid to liquid) and vaporisation is for boiling (liquid to gas)", "fusion: solid and liquid at the melting point; vaporisation: liquid and gas at the boiling point"],
           sample_fail=["fusion is hotter than vaporisation", "fusion gives out heat and vaporisation takes in heat"])

definition("d_thp_boil_evap", "thermal_props", 5, "9e",
           stem="State **three** differences between boiling and evaporation.", syllabi=PURE,
           points=[P("boiling occurs at a fixed temperature (the boiling point); evaporation at any temperature", ["fixed temperature", "boiling point", "specific temperature", "any temperature", "all temperatures", "below the boiling point"]),
                   P("boiling occurs throughout the liquid; evaporation only at the surface", ["throughout the liquid", "whole liquid", "within the liquid", "surface"]),
                   P("boiling forms bubbles; evaporation does not", ["bubbles"]),
                   P("boiling is fast / needs a heat source; evaporation is slow / uses energy from surroundings (cooling)", ["fast", "quick", "rapid", "slow", "heat source", "energy from the surroundings", "cooling", "cools"])],
           min_points=3,
           model_answer="Boiling happens at one fixed temperature (the boiling point), throughout the liquid, with bubbles forming, and is rapid with a heat source. Evaporation happens at any temperature, only at the surface, without bubbles, and is slow, taking energy from the liquid and its surroundings (so it causes cooling).",
           hints=["Think: where in the liquid, at what temperature, how fast, bubbles or not.", "Only one of them happens at a single fixed temperature.", "Give three contrasts, each stated for both processes."],
           keywords="fixed vs any temperature; throughout vs surface; bubbles; fast vs slow",
           sample_pass=["Boiling occurs at a fixed temperature throughout the liquid with bubbles; evaporation occurs at any temperature at the surface only, with no bubbles", "boiling: at boiling point, whole liquid, fast; evaporation: any temperature, surface, slow"],
           sample_fail=["boiling is hotter than evaporation", "evaporation happens throughout the liquid at any temperature"])

"""Definitions: Static electricity, Current of electricity, D.C. circuits, Practical electricity."""
from ..marker import Pitfall, Point
from .base import BOTH, PURE, definition

P, PF = Point, Pitfall

# ================================================================= 13 / 12  Static electricity
definition("d_static_charges", "static", 1, "12a",
           stem="State the two types of electric charge, the unit of charge, and how charges interact.",
           points=[P("positive and negative", ["positive and negative", "positive or negative", "negative and positive"]),
                   P("measured in coulombs (C)", ["coulomb", " c "]),
                   P("like charges repel, unlike charges attract", ["like charges repel", "unlike charges attract", "same charges repel", "opposite charges attract", "like repel", "unlike attract", "opposite attract"])],
           min_points=2,
           pitfalls=[PF(["like charges attract", "unlike charges repel", "same charges attract"], "The other way round: LIKE charges REPEL, UNLIKE charges ATTRACT.")],
           model_answer="There are positive and negative charges, measured in coulombs (C). Like charges repel and unlike charges attract.",
           hints=["Two types of charge; one unit.", "What do two positives do to each other?", "Name the unit as well."],
           keywords="positive / negative; coulomb; like repel, unlike attract",
           sample_pass=["positive and negative, measured in coulombs; like charges repel and unlike charges attract", "charge is in coulombs; opposite charges attract, same charges repel"], sample_fail=["positive and negative charges attract each other", "charge is measured in amperes"])

definition("d_static_field", "static", 2, "13c",
           stem="State what is meant by an **electric field**.", syllabi=PURE,
           points=[P("a region (of space)", ["region", "space around", "area around"]),
                   P("in which an electric charge experiences a force", ["charge experiences a force", "charge experiences an electric force", "charged object experiences a force", "charge feels a force", "force acts on a charge", "charged particle experiences a force", "charge is acted on by a force", "charge would experience a force"])],
           pitfalls=[PF(["mass experiences a force"], "A MASS experiencing a force describes a gravitational field. In an electric field it is a CHARGE that experiences a force.")],
           model_answer="An electric field is a region in which an electric charge experiences a force.",
           hints=["Compare with the definition of a gravitational field.", "A field is a region.", "What kind of object feels a force in it?"],
           keywords="region; charge experiences a force",
           sample_pass=["a region in which an electric charge experiences a force", "the region around a charged object where another charge feels a force"], sample_fail=["the force between two charges", "a region where a mass experiences a force"])

definition("d_static_field_direction", "static", 2, "13d",
           stem="State how the direction of an electric field line is defined, and the direction of the field lines around a positive point charge.", syllabi=PURE,
           points=[P("direction of the force on a positive (test) charge placed at that point", ["force on a positive charge", "force on a positive test charge", "force acting on a positive", "positive test charge would move", "positive charge would move", "force on a small positive", "positive charge would be pushed", "positive charge would be forced", "positive charge is pushed"], ordered=True),
                   P("lines point radially outwards from a positive charge (and inwards towards a negative charge)", ["away from the positive", "outwards from the positive", "radially outwards", "out of the positive", "away from positive", "towards the negative", "into the negative", "point away"])],
           pitfalls=[PF(["force on a negative charge", "negative test charge", "negative charge moves", "negative charge would move", "direction a negative charge", "into the positive charge", "towards the positive charge", "towards a positive charge"], "Field direction is defined by the force on a POSITIVE test charge, so lines point AWAY from positive charges (SEAB 2017 report: 'not well known').")],
           model_answer="The direction of an electric field line is the direction of the force on a positive test charge placed at that point. Around an isolated positive point charge the field lines point radially outwards (and radially inwards towards a negative charge).",
           hints=["Imagine placing a tiny positive charge in the field.", "Which way is it pushed? That is the field direction.", "So around a positive charge the lines point ... ?"],
           keywords="force on a positive test charge; away from positive, towards negative",
           sample_pass=["the direction of the force on a positive test charge; lines point away from a positive charge", "field lines show where a positive charge would be pushed, so they point radially outwards from a positive charge"],
           sample_fail=["the direction a negative charge moves; lines point into the positive charge", "field lines go from negative to positive"])

definition("d_static_rubbing", "static", 2, "13f",
           stem="Explain how a polythene rod becomes negatively charged when rubbed with a cloth.", syllabi=PURE,
           points=[P("electrons are transferred (by friction) from the cloth to the rod", ["electrons are transferred", "transfer of electrons", "electrons move from the cloth", "electrons are rubbed off", "gains electrons", "electrons from the cloth to the rod", "receives electrons", "electrons move onto the rod"]),
                   P("the rod gains electrons so has excess negative charge; the cloth loses electrons and becomes positively charged", ["excess electrons", "more electrons than protons", "extra electrons", "cloth becomes positive", "cloth is positively charged", "cloth loses electrons", "cloth has lost electrons"])],
           pitfalls=[PF(["protons move", "protons are transferred", "positive charges move", "positive charge is transferred"], "Only ELECTRONS move when charging by rubbing. Protons are fixed in the nucleus."),
                     PF(["charge is created", "electrons are created", "friction creates charge"], "Charge is not created, only transferred: the rod gains the electrons that the cloth loses.")],
           model_answer="Rubbing transfers electrons from the cloth to the polythene rod. The rod now has more electrons than protons, so it has a net negative charge, while the cloth, having lost electrons, becomes positively charged.",
           hints=["Only one kind of particle can move between the rod and the cloth.", "Which way do they move if the rod ends up negative?", "What happens to the cloth?"],
           keywords="electrons transferred from cloth to rod; rod gains electrons (negative), cloth loses (positive)",
           sample_pass=["electrons are transferred from the cloth to the rod, so the rod has excess electrons and the cloth becomes positive", "friction moves electrons onto the rod which gains a negative charge; the cloth loses electrons"],
           sample_fail=["protons move from the rod to the cloth", "rubbing creates negative charge on the rod"])

definition("d_static_induction", "static", 4, "13g",
           stem="Describe how to charge a metal sphere (on an insulating stand) **positively by induction** using a negatively charged rod.", syllabi=PURE,
           points=[P("bring the negatively charged rod near the sphere (without touching): electrons in the sphere are repelled to the far side", ["bring the rod near", "near the sphere without touching", "close to the sphere", "electrons are repelled to the far side", "electrons move to the far", "electrons repelled away", "electrons move away from the rod", "do not touch"]),
                   P("earth the sphere (touch it with a finger / connect to earth) while the rod is still there: electrons flow from the sphere to earth", ["earth the sphere", "touch the sphere with a finger", "connect to earth", "earthing", "electrons flow to earth", "electrons leave the sphere", "electrons flow to the ground", "earth it"]),
                   P("remove the earth connection first, then the rod: the sphere is left with a net positive charge", ["remove the earth first", "remove the finger first", "remove the earth connection before", "remove the earthing", "then remove the rod", "rod is removed last", "remove the rod after", "finger removed before the rod", "finger away first", "take the finger away first", "take away the finger first", "remove your finger first", "earth connection is removed first"])],
           pitfalls=[PF(["touch the sphere with the rod", "rod touches the sphere"], "In induction the rod must NOT touch the sphere (that would charge it negatively by contact)."),
                     PF(["remove the rod first", "remove the rod then", "rod is removed first"], "Remove the EARTH connection first, then the rod; otherwise the electrons flow back and the sphere ends up uncharged.")],
           model_answer="Bring the negatively charged rod close to the sphere without touching it; free electrons in the sphere are repelled to the far side. While the rod is still in place, earth the sphere by touching it with a finger, so the repelled electrons flow to earth. Remove the finger first, then the rod: the sphere is left with a net positive charge, spread over its surface.",
           hints=["Three steps: bring near, earth, remove in the right order.", "Which way do the sphere's electrons move when the negative rod comes near?", "Earthing lets them escape; what must be removed first?"],
           keywords="rod near (no touching); electrons repelled; earth; remove earth then rod",
           sample_pass=["Bring the negative rod near without touching so electrons are repelled to the far side; earth the sphere with a finger so electrons flow to earth; remove the finger, then the rod", "hold the rod close, touch the sphere to earth it, take the finger away first and then the rod, leaving it positive"],
           sample_fail=["touch the sphere with the rod to give it charge", "bring the rod near, earth it, then remove the rod first and then the finger"])

# ================================================================= 14 / 12  Current of electricity
definition("d_cur_current", "current", 1, "12c",
           stem="Define **electric current**.",
           points=[P("rate of flow of (electric) charge", ["rate of flow of charge", "rate of flow of electric charge", "charge flowing per unit time", "charge per unit time", "charge passing a point per second", "charge flow per second", "amount of charge flowing per second", "charge passing per unit time", "charge divided by time", "charge / time", "flow of charge per unit time", "rate at which charge flows"])],
           pitfalls=[PF(["flow of electrons"], "'Flow of electrons' is not the definition: current is the RATE of flow of CHARGE (charge per unit time)."),
                     PF(["measured in coulombs", "unit is the coulomb", "unit coulomb"], "The coulomb is the unit of CHARGE. Current is measured in amperes (1 A = 1 C/s).")],
           model_answer="Electric current is the rate of flow of electric charge (I = Q/t); its unit is the ampere (A).",
           hints=["Current is a rate.", "The rate of flow of what quantity?", "Say 'rate of flow of ...'."],
           keywords="rate of flow of charge",
           sample_pass=["the rate of flow of charge, measured in amperes", "charge flowing per unit time, unit A"], sample_fail=["the flow of electrons", "the rate of flow of charge, measured in coulombs"])

definition("d_cur_conventional", "current", 2, "12d",
           stem="Distinguish between **conventional current** and **electron flow**.",
           points=[P("conventional current flows from the positive terminal to the negative terminal (direction a positive charge would move)", ["positive to negative", "positive terminal to the negative", "from positive to the negative", "from the positive terminal", "direction a positive charge would move", "from + to -", "from + to −"]),
                   P("electrons flow the opposite way, from negative to positive", ["negative to positive", "negative terminal to the positive", "from the negative terminal", "opposite direction", "opposite to conventional", "from - to +", "from − to +"])],
           pitfalls=[PF(["conventional current flows from negative to positive", "conventional current is from negative", "conventional current goes from the negative"], "Conventional current goes from POSITIVE to NEGATIVE. It is the electrons that go from negative to positive.")],
           model_answer="Conventional current is taken to flow from the positive terminal of the source, around the circuit, to the negative terminal (the direction positive charges would move). Electron flow is in the opposite direction, from the negative terminal to the positive terminal.",
           hints=["Two directions around the circuit.", "Conventional current was defined before electrons were discovered: it follows positive charge.", "Electrons are negative, so they go the other way."],
           keywords="conventional: + to −; electrons: − to +",
           sample_pass=["conventional current goes from positive to negative while electrons flow from negative to positive", "conventional current is the direction a positive charge would move, + to −; electron flow is the opposite direction"],
           sample_fail=["conventional current flows from negative to positive", "they are the same thing"])

definition("d_cur_emf", "current", 2, "14d",
           stem="Define the **electromotive force (e.m.f.)** of a source, and state its unit.",
           points=[P("the work done (energy transferred) by the source per unit charge", ["work done per unit charge", "work done by the source per unit charge", "energy transferred per unit charge", "energy per unit charge", "work done per coulomb", "energy per coulomb", "energy converted per unit charge", "work done per unit charge by the source", "energy supplied per unit charge", "work done in driving a unit charge", "work done on each coulomb", "energy given to each coulomb", "energy transferred to each coulomb", "energy supplied to each coulomb"]),
                   P("in driving charge around a complete circuit", ["around a complete circuit", "round a complete circuit", "around the whole circuit", "around the circuit", "round the circuit", "complete circuit", "through the complete circuit", "around a circuit", "round a circuit"]),
                   P("unit: volt (V)", ["volt", " v ", "j/c", "joules per coulomb"])],
           pitfalls=[PF(["is the force", "e.m.f. is a force", "force that drives", "force which drives", "force to drive", "force that pushes"], "E.m.f. is NOT a force despite its name (examiner report 2021). It is work done per unit charge, measured in volts."),
                     PF(["through a component", "across a component", "through the component", "through a resistor"], "Work done per unit charge driving charge THROUGH A COMPONENT is potential difference. E.m.f. is for the source driving charge round the COMPLETE circuit.")],
           model_answer="The e.m.f. of a source is the work done by the source per unit charge in driving charge around a complete circuit; it is measured in volts (1 V = 1 J/C).",
           hints=["Despite the name it is not a force. It is about energy.", "Energy (work done) per unit of what?", "Who does the work, and over what path: through one component or around the whole circuit?"],
           keywords="work done by source per unit charge round a complete circuit; volt",
           sample_pass=["the work done by the source per unit charge in driving charge around a complete circuit, in volts", "energy transferred per coulomb by the source in moving charge round the whole circuit; unit V"],
           sample_fail=["the force that drives charge around the circuit", "the work done per unit charge in driving charge through a component"])

definition("d_cur_pd", "current", 2, "12g",
           stem="Define the **potential difference (p.d.)** across a component, and state its unit.",
           points=[P("the work done (energy transferred) per unit charge", ["work done per unit charge", "energy transferred per unit charge", "energy per unit charge", "work done per coulomb", "energy per coulomb", "energy converted per unit charge", "work done in driving a unit charge", "energy transferred by each coulomb", "energy converted by each coulomb", "work done by each coulomb", "energy converted per coulomb", "work done per unit charge in driving"]),
                   P("in driving charge through the component", ["through the component", "through a component", "through that component", "through the device", "through the resistor", "through the lamp", "across the component", "passing through the component"]),
                   P("unit: volt (V)", ["volt", " v ", "j/c", "joules per coulomb"])],
           pitfalls=[PF(["around a complete circuit", "round a complete circuit", "around the whole circuit", "around the circuit", "round the circuit"], "Driving charge around the COMPLETE circuit describes e.m.f. P.d. is for driving charge THROUGH A COMPONENT."),
                     PF(["is the force", "force that", "force which"], "P.d. is not a force: it is work done (energy) per unit charge.")],
           model_answer="The potential difference across a component is the work done per unit charge in driving charge through the component (energy transferred per coulomb); it is measured in volts (1 V = 1 J/C).",
           hints=["Like e.m.f., it is energy per unit charge, but for a different part of the circuit.", "Energy transferred per coulomb where?", "Give the unit."],
           keywords="work done per unit charge through the component; volt",
           sample_pass=["the work done per unit charge in driving charge through the component, in volts", "energy transferred per coulomb of charge passing through the component; unit V"],
           sample_fail=["the work done per unit charge in driving charge around a complete circuit", "the force pushing electrons through a resistor"])

definition("d_cur_resistance", "current", 1, "12h",
           stem="Define the **resistance** of a component, and state its unit.",
           points=[P("the ratio of the potential difference across it to the current through it (R = V/I)", ["ratio of the potential difference across it to the current", "potential difference divided by the current", "pd divided by current", "potential difference across it divided by the current through it", "voltage divided by current", "pd / current", "v / i", "v/i", "pd over current", "potential difference over current", "ratio of pd to current", "ratio of voltage to current", "ratio of potential difference to current", "ratio of the pd across", "pd across it to the current", "pd across the component to the current"]),
                   P("unit: ohm (Ω)", ["ohm", "ω"])],
           pitfalls=[PF(["current divided by", "current over the", "current / p.d.", "i / v", "i/v", "ratio of current to"], "Upside down: resistance = p.d. ÷ current."),
                     PF(["opposition to current", "how hard it is for current"], "'Opposition to current' is a description, not the definition. Define it as the ratio p.d./current, R = V/I.")],
           model_answer="The resistance of a component is the ratio of the potential difference across it to the current through it (R = V/I); its unit is the ohm (Ω).",
           hints=["It is a ratio of two electrical quantities.", "p.d. across the component and current through it: which is divided by which?", "Give the unit."],
           keywords="p.d. ÷ current; ohm",
           sample_pass=["the ratio of the p.d. across the component to the current through it, in ohms", "potential difference divided by current, unit Ω"], sample_fail=["how much a component opposes current", "the ratio of current to potential difference"])

definition("d_cur_resistance_factors", "current", 2, "12j",
           stem="State how the resistance of a wire depends on its **length** and on its **cross-sectional area**.",
           points=[P("resistance is directly proportional to length (longer wire, more resistance)", ["proportional to the length", "proportional to length", "increases with length", "longer wire has more resistance", "longer the wire the greater", "longer the wire the higher", "doubles when the length doubles", "directly proportional to its length", "longer wire higher resistance", "longer wire greater resistance"]),
                   P("resistance is inversely proportional to cross-sectional area (thicker wire, less resistance)", ["inversely proportional to the cross-sectional area", "inversely proportional to the area", "inversely proportional to cross sectional area", "decreases as the area increases", "thicker wire has less resistance", "thicker the wire the lower", "thicker the wire the smaller", "larger area lower resistance", "halves when the area doubles", "thicker wire lower resistance", "greater area smaller resistance", "bigger area less resistance"])],
           pitfalls=[PF(["proportional to the area", "increases with area", "thicker wire has more resistance"], "A thicker wire has LESS resistance: R is INVERSELY proportional to cross-sectional area.")],
           model_answer="Resistance is directly proportional to the length of the wire (R ∝ l) and inversely proportional to its cross-sectional area (R ∝ 1/A): a longer wire has more resistance, a thicker wire has less.",
           hints=["Two relationships, one for each quantity.", "Longer wire: more or less resistance? Is it proportional?", "Thicker wire: more or less? What kind of proportion?"],
           keywords="R ∝ length; R ∝ 1/area",
           sample_pass=["resistance is directly proportional to length and inversely proportional to cross-sectional area", "a longer wire has higher resistance, a thicker wire has lower resistance"],
           sample_fail=["resistance is proportional to length and area", "longer and thicker wires have more resistance"])

definition("d_cur_ohmic", "current", 3, "14k",
           stem="State what is meant by an **ohmic conductor**, and describe its I-V graph.", syllabi=PURE,
           points=[P("the current through it is directly proportional to the p.d. across it", ["current is directly proportional to the potential difference", "current is proportional to the p.d.", "current is directly proportional to the p.d.", "current proportional to voltage", "current is proportional to the potential difference", "i proportional to v", "i is directly proportional to v", "v proportional to i", "current directly proportional to the voltage"]),
                   P("provided the temperature (physical conditions) stays constant; resistance is constant", ["constant temperature", "temperature is constant", "temperature remains constant", "physical conditions are constant", "temperature does not change", "constant resistance", "resistance is constant", "resistance stays the same"]),
                   P("I-V graph: a straight line through the origin", ["straight line through the origin", "straight line passing through the origin", "linear through the origin", "straight line from the origin", "straight line graph through the origin"])],
           min_points=2,
           pitfalls=[PF(["curve", "curved"], "An ohmic conductor gives a STRAIGHT line through the origin, not a curve.")],
           model_answer="An ohmic conductor is one for which the current is directly proportional to the potential difference across it, provided the temperature (physical conditions) remains constant, so its resistance is constant. Its I-V graph is a straight line through the origin.",
           hints=["It obeys Ohm's law.", "How are I and V related, and under what condition?", "What shape is the graph of I against V?"],
           keywords="I ∝ V at constant temperature; straight line through origin",
           sample_pass=["current is directly proportional to p.d. at constant temperature; the graph is a straight line through the origin", "I proportional to V, constant resistance, straight line through the origin"],
           sample_fail=["a conductor with a curved I-V graph", "resistance increases with current"])

definition("d_cur_temperature_metal", "current", 3, "14j",
           stem="State and explain the effect of a temperature increase on the resistance of a metallic conductor.", syllabi=PURE,
           points=[P("resistance increases", ["resistance increases", "increases the resistance", "higher resistance", "greater resistance", "resistance rises", "resistance goes up", "more resistance", "goes up", "increases", "rises"]),
                   P("because the metal ions (atoms) vibrate more vigorously, so the free electrons collide with them more often, obstructing the flow", ["vibrate more", "vibrate faster", "vibrate with greater amplitude", "more collisions", "collide more", "more frequent collisions", "electrons collide", "obstruct", "impede", "hinder"])],
           pitfalls=[PF(["resistance decreases", "lower resistance", "resistance falls"], "For a METAL the resistance INCREASES with temperature. (It is the NTC thermistor, a semiconductor, whose resistance falls.)")],
           model_answer="The resistance of a metallic conductor increases as its temperature rises. The metal ions vibrate more vigorously, so the free electrons collide with them more frequently, which impedes the flow of charge.",
           hints=["A filament lamp gets hotter as the current rises: what happens to its resistance?", "Think about the metal ions and the free electrons.", "What do the vibrating ions do to the moving electrons?"],
           keywords="resistance increases; ions vibrate more, more electron collisions",
           sample_pass=["resistance increases because the metal ions vibrate more and the free electrons collide with them more often", "it goes up: atoms vibrate with larger amplitude so electrons are obstructed more"],
           sample_fail=["resistance decreases because the electrons move faster", "resistance stays the same"])

definition("d_cur_filament_diode", "current", 4, "14k",
           stem="Describe the I-V characteristic of (i) a filament lamp and (ii) a semiconductor diode.", syllabi=PURE,
           points=[P("filament lamp: curve that flattens (gradient decreases) as V increases, because the filament heats up and its resistance increases", ["gradient decreases", "curve flattens", "levels off", "curve becomes less steep", "bends towards the voltage axis", "resistance increases as it heats", "resistance increases with temperature", "resistance increases as the current", "not a straight line", "curved"]),
                   P("diode: conducts in one direction only (forward bias); negligible / zero current in reverse (very high resistance)", ["one direction only", "in one direction", "forward bias", "forward direction", "no current in reverse", "zero current when reversed", "negligible current in reverse", "very high resistance in reverse", "reverse bias", "does not conduct in the opposite"])],
           model_answer="(i) Filament lamp: the I-V graph is a curve whose gradient decreases as V increases (it bends towards the V axis), because the filament gets hotter and its resistance increases. (ii) Diode: current flows in one direction only (forward bias, after a small threshold); in the reverse direction the current is practically zero because the resistance is very high.",
           hints=["Neither is a straight line through the origin.", "The lamp heats up as current increases: what happens to its resistance and so to the gradient of the I-V graph?", "A diode is a one-way valve for current."],
           keywords="lamp: curve flattening, R rises with T; diode: one direction only",
           sample_pass=["lamp: the curve flattens because resistance increases as it gets hot; diode: conducts in one direction only, almost no current in reverse", "filament: gradient decreases as V rises; diode: current only in forward bias, high resistance in reverse"],
           sample_fail=["both are straight lines through the origin", "the lamp curve gets steeper and the diode conducts both ways"])

# ================================================================= 15 / 13  D.C. circuits
definition("d_dc_series_current", "dc", 1, "13b",
           stem="State the rule for the **current** in a series circuit.",
           points=[P("the current is the same at every point in a series circuit", ["same at every point", "same at all points", "same throughout", "same everywhere", "same through each component", "same through every component", "same in all parts", "current is the same", "does not change around", "equal at every point", "same current flows through"])],
           pitfalls=[PF(["current is shared", "current splits", "current is divided", "current gets used up", "current decreases"], "Current is NOT used up or shared in a series circuit: it is the same at every point.")],
           model_answer="In a series circuit the current is the same at every point (the same current flows through every component).",
           hints=["There is only one path for the charge.", "Can charge pile up or disappear anywhere along it?", "So what can you say about the current at different points?"],
           keywords="same at every point",
           sample_pass=["the current is the same at every point in the circuit", "the same current flows through each component"], sample_fail=["the current is shared between the components", "the current decreases after each resistor"])

definition("d_dc_series_pd", "dc", 1, "13c",
           stem="State the rule for the **potential differences** in a series circuit.",
           points=[P("the sum of the p.d.s across the components equals the p.d. across the whole circuit (the e.m.f. of the source)", ["sum of the potential differences", "sum of the p.d.", "sum of the pd", "p.d.s add up to", "potential differences add up", "add up to the e.m.f.", "add up to the supply", "equal to the p.d. across the whole circuit", "equal to the total p.d.", "total of the potential differences", "sum of the voltages", "voltages add up", "shared between the components", "p.d. is shared", "potential difference is shared", "divided between the components"])],
           pitfalls=[PF(["p.d. is the same across each", "same p.d. across every", "potential difference is the same"], "That is the PARALLEL rule. In series the p.d.s across the components ADD UP to the supply p.d.")],
           model_answer="In a series circuit the sum of the potential differences across the components is equal to the potential difference across the whole circuit (the e.m.f. of the source): the supply p.d. is shared between the components.",
           hints=["Energy per coulomb is given by the source and spent across the components.", "So how do the p.d.s across the components relate to the source p.d.?", "They add up to ..."],
           keywords="sum of p.d.s = p.d. across whole circuit",
           sample_pass=["the sum of the potential differences across the components equals the potential difference across the whole circuit", "the p.d.s across the components add up to the e.m.f."], sample_fail=["the p.d. is the same across every component", "the p.d. is the same at every point"])

definition("d_dc_parallel_current", "dc", 1, "13d",
           stem="State the rule for the **currents** in a parallel circuit.",
           points=[P("the sum of the currents in the separate branches equals the current from the source (the current entering the junction)", ["sum of the currents in the branches", "sum of the currents in the separate branches", "currents in the branches add up", "branch currents add up", "sum of the branch currents", "equal to the current from the source", "equals the main current", "equals the total current", "current splits between the branches", "current is shared between the branches", "current entering a junction equals the current leaving", "sum of currents entering", "currents add up to the"])],
           pitfalls=[PF(["current is the same in each branch", "same current in every branch", "current is the same at every point"], "In parallel the current SPLITS: the branch currents ADD UP to the source current (they are equal only if the branches have equal resistance).")],
           model_answer="In a parallel circuit the sum of the currents in the separate branches is equal to the current from the source (the current entering a junction equals the total current leaving it).",
           hints=["At a junction the charge has a choice of paths.", "Charge is not lost at a junction.", "So how do the branch currents relate to the current from the source?"],
           keywords="sum of branch currents = current from source",
           sample_pass=["the sum of the currents in the branches equals the current from the source", "the current splits at the junction and the branch currents add up to the main current"], sample_fail=["the current is the same in each branch", "the current is used up in the branches"])

definition("d_dc_parallel_pd", "dc", 1, "13e",
           stem="State the rule for the **potential difference** across branches in a parallel circuit.",
           points=[P("the p.d. across each (separate) branch is the same", ["same across each branch", "same across every branch", "same across all the branches", "same across the branches", "same for each branch", "same across each component", "p.d. across the branches is the same", "equal across each branch", "equal across all branches", "same potential difference across", "same voltage across each", "same p.d. across", "same pd across"])],
           pitfalls=[PF(["p.d.s add up", "sum of the p.d.", "potential differences add up", "shared between the branches"], "That is the SERIES rule. In parallel each branch has the SAME p.d. across it.")],
           model_answer="In a parallel circuit the potential difference across each separate branch is the same (and equal to the p.d. across the whole parallel combination).",
           hints=["Each branch is connected across the same two points.", "So what can you say about the p.d. across each branch?", "Same, or shared?"],
           keywords="same p.d. across each branch",
           sample_pass=["the potential difference across each branch is the same", "every branch has the same p.d. across it"], sample_fail=["the p.d.s across the branches add up to the e.m.f.", "the p.d. is shared between the branches"])

definition("d_dc_potential_divider", "dc", 3, "15h",
           stem="Describe the action of a **potential divider**.", syllabi=PURE,
           points=[P("two (or more) resistors in series across a supply share the supply p.d.", ["resistors in series", "two resistors connected in series", "in series across the supply", "share the p.d.", "share the potential difference", "divides the p.d.", "divides the voltage", "splits the voltage", "shares the supply voltage", "divide the supply"]),
                   P("in the ratio of their resistances (larger resistance takes a larger share of the p.d.)", ["ratio of their resistances", "proportional to the resistance", "in proportion to their resistance", "larger resistance has a larger p.d.", "bigger resistance gets a bigger share", "larger resistance larger voltage", "according to their resistance", "greater resistance greater p.d.", "ratio of the resistances", "larger share of the p.d."]),
                   P("so the output p.d. taken across one resistor can be set to a fraction of the supply (variable output with a variable resistor / slider)", ["output", "fraction of the supply", "part of the supply", "varies the p.d.", "variable p.d.", "adjust the voltage", "slider", "sliding contact", "wiper", "potentiometer"])],
           min_points=2,
           model_answer="A potential divider is two resistors (or a resistance wire with a sliding contact) connected in series across a supply. The supply p.d. is shared between them in the ratio of their resistances, so the p.d. taken across one of them is a fraction of the supply p.d.; changing the resistance ratio (e.g. moving the slider) changes the output p.d.",
           hints=["Series resistors share the supply p.d.", "How is the share decided?", "Where is the output taken, and how is it varied?"],
           keywords="series resistors share V in ratio of R; output across one resistor; variable",
           sample_pass=["two resistors in series share the supply p.d. in the ratio of their resistances, so the output across one of them is a fraction of the supply", "a resistor chain divides the voltage in proportion to resistance; moving the slider varies the output p.d."],
           sample_fail=["it divides the current between two branches", "a device that doubles the voltage"])

definition("d_dc_thermistor", "dc", 2, "15i",
           stem="State how the resistance of an **NTC thermistor** changes with temperature.", syllabi=PURE,
           points=[P("resistance decreases as temperature increases (negative temperature coefficient)", ["resistance decreases as the temperature increases", "resistance decreases when the temperature rises", "resistance falls as temperature rises", "higher temperature lower resistance", "resistance decreases with increasing temperature", "resistance drops when heated", "resistance decreases when heated", "hotter lower resistance", "resistance decreases as it gets hotter", "resistance goes down as temperature goes up", "temperature increases the resistance decreases", "resistance falls", "resistance decreases", "resistance drops", "resistance goes down", "resistance is lower", "lower resistance"])],
           pitfalls=[PF(["resistance increases as the temperature increases", "resistance increases when heated", "higher temperature higher resistance", "resistance increases", "resistance rises", "resistance goes up"], "An NTC thermistor's resistance DECREASES as temperature rises (negative temperature coefficient). It is a metal wire whose resistance increases.")],
           model_answer="The resistance of an NTC (negative temperature coefficient) thermistor decreases as its temperature increases.",
           hints=["NTC stands for negative temperature coefficient.", "'Negative' tells you the direction of the change.", "Heat it up: resistance goes ... ?"],
           keywords="resistance decreases as temperature rises",
           sample_pass=["its resistance decreases as the temperature increases", "when it gets hotter, the resistance falls"], sample_fail=["its resistance increases as the temperature increases", "its resistance does not change"])

definition("d_dc_ldr", "dc", 2, "15i",
           stem="State how the resistance of a **light-dependent resistor (LDR)** changes with light intensity.", syllabi=PURE,
           points=[P("resistance decreases as light intensity increases (high in the dark, low in bright light)", ["resistance decreases as the light intensity increases", "resistance decreases when light intensity increases", "resistance falls as it gets brighter", "brighter light lower resistance", "resistance decreases in bright light", "high resistance in the dark", "resistance is high in darkness", "low resistance in bright light", "resistance drops in the light", "more light less resistance", "resistance goes down as light increases", "light intensity increases the resistance decreases"])],
           pitfalls=[PF(["resistance increases as the light intensity increases", "resistance increases in bright light", "brighter light higher resistance"], "The other way: an LDR's resistance DECREASES in bright light and is high in the dark.")],
           model_answer="The resistance of an LDR decreases as the light intensity falling on it increases: it is high in the dark and low in bright light.",
           hints=["Think of a street lamp circuit that switches on at night.", "In the dark the LDR's resistance is high.", "So in bright light it is ... ?"],
           keywords="resistance decreases as light intensity increases",
           sample_pass=["its resistance decreases as light intensity increases", "high resistance in the dark, low in bright light"], sample_fail=["its resistance increases in bright light", "it produces electricity from light"])

# ================================================================= 16 / 14  Practical electricity
definition("d_prac_heating_effect", "practical", 2, "14a",
           stem="Explain how the **heating effect** of a current is used in an electric kettle.",
           points=[P("the heating element has a high resistance", ["high resistance", "resistance wire", "heating element", "resistive"]),
                   P("current through it transfers electrical energy to thermal energy (electrons collide with the lattice), heating the water", ["electrical energy to thermal", "electrical energy is converted to heat", "converted to thermal energy", "transferred to thermal energy", "electrons collide", "heats up", "thermal energy", "heat energy"])],
           model_answer="The kettle's heating element is a coil of wire with high resistance. When current flows through it, the electrons collide with the metal ions and electrical energy is transferred to thermal energy, which heats the water. The energy transferred is E = VIt (or I²Rt).",
           hints=["What is special about the wire in the element?", "What happens to the energy of the current as it passes through a resistance?", "Name the energy transfer."],
           keywords="high-resistance element; electrical energy -> thermal energy",
           sample_pass=["the element has high resistance so the current transfers electrical energy to thermal energy, heating the water", "current in the resistive heating element converts electrical to heat energy"],
           sample_fail=["the kettle uses a motor to heat the water", "electricity is hot"])

definition("d_prac_kwh", "practical", 2, "14c",
           stem="State what is meant by the **kilowatt-hour (kWh)**.",
           points=[P("a unit of energy", ["unit of energy", "amount of energy", "energy transferred", "energy used", "energy consumed", "energy"]),
                   P("equal to the energy transferred by a 1 kW appliance in 1 hour (3.6 MJ)", ["1 kw appliance in 1 hour", "1 kw for 1 hour", "1 kilowatt for one hour", "1000 w for 1 hour", "1 kw in one hour", "one kilowatt for one hour", "3.6 mj", "3 600 000 j", "3600000 j", "3.6 × 10^6", "3.6 x 10^6", "1 kw × 1 h", "power of 1 kw in a time of 1 h", "1 kw device running for 1 hour", "1 kw appliance used for 1 hour"])],
           pitfalls=[PF(["unit of power", "measure of power", "is a power"], "A kWh is a unit of ENERGY, not power (examiner report 2023: many said power).")],
           model_answer="The kilowatt-hour is a unit of energy: the energy transferred by a 1 kW appliance operating for 1 hour (1 kWh = 1000 W × 3600 s = 3.6 × 10⁶ J).",
           hints=["Kilowatt is a unit of power; hour is a unit of time. Power × time = ?", "So kWh is a unit of ... ?", "Define it with a 1 kW appliance running for 1 hour."],
           keywords="energy; 1 kW for 1 hour; 3.6 MJ",
           sample_pass=["the energy transferred by a 1 kW appliance in 1 hour", "a unit of energy equal to 3.6 MJ"], sample_fail=["a unit of power used by the electricity company", "1000 watts"])

definition("d_prac_hazards", "practical", 2, "14d",
           stem="State the hazard in each case: (i) damaged insulation, (ii) overheating of cables, (iii) damp conditions.",
           points=[P("damaged insulation: exposed live wire -> electric shock (or short circuit)", ["exposed live", "exposed wire", "bare wire", "touch the live", "electric shock", "electrocut", "short circuit"]),
                   P("overheating of cables: too large a current (overloading, too many appliances) heats the cable -> fire", ["fire", "melt the insulation", "catch fire", "burn"]),
                   P("damp conditions: water conducts / reduces skin resistance -> larger current through the body -> electric shock", ["water conducts", "water is a conductor", "conducts electricity", "lower resistance", "reduces the resistance", "path for the current", "larger current through the body", "shock"])],
           model_answer="(i) Damaged insulation exposes the live wire; touching it gives an electric shock, and bare wires touching cause a short circuit. (ii) Overheating cables (from too large a current, e.g. overloading a socket) can melt the insulation and start a fire. (iii) Water conducts electricity and lowers the resistance of the skin, so in damp conditions a much larger current can flow through the body, causing a severe shock.",
           hints=["Think shock, fire, shock.", "Damaged insulation: what becomes exposed?", "Why is water dangerous near electricity?"],
           keywords="exposed live wire -> shock; overheating -> fire; water conducts -> shock",
           sample_pass=["damaged insulation exposes the live wire giving shocks; overheated cables can catch fire; water conducts so damp conditions give electric shocks", "exposed wires cause electric shock or short circuit; hot cables melt insulation and cause fire; wet skin has lower resistance so a bigger current flows"],
           sample_fail=["they all waste electricity", "damaged insulation makes the appliance stop working"])

definition("d_prac_fuse", "practical", 2, "14e",
           stem="Explain how a **fuse** protects a circuit, and how its rating should be chosen.",
           points=[P("a thin wire that melts (breaks the circuit) when the current exceeds its rating", ["melts", "melt", "breaks the circuit", "break the circuit", "blows", "cuts off the current", "opens the circuit"]),
                   P("this happens when the current is too large (exceeds the rated value), preventing overheating / fire / damage", ["too large", "exceeds", "greater than the rating", "above the rating", "larger than", "too high", "overload", "excessive"]),
                   P("rating chosen slightly higher than the normal operating current of the appliance", ["slightly higher than the normal", "slightly above the normal", "just above the normal operating current", "slightly greater than the normal", "a little higher than the", "slightly larger than the normal", "just higher than the working current", "slightly more than the normal current"])],
           min_points=2,
           pitfalls=[PF(["rating lower than the normal", "rating less than the normal", "below the normal current"], "A rating BELOW the normal current would blow in normal use. Choose a rating slightly ABOVE the normal operating current."),
                     PF(["much higher than", "far above"], "Not much higher: a fuse rated far above the normal current would let a dangerous current flow. It should be only slightly above.")],
           model_answer="A fuse is a thin wire that melts and breaks the circuit when the current through it exceeds its rated value, cutting off the current before the excessive current can overheat the wiring or appliance and cause a fire. Its rating is chosen slightly higher than the normal operating current of the appliance.",
           hints=["What happens to a thin wire when too much current flows through it?", "What does that do to the circuit?", "The rating is compared with the appliance's normal current: a bit above or a bit below?"],
           keywords="wire melts when current exceeds rating, breaks circuit; rating slightly above normal current",
           sample_pass=["the fuse wire melts when the current is too large, breaking the circuit; its rating should be slightly higher than the normal operating current", "if current exceeds the rating the wire melts and cuts off the current to prevent fire; choose a rating just above the working current"],
           sample_fail=["the fuse stops electricity leaking", "the fuse melts when the current is too small; choose a rating much higher than the normal current"])

definition("d_prac_circuit_breaker", "practical", 2, "14e",
           stem="State what a **circuit breaker** does, and give one advantage it has over a fuse.",
           points=[P("an automatic switch that trips (opens / breaks the circuit) when the current exceeds a set value", ["switch", "trips", "opens the circuit", "breaks the circuit", "cuts off", "switches off", "disconnects"]),
                   P("it can be reset (does not need replacing) / acts faster", ["reset", "switched back on", "reused", "does not need to be replaced", "no need to replace", "faster", "quicker", "more sensitive"])],
           model_answer="A circuit breaker is an automatic switch that trips, breaking the circuit, when the current exceeds a set value. Unlike a fuse it can simply be reset (switched back on) once the fault is fixed, rather than replaced, and it usually acts faster.",
           hints=["It does the same job as a fuse, but differently.", "What does it do when the current is too large?", "After it has operated, what can you do with it that you cannot do with a blown fuse?"],
           keywords="automatic switch trips on excess current; can be reset",
           sample_pass=["an automatic switch that trips when the current is too large; it can be reset instead of replaced", "breaks the circuit on excess current and can be switched back on"],
           sample_fail=["it breaks the circuit when the voltage is too low", "a stronger kind of fuse"])

definition("d_prac_earth", "practical", 3, "14f",
           stem="Explain why the metal casing of an appliance must be **earthed**.",
           points=[P("if a fault makes the live wire touch the casing, the casing becomes live", ["live wire touches the casing", "live wire comes into contact with the casing", "casing becomes live", "fault", "live wire touching the metal"]),
                   P("the earth wire provides a low-resistance path for a large current to flow to earth", ["low resistance path", "path to earth", "current flows to earth", "large current flows", "current to the ground", "low resistance route"]),
                   P("which blows the fuse / trips the breaker, cutting off the supply and preventing electric shock", ["blows the fuse", "fuse blows", "melts the fuse", "trips the circuit breaker", "trip the breaker", "cuts off the supply", "disconnects", "prevents electric shock", "prevent a shock", "user does not get a shock", "no shock"])],
           min_points=2,
           model_answer="If a fault causes the live wire to touch the metal casing, the casing becomes live. The earth wire connects the casing to earth with a low-resistance path, so a large current flows to earth; this blows the fuse (or trips the breaker), cutting off the supply, and the user touching the casing does not get an electric shock.",
           hints=["Imagine the live wire inside comes loose and touches the metal case.", "Where does the current go if the case is earthed?", "What does that large current do to the fuse?"],
           keywords="live touches casing; large current to earth via low-resistance earth wire; blows fuse; no shock",
           sample_pass=["If the live wire touches the casing, the earth wire gives a low-resistance path so a large current flows to earth and blows the fuse, preventing a shock", "a fault making the casing live sends current to earth through the earth wire, which trips the breaker"],
           sample_fail=["earthing makes the appliance more powerful", "the earth wire carries the current back to the power station"])

definition("d_prac_double_insulation", "practical", 3, "14f",
           stem="State what is meant by **double insulation**, and why such an appliance does not need an earth wire.",
           points=[P("the appliance has a non-conducting (plastic) casing in addition to the insulation on the wires / internal parts", ["plastic casing", "insulating casing", "non-conducting casing", "non-metallic casing", "two layers of insulation", "second layer of insulation", "casing is an insulator", "insulated casing"]),
                   P("so no exposed metal part can become live, hence no earth wire is needed", ["cannot become live", "no exposed metal", "no metal parts", "cannot conduct", "cannot give a shock", "no earth wire is needed", "does not need earthing", "no need for an earth"])],
           model_answer="A double-insulated appliance has its live parts insulated in the usual way and, in addition, a casing made of an insulator such as plastic. Since no exposed metal part can ever become live, the user cannot get a shock from the casing, so no earth wire is needed (only live and neutral).",
           hints=["Think of a plastic hairdryer or phone charger.", "What is the casing made of?", "Why does that make an earth wire unnecessary?"],
           keywords="insulating (plastic) casing + insulated wires; no exposed metal can become live",
           sample_pass=["the casing is made of plastic as well as the wires being insulated, so no metal part can become live and no earth wire is needed", "two layers of insulation including a non-conducting case, so it cannot give a shock without an earth"],
           sample_fail=["it has two earth wires", "the wires are twice as thick"])

definition("d_prac_live_neutral_earth", "practical", 2, "14g",
           stem="State the meaning of the terms **live**, **neutral** and **earth** wires.",
           points=[P("live: carries the current to the appliance at high (alternating) potential (about 230 V)", ["high potential", "high voltage", "230 v", "240 v", "alternating potential", "carries the current to the appliance", "delivers the current", "brings the current"]),
                   P("neutral: completes the circuit, carrying current back, at about 0 V (earth potential)", ["completes the circuit", "complete the circuit", "returns the current", "carries the current back", "return path", "0 v", "zero potential", "earth potential", "zero volts"]),
                   P("earth: safety wire connected to the metal casing and to the ground (0 V); carries no current normally", ["safety", "connected to the casing", "metal casing", "connected to the ground", "to the earth", "no current normally", "normally carries no current", "carries current only if there is a fault", "protects the user"])],
           min_points=3,
           model_answer="The live wire carries the current to the appliance and is at a high alternating potential (about 230 V). The neutral wire completes the circuit, carrying the current back to the supply, and is at about 0 V. The earth wire is a safety wire connected to the metal casing and to the ground (0 V); it carries current only if there is a fault.",
           hints=["Three wires, three jobs.", "Which one is at 230 V? Which one is at 0 V and completes the circuit?", "Which one is only for safety?"],
           keywords="live: 230 V, carries current in; neutral: 0 V, completes circuit; earth: safety, to casing and ground",
           sample_pass=["live is at 230 V and brings the current; neutral completes the circuit at 0 V; earth is a safety wire connecting the casing to the ground", "the live wire is at high voltage, the neutral returns the current at zero potential, and the earth wire protects the user by connecting the metal casing to earth"],
           sample_fail=["live is positive, neutral is negative, earth is the ground", "live wire is brown"])

definition("d_prac_switch_live", "practical", 3, "14i",
           stem="Explain why switches and fuses are connected to the **live** wire rather than the neutral wire.",
           points=[P("so that when the switch is off / fuse blows, the appliance is disconnected from the high potential (live) side", ["disconnected from the live", "disconnects the live", "isolated from the live", "cuts off the live", "no longer connected to the high", "breaks the live", "disconnected from the high voltage", "disconnected from the supply", "isolates the appliance", "cuts the high voltage", "separates the appliance from the live"]),
                   P("otherwise the appliance would remain live (at 230 V) even when switched off, and a person touching it could get a shock", ["would still be live", "remains live", "still at 230 v", "still connected to the live", "still at high potential", "electric shock", "shock even when switched off", "still dangerous", "could still get a shock"])],
           model_answer="If the switch or fuse is in the live wire, opening it disconnects the appliance from the high-voltage live side, so the appliance is safe to touch. If it were in the neutral wire, the appliance would still be connected to the live wire at 230 V when switched off (or after the fuse blew), and a person touching it could receive an electric shock.",
           hints=["Which wire is at 230 V?", "If the switch were on the neutral side, what would the appliance still be connected to when 'off'?", "Say what the danger is."],
           keywords="disconnects the live (230 V) side; otherwise appliance stays live -> shock",
           sample_pass=["so that switching off disconnects the appliance from the live wire; otherwise it would still be at 230 V and could give a shock", "the switch in the live wire isolates the appliance from the high voltage; in the neutral it would remain live when off"],
           sample_fail=["because the live wire is thicker", "because the neutral wire has no current"])

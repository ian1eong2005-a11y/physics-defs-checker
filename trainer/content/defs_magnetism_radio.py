"""Definitions: Magnetism, Electromagnetism, Electromagnetic induction (6091), Radioactivity."""
from ..marker import Pitfall, Point
from .base import BOTH, PURE, definition

P, PF = Point, Pitfall

# ================================================================= 17 / 15  Magnetism
definition("d_mag_properties", "magnetism", 2, "15a",
           stem="State **three** properties of a magnet.",
           points=[P("has two poles, north and south (poles cannot be isolated)", ["two poles", "north and south", "north pole and a south pole", "n and s"]),
                   P("like poles repel, unlike poles attract", ["like poles repel", "unlike poles attract", "same poles repel", "opposite poles attract", "like repel", "unlike attract"]),
                   P("attracts magnetic materials (iron, steel, nickel, cobalt)", ["attracts magnetic materials", "attracts iron", "attracts steel", "attracts nickel", "attract magnetic"]),
                   P("a freely suspended magnet comes to rest pointing north-south", ["freely suspended", "points north", "north-south", "north south", "compass"]),
                   P("magnetic force is strongest at the poles", ["strongest at the poles", "strongest at the ends", "concentrated at the poles"])],
           min_points=3,
           model_answer="A magnet has two poles (north and south); like poles repel and unlike poles attract; it attracts magnetic materials such as iron, steel, nickel and cobalt; a freely suspended magnet comes to rest pointing north-south; the magnetic force is strongest at the poles.",
           hints=["Think of a bar magnet and a compass.", "Poles: how many, and how do they interact?", "What materials does it attract?"],
           keywords="two poles; like repel/unlike attract; attracts magnetic materials; points N-S",
           sample_pass=["it has a north and south pole, like poles repel and unlike poles attract, and it attracts iron", "two poles; attracts magnetic materials; a freely suspended magnet points north-south"],
           sample_fail=["it is made of metal and is heavy", "like poles attract and unlike poles repel"])

definition("d_mag_induced", "magnetism", 2, "15b",
           stem="State what is meant by **induced magnetism**.",
           points=[P("a magnetic material becomes a magnet (is magnetised)", ["becomes a magnet", "becomes magnetised", "is magnetised", "turns into a magnet", "becomes magnetic", "magnetism is produced in", "magnetic material becomes"]),
                   P("when it is placed near or in contact with a magnet (in a magnetic field), or inside a current-carrying solenoid", ["near a magnet", "close to a magnet", "in contact with a magnet", "touching a magnet", "in a magnetic field", "placed in a magnetic field", "solenoid", "near a strong magnet", "brought near a magnet", "within a magnetic field"])],
           model_answer="Induced magnetism is the magnetism produced in a magnetic material (such as iron) when it is placed near or in contact with a magnet or inside a current-carrying solenoid: the material becomes a magnet itself, with the pole nearest the magnet opposite to the inducing pole.",
           hints=["A paper clip hanging from a magnet can pick up another paper clip.", "What has the first paper clip become?", "What caused it?"],
           keywords="magnetic material becomes a magnet when near a magnet / in a solenoid",
           sample_pass=["a magnetic material becomes a magnet when placed near a magnet", "iron becomes magnetised when placed in a magnetic field or in a solenoid"], sample_fail=["a magnet that has lost its magnetism", "current produced by a magnet"])

definition("d_mag_temp_perm", "magnetism", 3, "15c",
           stem="Distinguish between **temporary** magnets (e.g. iron) and **permanent** magnets (e.g. steel), and give one use of each.",
           points=[P("iron is easily magnetised and easily demagnetised (loses its magnetism when the field is removed)", ["easily magnetised", "easy to magnetise", "loses its magnetism", "easily demagnetised", "quickly loses", "does not keep", "does not retain", "temporary"]),
                   P("steel is harder to magnetise but retains (keeps) its magnetism", ["retains its magnetism", "keeps its magnetism", "harder to magnetise", "difficult to magnetise", "does not lose its magnetism", "remains magnetised", "stays magnetised", "permanent"]),
                   P("uses: iron for electromagnets, relays, transformer cores, motor armatures; steel for permanent magnets, compass needles, fridge magnets", ["electromagnet", "relay", "transformer core", "core", "armature", "compass", "fridge magnet", "permanent magnet", "loudspeaker"])],
           model_answer="Iron (a soft magnetic material) is easily magnetised and easily demagnetised, so it is used where the magnetism must switch on and off: electromagnets, relays, transformer cores. Steel (a hard magnetic material) is harder to magnetise but retains its magnetism, so it is used for permanent magnets and compass needles.",
           hints=["One keeps its magnetism, the other loses it when the magnetising field is removed.", "Which would you want in an electromagnet that must switch off?", "Which would you want in a compass needle?"],
           keywords="iron: easy to magnetise/demagnetise, electromagnets; steel: retains magnetism, permanent magnets",
           sample_pass=["iron is easily magnetised and demagnetised so it is used in electromagnets; steel keeps its magnetism so it is used for permanent magnets", "steel retains magnetism, used for compass needles; iron loses it quickly, used in transformer cores"],
           sample_fail=["iron is stronger than steel", "steel is easily demagnetised so it is used in electromagnets"])

definition("d_mag_field", "magnetism", 2, "15d",
           stem="State what is meant by a **magnetic field**, and how the direction of the field at a point is defined.",
           points=[P("a region in which a magnetic material (or a magnet / current-carrying conductor / moving charge) experiences a (magnetic) force", ["region in which a magnetic", "region where a magnetic", "region around a magnet", "region in which a magnet experiences", "region in which a magnetic material experiences a force", "space around a magnet", "experiences a magnetic force", "experiences a force"]),
                   P("direction: the direction in which the north pole of a compass (free north pole) points, from N to S outside the magnet", ["north pole of a compass points", "direction a compass needle points", "compass north points", "direction of the force on a north pole", "north to south", "from north to south", "n to s", "free north pole would move", "compass needle"])],
           model_answer="A magnetic field is a region in which a magnetic material (or a magnet, moving charge or current-carrying conductor) experiences a force. The direction of the field at a point is the direction in which the north pole of a small compass placed there points; field lines run from the north pole to the south pole outside a magnet.",
           hints=["A field is a region.", "What experiences a force in it?", "How would you find the direction with a plotting compass?"],
           keywords="region where magnetic material experiences a force; direction a compass north pole points (N to S)",
           sample_pass=["a region in which a magnetic material experiences a force; its direction is the way a compass needle's north pole points", "the region around a magnet where a magnet feels a force, directed from north to south"],
           sample_fail=["the force between two magnets", "a region where a mass experiences a force"])

# ================================================================= 18 / 15  Electromagnetism
definition("d_emag_current_field", "electromag", 2, "15f",
           stem="Describe the magnetic field around a long straight current-carrying wire, and state how it changes if the current is (i) increased, (ii) reversed.",
           points=[P("concentric circles centred on the wire (field weaker further from the wire)", ["concentric circles", "circles around the wire", "circular", "circles centred on the wire", "circular field lines"]),
                   P("increasing the current makes the field stronger", ["stronger", "greater", "increases the strength", "more"]),
                   P("reversing the current reverses the direction of the field", ["reverses the direction", "field reverses", "opposite direction", "direction is reversed", "reverse the field", "field lines reverse"])],
           model_answer="The field lines are concentric circles around the wire, closer together near the wire (direction given by the right-hand grip rule). Increasing the current makes the field stronger; reversing the current reverses the direction of the field.",
           hints=["Picture iron filings around a vertical wire.", "What happens to the strength when the current grows?", "What happens to the direction when the current flows the other way?"],
           keywords="concentric circles; stronger with more current; reversed with reversed current",
           sample_pass=["concentric circles around the wire; a larger current gives a stronger field and reversing the current reverses the field direction", "circular field lines; more current, stronger field; opposite current, opposite direction"],
           sample_fail=["straight lines parallel to the wire", "the field does not depend on the current"])

definition("d_emag_flhr", "electromag", 2, "15h",
           stem="State **Fleming's left-hand rule**: what does each of the thumb, first finger and second finger represent?",
           points=[P("thumb: force (motion / thrust)", ["thumb force", "thumb is the force", "thumb motion", "thumb thrust", "thumb represents the force", "thumb shows the force", "thumb points in the direction of the force", "thumb gives the force", "force thumb", "thumb for force", "thumb direction of force"]),
                   P("first finger: (magnetic) field, N to S", ["first finger field", "first finger magnetic field", "forefinger field", "index finger field", "first finger represents the field", "first finger is the field", "first finger shows the field", "field first finger", "first finger for field", "first finger direction of the field", "first finger points in the direction of the field"]),
                   P("second finger: (conventional) current", ["second finger current", "middle finger current", "second finger is the current", "second finger represents the current", "second finger shows the current", "current second finger", "second finger for current", "second finger direction of the current", "second finger points in the direction of the current"]),
                   P("held mutually at right angles", ["right angles", "perpendicular", "90°", "90 degrees"])],
           min_points=3,
           pitfalls=[PF(["thumb current", "thumb is the current", "thumb represents the current", "second finger force", "second finger is the force", "first finger current", "first finger is the current"], "Mixed up: THumb = THrust (force), First finger = Field, seCond finger = Current.")],
           model_answer="Hold the thumb, first finger and second finger of the left hand mutually at right angles: the First finger points along the magnetic Field (N to S), the seCond finger along the conventional Current, and the thuMb gives the direction of the force (Motion) on the conductor.",
           hints=["Three digits at right angles.", "F-F-C: First finger - Field; seCond finger - Current.", "What is left for the thumb?"],
           keywords="thumb: force; first finger: field; second finger: current; at right angles",
           sample_pass=["thumb is the force, first finger the field and second finger the current, all at right angles", "First finger = field, second finger = current, thumb = motion"],
           sample_fail=["thumb is the current, first finger the field, second finger the force", "it finds the direction of the magnetic field around a wire"])

definition("d_emag_force_factors", "electromag", 3, "15g",
           stem="A current-carrying wire in a magnetic field experiences a force. State the effect on the force of (i) reversing the current, (ii) reversing the magnetic field, (iii) increasing the current.",
           points=[P("reversing the current reverses the direction of the force", ["reverses the force", "force reverses", "force is reversed", "opposite direction", "force acts in the opposite", "reverse the direction of the force", "force changes direction"]),
                   P("reversing the field also reverses the direction of the force", ["also reverses", "also reversed", "reversing the field reverses", "field reverses the force", "field also", "both reverse", "either reverses"]),
                   P("increasing the current (or field strength) increases the force", ["larger force", "greater force", "force increases", "bigger force", "stronger force", "increases the force", "more force", "increases with current", "increases with the current", "increases with a larger current"])],
           pitfalls=[PF(["reversing the current makes the force", "reversing the current increases", "reversing the current gives a bigger", "reversing the field makes the force bigger", "reversing the field increases"], "Reversing the current (or the field) changes the DIRECTION of the force, not its size. Increasing the current increases the force.")],
           model_answer="(i) Reversing the current reverses the direction of the force. (ii) Reversing the direction of the magnetic field also reverses the direction of the force. (iii) Increasing the current (or using a stronger magnetic field) increases the size of the force. (Reversing both current and field leaves the force unchanged.)",
           hints=["Use Fleming's left-hand rule for (i) and (ii).", "If one of field or current reverses, what happens to the force?", "For (iii), is the force bigger or smaller?"],
           keywords="reverse I -> force reverses; reverse B -> force reverses; more I -> bigger force",
           sample_pass=["reversing the current reverses the force; reversing the field also reverses the force; a larger current gives a larger force", "the force changes direction if either the current or the field is reversed, and increases with current"],
           sample_fail=["reversing the current makes the force bigger", "the force is not affected by the field direction"])

definition("d_emag_motor_turning", "electromag", 3, "15i",
           stem="Explain why a current-carrying rectangular coil in a magnetic field experiences a turning effect, and state **two** ways to increase it.",
           points=[P("the current flows in opposite directions in the two sides of the coil, so (by Fleming's left-hand rule) the forces on the two sides are in opposite directions", ["opposite directions", "current flows in opposite directions", "forces on the two sides are opposite", "one side up and the other down", "force upwards on one side and downwards on the other", "opposite forces on the two sides", "equal and opposite forces", "couple"]),
                   P("these two forces produce a (resultant) moment / couple that turns the coil about its axis", ["turning effect", "moment", "torque", "couple", "rotate", "turns the coil", "turn", "spin"]),
                   P("increase it by: more turns on the coil, larger current, stronger magnetic field (or a soft-iron core)", ["more turns", "number of turns", "larger current", "increase the current", "bigger current", "stronger magnet", "stronger field", "stronger magnetic field", "soft iron core", "iron core"])],
           min_points=2,
           model_answer="The current flows in opposite directions along the two sides of the coil that lie in the field, so by Fleming's left-hand rule the forces on these two sides are equal and opposite. Acting on opposite sides of the axis, they form a couple that produces a turning effect on the coil. The turning effect is increased by increasing the number of turns on the coil, increasing the current, or using a stronger magnetic field (and winding the coil on a soft-iron core).",
           hints=["Compare the current direction in the two long sides of the coil.", "Use Fleming's left-hand rule on each side: what do the two forces do together?", "What would make each force bigger, or give more of them?"],
           keywords="opposite currents -> opposite forces -> couple/turning effect; more turns, more current, stronger field",
           sample_pass=["the two sides carry current in opposite directions so the forces on them are opposite, producing a turning effect; increase the current or the number of turns", "forces on the two sides form a couple that rotates the coil; use a stronger magnet and more turns"],
           sample_fail=["the coil turns because the magnet attracts it", "the forces on both sides are in the same direction so it moves up"])

definition("d_emag_commutator", "electromag", 4, "18f",
           stem="Describe the function of the **split-ring commutator** in a d.c. motor.", syllabi=PURE,
           points=[P("it reverses the direction of the current in the coil", ["reverses the current", "reverses the direction of the current", "current in the coil is reversed", "switches the direction of the current", "changes the direction of the current", "current reverses"]),
                   P("every half revolution (each time the coil passes the vertical position)", ["every half revolution", "every half turn", "each half revolution", "every half a rotation", "twice every revolution", "when the coil is vertical", "passes the vertical", "every 180"]),
                   P("so that the force on each side reverses and the coil keeps turning in the same direction", ["same direction", "continues to rotate", "keeps turning", "keep rotating", "continuous rotation", "continue to turn", "keeps spinning", "turns continuously"])],
           min_points=2,
           pitfalls=[PF(["slip rings", "slip ring"], "Slip rings are used in an a.c. GENERATOR. A d.c. motor uses a SPLIT-RING commutator.")],
           model_answer="The split-ring commutator reverses the direction of the current in the coil every half revolution (as the coil passes the vertical). This reverses the forces on the two sides of the coil just as they swap places, so the turning effect stays in the same direction and the coil keeps rotating the same way.",
           hints=["Without it, the coil would rock back and forth and stop at the vertical.", "What must happen to the current in the coil each half turn?", "What is the result for the direction of rotation?"],
           keywords="reverses current in coil every half revolution; keeps coil turning the same way",
           sample_pass=["it reverses the current in the coil every half revolution so that the coil keeps turning in the same direction", "the commutator switches the current direction each half turn so rotation is continuous"],
           sample_fail=["it connects the coil to the battery", "slip rings keep the coil turning"])

# ================================================================= 19  Electromagnetic induction (6091)
definition("d_emi_induction", "emi", 2, "19a",
           stem="State what is meant by **electromagnetic induction**.", syllabi=PURE,
           points=[P("an e.m.f. (and hence a current, if the circuit is complete) is induced in a conductor / circuit", ["emf is induced", "induced emf", "induces an emf", "emf is produced", "produces an emf", "production of an emf", "emf is generated", "generates an emf", "voltage is induced", "current is induced", "induced current", "induces a current", "induced voltage"]),
                   P("when the magnetic field linking it changes (relative motion between conductor and field / conductor cuts magnetic field lines)", ["changing magnetic field", "magnetic field changes", "change in the magnetic field", "cuts magnetic field lines", "cuts the magnetic field", "cutting field lines", "relative motion between", "moves relative to a magnetic field", "moved in a magnetic field", "changing magnetic flux", "change in magnetic flux", "magnet is moved"])],
           model_answer="Electromagnetic induction is the production of an e.m.f. (and a current, if the circuit is complete) in a conductor or circuit when the magnetic field linking it changes, for example when the conductor moves relative to a magnetic field and cuts the field lines.",
           hints=["Move a magnet into a coil connected to a galvanometer.", "What is produced in the coil?", "What has to be happening to the magnetic field for this to occur?"],
           keywords="e.m.f. induced when magnetic field linking the circuit changes",
           sample_pass=["an e.m.f. is induced in a circuit when the magnetic field through it changes", "a conductor cutting magnetic field lines has an emf induced in it"], sample_fail=["a current produces a magnetic field", "a magnet attracts a conductor"])

definition("d_emi_lenz", "emi", 3, "19a",
           stem="State the rule that gives the **direction** of an induced e.m.f. (Lenz's law).", syllabi=PURE,
           points=[P("the induced e.m.f. (current) is in such a direction as to oppose the change producing it", ["oppose the change producing it", "opposes the change that produces it", "opposes the change causing it", "opposes the change that caused it", "oppose the change which produced", "oppose the change in the magnetic", "opposes the motion", "oppose the motion producing it", "opposes the change that created it", "opposes the change that induced it", "oppose the change"])],
           pitfalls=[PF(["same direction as the change", "assists the change", "helps the change"], "The induced e.m.f. OPPOSES the change that produces it (otherwise energy would be created from nothing).")],
           model_answer="The direction of the induced e.m.f. (and current) is such that it opposes the change producing it (Lenz's law), for example the induced current in a coil sets up a pole that repels an approaching magnet.",
           hints=["Push a north pole into a coil: the coil's near end becomes a north pole too.", "Is the coil helping or hindering the magnet?", "State it as a general rule about the change producing the e.m.f."],
           keywords="induced e.m.f. opposes the change producing it",
           sample_pass=["the induced current flows in such a direction as to oppose the change producing it", "it opposes the change that causes it"], sample_fail=["it is in the same direction as the magnetic field", "it helps the magnet move"])

definition("d_emi_factors", "emi", 3, "19a",
           stem="State **three** factors that increase the magnitude of the e.m.f. induced in a coil when a magnet is moved into it.", syllabi=PURE,
           points=[P("moving the magnet (or coil) faster (greater rate of change of magnetic field)", ["faster", "greater speed", "higher speed", "quickly", "rate of change", "move the magnet more quickly", "increase the speed"]),
                   P("more turns on the coil", ["more turns", "number of turns", "greater number of turns", "increase the turns"]),
                   P("a stronger magnet (stronger magnetic field) / larger coil area / soft-iron core", ["stronger magnet", "stronger magnetic field", "stronger field", "larger area", "bigger coil", "iron core", "soft iron"])],
           model_answer="The induced e.m.f. is larger when (1) the magnet (or coil) moves faster, so the magnetic field through the coil changes more quickly; (2) the coil has more turns; (3) a stronger magnet is used (also a larger coil area or a soft-iron core).",
           hints=["Think about what you could change: the magnet, the coil, the movement.", "Speed matters: the e.m.f. depends on the rate of change of the field.", "Give three factors."],
           keywords="faster motion; more turns; stronger magnet",
           sample_pass=["move the magnet faster, use more turns on the coil, use a stronger magnet", "greater speed, more turns, stronger magnetic field"], sample_fail=["use a bigger battery and thicker wire", "a heavier magnet"])

definition("d_emi_generator", "emi", 3, "19b",
           stem="In a simple a.c. generator, state the purpose of the **slip rings** and explain why the output is alternating.", syllabi=PURE,
           points=[P("slip rings keep the rotating coil connected to the external circuit (via the brushes) without the wires twisting, each end of the coil always connected to the same ring", ["connect the coil to the external circuit", "connect the rotating coil", "maintain contact", "keeps contact with the brushes", "without twisting", "without the wires twisting", "continuous contact", "connected to the same ring", "connected to the external circuit", "connection to the brushes", "electrical contact"]),
                   P("as the coil rotates, each side moves up through the field for half a turn and down for the next half, so the induced e.m.f. reverses every half revolution: alternating output", ["reverses every half", "changes direction every half", "each side moves up then down", "direction of motion reverses", "cuts the field in the opposite direction", "induced e.m.f. reverses", "current reverses direction", "alternates every half", "reverses direction every half turn", "alternating because the sides swap", "every half revolution", "swap direction", "each half turn", "sides of the coil swap", "swap sides", "swap over"])],
           model_answer="The slip rings rotate with the coil and press against fixed carbon brushes, keeping the coil connected to the external circuit without the wires twisting; each end of the coil stays connected to its own ring, so the output is not reversed by the rings. The output alternates because each side of the coil moves up through the field for half a revolution and down for the next half, so the direction of the induced e.m.f. reverses every half revolution.",
           hints=["Compare with the commutator of a motor: rings here are continuous.", "How does the coil stay connected to the outside circuit as it spins?", "What happens to the direction in which each side cuts the field every half turn?"],
           keywords="slip rings: continuous connection to brushes; e.m.f. reverses every half turn",
           sample_pass=["slip rings keep the rotating coil connected to the brushes without twisting; the e.m.f. reverses every half revolution because each side moves up then down through the field", "they maintain electrical contact with the external circuit; the current alternates as the sides of the coil swap direction each half turn"],
           sample_fail=["the slip rings reverse the current every half turn to keep it d.c.", "the output alternates because the magnet is turned on and off"])

definition("d_emi_transformer", "emi", 4, "19d",
           stem="Explain how a **transformer** transfers energy from the primary coil to the secondary coil.", syllabi=PURE,
           points=[P("an alternating current in the primary coil produces a changing (alternating) magnetic field", ["alternating current in the primary", "a.c. in the primary", "changing magnetic field", "alternating magnetic field", "varying magnetic field", "magnetic field that changes", "changing field"]),
                   P("the soft-iron core carries (links) this changing field to the secondary coil", ["iron core", "core", "links the secondary", "linked to the secondary", "passes through the secondary", "through the secondary coil", "carried to the secondary"]),
                   P("the changing field through the secondary induces an alternating e.m.f. in it (electromagnetic induction)", ["induces an e.m.f.", "induces an emf", "e.m.f. is induced", "emf is induced", "induced e.m.f.", "induced in the secondary", "electromagnetic induction", "induces an alternating", "induces a voltage", "induced voltage"])],
           min_points=2,
           pitfalls=[PF(["direct current in the primary", "d.c. in the primary", "works with d.c."], "A transformer needs ALTERNATING current: a steady d.c. gives a steady field and induces nothing."),
                     PF(["current flows through the core", "core conducts the current", "coils are connected"], "The coils are NOT electrically connected: the core carries the magnetic field, not the current.")],
           model_answer="The alternating current in the primary coil produces an alternating magnetic field in the soft-iron core. The core links this changing magnetic field to the secondary coil, so by electromagnetic induction an alternating e.m.f. is induced in the secondary coil. The voltage ratio equals the turns ratio, Vs/Vp = Ns/Np.",
           hints=["Three stages: primary coil, core, secondary coil.", "What kind of magnetic field does an a.c. produce, and what carries it to the other coil?", "What does a changing field through a coil do?"],
           keywords="a.c. -> changing field in core -> induced alternating e.m.f. in secondary",
           sample_pass=["The a.c. in the primary creates a changing magnetic field in the iron core, which induces an alternating e.m.f. in the secondary coil", "alternating current gives an alternating magnetic field linked by the core to the secondary, where an emf is induced"],
           sample_fail=["the current flows from the primary through the core to the secondary", "the primary coil heats the secondary coil"])

definition("d_emi_high_voltage", "emi", 4, "19f",
           stem="Explain why electrical energy is transmitted over long distances at **high voltage**.", syllabi=PURE,
           points=[P("for the same power transmitted, a higher voltage means a smaller current (P = VI)", ["smaller current", "lower current", "less current", "reduces the current", "current is reduced", "p = vi", "same power with a lower current"]),
                   P("so the power lost as heat in the cables (P = I²R) is much smaller / less energy wasted", ["less power loss", "less energy lost", "reduces the power loss", "power loss is reduced", "less heat", "i²r", "i^2r", "i2r", "less energy wasted", "lower power loss", "reduces heating of the cables", "smaller power loss", "less power is wasted", "less power wasted"])],
           pitfalls=[PF(["electricity travels faster", "current flows faster"], "Nothing to do with speed. High voltage means a LOWER CURRENT for the same power, so less I²R heating in the cables.")],
           model_answer="For a given power, P = VI, so transmitting at a high voltage means the current in the cables is small. The power wasted as heat in the cables is I²R, so a smaller current greatly reduces the energy lost in transmission.",
           hints=["Power delivered is P = VI: if V goes up, what happens to I for the same P?", "The cables have resistance. Power lost in them depends on which quantity?", "Put the two ideas together."],
           keywords="same power, smaller current; less I²R heat loss in cables",
           sample_pass=["high voltage means a smaller current for the same power, so the I²R power loss in the cables is reduced", "lower current means less energy is wasted as heat in the transmission lines"],
           sample_fail=["high voltage pushes the electricity faster", "high voltage reduces the resistance of the cables"])

# ================================================================= 20 / 16  Radioactivity
definition("d_rad_atom", "radio", 1, "16a",
           stem="Describe the composition of an atom.",
           points=[P("a positively charged nucleus containing protons (positive) and neutrons (neutral)", ["positively charged nucleus", "positive nucleus", "nucleus containing protons and neutrons", "protons and neutrons in the nucleus", "nucleus of protons and neutrons", "nucleus made of protons and neutrons", "protons and neutrons"]),
                   P("surrounded by negatively charged electrons (in shells / orbiting)", ["negatively charged electrons", "negative electrons", "electrons orbit", "electrons around", "surrounded by electrons", "electrons in shells", "electrons move around"])],
           pitfalls=[PF(["electrons in the nucleus", "nucleus contains electrons"], "Electrons are OUTSIDE the nucleus. The nucleus holds only protons and neutrons.")],
           model_answer="An atom has a small, dense, positively charged nucleus made of protons (positive) and neutrons (neutral), surrounded by negatively charged electrons. A neutral atom has equal numbers of protons and electrons.",
           hints=["Two regions: the centre and the outside.", "Which particles are in the nucleus, and what is its charge?", "Which particles are outside?"],
           keywords="positive nucleus (protons + neutrons); electrons outside",
           sample_pass=["a positively charged nucleus of protons and neutrons with negatively charged electrons around it", "protons and neutrons in the nucleus, electrons orbiting outside"], sample_fail=["protons, neutrons and electrons all in the nucleus", "a ball of positive charge"])

definition("d_rad_proton_number", "radio", 1, "16b",
           stem="State what is meant by the **proton (atomic) number** Z and the **nucleon (mass) number** A.",
           points=[P("proton number: the number of protons in the nucleus", ["number of protons"]),
                   P("nucleon number: the total number of protons and neutrons (nucleons) in the nucleus", ["number of protons and neutrons", "protons plus neutrons", "total number of nucleons", "number of nucleons", "protons and neutrons in the nucleus", "sum of protons and neutrons", "protons + neutrons"])],
           pitfalls=[PF(["nucleon number is the number of neutrons", "mass number is the number of neutrons", "number of neutrons in the nucleus"], "Nucleon number counts protons AND neutrons together; the number of neutrons alone is A − Z.")],
           model_answer="The proton (atomic) number Z is the number of protons in the nucleus. The nucleon (mass) number A is the total number of nucleons, i.e. protons plus neutrons, in the nucleus.",
           hints=["Both count particles in the nucleus.", "Z counts one kind of particle.", "A counts both kinds together."],
           keywords="Z = number of protons; A = protons + neutrons",
           sample_pass=["proton number is the number of protons; nucleon number is the number of protons plus neutrons", "Z is the number of protons and A is the total number of nucleons"], sample_fail=["proton number is the number of protons and nucleon number is the number of neutrons", "Z is the charge and A is the mass in grams"])

definition("d_rad_isotope", "radio", 2, "16b",
           stem="State what is meant by **isotopes**.",
           points=[P("atoms of the same element (same proton number)", ["same element", "same proton number", "same atomic number", "same number of protons"]),
                   P("with different numbers of neutrons (different nucleon numbers)", ["different numbers of neutrons", "different number of neutrons", "different nucleon number", "different mass number", "different neutron number", "differing numbers of neutrons", "different numbers of nucleons", "different neutrons"], ordered=True)],
           pitfalls=[PF(["different numbers of protons", "different number of protons", "different proton number", "different atomic number", "different protons", "same number of neutrons", "same neutron number"], "Isotopes have the SAME proton number (same element); it is the NEUTRON number that differs.")],
           model_answer="Isotopes are atoms of the same element, with the same proton number, but different numbers of neutrons and hence different nucleon numbers.",
           hints=["Carbon-12 and carbon-14 are an example.", "What is the same about them?", "What is different?"],
           keywords="same proton number, different neutron (nucleon) number",
           sample_pass=["atoms of the same element with the same number of protons but different numbers of neutrons", "same proton number, different nucleon number"], sample_fail=["atoms with the same number of neutrons but different protons", "radioactive atoms"])

definition("d_rad_nuclide", "radio", 2, "16c",
           stem="State what is meant by a **nuclide**, and what the symbols in the nuclide notation ᴬ₂X mean.",
           points=[P("a nuclide is a particular (species of) nucleus with a specific number of protons and neutrons", ["specific number of protons and neutrons", "particular number of protons and neutrons", "specific proton number and nucleon number", "type of nucleus", "species of nucleus", "particular nucleus", "nucleus with a given number", "particular atom characterised by", "nucleus characterised by"]),
                   P("A (top) is the nucleon (mass) number; Z (bottom) is the proton (atomic) number; X is the chemical symbol", ["a is the nucleon number", "a is the mass number", "top number is the nucleon", "top is the nucleon", "a nucleon number", "z is the proton number", "z is the atomic number", "bottom number is the proton", "bottom is the proton", "z proton number", "x is the symbol", "x is the element"])],
           model_answer="A nuclide is a particular type of nucleus characterised by its numbers of protons and neutrons. In the notation ᴬ₂X, A is the nucleon (mass) number, Z is the proton (atomic) number and X is the chemical symbol of the element.",
           hints=["Examiners note students confuse nuclide, nucleus and isotope (2024).", "A nuclide is one specific kind of nucleus.", "Say what the top and bottom numbers stand for."],
           keywords="specific nucleus (given Z and A); A = nucleon number, Z = proton number",
           sample_pass=["a nuclide is a nucleus with a specific number of protons and neutrons; A is the nucleon number and Z is the proton number", "a particular type of nucleus; top number A is the mass number, bottom Z is the atomic number"],
           sample_fail=["a nuclide is a radioactive element", "A is the number of protons and Z is the number of neutrons"])

definition("d_rad_decay", "radio", 2, "16d",
           stem="State what is meant by **radioactive (nuclear) decay**.",
           points=[P("an unstable nucleus", ["unstable nucleus", "unstable nuclei", "unstable atom"]),
                   P("emits radiation (alpha, beta or gamma) and loses energy, becoming more stable", ["emits radiation", "emitting radiation", "gives out radiation", "releases radiation", "emits alpha", "emits beta", "emits gamma", "emits particles", "emits a particle", "loses energy by emitting", "becomes more stable", "emission of radiation"]),
                   P("the process is random and spontaneous", ["random", "spontaneous"])],
           min_points=2,
           model_answer="Radioactive decay is a random and spontaneous process in which an unstable nucleus loses energy by emitting radiation (an alpha particle, a beta particle and/or gamma rays) to become more stable.",
           hints=["Which kind of nucleus decays?", "What does it give out?", "Two adjectives describe the nature of the process: it cannot be predicted and it is not affected by outside conditions."],
           keywords="unstable nucleus emits radiation; random, spontaneous",
           sample_pass=["an unstable nucleus emits radiation to become more stable; the process is random and spontaneous", "the spontaneous emission of alpha, beta or gamma radiation by an unstable nucleus"],
           sample_fail=["an atom loses its electrons", "a nucleus splits into two when hit by a neutron"])

definition("d_rad_random_spontaneous", "radio", 3, "16d",
           stem="Radioactive decay is described as **random** and **spontaneous**. State what each word means.",
           points=[P("random: it cannot be predicted which nucleus will decay next or when a particular nucleus will decay", ["cannot be predicted", "cannot predict", "unpredictable", "impossible to predict", "not possible to predict", "no way of knowing which", "do not know when"]),
                   P("spontaneous: it is not affected by external conditions such as temperature, pressure or chemical state (happens by itself)", ["not affected by external", "not affected by temperature", "unaffected by", "independent of external", "cannot be influenced", "cannot be controlled", "cannot be speeded up", "happens by itself", "without any external", "not triggered", "of its own accord", "cannot be affected", "external conditions"])],
           model_answer="Random means it is impossible to predict which nucleus will decay next, or when a given nucleus will decay (only the probability is known). Spontaneous means the decay happens by itself and is not affected by external conditions such as temperature, pressure or chemical reactions.",
           hints=["Random is about prediction.", "Spontaneous is about outside influences.", "Give a meaning for each word separately."],
           keywords="random: unpredictable which/when; spontaneous: unaffected by external conditions",
           sample_pass=["random: you cannot predict which nucleus decays or when; spontaneous: it is not affected by temperature or pressure", "random means unpredictable; spontaneous means it happens by itself without external influence"],
           sample_fail=["random means it happens anywhere; spontaneous means it happens quickly", "both mean it is dangerous"])

definition("d_rad_alpha", "radio", 2, "16e",
           stem="State the nature of an **alpha** particle, its charge, and its ionising and penetrating abilities.",
           points=[P("a helium nucleus: 2 protons and 2 neutrons", ["helium nucleus", "2 protons and 2 neutrons", "two protons and two neutrons", "helium-4 nucleus", "4 2 he"]),
                   P("charge +2 (relatively massive)", ["+2", "positive", "two positive", "charge of 2"]),
                   P("strongly (most) ionising, least penetrating: stopped by a sheet of paper or a few cm of air", ["most ionising", "highly ionising", "strongly ionising", "very ionising", "least penetrating", "stopped by paper", "sheet of paper", "few cm of air", "few centimetres of air", "low penetrating"])],
           min_points=2,
           pitfalls=[PF(["electron", "electromagnetic wave"], "An alpha particle is a HELIUM NUCLEUS (2p + 2n). An electron is beta; an EM wave is gamma.")],
           model_answer="An alpha particle is a helium nucleus (2 protons + 2 neutrons), charge +2 and relatively heavy. It is the most strongly ionising radiation but the least penetrating: it is stopped by a sheet of paper or a few centimetres of air.",
           hints=["It is the heaviest of the three radiations.", "Which nucleus is it identical to?", "Heavy and charged means it ionises strongly but does not get far."],
           keywords="helium nucleus, +2; most ionising, least penetrating (paper)",
           sample_pass=["a helium nucleus with charge +2; highly ionising but stopped by paper", "2 protons and 2 neutrons, positive, most ionising and least penetrating"], sample_fail=["a fast electron with charge -1", "an electromagnetic wave with no charge"])

definition("d_rad_beta", "radio", 2, "16e",
           stem="State the nature of a **beta** particle, its charge, where it comes from, and its ionising and penetrating abilities.",
           points=[P("a fast-moving electron", ["electron", "fast moving electron", "high speed electron", "high-energy electron"]),
                   P("charge −1; emitted from the nucleus when a neutron changes into a proton (and an electron)", ["-1", "−1", "negative", "neutron changes into a proton", "neutron decays into a proton", "neutron turns into a proton", "neutron becomes a proton", "from the nucleus"]),
                   P("moderately ionising and moderately penetrating: stopped by a few mm of aluminium", ["moderately ionising", "less ionising than alpha", "medium ionising", "moderately penetrating", "few mm of aluminium", "few millimetres of aluminium", "aluminium", "more penetrating than alpha", "less penetrating than gamma"])],
           min_points=2,
           pitfalls=[PF(["from the electron shells", "orbital electron", "an electron from the shell", "electron from outside the nucleus"], "A beta particle comes from the NUCLEUS (a neutron turns into a proton + electron), not from the electron shells.")],
           model_answer="A beta particle is a fast-moving electron, charge −1, emitted from the nucleus when a neutron changes into a proton and an electron. It is less ionising than alpha but more penetrating: it is stopped by a few millimetres of aluminium.",
           hints=["It is a familiar particle moving very fast.", "It comes from the nucleus even though the nucleus contains no electrons: which particle changes?", "Compare its ionising and penetrating power with alpha."],
           keywords="fast electron, −1, from neutron -> proton; moderate ionising, stopped by few mm Al",
           sample_pass=["a fast-moving electron with charge -1, formed when a neutron in the nucleus becomes a proton; stopped by a few mm of aluminium", "high speed electron, negative, moderately ionising and penetrating"],
           sample_fail=["a helium nucleus with charge +2 stopped by paper", "an electron from the outer shell of the atom"])

definition("d_rad_gamma", "radio", 2, "16e",
           stem="State the nature of **gamma** radiation, its charge, and its ionising and penetrating abilities.",
           points=[P("an electromagnetic wave (photon) of very high frequency / short wavelength", ["electromagnetic wave", "electromagnetic radiation", "em wave", "em radiation", "photon", "high frequency wave", "short wavelength"]),
                   P("no charge (and no mass)", ["no charge", "uncharged", "neutral", "zero charge", "charge of 0", "not charged"]),
                   P("weakly (least) ionising, most penetrating: intensity reduced by several cm of lead or thick concrete", ["least ionising", "weakly ionising", "low ionising", "most penetrating", "highly penetrating", "very penetrating", "lead", "thick concrete", "several cm of lead", "few cm of lead"])],
           min_points=2,
           pitfalls=[PF(["is a particle", "helium nucleus", "electron"], "Gamma is a WAVE (electromagnetic), not a particle.")],
           model_answer="Gamma radiation is a high-frequency electromagnetic wave, with no charge and no mass. It is the least ionising but the most penetrating: its intensity is reduced only by several centimetres of lead or thick concrete.",
           hints=["It is the only one of the three that is not a particle.", "What kind of wave, and what charge does a wave carry?", "Not being charged, it ionises weakly but penetrates far."],
           keywords="EM wave, no charge; least ionising, most penetrating (lead)",
           sample_pass=["a high-frequency electromagnetic wave with no charge; least ionising and most penetrating, needs lead to absorb it", "EM radiation, uncharged, very penetrating but weakly ionising"], sample_fail=["a helium nucleus that is stopped by paper", "a fast electron with negative charge"])

definition("d_rad_ionising", "radio", 2, "16e",
           stem="State what is meant by **ionising** radiation.",
           points=[P("radiation that removes (knocks out) electrons from atoms / molecules", ["removes electrons", "knocks electrons", "knocks out electrons", "strips electrons", "remove electrons from atoms", "electrons are removed", "knock off electrons", "electrons out of atoms", "dislodge electrons"]),
                   P("turning them into (charged) ions", ["ions", "ionise", "ioniz", "charged particles", "charged atoms"])],
           model_answer="Ionising radiation has enough energy to knock electrons out of the atoms or molecules it passes through, leaving them as charged ions.",
           hints=["Ionising means making ions.", "An atom becomes an ion when it loses or gains ... ?", "Which does radiation do to the atoms it hits?"],
           keywords="knocks electrons off atoms, forming ions",
           sample_pass=["radiation that knocks electrons out of atoms, forming ions", "it removes electrons from atoms so they become charged ions"], sample_fail=["radiation that is radioactive", "radiation that heats things up"])

definition("d_rad_background", "radio", 2, "16f",
           stem="State what is meant by **background radiation**, and give two sources.",
           points=[P("the (low-level) ionising radiation that is always present in the environment / surroundings, even with no radioactive source nearby", ["always present", "present all the time", "constantly present", "always around us", "present in the environment", "present in the surroundings", "naturally present", "all around us", "everywhere", "from the surroundings", "from the environment", "even when there is no source", "without a source", "in the absence of a source"]),
                   P("sources: rocks and soil, radon gas, cosmic rays, food and drink, medical X-rays, nuclear industry / fallout, building materials", ["rocks", "soil", "ground", "radon", "cosmic", "space", "sun", "food", "medical", "x-ray", "x ray", "nuclear", "fallout", "building materials", "granite"])],
           pitfalls=[PF(["radiation from the sample", "radiation from the source being measured"], "Background radiation is what is there WITHOUT the source: it must be subtracted from the measured count rate.")],
           model_answer="Background radiation is the low-level ionising radiation that is present in the environment all the time, even when no radioactive source is nearby. Sources include radioactive rocks and soil, radon gas in the air, cosmic rays from space, food and drink, medical X-rays and the nuclear industry.",
           hints=["A Geiger counter clicks even with no source nearby.", "Define it generally first (examiner report 2024), then give sources.", "Natural sources: rocks, air, space, food."],
           keywords="radiation always present in the surroundings; rocks, radon, cosmic rays",
           sample_pass=["low-level radiation that is always present in the environment, e.g. from rocks and cosmic rays", "the radiation detected even when no source is present, coming from radon gas and the ground"],
           sample_fail=["radiation from the back of the source", "cosmic rays"])

definition("d_rad_half_life", "radio", 2, "16g",
           stem="State what is meant by the **half-life** of a radioactive isotope.",
           points=[P("the time taken", ["time taken", "time for", "time it takes", "time needed", "time required", "average time", "time"]),
                   P("for half of the (number of) unstable nuclei / atoms in a sample to decay, or for the activity (count rate) to fall to half its original value", ["half the nuclei to decay", "half of the nuclei to decay", "half of the unstable nuclei", "half the atoms to decay", "half of the atoms to decay", "half the radioactive nuclei", "half of the radioactive nuclei", "number of nuclei to halve", "number of undecayed nuclei to halve", "activity to halve", "activity to fall to half", "activity to drop to half", "activity to decrease to half", "count rate to halve", "count rate to fall to half", "count rate to drop to half", "activity to reduce to half", "half of its original activity", "half its initial activity", "half of the original number", "half the original number of nuclei", "half of the sample to decay", "half the nuclei in a sample to decay", "half the radioactive atoms to decay", "half of the nuclei have decayed", "half the nuclei have decayed", "number of nuclei to fall to half", "number of nuclei to halve", "nuclei to decrease to half"])],
           pitfalls=[PF(["a nucleus to halve", "nucleus to halve", "nucleus to decay by half", "half of a nucleus", "atom to lose half its mass", "lose half its mass", "half of its mass", "half the mass to decay", "mass to halve", "half of the mass"], "A nucleus does not 'halve' and the mass does not disappear (examiner report 2024). Half-life is the time for half the NUMBER of unstable nuclei to decay (or the activity to halve)."),
                     PF(["half of the radiation", "half the radiation to"], "Say half the number of undecayed NUCLEI, or half the ACTIVITY (count rate), not 'half the radiation'.")],
           model_answer="The half-life is the time taken for half of the unstable nuclei in a sample to decay, which is also the time for the activity (count rate) of the sample to fall to half its original value.",
           hints=["It is a time.", "The time for half of what to happen?", "Count nuclei (or measure activity), not mass."],
           keywords="time for half the nuclei to decay / activity to halve",
           sample_pass=["the time taken for half the unstable nuclei in a sample to decay", "the time for the activity to fall to half its original value"],
           sample_fail=["the time for a nucleus to halve", "the time for an atom to lose half its mass"])

definition("d_rad_fission", "radio", 3, "20j",
           stem="State what is meant by **nuclear fission**.", syllabi=PURE,
           points=[P("a heavy (large, unstable) nucleus splits into two lighter nuclei (usually after absorbing a neutron)", ["heavy nucleus splits", "large nucleus splits", "nucleus splits into two", "splits into two smaller nuclei", "splits into two lighter", "splitting of a heavy nucleus", "heavy nucleus breaks up", "divides into two", "split into two", "breaks into two smaller", "uranium nucleus splits"]),
                   P("releasing energy (and neutrons)", ["releasing energy", "releases energy", "energy is released", "release of energy", "gives out energy", "large amount of energy", "energy released"])],
           pitfalls=[PF(["nuclei join", "nuclei combine", "two nuclei fuse", "light nuclei"], "Joining nuclei is FUSION. Fission is a heavy nucleus SPLITTING.")],
           model_answer="Nuclear fission is the splitting of a heavy, unstable nucleus (such as uranium-235, usually after absorbing a neutron) into two lighter nuclei, with the release of a large amount of energy and some neutrons.",
           hints=["Fission sounds like 'fissure': a split.", "What kind of nucleus, and what does it split into?", "What comes out along with the fragments?"],
           keywords="heavy nucleus splits into two lighter nuclei; energy released",
           sample_pass=["a heavy nucleus splits into two lighter nuclei, releasing energy", "the splitting of a large unstable nucleus such as uranium into smaller nuclei with release of energy and neutrons"],
           sample_fail=["two light nuclei join to form a heavier nucleus releasing energy", "a nucleus emits an alpha particle"])

definition("d_rad_fusion", "radio", 3, "20j",
           stem="State what is meant by **nuclear fusion**.", syllabi=PURE,
           points=[P("two light nuclei join (combine) to form a heavier nucleus", ["light nuclei join", "light nuclei combine", "light nuclei fuse", "small nuclei join", "two nuclei combine", "two nuclei join", "two nuclei fuse", "nuclei join together", "nuclei combine to form a heavier", "form a heavier nucleus", "form a larger nucleus", "hydrogen nuclei join", "hydrogen nuclei combine", "join to form"]),
                   P("releasing energy (needs very high temperature and pressure, as in the Sun)", ["releasing energy", "releases energy", "energy is released", "release of energy", "gives out energy", "large amount of energy", "energy released"])],
           pitfalls=[PF(["nucleus splits", "splitting", "splits into"], "Splitting is FISSION. Fusion is light nuclei JOINING.")],
           model_answer="Nuclear fusion is the joining of two light nuclei (such as hydrogen isotopes) to form a heavier nucleus, with the release of a large amount of energy. It needs extremely high temperatures and pressures, as in the Sun.",
           hints=["Fusion means joining together.", "What kind of nuclei, and what do they form?", "What is released?"],
           keywords="light nuclei join to form heavier nucleus; energy released",
           sample_pass=["two light nuclei join to form a heavier nucleus, releasing energy", "hydrogen nuclei combine into helium with the release of energy, as in the Sun"],
           sample_fail=["a heavy nucleus splits into two releasing energy", "atoms join to make molecules"])

definition("d_rad_hazards_uses", "radio", 3, "16h",
           stem="State **one hazard** of ionising radiation to the body and **two uses** of radioactive isotopes.",
           points=[P("hazard: ionisation damages or kills cells / damages DNA, causing mutations, cancer, radiation burns or sickness", ["damage cells", "kills cells", "kill cells", "damage dna", "mutation", "cancer", "radiation burns", "radiation sickness", "cell damage", "harm living"]),
                   P("uses: medical (tracers, sterilising equipment, radiotherapy / cancer treatment), industrial (thickness gauging, leak detection, sterilising food), smoke detectors, carbon dating, nuclear power", ["tracer", "steril", "radiotherapy", "treat cancer", "cancer treatment", "kill cancer", "thickness", "leak", "smoke detector", "smoke alarm", "carbon dating", "dating", "power", "medical imaging", "detect leaks", "food irradiation"])],
           model_answer="Hazard: ionising radiation damages or kills living cells and can alter DNA, causing mutations and cancer (high doses cause radiation burns and sickness). Uses: medical tracers and radiotherapy for cancer, sterilising medical equipment and food, thickness gauging and leak detection in industry, smoke detectors, carbon dating, and generating electricity in nuclear power stations.",
           hints=["Hazard: what does ionisation do to a living cell?", "Uses: hospitals, factories, your ceiling.", "Give one hazard and two uses."],
           keywords="hazard: cell/DNA damage, cancer; uses: tracers, radiotherapy, sterilising, thickness gauge, smoke detector, dating",
           sample_pass=["it can damage cells and cause cancer; used in smoke detectors and for sterilising medical equipment", "mutations in DNA; uses include radiotherapy and thickness gauging"],
           sample_fail=["it makes you glow; used in torches", "it is hot"])

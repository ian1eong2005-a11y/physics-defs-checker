"""Formulae from the 6091 / 5086 syllabuses. Each item lists accepted forms (any rearrangement listed is accepted; the
checker also accepts either side of the = first) and known wrong forms with a one-line message.
Level 1: core formulae. Level 2: the rest. Level 3: rearranged subjects. Level 4: combined / derived."""
from .base import BOTH, PURE, formula

# ================================================================= L1  core
formula("f_speed", "kin", 1, "2b", "Write the formula for **average speed**.",
        forms=["v = d/t", "speed = distance/time", "average speed = distance travelled / time taken", "s = d/t", "v = s/t", "speed = distance travelled / time taken", "average speed = distance / time", "average speed = total distance / total time", "v = x/t"],
        answer="average speed = distance travelled ÷ time taken  (v = d / t)", symbols="",
        wrongs={"v = t/d": "Upside down: speed is distance divided by time.", "speed = time/distance": "Upside down: speed is distance divided by time.", "v = dt": "Distance divided by time, not multiplied."},
        hints=["Speed is 'how far per how long'.", "Two quantities: a distance and a time.", "Which one is divided by which? Think of km per hour."],
        keywords="distance, time", sample_pass=["speed = distance / time", "v = d/t", "average speed = total distance / total time"], sample_fail=["v = dt", "d = vt^2"])

formula("f_acceleration", "kin", 1, "2c", "Write the formula for **acceleration** in terms of initial velocity u, final velocity v and time t.",
        forms=["a = (v-u)/t", "a = (v - u)/t", "a = delta v / t", "a = Δv/t", "a = change in velocity / time", "acceleration = change in velocity / time taken", "a = (v-u)/t"],
        answer="a = (v − u) / t", symbols="u is the initial velocity, v the final velocity",
        wrongs={"a = v/t": "That is only right when the object starts from rest (u = 0). In general a = (v − u)/t.", "a = (u-v)/t": "Final minus initial: a = (v − u)/t.", "a = (v-u)t": "Divide the change in velocity by the time, not multiply."},
        hints=["Acceleration is the rate of change of velocity.", "Change in velocity means final minus initial.", "Then divide by the time taken."],
        keywords="change in velocity, time", sample_pass=["a = (v-u)/t", "a = (v − u) ÷ t", "a = Δv / t"], sample_fail=["a = v/t", "a = (v-u)t"])

formula("f_weight", "mwg", 1, "3e", "Write the formula for **weight**.",
        forms=["W = mg", "weight = mass × gravitational field strength", "weight = mass x g", "W = m g", "weight = mg", "w = m*g"],
        answer="W = mg", symbols="g is the gravitational field strength (10 N/kg on Earth)",
        wrongs={"w = m/g": "Multiply: weight = mass × g.", "w = g/m": "Weight = mass × g.", "w = ma": "a is a general acceleration; weight uses the gravitational field strength g."},
        hints=["Weight is the gravitational force on a mass.", "It depends on the mass and on the strength of gravity.", "Multiply the two."],
        keywords="mass, gravitational field strength", sample_pass=["W = mg", "weight = mass × g", "W = m × g"], sample_fail=["W = m/g", "W = ma"])

formula("f_newton2", "newton", 1, "4c", "Write the formula relating **resultant force**, mass and acceleration.",
        forms=["F = ma", "resultant force = mass × acceleration", "F = m a", "a = F/m", "force = mass x acceleration", "Fnet = ma", "F net = ma", "F_net = ma", "Fr = ma"],
        answer="F = ma", symbols="F is the resultant (net) force",
        wrongs={"f = m/a": "Multiply: F = m × a.", "f = a/m": "F = m × a.", "f = mv": "mv is momentum (not in this syllabus). Force = mass × acceleration.", "f = mg": "mg is the weight, a special case. In general F = ma, with a the acceleration."},
        hints=["Newton's second law.", "A bigger mass needs a bigger force for the same acceleration.", "Multiply mass by acceleration."],
        keywords="mass, acceleration", sample_pass=["F = ma", "F = m × a", "a = F/m"], sample_fail=["F = m/a", "F = mv"])

formula("f_moment", "moments", 1, "5b", "Write the formula for the **moment of a force**.",
        forms=["moment = F × d", "moment = Fd", "M = Fd", "moment = force × perpendicular distance", "moment = force × perpendicular distance from pivot", "moment = F d", "M = F × d", "moment = F × d⊥", "torque = Fd", "moment of a force = force × perpendicular distance from the pivot", "moment = f x d", "moment = force x distance"],
        answer="moment = F × d", symbols="d is the perpendicular distance from the pivot to the line of action of the force",
        wrongs={"moment = f/d": "Multiply: moment = force × perpendicular distance.", "m = f/d": "Multiply: moment = force × perpendicular distance.", "moment = d/f": "moment = F × d."},
        hints=["A moment is a turning effect: it grows with the force and with the lever arm.", "Two quantities multiplied.", "The distance must be perpendicular from the pivot to the line of action."],
        keywords="force, perpendicular distance", sample_pass=["moment = F × d", "moment = Fd", "M = F d"], sample_fail=["moment = F/d", "moment = F + d"])

formula("f_pressure", "pressure", 1, "3i", "Write the formula for **pressure**.",
        forms=["p = F/A", "P = F/A", "pressure = force/area", "pressure = force / area", "p = f/a", "F = pA"],
        answer="p = F / A", symbols="F is the force acting perpendicular to the surface of area A",
        wrongs={"p = fa": "Divide: pressure = force ÷ area. A bigger area gives a smaller pressure.", "p = a/f": "Upside down: p = F/A."},
        hints=["Pressure is force per unit area.", "'Per unit area' means divide by area.", "p = ... / ..."],
        keywords="force, area", sample_pass=["p = F/A", "pressure = force ÷ area", "P = F / A"], sample_fail=["p = FA", "p = A/F"])

formula("f_density", "pressure", 1, "3g", "Write the formula for **density**.",
        forms=["ρ = m/V", "rho = m/V", "density = mass/volume", "density = mass / volume", "D = m/V", "d = m/v", "p = m/v", "m = ρV"],
        answer="ρ = m / V", symbols="ρ (rho) is the density",
        wrongs={"rho = v/m": "Upside down: density = mass ÷ volume.", "rho = mv": "Divide: density = mass ÷ volume.", "d = v/m": "Upside down: density = mass ÷ volume."},
        hints=["Density is mass per unit volume.", "'Per unit volume' means divide by volume.", "The symbol for density is the Greek letter rho (ρ)."],
        keywords="mass, volume", sample_pass=["ρ = m/V", "density = mass/volume", "rho = m / V"], sample_fail=["ρ = V/m", "ρ = mV"])

formula("f_work", "energy", 1, "6d", "Write the formula for **work done** by a force.",
        forms=["W = Fd", "W = Fs", "W = F × d", "W = F d", "work done = force × distance", "work done = force × distance moved in the direction of the force", "work = force x distance", "W = F x d", "E = Fd", "W = F s", "work done = Fd", "work done = Fs", "WD = Fd", "WD = Fs"],
        answer="W = F × d", symbols="d is the distance moved in the direction of the force",
        wrongs={"w = f/d": "Multiply: work = force × distance.", "w = ft": "Force × TIME is not work. Work = force × distance.", "w = mg": "mg is weight. Work done = force × distance moved."},
        hints=["Work is done when a force moves something.", "It depends on the force and how far the object moves.", "Multiply them (distance in the direction of the force)."],
        keywords="force, distance", sample_pass=["W = Fd", "work done = force × distance", "W = F s"], sample_fail=["W = F/d", "W = Ft"])

formula("f_power", "energy", 1, "6e", "Write the formula for **power**.",
        forms=["P = W/t", "P = E/t", "power = work done / time", "power = energy / time", "power = work done / time taken", "power = energy transferred / time taken", "power = energy transferred / time", "P = energy transferred / time taken", "P = energy transferred / time", "P = work done / time", "P = energy/time", "P = WD/t", "P = E / t", "power = rate of work done"],
        answer="P = W / t  (or P = E / t)", symbols="W is the work done (energy transferred) in time t",
        wrongs={"p = wt": "Divide: power = work done ÷ time.", "p = et": "Divide: power = energy ÷ time.", "p = t/w": "Upside down: P = W/t.", "p = fd": "That is work done. Power = work done ÷ time."},
        hints=["Power is the rate of doing work.", "'Rate' means per unit time.", "Energy or work divided by time."],
        keywords="work done / energy, time", sample_pass=["P = W/t", "P = E/t", "power = energy transferred / time"], sample_fail=["P = Wt", "P = Fd"])

formula("f_ke", "energy", 1, "6b", "Write the formula for **kinetic energy**.",
        forms=["Ek = ½mv²", "KE = ½mv²", "Ek = 1/2 mv^2", "KE = 1/2 m v^2", "E = ½mv²", "Ek = 0.5mv²", "KE = 0.5 m v^2", "kinetic energy = ½ × mass × velocity²", "Ek = mv²/2", "KE = mv^2/2", "Ek = (1/2)mv^2", "E_k = 1/2 m v^2", "ke = half m v squared", "kinetic energy = 1/2 mv^2"],
        answer="Ek = ½ m v²", symbols="v is the speed of the body",
        wrongs={"ek = mv2": "You have left out the ½: Ek = ½mv².", "ke = mv2": "You have left out the ½: Ek = ½mv².", "ek = 1/2mv": "The speed is SQUARED: Ek = ½mv².", "ke = 1/2mv": "The speed is SQUARED: Ek = ½mv².", "ek = 1/2m2v": "It is the velocity that is squared, not the mass.", "ke = mgh": "mgh is gravitational potential energy."},
        hints=["Kinetic energy depends on mass and speed.", "The speed appears squared.", "There is a factor of a half in front."],
        keywords="½, mass, velocity squared", sample_pass=["Ek = ½mv²", "KE = 1/2 m v^2", "KE = 0.5mv2"], sample_fail=["KE = mv²", "KE = ½mv"])

formula("f_gpe", "energy", 1, "6b", "Write the formula for **gravitational potential energy** near the Earth's surface.",
        forms=["Ep = mgh", "GPE = mgh", "PE = mgh", "E = mgh", "gravitational potential energy = mass × g × height", "E_p = mgh", "Ep = m g h", "GPE = m × g × h", "gpe = mass x gravitational field strength x height"],
        answer="Ep = m g h", symbols="h is the height above the reference level, g the gravitational field strength",
        wrongs={"ep = mg": "You need the height: Ep = mgh.", "gpe = mg": "You need the height: Ep = mgh.", "ep = mh": "You need g as well: Ep = mgh.", "ep = 1/2mv2": "That is kinetic energy. Ep = mgh.", "ep = mgh2": "Height is not squared: Ep = mgh."},
        hints=["It is energy due to height.", "It equals the work done lifting the object: weight × height.", "Weight is mg."],
        keywords="mass, g, height", sample_pass=["Ep = mgh", "GPE = m g h", "PE = mgh"], sample_fail=["Ep = mg", "Ep = ½mv²"])

formula("f_wave_speed", "waves", 1, "9d", "Write the **wave equation** relating speed, frequency and wavelength.",
        forms=["v = fλ", "v = f λ", "v = f × λ", "speed = frequency × wavelength", "v = f lambda", "wave speed = frequency x wavelength", "c = fλ", "v = λf", "v = lambda f", "v = λ × f"],
        answer="v = f λ", symbols="λ (lambda) is the wavelength, f the frequency",
        wrongs={"v = f/lambda": "Multiply: v = f × λ.", "v = lambda/f": "Multiply: v = f × λ. (λ/f would be wavelength ÷ frequency.)", "v = f/t": "Use wavelength, not time: v = fλ."},
        hints=["How far a wave travels per second = how many waves per second × length of each wave.", "Frequency times wavelength.", "The symbol for wavelength is λ (lambda)."],
        keywords="frequency, wavelength", sample_pass=["v = fλ", "v = f × λ", "speed = frequency × wavelength"], sample_fail=["v = f/λ", "v = λ/f"])

formula("f_frequency_period", "waves", 1, "9c", "Write the formula relating **frequency** and **period**.",
        forms=["f = 1/T", "T = 1/f", "frequency = 1 / period", "f = 1/t", "fT = 1", "period = 1/frequency"],
        answer="f = 1 / T", symbols="T is the period (time for one complete wave)",
        wrongs={"f = t": "Frequency is the RECIPROCAL of the period: f = 1/T.", "f = 1/lambda": "That is not the period. f = 1/T.", "f = v/t": "Mixing formulas. f = 1/T (or f = v/λ)."},
        hints=["If one wave takes 0.5 s, how many waves per second?", "Frequency and period are reciprocals.", "f = 1 / ..."],
        keywords="period", sample_pass=["f = 1/T", "T = 1/f", "frequency = 1/period"], sample_fail=["f = T", "f = T/1"])

formula("f_charge", "current", 1, "12e", "Write the formula relating **charge**, current and time.",
        forms=["Q = It", "Q = I t", "charge = current × time", "Q = I × t", "I = Q/t", "q = it", "charge = current x time", "current = charge/time"],
        answer="Q = I t", symbols="Q is the charge in coulombs",
        wrongs={"q = i/t": "Multiply: Q = I × t. (Current is charge ÷ time, so charge = current × time.)", "q = t/i": "Q = It.", "i = qt": "Current = charge ÷ time, so Q = It."},
        hints=["Current is the rate of flow of charge: I = Q/t.", "Rearrange to make Q the subject.", "Charge = current × time."],
        keywords="current, time", sample_pass=["Q = It", "Q = I × t", "I = Q/t"], sample_fail=["Q = I/t", "I = Qt"])

formula("f_resistance", "current", 1, "12i", "Write the formula relating **resistance**, potential difference and current.",
        forms=["R = V/I", "V = IR", "I = V/R", "resistance = p.d. / current", "resistance = potential difference / current", "resistance = voltage / current", "r = v/i", "V = I R", "V = I × R"],
        answer="R = V / I  (V = IR)", symbols="",
        wrongs={"r = i/v": "Upside down: R = V ÷ I.", "r = vi": "Divide: R = V ÷ I. (V × I is power.)", "v = i/r": "V = I × R."},
        hints=["Resistance is the ratio of p.d. to current.", "Ratio means divide.", "R = V ÷ ..."],
        keywords="p.d., current", sample_pass=["R = V/I", "V = IR", "I = V/R"], sample_fail=["R = I/V", "R = VI"])

formula("f_power_electrical", "practical", 1, "14b", "Write the formula for **electrical power** in terms of potential difference and current.",
        forms=["P = VI", "P = IV", "power = p.d. × current", "power = voltage × current", "P = V × I", "P = V I", "power = potential difference x current"],
        answer="P = V I", symbols="",
        wrongs={"p = v/i": "Multiply: P = V × I.", "p = i/v": "Multiply: P = V × I.", "p = vit": "V I t is the ENERGY. Power = V I.", "p = ir": "I R is the p.d. Power = V I (or I²R)."},
        hints=["Electrical power depends on p.d. and current.", "Energy per coulomb × coulombs per second = energy per second.", "Multiply V and I."],
        keywords="p.d., current", sample_pass=["P = VI", "P = IV", "P = V × I"], sample_fail=["P = V/I", "P = VIt"])

formula("f_energy_electrical", "practical", 1, "14b", "Write the formula for **electrical energy** transferred in terms of potential difference, current and time.",
        forms=["E = VIt", "E = IVt", "energy = p.d. × current × time", "E = V I t", "E = Pt", "E = P t", "energy = power × time", "W = VIt", "E = V × I × t", "energy = voltage x current x time"],
        answer="E = V I t  (= P t)", symbols="",
        wrongs={"e = vi": "V I is the POWER. Energy = V I t.", "e = vi/t": "Multiply by time: E = V I t.", "e = it": "I t is the CHARGE. Energy = V I t.", "e = p/t": "Energy = power × time."},
        hints=["Energy = power × time.", "Power is V I.", "So energy = V I × ..."],
        keywords="p.d., current, time", sample_pass=["E = VIt", "E = Pt", "energy = power × time"], sample_fail=["E = VI", "E = It"])

formula("f_series_resistance", "dc", 1, "13f", "Write the formula for the **effective resistance** of resistors in **series**.",
        forms=["R = R1 + R2", "R = R1 + R2 + R3", "R = R₁ + R₂", "Rt = R1 + R2", "R total = R1 + R2", "R_T = R1 + R2 + R3", "Reff = R1 + R2", "R eff = R1 + R2", "RT = R1 + R2", "R = R1 + R2 + ...", "Rtotal = R1 + R2"],
        answer="R = R₁ + R₂ (+ R₃ …)", symbols="",
        wrongs={"1/r = 1/r1 + 1/r2": "That is the PARALLEL formula. In series the resistances simply add.", "r = r1r2/r1+r2": "That is for two resistors in PARALLEL. In series R = R₁ + R₂.", "r = 1/r1 + 1/r2": "In series the resistances add directly: R = R₁ + R₂."},
        hints=["In series the current passes through each resistor in turn.", "Each one adds its own resistance.", "Just add them."],
        keywords="add the resistances", sample_pass=["R = R1 + R2", "R = R₁ + R₂ + R₃", "Rt = R1 + R2"], sample_fail=["1/R = 1/R1 + 1/R2", "R = R1 × R2"])

formula("f_parallel_resistance", "dc", 2, "13f", "Write the formula for the **effective resistance** of two resistors in **parallel**.",
        forms=["1/R = 1/R1 + 1/R2", "1/R = 1/R₁ + 1/R₂", "R = R1R2/(R1+R2)", "R = (R1 R2)/(R1 + R2)", "R = R1 × R2 / (R1 + R2)", "1/Rt = 1/R1 + 1/R2", "1/R total = 1/R1 + 1/R2", "1/R_T = 1/R1 + 1/R2", "1/Reff = 1/R1 + 1/R2", "1/RT = 1/R1 + 1/R2", "1/R = 1/R1 + 1/R2 + 1/R3", "R = R1R2/R1+R2", "1/Rtotal = 1/R1 + 1/R2"],
        answer="1/R = 1/R₁ + 1/R₂  (for two resistors, R = R₁R₂ / (R₁ + R₂))", symbols="",
        wrongs={"r = 1/r1 + 1/r2": "The LEFT side must also be a reciprocal: 1/R = 1/R₁ + 1/R₂ (examiner report 2018: a common slip). Do not forget to invert at the end.", "rt = 1/r1 + 1/r2": "The left side must also be a reciprocal: 1/R = 1/R₁ + 1/R₂.", "r = r1 + r2": "That is SERIES. In parallel, 1/R = 1/R₁ + 1/R₂.", "r = r1+r2/r1r2": "Upside down: R = R₁R₂ / (R₁ + R₂)."},
        hints=["In parallel the combined resistance is LESS than the smallest branch.", "It is the reciprocals that add.", "1/R = 1/R₁ + ... (and invert at the end)."],
        keywords="reciprocals add", sample_pass=["1/R = 1/R1 + 1/R2", "R = R1R2/(R1+R2)", "1/R = 1/R₁ + 1/R₂"], sample_fail=["R = 1/R1 + 1/R2", "R = R1 + R2"])

# ================================================================= L2  the rest
formula("f_g_field", "mwg", 2, "3d", "Write the formula for **gravitational field strength** in terms of weight and mass.",
        forms=["g = W/m", "g = F/m", "gravitational field strength = weight / mass", "g = w/m", "g = weight/mass", "W = mg"],
        answer="g = W / m", symbols="W is the weight (gravitational force) on the mass m",
        wrongs={"g = m/w": "Upside down: g = W/m (force per unit mass).", "g = wm": "Divide: g = W/m."},
        hints=["g is the gravitational force per unit mass.", "'Per unit mass' means divide by mass.", "g = weight ÷ ..."],
        keywords="weight, mass", sample_pass=["g = W/m", "g = F/m", "g = weight ÷ mass"], sample_fail=["g = m/W", "g = Wm"])

formula("f_liquid_pressure", "pressure", 2, "5e", "Write the formula for the **pressure due to a column of liquid**.", syllabi=PURE,
        forms=["p = hρg", "p = ρgh", "p = h ρ g", "P = hρg", "p = rho g h", "p = h rho g", "pressure = height × density × g", "pressure = height x density x gravitational field strength", "p = ρ g h", "p = gρh", "p = g rho h", "p = hgρ", "p = h g rho", "p = ρhg", "p = rho h g", "p = ghρ"],
        answer="p = h ρ g", symbols="h is the depth (height of the column), ρ the density of the liquid",
        wrongs={"p = h/rhog": "Multiply all three: p = hρg.", "p = rhog/h": "Multiply: p = hρg.", "p = rhogv": "Volume does not come into it: p = hρg.", "p = mgh": "mgh is gravitational potential energy. Liquid pressure is hρg."},
        hints=["Pressure in a liquid increases with depth and with density.", "Three quantities multiplied.", "height × density × g."],
        keywords="height, density, g", sample_pass=["p = hρg", "p = ρgh", "P = h × ρ × g"], sample_fail=["p = h/ρg", "p = mgh"])

formula("f_efficiency", "energy", 2, "6f", "Write the formula for **efficiency**.", syllabi=PURE,
        forms=["efficiency = useful energy output / total energy input × 100%", "efficiency = useful energy output / total energy input", "efficiency = useful output / total input × 100%", "efficiency = useful output / total input", "efficiency = useful power output / total power input × 100%", "efficiency = useful power output / total power input", "efficiency = useful energy output / total energy input x 100", "efficiency = useful output/total input x 100", "efficiency = useful energy output ÷ total energy input × 100%", "efficiency = (useful energy output / total energy input) × 100%", "efficiency = useful work output / total energy input × 100%", "efficiency = useful energy output / energy input × 100%", "efficiency = useful energy output / total energy input * 100%"],
        answer="efficiency = (useful energy output ÷ total energy input) × 100%", symbols="(power may replace energy)",
        wrongs={"efficiency = energy output/energy input": "Say USEFUL output and TOTAL input (examiner report 2020): without 'useful' it is always 100%.", "efficiency = output/input": "Say USEFUL output and TOTAL input.", "efficiency = total energy output/total energy input": "Total output ÷ total input is always 100%. It must be USEFUL output.", "efficiency = total energy input/useful energy output": "Upside down: useful output ÷ total input."},
        hints=["It compares what you get out usefully with what you put in.", "A fraction, usually as a percentage.", "USEFUL energy output on top, TOTAL energy input below."],
        keywords="useful output, total input, × 100%", sample_pass=["efficiency = useful energy output / total energy input × 100%", "efficiency = useful power output / total power input x 100%"], sample_fail=["efficiency = output / input", "efficiency = total energy output / total energy input"])

formula("f_shc", "thermal_props", 2, "9c", "Write the formula for the **thermal energy** needed to change the temperature of a body (specific heat capacity).", syllabi=PURE,
        forms=["Q = mcΔθ", "Q = mcΔT", "E = mcΔθ", "E = mcΔT", "Q = m c Δθ", "Q = mc delta theta", "Q = mc delta T", "E = mc(θ2 - θ1)", "Q = mc(T2 - T1)", "Q = mc(θ₂−θ₁)", "energy = mass × specific heat capacity × change in temperature", "Q = m c (T2-T1)", "E = m c Δθ", "E = mc delta T", "Q = mcθ", "Q = mcT"],
        answer="Q = m c Δθ", symbols="c is the specific heat capacity, Δθ the change in temperature",
        wrongs={"q = mc": "You need the temperature change: Q = mcΔθ.", "q = ml": "ml is for a change of STATE (latent heat). For a temperature change use Q = mcΔθ.", "q = cdeltatheta": "Mass is missing: Q = mcΔθ.", "q = mdeltatheta": "Specific heat capacity c is missing: Q = mcΔθ."},
        hints=["Energy to heat something depends on how much there is, what it is made of, and how much hotter it gets.", "mass × specific heat capacity × ...", "The last factor is the change in temperature."],
        keywords="mass, specific heat capacity, temperature change", sample_pass=["Q = mcΔθ", "E = mcΔT", "Q = mc(T2 - T1)"], sample_fail=["Q = mc", "Q = ml"])

formula("f_slh", "thermal_props", 2, "9g", "Write the formula for the **thermal energy** needed to change the state of a substance (specific latent heat).", syllabi=PURE,
        forms=["Q = ml", "E = ml", "Q = mL", "E = mL", "Q = m l", "energy = mass × specific latent heat", "Q = m × l", "E = m × L", "Q = mlf", "Q = mlv", "Q = m l_f", "Q = m l_v"],
        answer="Q = m l", symbols="l is the specific latent heat (of fusion or vaporisation)",
        wrongs={"q = mcdeltatheta": "mcΔθ is for a TEMPERATURE change. For a change of state at constant temperature use Q = ml.", "q = mldeltatheta": "No temperature change during a change of state: Q = ml.", "q = m/l": "Multiply: Q = ml.", "q = l/m": "Q = ml."},
        hints=["No temperature change, so no Δθ.", "Energy to change state depends only on the mass and the type of substance.", "mass × specific latent heat."],
        keywords="mass, specific latent heat", sample_pass=["Q = ml", "E = mL", "energy = mass × specific latent heat"], sample_fail=["Q = mcΔθ", "Q = m/l"])

formula("f_heat_capacity", "thermal_props", 2, "9b", "Write the formula relating **heat capacity** C to specific heat capacity c and mass m.", syllabi=PURE,
        forms=["C = mc", "C = m c", "heat capacity = mass × specific heat capacity", "C = m × c"],
        answer="C = m c", symbols="C is the heat capacity (J/K), c the specific heat capacity (J/(kg K))",
        wrongs={"c = m/c": "Multiply: C = m × c."},
        hints=["Specific heat capacity is per kilogram; heat capacity is for the whole body.", "So multiply by the mass.", "C = m × ..."],
        keywords="mass, specific heat capacity", sample_pass=["C = mc", "heat capacity = mass × specific heat capacity"], sample_fail=["C = m/c", "C = mcΔθ"])

formula("f_snell", "light", 2, "11d", "Write the formula for **refractive index** in terms of the angles of incidence and refraction.",
        forms=["n = sin i / sin r", "n = sin i/sin r", "n = sini/sinr", "refractive index = sin i / sin r", "n = sin(i)/sin(r)", "sin i / sin r = constant", "sin i/sin r = n", "sin i / sin r = constant"],
        answer="n = sin i / sin r", symbols="i is the angle of incidence (in air/vacuum), r the angle of refraction (in the medium)",
        wrongs={"n = sinr/sini": "Upside down: n = sin i / sin r (with i in air), so n > 1.", "n = i/r": "Use the SINES of the angles: n = sin i / sin r.", "n = sini sinr": "Divide: n = sin i / sin r."},
        hints=["Snell's law: a ratio of two sines is constant.", "Angle of incidence on top.", "n = sin ... / sin ..."],
        keywords="sin i, sin r", sample_pass=["n = sin i / sin r", "n = sin(i)/sin(r)", "sin i / sin r = constant"], sample_fail=["n = sin r / sin i", "n = i/r"])

formula("f_refractive_speed", "light", 2, "11e", "Write the formula for **refractive index** in terms of the speed of light.",
        forms=["n = c/v", "n = c / v", "refractive index = speed of light in vacuum / speed of light in medium", "n = speed in vacuum / speed in medium", "n = c/v", "refractive index = speed of light in a vacuum / speed of light in the medium", "n = speed of light in vacuum / speed of light in medium"],
        answer="n = c / v", symbols="c is the speed of light in a vacuum (3 × 10⁸ m/s), v its speed in the medium",
        wrongs={"n = v/c": "Upside down (examiner report 2020): n = c/v, speed in VACUUM over speed in MEDIUM, so n > 1.", "n = cv": "Divide: n = c/v."},
        hints=["It is a ratio of two speeds.", "Light is fastest in a vacuum, and n must be greater than 1.", "So the vacuum speed goes on top."],
        keywords="speed in vacuum, speed in medium", sample_pass=["n = c/v", "n = speed in vacuum / speed in medium"], sample_fail=["n = v/c", "n = cv"])

formula("f_critical_angle", "light", 2, "12f", "Write the formula relating the **critical angle** c to the refractive index n.", syllabi=PURE,
        forms=["sin c = 1/n", "n = 1/sin c", "sin c = 1 / n", "sinc = 1/n", "n = 1 / sin c", "sin(c) = 1/n", "n sin c = 1"],
        answer="sin c = 1 / n", symbols="c is the critical angle",
        wrongs={"sinc = n": "n is greater than 1, so sin c cannot equal n. sin c = 1/n.", "c = 1/n": "You need the SINE of the critical angle: sin c = 1/n.", "sinc = n/1": "sin c = 1/n."},
        hints=["At the critical angle the angle of refraction is 90°, and sin 90° = 1.", "Put i = c, r = 90° into n = sin r / sin i for light leaving the medium.", "sin c = 1 / ..."],
        keywords="sin c, 1/n", sample_pass=["sin c = 1/n", "n = 1/sin c"], sample_fail=["sin c = n", "c = 1/n"])

formula("f_transformer_turns", "emi", 2, "19e", "Write the **transformer turns-ratio** equation.", syllabi=PURE,
        forms=["Vp/Vs = Np/Ns", "Vs/Vp = Ns/Np", "V_p/V_s = N_p/N_s", "Vp/Vs = Np/Ns", "VP/VS = NP/NS", "Vp / Vs = Np / Ns", "V1/V2 = N1/N2", "Vs/Vp = Ns/Np", "Np/Ns = Vp/Vs", "Ns/Np = Vs/Vp"],
        answer="Vp / Vs = Np / Ns", symbols="Vp, Vs are the primary and secondary voltages; Np, Ns the numbers of turns",
        wrongs={"vp/vs = ns/np": "The ratios must match: primary over primary on both sides, Vp/Vs = Np/Ns.", "vpvs = npns": "It is a ratio: Vp/Vs = Np/Ns.", "vp/vs = is/ip": "That is the power equation (VpIp = VsIs). The turns ratio is Vp/Vs = Np/Ns."},
        hints=["The voltage ratio equals the turns ratio.", "Keep primary with primary on each side.", "Vp / Vs = N... / N..."],
        keywords="voltage ratio = turns ratio", sample_pass=["Vp/Vs = Np/Ns", "Vs/Vp = Ns/Np"], sample_fail=["Vp/Vs = Ns/Np", "VpVs = NpNs"])

formula("f_transformer_power", "emi", 2, "19e", "Write the equation for an **ideal transformer** relating the primary and secondary voltages and currents (power).", syllabi=PURE,
        forms=["VpIp = VsIs", "Vp Ip = Vs Is", "V_p I_p = V_s I_s", "VPIP = VSIS", "IpVp = IsVs", "Vp × Ip = Vs × Is", "Pp = Ps", "VpIp = VsIs", "Vp/Vs = Is/Ip", "Ip/Is = Vs/Vp", "V1I1 = V2I2"],
        answer="Vp Ip = Vs Is  (power in = power out for an ideal transformer)", symbols="",
        wrongs={"vp/vs = ip/is": "Upside down: a step-UP in voltage means a step-DOWN in current. VpIp = VsIs, so Vp/Vs = Is/Ip.", "vp/ip = vs/is": "VpIp = VsIs (products, not ratios).", "vp/vs = np/ns": "That is the turns-ratio equation. For power: VpIp = VsIs."},
        hints=["An ideal transformer wastes no power.", "Power = V I on each side.", "Primary power equals secondary power."],
        keywords="power in = power out", sample_pass=["VpIp = VsIs", "Vp Ip = Vs Is"], sample_fail=["Vp/Vs = Ip/Is", "Vp/Vs = Np/Ns"])

formula("f_kwh_cost", "practical", 2, "14c", "Write the formula for the **cost** of using an electrical appliance, using the kWh.",
        forms=["cost = energy in kWh × cost per kWh", "cost = kWh × cost per kWh", "cost = power (kW) × time (h) × cost per kWh", "cost = P × t × rate", "cost = energy × cost per kWh", "cost = kwh x price per kwh", "cost = number of kWh × cost per unit", "cost = P(kW) × t(h) × cost per kWh", "cost = kwh x rate", "cost = energy (kwh) x tariff", "cost = power x time x cost per kwh", "cost = power in kW × time in hours × cost per kWh"],
        answer="cost = energy (kWh) × cost per kWh, where energy (kWh) = power (kW) × time (h)", symbols="",
        wrongs={"cost = power x cost per kwh": "You must multiply by the TIME in hours as well: cost = P(kW) × t(h) × cost per kWh.", "cost = p/t x rate": "Energy = power × time (not divided).", "cost = wxsxrate": "Use kW and hours, not W and seconds, when the tariff is per kWh."},
        hints=["First find the energy in kWh.", "Energy (kWh) = power in kW × time in hours.", "Then multiply by the price of one kWh."],
        keywords="kWh = kW × h; × cost per kWh", sample_pass=["cost = energy in kWh × cost per kWh", "cost = power (kW) × time (h) × cost per kWh"], sample_fail=["cost = power × cost per kWh", "cost = VIt"])

formula("f_resistivity_prop", "current", 2, "12j", "Write the proportionality relating the **resistance** R of a wire to its length l and cross-sectional area A.",
        forms=["R ∝ l/A", "R ∝ L/A", "R is proportional to l/A", "R ∝ length/area", "R ∝ l / A", "R = ρl/A", "R = ρL/A", "R = rho l / A", "r proportional to l/a", "R ∝ l / A"],
        answer="R ∝ l / A  (R = ρ l / A)", symbols="l is the length of the wire, A its cross-sectional area, ρ the resistivity of the material",
        wrongs={"r ∝ a/l": "Upside down: R increases with LENGTH and decreases with AREA.", "r ∝ la": "R ∝ l/A: a thicker wire has LESS resistance.", "r ∝ l": "Also inversely proportional to the area: R ∝ l/A."},
        hints=["Longer wire: more resistance. Thicker wire: less.", "Length on top, area below.", "R ∝ ... / ..."],
        keywords="length, cross-sectional area", sample_pass=["R ∝ l/A", "R = ρl/A"], sample_fail=["R ∝ A/l", "R ∝ lA"])

formula("f_echo", "waves", 2, "9i", "Write the formula for the **distance to a reflecting surface** using an echo, in terms of the speed of sound v and the time t between the sound and its echo.",
        forms=["d = vt/2", "d = (vt)/2", "d = ½vt", "d = 1/2 vt", "2d = vt", "d = v t / 2", "distance = speed × time / 2", "d = vt ÷ 2", "d = 0.5vt", "distance = (speed x time)/2", "d = v × t / 2", "distance = speed × time ÷ 2"],
        answer="d = v t / 2  (the sound travels there and back, 2d = vt)", symbols="",
        wrongs={"d = vt": "That is the TOTAL distance there and back. The distance to the wall is half: d = vt/2.", "d = 2vt": "The other way: the sound covers 2d, so d = vt/2.", "d = v/2t": "d = (v × t)/2."},
        hints=["The sound goes to the wall and comes back.", "So speed × time gives twice the distance.", "Halve it."],
        keywords="speed × time ÷ 2", sample_pass=["d = vt/2", "2d = vt", "d = ½vt"], sample_fail=["d = vt", "d = 2vt"])

# ================================================================= L3  rearranged subjects
formula("f_r_mass_density", "pressure", 3, "3g", "Write an expression for the **mass** of an object in terms of its density ρ and volume V.",
        forms=["m = ρV", "m = rho V", "m = ρ × V", "mass = density × volume", "m = Vρ", "m = v rho", "m = density x volume", "m = rhov"],
        answer="m = ρ V", symbols="",
        wrongs={"m = rho/v": "From ρ = m/V, multiply both sides by V: m = ρV.", "m = v/rho": "m = ρV."},
        hints=["Start from ρ = m/V.", "Make m the subject.", "Multiply both sides by V."],
        keywords="density × volume", sample_pass=["m = ρV", "mass = density × volume"], sample_fail=["m = ρ/V", "m = V/ρ"])

formula("f_r_time_speed", "kin", 3, "2b", "Write an expression for the **time taken** to travel a distance d at speed v.",
        forms=["t = d/v", "time = distance / speed", "t = d / v", "t = s/v", "t = distance/speed", "time = distance ÷ speed"],
        answer="t = d / v", symbols="",
        wrongs={"t = v/d": "Upside down: t = d/v (e.g. 100 m at 5 m/s takes 100/5 = 20 s).", "t = dv": "Divide: t = d/v."},
        hints=["Start from v = d/t.", "Make t the subject.", "Distance divided by speed."],
        keywords="distance ÷ speed", sample_pass=["t = d/v", "time = distance/speed"], sample_fail=["t = v/d", "t = dv"])

formula("f_r_height_gpe", "energy", 3, "6b", "Write an expression for the **height** h gained by a body of mass m when its gravitational potential energy increases by Ep.",
        forms=["h = Ep/mg", "h = Ep/(mg)", "h = E/mg", "h = E/(mg)", "h = GPE/mg", "h = PE/mg", "h = Ep / (m g)", "h = gpe/(mg)", "h = Ep/(m × g)"],
        answer="h = Ep / (m g)", symbols="",
        wrongs={"h = mg/ep": "Upside down: h = Ep/(mg).", "h = ep/m": "Divide by g as well: h = Ep/(mg).", "h = epmg": "Divide: h = Ep/(mg)."},
        hints=["Start from Ep = mgh.", "Make h the subject.", "Divide both sides by mg."],
        keywords="Ep ÷ (mg)", sample_pass=["h = Ep/mg", "h = E/(m g)"], sample_fail=["h = mg/Ep", "h = Ep/m"])

formula("f_r_speed_ke", "energy", 3, "6b", "Write an expression for the **speed** v of a body of mass m with kinetic energy Ek.",
        forms=["v = √(2Ek/m)", "v = sqrt(2Ek/m)", "v = √(2E/m)", "v = sqrt(2E/m)", "v = √(2KE/m)", "v = sqrt(2KE/m)", "v² = 2Ek/m", "v^2 = 2Ek/m", "v2 = 2E/m", "v^2 = 2KE/m", "v = (2Ek/m)^(1/2)", "v = (2Ek/m)^0.5", "v = √2Ek/m", "v = sqrt 2Ek/m", "v = (2E/m)^1/2"],
        answer="v = √(2 Ek / m)", symbols="",
        wrongs={"v = 2ek/m": "Do not forget the square root: Ek = ½mv², so v² = 2Ek/m and v = √(2Ek/m).", "v = √ek/m": "Factor of 2 missing: v = √(2Ek/m).", "v = sqrtek/m": "Factor of 2 missing: v = √(2Ek/m).", "v = √ek/2m": "v = √(2Ek/m): the 2 is on top."},
        hints=["Start from Ek = ½mv².", "Make v² the subject first: multiply by 2, divide by m.", "Then square-root."],
        keywords="√(2Ek/m)", sample_pass=["v = √(2Ek/m)", "v^2 = 2Ek/m", "v = sqrt(2E/m)"], sample_fail=["v = 2Ek/m", "v = √(Ek/m)"])

formula("f_r_time_power", "energy", 3, "6e", "Write an expression for the **time** t taken by a machine of power P to do work W.",
        forms=["t = W/P", "t = E/P", "time = work done / power", "time = energy / power", "t = W / P", "t = work/power", "t = energy/power"],
        answer="t = W / P", symbols="",
        wrongs={"t = p/w": "Upside down: from P = W/t, t = W/P.", "t = pw": "Divide: t = W/P."},
        hints=["Start from P = W/t.", "Make t the subject.", "Work done divided by power."],
        keywords="work ÷ power", sample_pass=["t = W/P", "t = E/P"], sample_fail=["t = P/W", "t = PW"])

formula("f_r_current_power", "practical", 3, "14b", "Write an expression for the **current** drawn by an appliance of power P on a supply of voltage V.",
        forms=["I = P/V", "current = power / voltage", "I = P / V", "current = power/p.d.", "I = power/voltage"],
        answer="I = P / V", symbols="",
        wrongs={"i = v/p": "Upside down: from P = VI, I = P/V.", "i = pv": "Divide: I = P/V.", "i = v/r": "True but needs R; from the power, I = P/V."},
        hints=["Start from P = VI.", "Make I the subject.", "Power divided by voltage."],
        keywords="power ÷ voltage", sample_pass=["I = P/V", "current = power/voltage"], sample_fail=["I = V/P", "I = PV"])

formula("f_r_mass_shc", "thermal_props", 3, "9c", "Write an expression for the **specific heat capacity** c of a substance of mass m that needs energy Q to rise in temperature by Δθ.", syllabi=PURE,
        forms=["c = Q/(mΔθ)", "c = Q/mΔθ", "c = Q/(m Δθ)", "c = Q/(mΔT)", "c = Q/mΔT", "c = E/(mΔθ)", "c = E/mΔθ", "c = E/(mΔT)", "c = E/mΔT", "c = Q / (m × Δθ)", "c = Q/(m delta theta)", "c = Q/m delta T", "c = Q/(m(T2-T1))", "c = Q/(mθ)", "c = Q/mθ", "c = Q/(mT)"],
        answer="c = Q / (m Δθ)", symbols="",
        wrongs={"c = mdeltatheta/q": "Upside down: c = Q/(mΔθ).", "c = q/m": "Divide by the temperature change too: c = Q/(mΔθ).", "c = q/deltatheta": "That is the heat capacity C. Specific heat capacity is per kg: c = Q/(mΔθ)."},
        hints=["Start from Q = mcΔθ.", "Make c the subject.", "Divide both sides by m and by Δθ."],
        keywords="Q ÷ (m Δθ)", sample_pass=["c = Q/(mΔθ)", "c = E/mΔT"], sample_fail=["c = mΔθ/Q", "c = Q/m"])

formula("f_r_time_charge", "current", 3, "12e", "Write an expression for the **time** for a charge Q to pass when the current is I.",
        forms=["t = Q/I", "time = charge / current", "t = Q / I", "t = charge/current"],
        answer="t = Q / I", symbols="",
        wrongs={"t = i/q": "Upside down: from Q = It, t = Q/I.", "t = qi": "Divide: t = Q/I."},
        hints=["Start from Q = It.", "Make t the subject.", "Charge divided by current."],
        keywords="charge ÷ current", sample_pass=["t = Q/I", "time = charge/current"], sample_fail=["t = I/Q", "t = QI"])

formula("f_r_wavelength", "waves", 3, "9d", "Write an expression for the **wavelength** of a wave of speed v and frequency f.",
        forms=["λ = v/f", "lambda = v/f", "wavelength = speed / frequency", "λ = v / f", "wavelength = speed/frequency", "λ = vT", "lambda = vT", "λ = v T"],
        answer="λ = v / f  (= v T)", symbols="",
        wrongs={"lambda = f/v": "Upside down: from v = fλ, λ = v/f.", "lambda = vf": "Divide: λ = v/f.", "lambda = v/t": "Multiply by the period: λ = vT (or divide by the frequency, λ = v/f)."},
        hints=["Start from v = fλ.", "Make λ the subject.", "Speed divided by frequency."],
        keywords="speed ÷ frequency", sample_pass=["λ = v/f", "wavelength = speed/frequency", "λ = vT"], sample_fail=["λ = f/v", "λ = vf"])

formula("f_r_force_moment", "moments", 3, "5b", "Write an expression for the **force** F needed to produce a moment M at a perpendicular distance d from the pivot.",
        forms=["F = M/d", "F = moment/d", "force = moment / perpendicular distance", "F = M / d", "F = moment / distance", "F = moment/perpendicular distance"],
        answer="F = M / d", symbols="M is the moment, d the perpendicular distance from the pivot",
        wrongs={"f = d/m": "Upside down: from M = Fd, F = M/d.", "f = md": "Divide: F = M/d."},
        hints=["Start from moment = F × d.", "Make F the subject.", "Moment divided by distance."],
        keywords="moment ÷ distance", sample_pass=["F = M/d", "force = moment / perpendicular distance"], sample_fail=["F = d/M", "F = Md"])

formula("f_r_area_pressure", "pressure", 3, "3i", "Write an expression for the **area** over which a force F must act to produce a pressure p.",
        forms=["A = F/p", "A = F / p", "area = force / pressure", "A = force/pressure", "a = f/p"],
        answer="A = F / p", symbols="",
        wrongs={"a = p/f": "Upside down: from p = F/A, A = F/p.", "a = fp": "Divide: A = F/p."},
        hints=["Start from p = F/A.", "Make A the subject.", "Force divided by pressure."],
        keywords="force ÷ pressure", sample_pass=["A = F/p", "area = force/pressure"], sample_fail=["A = p/F", "A = Fp"])

formula("f_r_distance_vt", "kin", 3, "2h", "A body moves with uniform acceleration from velocity u to velocity v in time t. Write an expression for the **distance travelled** (the area under the velocity-time graph).",
        forms=["d = ½(u+v)t", "s = ½(u+v)t", "d = (u+v)t/2", "s = (u+v)t/2", "d = 1/2 (u+v) t", "s = 1/2(u+v)t", "distance = average velocity × time", "d = (u+v)/2 × t", "s = (u + v)/2 × t", "s = ((u+v)/2)t", "d = ((u+v)/2)t", "d = 0.5(u+v)t", "s = 0.5(u+v)t", "distance = ½(u + v) × t", "d = (u+v)/2 t", "s = (u+v)/2 t"],
        answer="d = ½ (u + v) t  (average velocity × time)", symbols="u and v are the initial and final velocities",
        wrongs={"d = vt": "Only true for CONSTANT velocity. With acceleration use the average velocity: d = ½(u + v)t.", "s = vt": "Only true for constant velocity. Use d = ½(u + v)t.", "d = u+vt": "Average velocity is (u + v)/2: d = ½(u + v)t.", "d = 1/2vt": "Only if it starts from rest (u = 0). In general d = ½(u + v)t."},
        hints=["Area under a v-t graph: a trapezium.", "Area of a trapezium = ½ × (sum of parallel sides) × width.", "The parallel sides are u and v; the width is t."],
        keywords="½(u + v)t", sample_pass=["d = ½(u+v)t", "s = (u+v)t/2", "d = 0.5(u+v)t"], sample_fail=["d = vt", "d = ut"])

# ================================================================= L4  combined / derived
formula("f_power_i2r", "practical", 4, "14b", "Write the formula for **electrical power** in terms of current and resistance only.",
        forms=["P = I²R", "P = I^2 R", "P = I2R", "P = RI²", "power = current² × resistance", "P = I × I × R", "P = (I^2)R", "P = I squared R"],
        answer="P = I² R", symbols="",
        wrongs={"p = ir": "I R is the p.d. Substitute V = IR into P = VI to get P = I²R.", "p = ir2": "It is the CURRENT that is squared: P = I²R.", "p = i2/r": "P = I²R (multiply). I²/R is not a power formula; V²/R is."},
        hints=["Start from P = VI.", "Replace V using V = IR.", "P = (IR) × I = ..."],
        keywords="I², R", sample_pass=["P = I²R", "P = I^2 R"], sample_fail=["P = IR", "P = I²/R"])

formula("f_power_v2r", "practical", 4, "14b", "Write the formula for **electrical power** in terms of potential difference and resistance only.",
        forms=["P = V²/R", "P = V^2/R", "P = V2/R", "power = voltage² / resistance", "P = V²/R", "P = (V^2)/R", "P = V squared / R"],
        answer="P = V² / R", symbols="",
        wrongs={"p = v/r": "V/R is the CURRENT. Power = V × I = V × V/R = V²/R.", "p = v2r": "Divide by R: P = V²/R.", "p = r/v2": "Upside down: P = V²/R."},
        hints=["Start from P = VI.", "Replace I using I = V/R.", "P = V × V/R = ..."],
        keywords="V², R", sample_pass=["P = V²/R", "P = V^2 / R"], sample_fail=["P = V/R", "P = V²R"])

formula("f_energy_i2rt", "practical", 4, "14b", "Write the formula for the **thermal energy** produced in a resistor in terms of current, resistance and time.",
        forms=["E = I²Rt", "E = I^2 R t", "E = I2Rt", "Q = I²Rt", "E = RI²t", "energy = current² × resistance × time", "E = I^2Rt", "W = I²Rt"],
        answer="E = I² R t", symbols="",
        wrongs={"e = irt": "The current is squared: E = I²Rt (from E = VIt with V = IR).", "e = i2r": "Multiply by time to get energy: E = I²Rt.", "e = vit": "Correct in general, but the question asked for current, resistance and time: E = I²Rt."},
        hints=["Energy = power × time.", "Power in terms of I and R is I²R.", "So energy = I²R × ..."],
        keywords="I²Rt", sample_pass=["E = I²Rt", "E = I^2 R t"], sample_fail=["E = IRt", "E = I²R"])

formula("f_pressure_depth_diff", "pressure", 4, "5e", "Write an expression for the **difference in pressure** between two points in a liquid of density ρ separated by a vertical height h.", syllabi=PURE,
        forms=["Δp = hρg", "Δp = ρgh", "delta p = h rho g", "Δp = h ρ g", "p2 - p1 = hρg", "p1 - p2 = hρg", "Δp = ρ g h", "Δp = gρh", "delta p = rho g h", "Δp = hgρ", "p2 - p1 = ρgh"],
        answer="Δp = h ρ g", symbols="h is the vertical height between the two points",
        wrongs={"deltap = h/rhog": "Multiply: Δp = hρg.", "deltap = mgh": "mgh is energy, not pressure. Δp = hρg."},
        hints=["Pressure in a liquid depends on depth.", "The extra pressure for an extra depth h is the liquid-column formula.", "Δp = h × ρ × g."],
        keywords="hρg", sample_pass=["Δp = hρg", "p2 - p1 = ρgh"], sample_fail=["Δp = h/ρg", "Δp = mgh"])

formula("f_ke_gpe_fall", "energy", 4, "6c", "A body falls freely from rest through a height h (no air resistance). Using conservation of energy, write an expression for its **speed** v just before impact.",
        forms=["v = √(2gh)", "v = sqrt(2gh)", "v² = 2gh", "v^2 = 2gh", "v2 = 2gh", "v = √2gh", "v = sqrt 2gh", "v = (2gh)^(1/2)", "v = (2gh)^0.5", "½mv² = mgh", "1/2 mv^2 = mgh", "mgh = ½mv²", "mgh = 1/2mv2", "v = (2gh)^1/2"],
        answer="v = √(2 g h)  (from mgh = ½mv²)", symbols="",
        wrongs={"v = 2gh": "Square root missing: v² = 2gh, so v = √(2gh).", "v = √gh": "Factor of 2 missing: ½mv² = mgh gives v² = 2gh.", "v = sqrtgh": "Factor of 2 missing: v = √(2gh).", "v = gh": "Equate mgh to ½mv²: v = √(2gh)."},
        hints=["GPE lost = KE gained.", "mgh = ½mv²: the mass cancels.", "Solve for v."],
        keywords="mgh = ½mv² → v = √(2gh)", sample_pass=["v = √(2gh)", "v² = 2gh", "mgh = ½mv²"], sample_fail=["v = 2gh", "v = √(gh)"])

formula("f_mass_from_weight", "mwg", 4, "3e", "On the Moon g = 1.6 N/kg. Write an expression for the **mass** of an object whose weight on the Moon is W.",
        forms=["m = W/g", "m = W/1.6", "m = W / g", "mass = weight / g", "mass = weight / gravitational field strength", "m = W ÷ 1.6", "m = weight/1.6"],
        answer="m = W / g = W / 1.6", symbols="",
        wrongs={"m = wg": "Divide: m = W/g.", "m = 1.6w": "Divide by g: m = W/1.6.", "m = w/10": "On the MOON g is 1.6 N/kg, not 10."},
        hints=["Start from W = mg.", "Make m the subject.", "Use the Moon's value of g."],
        keywords="W ÷ g", sample_pass=["m = W/g", "m = W/1.6"], sample_fail=["m = Wg", "m = W/10"])

formula("f_combined_power_force_speed", "energy", 4, "6e", "A car travels at constant speed v against a resistive force F. Write an expression for the **power** developed by the engine.",
        forms=["P = Fv", "P = F v", "P = F × v", "power = force × velocity", "power = force × speed", "P = Fd/t", "P = F d / t", "P = W/t = Fd/t"],
        answer="P = F v  (from P = W/t = F d/t)", symbols="",
        wrongs={"p = f/v": "P = W/t = F(d/t) = F × v: multiply.", "p = fd": "F d is the WORK done. Divide by time: P = Fd/t = Fv.", "p = 1/2mv2": "That is kinetic energy, not power. P = Fv."},
        hints=["Power = work done ÷ time.", "Work done = force × distance.", "Distance ÷ time is the speed."],
        keywords="force × speed", sample_pass=["P = Fv", "P = Fd/t"], sample_fail=["P = F/v", "P = Fd"])

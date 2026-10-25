"""Units, prefixes and unit equivalences from the 'Summary of key quantities, symbols and units' table (6091 / 5086).
L1 base units and common derived units; L2 compound units and alternatives; L3 prefixes; L4 equivalences."""
from .base import BOTH, PURE, unit

_H3 = ["Think of the formula that defines the quantity.", "Build the unit from the units of the quantities in that formula.", "Give the SI unit (symbol or name)."]


def _u(id, topic, level, lo, quantity, forms, answer, hints=None, wrongs=None, syllabi=BOTH, sample_pass=(), sample_fail=()):
    unit(id, topic, level, lo, f"State the SI unit of **{quantity}**.", forms, answer, hints or _H3, keywords=f"unit of {quantity}",
         wrongs=wrongs, syllabi=syllabi, sample_pass=sample_pass or [answer.split(" ")[0]], sample_fail=sample_fail or ["kg", "m"])


# ================================================================= L1  base units and common derived units
_u("u_mass", "meas", 1, "1b", "mass", ["kg", "kilogram"], "kg (kilogram)",
   hints=["It is one of the six SI base units.", "Not the gram.", "The one with the prefix built in."],
   wrongs={"g": "The SI base unit of mass is the KILOGRAM, kg (the gram is 1/1000 of it).", "n": "The newton is the unit of force / weight. Mass is in kg."}, sample_fail=["g", "N"])
_u("u_length", "meas", 1, "1b", "length", ["m", "metre", "meter"], "m (metre)",
   hints=["One of the six SI base units.", "Not cm or km.", "The metre."], wrongs={"cm": "The SI base unit is the metre, m.", "km": "The SI base unit is the metre, m."}, sample_fail=["cm", "kg"])
_u("u_time", "meas", 1, "1b", "time", ["s", "second"], "s (second)",
   hints=["One of the six SI base units.", "Not the minute or hour.", "The second."], wrongs={"min": "The SI unit is the second, s.", "h": "The SI unit is the second, s."}, sample_fail=["min", "h"])
_u("u_current", "meas", 1, "1b", "electric current", ["A", "ampere", "amp"], "A (ampere)",
   hints=["One of the six SI base units.", "Not the coulomb (that is charge).", "The ampere."], wrongs={"c": "The coulomb is the unit of CHARGE. Current is in amperes, A.", "v": "The volt is the unit of p.d. Current is in amperes, A."}, sample_fail=["C", "V"])
_u("u_temperature", "meas", 1, "1b", "temperature (SI base unit)", ["K", "kelvin"], "K (kelvin)",
   hints=["One of the six SI base units.", "Not °C, although that is accepted in most calculations.", "The kelvin."], wrongs={"degc": "°C is commonly used, but the SI BASE unit of temperature is the kelvin, K.", "c": "The SI base unit is the kelvin, K."}, sample_fail=["°C", "J"])
_u("u_amount", "meas", 1, "1b", "amount of substance", ["mol", "mole"], "mol (mole)",
   hints=["One of the six SI base units.", "Used in chemistry for counting particles.", "The mole."], wrongs={"kg": "Mass is in kg. Amount of substance is in moles, mol.", "g": "Amount of substance is in moles, mol."}, sample_fail=["kg", "g"])
_u("u_force", "mwg", 1, "3e", "force", ["N", "newton", "kg m/s^2", "kgm/s2", "kg m s^-2", "kgms-2"], "N (newton)",
   hints=["Named after a famous physicist.", "From F = ma: kg × m/s², given its own name.", "The newton."], wrongs={"kg": "kg is mass. Force is in newtons, N.", "j": "J is energy. Force is in newtons, N."}, sample_fail=["kg", "J"])
_u("u_weight", "mwg", 1, "3e", "weight", ["N", "newton"], "N (newton)",
   hints=["Weight is a force.", "So it has the unit of force.", "The newton."], wrongs={"kg": "kg is the unit of MASS. Weight is a force, in newtons, N.", "n/kg": "N/kg is gravitational field strength. Weight is in N."}, sample_fail=["kg", "N/kg"])
_u("u_energy", "energy", 1, "6b", "energy", ["J", "joule", "N m", "Nm", "kg m^2/s^2", "kgm2/s2"], "J (joule)",
   hints=["Work and energy share this unit.", "1 of these is 1 N × 1 m.", "The joule."], wrongs={"w": "W (watt) is power. Energy is in joules, J.", "n": "N is force. Energy is in joules, J.", "kwh": "The kWh is a practical unit of energy; the SI unit is the joule, J."}, sample_fail=["W", "N"])
_u("u_work", "energy", 1, "6d", "work done", ["J", "joule", "N m", "Nm"], "J (joule)",
   hints=["Work done is energy transferred.", "Force × distance: N × m.", "The joule."], wrongs={"w": "W is power. Work done is in joules, J.", "n": "N is force. Work done is in joules, J."}, sample_fail=["W", "N"])
_u("u_power", "energy", 1, "6e", "power", ["W", "watt", "J/s", "J s^-1", "js-1"], "W (watt)",
   hints=["Power is energy per second.", "J/s has its own name.", "The watt."], wrongs={"j": "J is energy. Power is energy per second, W.", "kwh": "kWh is ENERGY, not power. Power is in watts, W.", "n": "N is force. Power is in watts, W."}, sample_fail=["J", "kWh"])
_u("u_pressure", "pressure", 1, "3i", "pressure", ["Pa", "pascal", "N/m^2", "N/m2", "N m^-2", "nm-2", "newton per square metre", "n/m^2"], "Pa (pascal), i.e. N/m²",
   hints=["Pressure is force per unit area.", "N/m² has its own name.", "The pascal."], wrongs={"n": "N is force. Pressure is force per unit AREA: N/m² or Pa.", "n/m": "Per unit AREA: N/m², not N/m.", "n/m3": "Per square metre, not cubic: N/m²."}, sample_fail=["N", "N/m"])
_u("u_frequency", "waves", 1, "9c", "frequency", ["Hz", "hertz", "1/s", "s^-1", "s-1", "per second"], "Hz (hertz)",
   hints=["Number of waves per second.", "'Per second' has its own name here.", "The hertz."], wrongs={"s": "s is the unit of PERIOD. Frequency is per second: Hz.", "m": "m is wavelength. Frequency is in hertz, Hz."}, sample_fail=["s", "m"])
_u("u_charge", "current", 1, "12a", "electric charge", ["C", "coulomb", "A s", "As"], "C (coulomb)",
   hints=["Charge = current × time.", "A × s has its own name.", "The coulomb."], wrongs={"a": "A is current. Charge is in coulombs, C.", "v": "V is p.d. Charge is in coulombs, C."}, sample_fail=["A", "V"])
_u("u_pd", "current", 1, "12g", "potential difference", ["V", "volt", "J/C", "jc-1", "joule per coulomb"], "V (volt), i.e. J/C",
   hints=["Work done per unit charge.", "J/C has its own name.", "The volt."], wrongs={"a": "A is current. P.d. is in volts, V.", "j": "J is energy. P.d. is energy PER COULOMB: V.", "omega": "Ω is resistance. P.d. is in volts, V.", "ohm": "Ω is resistance. P.d. is in volts, V."}, sample_fail=["A", "J"])
_u("u_emf", "current", 1, "12f", "electromotive force (e.m.f.)", ["V", "volt", "J/C"], "V (volt)",
   hints=["Despite the name it is not a force.", "Work done per unit charge, like p.d.", "The volt."], wrongs={"n": "E.m.f. is NOT a force, so not newtons. It is work done per unit charge: volts, V.", "a": "A is current. E.m.f. is in volts, V."}, sample_fail=["N", "A"])
_u("u_resistance", "current", 1, "12h", "resistance", ["Ω", "ohm", "omega", "V/A", "va-1", "volt per ampere"], "Ω (ohm), i.e. V/A",
   hints=["R = V/I.", "V/A has its own name and a Greek-letter symbol.", "The ohm."], wrongs={"v": "V is p.d. Resistance is p.d. per unit current: Ω.", "a": "A is current. Resistance is in ohms, Ω.", "w": "W is power. Resistance is in ohms, Ω."}, sample_fail=["V", "W"])
_u("u_moment", "moments", 1, "5b", "moment of a force", ["N m", "Nm", "newton metre", "newton meter", "N·m"], "N m (newton metre)",
   hints=["Moment = force × perpendicular distance.", "Unit of force × unit of distance.", "Write both units, with a space, not as J."], wrongs={"j": "Although N m = J numerically, the moment of a force is written N m, not J (it is not an energy).", "n/m": "Multiply, do not divide: N m.", "n": "Force × distance: N m."}, sample_pass=["N m", "newton metre"], sample_fail=["J", "N/m"])

# ================================================================= L2  compound units and alternatives
_u("u_speed", "kin", 2, "2a", "speed", ["m/s", "m s^-1", "ms-1", "metre per second", "metres per second"], "m/s",
   hints=["Speed = distance / time.", "Unit of distance over unit of time.", "m/s."], wrongs={"m/s2": "m/s² is ACCELERATION. Speed is m/s.", "km/h": "km/h is a common unit, but the SI unit is m/s."}, sample_fail=["m/s²", "s/m"])
_u("u_acceleration", "kin", 2, "2c", "acceleration", ["m/s^2", "m/s2", "m s^-2", "ms-2", "metre per second squared", "metres per second squared", "m/s/s"], "m/s²",
   hints=["Acceleration = change in velocity / time.", "(m/s) per s.", "m/s²."], wrongs={"m/s": "m/s is speed. Acceleration is m/s².", "n/kg": "N/kg is equivalent to m/s² but is the usual unit for g; for acceleration write m/s².", "m/s3": "Per second squared, not cubed."}, sample_fail=["m/s", "m/s³"])
_u("u_density", "pressure", 2, "3g", "density", ["kg/m^3", "kg/m3", "kg m^-3", "kgm-3", "g/cm^3", "g/cm3", "kilogram per cubic metre", "g cm^-3", "gcm-3"], "kg/m³ (also g/cm³)",
   hints=["Density = mass / volume.", "Unit of mass over unit of volume.", "kg/m³ (or g/cm³)."], wrongs={"kg/m": "Per unit VOLUME: kg/m³, not kg/m.", "kg/m2": "Volume is m³, so kg/m³.", "kg": "kg is mass alone. Density is kg/m³.", "m3/kg": "Upside down: kg/m³."}, sample_fail=["kg/m²", "kg"])
_u("u_g", "mwg", 2, "3d", "gravitational field strength", ["N/kg", "N kg^-1", "nkg-1", "newton per kilogram", "m/s^2", "m/s2"], "N/kg (equivalent to m/s²)",
   hints=["Gravitational force per unit mass.", "Unit of force over unit of mass.", "N/kg."], wrongs={"n": "N is force. g is force PER UNIT MASS: N/kg.", "kg/n": "Upside down: N/kg.", "m/s": "m/s is speed. g is N/kg (or m/s²)."}, sample_fail=["N", "kg/N"])
_u("u_wavelength", "waves", 2, "9c", "wavelength", ["m", "metre", "meter"], "m (metre)",
   hints=["Wavelength is a distance.", "So it has the unit of length.", "The metre."], wrongs={"hz": "Hz is frequency. Wavelength is a length: m.", "s": "s is period. Wavelength is a length: m."}, sample_fail=["Hz", "s"])
_u("u_period", "waves", 2, "9c", "period", ["s", "second"], "s (second)",
   hints=["Period is the time for one wave.", "So it has the unit of time.", "The second."], wrongs={"hz": "Hz is FREQUENCY. Period is a time: s.", "m": "m is wavelength. Period is a time: s."}, sample_fail=["Hz", "m"])
_u("u_shc", "thermal_props", 2, "9b", "specific heat capacity", ["J/(kg K)", "J/(kg °C)", "J/kg K", "J/kg °C", "J kg^-1 K^-1", "jkg-1k-1", "J/kg/K", "J/kg/°C", "J kg^-1 °C^-1", "jkg-1degc-1", "joule per kilogram per kelvin", "J/(kgK)", "J/(kg·K)", "J/(kg C)", "J/kg C"], "J/(kg K)  or  J/(kg °C)",
   syllabi=PURE, hints=["From Q = mcΔθ, c = Q/(mΔθ).", "Energy per kilogram per kelvin.", "J/(kg K)."], wrongs={"j/k": "J/K is HEAT CAPACITY (no mass). Specific heat capacity is J/(kg K).", "j/kg": "J/kg is specific LATENT heat. Specific heat capacity also has a per-kelvin: J/(kg K).", "j": "Energy per kg per K: J/(kg K)."}, sample_pass=["J/(kg K)", "J/kg°C", "J kg^-1 K^-1"], sample_fail=["J/K", "J/kg"])
_u("u_heat_capacity", "thermal_props", 2, "9b", "heat capacity", ["J/K", "J/°C", "J K^-1", "jk-1", "joule per kelvin", "J/degC", "jdegc-1", "J °C^-1"], "J/K  or  J/°C",
   syllabi=PURE, hints=["Energy to raise the whole body by 1 K.", "Energy per kelvin, no mass.", "J/K."], wrongs={"j/kgk": "J/(kg K) is SPECIFIC heat capacity. Heat capacity (whole body) is J/K.", "j": "Energy per kelvin: J/K."}, sample_pass=["J/K", "J/°C"], sample_fail=["J/(kg K)", "J"])
_u("u_slh", "thermal_props", 2, "9f", "specific latent heat", ["J/kg", "J kg^-1", "jkg-1", "joule per kilogram", "J/g"], "J/kg",
   syllabi=PURE, hints=["From Q = ml, l = Q/m.", "Energy per kilogram, no temperature change so no kelvin.", "J/kg."], wrongs={"j/kgk": "J/(kg K) is specific HEAT CAPACITY. No temperature change in latent heat: J/kg.", "j": "Energy per kg: J/kg.", "j/k": "No kelvin: J/kg."}, sample_pass=["J/kg", "J kg^-1"], sample_fail=["J/(kg K)", "J"])
_u("u_latent_heat", "thermal_props", 2, "9f", "latent heat", ["J", "joule"], "J (joule)",
   syllabi=PURE, hints=["Latent heat (not specific) is an amount of energy.", "So it has the unit of energy.", "The joule."], wrongs={"j/kg": "J/kg is SPECIFIC latent heat. Latent heat itself is an energy: J.", "w": "W is power. Latent heat is energy: J."}, sample_fail=["J/kg", "W"])
_u("u_half_life", "radio", 2, "16g", "half-life", ["s", "second", "seconds", "year", "years", "day", "days", "hour", "hours", "minute", "minutes", "min", "h", "yr", "unit of time", "time"], "s (second), or any unit of time (minutes, hours, days, years)",
   hints=["Half-life is a time.", "So any unit of time; the SI unit is the second.", "The second."], wrongs={"bq": "Bq is ACTIVITY (decays per second). Half-life is a time: s.", "hz": "Half-life is a time, so s (not per second)."}, sample_pass=["s", "years"], sample_fail=["Bq", "Hz"])
_u("u_activity", "radio", 2, "16g", "activity of a radioactive source", ["Bq", "becquerel", "counts per second", "decays per second", "1/s", "s^-1", "s-1", "count/s", "counts/s"], "Bq (becquerel), i.e. decays per second",
   hints=["Activity is the number of decays per second.", "'Per second' here has a special name (not hertz).", "The becquerel."], wrongs={"hz": "Hz is for waves; for activity the unit is the becquerel, Bq (also decays per second).", "s": "s is a time (e.g. half-life). Activity is decays PER second: Bq."}, sample_pass=["Bq", "decays per second"], sample_fail=["s", "J"])
_u("u_kwh", "practical", 2, "14c", "energy, as used on an electricity bill (the practical unit)", ["kWh", "kW h", "kilowatt-hour", "kilowatt hour", "kw·h"], "kWh (kilowatt-hour) — a unit of energy",
   hints=["The 'unit' on an electricity bill.", "Power (kW) × time (h).", "The kilowatt-hour."], wrongs={"kw": "kW is POWER. The bill charges for ENERGY: kWh.", "j": "The SI unit is J, but bills use the much larger kWh (3.6 MJ).", "w": "W is power. Energy on a bill is in kWh."}, sample_pass=["kWh", "kilowatt-hour"], sample_fail=["kW", "W"])
_u("u_refractive_index", "light", 2, "11e", "refractive index", ["no unit", "none", "no units", "dimensionless", "unitless", "it has no unit", "nil", "no si unit", "ratio", "-", "nounit"], "no unit (it is a ratio of two speeds)",
   hints=["It is a ratio of two speeds.", "The units cancel.", "So it has none."], wrongs={"m/s": "n is a RATIO of two speeds, so the m/s cancel: no unit.", "deg": "Angles go into n = sin i / sin r but the sines have no unit: no unit."}, sample_pass=["no unit", "dimensionless"], sample_fail=["m/s", "degrees"])
_u("u_efficiency", "energy", 2, "6f", "efficiency", ["no unit", "none", "%", "percent", "percentage", "no units", "dimensionless", "ratio", "unitless", "nounit", "no si unit"], "no unit (a ratio, usually given as a percentage)",
   syllabi=PURE, hints=["It is a ratio of two energies.", "The joules cancel.", "No unit, or a percentage."], wrongs={"j": "Energy out ÷ energy in: the joules cancel. No unit (or %).", "w": "Power out ÷ power in: the watts cancel. No unit (or %)."}, sample_pass=["no unit", "%"], sample_fail=["J", "W"])
_u("u_angle", "light", 2, "11a", "angle of incidence", ["degree", "degrees", "°", "deg"], "degree (°)",
   hints=["Angles in optics.", "Measured with a protractor.", "The degree."], wrongs={"m": "An angle is not a length. Degrees.", "rad": "Radians exist, but at this level angles are in degrees (°)."}, sample_pass=["degrees", "°"], sample_fail=["m", "N"])

# ================================================================= L3  prefixes
_PH = ["Prefixes are powers of ten.", "Is this prefix bigger or smaller than one?", "Give it as a power of ten, e.g. 10^6, or as a number."]
for _id, _name, _sym, _forms, _ans, _wrong in [
    ("u_prefix_nano", "nano", "n", ["10^-9", "10^(-9)", "1e-9", "0.000000001", "1/10^9", "×10^-9", "x10^-9", "1/1000000000"], "10⁻⁹ (one billionth)", {"10-6": "10⁻⁶ is MICRO. Nano is 10⁻⁹.", "10-3": "10⁻³ is milli. Nano is 10⁻⁹.", "109": "That is giga (10⁹). Nano is 10⁻⁹ (a sub-multiple)."}),
    ("u_prefix_micro", "micro", "μ", ["10^-6", "10^(-6)", "1e-6", "0.000001", "1/10^6", "×10^-6", "x10^-6", "1/1000000"], "10⁻⁶ (one millionth)", {"10-9": "10⁻⁹ is nano. Micro is 10⁻⁶.", "10-3": "10⁻³ is milli. Micro is 10⁻⁶.", "106": "That is mega (10⁶). Micro is 10⁻⁶ (a sub-multiple)."}),
    ("u_prefix_milli", "milli", "m", ["10^-3", "10^(-3)", "1e-3", "0.001", "1/1000", "1/10^3", "×10^-3", "x10^-3"], "10⁻³ (one thousandth)", {"10-6": "10⁻⁶ is micro. Milli is 10⁻³.", "103": "That is kilo (10³). Milli is 10⁻³, a thousandth.", "1000": "1000 is kilo. Milli is 1/1000 = 10⁻³."}),
    ("u_prefix_centi", "centi", "c", ["10^-2", "10^(-2)", "1e-2", "0.01", "1/100", "1/10^2", "×10^-2", "x10^-2"], "10⁻² (one hundredth)", {"10-3": "10⁻³ is milli. Centi is 10⁻² (100 cm in a metre).", "100": "100 would be a multiple; centi is 1/100 = 10⁻²."}),
    ("u_prefix_deci", "deci", "d", ["10^-1", "10^(-1)", "1e-1", "0.1", "1/10", "×10^-1", "x10^-1"], "10⁻¹ (one tenth)", {"10-2": "10⁻² is centi. Deci is 10⁻¹ (10 dm in a metre).", "10": "Deci is a sub-multiple: 1/10 = 10⁻¹."}),
    ("u_prefix_kilo", "kilo", "k", ["10^3", "1000", "1e3", "×10^3", "x10^3", "×1000", "x1000"], "10³ (one thousand)", {"10-3": "10⁻³ is milli. Kilo is 10³ (1 km = 1000 m).", "106": "10⁶ is mega. Kilo is 10³.", "100": "Kilo is a THOUSAND, 10³."}),
    ("u_prefix_mega", "mega", "M", ["10^6", "1000000", "1e6", "×10^6", "x10^6", "1 000 000"], "10⁶ (one million)", {"103": "10³ is kilo. Mega is 10⁶.", "109": "10⁹ is giga. Mega is 10⁶.", "10-6": "10⁻⁶ is micro. Mega is 10⁶ (a multiple)."}),
    ("u_prefix_giga", "giga", "G", ["10^9", "1000000000", "1e9", "×10^9", "x10^9"], "10⁹ (one billion)", {"106": "10⁶ is mega. Giga is 10⁹.", "1012": "10¹² is tera. Giga is 10⁹.", "10-9": "10⁻⁹ is nano. Giga is 10⁹ (a multiple)."}),
    ("u_prefix_tera", "tera", "T", ["10^12", "1000000000000", "1e12", "×10^12", "x10^12"], "10¹² (one trillion)", {"109": "10⁹ is giga. Tera is 10¹².", "106": "10⁶ is mega. Tera is 10¹²."}),
]:
    unit(_id, "meas", 3, "1c", f"What multiple or sub-multiple does the prefix **{_name}** ({_sym}) stand for? Give it as a power of ten.",
         _forms, _ans, _PH, keywords=f"{_name} = power of ten", wrongs=_wrong, sample_pass=[_forms[0], _forms[1]], sample_fail=list(_wrong)[:2])

# ================================================================= L4  equivalences
_EH = ["Start from the defining formula.", "Replace each quantity by its unit.", "Write the equivalent unit."]
for _id, _topic, _lo, _stem, _forms, _ans, _wrong in [
    ("u_eq_newton", "mwg", "3e", "Express the **newton** in terms of SI base units (use F = ma).", ["kg m/s^2", "kg m/s2", "kgm/s2", "kg m s^-2", "kgms-2", "1 N = 1 kg m/s^2", "kg·m/s²", "kg m s-2"], "1 N = 1 kg m/s²", {"kgm/s": "kg m/s would be momentum. From F = ma: kg × m/s².", "kg/ms2": "Mass TIMES acceleration: kg m/s².", "kgm": "Acceleration is m/s²: so kg m/s²."}),
    ("u_eq_pascal", "pressure", "3i", "Express the **pascal** in terms of newtons and metres.", ["N/m^2", "N/m2", "N m^-2", "nm-2", "1 Pa = 1 N/m^2", "newton per square metre"], "1 Pa = 1 N/m²", {"n/m": "Per square metre: N/m².", "nm2": "Divide by area: N/m².", "n/m3": "Square metre, not cubic."}),
    ("u_eq_joule", "energy", "6d", "Express the **joule** in terms of newtons and metres.", ["N m", "Nm", "1 J = 1 N m", "newton metre", "N·m", "kg m^2/s^2", "kgm2/s2"], "1 J = 1 N m", {"n/m": "Work = force × distance: N m (multiply).", "nm2": "Force × distance, not area: N m.", "w/s": "That is upside down: 1 J = 1 W s."}),
    ("u_eq_watt", "energy", "6e", "Express the **watt** in terms of joules and seconds.", ["J/s", "J s^-1", "js-1", "1 W = 1 J/s", "joule per second"], "1 W = 1 J/s", {"js": "Power = energy ÷ time: J/s.", "s/j": "Upside down: J/s.", "j": "Per second: J/s."}),
    ("u_eq_volt", "current", "12g", "Express the **volt** in terms of joules and coulombs.", ["J/C", "J C^-1", "jc-1", "1 V = 1 J/C", "joule per coulomb"], "1 V = 1 J/C  (work done per unit charge)", {"jc": "Work done PER charge: J/C.", "c/j": "Upside down: J/C.", "j/a": "Per coulomb (charge), not per ampere: J/C."}),
    ("u_eq_ampere", "current", "12c", "Express the **ampere** in terms of coulombs and seconds.", ["C/s", "C s^-1", "cs-1", "1 A = 1 C/s", "coulomb per second"], "1 A = 1 C/s  (rate of flow of charge)", {"cs": "Charge PER second: C/s.", "s/c": "Upside down: C/s."}),
    ("u_eq_ohm", "current", "12h", "Express the **ohm** in terms of volts and amperes.", ["V/A", "V A^-1", "va-1", "1 Ω = 1 V/A", "volt per ampere"], "1 Ω = 1 V/A", {"va": "R = V/I: divide. V/A.", "a/v": "Upside down: V/A."}),
    ("u_eq_hertz", "waves", "9c", "Express the **hertz** in terms of seconds.", ["1/s", "s^-1", "s-1", "1 Hz = 1/s", "per second", "1 Hz = 1 s^-1"], "1 Hz = 1 /s  (one per second)", {"s": "Frequency is PER second: 1/s.", "m/s": "That is speed. 1 Hz = 1/s."}),
    ("u_eq_kwh", "practical", "14c", "Express **1 kWh** in joules.", ["3.6 × 10^6 J", "3.6 x 10^6 J", "3.6×10^6 J", "3600000 J", "3 600 000 J", "3.6 MJ", "3.6e6 J", "1 kWh = 3.6 × 10^6 J", "3.6 x 10^6", "3.6×10^6", "3600000", "3.6e6", "3.6 MJ"], "1 kWh = 1000 W × 3600 s = 3.6 × 10⁶ J (3.6 MJ)", {"3600j": "1 kWh = 1000 W × 3600 s = 3 600 000 J.", "1000j": "1 kWh = 1000 W × 3600 s = 3.6 × 10⁶ J.", "3.6×103j": "3.6 × 10⁶ J: kilo (10³) × 3600 (3.6 × 10³)."}),
    ("u_eq_nkg", "mwg", "3d", "Show that N/kg is equivalent to another SI unit: express **N/kg** in base units.", ["m/s^2", "m/s2", "m s^-2", "ms-2", "1 N/kg = 1 m/s^2", "metre per second squared"], "1 N/kg = 1 m/s²  (since N = kg m/s²)", {"m/s": "N/kg = (kg m/s²)/kg = m/s².", "kgm/s2": "Divide by kg: m/s²."}),
]:
    unit(_id, _topic, 4, _lo, _stem, _forms, _ans, _EH, keywords="unit equivalence", wrongs=_wrong, sample_pass=[_forms[0], _forms[1]], sample_fail=list(_wrong)[:2])

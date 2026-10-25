"""Definitions: General wave properties, Electromagnetic spectrum, Light."""
from ..marker import Pitfall, Point
from .base import BOTH, PURE, definition

P, PF = Point, Pitfall

# ================================================================= 10 / 9  Waves
definition("d_wave_wave", "waves", 2, "9b",
           stem="State what a **wave** does, and what it does not do, as it travels.",
           points=[P("transfers energy from one place to another", ["transfers energy", "transfer of energy", "carries energy", "energy is transferred", "energy is carried", "carried along", "transports energy", "transmits energy", "energy is transmitted", "energy is transported", "moves energy"]),
                   P("without transferring matter (the particles only oscillate about their rest positions)", ["without transferring matter", "does not transfer matter", "no transfer of matter", "matter is not transferred", "without transferring the medium", "particles do not travel", "particles only vibrate", "particles oscillate about", "no net movement of particles", "without moving matter"])],
           model_answer="A wave transfers energy from one point to another without transferring matter: the particles of the medium only oscillate about their rest positions.",
           hints=["Think of a cork bobbing on water waves: does it travel with the wave?", "What does travel along the wave?", "Say what is transferred and what is not."],
           keywords="transfers energy, not matter",
           sample_pass=["it transfers energy without transferring matter", "energy is carried along but the particles only vibrate about their rest positions"], sample_fail=["it moves water from one place to another", "it goes up and down"])

definition("d_wave_wavefront", "waves", 2, "9a",
           stem="State what is meant by a **wavefront**.",
           points=[P("an (imaginary) line or surface joining all the points of a wave that are in phase, e.g. all the crests", ["in phase", "same phase", "joining all the crests", "line joining crests", "points that are at the same point in their cycle", "same stage of oscillation", "joining points of equal phase"])],
           pitfalls=[PF(["front of the wave", "the first wave"], "Not 'the front of the wave': a wavefront is a line joining points that are IN PHASE, such as a line along a crest.")],
           model_answer="A wavefront is an imaginary line (or surface) joining all the points of a wave that are in phase, for example all the points along one crest.",
           hints=["In a ripple tank you see bright lines moving along: each is one of these.", "The line joins points that are at the same stage of their vibration.", "Use the words 'in phase'."],
           keywords="line joining points in phase (e.g. a crest)",
           sample_pass=["an imaginary line joining all points of the wave that are in phase", "a line joining all the crests"], sample_fail=["the front of a wave", "the distance between two waves"])

definition("d_wave_frequency", "waves", 1, "9c",
           stem="Define the **frequency** of a wave.",
           points=[P("number of complete waves (oscillations) produced / passing a point per unit time (per second)", ["number of complete waves per unit time", "number of complete waves per second", "number of waves per second", "number of waves produced per second", "number of oscillations per second", "number of complete oscillations per unit time", "number of oscillations per unit time", "number of complete waves passing a point per second", "number of waves passing a point per second", "waves per second", "oscillations per second", "number of vibrations per second", "number of cycles per second", "number of complete waves generated per second", "number of complete waves in one second"])],
           pitfalls=[PF(["time for one", "time taken for one", "time for one complete"], "Time for one complete wave is the PERIOD. Frequency is the number of waves per second.")],
           model_answer="Frequency is the number of complete waves produced per unit time (or the number of complete waves passing a point per second); unit hertz (Hz).",
           hints=["Hz means 'per second'.", "Per second, count how many of what?", "Say 'number of complete waves per second'."],
           keywords="number of complete waves per second",
           sample_pass=["the number of complete waves produced per second", "number of oscillations per unit time"], sample_fail=["the time for one complete wave", "how often the wave vibrates"])

definition("d_wave_wavelength", "waves", 1, "9c",
           stem="Define the **wavelength** of a wave.",
           points=[P("the (shortest) distance between two consecutive points in phase, e.g. crest to adjacent crest", ["distance between two consecutive points in phase", "distance between two successive points in phase", "distance between two adjacent points in phase", "distance between two consecutive crests", "distance between two successive crests", "distance between adjacent crests", "distance between two neighbouring crests", "distance between two consecutive troughs", "crest to the next crest", "distance between two points in phase", "distance between successive compressions", "distance from one crest to the next", "distance of one complete wave", "length of one complete wave"])],
           pitfalls=[PF(["crest to trough", "crest and a trough", "crest and the trough", "crest to the trough"], "Crest to trough is only HALF a wavelength. Wavelength is crest to the NEXT crest (two consecutive points in phase).")],
           model_answer="Wavelength is the shortest distance between two consecutive points on a wave that are in phase, e.g. from one crest to the next crest; unit metre.",
           hints=["It is a distance.", "Between which two points? Think of two neighbouring crests.", "Say 'two consecutive points in phase' or 'crest to the next crest'."],
           keywords="distance between two consecutive points in phase (crest to crest)",
           sample_pass=["the distance between two consecutive crests", "shortest distance between two points in phase"], sample_fail=["the distance from a crest to a trough", "how long the wave is"])

definition("d_wave_period", "waves", 1, "9c",
           stem="Define the **period** of a wave.",
           points=[P("time taken to produce one complete wave / for one complete oscillation", ["time for one complete wave", "time taken for one complete wave", "time to produce one complete wave", "time taken for one complete oscillation", "time for one oscillation", "time for one complete cycle", "time for one wave to pass", "time taken for one wavelength to pass", "time for one complete vibration", "time taken for one complete wave to pass"])],
           pitfalls=[PF(["number of waves per", "waves per second", "oscillations per second"], "Number of waves per second is the FREQUENCY. Period is a time.")],
           model_answer="Period is the time taken to produce one complete wave (one complete oscillation); T = 1/f, unit second.",
           hints=["Period is a time.", "The time for how much of the wave?", "Say 'time for one complete ...'."],
           keywords="time for one complete wave / oscillation",
           sample_pass=["the time taken for one complete oscillation", "time to produce one complete wave"], sample_fail=["the number of waves per second", "the length of a wave"])

definition("d_wave_amplitude", "waves", 1, "9c",
           stem="Define the **amplitude** of a wave.",
           points=[P("the maximum displacement of a point (particle) from its rest / equilibrium position", ["maximum displacement from the rest position", "maximum displacement from its rest position", "maximum displacement from the equilibrium position", "maximum displacement from its equilibrium", "maximum displacement from the undisturbed position", "maximum displacement from the mean position", "maximum displacement from the centre", "maximum displacement of a particle from", "maximum displacement of a point from", "greatest displacement of a particle from", "greatest displacement of a point from", "largest displacement of a particle from", "greatest displacement from its equilibrium", "greatest displacement from its rest", "largest displacement from its rest", "largest displacement from the rest", "maximum displacement from its rest", "maximum displacement from its equilibrium", "greatest displacement from the equilibrium", "greatest displacement from the rest", "largest displacement from the equilibrium", "height of a crest above the rest position", "maximum displacement from the undisturbed"], window=12)],
           pitfalls=[PF(["crest to trough", "crest and trough", "peak to trough", "top to bottom"], "Crest to trough is TWICE the amplitude. Amplitude is measured from the rest position to a crest (or trough)."),
                     PF(["height of the wave"], "'Height of the wave' is ambiguous. Say the maximum displacement from the rest position.")],
           model_answer="Amplitude is the maximum displacement of a point from its rest (equilibrium) position.",
           hints=["It is a displacement.", "Measured from where to where? Start from the rest position.", "Say 'maximum displacement from the rest position'."],
           keywords="maximum displacement from rest position",
           sample_pass=["the maximum displacement from the rest position", "greatest displacement of a particle from its equilibrium position"], sample_fail=["the distance from crest to trough", "the height of the wave"])

definition("d_wave_transverse", "waves", 2, "9e",
           stem="State what is meant by a **transverse** wave, and give one example.",
           points=[P("the oscillations (vibrations) are perpendicular (at right angles) to the direction of wave travel / energy transfer", ["perpendicular to the direction", "at right angles to the direction", "right angles to the direction of travel", "perpendicular to the direction of propagation", "perpendicular to the direction of energy transfer", "90° to the direction", "90 degrees to the direction", "oscillate at right angles", "vibrate perpendicular"]),
                   P("example: light / electromagnetic waves, water waves, waves on a rope", ["light", "electromagnetic", "water wave", "ripples", "rope", "radio", "microwaves", "x-rays"])],
           pitfalls=[PF(["sound"], "Sound is LONGITUDINAL, not transverse.")],
           model_answer="In a transverse wave the particles (or fields) oscillate perpendicular to the direction in which the wave travels (the direction of energy transfer), e.g. light and all electromagnetic waves, water waves, waves on a rope.",
           hints=["Compare the direction the particles move with the direction the wave travels.", "For this type they are at right angles.", "Give one example (not sound)."],
           keywords="oscillations perpendicular to direction of travel; e.g. light, water waves",
           sample_pass=["vibrations are perpendicular to the direction of wave travel, e.g. light", "the particles oscillate at right angles to the direction of energy transfer, like water waves"],
           sample_fail=["the vibrations are parallel to the direction of travel, e.g. sound", "a wave that goes across"])

definition("d_wave_longitudinal", "waves", 2, "9e",
           stem="State what is meant by a **longitudinal** wave, and give one example.",
           points=[P("the oscillations are parallel to (along) the direction of wave travel / energy transfer", ["parallel to the direction", "along the direction of travel", "along the direction of energy transfer", "along the direction of propagation", "along the direction of the wave", "along the direction", "same direction as the wave", "same direction as the energy", "in the direction of propagation", "parallel to the direction of energy transfer", "back and forth along the direction", "parallel to the direction of the wave"]),
                   P("example: sound waves (also compression waves in a spring)", ["sound", "slinky", "spring", "ultrasound", "p-wave", "p wave"])],
           pitfalls=[PF(["light", "water wave"], "Light and water waves are TRANSVERSE. The standard longitudinal example is sound.")],
           model_answer="In a longitudinal wave the particles oscillate parallel to the direction in which the wave travels (the direction of energy transfer), forming compressions and rarefactions, e.g. sound waves.",
           hints=["Compare the direction the particles move with the direction the wave travels.", "For this type they are the same (parallel).", "Give one example."],
           keywords="oscillations parallel to direction of travel; e.g. sound",
           sample_pass=["particles vibrate parallel to the direction of wave travel, e.g. sound", "oscillations are along the direction of energy transfer, like in a sound wave"],
           sample_fail=["vibrations perpendicular to the direction of travel, e.g. light", "a long wave"])

definition("d_wave_compression_rarefaction", "waves", 2, "9g",
           stem="State what is meant by a **compression** and a **rarefaction** in a sound wave.",
           points=[P("compression: a region where the particles (air molecules) are closer together / pressure is higher", ["closer together", "close together", "compressed", "high pressure", "higher pressure", "more dense", "denser", "crowded"]),
                   P("rarefaction: a region where the particles are further apart / pressure is lower", ["further apart", "farther apart", "spread out", "low pressure", "lower pressure", "less dense", "more spaced"])],
           model_answer="A compression is a region of the wave where the air particles are closer together than normal (higher pressure). A rarefaction is a region where the particles are further apart than normal (lower pressure).",
           hints=["Think of the coils of a slinky as a pulse passes.", "In one region the particles are squashed together; in the other they are spread out.", "Describe both regions."],
           keywords="compression: particles closer, high pressure; rarefaction: further apart, low pressure",
           sample_pass=["a compression is where the particles are closer together and a rarefaction is where they are further apart", "compression = region of high pressure, rarefaction = region of low pressure"],
           sample_fail=["a compression is the crest and a rarefaction is the trough", "compression is loud and rarefaction is quiet"])

definition("d_wave_sound_medium", "waves", 2, "9f",
           stem="State how sound is produced and why it cannot travel through a vacuum.",
           points=[P("sound is produced by vibrating sources", ["vibrating source", "vibrating object", "vibration", "vibrates"]),
                   P("it needs a medium (particles) to transfer the vibrations; a vacuum has no particles", ["needs a medium", "requires a medium", "material medium", "particles to transfer", "particles to transmit", "requires particles", "no particles", "no medium", "no matter in a vacuum", "nothing to vibrate", "particles to carry", "needs particles", "particles to pass", "medium to travel through"])],
           model_answer="Sound is produced by a vibrating source. It is a longitudinal wave that needs a medium (solid, liquid or gas) whose particles pass on the vibrations; a vacuum contains no particles, so sound cannot travel through it.",
           hints=["Touch a loudspeaker cone while it plays.", "What carries the vibration from the source to your ear?", "What is missing in a vacuum?"],
           keywords="vibrating source; needs a medium; vacuum has no particles",
           sample_pass=["sound comes from a vibrating source and needs a medium; a vacuum has no particles to vibrate", "produced by vibrations and requires particles to transmit it, so no sound in a vacuum"],
           sample_fail=["sound is too slow to travel in space", "sound is an electromagnetic wave"])

definition("d_wave_loudness_pitch", "waves", 2, "9h",
           stem="State what property of a sound wave determines its **loudness**, and what determines its **pitch**.",
           points=[P("loudness depends on amplitude (larger amplitude, louder)", ["amplitude"]),
                   P("pitch depends on frequency (higher frequency, higher pitch)", ["frequency"])],
           pitfalls=[PF(["loudness depends on frequency", "louder with higher frequency", "pitch depends on amplitude"], "The other way round: loudness ↔ AMPLITUDE, pitch ↔ FREQUENCY.")],
           model_answer="Loudness is determined by the amplitude of the wave: the larger the amplitude, the louder the sound. Pitch is determined by the frequency: the higher the frequency, the higher the pitch.",
           hints=["Two wave properties, one for each.", "Big vibrations are loud.", "Fast vibrations are high-pitched."],
           keywords="loudness: amplitude; pitch: frequency",
           sample_pass=["loudness depends on amplitude and pitch on frequency", "larger amplitude is louder; higher frequency is higher pitch"], sample_fail=["loudness depends on frequency and pitch on amplitude", "loudness depends on wavelength"])

definition("d_wave_echo", "waves", 3, "9i",
           stem="State what an **echo** is, and explain how echoes can be used to measure the distance to a wall.",
           points=[P("an echo is sound reflected from a hard surface", ["reflected", "reflection", "bounces off", "bounced back"]),
                   P("measure the time between emitting the sound and hearing the echo; distance = speed × time ÷ 2 (sound travels there and back)", ["there and back", "to the wall and back", "twice the distance", "divide by 2", "divided by two", "halve", "half the", "speed × time / 2", "speed x time / 2", "2d = vt", "2d = v t", "2 d = v t", "d = vt/2", "d = v t / 2", "distance = speed × time", "vt / 2", "v t / 2", "vt/2"])],
           model_answer="An echo is sound reflected from a hard surface. Make a sound, measure the time until the echo is heard, and use distance = speed of sound × time. The sound travels to the wall and back, so the distance to the wall is half of this: d = vt/2.",
           hints=["What happens to sound when it hits a hard wall?", "What two things do you need to measure or know to get a distance?", "The sound makes a round trip: careful with the factor of 2."],
           keywords="reflected sound; d = vt/2 (there and back)",
           sample_pass=["an echo is reflected sound; time the echo, use distance = speed × time and halve it since the sound goes there and back", "reflection of sound from the wall; 2d = v t"],
           sample_fail=["an echo is a repeated sound; distance = speed × time", "an echo is sound that is refracted"])

definition("d_wave_ultrasound", "waves", 2, "10j",
           stem="State what is meant by **ultrasound**, and give one use.", syllabi=PURE,
           points=[P("sound with a frequency above the upper limit of human hearing (above 20 kHz / 20 000 Hz)", ["above 20 khz", "above 20 000 hz", "above 20000 hz", "more than 20 khz", "higher than 20 khz", "greater than 20 khz", "above the range of human hearing", "above the upper limit of human hearing", "too high for humans to hear", "beyond human hearing", "higher than humans can hear", "above human hearing"]),
                   P("use: sonar / depth finding, medical scanning (e.g. of a fetus), cleaning, quality control", ["sonar", "depth", "echo sounding", "medical scan", "ultrasound scan", "scanning", "fetus", "foetus", "baby", "soft tissue", "cleaning", "detecting cracks", "flaw detection"])],
           model_answer="Ultrasound is sound of frequency above the upper limit of human hearing, i.e. above 20 kHz. Uses include sonar (measuring sea depth or locating objects) and medical scanning of soft tissue such as an unborn baby.",
           hints=["Humans hear from about 20 Hz to 20 kHz.", "Ultrasound is outside this range: which end?", "Give one use (ships or hospitals)."],
           keywords="frequency above 20 kHz; sonar / medical scanning",
           sample_pass=["sound with frequency above 20 kHz, used in sonar", "sound too high for humans to hear, used for scanning a fetus"], sample_fail=["very loud sound used in concerts", "sound below 20 Hz"])

# ================================================================= 11 / 10  Electromagnetic spectrum
definition("d_em_properties", "em", 2, "10a",
           stem="State **two** properties that all electromagnetic waves have in common.",
           points=[P("they are transverse waves", ["transverse"]),
                   P("they all travel at the same speed in a vacuum (3 × 10⁸ m/s)", ["same speed in a vacuum", "same speed in vacuum", "speed of light", "3 × 10^8", "3 x 10^8", "3 × 108", "3x108", "300 000 000", "3 × 10⁸", "same speed in free space"]),
                   P("they can travel through a vacuum / do not need a medium / transfer energy / obey v = fλ / can be reflected and refracted", ["through a vacuum", "no medium", "do not need a medium", "transfer energy", "carry energy", "v = fλ", "reflected", "refracted", "electric and magnetic fields"])],
           min_points=2,
           pitfalls=[PF(["longitudinal"], "Electromagnetic waves are TRANSVERSE, not longitudinal."),
                     PF(["same wavelength", "same frequency"], "They have different wavelengths and frequencies; what they share is the same SPEED in a vacuum.")],
           model_answer="All electromagnetic waves are transverse waves, travel at the same speed in a vacuum (3 × 10⁸ m/s), need no medium (can travel through a vacuum), transfer energy, and obey v = fλ.",
           hints=["Think about light, radio waves and X-rays: what is the same about all of them?", "One property is about the type of wave; another about how fast they go in empty space.", "Give two."],
           keywords="transverse; same speed in vacuum (3 × 10⁸ m/s); no medium needed",
           sample_pass=["they are transverse and travel at the same speed in a vacuum", "all travel at 3 × 10^8 m/s in a vacuum and need no medium"], sample_fail=["they all have the same wavelength", "they are longitudinal waves"])

definition("d_em_order", "em", 2, "10b",
           stem="List the regions of the electromagnetic spectrum in order of **increasing frequency**.",
           points=[P("radio, microwaves, infrared, visible light, ultraviolet, X-rays, gamma rays (in this order)", ["radio microwave infrared visible ultraviolet x gamma", "radio microwaves infrared light ultraviolet x gamma", "radio microwave infra red visible ultraviolet x gamma", "radio microwaves infrared visible uv x gamma", "radio microwaves ir visible uv x gamma", "radio microwaves infrared visible ultraviolet xrays gamma", "radio microwaves infrared visible uv xrays gamma"], ordered=True, window=20)],
           pitfalls=[PF(["gamma rays x rays ultraviolet", "gamma x ultraviolet", "gamma rays, x-rays, ultraviolet"], "That is the order of DECREASING frequency (increasing wavelength). Increasing frequency starts from radio waves.")],
           model_answer="Radio waves, microwaves, infrared, visible light, ultraviolet, X-rays, gamma rays (increasing frequency = decreasing wavelength).",
           hints=["Lowest frequency (longest wavelength) first.", "Radio waves have the longest wavelength; gamma rays the shortest.", "Seven regions: remember a mnemonic such as 'Raging Martians Invaded Venus Using X-ray Guns'."],
           keywords="radio, micro, IR, visible, UV, X, gamma",
           sample_pass=["radio waves, microwaves, infrared, visible light, ultraviolet, X-rays, gamma rays", "radio, microwaves, infra-red, visible, ultraviolet, X-rays, gamma"],
           sample_fail=["gamma rays, X-rays, ultraviolet, visible, infrared, microwaves, radio", "radio, infrared, microwaves, visible, X-rays, ultraviolet, gamma"])

definition("d_em_hazards", "em", 3, "10d",
           stem="Describe **two** hazardous effects that over-exposure to electromagnetic waves can have on living cells and tissue, naming the regions responsible.",
           points=[P("heating effect: microwaves / infrared heat body tissue (internal heating, burns)", ["heating", "heat", "burn", "cook"]),
                   P("ionising effect: ultraviolet, X-rays and gamma rays ionise atoms, damaging cells / DNA, causing mutations and cancer", ["ionis", "ioniz", "mutation", "cancer", "damage cells", "kill cells", "damage dna"]),
                   P("regions named: microwaves/infrared for heating; UV/X/gamma for ionising (UV also causes sunburn / skin cancer / eye damage)", ["microwave", "infrared", "ultraviolet", "uv", "x-ray", "x ray", "gamma", "sunburn", "skin cancer", "cataract"])],
           min_points=2,
           model_answer="Microwaves and infrared have a heating effect: they can heat internal tissue and cause burns. Ultraviolet, X-rays and gamma rays are ionising: they can damage or kill cells and alter DNA, causing mutations and cancer (UV also causes sunburn, skin cancer and eye damage).",
           hints=["Two kinds of damage: one is about temperature, one is about electrons being knocked off atoms.", "Which regions have enough energy to ionise?", "Name the effect and the region."],
           keywords="heating (microwaves, IR); ionising (UV, X-rays, gamma) -> cell damage, cancer",
           sample_pass=["Microwaves and infrared cause heating of tissue; UV, X-rays and gamma rays are ionising and can cause cancer", "ionising radiation like gamma damages DNA causing mutations; infrared burns the skin"],
           sample_fail=["radio waves cause cancer", "EM waves are dangerous because they are fast"])

# ================================================================= 12 / 11  Light
definition("d_light_normal_angles", "light", 1, "11a",
           stem="State what is meant by the **normal** and the **angle of incidence** at a reflecting surface.",
           points=[P("normal: a line perpendicular (at 90°) to the surface at the point of incidence", ["perpendicular to the surface", "at right angles to the surface", "90° to the surface", "90 degrees to the surface", "90° to the mirror", "90 degrees to the mirror", "perpendicular to the mirror", "right angles to the mirror", "perpendicular to the boundary", "90° to the boundary", "perpendicular to the reflecting"]),
                   P("angle of incidence: the angle between the incident ray and the normal", ["between the incident ray and the normal", "incident ray and the normal", "incident ray makes with the normal", "between the normal and the incident ray"])],
           pitfalls=[PF(["angle between the incident ray and the surface", "incident ray and the mirror", "ray and the surface"], "Angles in optics are measured from the NORMAL, not from the surface.")],
           model_answer="The normal is a line drawn perpendicular to the surface at the point where the ray strikes it. The angle of incidence is the angle between the incident ray and the normal.",
           hints=["The normal is a construction line.", "At what angle is it drawn to the surface?", "Angles of incidence, reflection and refraction are all measured from this line."],
           keywords="normal: perpendicular to surface; angle of incidence: between incident ray and normal",
           sample_pass=["the normal is perpendicular to the surface at the point of incidence; the angle of incidence is between the incident ray and the normal", "normal: line at 90° to the mirror; angle of incidence: angle the incident ray makes with the normal"],
           sample_fail=["the angle of incidence is between the incident ray and the mirror surface", "the normal is the reflected ray"])

definition("d_light_reflection_law", "light", 2, "11b",
           stem="State the **law of reflection**.",
           points=[P("the angle of incidence is equal to the angle of reflection", ["angle of incidence is equal to the angle of reflection", "angle of incidence equals the angle of reflection", "angle of incidence = angle of reflection", "angle of reflection is equal to the angle of incidence", "angle of reflection equals the angle of incidence", "i = r", "angle of incidence and the angle of reflection are equal"])],
           model_answer="The angle of incidence is equal to the angle of reflection (both measured from the normal); the incident ray, reflected ray and normal all lie in the same plane.",
           hints=["It compares two angles.", "Both are measured from the normal.", "Which two angles are equal?"],
           keywords="angle of incidence = angle of reflection",
           sample_pass=["the angle of incidence equals the angle of reflection", "angle of incidence = angle of reflection, measured from the normal"], sample_fail=["light bounces off a mirror", "the angle of incidence equals the angle of refraction"])

definition("d_light_refraction", "light", 2, "11c",
           stem="State what is meant by **refraction** of light, and state its cause.",
           points=[P("the bending (change of direction) of light as it passes from one medium to another", ["bending of light", "change in direction", "changes direction", "bends", "deviation of light"]),
                   P("caused by a change in the speed of light in the different media", ["change in speed", "changes speed", "different speeds", "slows down", "speeds up", "speed of light changes", "travels at different speed", "change of speed"])],
           pitfalls=[PF(["bounces", "reflected"], "That is reflection. Refraction is the BENDING of light as it crosses into a different medium.")],
           model_answer="Refraction is the bending (change in direction) of light when it passes from one medium to another, caused by the change in the speed of light between the two media.",
           hints=["A straw in water looks bent.", "What happens to the direction of the ray at the boundary?", "Why: what property of light changes when it enters glass or water?"],
           keywords="bending of light between media; due to change in speed",
           sample_pass=["the bending of light as it passes from one medium to another because its speed changes", "light changes direction at the boundary due to a change in speed"],
           sample_fail=["light bouncing off a surface", "light bends because glass is thick"])

definition("d_light_refractive_index", "light", 2, "11e",
           stem="Define the **refractive index** of a medium.",
           points=[P("the ratio of", ["ratio", "divided by", "over", "/", "÷"]),
                   P("the speed of light in a vacuum", ["speed of light in a vacuum", "speed of light in vacuum", "speed of light in free space", "speed of light in air"]),
                   P("to the speed of light in the medium", ["speed of light in the medium", "speed of light in that medium", "speed of light in the material", "speed in the medium", "speed of light in glass", "speed of light in water", "speed in the material", "speed of light in the substance"])],
           pitfalls=[PF(["speed of light in the medium to the speed of light in a vacuum", "speed of light in the medium to the speed of light in vacuum", "speed in the medium to the speed in a vacuum", "speed of light in the medium divided by the speed of light in a vacuum", "speed in the medium divided by the speed in a vacuum", "speed of light in the material to the speed of light in a vacuum"], "Upside down (examiner report 2020). Refractive index = speed in VACUUM ÷ speed in the MEDIUM, so it is greater than 1.")],
           model_answer="The refractive index of a medium is the ratio of the speed of light in a vacuum to the speed of light in the medium (n = c/v). It can also be found from n = sin i / sin r.",
           hints=["It is a ratio of two speeds.", "One is the speed of light in a vacuum; the other is its speed in the medium.", "Which one goes on top? Remember n is always greater than 1 for glass or water."],
           keywords="speed of light in vacuum ÷ speed of light in medium",
           sample_pass=["the ratio of the speed of light in a vacuum to the speed of light in the medium", "speed of light in vacuum divided by speed of light in the medium"],
           sample_fail=["the ratio of the speed of light in the medium to the speed of light in a vacuum", "how much light bends"])

definition("d_light_critical_angle", "light", 3, "12f",
           stem="Explain what is meant by the **critical angle**.", syllabi=PURE,
           points=[P("the angle of incidence in the (optically) denser medium", ["angle of incidence in the denser medium", "angle of incidence in the optically denser", "angle of incidence in glass", "angle of incidence in the medium", "angle of incidence in water", "angle of incidence"]),
                   P("for which the angle of refraction (in the less dense medium) is 90°", ["angle of refraction is 90", "angle of refraction equals 90", "angle of refraction of 90", "angle of refraction is 90°", "angle of refraction equals 90°", "angle of refraction of 90°", "angle of refraction = 90", "angle of refraction = 90°", "refracted ray travels along the boundary", "refracted ray grazes", "refracted along the surface", "refraction is 90", "refraction is 90°", "refracted at 90", "refracted at 90°", "refraction becomes 90", "refraction becomes 90°", "refraction reaches 90", "refraction reaches 90°"])],
           pitfalls=[PF(["angle of reflection is 90", "reflected at 90"], "It is the angle of REFRACTION that is 90°, not reflection."),
                     PF(["angle of incidence in the less dense", "angle of incidence in air", "incidence in the less dense medium", "angle of incidence in the air"], "The critical angle is the angle of incidence in the DENSER medium (e.g. in the glass), not in the air.")],
           model_answer="The critical angle is the angle of incidence in the optically denser medium for which the angle of refraction in the less dense medium is 90° (the refracted ray travels along the boundary).",
           hints=["Light is going from glass towards air.", "As the angle of incidence grows, the refracted ray bends further from the normal: what is the biggest possible angle of refraction?", "The critical angle is the angle of incidence that gives that."],
           keywords="angle of incidence in denser medium; angle of refraction = 90°",
           sample_pass=["the angle of incidence in the denser medium for which the angle of refraction is 90°", "angle of incidence in glass when the refracted ray travels along the boundary"],
           sample_fail=["the angle at which light is totally reflected", "the angle of incidence in air when the angle of refraction is 90°"])

definition("d_light_tir", "light", 3, "12f",
           stem="State the **two conditions** for total internal reflection to occur.", syllabi=PURE,
           points=[P("light must be travelling from an optically denser medium towards a less dense medium (e.g. glass to air)", ["denser medium to a less dense", "denser to less dense", "denser medium to the less dense", "from the denser medium", "from glass to air", "from water to air", "optically denser medium into", "denser medium towards", "more dense to less dense"]),
                   P("the angle of incidence must be greater than the critical angle", ["greater than the critical angle", "larger than the critical angle", "exceeds the critical angle", "more than the critical angle", "above the critical angle", "bigger than the critical angle"])],
           pitfalls=[PF(["less than the critical angle", "smaller than the critical angle"], "The angle of incidence must be GREATER than the critical angle."),
                     PF(["from air to glass", "less dense to denser", "from the less dense"], "Light must travel from the DENSER medium towards the LESS dense one (e.g. glass to air).")],
           model_answer="(1) Light must travel from an optically denser medium towards a less dense medium (e.g. from glass to air). (2) The angle of incidence in the denser medium must be greater than the critical angle.",
           hints=["One condition is about the direction between the two media.", "The other compares the angle of incidence with the critical angle.", "Both must be true."],
           keywords="denser to less dense; angle of incidence > critical angle",
           sample_pass=["light travels from a denser to a less dense medium and the angle of incidence is greater than the critical angle", "from glass to air with angle of incidence exceeding the critical angle"],
           sample_fail=["angle of incidence less than the critical angle", "light travels from air into glass at a large angle"])

definition("d_light_converging_action", "light", 2, "11f",
           stem="Describe the action of a thin **converging lens** on a beam of light parallel to its principal axis.",
           points=[P("the rays are refracted and converge (brought together) to a point", ["converge", "brought to a point", "meet at a point", "focused to a point", "brought together", "bend towards", "bend inwards", "come together"]),
                   P("at the principal focus (focal point) on the other side of the lens", ["principal focus", "focal point", "focus"])],
           model_answer="A thin converging lens refracts the parallel rays so that they converge and meet at a single point, the principal focus, on the far side of the lens.",
           hints=["Converging means coming together.", "What happens to parallel rays after passing through the lens?", "Name the point where they meet."],
           keywords="rays converge to the principal focus",
           sample_pass=["the rays converge to the principal focus on the other side", "parallel rays are refracted and meet at the focal point"], sample_fail=["the rays spread out", "the light is reflected"])

definition("d_light_focal_length", "light", 2, "11g",
           stem="Define the **focal length** of a converging lens.",
           points=[P("the distance", ["distance", "length between", "how far"]),
                   P("between the optical centre of the lens and the principal focus (focal point)", ["optical centre and the principal focus", "optical centre to the principal focus", "centre of the lens to the principal focus", "centre of the lens and the principal focus", "optical centre to the focal point", "optical centre and the focal point", "centre of the lens to the focal point", "lens to the principal focus", "lens to the focal point", "lens and the principal focus", "from the lens to the focus"]),
                   P("where rays parallel to the principal axis converge after passing through the lens", ["parallel rays converge", "parallel to the principal axis converge", "parallel rays meet", "parallel rays are brought to a focus", "parallel rays are focused", "parallel to the axis meet", "parallel rays come together", "parallel rays are brought together"])],
           min_points=2,
           pitfalls=[PF(["focal length is the point", "focal length is a point", "length is the point", "length is a point"], "Focal length is a DISTANCE, not a point (examiner reports 2018, 2023: many defined the focal point instead).")],
           model_answer="The focal length is the distance between the optical centre of the lens and the principal focus, the point on the principal axis where rays parallel to the axis converge after passing through the lens.",
           hints=["A length is a distance between two points.", "One is the optical centre of the lens. The other is where parallel rays meet.", "Say what the principal focus is as well (examiners expected this)."],
           keywords="distance from optical centre to principal focus (where parallel rays converge)",
           sample_pass=["the distance between the optical centre of the lens and the principal focus", "distance from the lens to the point where rays parallel to the principal axis converge"],
           sample_fail=["the point where parallel rays meet", "the length of the lens"])

definition("d_light_real_virtual", "light", 3, "11h",
           stem="Distinguish between a **real** image and a **virtual** image.",
           points=[P("a real image is formed where rays actually meet and can be formed (captured) on a screen", ["rays actually meet", "rays actually converge", "actual intersection", "real rays meet", "can be formed on a screen", "can be captured on a screen", "can be projected", "formed on a screen"]),
                   P("a virtual image is formed where rays only appear to come from (diverge from) and cannot be formed on a screen", ["appear to come from", "appear to diverge", "appear to meet", "seem to come from", "cannot be formed on a screen", "cannot be captured on a screen", "cannot be projected", "not on a screen"])],
           model_answer="A real image is formed where the rays of light actually meet, so it can be formed on a screen. A virtual image is formed where the rays only appear to come from; the rays do not actually pass through it, so it cannot be formed on a screen.",
           hints=["Think of a cinema projector versus a plane mirror.", "In one case the rays really meet; in the other they only appear to.", "Which can be caught on a screen?"],
           keywords="real: rays actually meet, on a screen; virtual: rays appear to come from, not on a screen",
           sample_pass=["a real image can be formed on a screen because the rays actually meet; a virtual image cannot, the rays only appear to come from it", "real: actual intersection of rays, can be projected; virtual: rays appear to diverge from it, cannot be captured on a screen"],
           sample_fail=["a real image is upright and a virtual image is inverted", "a real image is bigger"])

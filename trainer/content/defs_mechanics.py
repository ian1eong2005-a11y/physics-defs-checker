"""Definitions: Measurement, Kinematics, Forces / mass / weight, Newton's laws, Moments, Pressure, Energy.
Wording follows the 6091 / 5086 syllabus learning outcomes; pitfalls come from SEAB examiner reports 2016-2025."""
from ..marker import Pitfall, Point
from .base import BOTH, PURE, definition

P, PF = Point, Pitfall

# ================================================================= 1  Measurement
definition("d_meas_quantity", "meas", 1, "1a",
           stem="A physical quantity is written as '2.5 kg'. State the two parts that make up a physical quantity.",
           points=[P("a numerical magnitude and a unit", ["numerical magnitude and a unit", "number and a unit", "magnitude and a unit", "numerical value and a unit", "number and unit", "value and a unit"])],
           model_answer="A physical quantity consists of a numerical magnitude (2.5) and a unit (kg).",
           hints=["Look at 2.5 kg. One part is a number.", "The other part says what the number is counting.", "Name both parts in one sentence."],
           keywords="numerical magnitude, unit",
           sample_pass=["a number and a unit", "A numerical magnitude and a unit"], sample_fail=["mass and weight", "a decimal and letters"])

definition("d_meas_scalar_vector", "meas", 2, "1f",
           stem="State what is meant by a **scalar** quantity and a **vector** quantity. Give one example of each.",
           points=[P("scalar: magnitude (size) only", ["magnitude only", "size only", "magnitude but no direction", "size but no direction", "only magnitude", "only has magnitude", "has no direction"]),
                   P("vector: magnitude and direction", ["magnitude and direction", "size and direction", "both magnitude and direction"]),
                   P("examples (scalar: mass, speed, distance, time, energy, work; vector: force, velocity, displacement, acceleration, weight)", ["mass", "speed", "distance", "time", "energy", "work", "temperature", "force", "velocity", "displacement", "acceleration", "weight"])],
           pitfalls=[PF(["work is a vector", "energy is a vector", "work done is a vector"], "Work and energy are SCALARS (examiner report 2022: 'work' was often wrongly listed as a vector).")],
           model_answer="A scalar has magnitude only, e.g. mass, speed, distance, time, energy. A vector has both magnitude and direction, e.g. force, velocity, displacement, acceleration, weight.",
           hints=["One of them has a direction; the other does not.", "Does '5 N to the left' make sense? Does '5 kg to the left'?", "State the difference and give one example of each."],
           keywords="scalar: magnitude only; vector: magnitude and direction",
           sample_pass=["A scalar has magnitude only e.g. speed; a vector has magnitude and direction e.g. velocity", "scalar = size only like mass, vector = size and direction like force"],
           sample_fail=["A scalar is small and a vector is big", "Vectors have direction, e.g. work done"])

definition("d_meas_period", "meas", 1, "1e",
           stem="State what is meant by the **period** of a simple pendulum.",
           points=[P("time taken for one complete oscillation", ["time for one complete oscillation", "time taken for one oscillation", "time for one complete swing", "time for one full swing", "time taken for one complete cycle", "time for one complete to and fro", "time for one complete vibration", "time for 1 complete", "time for 1 oscillation", "time taken for 1 complete", "time for one oscillation"])],
           pitfalls=[PF(["number of oscillations per", "oscillations per second", "oscillations in one second"], "Oscillations per second is the FREQUENCY. Period is a time.")],
           model_answer="The period is the time taken for one complete oscillation (one full swing there and back).",
           hints=["A period is a time.", "The time for how much of the motion?", "One complete oscillation means back to the start, moving the same way."],
           keywords="time for one complete oscillation",
           sample_pass=["the time taken for one complete oscillation", "time for 1 complete swing"], sample_fail=["the number of swings per second", "how long the string is"])

definition("d_meas_precision_instruments", "meas", 3, "1e",
           stem="State the precision of (i) a metre rule, (ii) a pair of vernier calipers and (iii) a micrometer screw gauge.",
           points=[P("metre rule: 0.1 cm (1 mm)", ["0.1 cm", "1 mm", "0.001 m"]),
                   P("vernier calipers: 0.01 cm (0.1 mm)", ["0.01 cm", "0.1 mm"]),
                   P("micrometer: 0.001 cm (0.01 mm)", ["0.01 mm", "0.001 cm"])],
           model_answer="Metre rule: 0.1 cm (1 mm). Vernier calipers: 0.01 cm (0.1 mm). Micrometer screw gauge: 0.001 cm (0.01 mm).",
           hints=["Each instrument is ten times more precise than the one before.", "A metre rule reads to the nearest millimetre.", "Give all three, with units."],
           keywords="0.1 cm, 0.01 cm, 0.001 cm",
           sample_pass=["metre rule 0.1 cm, vernier 0.01 cm, micrometer 0.001 cm", "1 mm, 0.1 mm and 0.01 mm"], sample_fail=["1 cm, 1 mm, 1 mm", "they are all 0.1 cm"])

# ================================================================= 2  Kinematics
definition("d_kin_speed", "kin", 1, "2a",
           stem="State what is meant by **speed**.",
           points=[P("distance travelled per unit time", ["distance travelled per unit time", "distance per unit time", "distance moved per unit time", "rate of change of distance", "distance travelled per second", "distance moved per second", "distance covered per second", "distance per second", "distance travelled in one second", "distance divided by time", "distance / time", "distance over time", "distance travelled divided by time"])],
           pitfalls=[PF(["displacement per unit time", "rate of change of displacement"], "That is VELOCITY. Speed is the distance travelled per unit time, with no direction.")],
           model_answer="Speed is the distance travelled per unit time.",
           hints=["Speed tells you how far you go in a given time.", "Use the words 'distance' and 'time'.", "Per unit time means 'in each second'."],
           keywords="distance travelled per unit time",
           sample_pass=["Distance travelled per unit time", "the distance moved per second"], sample_fail=["How fast something is going", "displacement per unit time"])

definition("d_kin_velocity", "kin", 1, "2a",
           stem="State what is meant by **velocity**.",
           points=[P("rate of change of displacement (distance travelled per unit time in a specified direction)", ["rate of change of displacement", "displacement per unit time", "change in displacement per unit time", "displacement divided by time", "displacement / time", "distance per unit time in a specified direction", "distance travelled per unit time in a given direction", "distance per unit time in a stated direction", "speed in a specified direction", "speed in a given direction", "speed in a stated direction", "speed in a particular direction"])],
           pitfalls=[PF(["rate of change of displacement per unit time"], "'Rate of change of displacement PER UNIT TIME' double-counts the time and reads like the definition of acceleration (examiner report 2022). Say 'rate of change of displacement' OR 'displacement per unit time'."),
                     PF(["rate of change of velocity"], "Rate of change of velocity is ACCELERATION.")],
           model_answer="Velocity is the rate of change of displacement, i.e. the distance travelled per unit time in a specified direction.",
           hints=["Velocity is a vector, so direction matters.", "It is like speed, but uses displacement instead of distance.", "Say 'rate of change of displacement' or 'displacement per unit time' (not both together)."],
           keywords="rate of change of displacement; direction",
           sample_pass=["rate of change of displacement", "distance travelled per unit time in a specified direction"], sample_fail=["rate of change of displacement per unit time", "how fast an object moves"])

definition("d_kin_acceleration", "kin", 1, "2c",
           stem="State what is meant by **acceleration**.",
           points=[P("rate of change of velocity", ["rate of change of velocity", "change in velocity per unit time", "change of velocity per unit time", "velocity change per unit time", "change in velocity divided by time taken", "change in velocity / time", "change in velocity over time"])],
           pitfalls=[PF(["rate of change of speed", "change in speed per unit time", "increase in speed per unit time"], "Acceleration is the rate of change of VELOCITY (a vector): a change of direction at constant speed is also an acceleration. 'Speed' loses the mark.")],
           model_answer="Acceleration is the rate of change of velocity (change in velocity per unit time).",
           hints=["Acceleration describes how quickly something changes.", "The quantity that changes is a vector.", "Say 'rate of change of ...' or 'change in ... per unit time'."],
           keywords="rate of change of velocity",
           sample_pass=["rate of change of velocity", "change in velocity per unit time"], sample_fail=["rate of change of speed", "getting faster"])

definition("d_kin_uniform_accel", "kin", 2, "2c",
           stem="State what is meant by **uniform acceleration**.",
           points=[P("velocity changes by equal amounts in equal intervals of time (constant rate of change of velocity)", ["velocity changes by equal amounts in equal", "equal changes in velocity in equal", "same change in velocity every second", "constant rate of change of velocity", "rate of change of velocity is constant", "velocity changes at a constant rate", "acceleration is constant", "constant acceleration", "velocity increases by the same amount every second"])],
           pitfalls=[PF(["constant velocity", "velocity stays the same", "velocity remains constant", "velocity does not change", "velocity remains the same"], "Constant VELOCITY means zero acceleration. Uniform acceleration means the velocity changes at a steady rate.")],
           model_answer="Uniform acceleration means the velocity changes by equal amounts in equal intervals of time, i.e. the rate of change of velocity is constant.",
           hints=["'Uniform' means the same throughout.", "What stays the same: the velocity, or the change in velocity each second?", "Put it as 'velocity changes by ... in ...'."],
           keywords="equal changes in velocity in equal time intervals",
           sample_pass=["the velocity changes by equal amounts in equal time intervals", "constant rate of change of velocity"], sample_fail=["the velocity is constant", "it speeds up"])

definition("d_kin_free_fall", "kin", 2, "2i",
           stem="State the value of the acceleration of free fall near the Earth's surface, and state what this value tells you about the motion of a falling body (ignoring air resistance).",
           points=[P("about 10 m/s² (9.8 m/s²)", ["10 m/s2", "10 m/s^2", "9.8 m/s2", "9.81 m/s2", "10 ms-2", "10 metres per second squared", "10 m s-2", "approximately 10"]),
                   P("constant acceleration: velocity increases by 10 m/s every second, the same for all masses", ["constant", "uniform", "same for all", "regardless of mass", "independent of mass", "increases by 10 m/s every second"])],
           model_answer="The acceleration of free fall is constant at approximately 10 m/s² near the Earth: a falling body's velocity increases by about 10 m/s every second, whatever its mass.",
           hints=["Give a number with a unit.", "Is this acceleration the same throughout the fall? Does it depend on the mass?", "State the value and say that it is constant."],
           keywords="10 m/s², constant, independent of mass",
           sample_pass=["g is about 10 m/s2 and is constant for all objects", "9.8 m/s², uniform acceleration regardless of mass"], sample_fail=["10 m/s", "it falls faster if heavier"])

definition("d_kin_terminal_velocity", "newton", 3, "3m",
           stem="State what is meant by **terminal velocity**, and explain why a falling body reaches it.", syllabi=PURE,
           points=[P("the constant (maximum) velocity reached by a falling body", ["constant velocity", "maximum velocity", "constant speed", "maximum speed", "velocity stops increasing", "no longer accelerates", "stops accelerating"]),
                   P("because air resistance has grown to equal the weight, so the resultant force (and acceleration) is zero", ["air resistance equals the weight", "air resistance equal to weight", "air resistance is equal to the weight", "drag equals weight", "air resistance balances the weight", "resultant force is zero", "net force is zero", "forces are balanced", "zero acceleration", "acceleration is zero"])],
           pitfalls=[PF(["no forces act", "no force acts", "gravity stops"], "Forces still act: the weight and air resistance are equal and opposite, so the RESULTANT force is zero.")],
           model_answer="Terminal velocity is the constant maximum velocity reached by a falling body when the air resistance has increased to equal its weight, so the resultant force and the acceleration are zero.",
           hints=["Air resistance increases as the body speeds up.", "What happens to the resultant force when air resistance equals weight?", "Say what the velocity does from then on."],
           keywords="constant velocity; air resistance = weight; resultant force zero",
           sample_pass=["constant velocity reached when air resistance equals the weight so resultant force is zero", "maximum speed where drag balances weight and acceleration is zero"],
           sample_fail=["the fastest speed before hitting the ground", "when gravity stops acting"])

# ================================================================= 3  Forces, mass, weight, gravitational field
definition("d_mwg_mass", "mwg", 1, "3b",
           stem="State what is meant by the **mass** of a body.",
           points=[P("a measure of the amount of matter in a body", ["amount of matter", "quantity of matter", "measure of the matter", "amount of substance in a body"])],
           pitfalls=[PF(["force of gravity", "gravitational force", "pull of gravity"], "That is WEIGHT. Mass is the amount of matter and does not depend on gravity."),
                     PF(["how heavy"], "'How heavy' describes weight. Mass is the amount of matter in the body.")],
           model_answer="Mass is a measure of the amount of matter in a body.",
           hints=["Mass is not a force.", "It is about what the body is made of.", "Use the word 'matter'."],
           keywords="amount of matter",
           sample_pass=["the amount of matter in a body", "a measure of the quantity of matter in an object"], sample_fail=["the force of gravity on a body", "how heavy it is"])

definition("d_mwg_weight", "mwg", 1, "3e",
           stem="State what is meant by the **weight** of a body.",
           points=[P("the gravitational force acting on the body (force of gravity on its mass)", ["gravitational force acting on", "gravitational force on", "force of gravity acting on", "force of gravity on", "force due to gravity", "gravitational pull on", "pull of gravity on", "gravitational force experienced"])],
           pitfalls=[PF(["amount of matter"], "Amount of matter is MASS. Weight is the gravitational force on that mass."),
                     PF(["gravitational field strength"], "Gravitational field strength is force PER UNIT MASS (N/kg). Weight is the force itself (N).")],
           model_answer="Weight is the gravitational force acting on a body (the force of gravity on its mass); W = mg.",
           hints=["Weight is a force, measured in newtons.", "Which force? Caused by what?", "Say 'the ... force acting on the body'."],
           keywords="gravitational force acting on a body",
           sample_pass=["the gravitational force acting on an object", "the force of gravity on a mass"], sample_fail=["the amount of matter in a body", "how heavy an object is in kg"])

definition("d_mwg_grav_field", "mwg", 2, "3c",
           stem="State what is meant by a **gravitational field**.",
           points=[P("a region (of space)", ["region", "region of space", "space around", "area around"]),
                   P("in which a mass experiences a force due to gravitational attraction", ["mass experiences a force", "mass experiences a gravitational force", "mass feels a force", "force acts on a mass", "mass is acted on by a force", "mass experiences gravitational attraction", "mass experiences an attractive force"])],
           pitfalls=[PF(["field is the force", "field is a force", "the force of gravity on"], "A field is a REGION, not a force (examiner report 2021: candidates said 'the field is the force or the amount rather than a region').")],
           model_answer="A gravitational field is a region in which a mass experiences a force due to gravitational attraction.",
           hints=["A field is a place, not a force.", "What kind of object feels a force there?", "Start with 'a region in which ...'."],
           keywords="region; mass experiences a force",
           sample_pass=["a region in which a mass experiences a force due to gravitational attraction", "the region of space where a mass feels a gravitational force"],
           sample_fail=["the force of gravity on an object", "the pull of the Earth"])

definition("d_mwg_g_strength", "mwg", 2, "3d",
           stem="Define **gravitational field strength**, g.",
           points=[P("gravitational force per unit mass (acting on a mass placed at that point)", ["gravitational force per unit mass", "force per unit mass", "gravitational force acting per unit mass", "gravitational force per kg", "gravitational force per kilogram", "weight per unit mass", "force acting on each kilogram"])],
           pitfalls=[PF(["mass per unit force"], "The other way round: g is FORCE per unit MASS."),
                     PF(["force per unit weight", "weight per unit force"], "Per unit MASS, not weight.")],
           model_answer="Gravitational field strength is the gravitational force per unit mass acting on a mass placed at that point (g = W/m, unit N/kg).",
           hints=["The unit N/kg is a big clue.", "'Per unit mass' means 'for each kilogram'.", "Say which force, per unit of what."],
           keywords="gravitational force per unit mass",
           sample_pass=["the gravitational force per unit mass", "gravitational force acting per kg of mass at that point"], sample_fail=["the acceleration of gravity", "the weight of an object"])

definition("d_mwg_contact_noncontact", "mwg", 3, "3a",
           stem="Distinguish between **contact** and **non-contact** forces, giving two examples of each.",
           points=[P("contact forces act only when objects touch; non-contact forces act at a distance", ["touch", "in contact", "touching", "physical contact", "at a distance", "without touching", "without contact", "not in contact"]),
                   P("contact examples: friction, air resistance, tension, normal (contact) force", ["friction", "air resistance", "tension", "normal force", "normal contact force", "drag", "upthrust"]),
                   P("non-contact examples: gravitational, electrostatic (electric), magnetic", ["gravitational", "gravity", "weight", "electrostatic", "electric force", "magnetic"])],
           pitfalls=[PF(["gravity is a contact force", "gravity are both contact", "gravity are contact forces", "gravitational is a contact", "weight is a contact force", "magnetic is a contact force", "magnetic force is a contact", "friction is a non-contact", "tension is a non-contact", "friction is non-contact"], "Gravitational, electrostatic and magnetic forces act at a distance: they are NON-contact. Friction, tension, air resistance and the normal force need contact.")],
           model_answer="Contact forces act between objects that are touching, e.g. friction, air resistance, tension and the normal force. Non-contact forces act at a distance without the objects touching, e.g. gravitational, electrostatic and magnetic forces.",
           hints=["Think about whether the objects need to touch.", "Which forces act through empty space?", "Give the difference and two examples of each kind."],
           keywords="touching vs at a distance; friction, tension; gravitational, magnetic",
           sample_pass=["Contact forces need the objects to touch, e.g. friction and tension; non-contact act at a distance, e.g. gravitational and magnetic", "friction and air resistance act in contact; gravity and electrostatic forces act without touching"],
           sample_fail=["contact forces are stronger", "friction and gravity are both contact forces because they touch"])

definition("d_mwg_mass_vs_weight", "mwg", 5, "3f",
           stem="State **three** differences between mass and weight.",
           points=[P("mass is the amount of matter; weight is the gravitational force on it", ["amount of matter", "gravitational force", "force of gravity", "force due to gravity"]),
                   P("mass is a scalar; weight is a vector", ["scalar", "vector"]),
                   P("units: mass in kg; weight in N", ["kg", "kilogram", "newton", " n "]),
                   P("mass is constant everywhere; weight changes with gravitational field strength (place)", ["constant everywhere", "same everywhere", "does not change", "changes with location", "depends on gravitational field", "depends on g", "varies from place to place", "different on the moon", "changes from place to place"]),
                   P("measured with a beam balance (mass) vs spring balance / newton meter (weight)", ["beam balance", "electronic balance", "spring balance", "newton meter", "force meter"])],
           min_points=3,
           model_answer="Mass is the amount of matter in a body, a scalar, measured in kg, and is the same everywhere. Weight is the gravitational force on the body, a vector, measured in N, and changes with the gravitational field strength (e.g. smaller on the Moon). Mass is measured with a beam balance, weight with a spring balance.",
           hints=["Think: what each one is, its unit, scalar or vector, and whether it changes on the Moon.", "One is a force, the other is not.", "Give three clear contrasts."],
           keywords="matter vs force; scalar vs vector; kg vs N; constant vs depends on g",
           sample_pass=["Mass is the amount of matter and is a scalar in kg; weight is the gravitational force, a vector in N, and changes with location", "mass constant everywhere, weight depends on g; mass kg, weight N; mass scalar, weight vector"],
           sample_fail=["mass is smaller than weight", "mass is in kg"])

# ================================================================= 3/4  Newton's laws, friction, inertia
definition("d_newton_resultant", "newton", 2, "4a",
           stem="State what is meant by the **resultant force** on a body.",
           points=[P("the single force that has the same effect as all the forces acting together (vector sum)", ["single force that has the same effect", "one force that has the same effect", "same effect as all the forces", "vector sum of all the forces", "sum of all the forces", "net force", "overall force", "combination of all the forces", "all the forces added"])],
           model_answer="The resultant force is the single force that has the same effect on the body as all the individual forces acting together (the vector sum of the forces).",
           hints=["Several forces can be replaced by one.", "That one force must do the same job as all of them.", "Use 'single force' and 'same effect'."],
           keywords="single force with the same effect as all the forces",
           sample_pass=["the single force that has the same effect as all the forces acting on the body", "the vector sum of all the forces"], sample_fail=["the biggest force on the body", "the force that results"])

definition("d_newton_balanced", "newton", 3, "4a",
           stem="Describe the motion of a body when the forces acting on it are **balanced** (resultant force zero).",
           points=[P("it stays at rest, or", ["remains at rest", "stays at rest", "stay stationary", "remains stationary", "at rest"]),
                   P("continues moving at constant velocity (constant speed in a straight line)", ["constant velocity", "uniform velocity", "constant speed in a straight line", "same speed in a straight line", "moves at a steady speed in a straight line", "does not accelerate", "no acceleration", "zero acceleration"])],
           pitfalls=[PF(["slows down", "comes to a stop", "stops moving", "decelerates"], "No. With zero resultant force a moving body keeps its velocity; it does not slow down.")],
           model_answer="With balanced forces (zero resultant force) a body at rest stays at rest, and a moving body continues to move at constant velocity, i.e. at constant speed in a straight line.",
           hints=["Two cases: a body that is still, and one that is already moving.", "Zero resultant force means zero acceleration.", "What does zero acceleration mean for a moving body's velocity?"],
           keywords="at rest stays at rest; moving body keeps constant velocity",
           sample_pass=["it stays at rest or moves at constant velocity", "remains stationary or keeps moving at constant speed in a straight line"], sample_fail=["it slows down and stops", "it accelerates"])

definition("d_newton_unbalanced", "newton", 3, "4a",
           stem="Describe the ways in which an **unbalanced** (resultant) force may change the motion of a body.",
           points=[P("it accelerates the body in the direction of the resultant force (F = ma)", ["accelerate", "acceleration", "f = ma", "changes its velocity", "change in velocity"]),
                   P("i.e. it can change the speed (speed up or slow down) and/or change the direction of motion", ["speed up", "slow down", "increase its speed", "decrease its speed", "change its speed", "change in speed", "change its direction", "change of direction", "changes direction"])],
           min_points=2,
           model_answer="A resultant force produces an acceleration in the direction of the force (F = ma): it can make the body speed up, slow down, or change direction.",
           hints=["Newton's second law.", "Acceleration can mean more than just speeding up.", "Mention speed and direction."],
           keywords="acceleration; change speed and/or direction",
           sample_pass=["it accelerates the body: it can speed it up, slow it down or change its direction", "produces an acceleration, changing the speed or direction of motion"],
           sample_fail=["it keeps it moving", "the body stays at constant velocity"])

definition("d_newton_action_reaction", "newton", 4, "4a",
           stem="State the features of an **action-reaction pair** of forces (Newton's third law).",
           points=[P("equal in magnitude", ["equal in magnitude", "equal in size", "same magnitude", "same size", "equal and opposite", "equal but opposite"]),
                   P("opposite in direction", ["opposite in direction", "opposite direction", "equal and opposite", "equal but opposite", "opposite directions"]),
                   P("act on different bodies", ["different bodies", "different objects", "on each other", "on the other body", "two different"]),
                   P("same type of force", ["same type", "same kind", "same nature"])],
           min_points=3,
           pitfalls=[PF(["same body", "same object", "act on the same"], "Action and reaction act on DIFFERENT bodies: that is why they never cancel. Two balanced forces on the same body are NOT an action-reaction pair (examiner report 2020).")],
           model_answer="The two forces are equal in magnitude, opposite in direction, of the same type, and act on two different bodies (each body exerts one force on the other).",
           hints=["Think of you pushing a wall: where does each force act?", "Compare their sizes, directions and types.", "List at least three features."],
           keywords="equal, opposite, same type, on different bodies",
           sample_pass=["equal in magnitude, opposite in direction, acting on different bodies", "they are equal and opposite, of the same type, and act on two different objects"],
           sample_fail=["equal and opposite forces on the same body that cancel", "the ground pushes back"])

definition("d_newton_inertia", "newton", 2, "3k",
           stem="State what is meant by **inertia**, and state what it depends on.", syllabi=PURE,
           points=[P("the reluctance of a body to change its state of rest or motion (resists change in motion)", ["reluctance to change", "resists change in motion", "resistance to change in motion", "resists a change in its state", "tendency to remain at rest or", "tendency to resist", "opposes any change in its motion", "reluctance of a body to start moving or"]),
                   P("depends on the mass: the greater the mass, the greater the inertia", ["mass", "depends on the mass", "greater mass"])],
           pitfalls=[PF(["depends on the weight", "depends on weight", "depends on its speed"], "Inertia depends on MASS only, not on weight or speed.")],
           model_answer="Inertia is the reluctance of a body to change its state of rest or of motion. It depends only on the mass of the body: the larger the mass, the larger the inertia.",
           hints=["Why is a loaded trolley harder to start and harder to stop?", "Inertia is about resisting change in motion.", "Name the property of the body that inertia depends on."],
           keywords="reluctance to change state of rest or motion; mass",
           sample_pass=["the reluctance of a body to change its state of rest or motion; it depends on mass", "a body resists change in motion, and the more mass the more inertia"],
           sample_fail=["the force that keeps a body moving", "it depends on the weight of the body"])

definition("d_newton_friction", "newton", 3, "4d",
           stem="State **two** effects of friction on the motion of a body.",
           points=[P("opposes (relative) motion between surfaces in contact, slowing the body / reducing its speed", ["opposes motion", "opposes the motion", "opposes relative motion", "acts against the motion", "opposite to the direction of motion", "slows", "decelerate", "reduces its speed", "brings it to rest", "resists motion"]),
                   P("converts kinetic energy to thermal energy (heating / wear) OR provides the grip needed to walk, drive or stop", ["thermal energy", "heat", "wear", "grip", "traction", "allows us to walk", "lets us walk", "needed for walking", "tyres grip", "enables us to"])],
           model_answer="Friction acts opposite to the motion between two surfaces in contact, slowing the body down (deceleration) and converting kinetic energy to thermal energy and causing wear. It is also useful: it gives the grip that lets us walk, drive and brake.",
           hints=["Which direction does friction act relative to motion?", "What happens to the kinetic energy that friction removes?", "Give two effects."],
           keywords="opposes motion, slows down; heating / wear; grip",
           sample_pass=["it opposes motion and slows the body down, producing heat", "friction acts against the motion, decelerating the body, and lets tyres grip the road"],
           sample_fail=["friction makes things move faster", "friction is a contact force"])

# ================================================================= 4/5  Turning effects of forces
definition("d_mom_moment", "moments", 1, "5b",
           stem="Define the **moment of a force** about a pivot.",
           points=[P("product of the force and the perpendicular distance from the pivot to the line of action of the force", ["force and the perpendicular distance", "force multiplied by the perpendicular distance", "force times the perpendicular distance", "force * perpendicular distance", "force × perpendicular distance", "product of force and perpendicular distance", "force x perpendicular distance"]),
                   P("'perpendicular' and 'from the pivot (to the line of action)' both stated", ["perpendicular distance from the pivot", "perpendicular distance between the pivot", "perpendicular distance to the pivot", "perpendicular distance from the line of action"])],
           pitfalls=[PF(["turning force"], "A moment is the turning EFFECT of a force, not a 'turning force'. Define it as force × perpendicular distance from the pivot."),
                     PF(["clockwise moments equal", "sum of clockwise", "total clockwise"], "That is the PRINCIPLE of moments, not the definition of a moment (examiner report 2023).")],
           model_answer="The moment of a force about a pivot is the product of the force and the perpendicular distance from the pivot to the line of action of the force.",
           hints=["It is a product of two quantities.", "One is the force; the other is a distance measured in a particular way from the pivot.", "The distance must be perpendicular to the line of action of the force."],
           keywords="force × perpendicular distance from pivot to line of action",
           sample_pass=["the product of the force and the perpendicular distance from the pivot to the line of action of the force", "force × perpendicular distance from the pivot"],
           sample_fail=["force times distance", "the turning force about a pivot"])

definition("d_mom_principle", "moments", 3, "5c",
           stem="State the **principle of moments**.",
           points=[P("for a body in equilibrium", ["equilibrium", "balanced", "not rotating", "not turning"]),
                   P("the sum of clockwise moments equals the sum of anticlockwise moments", ["sum of clockwise moments is equal to the sum of anticlockwise", "sum of clockwise moments equals the sum of anticlockwise", "total clockwise moment equals the total anticlockwise", "total clockwise moments equal total anticlockwise", "clockwise moments equal anticlockwise moments", "clockwise moment is equal to the anticlockwise moment", "sum of the clockwise moments = sum of the anticlockwise", "clockwise moments = anticlockwise moments", "anticlockwise moments equal the clockwise"]),
                   P("about the same pivot (any point)", ["about the same pivot", "about the same point", "about any point", "about any pivot", "about a pivot", "about the pivot", "same point"])],
           pitfalls=[PF(["force times perpendicular distance", "force × perpendicular distance", "product of force and perpendicular"], "That is the definition of a MOMENT. The principle of moments is about clockwise and anticlockwise moments being equal in equilibrium.")],
           model_answer="When a body is in equilibrium, the sum of the clockwise moments about any point is equal to the sum of the anticlockwise moments about the same point.",
           hints=["Start with the condition: when is the principle true?", "Compare the clockwise turning effects with the anticlockwise ones.", "Say about which point the moments are taken (examiner report 2025: many forgot 'in equilibrium')."],
           keywords="equilibrium; sum of clockwise moments = sum of anticlockwise moments; same pivot",
           sample_pass=["For a body in equilibrium, the sum of clockwise moments about any point equals the sum of anticlockwise moments about the same point", "when balanced, total clockwise moment = total anticlockwise moment about the pivot"],
           sample_fail=["moment = force × perpendicular distance from pivot", "clockwise moments equal anticlockwise moments"])

definition("d_mom_cg", "moments", 2, "5e",
           stem="State what is meant by the **centre of gravity** of a body.",
           points=[P("the point", ["point", "single point", "position"]),
                   P("through which the whole weight of the body appears to act", ["weight appears to act", "weight seems to act", "weight acts", "whole weight", "entire weight", "weight is considered to act", "weight can be taken to act", "weight may be taken as acting", "weight is taken to act"])],
           pitfalls=[PF(["centre of the object", "middle of the object", "centre of the body"], "Not simply the middle of the object: it is the point through which the whole WEIGHT appears to act."),
                     PF(["mass is concentrated", "where the mass is"], "That is centre of mass. For this syllabus, talk about where the WEIGHT appears to act (examiner report 2019).")],
           model_answer="The centre of gravity is the point through which the whole weight of the body appears to act.",
           hints=["It is a point.", "Which force seems to act at that point?", "Use 'whole weight' and 'appears to act'."],
           keywords="point through which the whole weight appears to act",
           sample_pass=["the point through which the whole weight of the body appears to act", "the single point where the entire weight seems to act"], sample_fail=["the centre of the object", "where the mass is concentrated"])

definition("d_mom_equilibrium", "moments", 3, "5c",
           stem="State the **two conditions** for a body to be in equilibrium.",
           points=[P("the resultant force on it is zero (forces balanced)", ["resultant force is zero", "net force is zero", "resultant force zero", "sum of forces is zero", "forces are balanced", "no resultant force"]),
                   P("the resultant moment about any point is zero (sum of clockwise moments = sum of anticlockwise)", ["resultant moment is zero", "net moment is zero", "resultant moment zero", "sum of moments is zero", "no resultant moment", "clockwise moments equal anticlockwise", "clockwise moments = anticlockwise", "sum of clockwise moments equals", "total clockwise moment equals"])],
           model_answer="(1) The resultant force on the body is zero. (2) The resultant moment about any point is zero, i.e. the sum of clockwise moments equals the sum of anticlockwise moments.",
           hints=["One condition is about forces, the other about turning.", "What must the resultant force be?", "What must the resultant moment be?"],
           keywords="resultant force = 0; resultant moment = 0",
           sample_pass=["resultant force is zero and resultant moment is zero", "forces balanced, and clockwise moments equal anticlockwise moments"], sample_fail=["it is not moving", "the weight acts at the centre of gravity"])

definition("d_mom_stability", "moments", 4, "4f",
           stem="State **two** ways of making an object more stable, and explain why each works.", syllabi=PURE,
           points=[P("lower the centre of gravity", ["lower centre of gravity", "lower the centre of gravity", "low centre of gravity", "lowering the centre of gravity", "centre of gravity lower", "lower c.g."]),
                   P("widen the base area", ["wider base", "wide base", "larger base", "broader base", "increase the base", "widen the base", "bigger base"]),
                   P("because the line of action of the weight stays within the base when tilted, so the moment of the weight restores it (it must tilt further before toppling)", ["line of action of the weight", "weight stays within the base", "weight acts within the base", "within the base", "inside the base", "tilted further before", "tilt more before", "restoring moment", "moment of the weight returns", "returns to its original position"])],
           model_answer="Lower the centre of gravity and widen the base. Both mean the object can be tilted through a larger angle before the line of action of its weight falls outside the base, so the moment of the weight turns it back to its original position instead of toppling it.",
           hints=["Think of a racing car versus a bus.", "Where is the centre of gravity, and how big is the base?", "Explain in terms of where the line of action of the weight falls when the object is tilted."],
           keywords="lower centre of gravity; wider base; line of action of weight within base",
           sample_pass=["Lower the centre of gravity and widen the base, so that when tilted the line of action of the weight stays within the base and the weight's moment returns it", "A wider base and a lower c.g. mean it must be tilted further before the weight acts outside the base"],
           sample_fail=["make it heavier", "lower the centre of gravity and make it taller"])

# ================================================================= 5/3  Pressure and density
definition("d_pres_pressure", "pressure", 1, "3h",
           stem="Define **pressure**.",
           points=[P("force (acting perpendicularly) per unit area", ["force per unit area", "force acting per unit area", "force acting normally per unit area", "perpendicular force per unit area", "normal force per unit area", "force divided by area", "force / area", "force over area", "force exerted per unit area"])],
           pitfalls=[PF(["force on an area", "force acting on an area", "force on a surface", "force acting on a surface", "force on the area"], "'Force on an area' does not define pressure (examiner reports 2021, 2022). It must be force PER UNIT area (force divided by area)."),
                     PF(["area per unit force"], "The other way round: pressure is force per unit area.")],
           model_answer="Pressure is the force acting per unit area (p = F/A).",
           hints=["The unit N/m² is the clue.", "'Per unit area' means 'on each square metre'.", "Say 'force per unit area' (not 'force on an area')."],
           keywords="force per unit area",
           sample_pass=["force per unit area", "the force acting normally per unit area"], sample_fail=["the force on an area", "how hard something presses"])

definition("d_pres_density", "pressure", 1, "3g",
           stem="Define **density**.",
           points=[P("mass per unit volume", ["mass per unit volume", "mass divided by volume", "mass / volume", "mass over volume", "mass per cubic metre", "mass of a unit volume", "mass in one unit of volume"])],
           pitfalls=[PF(["volume per unit mass"], "Other way round: density is MASS per unit VOLUME."),
                     PF(["weight per unit volume"], "Density uses MASS (kg), not weight (N).")],
           model_answer="Density is the mass per unit volume of a substance (ρ = m/V).",
           hints=["The unit kg/m³ is the clue.", "It compares two quantities: one in kg, one in m³.", "Say '... per unit ...'."],
           keywords="mass per unit volume",
           sample_pass=["mass per unit volume", "the mass of a substance divided by its volume"], sample_fail=["how heavy something is for its size", "volume per unit mass"])

definition("d_pres_hydraulic", "pressure", 3, "5c",
           stem="State the principle on which a **hydraulic press** works, and explain why a small force on the small piston can lift a large load on the large piston.", syllabi=PURE,
           points=[P("pressure is transmitted equally (undiminished) throughout an enclosed liquid (liquids are incompressible)", ["pressure is transmitted equally", "pressure is transmitted throughout", "pressure is the same throughout", "same pressure throughout", "transmitted undiminished", "pressure at both pistons is the same", "equal pressure at both pistons", "same pressure at both pistons", "pressure is equal at both"]),
                   P("so the same pressure on a larger area gives a larger force (F = pA)", ["larger area", "bigger area", "greater area", "f = pa", "force = pressure × area", "force is pressure times area", "same pressure on a larger"])],
           pitfalls=[PF(["force is transmitted", "same force"], "It is the PRESSURE that is transmitted equally, not the force. The forces differ because the areas differ.")],
           model_answer="The pressure applied to an enclosed liquid is transmitted equally to every part of the liquid. The pressure at the large piston is the same as at the small piston, and since F = pA, the same pressure acting on a larger area produces a larger force.",
           hints=["Liquids cannot be squashed.", "What quantity is the same at both pistons: force or pressure?", "Then use F = pA on the larger area."],
           keywords="pressure transmitted equally; F = pA on larger area",
           sample_pass=["Pressure is transmitted equally throughout the liquid, so the same pressure on the larger area gives a larger force", "the pressure at both pistons is the same and F = pA so the bigger piston has the bigger force"],
           sample_fail=["the force is transmitted through the liquid", "the liquid pushes harder on the big piston"])

definition("d_pres_barometer", "pressure", 4, "5f",
           stem="Describe how the height of a liquid column may be used to measure atmospheric pressure (a simple mercury barometer).", syllabi=PURE,
           points=[P("a tube full of mercury inverted into a dish of mercury; the space above the column is a vacuum", ["vacuum", "inverted", "upside down", "tube filled with mercury", "tube full of mercury", "dish of mercury", "trough of mercury"]),
                   P("atmospheric pressure acting on the surface in the dish supports the column: p_atm = hρg, about 760 mm Hg", ["supports the column", "holds up the column", "atmospheric pressure acting on the mercury", "atmospheric pressure pushing on", "balances the pressure of the column", "equal to the pressure due to the column", "760 mm", "76 cm", "hρg", "h rho g", "height × density × g"]),
                   P("the vertical height of the column measures the pressure (independent of tube width or tilt)", ["vertical height", "height of the column", "height of the mercury", "measure the height"])],
           min_points=2,
           model_answer="A tube filled with mercury is inverted into a dish of mercury, leaving a vacuum above the column. Atmospheric pressure on the mercury surface in the dish supports the column, so atmospheric pressure equals the pressure due to the column, hρg. The vertical height of the column (about 760 mm Hg) measures the atmospheric pressure.",
           hints=["Picture the mercury barometer: a tube, a dish and a vacuum.", "What holds the column up?", "Which measurement of the column gives the pressure?"],
           keywords="inverted tube, vacuum, atmosphere supports column, height = p/ρg, 760 mm Hg",
           sample_pass=["Invert a tube of mercury into a dish; the vacuum above lets the atmosphere support the column, whose vertical height (760 mm) gives atmospheric pressure", "atmospheric pressure on the dish holds up the mercury column so p = hρg from the height of the column"],
           sample_fail=["a tube of water measures the pressure", "the mercury pushes the air down"])

definition("d_pres_manometer", "pressure", 4, "5g",
           stem="Describe how a **manometer** is used to measure the pressure of a gas supply.", syllabi=PURE,
           points=[P("a U-tube containing liquid, one side open to the atmosphere, the other connected to the gas", ["u-tube", "u tube", "one side open to the atmosphere", "one arm open", "other side connected to the gas", "connected to the gas supply"]),
                   P("the difference in liquid levels gives the pressure difference, hρg, between the gas and the atmosphere", ["difference in levels", "difference in height", "height difference", "difference in liquid levels", "hρg", "h rho g", "height × density × g", "pressure difference"]),
                   P("gas pressure = atmospheric pressure + hρg (if its level is pushed down)", ["atmospheric pressure + ", "plus atmospheric", "add atmospheric pressure", "above atmospheric", "added to atmospheric", "more than atmospheric"])],
           min_points=2,
           model_answer="A manometer is a U-tube containing a liquid, with one arm open to the atmosphere and the other connected to the gas. The gas pushes the liquid down on its side; the difference in the liquid levels, h, gives the pressure difference hρg between the gas and the atmosphere, so the gas pressure is atmospheric pressure + hρg.",
           hints=["It is a U-tube of liquid.", "What does the difference in levels tell you?", "Is the gas pressure the level difference alone, or atmospheric pressure plus that?"],
           keywords="U-tube, one side open; level difference h; p_gas = p_atm + hρg",
           sample_pass=["U-tube with liquid, one side open to the air and the other to the gas; the difference in levels gives hρg, the excess over atmospheric pressure", "The height difference between the two arms gives the pressure difference, so gas pressure is atmospheric plus hρg"],
           sample_fail=["a tube that measures gas", "the liquid level shows the temperature"])

# ================================================================= 6  Energy
definition("d_en_stores", "energy", 2, "6a",
           stem="Name **four** energy stores.",
           points=[P("kinetic", ["kinetic"]), P("gravitational potential", ["gravitational potential", "gravitational"]), P("chemical (potential)", ["chemical"]),
                   P("elastic (potential)", ["elastic", "strain"]), P("nuclear", ["nuclear"]), P("internal (thermal)", ["internal", "thermal"])],
           min_points=4,
           pitfalls=[PF(["heat energy", "light energy", "sound energy", "electrical energy"], "In the current syllabus heat, light, sound and electricity are energy TRANSFERS (pathways), not stores. Stores: kinetic, gravitational potential, chemical, elastic, nuclear, internal.")],
           model_answer="Energy stores: kinetic, gravitational potential, chemical potential, elastic potential, nuclear and internal.",
           hints=["Stores are where energy is held, e.g. in a moving object or a stretched spring.", "Think: motion, height, fuel/food, springs, atomic nuclei, hot objects.", "Name four of the six."],
           keywords="kinetic, gravitational potential, chemical, elastic, nuclear, internal",
           sample_pass=["kinetic, gravitational potential, chemical and elastic", "nuclear, internal, kinetic, gravitational potential energy"], sample_fail=["heat, light, sound and electrical", "kinetic and potential"])

definition("d_en_pathways", "energy", 3, "6a",
           stem="State the **four ways** in which energy can be transferred from one store to another.",
           points=[P("mechanically (by a force acting over a distance / work done)", ["mechanical", "force acting over a distance", "force moving through a distance", "work done", "by a force"]),
                   P("electrically (by an electric current)", ["electric", "current"]),
                   P("by heating (due to a temperature difference)", ["heating", "temperature difference", "thermal"]),
                   P("by waves (electromagnetic or mechanical, e.g. light, sound)", ["waves", "radiation", "light", "sound"])],
           min_points=3,
           model_answer="Mechanically (by a force acting over a distance), electrically (by an electric current), by heating (due to a temperature difference) and by the propagation of waves (electromagnetic and mechanical).",
           hints=["These are the 'pathways', not the stores.", "Think: pushing, wires, hot to cold, light and sound.", "Name at least three."],
           keywords="mechanically, electrically, by heating, by waves",
           sample_pass=["mechanically, electrically, by heating and by waves", "by a force over a distance, by an electric current, by heating, by light and sound waves"], sample_fail=["kinetic and potential", "conduction"])

definition("d_en_ke", "energy", 1, "6b",
           stem="State what is meant by the **kinetic energy** of a body.",
           points=[P("energy a body possesses due to its motion", ["due to its motion", "because of its motion", "because it is moving", "due to motion", "energy of motion", "energy of a moving", "by virtue of its motion", "as a result of its motion"])],
           model_answer="Kinetic energy is the energy a body possesses due to its motion (Ek = ½mv²).",
           hints=["Kinetic comes from a Greek word for motion.", "When does a body have it?", "Say 'energy due to its ...'."],
           keywords="energy due to motion",
           sample_pass=["the energy a body has because of its motion", "energy due to motion"], sample_fail=["half m v squared", "the energy a body has because of its height"])

definition("d_en_gpe", "energy", 1, "6b",
           stem="State what is meant by the **gravitational potential energy** of a body.",
           points=[P("energy a body possesses due to its position (height) in a gravitational field", ["due to its position", "because of its position", "due to its height", "because of its height", "due to height", "position in a gravitational field", "height above the ground", "height in a gravitational field", "by virtue of its height", "by virtue of its position", "as a result of its height"])],
           pitfalls=[PF(["energy in a gravitational field"], "Not just 'energy in a gravitational field': you must mention the body's HEIGHT or POSITION (examiner report 2019).")],
           model_answer="Gravitational potential energy is the energy a body possesses due to its position (height) in a gravitational field (Ep = mgh).",
           hints=["Potential means stored by position.", "Which position? Think of what h stands for in mgh.", "Say 'energy due to its height / position in a gravitational field'."],
           keywords="energy due to height / position in a gravitational field",
           sample_pass=["the energy a body has because of its height above the ground", "energy due to its position in a gravitational field"], sample_fail=["energy in a gravitational field", "m g h"])

definition("d_en_conservation", "energy", 3, "6c",
           stem="State the **principle of conservation of energy**.",
           points=[P("energy cannot be created or destroyed", ["cannot be created or destroyed", "can neither be created nor destroyed", "not created or destroyed", "cannot be created nor destroyed", "neither created nor destroyed", "is never created or destroyed"]),
                   P("it can only be converted from one form / store to another, so the total energy (of a closed system) stays constant", ["converted from one form to another", "transferred from one store to another", "changed from one form to another", "transformed from one form", "converted from one store", "total energy remains constant", "total energy is constant", "total amount of energy stays the same", "total energy is conserved", "transferred from one form"])],
           pitfalls=[PF(["energy is lost", "energy is used up", "energy disappears"], "Energy is never 'lost' or 'used up'; it is transferred to other stores (often as thermal energy to the surroundings).")],
           model_answer="Energy cannot be created or destroyed; it can only be converted from one form (store) to another, so the total energy of a closed system remains constant.",
           hints=["Two halves: what cannot happen to energy, and what can.", "Can energy appear from nothing or vanish?", "What happens to the total amount when energy changes form?"],
           keywords="not created or destroyed; only converted; total constant",
           sample_pass=["Energy cannot be created or destroyed, only converted from one form to another", "energy is neither created nor destroyed; the total energy stays constant"],
           sample_fail=["energy is always conserved", "energy is lost as heat"])

definition("d_en_work", "energy", 1, "6d",
           stem="Define **work done** by a force.",
           points=[P("product of the force and the distance moved", ["force and the distance moved", "force multiplied by the distance", "force times the distance", "force × distance", "force x distance", "force * distance", "product of force and distance", "force and distance moved"]),
                   P("distance moved in the direction of the force", ["in the direction of the force", "along the direction of the force", "parallel to the force", "distance moved in the direction"])],
           pitfalls=[PF(["force and time", "force times time", "force × time"], "Work involves force and DISTANCE, not time."),
                     PF(["energy needed to", "amount of energy"], "Define it as force × distance moved in the direction of the force, not as an amount of energy.")],
           model_answer="Work done by a force is the product of the force and the distance moved by its point of application in the direction of the force (W = Fs).",
           hints=["It is a product of two quantities.", "Force and a distance: which direction must the distance be measured in?", "Examiners reject 'force × distance' without 'in the direction of the force' (report 2020)."],
           keywords="force × distance moved in the direction of the force",
           sample_pass=["the product of the force and the distance moved in the direction of the force", "force × distance moved in the direction of the force"], sample_fail=["force times distance", "force times time"])

definition("d_en_power", "energy", 1, "6e",
           stem="Define **power**.",
           points=[P("rate of work done / rate of energy transfer (work done or energy transferred per unit time)", ["rate of work done", "rate of doing work", "rate at which work is done", "rate of energy transfer", "rate of energy conversion", "rate at which energy is transferred", "rate at which energy is converted", "work done per unit time", "energy transferred per unit time", "energy converted per unit time", "work done per second", "energy per unit time", "work done divided by time", "energy transferred divided by time", "work done / time", "energy / time"])],
           pitfalls=[PF(["force per unit time", "force × velocity"], "Power is energy (or work) per unit time. Define it in terms of work done or energy transferred."),
                     PF(["amount of work done", "amount of energy"], "Not an amount: power is a RATE, i.e. per unit time.")],
           model_answer="Power is the rate of work done, or the rate of energy transfer (P = W/t = E/t).",
           hints=["Power is about how fast energy is transferred.", "'Rate of' means 'per unit time'.", "Say 'rate of work done' or 'energy transferred per unit time'."],
           keywords="rate of work done / energy transfer",
           sample_pass=["the rate of work done", "energy transferred per unit time"], sample_fail=["the amount of work done", "how strong something is"])

definition("d_en_efficiency", "energy", 2, "6f",
           stem="Define the **efficiency** of an energy transfer.", syllabi=PURE,
           points=[P("useful energy (or power) output", ["useful energy output", "useful output", "useful power output", "useful work output", "useful energy"]),
                   P("divided by the total energy (or power) input, usually × 100%", ["divided by the total energy input", "total energy input", "total input", "over the total input", "/ total energy input", "divided by the total input", "total power input", "ratio of useful", "fraction of", "percentage of the"])],
           pitfalls=[PF(["total energy output", "total output"], "Not 'total output' (that would always be 100%): efficiency uses the USEFUL output (examiner report 2020)."),
                     PF(["input divided by", "input over output", "input / output"], "Upside down: efficiency = useful output ÷ total input.")],
           model_answer="Efficiency = (useful energy output ÷ total energy input) × 100%. It can equally be written with power in place of energy.",
           hints=["It is a ratio of two energies (or powers).", "Which output? Which input? One word before each matters.", "Useful ... output over total ... input, as a percentage."],
           keywords="useful energy output ÷ total energy input × 100%",
           sample_pass=["useful energy output divided by total energy input times 100%", "the ratio of useful power output to total power input"], sample_fail=["output divided by input", "total energy output over total energy input"])

definition("d_en_renewable", "energy", 3, "6g",
           stem="State what is meant by a **renewable** energy resource and a **non-renewable** one, with one example of each.", syllabi=PURE,
           points=[P("renewable: replenished naturally (in a short time) / will not run out", ["replenished", "replaced naturally", "will not run out", "does not run out", "cannot be used up", "never run out", "never used up", "not used up", "renewed naturally", "naturally replaced", "never runs out", "will never run out", "infinite", "unlimited"]),
                   P("non-renewable: finite, used faster than it is formed, will run out", ["finite", "will run out", "runs out", "used up", "cannot be replaced", "limited supply", "takes millions of years"]),
                   P("examples: renewable e.g. solar, wind, hydro, tidal, geothermal, biofuel; non-renewable e.g. coal, oil, natural gas, nuclear", ["solar", "wind", "hydro", "tidal", "tides", "geothermal", "biofuel", "coal", "oil", "natural gas", "fossil fuel", "nuclear"])],
           model_answer="A renewable resource is one that is replenished naturally and will not run out, e.g. solar, wind, hydro, tidal, geothermal or biofuel. A non-renewable resource is finite and will eventually run out because it is used far faster than it forms, e.g. fossil fuels (coal, oil, natural gas) and nuclear fuel.",
           hints=["Think about whether the supply runs out.", "Which ones are replaced by nature as fast as we use them?", "Give one example of each."],
           keywords="replenished naturally vs finite; solar/wind vs fossil fuels",
           sample_pass=["Renewable resources are replenished naturally and will not run out, e.g. solar; non-renewable ones are finite and will run out, e.g. coal", "wind is renewable because it is never used up; oil is non-renewable because it is finite"],
           sample_fail=["renewable energy is cleaner", "renewable means it can be recycled like plastic"])

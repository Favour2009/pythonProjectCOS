# program to calculate speed
def calculate_speed(distance, time):
    if time == 0:
       return "Time cannot be zero!"
    return distance / time

# user input
distance =float(input("Enter the distance (in meters): "))
time = float(input("Enter the (in seconds):"))

#output
print(f"The speed is {calculate_speed(distance, time)} m/s.")


# program to calculate voltage using ohm's Law
def calculate_voltage(current, resistance):
    return current * resistance

#user input
current = float(input("Enter the current (in amperes): "))
resistance = float(input("Enter the resistance(in ohms): "))

#output
print(f"The voltage is{calculate_voltage(current, resistance)} V (volt).")


# program to calculate kinetic energy
def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

# user input
mass = float(input("Enter the mass (in kg): "))
velocity = float(input("Enter the velocity (in m/s): "))

#output
print(f"The kinetic energy is{calculate_kinetic_energy(mass, velocity)} J (Joule).")


# program to calculate force
def calculate_force(mass, acceleration):
    return mass * acceleration

# user input
mass = float(input("Enter the mass in kg): "))
acceleration = float(input("Enter the acceleration (in m/s^2): "))

#output
print(f"The force is {calculate_force(mass, acceleration)} N (Newton).")


#Program to calculate gravitational potential energy
def calculate_potential_energy(mass, gravity, height):
    return mass * gravity * height

# user input
mass = float(input("Enter the mass (in kg):"))
height = float("Enter the height (in meters): ")
gravity = 9.81 # standard gravitational acceleration (m/s^2)

# output
print(f"The gravitational potential energy is{calculate_potential_energy(mass, gravity, height)} J (Joule).")

import rocket_data as rd
import matplotlib.pyplot as plt

satv = rd.SaturnV()

print(f'{satv.dry_mass=}')
print(f'{satv.mass=}')
print(f'{satv.vel_exhaust=}')
print(f'{satv.fuel_burn_rate=}')
print(f'{satv.acceleration=}')

max_propellant = satv.mass - satv.dry_mass
accs = []
propellant = []
for t in range(1200):
    accs.append(satv.acceleration)
    satv.mass = satv.mass - satv.fuel_burn_rate
    satv.mass = max(satv.dry_mass, satv.mass)
    current_propellant = (satv.mass - satv.dry_mass) / max_propellant
    propellant.append(current_propellant)
    if satv.dry_mass >= satv.mass:
        satv.vel_exhaust = 0

velocities = []
vel = 0
for acc in accs:
    velocities.append(vel)
    vel += acc

altitudes = []
altitude = 0
for v in velocities:
    altitudes.append(altitude)
    altitude += v

plt.subplot(2, 2, 1)
plt.plot(accs)
plt.subplot(2, 2, 2)
plt.plot(propellant)
plt.subplot(2, 2, 3)
plt.plot(velocities)
plt.subplot(2, 2, 4)
plt.plot(altitudes)
plt.show()
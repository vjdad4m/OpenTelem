import matplotlib.pyplot as plt

g = 9.81 # m/s^2

def calc_acceleration(m, Ve, Dm, Dt = 1):
    # a = (Ve/m) * (Dm/Dt) - g
    return (Ve/m) * (Dm/Dt) - g

def main():
    # Saturn V's data
    dry_mass = 1.31 * 10 ** 5
    mass = 2.3 * 10**6                  # Kg
    fuel_burn_rate = 1.4 * 10 ** 4      # Kg / s
    exhaust_velocity = 2.4 * 10 ** 3    # m/s
    
    delta_s = 1200   # First n seconds of flight
    
    acc_per_s = []
    for i in range(delta_s):    
        acc = calc_acceleration(mass, exhaust_velocity, fuel_burn_rate)
        mass = max(dry_mass, mass - fuel_burn_rate) # No negative mass
        if mass == dry_mass:
            exhaust_velocity = 0
        acc_per_s.append(acc)

    v_per_s = []
    v = 0
    for t in acc_per_s:
        v += t
        v_per_s.append(v)

    alt_per_s = []
    alt = 0
    for v in v_per_s:
        alt += v
        alt_per_s.append(alt)

    plt.subplot(1, 3, 1)
    plt.plot(acc_per_s)
    plt.ylabel('Acceleration (m/s^2)')
    plt.xlabel('Time (s)')
    
    plt.subplot(1, 3, 2)
    plt.plot(v_per_s)
    plt.ylabel('Velocity (m/s)')
    plt.xlabel('Time (s)')

    plt.subplot(1, 3, 3)
    plt.plot(alt_per_s)
    plt.ylabel('Altitude (m)')
    plt.xlabel('Time (s)')

    plt.show()

if __name__ == '__main__':
    main()
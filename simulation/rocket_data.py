g = 9.81

class Rocket:
    def __init__(self):
        self.height = 0         # m
        self.dry_mass = 0       # kg
        self.mass = 0           # kg
        self.fuel_burn_rate = 0 # kg / s
        self.vel_exhaust = 0    # m / s
    
    @property
    def acceleration(self):
        acc = (self.vel_exhaust / self.mass) * self.fuel_burn_rate - g
        return acc

class SaturnV(Rocket):
    def __init__(self):
        self.height = 111
        self.dry_mass = 183_600
        self.mass = 2_970_000
        self.fuel_burn_rate = 15_000
        self.vel_exhaust = 2400
# http://pdg.lbl.gov/2007/mcdata/mass_width_2006.csv
# https://en.wikipedia.org/wiki/List_of_particles
# http://www.wavcott.org.uk/pcalc/
# https://phys.libretexts.org/TextBooks_and_TextMaps/University_Physics/Book%3A_University_Physics_(OpenStax)/Map%3A_University_Physics_III_-_Optics_and_Modern_Physics_(OpenStax)/11%3A_Particle_Physics_and_Cosmology/11.2%3A_Particle_Conservation_Laws

# EVENTUALLY, import particle data in
# electron = {"mass": 0.511,"charge": -1, "l_e": 1, "l_m": 0, "l_t": 0, "b": 0, "s": 0}
# electron_neutrino = {"mass": 2.2e-6, "charge": 0, "l_e": 1, "l_m": 0, "l_t": 0, "b": 0, "s": 0}
# muon = {"mass": 105.658, "charge": -1, "l_e": 0, "l_m": 1, "l_t": 0, "b": 0, "s": 0}
# muon_neutrino = {"mass": 105.658, "charge": 0, "l_e": 0, "l_m": 1, "l_t": 0, "b": 0, "s": 0}
# tau = {"mass": 1776.82, "charge": -1, "l_e": 0, "l_m": 0, "l_t": 1, "b": 0, "s": 0}
# tau_neutrino = {"mass"15.5: , "charge": 0, "l_e": 0, "l_m": 0, "l_t": 1, "b": , "s": }
# muon = {"mass": , "charge": , "l_e": , "l_m": , "l_t": , "b": , "s": }

class Particle:
    def __init__(self, name, mass, charge, spin, l_e, l_m, l_t, b, s, pos):
        self.name = name
        self.mass = mass
        self.charge = charge
        self.spin = spin
        self.l_e = l_e
        self.l_m = l_m
        self.l_t = l_t
        self.b = b
        self.s = s
        # pos is either 0 for initial (left side), or 1 for final (right side)
        self.pos = pos


class SystemOfParticles:
    def __init__(self, *args):

        self.left_side = []
        self.right_side = []

        for arg in args:
            if arg.pos == 0:
                self.left_side.append(arg)
            elif arg.pos == 1:
                self.right_side.append(arg)

    def get_total_mass(self, particles):
        mass = 0
        for particle in particles:
            mass += particle.mass
        return mass

    def charge_conservation(self):
        left_charge_count = 0
        right_charge_count = 0
        charge_conserved = False
        for particle in self.left_side:
            left_charge_count += particle.charge
        for particle in self.right_side:
            right_charge_count += particle.charge
        if left_charge_count == right_charge_count:
            charge_conserved = True
        return charge_conserved


    def baryon_number_conservation(self):
        left_b_count = 0
        right_b_count = 0
        baryon_conserved = False
        for particle in self.left_side:
            left_b_count += particle.b
        for particle in self.right_side:
            right_b_count += particle.b
        if left_b_count == right_b_count:
            baryon_conserved = True
        return baryon_conserved

    def system_conservation(self):
        system_conserved = False
        if self.charge_conservation and self.baryon_number_conservation:
            system_conserved = True
        return system_conserved


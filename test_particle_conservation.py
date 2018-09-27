import unittest
import particle_conservation as pc

# Test creating a Particle
class ParticleCreationTests(unittest.TestCase):

    def test_particle_is_saved(self):
        valid_particle = pc.Particle('testparticle', 0.511, -1, 1/2, 0, 1, 0, 1, 0, 0)
        self.assertEqual(valid_particle.name, 'testparticle')
        self.assertEqual(valid_particle.mass, 0.511)
        self.assertEqual(valid_particle.charge, -1)
        self.assertEqual(valid_particle.spin, 1/2)
        self.assertEqual(valid_particle.l_e, 0)
        self.assertEqual(valid_particle.l_m, 1)
        self.assertEqual(valid_particle.l_t, 0)
        self.assertEqual(valid_particle.b, 1)
        self.assertEqual(valid_particle.s, 0)
        self.assertEqual(valid_particle.pos, 0)


# Test the charge_conservation method
class ChargeConservationTests(unittest.TestCase):

    # Before the tests, set up a test 'system' of particles
    @classmethod
    def setUpClass(cls):
        p1_left = pc.Particle('leftparticle1', 0, -1, 0, 0, 0, 0, 0, 0, 0)
        p2_left = pc.Particle('leftparticle2', 0, 1, 0, 0, 0, 0, 0, 0, 0)
        p3_left = pc.Particle('leftparticle3', 0, 0, 0, 0, 0, 0, 0, 0, 0)
        p1_right = pc.Particle('rightparticle1', 0, -1, 0, 0, 0, 0, 0, 0, 1)
        p2_right = pc.Particle('rightparticle2', 0, 1, 0, 0, 0, 0, 0, 0, 1)
        p3_right = pc.Particle('rightparticle3', 0, 0, 0, 0, 0, 0, 0, 0, 1)

        cls.conserved_system1 = pc.SystemOfParticles(p1_left, p2_left, p3_left, p1_right, p2_right)
        cls.non_conserved_system1 = pc.SystemOfParticles(p1_left, p1_right, p2_right)

    def test_conserved_charge_is_true(self):
        """Verify testing for conserved charge returns true when it should"""
        self.assertTrue(self.conserved_system1.charge_conservation())

    def test_not_conserved_charge_is_false(self):
        """Verify testing for non-conserved charge returns false when it should"""
        self.assertFalse(self.non_conserved_system1.charge_conservation())

from revsim import *
import unittest

class TruthTables(unittest.TestCase):
    TT_toffoli = { (0,0,0): (0,0,0),
                   (0,0,1): (0,0,1),
                   (0,1,0): (0,1,0),
                   (0,1,1): (0,1,1),
                   (1,0,0): (1,0,0),
                   (1,0,1): (1,0,1),
                   (1,1,0): (1,1,1),
                   (1,1,1): (1,1,0) }

    TT_fredkin = { (0,0,0): (0,0,0),
                   (0,0,1): (0,0,1),
                   (0,1,0): (0,1,0),
                   (0,1,1): (0,1,1),
                   (1,0,0): (1,0,0),
                   (1,0,1): (1,1,0),
                   (1,1,0): (1,0,1),
                   (1,1,1): (1,1,1) }

    TT_swap = { (0,0): (0,0),
                (0,1): (1,0),
                (1,0): (0,1),
                (1,1): (1,1) }

    TT_inverter = { 0: 1,
                    1: 0 }

    def test_toffoli_values(self):
        for line in self.TT_toffoli:
            expected = self.TT_toffoli[line]
            actual = apply(line, toffoli, [0,1], 2)
            self.assertEqual(expected, actual)

    def test_fredkin_values(self):
        for line in self.TT_fredkin:
            expected = list(self.TT_fredkin[line])
            actual = apply(list(line), fredkin, [0], [1,2])
            self.assertEqual(expected, actual)

    def test_swap_values(self):
        for line in self.TT_swap:
            expected = list(self.TT_swap[line])
            actual = apply(list(line), swap, 0, 1)
            self.assertEqual(expected, actual)

    def test_inverter_values(self):
        for line in self.TT_inverter:
            expected = [self.TT_inverter[line]]
            actual = apply([line], inverter, [0], 0)
            self.assertEqual(expected, actual)


class TestAdder(unittest.TestCase):
    lines = [0, 0, 0, 0]
    adder = Cascade(lines)
    adder.append(toffoli, [0, 1], 2)
    adder.append(toffoli, [0], 3)
    adder.append(toffoli, [1], 3)

    TT_adder = { (0,0,0,0): (0,0),
                 (0,1,0,0): (0,1),
                 (1,0,0,0): (0,1),
                 (1,1,0,0): (1,0) }

    def test_adder_result(self):
        for line in self.TT_adder:
            expected = list(self.TT_adder[line])
            self.adder.replace_lines(list(line))
            actual = self.adder.run()[2:4] # only the last two vals matter
            self.assertEqual(expected, actual)

    def test_adder_length(self):
        self.assertEqual(len(self.adder), 3)

    def test_adder_subscript(self):
        expected = [(toffoli, [0,1], 2), (toffoli, [0], 3), (toffoli, [1], 3)]
        for i in range(0, 3):
            self.assertEqual(expected[i], self.adder[i])


class TestCascadeOperations(unittest.TestCase):
    lines = [0, 0, 0, 0]
    adder = Cascade(lines)
    adder.append(toffoli, [0, 1], 2)
    adder.append(toffoli, [0], 3)
    adder.append(toffoli, [1], 3)

    def test_cascade_copy(self):
        copied = self.adder.copy()
        for i in range(0, 3):
            self.assertEqual(copied[i], self.adder[i])
        self.assertEqual(len(copied), len(self.adder))

    def test_cascade_reference(self):
        ref = self.adder
        for i in range(0, 3):
            self.assertEqual(ref[i], self.adder[i])
        self.assertEqual(len(ref), len(self.adder))
        ref.append(toffoli, [0], 2)
        for i in range(0, 4):
            self.assertEqual(ref[i], self.adder[i])
        self.assertEqual(len(ref), len(self.adder))
        ref.remove(3)

    def test_cascade_insert_valid(self):
        self.adder.insert(toffoli, [0], 2, 2)
        self.assertEqual(len(self.adder), 4)
        self.assertEqual(self.adder[2], (toffoli, [0], 2))
        
    def test_cascade_insert_invalid(self):
        self.assertRaises(ValueError, self.adder.insert, toffoli, [0], 2, -1)
        self.assertRaises(ValueError, self.adder.insert, toffoli, [0], 2, 100)

    def test_cascade_remove_valid(self):
        self.adder.remove(2)
        self.assertEqual(len(self.adder), 3)

    def test_cascade_remove_invalid(self):
        self.assertRaises(IndexError, self.adder.remove, -1)
        self.assertRaises(IndexError, self.adder.remove, 100)

class TestGateSanity(unittest.TestCase):
    def test_toffoli_sanity(self):
        """ Target must not be contained in controls """
        self.assertRaises(ValueError, apply, [0,0,0], toffoli, [0,1], 1)
        """ Controls and targets must be in the line range """
        self.assertRaises(ValueError, apply, [0], toffoli, [1], 0)
        self.assertRaises(ValueError, apply, [0], toffoli, [0], 1)
        """ Must not be able to apply on empty line list """
        self.assertRaises(ValueError, apply, [], toffoli, [0], 1)
        """ Toffoli gates must only have a single target """
        self.assertRaises(ValueError, apply, [0,0,0], toffoli, [0], [1,2])
        """ Controls must be specified in a list """
        self.assertRaises(ValueError, apply, [0,0,0], toffoli, 1, 2)
        """ Target must be specified by an integer """
        self.assertRaises(ValueError, apply, [0,0,0], toffoli, [0,1], [2])

    def test_fredkin_sanity(self):
        """ Targets must not be contained in controls """
        self.assertRaises(ValueError, apply, [0,0,0], fredkin, [0,1], [1,2])
        
        pass

    def test_inverter_sanity(self):
        pass

    def test_swap_sanity(self):
        pass

class TestCascadeSanity(unittest.TestCase):
    c = Cascade([0,0,0])
    def test_remove_sanity(self):
        """ Cascades must not allow removal of gate indices that don't exist """
        self.assertRaises(IndexError, self.c.remove, 1)
        """ Disallow removal of negative indices """
        self.assertRaises(IndexError, self.c.remove, -1)

    def test_replace_lines_sanity(self):
        """ Must not allow replacement of lines with a set of lines that is smaller """
        self.assertRaises(ValueError, self.c.replace_lines, [0,0])
        """ Must not allow replacement of lines with a larger set of lines """
        self.assertRaises(ValueError, self.c.replace_lines, [0,0,0,0])

if __name__ == "__main__":
    unittest.main()

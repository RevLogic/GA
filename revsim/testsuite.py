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
            expected = list(self.TT_toffoli[line])
            actual = apply(list(line), toffoli, [0,1], 2)
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

if __name__ == "__main__":
    unittest.main()

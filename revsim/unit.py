from revsim import *
from sym9 import *
import unittest

class GateTests(unittest.TestCase):
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
        line_labels = ['a', 'b', 'c']
        for line in self.TT_toffoli:
            in_lines = dict(zip(line_labels, line))
            tof = Toffoli(['a', 'b'], 'c')
            actual = tof.eval(in_lines)
            expected = dict(zip(line_labels, self.TT_toffoli[line]))
            self.assertEqual(actual, expected)

    def test_fredkin_values(self):
        line_labels = ['a', 'b', 'c']
        for line in self.TT_fredkin:
            in_lines = dict(zip(line_labels, line))
            fred = Fredkin(['a'], ['b', 'c'])
            actual = fred.eval(in_lines)
            expected = dict(zip(line_labels, self.TT_fredkin[line]))
            self.assertEqual(actual, expected)

    def test_swap_values(self):
        line_labels = ['a', 'b']
        for line in self.TT_swap:
            in_lines = dict(zip(line_labels, line))
            sw = Swap([], ['a', 'b'])
            actual = sw.eval(in_lines)
            expected = dict(zip(line_labels, self.TT_swap[line]))
            self.assertEqual(actual, expected)

    def test_inverter_values(self):
        line_label = 'a'
        for line in self.TT_inverter:
            in_lines = dict([(line_label, line)])
            inv = Inverter('a')
            actual = inv.eval(in_lines)
            expected = dict([(line_label, self.TT_inverter[line])])
            self.assertEqual(actual, expected)


class CascadeOperationTests(unittest.TestCase):
    lines = {'a':0, 'b':0, 'c':0, 's':0}
    adder = Cascade(lines)
    adder.append(Toffoli(['a', 'b'], 'c'))
    adder.append(Toffoli(['a'], 's'))
    adder.append(Toffoli(['b'], 's'))

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
        ref.append(Toffoli(['a'], 'c'))
        for i in range(0, 4):
            self.assertEqual(ref[i], self.adder[i])
        self.assertEqual(len(ref), len(self.adder))
        ref.remove(3)

    def test_cascade_insert_valid(self):
        self.adder.insert(Toffoli(['a'], 'c'), 2)
        self.assertEqual(len(self.adder), 4)
        self.assertEqual(self.adder[2], Toffoli(['a'], 'c'))

    def test_cascade_insert_invalid(self):
        self.assertRaises(ValueError, self.adder.insert, Toffoli(['a'], 'c'), -1)
        self.assertRaises(ValueError, self.adder.insert, Toffoli(['a'], 'c'), 100)

    def test_cascade_remove_valid(self):
        self.adder.remove(2)
        self.assertEqual(len(self.adder), 3)

    def test_cascade_remove_invalid(self):
        self.assertRaises(IndexError, self.adder.remove, -1)
        self.assertRaises(IndexError, self.adder.remove, 100)


class CascadeSanity(unittest.TestCase):
    c = Cascade({'a':0, 'b':0, 'c':0})
    def test_remove_sanity(self):
        # Cascades must not allow removal of gate indices that don't exist
        self.assertRaises(IndexError, self.c.remove, 1)
        # Disallow removal of negative indices
        self.assertRaises(IndexError, self.c.remove, -1)

    def test_update_lines_sanity(self):
        # Must not allow replacement of lines with a set of lines that is smaller
        self.assertRaises(ValueError, self.c.update_lines, {'a':0, 'b':0})
        # Must not allow replacement of lines with a larger set of lines
        self.assertRaises(ValueError, self.c.update_lines, {'a':0, 'b':0, 'c':0, 'd':0})


class TestGateSanity(unittest.TestCase):
    def test_toffoli_sanity(self):
        tof1 = Toffoli(['a', 'b'], 'd')
        tof2 = Toffoli(['a', 'd'], 'b')
        # Target must not be contained in controls 
        self.assertRaises(ValueError, Toffoli, ['a', 'b'], 'a')
        # Controls and targets must be in the line range
        self.assertRaises(ValueError, tof1.eval, {'a':0, 'b':0, 'c':0})
        self.assertRaises(ValueError, tof2.eval, {'a':0, 'b':0, 'c':0})
        # Must not be able to apply on empty line list
        self.assertRaises(ValueError, tof1.eval, {})
        # Toffoli gates must only have a single target
        tof3 = Toffoli(['a', 'b'], ['c', 'd'])
        self.assertRaises(ValueError, tof3.eval, {'a':0, 'b':0, 'c':0, 'd':0})

    def test_fredkin_sanity(self):
        # Targets must not be contained in controls
        #self.assertRaises(ValueError, apply, [0,0,0], fredkin, [0,1], [1,2])
        pass

    def test_inverter_sanity(self):
        pass

    def test_swap_sanity(self):
        pass


class IOTests(unittest.TestCase):    
    current_cascade = None

    def test_writing_real(self):
        w = RealWriter(sym9)
        w.write("sym9_unittest.real")

    def test_reading_real(self):
        r = RealReader("sym9_unittest.real")
        self.current_cascade, non_garbage = r.read_cascade()
        self.assertEqual(self.current_cascade, sym9)

    def test_writing_pickle(self):
        pass
    
    def test_reading_pickle(self):
        pass


class SharedCubeTests(unittest.TestCase):
    c = Cascade({'x1':1, 'x2':1, 'x3':1, 'x4':1, 'f1':0, 'f2':0, 'f3':0, 'f4':0, 'f5':0},
            ['f1', 'f2', 'f3', 'f4', 'f5'])

    c.append(Toffoli(['x1', 'x2', 'x4'], 'f1'))
    c.append(Toffoli(['x1', 'x3'], 'f1'))
    c.append(Toffoli(['x2', 'x4'], 'f1'))
    c.append(Toffoli(['f1'], 'f3'))
    c.append(Toffoli(['x1', 'x2', 'x4'], 'f4'))
    c.append(Toffoli(['x1', 'x3'], 'f4'))
    c.append(Toffoli(['f4'], 'f5'))
    c.append(Toffoli(['x1', 'x2', 'x4'], 'f2'))

    s = SharedCube(c)
    cube_list = s.generate()

    def test_check_cube_list(self):
        actual = { ('x2', 'x4'): ['f1', 'f3'],
                   ('x1', 'x3'): ['f1', 'f4', 'f3', 'f5'],
                   ('x1', 'x2', 'x4'): ['f1', 'f4', 'f2', 'f3', 'f5'] }
        
        self.assertEqual(self.cube_list, actual)

class QuantumCostTest(unittest.TestCase):
    costs = []
    gates = []
    def test_toffoli_quantum(self):
        self.costs = [1, 1, 5, 13, 29, 61, 125, 253, 509, 1021]
        self.gates.append(Inverter('a')) # 1
        self.gates.append(Toffoli(['a'], 'b')) # 1
        self.gates.append(Toffoli(['a', 'b'], 'c')) # 5
        self.gates.append(Toffoli(['a', 'b', 'c'], 'd')) # 13
        self.gates.append(Toffoli(['a', 'b', 'c', 'd'], 'e')) # 29
        self.gates.append(Toffoli(['a', 'b', 'c', 'd', 'e'], 'f')) # 61
        self.gates.append(Toffoli(['a', 'b', 'c', 'd', 'e', 'f'], 'g')) # 125
        self.gates.append(Toffoli(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 'h')) # 253
        self.gates.append(Toffoli(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'], 'i')) # 509
        self.gates.append(Toffoli(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'], 'j')) # 1021

        for i in range(0, len(self.gates)):
            self.assertEqual(self.gates[i].cost(), self.costs[i])
            
if __name__ == "__main__":
    unittest.main()

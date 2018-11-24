function leftPad(arr: any[], n: number, v: any) {
  let vals = [];

  for (let i = 0; i < n; i++) {
    vals.push(v)
  }

  return vals.concat(arr);
}

function generatePermutations(n: number) {
  let perms: boolean[][] = [];

  for (let i = 0; i < Math.pow(2, n); i++) {
    let perm = (i >>> 0).toString(2).split('');

    const len = perm.length;
    if (len !== n) {
      perm = leftPad(perm, n - len, '0');
    }

    perms.push(perm.map(val => (val === '0' ? false : true)));
  }

  return perms;
}

function tof(control_indices: number[], output_index: number) {
  return function (inputs: boolean[]) {
    const control_values = control_indices.map(i => inputs[i]);

    if (!control_values.length || control_values.every(v => v)) {
      let outputs = [...inputs];
      outputs.splice(output_index, 1, !inputs[output_index]);
      return outputs;
    } else {
      return inputs;
    }
  }
}

function runCircuit(circuit: Function[], initial_state: boolean[]) {
  return circuit.reduce((state: boolean[], gate: Function) => gate(state), initial_state);
}

function mask(perm: boolean[], inputs: string[]) {
  let perm_index = 0;
  return inputs.map((input) => {
    switch (input) {
      case '0':
        return false;
      case '1':
        return true;
      default:
        return perm[perm_index++]; // get the "current index" in perms list
    }
  });
}

`
# Function: ryy6
# Used Library: MCT (Gates: 44, Quantum costs: 4292)
# This file have been taken from RevLib (www.revlib.org).
.version  1.0
# Created by tfc2real J. Rice Jan 2009
# Parameters for Exorcism: -n 1 -r 1 -a 0 -b 1 -c 1
# Templates applied in both directions
.numvars 17
.variables  f0 x15 x14 x13 x12 x11 x10 x9 x8 x7 x6 x5 x4 x3 x2 x1 x0
.inputs  0 x15 x14 x13 x12 x11 x10 x9 x8 x7 x6 x5 x4 x3 x2 x1 x0
.outputs  f0 x15 x14 x13 x12 x11 x10 x9 x8 x7 x6 x5 x4 x3 x2 x1 x0
.constants 0----------------
.garbage 1111111111111111-
`

const variables = ['f0', 'x15', 'x14', 'x13', 'x12', 'x11', 'x10', 'x9', 'x8', 'x7', 'x6', 'x5', 'x4', 'x3', 'x2', 'x1', 'x0'];
const inputs = ['0', 'x15', 'x14', 'x13', 'x12', 'x11', 'x10', 'x9', 'x8', 'x7', 'x6', 'x5', 'x4', 'x3', 'x2', 'x1', 'x0'];
const garbage = ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'g', 'f', 'f'];
const constants = inputs.filter(i => i === '0' || i === '1');
const dimensions = inputs.length - constants.length;
const perms = generatePermutations(dimensions);
const masked_perms = perms.map(p => mask(p, inputs));

const gate_strings = [
  't1 x1',
  't14 x1 x2 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15 f0',
  't12 x1 x2 x5 x6 x9 x10 x11 x12 x13 x14 x15 f0',
  't10 x1 x2 x9 x10 x11 x12 x13 x14 x15 f0',
  't16 x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 x12 x13 x14 x15 f0',
  't14 x1 x2 x3 x4 x5 x6 x9 x10 x11 x12 x13 x14 x15 f0',
  't12 x1 x2 x3 x4 x9 x10 x11 x12 x13 x14 x15 f0',
  't14 x1 x2 x3 x4 x7 x8 x9 x10 x11 x12 x13 x14 x15 f0',
  't12 x1 x2 x5 x6 x7 x8 x9 x12 x13 x14 x15 f0',
  't14 x1 x2 x3 x4 x5 x6 x7 x8 x9 x12 x13 x14 x15 f0',
  't12 x1 x2 x3 x4 x7 x8 x9 x12 x13 x14 x15 f0',
  't10 x1 x2 x5 x6 x7 x8 x9 x10 x11 f0',
  't8 x1 x2 x5 x6 x9 x10 x11 f0',
  't6 x1 x2 x9 x10 x11 f0',
  't12 x1 x2 x3 x4 x5 x6 x7 x8 x9 x10 x11 f0',
  't10 x1 x2 x3 x4 x5 x6 x9 x10 x11 f0',
  't8 x1 x2 x3 x4 x9 x10 x11 f0',
  't10 x1 x2 x3 x4 x7 x8 x9 x10 x11 f0',
  't8 x1 x2 x5 x6 x7 x8 x9 f0',
  't10 x1 x2 x3 x4 x5 x6 x7 x8 x9 f0',
  't8 x1 x2 x3 x4 x7 x8 x9 f0',
  't12 x1 x2 x7 x8 x9 x10 x11 x12 x13 x14 x15 f0',
  't8 x1 x2 x7 x8 x9 x10 x11 f0',
  't10 x1 x2 x7 x8 x9 x12 x13 x14 x15 f0',
  't6 x1 x2 x7 x8 x9 f0',
  't6 x1 x12 x13 x14 x15 f0',
  't8 x1 x3 x4 x12 x13 x14 x15 f0',
  't8 x1 x5 x6 x12 x13 x14 x15 f0',
  't10 x1 x3 x4 x5 x6 x12 x13 x14 x15 f0',
  't2 x1 f0',
  't4 x1 x3 x4 f0',
  't4 x1 x5 x6 f0',
  't6 x1 x3 x4 x5 x6 f0',
  't1 x1',
  't1 x2',
  't1 x0',
  't8 x0 x1 x2 x12 x13 x14 x15 f0',
  't10 x0 x1 x2 x3 x4 x12 x13 x14 x15 f0',
  't10 x0 x1 x2 x5 x6 x12 x13 x14 x15 f0',
  't12 x0 x1 x2 x3 x4 x5 x6 x12 x13 x14 x15 f0',
  't4 x0 x1 x2 f0',
  't6 x0 x1 x2 x3 x4 f0',
  't6 x0 x1 x2 x5 x6 f0',
  't8 x0 x1 x2 x3 x4 x5 x6 f0'
];

function str2tof(gate_string: string, variables: string[]) {
  let lines = gate_string.split(' ');
  lines.splice(0, 1);
  const [output_line] = lines.splice(lines.length - 1, 1).map(l => variables.indexOf(l));
  const controls = lines.map(l => variables.indexOf(l));
  return tof(controls, output_line);
}

function discardGarbage(outputs: boolean[], garbage: string[]) {
  let cleaned = [];

  garbage.forEach((g: string, index: number) => {
    const is_garbage = g.toLowerCase() === 'g';
    if (!is_garbage) {
      cleaned.push(outputs[index]);
    }
  });
  
  return cleaned;
}

const circuit = gate_strings.map((str: string) => str2tof(str, variables));

masked_perms.forEach((perm: boolean[], index: number) => {
  const val = discardGarbage(runCircuit(circuit, perm), garbage);
  console.log(index, val);
})
1. What is a quantum computer?
  0. Briefly mention what is conventionally called a quantum
  computer is not a entirely quantum, but an interface between a classical
  computer  and quantum hardware. What sits in the quantum hardware, is a
  collection of two-level quantum systems called qubits (analogous to the bit),
  should provide a segue to the qubit vs bit distinction.

  1. Quantum software (Qiskit) and simple companion examples.
  Maybe show a python code snippet creating a circuit,
  adding gates, and performing measurements. (And maybe
  it's OPENQASM equivalence)

2. Whence is the computational power derived from?
  0. Formally, introduce the qubit and bit distinction, emphasize
  the differences between the two. Highlight superposition / interference
  for the qubit.

  1. Show representation of bit (sphere with a north and south pole
  representating 0 & 1) vs representation of qubit on a Bloch sphere (as a
  2^n dimenstional vector). Use this as segue way to hone in the point that to
  classically simulate n qubits , you need exponentially many classical bits (~2^n).
  Maybe also mention a bit of trivia regarding this. _i.e._ to classically represent
  a system of 500 qubits in superposition, you would need more bits than there are atoms in the observable universe.

  This subsection will draw inspiration from [The Case for Quantum](https://qiskit.org/textbook/ch-states/case-for-quantum.html)
  in the Qiskit textbook, _i.e._ Graph showing Big O notation, classical search
  versus quantum search, maybe a more nuanced and stark instance such as Shor's
  prime factorization.

3. Quantum computation
  0. Formally introducing quantum circuits; Representation of qubits as wires, time evolution goes
  from left to right, single qubit gate and multi-qubit gates (computation) in between,
  and qubit measurements at the end, extracting results from the circuits.

  1. Single qubit gates
  Have a typical circuit (3-qubit toffoli gate T,S and CNOT decomposition)
  to explain single qubits (highlighted them in the circuit and show corresponding matrix)

  2. Two-qubit gates
  Same idea as 5.1 explain two-qubit gates (highlighted them in the circuit and show
  corresponding matrix)

  3. Metrics used to measure quantum circuit complexity.
  Circuit depth and number of multi-qubit (i.e CNOT gate count) gauge are
  complicated quantum circuits. [Perhaps, I can mention this before the case for
  quantum section? Since the section assumes that the audience is aware of how
  circuit complexity is measurement]

  3. Universality
  Segue to universality; single qubit + two-qubit gates allow us to do any
  quantum logical operation (unitary operation). We can possibly draw parallels
  between these and their classical equivalents.

  (0?). Non-seperability (entanglement) [BIG IF]

  4. Simplest algorithm: Quantum search / Deutsch-Jozsa algorithm / Superdense coding  / Quantum teleportation (Draw from the textbook) _etc pp_
  We can pick an algorithm, to fill in some of the details, we glossed over,
  for instance, quantum teleportation / Superdense coding are great examples
  to highlight how the non-seperability of quantum states leads to strange
  and counterintuitive consequences. While Deutsch-Jozsa and Quantum search are more so to highlight the possible
  speed ups quantum algorithms may have over their classical counterparts. The
  format of this bit will resemble:
  - Problem statement
  - Classical solution
  - Quantum solution
  - What is the difference between the two? Use this to highlight earlier points

4.0?. Noisy intermediate scale quantum computation (Maybe already in part Uno)
  What's that? What kinds of limitation does this place on what we can do?

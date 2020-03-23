from qiskit import *

# Three Qubits and three scientific bits
new_circuit = QuantumCircuit(3, 3)
# Three quantum qubits and 3 classical bits
# q_0: |0>
# q_1: |0>
# q_2: |0>
# c_0: 0
# c_1: 0
# c_2: 0
# The code helps us to draw circuit
%matplotlib inline
circuit.draw(output = 'mpl')
# This part deals with setting up an example for unknown quantum state
new_circuit.x(0)
# Here we add the barrier in the first two stages of the circuit
new_circuit.barrier()
# Now, the code to draw the circuit at the current stage is included
new_circuit.draw(output="mpl")
#
#         ┌───┐ ░
# q_0: |0>┤ X ├─░─
        # └───┘ ░
# q_1: |0>──────░─
#               ░
# q_2: |0>──────░─
#               ░
# c_0: 0 ════════
# c_1: 0 ════════
# c_2: 0 ════════

# The next stage is ERP bell state that we will use in teleportation protocol. This is define
# between sender Q1 and reciever Q2
# We can define the ERP bell state by taking Hardmard gate and than takinf CNOT of it.
new_circuit.h(0)
new_circuit.cx(0, 1)

# Now code to draw the circuit at current stage is included.
new_circuit.draw(output='mpl')

# That's the first part of teleportation
# Put another barrier
new_circuit.barrier()
# Apply CNOT Gate
new_circuit.cx(0, 1)
# Apply Hadmard Gate
new_circuit.h(0)
# Draw the diagram
new_circuit.draw(output='mpl')

#         ┌───┐ ░ ┌───┐      ░  ░      ┌───┐ ░      ┌───┐┌─┐ ░                 »
# q_0: |0>┤ X ├─░─┤ H ├──■───░──░───■──┤ H ├─░───■──┤ H ├┤M├─░───────■───────■─»
#         └───┘ ░ └───┘┌─┴─┐ ░  ░ ┌─┴─┐└───┘ ░ ┌─┴─┐└┬─┬┘└╥┘ ░       │       │ »
# q_1: |0>──────░──────┤ X ├─░──░─┤ X ├──────░─┤ X ├─┤M├──╫──░───■───┼───■───┼─»
#               ░      └───┘ ░  ░ └───┘      ░ └───┘ └╥┘  ║  ░ ┌─┴─┐ │ ┌─┴─┐ │ »
# q_2: |0>──────░────────────░──░────────────░────────╫───╫──░─┤ X ├─■─┤ X ├─■─»
#               ░            ░  ░            ░        ║   ║  ░ └───┘   └───┘   »
#  c_0: 0 ════════════════════════════════════════════╬═══╩════════════════════»
#                                                     ║                        »
#  c_1: 0 ════════════════════════════════════════════╩════════════════════════»
#                                                                              »
#  c_2: 0 ═════════════════════════════════════════════════════════════════════»
#                                                                              »
# «                ┌─┐ ░  ░      ┌───┐
# «q_0: ──────■────┤M├─░──░───■──┤ H ├
# «           │ ┌─┐└╥┘ ░  ░ ┌─┴─┐└───┘
# «q_1: ──■───┼─┤M├─╫──░──░─┤ X ├─────
# «     ┌─┴─┐ │ └╥┘ ║  ░  ░ └───┘
# «q_2: ┤ X ├─■──╫──╫──░──░───────────
# «     └───┘    ║  ║  ░  ░
# «c_0: ═════════╬══╩═════════════════
# «              ║
# «c_1: ═════════╩════════════════════
# «
# «c_2: ══════════════════════════════
# «
# In next step we are going to measure each of the qubit
new_circuit.measure([0, 1], [0, 1])
new_circuit.barrier()
new_circuit.draw(output="mpl")
#         ┌───┐ ░ ┌───┐      ░  ░      ┌───┐ ░      ┌───┐┌─┐ ░                 »
# q_0: |0>┤ X ├─░─┤ H ├──■───░──░───■──┤ H ├─░───■──┤ H ├┤M├─░───────■───────■─»
#         └───┘ ░ └───┘┌─┴─┐ ░  ░ ┌─┴─┐└───┘ ░ ┌─┴─┐└┬─┬┘└╥┘ ░       │       │ »
# q_1: |0>──────░──────┤ X ├─░──░─┤ X ├──────░─┤ X ├─┤M├──╫──░───■───┼───■───┼─»
#               ░      └───┘ ░  ░ └───┘      ░ └───┘ └╥┘  ║  ░ ┌─┴─┐ │ ┌─┴─┐ │ »
# q_2: |0>──────░────────────░──░────────────░────────╫───╫──░─┤ X ├─■─┤ X ├─■─»
#               ░            ░  ░            ░        ║   ║  ░ └───┘   └───┘   »
#  c_0: 0 ════════════════════════════════════════════╬═══╩════════════════════»
#                                                     ║                        »
#  c_1: 0 ════════════════════════════════════════════╩════════════════════════»
#                                                                              »
#  c_2: 0 ═════════════════════════════════════════════════════════════════════»
#                                                                              »
# «                ┌─┐ ░
# «q_0: ──────■────┤M├─░─
# «           │ ┌─┐└╥┘ ░
# «q_1: ──■───┼─┤M├─╫──░─
# «     ┌─┴─┐ │ └╥┘ ║  ░
# «q_2: ┤ X ├─■──╫──╫──░─
# «     └───┘    ║  ║  ░
# «c_0: ═════════╬══╩════
# «              ║
# «c_1: ═════════╩═══════
# «
# «c_2: ═════════════════
# «
# Draw a CNOT from line 1 to line 2
new_circuit.cx(1, 2)
# Draw CZ from line 0 to line 2
new_circuit.cz(0, 2)
new_circuit.draw(output = 'mpl')
#         ┌───┐ ░ ┌───┐      ░  ░      ┌───┐ ░      ┌───┐┌─┐ ░                 »
# q_0: |0>┤ X ├─░─┤ H ├──■───░──░───■──┤ H ├─░───■──┤ H ├┤M├─░───────■───────■─»
#         └───┘ ░ └───┘┌─┴─┐ ░  ░ ┌─┴─┐└───┘ ░ ┌─┴─┐└┬─┬┘└╥┘ ░       │       │ »
# q_1: |0>──────░──────┤ X ├─░──░─┤ X ├──────░─┤ X ├─┤M├──╫──░───■───┼───■───┼─»
#               ░      └───┘ ░  ░ └───┘      ░ └───┘ └╥┘  ║  ░ ┌─┴─┐ │ ┌─┴─┐ │ »
# q_2: |0>──────░────────────░──░────────────░────────╫───╫──░─┤ X ├─■─┤ X ├─■─»
#               ░            ░  ░            ░        ║   ║  ░ └───┘   └───┘   »
#  c_0: 0 ════════════════════════════════════════════╬═══╩════════════════════»
#                                                     ║                        »
#  c_1: 0 ════════════════════════════════════════════╩════════════════════════»
#                                                                              »
#  c_2: 0 ═════════════════════════════════════════════════════════════════════»
#                                                                              »
# «
# «q_0: ──────■─
# «           │
# «q_1: ──■───┼─
# «     ┌─┴─┐ │
# «q_2: ┤ X ├─■─
# «     └───┘
# «c_0: ════════
# «
# «c_1: ════════
# «
# «c_2: ════════
# «

#measure will connect quantum 2 to classical 2
circuit.measure(2, 2)
simulator = Aer.get_backend('qasm_simulator')result = execute(circuit, backend=simulator, shots=1024).result()
counts=result.get_counts()
from qiskit.tools.visualization import plot_histogram

#         ┌───┐ ░
# q_0: |0>┤ X ├─░───────
#         └───┘ ░
# q_1: |0>──────░───────
#               ░ ┌─┐┌─┐
# q_2: |0>──────░─┤M├┤M├
#               ░ └╥┘└╥┘
# c_0: 0 ═════════╬══╬═
#                 ║  ║
# c_1: 0 ═════════╬══╬═
#                 ║  ║
# c_2: 0 ═════════╩══╩═


plot_histogram(counts)

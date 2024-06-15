from ase import Atoms
from ase.build import make_supercell
from ase.io import write
import numpy as np

# Define the unit cell for Cu2GeS3
# Replace these lattice parameters and atomic positions with correct ones for Cu2GeS3
lattice_constant = 5.53
c_length = 11.06
unit_cell = Atoms(
    symbols=['Cu', 'Cu', 'Ge', 'S', 'S', 'S'],
    positions=[(0, 0, 0),
               (0.5, 0.5, 0),
               (0.25, 0.25, 0.5),
               (0.75, 0.25, 0.5),
               (0.25, 0.75, 0.5),
               (0.75, 0.75, 0.5)],
    cell=[lattice_constant, lattice_constant, c_length],
    pbc=True
)

# Define the supercell matrix (2x2x2 supercell)
supercell_matrix = [[2, 0, 0],
                    [0, 2, 0],
                    [0, 0, 2]]

# Number of compositions to generate
num_compositions = 10

for i in range(num_compositions):
    # Randomly generate x (fraction of Se)
    x = np.random.uniform(0, 1)  # Generates a random number between 0 and 1

    # Create the supercell
    supercell = make_supercell(unit_cell, supercell_matrix)

    # Get the positions of S atoms and replace a fraction with Se
    positions = supercell.get_positions()
    species = supercell.get_chemical_symbols()

    # Determine which S atoms to replace with Se
    s_indices = [j for j, atom in enumerate(species) if atom == 'S']
    num_se = int(x * len(s_indices))  # Number of Se atoms to replace

    # Randomly replace S atoms with Se
    np.random.shuffle(s_indices)
    for k in range(num_se):
        species[s_indices[k]] = 'Se'

    # Update the chemical symbols
    supercell.set_chemical_symbols(species)

    # Write the modified structure to POSCAR format
    filename = f'POSCAR_{i+1}_x{round(x, 2)}'
    write(filename, supercell)

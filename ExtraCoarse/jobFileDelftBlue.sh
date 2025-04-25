#!/bin/sh
#SBATCH --job-name="KVLCC2_extra_coarse"
#SBATCH --time=4:00:00
#SBATCH --partition=compute
#SBATCH --ntasks=50
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=2G
#SBATCH --account=education-me-courses-mt44025

module load 2024r1
module load openmpi
module load openfoam
module load python
module load py-numpy
module load py-scipy
module load py-matplotlib


./AllrunSimulation.sh

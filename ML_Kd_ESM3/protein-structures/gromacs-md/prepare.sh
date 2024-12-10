
export path=$1
export file_name=$2
# First step: pdb2gmx
gmx_mpi pdb2gmx -f $path/$file_name.pdb -o $path/$file_name.gro -water tip3p -ignh -ff charmm36-jul2022 -p $path/topol.top -i $path/posre.itp
gmx_mpi pdb2gmx -f $path/$file_name.pdb -o $path/${file_name}_prepared.pdb -water tip3p -ignh -ff charmm36-jul2022 -p $path/topol.top -i $path/posre.itp

# Replace "./charmm36-jul2022.ff" by "../charmm36-jul2022.ff" in topol.top
sed -i 's/\.\/charmm36-jul2022\.ff/..\/charmm36-jul2022\.ff/g' $path/topol.top

# Define the box
gmx_mpi editconf -f $path/$file_name.gro -o $path/$file_name-box.gro -bt dodecahedron -d 1.0 -c
gmx_mpi solvate -cp $path/$file_name-box.gro -cs spc216.gro -o $path/$file_name-solv.gro -p $path/topol.top

# Add ions
# -maxwarn 1: ignore warnings (does not like PME for non neutral systems)
gmx_mpi grompp -f template/1.minim.mdp -c $path/$file_name-solv.gro -p $path/topol.top -o $path/ions.tpr -maxwarn 1
# echo allows to answer the interactive selection of the group to replace by the ions
echo SOL | gmx_mpi genion -s $path/ions.tpr -o $path/$file_name-solv-ions.gro -p $path/topol.top -pname NA -nname CL -neutral -conc 0.15

# Replace "#include "$path/posre_Protein_chain_A.itp" " by "#include "posre_Protein_chain_A.itp" in topol_Protein_chain_A.itp for any A, B and C
# for chain in A
# do
#     sed -i "s|#include \"${path}/posre_Protein_chain_${chain}.itp\"|#include \"posre_Protein_chain_${chain}.itp\"|g" $path/topol_Protein_chain_${chain}.itp
# done

sed -i 's|#include "'$path'/posre.itp"|#include "posre.itp"|g' $path/topol.top
import sys
import os

os.system("wget -qnc https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh")
os.system("bash Miniforge3-Linux-x86_64.sh -bfp /usr/local")
os.system("mamba config --set auto_update_conda false")
sys.path.append('/usr/local/lib/python3.12/site-packages/')
os.system("mamba install -y -c conda-forge -c veloxchem veloxchem xtb-python dftd4-python py3Dmol MDAnalysis openmm matplotlib python=3.12")
os.system("pip install rdkit")
import veloxchem as vlx

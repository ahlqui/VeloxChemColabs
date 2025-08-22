!/bin/bash
python sys.path.append('/usr/local/lib/python3.12/site-packages/')
mamba install -y -c conda-forge -c veloxchem veloxchem xtb-python dftd4-python py3Dmol MDAnalysis openmm matplotlib python=3.12
pip install rdkit
python import veloxchem as vlx

import sys
import os

python_version = f"{sys.version_info.major}.{sys.version_info.minor}"

os.system("wget -qnc https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh")
os.system("bash Miniforge3-Linux-x86_64.sh -bfp /usr/local")
os.system("mamba config --set auto_update_conda false")
site_packages_path = f"/usr/local/lib/python{python_version}/site-packages/"
os.environ['PYTHONPATH'] = site_packages_path + ':' + os.environ.get('PYTHONPATH', '')
os.system(f"mamba install -y -c conda-forge -c veloxchem veloxchem xtb-python dftd4-python py3Dmol MDAnalysis openmm matplotlib python={python_version}")
os.system("pip install rdkit")

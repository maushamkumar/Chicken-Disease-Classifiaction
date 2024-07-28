import os 
from pathlib import Path
import logging 

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "CNNClassifier"

list_of_files = [
    ".github/workflows/.gitkeep", 
    f"src/__init__.py", 
    f"src/components/__init__.py", 
    f"src/utils/__init__.py", 
    f"src/config/__init__.py", 
    f"src/config/configuration.py", 
    f"src/pipeline/__init__.py", 
    f"src/entity/__init__.py", 
    f"src/constants/__init__.py", 
    "config/config.yaml", 
    "dvc.yaml", 
    "params.yaml", 
    "requirement.txt", 
    "setup.py", 
    "research/trials.ipynb"
    
    
    
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(F"Creating Directory: {filedir} for the file: {filename}")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass 
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already exists")
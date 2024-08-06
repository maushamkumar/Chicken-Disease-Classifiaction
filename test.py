import os
from box.exceptions import BoxValueError
import yaml
from src import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """Reads yaml file and returns 
    
    Args: 
        path_to_yaml (str): path like input
        
    Raises:
        ValueError: if yaml file is empty
        e: empty file
        
    Returns:
        configBox: ConfigBox type
    """
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError: 
        raise ValueError("yaml file is empty")
    except Exception as e:
        return e 
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Create list of directories
    
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")
            
    
# While doing evaluation at the time I'll get some loss and accuracy 
# matrix okey that matrix I'll be saving as json okey that's why I need this 
@ensure_annotations
def save_json(path: Path, data: dict):
    """Save json data
    
    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        
    logger.info(f"json file saved at: {path}")
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data 
    
    Args:
        Path(Path): Path to json file
        
    Returns: 
        ConfigBox: data as class attributes instead of dict
    """
    
    with open(path) as f:
        content = json.load(f)
        
    logger.info(f"josn file loaded successfully from: {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """Save binary file
    
    Args: 
        data (Any): data to be saved as binary 
        path(Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")
    
@ensure_annotations
def load_bin(path: Path) -> Any:
    """load binary data
    
    Args: 
        path(Path): path to binary file
        
    Returns:
        Any: Object stored in the file 
    """
    
    data = joblib.load(path)
    logger.info(f"binary file loaded from: {path}")
    return data 

@ ensure_annotations
def get_size(path: Path) -> str:
    """get size in KB
    
    Args: 
        path (Path): path of the file
        
    Returns: 
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~{size_in_kb} KB"

def decoderImage(imgstring, fileName):
    imgdata = base64.b64decode(imgstring)
    with open(fileName, 'wb') as f:
        f.write(imgdata)
        f.close()
        
def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, 'rb') as f:
        return base64.b64encode(f.read())
        
    
    
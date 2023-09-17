import os 
from box.exceptions import BoxValueError
import yaml
from wine_quality import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(path_to_yaml: Path)->ConfigBox:
    """
    Reads yaml file and returns
    Args:
        path_to_yaml (str): path like input
    Raises:
        ValueError: if yaml file is empty
        e: empty file
    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content =yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("YAML file is Empty")

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories
    Args:
        path_to_directories (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created Directory At: {path}")

@ensure_annotations
def save_json(path: Path,data:dict):
    """
    Save JSON data
    Args:
        path(Path): path to json file
        data(dict): data to be saved in json file
    """
    with open(path,"w") as f:
        json.dump(data,f,indent=4)
    logger.info(f"JSON File Saved At {path}")

@ensure_annotations
def load_json(path: Path)->ConfigBox:
    """
    Load JSON files data
    Args:
        path(Path): path to json file
    Returns:
        ConfigBox: data as class attributes instead of dict
    """
    with open(path) as f:
        content=json.load(f)
    logger.info(f"JSON File Loaded Succesfully From  {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data:Any,path:Path):
    """
    Save binary file
    Args:
        data(Any): data to be saved as binary
        path(Path): path to binary file
    """
    json.dump(value=data, filename=path)
    logger.info(f"Binary File Saved At {path}")

@ensure_annotations
def load_bin(path:Path):
    """
    Load binary file
    Args:
        path(Path): path to binary file
    Returns:
        Any:object stored in the file
    """
    data =joblib.load(path)
    logger.info(f"Binary File Loaded From {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get size in KB
    Args:
        path (Path): path of the file
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
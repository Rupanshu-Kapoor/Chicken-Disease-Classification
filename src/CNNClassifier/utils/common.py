import os
from box.exceptions import BoxValueError
import yaml
from CNNClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a YAML file from the given path and returns its contents as a ConfigBox object.
    
    Args:
        path_to_yaml (Path): The path to the YAML file to be read.
        
    Returns:
        ConfigBox: The contents of the YAML file as a ConfigBox object.
        
    Raises:
        ValueError: If the YAML file is empty.
        Exception: If any other exception occurs during the reading process.
    """
    
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directory: list, verbose=True):
    """
    Creates directories based on the paths provided in the list. Optionally, it can log the creation of each directory if verbose is set to True.
    
    Args:
        path_to_directory (list): List of paths for which directories need to be created.
        verbose (bool): If True, log the creation of each directory.
    """
    
    for path in path_to_directory:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Saves the input data to a JSON file at the specified path.

    Args:
        path (Path): The path where the JSON file will be saved.
        data (dict): The data to be saved to the JSON file.
    """

    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logger.info(f"json file saved at {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    Loads the contents of a JSON file at the specified path as a ConfigBox object.

    Args:
        path (Path): The path to the JSON file to be loaded.

    Returns:
        ConfigBox: The contents of the JSON file as a ConfigBox object.
    """

    with open(path) as f:
        content = json.load(f)
    
    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves the input data as a binary file at the specified path.

    Args:
        data (Any): The data to be saved as a binary file.
        path (Path): The path where the binary file will be saved.

    Returns:
        None
    """

    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    Load a binary file from the specified path and return the data.

    Args:
        path (Path): The path to the binary file.

    Returns:
        Any: The data loaded from the binary file.

    """
    data = joblib.load(path)
    logger.info(f"binary file loaded successfully from: {path}")
    return data


@ensure_annotations
def get_size(path: Path) -> str:
    """
    Get the size of a file in kilobytes.

    Args:
        path (Path): The path to the file.

    Returns:
        str: The size of the file in kilobytes, formatted as " ~{size_in_kb} KB".
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f" ~{size_in_kb} KB"


def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    """
    Decodes a base64 encoded image string and saves it to a file.

    Args:
        imgstring (str): The base64 encoded image string.
        filename (str): The name of the file to save the decoded image.

    Returns:
        None
    """
    with open(filename, "wb") as f:
        f.write(imgdata)
        f.close()
    

def encodeImageIntoBase64(image):
    """
    Encodes an image into a base64 encoded string.

    Args:
        image (str): The path to the image file.

    Returns:
        str: The base64 encoded image string.
    """
    with open(image, "rb") as f:
        return base64.b64encode(f.read()).decode()

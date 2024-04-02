from typing import List, Optional, Dict, Union
from pydantic import BaseModel, ValidationError
import yaml

class DataConfig(BaseModel):
    csv_path: Optional[str] = None
    json_path: Optional[str] = None
    parquet_path: Optional[str] = None

class SKLearnConfig(BaseModel):
    model: str
    params: Dict[str, Union[int, float, str]]

class ToolConfig(BaseModel):
    use: bool
    brokers: Optional[List[str]] = None
    topic: Optional[str] = None
    tracking_uri: Optional[str] = None
    entity: Optional[str] = None
    project: Optional[str] = None
    url: Optional[str] = None
    params: Optional[Dict[str, str]] = None

class AppConfig(BaseModel):
    project_name: str
    environment: str
    data: DataConfig
    tools: Dict[str, ToolConfig]

def load_config(file_path: str) -> AppConfig:
    """Load and validate the configuration from a YAML file.

    Args:
        file_path (str): The path to the YAML configuration file.

    Returns:
        AppConfig: The validated application configuration.
    """
    with open(file_path, 'r') as file:
        config_data = yaml.safe_load(file)
    return AppConfig(**config_data)

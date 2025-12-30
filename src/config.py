"""
JARVIS Configuration Module
===========================
Central configuration loading from config.yaml and .env
"""

import os
from pathlib import Path
from typing import Any, Dict
import yaml
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

# Load .env file
load_dotenv()

class JarvisSettings(BaseSettings):
    """JARVIS Pydantic Settings"""
    
    # API Keys
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")
    elevenlabs_api_key: str = os.getenv("ELEVENLABS_API_KEY", "")
    
    # Backend
    backend_host: str = "127.0.0.1"
    backend_port: int = 8000
    
    # Paths
    project_root: Path = Path(__file__).parent.parent
    data_dir: Path = project_root / "data"
    models_dir: Path = project_root / "models"
    logs_dir: Path = project_root / "logs"
    
    class Config:
        env_file = ".env"

# Load config.yaml
def load_config() -> Dict[str, Any]:
    """Load configuration from config.yaml"""
    config_path = Path("config.yaml")
    if not config_path.exists():
        raise FileNotFoundError("config.yaml not found!")
    
    with open(config_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

# Global config
config = load_config()
settings = JarvisSettings()

print("✅ JARVIS Configuration loaded successfully!")
print(f"Project root: {settings.project_root}")
print(f"Config loaded: {len(config)} sections")

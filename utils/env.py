#!/usr/bin/env python3
from dataclasses import dataclass
from dotenv import load_dotenv, dotenv_values
load_dotenv()

@dataclass(frozen=True)
class EnvBase:
    """Setup for environment variables, check .env for attributes"""
    ENV: str = "dev"
    DB_HOST: str = "localhost"
    DB_NAME: str = ""
    DB_USERNAME: str = ""
    DB_PASSWORD: str = ""

    def __post_init__(self):
        for k, v in dotenv_values().items():
            # setattr(self, k, v)
            object.__setattr__(self, k, v)

Env = EnvBase()

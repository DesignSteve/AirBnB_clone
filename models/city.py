#!/usr/bin/python3
"""User class module"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class to manage city attributes"""
    state_id = ""
    name = ""

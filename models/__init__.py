#!/usr/bin/python3
"""Instance that initializes the application"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()

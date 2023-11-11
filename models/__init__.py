#!/usr/bin/python3
""" __init__ that creates a unique storage instance for the application """
from .engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()

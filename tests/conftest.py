"""Archivo de configuracion para pytest."""
import os
import sys
from pathlib import Path

# Agregamos el path de la app para los import de python
app_path = os.path.join(Path(__file__).resolve().parents[1], "app")
sys.path.insert(0, app_path)




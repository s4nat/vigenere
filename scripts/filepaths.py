from pathlib import Path
from os import listdir, path

ROOT_DIR = (Path.cwd())
DATA_DIR = Path(ROOT_DIR, "CrypticFiles")
OUTPUT_DIR = Path(DATA_DIR, "output")
# CIPHERS_DIR = Path(OUTPUT_DIR, "ciphertexts")
# GIVEN_DIR = Path(OUTPUT_DIR, "long-key")

paths = {
    'ROOT_DIR' : (Path.cwd()).parent,
    'DATA_DIR' : Path(DATA_DIR),
    'OUTPUT_DIR' : Path(OUTPUT_DIR),
    # 'CIPHERS_DIR' : Path(CIPHERS_DIR),
    # 'GIVEN_DIR' : Path(GIVEN_DIR),
    
}

for p in paths.values():
    p.mkdir(exist_ok=True)
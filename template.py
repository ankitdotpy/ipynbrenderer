import os
from pathlib import Path
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s: %(levelname)s]: %(message)s"
)

while True:
    project_name = input("Enter project name: ")
    if project_name:
        break

logging.info(f'Creating project: {project_name}')

list_of_files = [
    '.github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'test/__init__.py',
    f'test/unit/__init__.py',
    f'test/integration/__init__.py',
    'setup.py',
    'init_setup.sh',
    'requirements.txt',
    'requirements_dev.txt',
    'pyproject.toml',
    'setup.cfg',
    'tox.ini',
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir,filename = os.path.split(filepath)
    if filedir!='':
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'Creating directory: {filedir}')
    if (not os.path.exists(filepath)):
        with open(filepath,'w') as f:
            pass
        logging.info(f'Creating a new file: {filename}')
    else:
        logging(f'{filename} already present at {filepath}')

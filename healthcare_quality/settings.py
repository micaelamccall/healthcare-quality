import os
import sys
def set_root_dir():
    """Sets the root directory of the project"""
    print("Verifying current working directory, which is: " + str(os.getcwd()))
    
    if os.getcwd()[-33:] != 'drug-consumption/drug_consumption':
        print('Appending project directory to the current working directory...')
        PROJ_ROOT_DIR = os.path.join(os.getcwd(), "drug_consumption")
    else:
        PROJ_ROOT_DIR = os.getcwd()

    return PROJ_ROOT_DIR

PROJ_ROOT_DIR=set_root_dir()

def make_proj_module(project_directory=PROJ_ROOT_DIR):
    """Tells python to check in this directory for modules"""
    if not PROJ_ROOT_DIR in sys.path:
        print("Telling python to check for modules in the project directory...")
        sys.path.append(os.path.abspath(PROJ_ROOT_DIR))
    else:
        print("Python is checking for modules in this directory")

if __name__ == '__main__':
    make_proj_module()
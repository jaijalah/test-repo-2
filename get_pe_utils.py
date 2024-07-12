import sys

ROOT_REPO = "platform-enablement"

file_paths = {
    "constants": "",
    "static_data_functions": "/common/src",
    "contract_creation": "/contract-creation/src",
    "portfolios": "/portfolio-builder/src"
}

def get_system_path():
    system_path = sys.path[0]

    return system_path

def __get_file(system_path: str, file_to_look_for: str = None):
    # Get path to repo where the file lives.
    head, sep, tail = system_path.partition(ROOT_REPO)
    repo_path = head+sep+file_paths[file_to_look_for]

    # Dynamically reference repo in order to point to file.
    sys.path.insert(0, repo_path)

def get_constants(system_path: str):
    __get_file(system_path, "constants")

    import Constants
    return Constants

def get_static_data_functions(system_path: str):
    __get_file(system_path, "static_data_functions")

    import static_data_functions
    return static_data_functions

def get_contract_creation(system_path: str):
    __get_file(system_path, "contract_creation")

    import contract_creation
    return contract_creation

def get_portfolios(system_path: str):
    __get_file(system_path, "portfolios")

    import portfolios
    return portfolios
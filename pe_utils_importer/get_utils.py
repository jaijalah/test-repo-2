import sys

ROOT_REPO = "platform-enablement"

def get_system_path():
    system_path = sys.path[0]

    return system_path

def get_file(system_path: str, this_is_static_data_functions: bool = False):
    # Get path to repo where the file lives.
    head, sep, tail = system_path.partition(ROOT_REPO)

    if this_is_static_data_functions == True:
        repo_path = head+sep+'/common/src'
        print(repo_path)
    else:
        repo_path = head+sep

    # Dynamically reference repo in order to point to file.
    sys.path.insert(0, repo_path)

def get_constants(system_path: str):

    get_file(system_path)

    import Constants
    return Constants

def get_static_data_functions(system_path: str):

    get_file(system_path, True)

    import static_data_functions
    return static_data_functions
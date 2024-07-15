import sys
import os

ROOT_REPO = "platform-enablement"

FILE_PATHS = {
    "constants": "",
    "static_data_functions": "/common/src",
    "contract_creation": "/contract-creation/src",
    "portfolios": "/portfolio-builder/src"
}

def get_pe_utils(*utils_to_get):
    # We take the system path from the working directory where this function
    # is called so that later we can dynamically retrieve the requested utils
    # from the requesting user's path.
    system_path = os.path.abspath(sys.argv[0])

    pe_utils = []

    for util in utils_to_get:
        try:
            retrieved_util = __get_file(system_path, util)
            pe_utils.append(retrieved_util)
        except:
            print(f"""ERROR: You may have misspelled a util name. You passed 
                  through '{util}', but currently the only supported utils 
                  are: 'constants', 'static_data_functions', 'contract_creation' 
                  and 'portfolios'. Please pass through one of these values.
                  \nIf your value still doesn't match up to any of those, 
                  it probably means that it has not yet been added to the 
                  pe-utils-importer module or that it just doesn't exist.""")
            
    # You get an AttributeError if the returned list only has one element, 
    # but if you return the single element itself i.e. outside of a list,
    # then there is no error.
    if len(pe_utils) == 1:
        return pe_utils[0]
    else:
        return pe_utils

def __get_file(system_path: str, file_to_look_for: str = None):
    # Most utils live in different folders in the PE repo,
    # which is why a separate method is needed from the get_pe_utils method
    # in order to get the files needed for each util.
    
    # Get the path to the repo where the file lives.
    head, sep, tail = system_path.partition(ROOT_REPO)
    repo_path = head+sep+FILE_PATHS[file_to_look_for]

    # Dynamically reference repo in order to point to relevant file.
    sys.path.insert(0, repo_path)

    # We use the builtin Python __import__ method because we want to import
    # using a variable name.
    util_to_import = __import__(file_to_look_for)
    return util_to_import
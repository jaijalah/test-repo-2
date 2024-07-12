# pe-utils-importer

A package for importing the various utililies and helpers from the root `platform-enablement` repo into the working directory. 

This is necessary because not everyone will store their repos in the same parent directories - otherwise we could just use static paths. This module is just the backend magic to make the scripts work smoothly for everyone regardless of their repo locations, so that we don't need to glob the path every time we need a utility or helper.

## Installation

Via CLI: `pip install "git+https://github.com/jaijalah/test-repo-2.git"`

Via requirements.txt: `pe-utils-importer @ git+https://github.com/jaijalah/test-repo-2.git`


## Usage

1. Import the module into your file.
```
from get_pe_utils import get_system_path, get_static_data_functions, get_constants
```

2. Within the same file, get the system path using the module's get_system_path method.
```
system_path = get_system_path()
```

3. Use one of the methods to import your utilities i.e. `get_static_data_functions` and `get_constants`, make sure to pass through the system path.

```
static_data_functions = get_static_data_functions(system_path)

constants = get_constants(system_path)
```

4. If using constants, retrieve the specific constants you need like this:
```
PROD_URL = constants.PROD_URL
```
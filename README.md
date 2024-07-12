# pe-utils-importer

A package for importing `static_data_functions.py` and `Constants.py` and  files in the root `pe` repo into the working directory.

## Usage

1. Import the module into your file.
```
from pe_utils_import.import_utils import get_static_data_functions, get_constants
```

2. Within the same file, get the system path.
```
system_path = sys.path[0]
```

3. Use the `get_static_data_functions` and `get_constants` methods to import the static_data_functions and constants, pass through the system path.

```
static_data_functions = get_static_data_functions(system_path)

constants = get_constants(system_path)
```

4. Reference the specific constants you need as such:
```
PROD_URL = constants.PROD_URL
```
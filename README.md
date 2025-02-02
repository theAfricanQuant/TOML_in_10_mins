# What is a TOML file?

TOML,which stands for **Tom's Obvious, Minimal Language**, is a configuration file format that prioritizes human readability. It was created in 2013 and named after its creator. TOML aims to be a minimal configuration file format that is easy to read, maps unambiguously, and is easy to parse. TOML supports familiar syntax including strings, integers, floats, and booleans.

Here are some key features of TOML:
*   **Basic Syntax**: A typical TOML file consists of key-value pairs.
*   **Comments**: You can add comments to a TOML file using the hash symbol `#`.
*   **Data Types**: TOML supports strings, integers, floats, and booleans. Boolean values are represented in lowercase as `true` and `false`.
*   **Tables**: You can group related key-value pairs into tables using square brackets `[]` followed by a name, for example, `[items]`. Tables can contain other nested tables. Subtables are created using dot notation, such as `items.details`.
*  **Subkeys:** You can create subkeys using dot notation, such as `file.type` and `file.path`.
*   **Inline Tables:**  Inline tables can be created using curly braces `{}` and are suitable for short, simple dictionaries.
*   **Lists of Tables**: You can create a list of tables by using double square brackets `[[ ]]`. Each table group in the list will be grouped together.
*   **No Null Type**: TOML does not have a null type, so `none` cannot be used and values cannot be left blank.
*   **UTF-8 Encoding**: TOML files use UTF-8 encoding, which supports a wide variety of symbols and characters. If you use a symbol that is not a normal letter or number, you must surround the symbol in quotation marks. Both single and double quotation marks work, but double quotation marks are often preferred.

TOML files are typically used for configuration purposes and can be loaded into your projects to grab information. In Python 3.11 and later, you can use the `tomllib` library to load TOML data, which returns a dictionary that can then be accessed in your script. Changes made to a TOML file will be reflected in your project once the file is reloaded.

## Getting Started with TOML

To get started with TOML, you can follow these steps:

*   **Create a new TOML file** with the extension `.toml`. For example, `config.toml`. This file will hold the configuration for your code.
*   **Add key-value pairs** to the file. For instance, you can define a `name` for your project, a `version` number, and a `website`.
*   You can **write comments** in the TOML file using a hash symbol `#`.
*   **Load the TOML data** into your script. As of Python 3.11, you can use the `tomllib` library to load the TOML data. You can use the `load()` method from the `tomllib` library to load the TOML data from a file, which will return a dictionary.
*   **Access the data** from the loaded dictionary in your script.
*   **Make changes** to the TOML file which will then be reflected in your project.

Here's a basic example of how you would write a TOML file:

```toml
# config file
name = "my project"
version = "1.0.0"
website = "example.com"
```

Here's how you can load and print this TOML data in Python:

```python
import tomllib
from pprint import pprint

def load_toml():
    with open("config.toml", "rb") as f:
        toml_data = tomllib.load(f)
    return toml_data

if __name__ == "__main__":
    data = load_toml()
    pprint(data, sort_dicts=False)
```

Additionally, you can also use tables, sub-tables, sub-keys, and inline tables for more complex configurations. You can also create lists of tables. TOML also supports timestamps, which are returned as objects based on your programming language.


[Link to video](https://youtu.be/D_Jb52jw2HY?list=TLPQMDEwMjIwMjVkXBizuVE2WA)
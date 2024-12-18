# acms80870_project_palathinkal

## Review of displib package:

To create the `dsiplib` package, I started by setting up the project structure using a `src`-based layout, with the source code in `src/dsiplib` and tests in the `tests` folder. Inside `src/dsiplib`, I created two modules: `haversine.py` for calculating distances using the Haversine formula and `earfcn_to_freq.py` for converting EARFCN values to frequencies. An `__init__.py` file was added to expose these functions for easy import.

Unit tests for both functions were written and stored in `tests`. I used `pytest` to ensure all tests passed. For dependency management, I configured a `pyproject.toml` file using Poetry, specifying metadata, dependencies, and the `src` directory as the package root. The package was built with `poetry build` and tested locally using `pip install -e .`.

The package was pushed to GitHub and made installable directly from the repository using `pip install git+https://github.com/joshuaroy873/acms80870_project_palathinkal.git#subdirectory=dsiplib`. A detailed `README.md` in the `dsiplib` folder documents installation, usage, and examples. For more information, please refer to the `README` in the `dsiplib` folder.

Additionally, information about the `\final_project` is provided in the `\final_project\documents\final_report.pdf` file. Please refer to this document for further details.
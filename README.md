# acms80870_project_palathinkal

## Review of `displib` package:

To create the `dsiplib` package, I started by setting up the project structure using a `src`-based layout, with the source code in `src/dsiplib` and tests in the `tests` folder. Inside `src/dsiplib`, I created two modules: `haversine.py` for calculating distances using the Haversine formula and `earfcn_to_freq.py` for converting EARFCN values to frequencies. An `__init__.py` file was added to expose these functions for easy import.

Unit tests for both functions were written and stored in `tests`. I used `pytest` to ensure all tests passed. For dependency management, I configured a `pyproject.toml` file using Poetry, specifying metadata, dependencies, and the `src` directory as the package root. The package was built with `poetry build` and tested locally using `pip install -e .`.

The package was pushed to GitHub and made installable directly from the repository using `pip install git+https://github.com/joshuaroy873/acms80870_project_palathinkal.git#subdirectory=dsiplib`. A detailed `README.md` in the `dsiplib` folder documents installation, usage, and examples. For more information, please refer to the `README` in the `dsiplib` folder.

## Review of `final_project`:

Additionally, information about the `\final_project` is provided in the `\final_project\documents\final_report.pdf` file. This document contains a comprehensive explanation of the project's objectives, methods, and results. Please refer to this document for further details.

All notebook files inside the `\final_project\notebooks` folder are reproducible using the `final_project\environment.yml` file, which is a Conda environment file. To reproduce the results, create a Conda environment using the following command:
```bash
conda env create -f final_project/environment.yml
conda activate acms_env
```

After activating the `acms_env` environment, you can run the notebooks to reproduce the analyses and results.
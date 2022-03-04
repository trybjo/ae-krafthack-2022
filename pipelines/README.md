# AE Krafthack 2022 - Pipelines and Data Workflows

## Directory structure

    ├── requirements.txt      <- The requirements for reproducing the test environment
    ├── pipelines.py          <- The CLI entry point for all the pipelines
    ├── <repo_name>           <- Code for the various steps of the pipelines
        ├──  __init__.py
        ├── etl.py            <- Download, generate, and process data
        ├── visualize.py      <- Create exploratory and results oriented visualizations
        ├── features.py       <- Turn raw data into features for modeling
        ├── train.py          <- Train and evaluate models
        └── test.py           <- Test and validate models
    

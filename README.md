# Cookiecutter Container Workload

_A template for Container Workloads on GVA_



## Project Structure
~~~
root/
  ├── .github/
  │    └── workflows/     <- Scripts to be run on PUSH to GitHub
  │       ├── container_scan.yml
  │       ├── maintainability.yml
  │       ├── regression_suite.yml
  |       ├── secrets.yml
  |       ├── stale.yml
  │       └── static_analysis.yml
  │
  ├── src/
  │   ├── models/         <- Data models
  │   ├── main.py
  │   └── ...             <- Other files and folders to create the application
  │
  ├── tests/
  │   └── ...             <- Unit and regression test scripts, will be 
  │                          automagically run on PUSH to GitHub
  │
  ├── .env                <- Development environment variables
  ├── .gitignore          <- Tells git what not to check-into GitHub
  ├── cloudbuild.yaml     <- CloudBuild deployment script
  ├── dockerfile          <- Docker container build script
  ├── README.md           <- The top-level README explaining the project.
  ├── requirements.txt    <- The requirements file for all dependencies usually
  │                          generated with `pip freeze > requirements.txt`
  └── TEMPLATE            <- The version of the template
~~~

### Notes
- The provided files should not be updated except for `main.py`, `README.md`
  and `requirements.txt`, it is expected that there will be a bot written
  at some point in the future to ensure repos are updated when the template
  is updated
- The default `dockerfile` exposes port 8080, your app should do the same
- Tests will only be executed if they are named `test_*.py`
- Stale Pull Requests will be pruned once a week, at 0400 on Monday

### Quality Bars
| Measure | Tool | Script | Passing Metric |
| ------- | ---- | ------ | -------------- |
| Count of components with known weaknesses | trivy | container_scan | 0 Patchable AND CRITICAL |
| Maintainability Index | radon | maintainability | over 50 |
| Percentage Stale Components | PyPI | maintainability | less than 20% |
| Count of failed regression tests | pytest | regression_suite | 0 |
| Percentage of untested code | coverage | regression_suite | less than 20% |
| Count of weak coding practices | bandit | static_analysis  | 0 |
| Count of leaked secrets | TruffleHog | secrets | 0 |

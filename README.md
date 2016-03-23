# Sentiment in research software


This repository provides the `flask` app to coordinate and visualise
all the different modules needed to analyse your software package.

## Requirements

- `flask`
- `pandas`
- `bokeh`

using `requirements.txt`

or install a conda environment using the `environment.yml` as:

```bash
conda create --name happy --file environment.yml
source activate happy
```

## Deployment

```bash
python happy.py
```

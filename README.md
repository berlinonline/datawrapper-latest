# Datawrapper Latest

A simple class that gets the current version number of a [Datawrapper](https://www.datawrapper.de) project based on the chart Id.
This is necessary because currently there is no API that does this, and no automatic redirect to the current version (that doesn't involve JavaScript!).

## Requirements

- Python (tested with Python 3.13)
- [requests](https://pypi.org/project/requests/)


## Installation

### ... as a project requirement

Add this repository as a requirement to your project by adding the following line to your project's `requirements.txt`:

```
datawrapper-latest @ git+https://github.com/berlinonline/datawrapper-latest@main
```

Install the requirements:

```
$ pip install -r requirements.txt
```

### ... directly with pip

Alternatively, install directly via `pip`:

```
pip install git+https://github.com/berlinonline/datawrapper-latest@main
```

### ... from source

You can also clone the repository and install it from source:

```
$ git clone https://github.com/berlinonline/datawrapper-latest
$ cd datawrapper-latest
$ python -m venv venv
$ . venv/bin/activate
(venv) $ pip install .
```

## Usage

### From the Command Line

If you have cloned the repository, you can use the `get_latest` script that comes with it:

```
(venv) $ python bin/get_latest.py --help
usage: get_latest.py [-h] [--base_url BASE_URL] CHART_ID

Get the URL for the data of the latest version of a DataWrapper chart.

positional arguments:
  CHART_ID

options:
  -h, --help           show this help message and exit
  --base_url BASE_URL  Base URL of the DataWrapper service. Default: https://datawrapper.dwcdn.net
```

For example:

```
(venv) $ python bin/get_latest.py gaYjb 
https://datawrapper.dwcdn.net/gaYjb/4/dataset.csv
```

### In Code

If you have installed the Datawrapper connector into the site packages (with `pip` or otherwise), you can use it in code like this:

```python
from berlinonline.datawrapper.connector import Connector

chart_id = 'gaYjb'
connector = Connector()
latest_version = connector.latest_version(chart_id)
# 'https://datawrapper.dwcdn.net/gaYjb/4/'

data_url = connector.data_url(chart_id)
# 'https://datawrapper.dwcdn.net/gaYjb/4/dataset.csv'
```

Also, check out [bin/get_latest.py](bin/get_latest.py).

## License

All code in this repository is published under the [MIT License](License).

import argparse
from berlinonline.datawrapper.connector import Connector

DEFAULT_BASE_URL = 'https://datawrapper.dwcdn.net'

parser = argparse.ArgumentParser(
    description="Get the URL for the data of the latest version of a DataWrapper chart.")
parser.add_argument('CHART_ID'),
parser.add_argument('--base_url',
                    help=f"Base URL of the DataWrapper service. Default: {DEFAULT_BASE_URL}",
                    type=str,
                    default=DEFAULT_BASE_URL
                    )

args = parser.parse_args()

connector = Connector(base_url=args.base_url)
data_url = connector.data_url(chart_id=args.CHART_ID)
print(data_url)

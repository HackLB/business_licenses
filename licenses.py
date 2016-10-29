#!/usr/bin/env python
import os, sys
import requests
import simplejson as json
from pprint import pprint


api_url = 'http://dev.longbeachca.opendata.arcgis.com/datasets/6da7e4cfba7446faa7d6a734eef93cea_0.geojson'


def get_subdirectory(base_name):
    """
    Takes the base filename and returns a path to a subdirectory, creating it if needed.
    For example, given the base name 0003168449, returns a path like:
    ./_data/0003/16/84
    """
    sub_dir = os.path.join(data_path, base_name[0:-6], base_name[-6:-4], base_name[-4:-2])
    os.makedirs(sub_dir, exist_ok=True)
    return sub_dir


def get_business_license_data():
    print('Getting business license data...')
    r = requests.get(api_url)
    return r.json()['features']


def save_license_data(records):
    print('Saving business license data...')
    for record in records:
        license_number = record['properties']['LICENSENO']
        file_name = '{}.json'.format(license_number)
        directory = get_subdirectory(license_number)

        path = os.path.join(directory, file_name)
        with open(path, 'w') as f:
            json.dump(record, f, indent=4, ensure_ascii=False, sort_keys=True)


if __name__ == "__main__":
    repo_path = os.path.dirname(os.path.realpath(sys.argv[0]))    # Path to current directory
    data_path = os.path.join(repo_path, '_data')                  # Root path for record data
    os.makedirs(data_path, exist_ok=True)                         # Create _data directory

    records = get_business_license_data()                         # Fetch license data as JSON
    save_license_data(records)                                    # Save it into _data

"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build a `NEODatabase`.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path: str) -> tuple:
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    neos = []
    with open(neo_csv_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            neos.append(NearEarthObject(row["pdes"], row["name"], row['diameter'], row['pha']))

    return tuple(neos)


def load_approaches(cad_json_path: str) -> tuple:
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    cads = []
    with open(cad_json_path, 'r') as file:
        json_cads = json.load(file)
    indices = {json_cads['fields'].index(column_name): column_name for column_name in ['des', 'cd', 'dist', 'v_rel']}
    for cad in json_cads['data']:
        cads.append(CloseApproach(**{
            indices[key]: cad[key] for key in indices.keys()
        }))
    return tuple(cads)

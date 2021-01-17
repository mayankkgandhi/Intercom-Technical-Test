import argparse
import json
from read_write_customers import get_customers, invite_list_output
from calculate_distance import distance_between_coordinates

def main(config_path):
    """
    This function -
    1) Extracts customer data
    2) Calculates distance between customer and office corodinates
    3) Write text file containing all customers within a 100km of the Dublin office
    """

    # loading config from json
    config = json.load(open(config_path))

    # extracting customer List from given url
    customerList = get_customers(config['customer_list_url'])
    invite_list = []

    # for each customer calculate the distance between 'customer' and Intercom's
    # Dublin office and append to invite_list array
    for customer in customerList:
        distance = distance_between_coordinates(
            config['intercom_latitude'], config['intercom_longitude'],
            customer['latitude'], customer['longitude'])

        if distance <= config['distance_threshold']:
            invite_list.append((customer["name"], customer["user_id"]))

    # sorting the invite_list  by 'user_id' in ascending order
    invite_list.sort(key=lambda k: k[1])

    # saving the invite_list to an output file 'output.txt'
    invite_list_output(invite_list, config['output_file_path'])


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Generate Invite List')
    parser.add_argument('config_path', help='Config File Path')
    args = parser.parse_args()

    try:
        main(args.config_path)
    except KeyError as keyerr:
        raise keyerr
    except Exception as err:
        raise err

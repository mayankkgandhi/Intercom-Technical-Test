import urllib.request
import json

def get_customers(url):
    """
    Extract data from url and return the data
    Parameters:
        url : Given url to extract customers data
    Returns:
        customers: List of each customer in JSON
    """
    # extract data from url
    data = urllib.request.urlopen(url)
    customers = []

    # converting 'customer_data' to a JSON object and
    # appending to cutomers list.
    for customer_data in data:
        decoded = customer_data.decode('utf-8')
        customer_json = json.loads(decoded)
        customers.append(customer_json)

    return customers


def invite_list_output(invite_list, filename):
    """
    Write the invite_list to an output file
    Parameters:
        invite_list: list to read from
        filename: file to write the output
    """
    try:
        with open(filename, "w") as file:
            for invitee in invite_list:
                file.write(f"{invitee[0]}, {invitee[1]}\n")
    except Exception as err:
        raise err

from argparse import ArgumentParser
from ncclient import manager
import requests
from requests.auth import HTTPBasicAuth

if __name__ == '__main__':

    parser = ArgumentParser(description='Select options.')

    # Input parameters
    parser.add_argument('-host', type=str, required=True,
                        help="The device IP or DN")
    parser.add_argument('-u', '--username', type=str, default='cisco',
                        help="Go on, guess!")
    parser.add_argument('-p', '--password', type=str, default='cisco',
                        help="Yep, this one too! ;-)")
    parser.add_argument('-port', type=int, default=8008,
                        help="Specify this if you want a non-default port")

    args = parser.parse_args()

    username = args.username
    password = args.password
    host = args.host
    port = str(args.port)

    url = "http://" + host + ":" + port + "/api/running/native/hostname"

    headers = {
       'content-type': "application/vnd.yang.data+json",
       'accept': "application/vnd.yang.data+json",
       }
    response = requests.request("GET", url, headers=headers, auth=(username,password))

    print(response.text)

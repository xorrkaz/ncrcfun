import sys
from argparse import ArgumentParser
from ncclient import manager

data = '''<filter>
  <native xmlns="urn:ios">
<hostname/>
</native>
</filter>'''

if __name__ == '__main__':

    parser = ArgumentParser(description='Select options.')

    # Input parameters
    parser.add_argument('-host', type=str, required=True,
                        help="The device IP or DN")
    parser.add_argument('-u', '--username', type=str, default='cisco',
                        help="Go on, guess!")
    parser.add_argument('-p', '--password', type=str, default='cisco',
                        help="Yep, this one too! ;-)")
    parser.add_argument('-port', type=int, default=2022,
                        help="Specify this if you want a non-default port")

    args = parser.parse_args()

    m =  manager.connect(host=args.host,
                         port=args.port,
                         username=args.username,
                         password=args.password,
                         device_params={'name':"csr"})
    print m.get(data)

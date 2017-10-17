import argparse
import configparser
import os

from redis import StrictRedis

cparser = configparser.ConfigParser()
cparser.read(os.path.dirname(os.path.realpath(__file__)) + "/defaults.cfg")

aparser = argparse.ArgumentParser()
aparser.add_argument("-c", "--config", help="Specify config file", metavar="FILE")
args, argv = aparser.parse_known_args()

if args.config:
    cparser.read(args.config)
else:
    cparser.read(cparser.get("Core", "config"))

config = {s:dict(cparser.items(s)) for s in cparser.sections()}
config["Core"]["api"] = config["Core"]["api"].split()
config["Core"]["auth"] = config["Core"]["auth"].split()

_db = StrictRedis(host=config["Core"]["redis_host"], \
        port=config["Core"]["redis_port"], db=config["Core"]["redis_db"], \
        password=config["Core"]["redis_password"])

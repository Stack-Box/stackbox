#!/usr/bin/env python3
from __future__ import print_function
import yaml
import sys

# Map a Docker Compose "service" name to its image.
CLIENTS = ['app', 'ui']

# docker-compose.yml skeleton to fill out using "service" entries above.
COMPOSITION = {'version': '3', 'services': {}}


if __name__ == '__main__':

    error_clients = []
    error_services = []

    # Loads the master yaml containing docker service definitions
    with open('./master.yaml') as master_service_file:
        master_services = yaml.load(master_service_file, Loader=yaml.FullLoader)

    # Populates clients in docker-compose
    for client in CLIENTS:
        if client in master_services:
            COMPOSITION['services'][client] = master_services[client]
            COMPOSITION['services'][client]['depends_on'] = []
        else:
            error_clients.append(client)
            CLIENTS.remove(client)

    # Populates services requested by user
    for service in sys.argv[1:]:
        if service in master_services:
            for client in CLIENTS:
                COMPOSITION['services'][client]['depends_on'].append(service)
            COMPOSITION['services'][service] = master_services[service]
        else:
            error_services.append(service)

    with open('docker-compose.yml', 'w') as outfile:
        yaml.dump(COMPOSITION, outfile, default_flow_style=False, indent=2)

    if len(error_services) > 0:
        print("Couldn't add the following services: ")
        for service in error_services:
            print("- "+service+"\n")

#!/usr/bin/env python3
import yaml
import sys
import netifaces as ni

ni.ifaddresses('en0')
ip = ni.ifaddresses('en0')[ni.AF_INET][0]['addr']

# List of clients
CLIENTS = ['flask', 'vue', 'rubyonrails', 'angular']

# docker-compose.yml skeleton to fill out using "service" entries above.
COMPOSITION = {'version': '3', 'services': {}}

if __name__ == '__main__':

    error_clients = []
    error_services = []
    args = sys.argv[1:]
    args = list(dict.fromkeys(args))

    services = [x for x in args if x not in CLIENTS]
    clients = [x for x in args if x in CLIENTS]

    # Loads the master yaml containing docker service definitions
    with open('./master.yaml') as master_service_file:
        master_services = yaml.load(master_service_file, Loader=yaml.FullLoader)

    # Populates clients in docker-compose
    for client in clients:
        if client in master_services:
            COMPOSITION['services'][client] = master_services[client]
            COMPOSITION['services'][client]['depends_on'] = []
        else:
            error_clients.append(client)
            CLIENTS.remove(client)

    # Populates services requested by user
    for service in services:
        if service in master_services:
            for client in clients:
                COMPOSITION['services'][client]['depends_on'].append(service)
            COMPOSITION['services'][service] = master_services[service]
        else:
            error_services.append(service)
        if service == 'kafka':
            COMPOSITION['services'][service]['environment']['KAFKA_ADVERTISED_HOST_NAME'] = ip

    with open('docker-compose.yml', 'w') as outfile:
        yaml.dump(COMPOSITION, outfile, default_flow_style=False, indent=2)

    if len(error_services) > 0:
        print("Couldn't add the following services: ")
        for service in error_services:
            print("- " + service + "\n")

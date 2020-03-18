![Vue](https://github.com/Stack-Box/StackBox/workflows/Vue/badge.svg)

# StackBox
Create app stacks loaded with all your favourite clients, services and infra in under 5 mins.

Sets up a docker containers based infra. Generates a docker-compose.yml for services in the cli params and runs those containers. Specific client code in certain clients like Flask are preconfigured to the exact running ports of services in containers. For example, Flask would have an endpoint view_stacks that will list rows from  a table in the running mysql container.

![Screenshot](https://ik.imagekit.io/sn5/Webp.net-resizeimage_MC8zaRvlY.png)

## Run

    sh stack_box.sh <client-name-1> <client-name-2> <service-name-1> <service-name-2> ...
    
## Example:

    sh stack_box.sh vue flask mysql
 
 The above example brings up the following:
 
 - mysql container 
    - With a sample preloaded table
 - flask backend container 
    - with mysql client code
    - endpoints configured to connect to mysql
 - vue frontend 
    - mysql table views connecting to flask backend
    
## Supported Clients

- vue
- flask

## Supported Services

- mysql
- elasticsearch
- kibana
- nginx

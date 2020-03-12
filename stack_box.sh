#!/bin/bash

args="$*"
python stack.py $args

beginswith() { case $2 in "$1"*) true;; *) false;; esac; }

docker-compose down > logs/docker-compose-down-log.txt
docker-compose build > logs/docker-compose-build-log.txt
docker-compose up -d --remove-orphans

echo "     _             _    _"
echo " ___| |_ __ _  ___| | _| |__   _____  __"
echo "/ __| __/ _  |/ __| |/ / '_ \ / _ \ \/ /"
echo "\__ \ || (_| | (__|   <| |_) | (_) >  <"
echo '|___/\__\__,_|\___|_|\_\_.__/ \___/_/\_\'
echo "\n"

containers=$(docker ps --format '{{.Names}}')
ports="$(docker ps --format '{{.Ports}}')"

service_ports=()

for port in $ports;
do
  if beginswith "0.0.0.0" "$port";
  then
    port1=$(echo "$port" | awk -F[:-] '{print $2}')
    service_ports+=("$port1")
  fi
done

i=-1

for container in $containers;
do
  i=$i+1
  if [ "$container" != "registry" ];
  then
    if beginswith "stackbox" "$container";
    then
      tmp=${container%"_1"}
      echo ${tmp#"stackbox_"} is up at localhost:${service_ports[i]}
    fi
  fi
done
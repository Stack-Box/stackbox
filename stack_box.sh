#!/bin/bash

echo "     _             _    _"
echo " ___| |_ __ _  ___| | _| |__   _____  __"
echo "/ __| __/ _  |/ __| |/ / '_ \ / _ \ \/ /"
echo "\__ \ || (_| | (__|   <| |_) | (_) >  <"
echo '|___/\__\__,_|\___|_|\_\_.__/ \___/_/\_\'
echo "\n"

args="$*"

beginswith() { case $2 in "$1"*) true;; *) false;; esac; }

python_version=$(python --version)
python3_version=$(python3 --version)

if beginswith "Python 3" "$python_version" ;
then
  python stack.py $args
elif beginswith "Python 3" "$python3_version";
then
  python3 stack.py $args
else
  echo "Unable to find a python 3 installation"
fi

docker-compose down > logs/docker-compose-down-log.txt
echo "\n"
docker-compose build > logs/docker-compose-build-log.txt
echo "\n"
docker-compose up -d --remove-orphans

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

echo "\n"

for container in $containers;
do
  i=$i+1
  if [ "$container" != "registry" ];
  then
    if beginswith "stackbox" "$container";
    then
      tmp=${container%"_1"}
      echo ${tmp#"stackbox_"} is up at http://localhost:${service_ports[i]}
    fi
  fi
done
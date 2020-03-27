#!/bin/bash

echo "     _             _    _"
echo " ___| |_ __ _  ___| | _| |__   _____  __"
echo "/ __| __/ _  |/ __| |/ / '_ \ / _ \ \/ /"
echo "\__ \ || (_| | (__|   <| |_) | (_) >  <"
echo '|___/\__\__,_|\___|_|\_\_.__/ \___/_/\_\'
echo "\n"

echo "######## SELECT YOUR STACK #############\n"

stack=()

PS3='Select your backend: '

echo "BACKEND OPTIONS:"

backend_options=("Flask" "Rails")
select opt in "${backend_options[@]}"
do
    case $opt in
        "Flask")
            echo "You've chosen Flask"
            stack+=("flask")
            break;
            ;;
        "Option 2")
            echo "You've chosen Rails"
            stack+=("rubyonrails")
            break;
            ;;
        *) echo "invalid option $REPLY";;
    esac
done

printf "\n"
PS3='Add your services. Choose 5 to finish adding: '

echo "SERVICE OPTIONS:"
service_options=("MySQL" "Kafka" "Elasticsearch" "Nginx" "Done")
select opt in "${service_options[@]}"
do
    case $opt in
        "MySQL")
            echo "You've chosen MySQL"
            stack+=("mysql")
            continue;
            ;;
        "Kafka")
            echo "You've chosen Kafka. Zookeper will also be set up."
            stack+=("kafka")
            stack+=("zookeeper")
            continue;
            ;;
        "Elasticsearch")
            echo "You've chosen Elasticsearch"
            stack+=("elasticsearch")
            # shellcheck disable=SC2162
            read -p "Do you want Kibana as well? (y/n)" yn
              case $yn in
                [Yy]* )
                  echo "You've chosen Kibana + Elasticsearch"
                  stack+=("kibana")
                  continue;;
                [Nn]* )
                  echo "You've chosen Elasticsearch without Kibana"
                  continue;;
                 * ) echo "Please answer yes or no.";;
              esac
            ;;
        "Nginx")
            echo "You've chosen Nginx"
            stack+=("nginx")
            continue;
            ;;
        "Done")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done

printf "\n"
printf "The services you've chosen are:  "
echo "${stack[*]}"
printf "\n"

echo "######## BUILDING YOUR STACK ###############\n"

beginswith() { case $2 in "$1"*) true;; *) false;; esac; }

python_version=$(python --version)
python3_version=$(python3 --version)

if beginswith "Python 3" "$python_version" ;
then
  var="$(pip --disable-pip-version-check install -r requirements.txt) > /dev/null "
  python stack.py ${stack[*]}
elif beginswith "Python 3" "$python3_version";
then
  var="$(pip3  --disable-pip-version-check install -r requirements.txt) > /dev/null"
  python3 stack.py ${stack[*]}
else
  echo "Unable to find a python 3 installation"
fi

docker-compose down 2> /dev/null > logs/docker-compose-down-log.txt
docker-compose build > logs/docker-compose-build-log.txt

echo "\n######## DEPLOYING YOUR STACK ##############\n"

docker-compose up -d --remove-orphans

sleep 5

echo "\n######## YOUR STACK ########################\n"

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
      echo ${tmp#"stackbox_"} is up at http://localhost:${service_ports[i]}
    fi
  fi
done

echo "\n"
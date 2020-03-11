args="$*"
python stack.py $args

docker-compose down
docker-compose build
docker-compose up
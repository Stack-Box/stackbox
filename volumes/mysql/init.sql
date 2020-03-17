CREATE DATABASE stackbox;
use stackbox;

CREATE TABLE stacks(
    name VARCHAR(50) NOT NULL UNIQUE,
    image VARCHAR(100),
    build VARCHAR(10),
    port int,
    PRIMARY KEY(name)
);

INSERT INTO stacks values("mysql", "mysql:5.7", "none", 3306);
INSERT INTO stacks values("elasticsearch", "docker.elastic.co/elasticsearch/elasticsearch:7.0.0", "none", 9200);
INSERT INTO stacks values("kibana", "docker.elastic.co/kibana/kibana:7.0.0", "none", 5601);
INSERT INTO stacks values("app", "python:3.6 custom", "app", 5001);
INSERT INTO stacks values("ui", "node:lts-alpine custom", "ui", 8081);

SELECT * FROM stackbox.stacks;
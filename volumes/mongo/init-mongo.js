 db = db.getSiblingDB("stackbox")


db.runCommand(
   {
      insert: "stacks",
      documents: [
         { name: "mysql", image: "mysql:5.7", build: "none", port: 3306},
         { name: "elasticsearch", image: "docker.elastic.co/elasticsearch/elasticsearch:7.0.0", build: "none", port: 9200 },
         { name: "kibana", image: "docker.elastic.co/kibana/kibana:7.0.0", build: "none", port: 5601 },
         { name: "app", image: "python:3.6 custom", build: "app", port: 5001},
         { name: "ui", image: "node:lts-alpine custom", build: "ui", port: 8081},
      ],
      ordered: false,
      writeConcern: { w: "majority", wtimeout: 5000 }
   }
)

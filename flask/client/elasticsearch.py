from elasticsearch import Elasticsearch
from config.config import Config
from client.mysql import SQLClient


class ElasticsearchClient:

    def __init__(self, config: Config):
        self.es = Elasticsearch([config.es_host], port=config.es_port)
        self.sql_client = SQLClient(config)
        self.index = config.es_index

    def index_es(self, doc_id, doc):
        res = self.es.index(index=self.index, id=doc_id, body=doc)
        print(res)

    def get_id_from_index(self, doc_id):
        res = self.es.get(index=self.index, id=doc_id)
        return res['_source']

    def match_all(self):
        try:
            res = self.es.search(index=self.index, body={"query": {"match_all": {}}})
            j = dict()
            i = 0
            for obj in res['hits']['hits']:
                j[i] = obj['_source']
                i = i+1
            return j
        except:
            return 500


    def full_search(self, query):
        res = self.es.search(index=self.index, body={"query": {"match": {"message" : {"query" : query}}}})
        print("Got %d Hits:" % res['hits']['total']['value'])
        for hit in res['hits']['hits']:
            print("_source: "+str(hit["_source"]))

    def field_search(self, field_name, field_query):
        res = self.es.search(index=self.index, body={"query": {"bool": {"must": [{"term": {field_name: field_query}}]}}})
        print("Got %d Hits:" % res['hits']['total']['value'])
        for hit in res['hits']['hits']:
            print("_source: "+str(hit["_source"]))

    def populate_index_from_mysql(self):
        rows = self.sql_client.fetch_all_stacks()
        i = 0
        for row in rows:
            i = i+1
            body = {
                'name': row[0],
                'image': row[1],
                'build': row[2],
                'port': row[3]
            }
            self.index_es(i, body)

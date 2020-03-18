class JsonUtils:

    @staticmethod
    def json_obj_to_array(res):
        arr = []
        for key in res:
            arr.append(res[key])
        return arr

    @staticmethod
    def array_to_json_array(res):
        arr = []
        for record in res:
            j = dict()
            j['build'] = record[0]
            j['image'] = record[1]
            j['build'] = record[2]
            j['port'] = record[3]
            arr.append(j)
        return arr




import json

def export_to_json(material, json_file):
    output = json.dumps(material, indent=4, ensure_ascii=False)
    op = open(json_file, 'w', encoding="utf-8")
    op.write(output)
    op.close()

def load_from_json(json_file):
    op = open(json_file, 'r')
    data = op.read()
    dic = json.loads(data)
    return dic

def to_dict(para_1, para_2, para_3, para_4, para_5, para_6, para_7):
    return {
        "source" : para_1,
        ".vn" : para_2,
        ".com" : para_3,
        ".com.vn" : para_4,
        ".net" : para_5,
        ".org" : para_6,
        ".info" : para_7
    }
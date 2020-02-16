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

def to_dict(para_1, para_2, para_3, para_4, para_5, para_6, para_7, para_8):
    return {
        "source" : para_1,
        "homepage": para_2,
        ".vn" : para_3,
        ".com" : para_4,
        ".com.vn" : para_5,
        ".net" : para_6,
        ".org" : para_7,
        ".info" : para_8
    }
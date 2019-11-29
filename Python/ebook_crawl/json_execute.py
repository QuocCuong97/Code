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


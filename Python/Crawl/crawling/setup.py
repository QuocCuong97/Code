import json
from .some_modules import news_cloud365_vn

lst = news_cloud365_vn.get_list()
output = json.dumps(lst, indent=4, ensure_ascii=False)
op = open('output.json', 'w', encoding="utf-8")
op.write(output)
op.close()

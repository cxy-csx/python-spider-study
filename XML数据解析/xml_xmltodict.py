import xmltodict
import json


with open('ele.xml', 'r', encoding='utf-8') as fp:
    res = xmltodict.parse(fp.read())
    # print(type(res))  # <class 'collections.OrderedDict'>
    # print(res['root'])
    # dict -> json_str
    json_str = json.dumps(res)
    # print(json_str)
    # json_str -> dict
    dit = json.loads(json_str)
    # print(dit['root']['person']['name'])

    # dict -> xml
    xml = xmltodict.unparse(dit)
    print(xml)





















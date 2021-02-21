import xml.etree.ElementTree as ET
from io import StringIO

# 根据节点树查找节点
obj = ET.ElementTree(file='test.xml')  # xml.etree.ElementTree.ElementTree
# root = obj.getroot()  # 查找根节点
# sub_child = obj.find("student")  # 查找子节点
# sub_child = obj.find("{http://www.itlike.com/itlike}student")  # 查找子节点
# sub_child = obj.find("itlike:student", namespaces={'itlike': 'http://www.itlike.com/itlike'})  # 查找子节点
# all_child = obj.findall("student")  # 查找后代所有节点
# text = obj.findtext("student")  # 查找文本节点, 只返回查找到第一个文本节点对象
# text = obj.findtext("no_exits_node", default='默认值')  # 如果找不到，则使用一个默认值
#
# obj_iter = obj.iter()  # 构建节点树迭代器
# obj_iter = obj.iter('name')  # 对整个节点树做一层过滤
# for ele in obj_iter:
#     print(ele)
#
# obj_iter = obj.iterfind('student')  # 根据查找到的子节点，构建节点树迭代器
# for ele in obj_iter:
#     print(ele)

obj.write('new.xml', encoding='utf-8')  # 写入文件














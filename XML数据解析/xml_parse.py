import xml.etree.ElementTree as ET
from io import StringIO

# 字符串 > ElementTree对象

# 方法一
# with open('test.xml', 'r', encoding='utf-8') as fp:
#     obj = ET.parse(fp)
#     print(obj)  # xml.etree.ElementTree.ElementTree

# 方法二
# obj = ET.parse('test.xml')
# print(obj)

# 方法三
# xml_str = """
#     <root>
#         <name>姓名：逍遥子</name>
#     </root>
# """
# f = StringIO(xml_str)  # 返回一个类文件对象 _io.StringIO object
# obj = ET.parse(f)
# print(obj)

# 方法四
# obj = ET.ElementTree(file='test.xml')
# print(obj)

# ElementTree对象 > Element

# 方法五
# ele = ET.fromstringlist(("<root><name>逍遥子</name>", "<age>18</age></root>"))  # 返回根节点
# obj = ET.ElementTree(ele)  # 根据传入的节点构建节点树
# print(obj)

# 方法一
# with open('test.xml', 'r', encoding='utf-8') as fp:
#     ele = ET.XML(fp.read())  # 根节点
#     print(ele)

# 方法二
ele = ET.fromstringlist(("<root><name>逍遥子</name>", "<age>18</age></root>"))
print(ele)  # root







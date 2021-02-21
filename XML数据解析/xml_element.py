import xml.etree.ElementTree as ET
from io import StringIO

# 创建节点
# ele = ET.Element("name", {"age": "18"})
# ele.text = '逍遥子'
# # 构建节点树
# obj = ET.ElementTree(ele)
# # 写入xml文件
# obj.write('ele.xml', encoding='utf-8')

# 节点属性和方法
obj = ET.ElementTree(file='ele.xml')
# 查找person节点
ele = obj.find('person')
# 节点属性
# print(ele.tag)
# print(ele.attrib)
# print(ele.text)
# print(ele.tail)
# 节点方法
# print(ele.keys())
# print(ele.items())
# print(ele.get('class'))  # 获取节点属性值
# print(ele.attrib['class'])  # 获取节点属性值
# ele.set('info', 'error')  # 设置节点属性

# 增
# 构造新的节点
# sub_ele = ET.Element("new")
# sub_ele.text = 'new'
# ele.append(sub_ele)
# ele.insert(0, sub_ele)

# root = obj.getroot()
# sub_ele = ET.SubElement(root, 'new')
# sub_ele.text = 'new'
# 删
# root = obj.getroot()
# new_node = obj.find('new')
# root.remove(new_node)
# 查
# root = obj.getroot()
# iter_text = root.itertext()  # 文本迭代器
# for text in iter_text:
#     print(text)

# 对节点自身的操作
# root = obj.getroot()
# print(root)
# root.clear()  # 只剩下一个闭合单标签<root />

# 增量式解析
obj = ET.iterparse('ele.xml', events=('start', 'end'))  # 监听开始和结束事件
print(obj)
for event, ele in obj:
    print(event)
    print(ele)

# 保存节点树
# obj.write('ele.xml', encoding='utf-8')

















from bs4 import BeautifulSoup, SoupStrainer


html_str = """
    <div><a href='http://www.baidu.com/'>百度</a>hello<h1><span class='span' id='span'>xxx</span><a>跳转链接</a></h1></div>
    <a>hello world</a>
"""

# 指定不同的解析器
# html = BeautifulSoup(html_str, 'lxml')  # html
# html = BeautifulSoup(html_str, 'html5lib')  # html
# html = BeautifulSoup(html_str, 'html.parser')  # html
# xml = BeautifulSoup(html_str, 'xml')  # xml

# 基本操作
html = BeautifulSoup(html_str, 'lxml')
# print(html)
# print(html.prettify())  # 美化输出
# print(html.reset())  # 清空, 返回None

# 创建标签节点
# div_node = html.new_tag('div', 'http://gmbjzg/', 'gmbjzg', {'class': 'top'})  # <gmbjzg:div class="top"></gmbjzg:div>
# print(div_node)
# print(type(div_node))  # Tag

# 创建文本节点
# text_node = html.new_string('百度')
# print(text_node)
# print(type(text_node))  # NavigableString

# 查找节点
# a_node = html.find('a')  # 返回Tag类
# a_node = html.a  # 简写
# all_a_node = html.find_all('a')  # 返回list [Tag, Tag]
# a_node = html('a')  # 简写 返回list [Tag, Tag]

# 节点操作
a_node = html.a
div_node = html.div
# print(a_node.name)  # 节点名称
# a_node.name = 'b'  # 修改节点名称

# print(a_node.attrs)  # 获取节点属性, 返回一个字典
# print(a_node.get_attribute_list('href'))  # 返回一个列表
# print(a_node.get('href'))

# a_node.href = 'http://www.gmbjzg.top'  # 修改节点属性
# del a_node.href  # 删除节点属性
# print(a_node.has_attr('href'))  # 判断是否拥有某个属性

# print(a_node.text) # 获取文本内容，返回str
# print(div_node.get_text(separator='-', strip=True))  # strip是否去除空格, separator指定分割符

# print(a_node.string)  # 返回一个文本节点类 bs4.element.NavigableString
# print(a_node.string.parent)  # 通过文本节点类查找父节点
# a_node.string = '新浪'  # 赋值操作

# print(div_node.strings)  # 返回一个文本生成器
# print(div_node.stripped_strings)  # 返回一个文本生成器, 去除空格
# a_node.clear()  # 清空子节点
# a_node.decompose()  # 删除自身节点
# print(a_node.is_empty_element)  # 判断是否是空节点 空节点<img/>
# print(div_node.index(a_node))  # 判断子节点的索引位置

# print(div_node.contents)  # 获取所有子节点
# print(div_node.children)  # 获取所有子节点，返回一个迭代器
# print(div_node.descendants)  # 获取所有后代节点， 返回一个生成器


# print(div_node.find('a'))  # 查找节点a, 默认递归查找
# print(div_node.find('span', recursive=False))  # 只查找子节点

# 自定义过滤函数
# def filter_tag(tag):
#     # print(tag)
#     return tag.name == 'a'

# print(div_node.find(filter_tag))

# print(div_node.find('a', attrs={'href': 'http://www.xinlang.com'}))  # 属性过滤
# print(div_node.find(attrs={'class': 'span'}))
# print(div_node.find(text='hello').parent)
# print(div_node.find(class_='span'))
# print(div_node.find_all('a', limit=1))

# CSS3选择器
# print(html.select('div'))
# print(html.select_one('div'))
# print(html.select_one('span.span'))
# print(html.select_one('div a'))
# print(html.select_one('*'))  # 查找所有子节点
# print(html.select_one('.span'))
# print(html.select("[class=span]"))
# print(html.select('span[class=span]'))
# print(html.select("[class=span][id=span]"))
# print(html.select('div a'))
# print(html.select('div>a'))
# print(html.select('div+a'))  # 下一个兄弟节点
# print(html.select('div~a'))  # 后代节点
# print(html.select('span[class=span]'))
# print(html.select('a, span'))  # 查找a和span

# 其他
# print(div_node.parent)  # 父节点
# print(a_node.setup(parent=div_node))
# print(a_node.parent)
# new_node = html.new_tag('box')
# div_node.replace_with(new_node)  # 节点替换
# print(html)

# print(div_node.extract())  # 从节点树中删除
# print(a_node.unwrap())  # 去除标签，拆包
# new_node = html.new_tag('box')
# print(a_node.wrap(new_node))  # 包装
# print(html)

# new_node1 = html.new_tag('new1')
# new_node2 = html.new_tag('new2')
# # div_node.insert(0, new_node)  # 内部插入节点
# # div_node.append(new_node)  # 内部后插入节点
# # div_node.insert_before(new_node)  # 前面插入，兄弟节点
# # print(div_node.insert_after(new_node))  # 后面插入，兄弟节点
# # print(html)
# print(div_node.extend([new_node1, new_node2]))  # 内部插入多个节点
# print(html)

# 查找(深度优先)
# print(div_node.find_next())
# print(div_node.find_all_next('a'))
# print(div_node.find_previous())
# print(div_node.find_next_siblings('a'))  # 深度优先遍历，查找下一个兄弟节点
# print(div_node.find_previous_siblings('a'))  # 深度优先遍历，查找上一个兄弟节点
# print(div_node.next_siblings)  # 返回一个迭代器

# 深拷贝
# import copy
# new_node = copy.copy(div_node)
# print(id(div_node))
# print(id(new_node))

# 文档部分解析
html_strainer = SoupStrainer('div')
html = BeautifulSoup(html_str, features='lxml', parse_only=html_strainer)
print(html)  # 只生成部分文档树

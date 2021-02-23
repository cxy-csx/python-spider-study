from lxml import etree

# xml = etree.parse('test.xml')
# html = etree.HTML('test.html')
# print(xml)  # lxml.etree._ElementTree
# print(html)  # Element html

# Xpath语法
# / 子节点
# // 后代节点
# . 当前节点
# .. 上一个节点
# * 代表所有元素节点
# @ 属性
# node() 文本或元素节点
# text() 文本节点
# [] 过滤条件

html_str = """
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        <div class='box1'>
            <div class="left">左边</div>
            <div class="right">右边</div>
        </div>
        <div class='box2'>
            <div class="left">左边</div>
            <div class="right">右边</div>
        </div>
    </body>
    </html>
"""
# parse = etree.HTMLParser()  # 指定html解析器, 默认是xml解析器
# html = etree.parse('test.html', parser=parse)
html = etree.HTML(html_str)
# print(etree.tostring(html, encoding='UTF-8').decode('UTF-8'))

# html = html.xpath("/html")
# divs = html.xpath("//div")
# div = html.xpath("//div[@class='box1']")
# left_div_text = html.xpath("//div[@class='box1']/div")[0].xpath('./text()')  # 返回一个列表
# box2 = html.xpath("//div[@class='box1']/following-sibling::div")  # following-sibling::div 在box1后面的范围查找

# all_div_node = html.xpath("//div/*/@class")  # 获取属性值
divs_node = html.xpath("//div/*[last() -1]/@class")  # last()为xpath的内置函数
print(divs_node)


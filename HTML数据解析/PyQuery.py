from pyquery import PyQuery as PQ


html_str = """
<div>
    <a href='http://www.baidu.com'><img src='pic1.jpg'></img></a>
    <a href='http://www.baidu.com'><img src='pic2.jpg'></img></a>
    <a href='http://www.baidu.com'><img src='pic3.jpg'></img></a>
</div>
"""
pq = PQ(html_str)  # <class 'pyquery.pyquery.PyQuery'>
div = pq('div')
a = div.children('a')
first_a = a.eq(0)
all_a = pq.items('a')  # 返回一个生成器generator
# print(div)
# print(a)
# print(a.parent())
# print(first_a.siblings())

# pq('a').each(lambda i, ele: print(i, ele))  # 遍历
# print(pq('img').eq(0).attr('src'))


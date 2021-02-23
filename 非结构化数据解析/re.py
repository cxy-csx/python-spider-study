import re

str_ = 'I Love You China'

# 正则匹配规则
# . 除了'\n'以外的任意一个字符
# [] 中括号中任意一个字符
# [^] 除了中括号里的字符外任意一个字符
# 量词 * 任意次，可以是0次 *?: 代表非贪婪模式
# 量词 + 1次 或 多次
# 量词 ? 0次 或 1次 \d?: 代表可以是0次或1次，默认是贪婪模式
# 边界处理 $ 结尾处
# 边界处理 ^ 起始处
# 单词边界 \b
# 转义字符 正则规则会经过两层转换, 第一层是普通字符的转换， 第二层是正则层面的一层转换
# \num \1 与第一个分组, 值相同

# res = re.match('I', str_)  # 从左到右进行匹配，如果匹配不到则停止检索
# print(res.group())  # 返回匹配到的结果
# print(re.match('.', "\n"))  # None
# print(re.match('[ab]', ''))
# print(re.match('[^ab]', 'b'))  # None

# print(re.match("\d{11}", '15018707754'))  # 匹配11个数字

# print(re.match('\\\d', '\d'))  # 正则匹配的是未转义后的字符串, 即匹配\d

# 日期匹配
# 2021-02-23
# res = re.match('\d{4}-(0\d|1[12])-([012]\d|3[01])', '2021-12-23')
# print(res.group(0))
# print(res.group(1))
# print(res.group(2))
# print(res.groups())  # 返回一个元组
# print(res.start())  # 匹配到的字符串的开始位置
# print(res.end())  # 匹配到的字符串的结束位置
# print(res.string)  # 匹配到的字符串

# 标签
# html_str = "<div>hello world</div>"
# # res = re.match('<\w+>(.*)</\w+>', html_str)
# res = re.match(r'<(\w+)>([\w\W]*)</\1>', html_str)  # \1代表与\w值一样
# res = re.match(r'<(?P<tag_name>\w+)>([\w\W]*)</(?P=tag_name)>', html_str)  # 给分组取别名

# re.search 从左往右检索，匹配到则停止。
# res = re.findall('.', str_)  # 从左往右检索，找到所有符合的字符串，返回一个列表

# re.compile
# str_ = 'hello python'
# # 对正则表达式先编译, 编译一次, 可以多次调用
# rc = re.compile('\w{2}', flags=re.I)  # re.I忽略大小写
# res = rc.match('he')
# print(res)

# re.split 正则分割
# str_ = '2021-02/23'
# res = re.split('/|-', str_)
# print(res)

# re.sub 正则替换
# str_ = '2021/02/23'
# res = re.sub('/', '-', str_)
# res = re.subn('/', '-', str_)  # subn 返回替换后的结果以及替换的次数
# print(res)
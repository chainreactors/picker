---
title: 如何利用AI大模型辅助漏洞挖掘
url: https://forum.butian.net/share/4378
source: 奇安信攻防社区
date: 2025-06-10
fetch_date: 2025-10-06T22:47:49.270233
---

# 如何利用AI大模型辅助漏洞挖掘

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 如何利用AI大模型辅助漏洞挖掘

* [安全工具](https://forum.butian.net/topic/53)

本文从php为切入点，详细讲了自己在设计一款半自动化开源审计工具时候的调研思路和开发过程

传统审计
----
### 正则匹配
原理就是通过正则匹配来实现,挨个进行正则匹配，比如这条:
```xml
<rule name="读取文件函数中存在变量，可能存在任意文件读取漏洞">
<regmatch>
<regexp>
(file\_get\_contents|fopen|readfile|fgets|fread|parse\_ini\_file|highlight\_file|fgetss|show\_source)\s{0,5}\(.{0,40}\$\w{1,15}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}
</regexp>
</regmatch>
</rule>
```
就是匹配高危函数后是否带有`$`的字符，也就是变量俩判断有无潜在的漏洞，上古时代的神器Seay就有很多这样的规则:
```xml
<root>
<phpid vultype="File Inclusion">
<function>
<rule name="文件包含函数中存在变量,可能存在文件包含漏洞">
<regmatch>
<regexp>(include|require)(\_once){0,1}(\s{1,5}|\s{0,5}\().{0,60}\$(?!.\*(this-&gt;))\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}</regexp>
</regmatch>
</rule>
<rule name="读取文件函数中存在变量，可能存在任意文件读取漏洞">
<regmatch>
<regexp>(file\_get\_contents|fopen|readfile|fgets|fread|parse\_ini\_file|highlight\_file|fgetss|show\_source)\s{0,5}\(.{0,40}\$\w{1,15}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}</regexp>
</regmatch>
</rule>
</function>
</phpid>
<phpid vultype="EXEC">
<function>
<rule name="preg\_replace的/e模式，且有可控变量，可能存在代码执行漏洞">
<regmatch>
<regexp>preg\_replace\(\s{0,5}.\*/[is]{0,2}e[is]{0,2}["']\s{0,5},(.\*\$.\*,|.\*,.\*\$)</regexp>
</regmatch>
</rule>
<rule name="call\_user\_func函数参数包含变量，可能存在代码执行漏洞">
<regmatch>
<regexp>call\_user\_func(\_array){0,1}\(\s{0,5}\$\w{1,15}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}</regexp>
</regmatch>
</rule>
<rule name="命令执行函数中存在变量，可能存在任意命令执行漏洞">
<regmatch>
<regexp>(system|passthru|pcntl\_exec|shell\_exec|escapeshellcmd|exec)\s{0,10}\(.{0,40}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}</regexp>
</regmatch>
</rule>
<rule name="可能存在代码执行漏洞,或者此处是后门">
<regmatch>
<regexp>\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}\s{0,5}\(\s{0,5}\$\_(POST|GET|REQUEST|SERVER)\[.{1,20}\]</regexp>
</regmatch>
</rule>
<rule name="``反引号中包含变量，变量可控会导致命令执行漏洞">
<regmatch>
<regexp>`\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}`</regexp>
</regmatch>
</rule>
<rule name="array\_map参数包含变量，变量可控可能会导致代码执行漏洞">
<regmatch>
<regexp>array\_map\s{0,4}\(\s{0,4}.{0,20}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}\s{0,4}.{0,20},</regexp>
</regmatch>
</rule>
<rule name="eval或者assertc函数中存在变量，可能存在代码执行漏洞">
<regmatch>
<regexp>(eval|assert)\s{0,10}\(.{0,60}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}</regexp>
</regmatch>
</rule>
</function>
</phpid>
<phpid vultype="Information Disclosure">
<function>
<rule name="phpinfo()函数，可能存在敏感信息泄露漏洞">
<regmatch>
<regexp>phpinfo\s{0,5}\(\s{0,5}\)</regexp>
</regmatch>
</rule>
</function>
</phpid>
<phpid vultype="Parameter Injection">
<function>
<rule name="parse\_str函数中存在变量,可能存在变量覆盖漏洞">
<regmatch>
<regexp>(mb\_){0,1}parse\_str\s{0,10}\(.{0,40}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}</regexp>
</regmatch>
</rule>
<rule name="双$符号可能存在变量覆盖漏洞">
<regmatch>
<regexp>\${{0,1}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}\s{0,4}=\s{0,4}.{0,20}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}</regexp>
</regmatch>
</rule>
<rule name="extract函数中存在变量，可能存在变量覆盖漏洞">
<regmatch>
<regexp>(extract)\s{0,5}\(.{0,30}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}\s{0,5},{0,1}\s{0,5}(EXTR\_OVERWRITE){0,1}\s{0,5}\)</regexp>
</regmatch>
</rule>
</function>
</phpid>
<phpid vultype="Other">
<function>
<rule name="获取IP地址方式可伪造，HTTP\_REFERER可伪造，常见引发SQL注入等漏洞">
<regmatch>
<regexp>["'](HTTP\_CLIENT\_IP|HTTP\_X\_FORWARDED\_FOR|HTTP\_REFERER)["']</regexp>
</regmatch>
</rule>
<rule name="文件操作函数中存在变量，可能存在任意文件读取/删除/修改/写入等漏洞">
<regmatch>
<regexp>(unlink|copy|fwrite|file\_put\_contents|bzopen)\s{0,10}\(.{0,40}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}</regexp>
</regmatch>
</rule>
<rule name="urldecode绕过GPC,stripslashes会取消GPC转义字符">
<regmatch>
<regexp>^(?!.\*\baddslashes).{0,40}\b((raw){0,1}urldecode|stripslashes)\s{0,5}\(.{0,60}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}</regexp>
</regmatch>
</rule>
<rule name="header函数或者js location有可控参数，存在任意跳转或http头污染漏洞">
<regmatch>
<regexp>(header\s{0,5}\(.{0,30}|window.location.href\s{0,5}=\s{0,5})\$\_(POST|GET|REQUEST|SERVER)</regexp>
</regmatch>
</rule>
<rule name="存在文件上传，注意上传类型是否可控">
<regmatch>
<regexp>move\_uploaded\_file\s{0,5}\(</regexp>
</regmatch>
</rule>
</function>
</phpid>
<phpid vultype="SQLi">
<function>
<rule name="SQL语句select中条件变量无单引号保护，可能存在SQL注入漏洞">
<regmatch>
<regexp>select\s{1,4}.{1,60}from.{1,50}\bwhere\s{1,3}.{1,50}=["\s\.]{0,10}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}</regexp>
</regmatch>
</rule>
<rule name="SQL语句delete中条件变量无单引号保护，可能存在SQL注入漏洞">
<regmatch>
<regexp>delete\s{1,4}from.{1,20}\bwhere\s{1,3}.{1,30}=["\s\.]{0,10}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}</regexp>
</regmatch>
</rule>
<rule name="SQL语句insert中插入变量无单引号保护，可能存在SQL注入漏洞">
<regmatch>
<regexp>insert\s{1,5}into\s{1,5}.{1,60}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}</regexp>
</regmatch>
</rule>
<rule name="SQL语句delete中条件变量无单引号保护，可能存在SQL注入漏洞">
<regmatch>
<regexp>update\s{1,4}.{1,30}\s{1,3}set\s{1,5}.{1,60}\$\w{1,20}((\[["']|\[)\${0,1}[\w\[\]"']{0,30}){0,1}</regexp>
</regmatch>
</rule>
</function>
</phpid>
<phpid vultype="XSS">
<function>
<rule name="echo等输出中存在可控变量，可能存在XSS漏洞">
<regmatch>
<regexp>(echo|print|print\_r)\s{0,5}\({0,1}.{0,60}\$\_(POST|GET|REQUEST|SERVER)</regexp>
</regmatch>
</rule>
</function>
</phpid>
</root>
```
然后去匹配:
```py
# coding=utf-8
'''
by：Segador
Improved by: 7ech\_N3rd
'''
import re
import os
import optparse
import sys
import chardet
import json
from lxml.html import etree
class phpid(object):
def \_\_init\_\_(self, dir):
self.\_function = ''
self.\_fpanttern = ''
self.\_line = ''
self.\_dir = dir
self.\_filename = ''
self.\_vultype = ''
self.choice = '1'
self.results = [] # 用于存储匹配结果
def \_run(self):
try:
self.handlePath(self.\_dir)
# print("danger information Finished!")
# 输出结果为 JSON 格式
print(json.dumps(self.results, indent=4, ensure\_ascii=True))
except Exception as e:
print(f"Error: {e}")
raise
def report\_id(self, vul,matches):
message = {
"vulnerability": vul,
"function": self.\_function,
"file": self.\_filename,
"matches": matches
}
self.results.append(message)
def report\_line(self, line\_content):
# 将匹配的行号和内容添加到最后一个 result 中
if self.results:
self.results[-1]["matches"].append({
"line": self.\_line,
"content": line\_content.strip()
})
def handlePath(self, path):
dirs = os.listdir(path)
for d in dirs:
subpath = os.path.join(path, d)
if os.path.isfile(subpath):
if os.path.splitext(subpath)[1] in ['.php','.phtml']:
self.\_filename = subpath
file = "regexp"
self.handleFile(subpath, file)
else:
self.handlePath(subpath)
def handleFile(self, fileName, file):
with open(fileName, 'rb') as f: # 以二进制模式打开
raw\_data = f.read()
result = chardet.detect(raw\_data) # 检测编码
encoding = result['encoding']
# 使用检测到的编码读取文件
with open(fileName, 'r', encoding=encoding, errors='ignore') as f:
self.\_line = 0
content = f.read()
content = self.remove\_comment(content)
self.check\_regexp(content, file)
def function\_search\_line(self):
with open(self.\_filename, 'r', encoding='utf-8', errors='ignore') as fl:
self.\_line = 0
while True:
line = fl.readline()
if not line:
break
self.\_line += 1
# 调试输出：查看每一行是否包含函数名
# print(f"Checking line {self.\_line}: {line.strip()}")
if self.\_function in line:
# print(f'find danger information on line: {line.strip()}')
self.report\_line(line.strip())
def regexp\_search(s...
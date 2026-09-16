---
title: 网安入门必学：基础不牢，漏洞白学
url: https://mp.weixin.qq.com/s/hQphKssKvTZ0q3G2mrny8A
source: Doonsec's feed
date: 2026-09-15
fetch_date: 2026-09-16T07:00:43.782546
---

# 网安入门必学：基础不牢，漏洞白学

# 网安入门必学：基础不牢，漏洞白学

原创

龙哥
龙哥

龙哥网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

很多刚入坑网络安全的新手，一上来就死磕漏洞、疯狂装工具，却忽略了最底层的系统操作。敲命令报错、写 SQL 语句翻车，做信息收集的时候处处踩坑，大量时间白白浪费。

其实漏洞原理本身并不复杂，真正卡住人的，是操作系统、数据库、网络基础没有学扎实。今天整理一份网安入门核心基础笔记，从系统操作到 Web 安全前置知识，适合新手打基础。

## 一、Windows 系统基础

Windows 是我们日常最熟悉的系统，在内网安全排查、渗透场景里，它的基础知识点非常关键。

**1. 核心目录说明**

Program Files 用来存放 64 位软件；Program Files (x86) 存放 32 位程序。Windows 文件夹是系统核心目录；用户目录则保存每个账号的桌面、文档等个人文件。

**2. 开机自启项**

按下 win+r，输入 shell:startup 回车，就能直接打开开机启动文件夹。只需要把程序快捷方式放入文件夹，程序就会开机自动运行。排查恶意程序时，这个路径是重点检查位置。

**3. 基础查询与共享**

查看本机 IP 地址，终端输入 ipconfig。

文件开启共享：右键文件→属性→共享，添加 everyone 访问权限。访问其他主机共享文件夹格式为 \IP 地址 \ 共享目录，需要账号密码完成验证。

**4. 注册表**

regedit 命令打开注册表。它相当于 Windows 的核心数据库，管控系统启动、硬件驱动、软件配置。恶意程序常常修改注册表，实现程序持久化驻留。

## 二、Linux 系统常用命令

Linux 是服务器主流操作系统，做网安学习，文件操作命令是基本功，需要熟练掌握。

**1. 远程连接与开关机**远程登录服务器命令：ssh 用户名 @IP，示例 ssh root@192.168.61.131；exit 退出远程连接。

重启：reboot；立刻关机：shutdown -h now。

**2. 文件目录基础操作**

* 创建文件：touch，支持批量创建文件
* 查看目录内容：ls，-a 查看隐藏文件，-l 展示文件详细权限信息
* 移动 / 重命名：mv。目标不存在时为重命名；目标存在，则移动文件到目标目录
* 复制文件：cp，-r 参数专门用来复制文件夹
* 删除文件：rm，Linux 没有回收站，删除数据无法恢复。-f 强制删除，-r 用来删除文件夹，常用组合 rm -rf
* 创建文件夹：mkdir，支持批量创建目录

##

## 三、MySQL 数据库基础

绝大多数 Web 业务都依赖数据库，SQL 注入漏洞本质就是可控的数据库语句。想要看懂注入原理，数据库基础必须吃透。

**1. CentOS7 环境安装**CentOS7 系统默认自带 MariaDB，配置 yum 源后，执行 yum install mariadb-server -y 完成安装。启动服务并且设置开机自启，安装结束执行 mysql\_secure\_installation 完成安全初始化。

**2. 账号授权管理**默认情况下 root 账号不允许远程连接。

授权基础语法：grant 权限 on 库名。表名 to 用户 @地址 identified by ' 密码'

可以单独创建用户、分配权限，也可以回收用户权限；show grants for 用户可以查看账号拥有的权限。

**3. 登录与密码修改**远程登录命令：mysql -u 用户名 -p 密码 -h 目标 IP。

修改密码，既可以使用安全初始化工具，也能在数据库内部执行 set password 语句修改。

**4. 数据类型与 PHP 交互**常用数据类型：int 整型、float 浮点、char 定长字符串、text 长文本、enum 枚举、date 日期。

整型包含 TINYINT、SMALLINT、MEDIUMINT、INT、BIGINT，占用存储空间依次增大。

PHP 可以连接 MySQL，完成建库、建表、插入、查询数据操作，这也是网站和数据库交互的底层逻辑，SQL 注入就发生在这个交互环节。

## 四、网络基础与信息收集

**1. 常见服务端口**HTTP 80、HTTPS 443、DNS 53、SMB 445、Telnet 23、FTP 20/21。端口扫描时，这些是最先识别的高频服务端口。

**2. 域名信息收集**信息收集是渗透测试的第一步。Whois 查询可以获取域名注册信息；在线子域名工具能够批量挖掘子域名，扩大目标资产范围。

## 五、Web 安全前置知识点

**1. SQL 注入基础**SQL 注释符号是注入的核心，#、-- 可以截断后面的 SQL 语句。GET 请求中 -- 后的空格需要 URL 编码；POST 表单注入场景，可以直接使用 #。

单引号、双引号是基础注入点测试 Payload，用来闭合原有 SQL 语句，构造 or 1=1 这类判断语句，验证注入漏洞。

**2. PHP 序列化与反序列化**序列化，就是把对象转为字符串，方便存储传输；反序列化是将字符串还原为对象。

如果反序列化的参数可控，攻击者可以构造恶意序列化字符串，触发类里面的魔术方法，执行恶意代码，也就是反序列化漏洞。

## 六、环境搭建补充

Docker 能够快速搭建各类漏洞练习环境。文档内附带 ARL 资产侦察灯塔一键部署脚本，适合本地搭建练习环境，用来练习资产收集。

## 最后总结

网络安全学习，千万不要跳过基础直接去刷漏洞。Windows 注册表、Linux 基础命令、MySQL 账号权限、域名信息收集、SQL 基础，全部都是 Web 漏洞学习的地基。

搞懂系统如何读写文件、数据库怎么执行语句、网站如何和数据库交互，你才能真正理解 SQL 注入、反序列化这类漏洞的形成原理。基础打扎实之后，再去学习漏洞利用、工具使用，上手速度会快很多。

**网络安全学习包**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/TiaI8Dth4IiaRCFva2ZibMZKuNBEDOAEmkUGiakynth3MRTicLcHaV4MAvjubiaIicUx4ZrMxuSdSicjzT5HfEAzJy782g/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=7)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/TiaI8Dth4IiaRCFva2ZibMZKuNBEDOAEmkU7VZiaRU6vdoIQC9ToNyrFNvkWmp92gn3R2RWyGVEiaxjTlDjic3dPsW6g/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=8)

**资料目录**

1. 成长路线图&学习规划
2. 配套视频教程
3. SRC&黑客文籍
4. 护网行动资料
5. 黑客必读书单
6. 面试题合集

   **282G**《**网络安全/黑客技术入门学习大礼包**》，可以**扫描下方二维码免费领取**！

   ![图片](https://mmbiz.qpic.cn/mmbiz_jpg/8cylv3yeUGb0ZAoUNnyIKQ2VxuxLbspBfcKnwUvCnPuTg7ZYNlu0ssI3bBMfSDBIcicvib0NBdTdhsdaGuLVfj0ZZ3t2ib3sic4icMUK5V7B9ibbg/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

   1.成长路线图&学习规划

   要学习一门新的技术，作为新手一定要**先学习成长路线图**，**方向不对，努力白费**。

   对于从来没有接触过网络安全的同学，我们帮你准备了详细的学习成长路线图&学习规划。可以说是最科学最系统的学习路线，大家跟着这个大的方向学习准没问题。

   ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/71ibgGpZLr2W93cZWq7t2hVfaCvicInAznWcibcMdSKWsxbRn4qOUH3FiapXR7WicIiaRXx4lp8bNDnKTndzOPmKjERg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=10)

   ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/evTLxnBbHv6fa8BCJ5052WLSGZjTIfEDgymVV6FeniaFszgpka15xzMolFmtXDdiaaDJMwXSqTQgRgBicvbYv4tNw/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=11)

   2.视频教程

   很多朋友都不喜欢**晦涩的文字**，我也为大家准备了视频教程，其中一共有**21个章节**，每个章节都是**当前板块的精华浓缩**。

   ![图片](https://mmbiz.qpic.cn/mmbiz_png/NAkrkExZ3dnMVja8hzZpia0AkKu6AWrQn8E3Yp6lXhRo3D1Bttpiao3a0poRH29MC1MBC0hk5gKMCiaicy3wOiaUviag/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=12)

   ![图片](https://mmbiz.qpic.cn/mmbiz_png/NAkrkExZ3dnMVja8hzZpia0AkKu6AWrQnHBEMEd0W8dr6zFFQetPOhwiax5u8YYm0YZtWJSmyJ7d85QmuVQEicLVQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=13)

   3.SRC&黑客文籍

   大家最喜欢也是最关心的**SRC技术文籍&黑客技术**也有收录

   **SRC技术文籍：**

   ![图片](https://mmbiz.qpic.cn/mmbiz_png/NAkrkExZ3dkY8ctWgyFKc2oWZY3ibCDm5lMpjofvtGCicHTLibsOF8b841UOfozGsdjDvJKiaFgibdTunKlgC9kzrTQ/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=14)

   **黑客资料由于是敏感资源，这里不能直接展示哦！**

   4.护网行动资料

   其中关于**HW护网行动，也准备了对应的资料，这些内容可相当于比赛的金手指！**

   ![图片](https://mmbiz.qpic.cn/mmbiz_png/NAkrkExZ3dnMVja8hzZpia0AkKu6AWrQnaPKJSI9dNKiaR4vaJf0hqApKNbJeZnCpsQSElEicDrlAMLkRXHoyKN8A/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=15)

   5.黑客必读书单

   **![图片](https://mmbiz.qpic.cn/mmbiz_jpg/UK2533DyHVnfYtD0I7BeGkCGDKyhAWVrH5kVnnjmBtUJsEgfOIxkutcoVnJZDhibib7JqPQ3BEZWw06QZ3O1mc8Q/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=16)**

   6.面试题合集

   当你自学到这里，你就要开始**思考找工作**的事情了，而工作绕不开的就是**真题和面试题。**

   ![图片](https://mmbiz.qpic.cn/mmbiz_png/NAkrkExZ3dnMVja8hzZpia0AkKu6AWrQnXxPNhSSySbwUMEWOicYYS62D1UOQExv0cYuVQ68gk2uFF2xJ4TPmRHA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=17)

   **更多内容为防止和谐，可以扫描获取~**

   ![图片](https://mmbiz.qpic.cn/mmbiz_png/NAkrkExZ3dnMVja8hzZpia0AkKu6AWrQnGktIUCicPreibR6b3sx1Qu0CsCZP0sZtCP4RHlMdxXuE4icCFSoL2yyBg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=18)

   朋友们需要全套共**282G**的《**网络安全/黑客技术入门学习大礼包**》，可以**扫描下方二维码免费领取**！

   ![图片](https://mmbiz.qpic.cn/mmbiz_jpg/8cylv3yeUGb0ZAoUNnyIKQ2VxuxLbspBfcKnwUvCnPuTg7ZYNlu0ssI3bBMfSDBIcicvib0NBdTdhsdaGuLVfj0ZZ3t2ib3sic4icMUK5V7B9ibbg/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=13)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7O8nPRxfRT7NHG7rzgsoLIZoUNftOgFkUvw7cg5pYj1cC5HG9Au30Xd3tbUySlm1gsrt7B2sehicBlb3mFmNLFw/0?wx_fmt=png)

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
---
title: Win10资源管理器的文件搜索
url: http://blog.nsfocus.net/win10/
source: 绿盟科技技术博客
date: 2023-03-29
fetch_date: 2025-10-04T11:01:04.739653
---

# Win10资源管理器的文件搜索

* [登录](http://blog.nsfocus.net/wp-login.php)
* [注册](http://blog.nsfocus.net/wp-login.php?action=register)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

[![Logo](http://blog.nsfocus.net/wp-content/uploads/2020/07/blog-logo.png)](https://blog.nsfocus.net/)

* [技术产品](https://blog.nsfocus.net/category/technology-product/)
* [数智安全](https://blog.nsfocus.net/category/digital-intelligence-secuirty/)
* [威胁通告](https://blog.nsfocus.net/category/threat-alert/)
* [研究调研](https://blog.nsfocus.net/category/security-research/)
* [洞见RSA](https://blog.nsfocus.net/category/rsac/)
* [公益译文](https://blog.nsfocus.net/category/translation/)
* [安全分享](https://blog.nsfocus.net/category/security-sharing/)

# Win10资源管理器的文件搜索

### Win10资源管理器的文件搜索

[2023-03-28](https://blog.nsfocus.net/win10/ "Win10资源管理器的文件搜索")[scz](https://blog.nsfocus.net/author/scz/ "View all posts by scz")

阅读： 1,254

Q:Win10资源管理器菜单栏一般有「文件、主页、共享、查看」这几项，而其他项并不固定，试举几例

选中 | 菜单栏
—–+——————
盘符 |「管理-驱动器工具」
图片 |「管理-图片工具」
EXE |「管理-应用程序工具」
音频 |「播放-音乐工具」
视频 |「播放-视频工具」

在Win10资源管理器中进行文件搜索后，无论是否找到匹配文件，菜单栏将出现「管理-搜索工具」，此时可对「修改日期、类型、大小、其他属性」进行有限过滤，但非完全可控的过滤机制；在「最近的搜索内容」中有「清除搜索历史记录」。

为了调出「搜索工具」，最简方案是对一个空目录随便搜个不存在的文件，搜索将快速结束，同时「搜索工具」出现在菜单栏上。但这样做意义不大，一旦切换目录，「搜索工具」又会消失。

我的问题是，有没有注册表、组策略，让「搜索工具」始终出现在菜单栏上，而非搜索发生后动态出现。

D: scz 2023-03-24

LTSB版本Win10只要点击”搜索框”，无须实际搜索，菜单栏就会出现「搜索工具」，
此行为与非LTSB版本不同。英文版与中文版的显示内容可能有细微差别。没有注册表、
组策略设置使得「搜索工具」永久固定。

Q:如何搜索大于50KB小于100KB的pyc文件？

A: scz 2023-03-25

在资源管理器搜索框中输入

\*.pyc size:>50KB<100KB // 英文版
\*.pyc size:50KB..100KB

\*.pyc 大小:>50KB<100KB // 中文版
\*.pyc 大小:50KB..100KB

此处中英文版关键字无法混用。用”..”方式时，我未实测是闭区间还是其他什么。

另有命令行方案，下列命令以当前目录为根，搜索大于等于50KB、小于等于100KB的pyc文件，显示其绝对路径与大小

forfiles /p . /s /m \*.pyc /c “cmd /c if @fsize geq 51200 if @fsize leq 102400 echo @path @fsize”cmd的多个if命令之间是逻辑与的关系，逻辑或只能用if/else if/else变相实现。

Q:如何搜索最后修改时间位于2023/3/1之后大于50KB小于100KB的pyc文件？

A: scz在资源管理器搜索框中输入

\*.pyc datemodified:>=3/1/2023 size:>50KB<100KB // 英文版
\*.pyc datemodified:>=3/1/2023 size:50KB..100KB

\*.pyc 修改日期:>=2023/3/1 大小:>50KB<100KB // 中文版
\*.pyc 修改日期:>=2023/3/1 大小:50KB..100KB

时间格式需用当前系统设定格式，对应”date /t”看到的格式，上面只是示例。

命令行方案

forfiles /p . /s /m \*.pyc /d +2023/3/1 /c “cmd /c if @fsize geq 51200 if @fsize leq 102400 echo @path @fsize @fdate @ftime”

“/d -2023/3/1″表示最后修改时间位于2023/3/1之前

Q:如何搜索最后修改时间位于2023/3/1与2023/3/25之间大于50KB小于100KB的pyc文件？

A: scz

在资源管理器搜索框中输入

\*.pyc datemodified:>=3/1/2023<=3/25/2023 size:>50KB<100KB // 英文版
\*.pyc datemodified:>=3/1/2023..3/25/2023 size:50KB..100KB

\*.pyc 修改日期:>=2023/3/1<=2023/3/25 大小:>50KB<100KB // 中文版
\*.pyc 修改日期:>=2023/3/1..2023/3/25 大小:50KB..100KB

该需求无法用forfiles实现，/d只允许用一次，@fdate无法进行比较操作。

可用PowerShell脚本达此目的

Get-ChildItem -Path “.” -Recurse -Filter “\*.pyc” | Where-Object { $\_.LastWriteTime -ge ‘2023-03-01’ -and $\_.LastWriteTime -le ‘2023-03-25’ -and $\_.Length -gt 51200 -and $\_.Length -lt 102400 } | Select-Object -Property FullName, Length, LastWriteTime | Format-List \*

PowerShell太重型了，forfiles也好不到哪去，DOS批处理或许也可以，但更重型，还是GUI搜索框相对直观，过去XP的搜索界面更直观。

**版权声明**
本站“技术博客”所有内容的版权持有者为绿盟科技集团股份有限公司（“绿盟科技”）。作为分享技术资讯的平台，绿盟科技期待与广大用户互动交流，并欢迎在标明出处（绿盟科技-技术博客）及网址的情形下，全文转发。
上述情形之外的任何使用形式，均需提前向绿盟科技（010-68438880-5462）申请版权授权。如擅自使用，绿盟科技保留追责权利。同时，如因擅自使用博客内容引发法律纠纷，由使用者自行承担全部法律责任，与绿盟科技无关。

Spread the word. Share this post!

[Previous](https://blog.nsfocus.net/5g/)

[Next](https://blog.nsfocus.net/open-world-anomaly-detection/)

### Meet The Author

scz

C/ASM程序员

咨询与合作：nsmagazine@nsfocus.com

* [绿盟科技官网](https://www.nsfocus.com.cn)
* [绿盟威胁情报中心（NTI）](https://nti.nsfocus.com)
* [绿盟云](https://cloud.nsfocus.com)
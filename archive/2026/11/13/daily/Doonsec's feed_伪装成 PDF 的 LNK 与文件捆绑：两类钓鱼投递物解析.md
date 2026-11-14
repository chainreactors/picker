---
title: 伪装成 PDF 的 LNK 与文件捆绑：两类钓鱼投递物解析
url: https://mp.weixin.qq.com/s/ehI8A7etPg423Yy6SriDiw
source: Doonsec's feed
date: 2026-11-13
fetch_date: 2026-11-14T08:13:39.435992
---

# 伪装成 PDF 的 LNK 与文件捆绑：两类钓鱼投递物解析

# 伪装成 PDF 的 LNK 与文件捆绑：两类钓鱼投递物解析

原创

One
One

One security

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

一、伪装成 PDF 的 LNK 快捷方式

▍核心思路

Windows 默认隐藏已知文件扩展名，因此 `发票.pdf.lnk` 在资源管理器中显示为 `发票.pdf`。双击后实际执行：

C:\Windows\explorer.exe ".\data\data\data\data\open.vbs"

由资源管理器按相对路径加载隐藏目录中的载荷。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pqOYI94QTU6yqskxaZ7TnSBibZicxn5FYnhBqEzv4qPRn9F1bpgibTtuXkIBOhNZ53iaUlUgjpUX4qB5QBHxYD4Mvof85ONhZuJJAT2VoEibyAxs/640?wx_fmt=png&from=appmsg)

▍关键实现

* **目标伪装：**

  目标设为 explorer.exe，参数使用相对路径，整个目录可整体迁移。
* **隐藏目录：**

  载荷放入多层同名目录并设置隐藏属性，资源管理器默认不可见。
* **结构修补：**

  插入 Shell Item ID List，并修正 LinkInfo 与 UNC 偏移字段。
* **隐藏窗口：**

  改写 Shell Link Header 的 ShowCommand 为 SW\_HIDE，执行时不弹窗。

▍使用方法

pip install pylnk3

python lnkgen\_gui.py

必填项：文件名、目标文件、目录名、嵌套层数、输出目录；可选图标文件与额外部署文件。

▍生成结构

output\ ├── 发票.pdf.lnk          ← 可见 └── data\data\data\data\     └── open.vbs         ← 实际执行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pqOYI94QTU5u4DabQHEU52XxO6ic93xqRrgbiaWoWiaJqlW5BI7GoETUL08XN435fOFqFJzG6Hpric7v7kjuNtV3ysHLoeEjOf1NsEz3JwO27oM/640?wx_fmt=png&from=appmsg)

注意：图标留空时跟随目标文件的关联图标。目标为 .vbs 时需手动指定 PDF 图标，否则显示脚本图标。

二、文件捆绑生成器

▍核心思路

将多个文件以 base64 内嵌进解包脚本，由 PyInstaller 打包为单文件 exe，图标取系统 PDF 关联图标。运行时释放到 %TEMP% 并逐个执行：exe/bat 以隐藏窗口启动，其余调用 os.startfile。

▍使用方法

pip install pylnk3

pyinstaller python binder\_gui.py

binder\_gui.py 依赖同目录的 lnkgen.py。填写产物名、添加文件、选择输出目录后生成，打包约需 1~2 分钟；打包与图标提取依赖 Windows。

产物扩展名为 .exe，伪装依赖“隐藏已知扩展名”与 PDF 图标，本质是一个自解压执行体。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pqOYI94QTU4FV1mDrp2ljs5icF1KzcH3eyic2lMYlqkqibXMVOiakUrCnXnIAhx6ZlKSVicysjpbqILA9JErATtCVicEIQLicBvJweEANgDvHhFx28/640?wx_fmt=png&from=appmsg)

需要的师傅可进入交流群

![](https://mmbiz.qpic.cn/sz_mmbiz_png/pqOYI94QTU4ukADmZRPtxl9JnssVXkaNmOk2WlbHQScectRU4JZeesJl9Qicnw9GVQCXgIAOZMRiaZXpicvIpRyoIdkEZr0je7pzWv3e8Y5ggc/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/xuE8qjs4aGLhPiaZZFjhwrkicyMfPgaPqTJqicELsaBWEFNtZ0msbo3pLcMFH9Hurd3pqiaMHJ2HQJmjEnBT7kicSRg/0?wx_fmt=png)

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
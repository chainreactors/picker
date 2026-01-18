---
title: ctftools-all-in-oneV8.7研发进度
url: https://mp.weixin.qq.com/s/7J3ZzhRdBFUNOQFPRwQp9A
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:37:57.101429
---

# ctftools-all-in-oneV8.7研发进度

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kiaoFVP7GOX2ROaAZqejbTibeToHSiczBNh1pCO7sskmR7r0HZn4PkxiaOMY0T2gsOt5CU52hTUkEOgfeiaWeW8SuvA/0?wx_fmt=jpeg)

# ctftools-all-in-oneV8.7研发进度

原创

teacher李
teacher李

由由学习吧

![]()

在小说阅读器中沉浸阅读

ctftools-all-in-one之后的版本将在VIP群里面进行发布，可以通过贡献代码或者赞助加群，群内会定时更新最新版本，如果需要赞助获取最新版本的软件请联系qq:841350625

演示视频b站：T\_N\_T\_liyou

（1）拖入文件框中的内容能够自动替换，不用再手动删除之前的内容再拖入文件了

（2）更新新的机器码和认证方式（避免虚拟机问题）

（3）修复时间戳计算bug

（4）加入LM和ollama的api接入接口（理论上符合这两种规范的模型均能接入）

（5）优化fun call的调用方式

（6）pwn一把梭已汉化并更新到最新版本（需wsl的pwn环境，具体可以参照群文件wsl配置教程，可能需要合理上网）

（7）加解密模块加入base100

（8）终端功能完善：终端高DPI显示，并且选择文字使用ctrl+c为复制，不选中时候为中断，ctrl+v直接粘贴

（9）加入代码审计功能可以审计php、jsp、asp等webshell

另外正在研发的新工具：

替代IDA的反汇编工具（可以做逆向和pwn题目，无需多余切换）详见下面的视频

替代010edit和winhex的工具

加入编码切换

![](https://mmbiz.qpic.cn/mmbiz_png/kiaoFVP7GOX2ROaAZqejbTibeToHSiczBNhYMTzBFwFezPllz0fNh4CGCDezca9PaIZPMvLRF4XS8YkjxhbRQslsg/640?wx_fmt=png&from=appmsg)

高亮文件头（支持bt脚本）

![](https://mmbiz.qpic.cn/mmbiz_png/kiaoFVP7GOX2ROaAZqejbTibeToHSiczBNhiaQuEwwibPZCjN99b96fuj16fJYaBrSeic1RK7excVHia7oBS4QibIvw6Kg/640?wx_fmt=png&from=appmsg)

核心功能

1. 文件操作

- 文件加载：支持任意大小文件的加载，大文件采用流式读取

- 文件保存：支持保存修改后的文件

- 拖拽支持：可直接拖拽文件到窗口打开

2. 16进制编辑

- 16进制显示：以表格形式显示文件的16进制内容

- 文本显示：右侧显示对应的ASCII文本

- 编辑功能：支持直接编辑16进制值和ASCII字符

- 撤销/重做：完整的编辑历史管理

3. 搜索功能

- 16进制搜索：支持搜索16进制字节序列

- 文本搜索：支持搜索ASCII字符串

- 正则表达式搜索：支持模式匹配搜索

- 多线程搜索：大文件搜索不阻塞界面

4. 文件格式识别

- 魔数识别：通过文件头识别常见文件格式

- 扩展名识别：结合文件扩展名进行识别

- 支持格式：PNG、JPEG、ZIP、EXE、PDF等

5. BT模板高亮

- 010 Editor兼容：支持解析010 Editor的BT模板文件

- 结构化高亮：根据模板自动高亮显示文件结构

- 智能颜色：根据字段类型自动分配颜色

- 内置模板：包含PNG、JPEG、ZIP、PE等常见格式模板

6. 预览功能

- 文件预览：侧边栏显示文件内容的可视化预览

- 快速导航：点击预览栏可快速跳转到对应位置

- 位置指示：显示当前查看位置和可见范围

7. 界面特性

- 多标签页：支持同时打开多个文件

- 状态栏：显示文件信息、当前位置、选中内容等

- 工具栏：常用操作快捷按钮

- 右键菜单：复制、粘贴、撤销等操作

8. 高级功能

- 数据解析：支持多种数据类型的解析显示

- 字节序转换：支持大端/小端字节序

- 编码支持：支持多种字符编码

- 书签功能：可添加和管理书签

9. 性能优化

- 虚拟滚动：大文件采用虚拟滚动技术

- 内存管理：优化内存使用，支持超大文件

- 多线程：耗时操作使用独立线程

10. 自定义功能

- 主题设置：支持明暗主题切换

- 字体设置：可自定义显示字体

- 显示设置：可调整每行显示字节数等参数

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/kiaoFVP7GOX1ouTFTRKuyDibX1LHIayE9ybFzUua8vmB62OT6XNxxva6G28Wx5AR6REzKbEHPibdmdfUt3eOTCpXQ/0?wx_fmt=png)

由由学习吧

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kiaoFVP7GOX1ouTFTRKuyDibX1LHIayE9ybFzUua8vmB62OT6XNxxva6G28Wx5AR6REzKbEHPibdmdfUt3eOTCpXQ/0?wx_fmt=png)

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
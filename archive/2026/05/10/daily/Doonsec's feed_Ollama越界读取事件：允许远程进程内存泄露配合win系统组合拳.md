---
title: Ollama越界读取事件：允许远程进程内存泄露配合win系统组合拳
url: https://mp.weixin.qq.com/s/uFteAf4OObFN9JN7VrBfug
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:52:15.605297
---

# Ollama越界读取事件：允许远程进程内存泄露配合win系统组合拳

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eefCd8vibaic0a91FiaCwZp7PqOicPBJgb9zfcVgr0tWtYBiaeqxicj5nibpgPhVndQCfT89YVjOoazdbtbhCTBP1nITYcR5a3n2Kw5IbnuLG67nvk/0?wx_fmt=jpeg)

# Ollama越界读取事件：允许远程进程内存泄露配合win系统组合拳

原创

404号浪漫
404号浪漫

404号浪漫

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

---

0x01 核心速览

|  |  |
| --- | --- |
| 【事件】 | 【影响】 |
| Ollama 开源大模型 运行框架被披露存在一个严重漏洞CVE-2026-7482（代号 Bleeding Llama），可导致未认证的远程攻击者泄露整个进程内存；同时，其 Windows 客户端更新机制也被发现两个未修补漏洞（CVE-2026-42248、CVE-2026-42249），可串联实现持久化任意代码执行。 | CVE-2026-7482 影响全球超过 30 万台暴露在互联网的服务器，可能导致 API 密钥、对话数据等敏感信息泄露；Windows 更新漏洞影响 0.12.10 至 0.22.0 版本，允许攻击者在用户登录时静默执行任意代码 |

---

0x02 正文解读

2.0-事件发现与确认

CVE-2026-7482：Bleeding Llama 堆越界读取漏洞

Ollama 在 0.17.1 之前的版本中，其中 GGUF  模型加载器存在堆越界读取漏洞。根源在于 fs/ggml/gguf.go 与 server/quantization.go 的 WriteTo() 函数使用了 Go 语言的 unsafe 包，绕过了内存安全保证。攻击者可通过向暴露的服务器提交特制 GGUF 文件，将张量的形状声明为极大值，使得在通过 /api/create 端点执行量化期间，服务器读取超出已分配堆缓冲区的内存。

2.1-利用链与数据外泄
完整的利用过程分三步：

1. 通过 HTTP POST 将构造的 GGUF 文件上传到可网络访问的Ollama 服务器；
2. 调用 /api/create 端点触发越界读取，将进程内存中的数据写入模型 产物；
3. 使用 /api/push 端点将含有敏感数据的模型产物推送到攻击者控制的注册表，实现数据外泄。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eefCd8vibaic2QBWykyler0kE4qYg7zPyaXaL0yG7O2Hw1CsY38T6JC44wCr48ib9FxYF10oZp1jA29UDL2puv7LaZhtw52kZkJGgesfqRu7jg/640?wx_fmt=png&from=appmsg)

被泄露的数据可能包括环境变量、API 密钥、系统提示以及并发用户的对话内容。尤其当工程师将 Ollama 与 Claude Code 等工具连接时，所有工具输出都可能落入攻击者之手。

2.2-两个未修补的 Windows 更新漏洞

Striga 研究人员发现，Ollama Windows 桌面客户端存在两个未修复漏洞，影响版本 0.12.10 至 0.17.5（另一处描述为至 0.22.0），披露至今已逾 90 天仍未修补。

* CVE-2026-42248（CVSS 7.7）：签名验证缺失漏洞。Windows 更新程序在安装更新前未验证二进制文件的签名，与 macOS 版本行为不一致。
* CVE-2026-42249（CVSS 7.7）：路径遍历漏洞。更新程序直接从 HTTP 响应头构造安装程序暂存目录的本地路径，未进行任何清理。

攻击者若能够篡改 Ollama 客户端的更新响应（如覆盖 OLLAMA\_UPDATE\_URL 环境变量指向恶意 HTTP 服务器，且 AutoUpdateEnabled 为默认启用的状态），即可利用签名验证缺失下发恶意程序。单独利用此缺陷可获得一次非持久化的代码执行；

结合路径遍历漏洞，则可将恶意可执行文件写入 Windows 启动文件夹（%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup），在每次用户登录时实现静默、持久的任意代码执行。

2.3-缓解与应对

对于 CVE-2026-7482，用户应升级至修复版本，并通过防火墙隔离、审计暴露面、在 Ollama 实例前部署认证代理或 API 网关等方式限制网络访问。对于 Windows 更新漏洞，因暂无官方补丁，建议立即关闭自动更新，并移除启动文件夹中的 Ollama 快捷方式，以阻断静默登录执行路径。

---

0x03 动作指引

* 升级版本：将 Ollama 升级至 0.17.1 或更高版本，以修复 CVE-2026-7482。
* 网络加固：限制对 Ollama 服务器的网络暴露，部署认证代理或 API 网关，因为 REST API 默认不提供身份验证。
* Windows 客户端应急措施：

+ 关闭自动更新，或将 AutoUpdateEnabled 设为 false。

+ 删除启动文件夹中的 Ollama 快捷方式：%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup 下的相关条目。

* 注意：移除恶意投递的文件可以终止持久化，但底层漏洞仍然存在，需持续关注后续补丁。

---

0x04 参考链接

1.https://thehackernews.com/2026/05/ollama-out-of-bounds-read-vulnerability.html

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/wEkiap6hicP8wF2BoUKvl2PZeYrzoL5WHkKL84ARsl3RQuvwffNibLvWIUO0bmIE5zQDGt4JTT0BUNwIiaUCSSrfOQ/0?wx_fmt=png)

404号浪漫

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/wEkiap6hicP8wF2BoUKvl2PZeYrzoL5WHkKL84ARsl3RQuvwffNibLvWIUO0bmIE5zQDGt4JTT0BUNwIiaUCSSrfOQ/0?wx_fmt=png)

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
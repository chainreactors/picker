---
title: 一个开源工具的逆袭：用真实浏览器指纹正面刚Cloudflare Turnstile
url: https://mp.weixin.qq.com/s/yMVuXyKMrs2GotpGvbudGQ
source: Doonsec's feed
date: 2026-07-13
fetch_date: 2026-07-14T04:44:31.212516
---

# 一个开源工具的逆袭：用真实浏览器指纹正面刚Cloudflare Turnstile

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/dscLuiaicVquMdHa6qZdLWDwcBVnKx0DYF2tgB2XibFe3QJHtmOLLjXDjRR2S8cXIuaKutOia0YX8a4JpPEkjbJUItDEf3otjSkdYsksm7JvjDY/0?wx_fmt=jpeg)

# 一个开源工具的逆袭：用真实浏览器指纹正面刚Cloudflare Turnstile

原创

RAT-C2
RAT-C2

船山信安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 绕过Cloudflare Turnstile，一个自动提交漏洞到VulDB的开源工具

VulDB（vuldb.com）是安全圈里知名度颇高的漏洞数据库平台，但用过它Web界面提交漏洞的人都知道，那体验实在算不上友好。两道关卡横在面前：Cloudflare Turnstile浏览器端人机验证（JS挑战加指纹检测），以及VulDB登录后的CSRF保护——每次请求必须携带动态token。

有个开源工具把这事解决了——vuldb-submit，基于DrissionPage加Claude Code Skill的VulDB漏洞自动化提交工具。依赖环境由SKILL.md引导AI自动初始化，用户只需配置账号、触发关键词就能用。

## 快速开始

部署简单得离谱。把vuldb-submit整个目录复制到Claude Code的skills目录就行，Windows丢到C:\Users\用户.claude\skills\vuldb-submit，Linux和macOS丢到~/.claude/skills/vuldb-submit。然后编辑scripts/submit\_vuln.py，修改第25-26行的USERNAME和PASSWORD，仅此两步，部署完成。

在Claude Code里敲一句/vuldb-submit，AI自动读取SKILL.md，检查并初始化依赖环境，然后引导你一步步完成漏洞提交。项目已在Linux和Windows下验证通过。

## 使用流程

交互过程设计得很接地气。流程是这样的：输入/vuldb-submit后AI让你指定漏洞报告文件路径，支持txt、md、pdf格式。AI自动读取文件后把vendor、product、version、class、desc、link这些字段用表格回显出来，问你确认还是修改。确认就发出去，中途想改随时可以输入修改vendor=xxx调整字段，想取消就取消。

命令行模式也有，适合不想交互的场景：

```
# Windows
.venv\Scripts\python scripts\submit_vuln.py --file data.json

# Linux
xvfb-run --auto-servernum .venv/bin/python scripts/submit_vuln.py --json '{"vendor":"...","...}'
```

## 技术架构

整个工具分两层。上层是Claude Code交互层，负责读取SKILL.md、引导用户、读取报告文件、提取字段、确认后调用脚本。下层是提交引擎submit\_vuln.py，执行五个步骤：第一步DrissionPage启动Chromium，靠真实浏览器TLS指纹让Cloudflare自动通过；第二步登录VulDB，wait\_cf()等待Turnstile挑战完成后填写账号密码点击Login；第三步GET /vuln/add提取CSRF token；第四步通过浏览器内JS的fetch()发送POST，利用浏览器TLS连接保证CF不拦截；第五步响应分析加自动重试，Thank you for submitting就是成功，We need more details说明描述太短，duplicate可能是重复，遇到新CSRF token则刷新重试最多3次。

## 为什么能绕过Cloudflare

VulDB使用Cloudflare Turnstile做验证。作者列了完整的实测对比：requests直接403被拦，cloudscraper只支持旧版IUAM挑战不支持Turnstile，curl\_cffi的TLS指纹伪装对GET偶尔有效但POST仍被403，playwright的headless模式被检测、非headless仍需手动交互。最终锁定DrissionPage加浏览器内fetch，真实浏览器TLS加JS环境，Turnstile自动通过。

核心原理在于Turnstile对每个HTTP连接做TLS指纹校验。requests或curl\_cffi发起的POST与浏览器GET的TLS指纹不同，Cloudflare会再次拦截POST。这个工具通过tab.run\_js(fetch(...))在浏览器JS上下文内发起POST，请求复用浏览器的TLS连接、cookie存储和HTTP栈，Cloudflare看到的是同一个浏览器的后续请求，不会二次挑战。

## 字段与配置

必填字段五个：vendor厂商名称、product产品名称、version受影响版本、class漏洞类型（SQL Injection、XSS、RCE等）、desc详细描述（技术细节加影响范围，建议150字符以上）。link参考链接或Advisory URL是可选的。

脚本可调配置三项：USERNAME和PASSWORD必改；max\_retries提交重试次数默认3次，在submit\_with\_retry()函数参数中修改；timeout控制Cloudflare等待超时默认90秒，在wait\_cf()函数参数中修改。

## 常见问题

文档覆盖了八类问题。报Missing X server需要安装xvfb并用xvfb-run包装。浏览器连接失败要检查Chromium是否安装、是否需要--no-sandbox参数（Docker或root环境）。长时间卡Cloudflare验证可能是IP触发了更严格验证，等一两分钟或换网络、换代理。描述被拒就扩充desc字段。被判重复说明相同vendor+product+version组合可能已有待审记录。401是会话过期需重新登录。调试可直接用tab.screenshot(path="/tmp/debug.png")截图。

## 项目结构

```
vuldb-submit/
├── README.md              # 用户部署指南和技术文档
├── SKILL.md               # Skill定义，AI操作手册，含依赖初始化流程
├── scripts/
│   └── submit_vuln.py     # 核心提交脚本
├── .vuldb_cookies.json    # 运行时生成的浏览器cookie缓存
└── .venv/                 # Python虚拟环境，AI加载skill时自动初始化
```

许可证声明：本项目仅供学习研究使用，禁止通过滥用或二次修改对VulDB平台造成任何不良影响，相关风险由使用者自行承担，请遵守VulDB平台的使用条款。

GitHub地址：https://github.com/Jack-MRJ/vuldb-submit

## 成功案例

Linux 下提交：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquOuc0OweGMXxyTLGia7mdqoVvtM5PEsO5WC6TENqYYf35UBwrUmtkLOLicseP2o3HJSwptNI4kgklpFYxXjDibp4VIvM53B3X5VQk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquMjWmbGic2BJbfjIVN5Ht5HcKGVvYE6YxbsaBIc2ia5TS5qHZyAV2U1sNgLLPUu0YgO1fNrWicsNsS2tNKgsibpRRZVw36CnhickNJw/640?wx_fmt=png&from=appmsg)

Windows 下提交：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquMVXQhZPibp8NYSKhLKdpVFLlMMcJsyWEXb3REMvZnUichSiaRUZo37vibd0EBWvaQCiaV1eeyk4E4vMkqNtbBs05ouI4icACq2XkRkk/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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
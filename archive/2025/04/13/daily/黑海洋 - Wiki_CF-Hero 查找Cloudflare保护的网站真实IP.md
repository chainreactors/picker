---
title: CF-Hero 查找Cloudflare保护的网站真实IP
url: https://blog.upx8.com/4739
source: 黑海洋 - Wiki
date: 2025-04-13
fetch_date: 2025-10-06T22:05:24.998403
---

# CF-Hero 查找Cloudflare保护的网站真实IP

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# CF-Hero 查找Cloudflare保护的网站真实IP

发布时间:
2025-04-12

分类:
[系统安全/os\_security](https://blog.upx8.com/os_security/)

热度:
33578

## CF-Hero它是什么？

CF-Hero 是一款综合侦察工具，旨在发现受 Cloudflare 保护的 Web 应用程序的真实 IP 地址。它通过多种方法进行多源情报收集。

### DNS 侦察

* 当前 DNS 记录（A，TXT）
* 历史DNS数据分析
* 关联域发现

### 情报来源

* 主动 DNS 枚举
* Censys 搜索引擎
* Shodan 搜索引擎
* SecurityTrails 历史记录
* 相关领域关联

该工具分析来自这些来源的数据，以识别受 Cloudflare 保护的目标的潜在原始 IP 地址。它通过响应分析来验证发现，以最大限度地减少误报。

**该工具的简单流程图**

[![CF-Hero 查找Cloudflare保护的网站真实IP](https://www.ddosi.org/wp-content/uploads/2025/04/01133020.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI1LzA0LzAxMTMzMDIwLndlYnA)

#

## 特征

* DNS 侦察
  + 检查当前 DNS 记录（A、TXT）
  + 提取 Cloudflare 背后的域名
  + 提取不在 Cloudflare 后面的域

* 第三方情报
  + Censys 集成
  + Shodan 集成
  + SecurityTrails 集成
  + 关联域的反向 IP 查找

* 高级功能
  + 自定义 JA3 指纹支持
  + 并发扫描功能
  + 标准输入支持（管道）
  + HTML 标题比较以进行验证
  + 代理支持
  + 自定义用户代理配置

## 当前 DNS 记录

让我们看一些 DNS 设置错误的用例。

如您所见，常规 DNS 查询会返回域的 IP 地址。例如，musana.net 位于 Cloudflare (CF) 后面，但有时域有多个 A 记录，其中一些可能不对应于与 CF 关联的 IP 地址。（此 DNS 输出仅为说明性示例，可能不代表 musana.net 的确切 DNS 答案。）

```
;; ANSWER SECTION:
musana.net.    300    IN    A    104.16.42.102
musana.net.    300    IN    A    104.16.43.102
musana.net.    300    IN    A    123.45.67.89 (Real IP exposed)
musana.net.    300    IN    A    123.45.76.98 (Real IP exposed)
```

另一种情况与 TXT 记录有关。有时域名落后于 CF，但域名的真实 IP 可能用于 TXT 记录。CF-Hero 检查所有 TXT 记录，然后提取所有 IP 地址，最后尝试通过 HTTP 连接它找到的 IP。

假设我们有类似 DNS TXT 记录。如 TXT 记录所示，有 SPF 记录。有些公司可以托管自己的邮件服务器，TXT 记录可能包含指向目标域的 IP。

正如您在以下 DNS 答案中看到的，SPF 记录有一些 IP 地址。Cf-Hero 也会检查这些。

```
;; ANSWER SECTION:
musana.net.    115    IN    TXT    "1password-site-verification=LROK6G5XFJG5NF76TE2FBTABUA"
musana.net.    115    IN    TXT    "5fG-7tA-G4V"
musana.net.    115    IN    TXT    "MS=ms16524910"
musana.net.    115    IN    TXT    "OSSRH-74956"
musana.net.    115    IN    TXT    "docker-verification=6910d334-a3fc-419c-89ac-57668af5bf0d"
musana.net.    115    IN    TXT    "docusign=4c6d27bb-572e-4fd4-896c-81bfb0af0aa1"
musana.net.    115    IN    TXT    "shopify-verification-code=1Ww5VsPpkIf32cJ5PdDHdguRk22K2R"
musana.net.    115    IN    TXT    "shopify-verification-code=NM243t2faQbaJs8SRFMSEQAc4J9UQf"
musana.net.    115    IN    TXT    "v=spf1 include:_spf.google.com include:cust-spf.exacttarget.com include:amazonses.com include:mail.zendesk.com include:servers.mcsv.net include:spf.mailjet.com ip4:216.74.162.13 ip4:216.74.162.14  ip4:153.95.95.86 ip4:18.197.36.5 -all"
```

## 开源情报

OSINT 是另一种查找任何落后于 CF 的域名的真实 IP 的技术。有许多专门用于特殊目的的搜索引擎。Shodan 和 Censys 就是其中两个。它们提供更多细节和技术信息。这些搜索引擎不断扫描整个互联网并发现新资产或监控和记录资产的变化。当一个不落后于 CF 的域名启动时，这些引擎的机器人可以记录该域名的真实 IP。一段时间后，如果该域名落后于 cloudflare，则可以使用这些搜索引擎找到它们的 IP。

CF-Hero 也会检查 censys 和 shodan。（请注意，当您使用这些服务时，您会受到 API 配额的限制。）

## （子）域名

另一个技巧是（子）域名技术。实际上它不一定是子域名，也可以是域名。关键点在这里；域名应该属于同一家公司。

假设我们有 2 个域。其中一个在 CF 后面，而另一个不在。在这种情况下，您连接到不在 CF 后面的域，然后将主机标头更改为在 CF 后面的域。如果您收到在 CF 后面的应用程序的响应，那么恭喜您绕过了 CF。您可以直接从 IP 访问 Web 应用程序。（当然这也取决于配置）

让我们仔细看看

```
--> TCP --> blog.musana.net [123.45.67.89] ---> HTTPs -------------\
                                                                    \
--> TCP --> api.musana.net [123.67.45.98] ----> HTTPs -----------\   \
                                                                  \   \
--> TCP --> test.musana.net [123.89.44.88] ---> HTTPs -------------\   \
                                                                    \___\____________________
--> TCP --> tools.musana.net [123.44.55.66] --> HTTPs -------------> | GET / HTTP/2          |
                                                                     | Host: musana.net      | ====> Check & Compare Responses
--> TCP --> admin.musana.net [33.44.123.45] --> HTTPs -------------->|_______________________|
                                                                          /    /
--> TCP --> ... [...] ------------------------> HTTPs ------------------>/    /
                                                                        /    /
--> TCP --> ... [...] ------------------------> HTTPs ---------------->/    /
                                                                      /    /
--> TCP --> random-test.com [55.44.11.33] ----> HTTPs -------------->/    /
                                                                         /
--> TCP --> fsubsidiary.net [66.77.22.123] ---> HTTPs ----------------->/
```

## 历史 DNS 记录

历史 DNS 记录服务会尝试发现互联网上的所有域并记录这些域的 DNS 记录中的更改。这些服务中最著名的是 securitytrails。如果某个域使用其真实 IP 地址在互联网上发布，则这些服务的机器人可以记录其真实 IP 地址，然后如果该域被 cloudflare 接管，则可以使用这些服务找出真实 IP 地址。因此，我们可以找到过去通过真实 IP 地址广播过的域的真实 IP 地址。

它使用安全跟踪服务来获取历史 DNS 记录。在 cf-hero.yaml 文件中输入 API 密钥后，您可以使用参数`-securitytrails`执行此扫描。

# 安装说明

cf-hero 需要**go1.18**才能成功安装。运行以下命令进行安装。

```
go install -v github.com/musana/cf-hero/cmd/cf-hero@latest
```

# 用法

```
        ____         __
  _____/ __/        / /_  ___  _________
 / ___/ /__  ___   / __ \/ _ \/ ___/ __ \
/ /__/ ___/ (___) / / / /  __/ /  / /_/ /
\___/_/          /_/ /_/\___/_/   \____/

                                @musana
_____________________________________________

揭示受 Cloudflare 保护的域名的源 IP

用法:
  cf-hero [flags]

选项：
通用选项：
  -w int 工作线程数（默认 16）
  -f string 包含主机/域名列表的输入文件

输出选项：
  -cf 输出受 Cloudflare 保护的域名
  -non-cf 输出未受 Cloudflare 保护的域名

数据源：
  -censys 在扫描中包含 Censys
  -securitytrails 在扫描中包含 SecurityTrails 历史 DNS 记录
  -shodan 在扫描中包含 Shodan 历史 DNS 记录
  -dl string 用于子域/域扫描的域名列表
  -td string 用于子域/域扫描的目标域

配置：
  -hm string HTTP 方法（默认 "GET"）
  -ja3 string JA3 指纹（默认 "772,4865-4866-4867-49195-49199-49196-49200-52393-52392-49171-49172-156-157-47-53,18-10-16-23-45-35-5-11-13-65281-0-51-43-17513-27,29-23-24,0"）

  -ua string HTTP User-Agent（默认 "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/113.0"）
  -px string HTTP 代理 URL
```

# 运行 CF-Hero

最基本的运行命令。默认检查A记录和TXT记录。

```
# cat domains.txt | cf-hero
```

或者您可以将“f”参数传递给它。

```
# cf-hero -f domains.txt
```

使用**censys**参数将 Shodan 纳入扫描

```
# cat domain.txt | cf-hero -censys
```

使用**shodan**参数将 Shodan 纳入扫描

```
# cat domain.txt | cf-hero -shodan
```

使用**securitytrails**参数将 Shodan 纳入扫描

```
# cat domain.txt | cf-hero -securitytrails
```

使用 -td 和 -dl 参数尝试利用不在 Cloudflare 后面的域或子域列表来查找目标域的 IP 地址。通过使用 -dl 参数在已识别目标云或本地基础设施使用的实时 IP 地址的块中指定 IP 地址，您可以找到目标域的真实 IP 地址

```
# cf-hero -td https://musana.net -dl sub_domainlist.txt
```

获取 CF 背后的域名

```
# cf-hero -f domains.txt -cf
```

获取不落后于CF的域名

```
# cf-hero -f domains.txt -non-cf
```

其他选项（自定义 ja3、代理、工作者、用户代理）

```
# cf-hero -d https://musana.net -ua "Mozilla" -w 32 -ja3 "771,22..." -px "http://127.0.0.1:8080"
```

在 $HOME/.config/ 目录下创建 cf-hero.yaml 文件来设置 censys API 密钥

```
# touch ~/.config/cf-hero.yaml

// content of YAML file should be like;

securitytrails:
  - "api_key_here"
shodan:
  - "api_key_here"
censys:
  - "api_key_here"
```

## 截图

[![CF-Hero 查找Cloudflare保护的网站真实IP](https://www.ddosi.org/wp-content/uploads/2025/04/01133357.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI1LzA0LzAxMTMzMzU3LndlYnA)
[![CF-Hero 查找Cloudflare保护的网站真实IP](https://www.ddosi.org/wp-content/uploads/2025/04/01133404.webp)](https://blog.upx8.com/go/aHR0cHM6Ly93d3cuZGRvc2kub3JnL3dwLWNvbnRlbnQvdXBsb2Fkcy8yMDI1LzA0LzAxMTMzNDA0LndlYnA)

## 待办事项

* JA3 随机化。（在某些情况下，Cloudflare 会在 TLS 层阻止用于自动化/扫描目的的库的 JA3 哈希。此功能旨在绕过该保护。您目前可以提供自定义 JA3 字符串来绕过此保护。）
* 将添加一种更有效的技术来确定两个 HTTP 响应是否相同。

## GitHub：

[https://github.com/musana/CF-Hero](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL211c2FuYS9DRi1IZXJv)

## 下载地址

[https://github.com/musana/CF-Hero/archive/refs/tags/v1.0.2.zip](https://blog.upx8.com/go/aHR0cHM6Ly9naXRodWIuY29tL211c2FuYS9DRi1IZXJvL2FyY2hpdmUvcmVmcy90YWdzL3YxLjAuMi56aXA)

[取消回复](https://blog.upx8.com/4739#respond-post-4739)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianme...
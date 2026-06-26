---
title: 创宇安全智脑通用安全能力升级通告（20260625）
url: https://mp.weixin.qq.com/s/SesOvlXdBGBtDq3eeKoJ0A
source: Doonsec's feed
date: 2026-06-25
fetch_date: 2026-06-26T06:07:09.864321
---

# 创宇安全智脑通用安全能力升级通告（20260625）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ou5agVlRCt9cGZkgUJrkScKfqa7mYjibdCNIDJI9skN9cjDxfj3vGPNX8sHiap2NOuGib2dY9kjX2SMPZxibljAJdMjTSTkpGIO8ichN1qYp6ATE/0?wx_fmt=jpeg)

# 创宇安全智脑通用安全能力升级通告（20260625）

创宇安全智脑
创宇安全智脑

创宇安全智脑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**创宇安全智脑**是基于知道创宇17年来AI+安全大数据在真实攻防场景中的经验积累构建的下一代全场景安全智能算力平台。平台拥有海量真实攻防数据和安全大数据持续生产能力；结合面向多个实战场景的AI智能模型，持续汇聚、萃取和分析，实时输出高精准高价值威胁情报、安全态势、攻防策略；持续全场景赋能知道创宇全产品矩阵和安全托管服务。

**创宇安全智脑目前已经联动支撑知道创宇全产品矩阵，包括：创宇盾、抗D保、ScanV、创宇大模型网关、大模型盾、ZoomEye互联网攻击面管理平台、创宇蜜罐、创宇云图、创宇云影、创宇猎幽、创宇威胁情报网关等。**

本月共新增插件330个，大模型规则277个，其中重点插件10个，重点大模型规则10个。

**详情如下：**

**大模型安全能力更新列表**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ou5agVlRCtib0SrPOgSViaE7ibMfPzkdMX8icFJZEKJdibx1TtHKl0jFUNLe0hZs2icEIkXeDX80ib2qAGTjoYZnNSyXN5fMdclobn13h6VU5uJAr0/640?wx_fmt=png&from=appmsg)

**漏洞插件更新列表**

![](https://mmbiz.qpic.cn/mmbiz_png/Ou5agVlRCticrYibKEYjUCmwfI6ZCZTJExb17e0289TKF1E82qQmQeAleibTNKn5Ak05zMVhbsTGn0B9U2nM18ahttXwdYwn2p2os7V4bNx5YE/640?wx_fmt=png&from=appmsg)

**漏洞详情**

**新增插件：**

**1****、UniFi OS Server 命令注入（CVE-2026-34910）**

**发布时间**：2026-06-22

**漏洞等级**：严重
**漏洞来源**：https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-34910

**漏洞描述**：

UniFi OS 是 Ubiquiti 公司开发的网络设备管理操作系统，可运行于 Ubiquiti 硬件控制台或自托管在标准服务器上，提供统一的 Web 管理界面用于集中管理网络设备、摄像头、门禁系统等。UniFi OS Server 5.0.8 以下版本存在输入验证不当漏洞，由于认证模块与 Nginx 对请求 URI 的处理存在不一致（认证模块使用原始 URI 进行鉴权，Nginx 使用规范化后的 URI 进行路由），未经认证的远程攻击者可通过路径穿越绕过身份认证，向 ucs/update/latest\_package 接口的 pkg\_name 参数注入恶意系统命令。恶意攻击者可以利用该漏洞在服务器上执行系统命令，直接操控操作系统资源，对业务系统和内网环境造成严重破坏。
**漏洞危害：**
恶意攻击者可以利用该漏洞注入任意系统命令，获取系统权限。
**建议解决方案：**
1、升级 UniFi OS Server 至 5.0.8 或更高版本，官方已修复该漏洞；2、在网络边界部署 WAF 拦截包含路径穿越和命令注入特征的恶意请求；3、限制 UniFi OS Server 管理 Web 接口的网络访问范围，仅允许可信来源连接；4、监控服务器上的异常进程和 sudo 调用记录，排查是否存在已被入侵的痕迹。
**影响范围：**
根据ZoomEye网络空间搜索引擎关键字 app="UniFi OS" 对潜在可能目标进行搜索，共得到356,863条搜索结果。主要分布在美国、德国等国家。
（ZoomEye搜索链接：https://www.zoomeye.org/searchResult?q=app%3D%22UniFi%20OS%22）

![](https://mmbiz.qpic.cn/mmbiz_png/Ou5agVlRCt8DqLou9y6VuYIzDaW53zaCKV1mIB38UzEdf921CMmdzAweqEzZ8ltuqribibqaPHcC3EnbIbVHaNbIDLOT4zNObW1DuOwe7yB5g/640?wx_fmt=png&from=appmsg)

**区域分布**：

![](https://mmbiz.qpic.cn/mmbiz_png/Ou5agVlRCt9QGP8WwqV6Ajyl65iba4WBHL6WF8bic7qTib5VL7AQWEpx2xZ8p9kNyib66LhcEGW4SvtqhkLSrBfS1RD2MPOG9Byic1psWMdq75Fw/640?wx_fmt=png&from=appmsg)

**2****、Amasty Order Attributes 任意文件上传（CVE-2026-53787）**

**发布时间**：2026-06-23
**漏洞等级**：严重
**漏洞来源**：https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-53787

**漏洞描述**：

Amasty Order Attributes是Amasty公司开发的一款Magento 2扩展插件，允许商家在结账页面添加自定义订单字段并收集客户的额外订单信息。Amasty Order Attributes for Magento 2 4.0.0之前版本文件上传接口存在任意文件上传漏洞。未经授权的远程攻击者可向服务器上传恶意文件并被解析执行，进而获取服务器控制权、植入后门或横向渗透内部系统。
**漏洞危害：**
未经授权的远程攻击者可向服务器上传恶意文件并被解析执行，进而获取服务器控制权、植入后门或横向渗透内部系统。
**建议解决方案：**
1、升级Amasty Order Attributes到4.0.0或更高版本；2、确保pub/media目录禁止执行PHP文件；3、部署Web应用防火墙拦截对uploadFile接口的异常文件上传请求；4、使用安全扫描工具检测服务器是否存在WebShell或后门文件。
**影响范围：**
根据ZoomEye网络空间搜索引擎关键字 app="Amasty Order Attributes" 对潜在可能目标进行搜索，共得到5条搜索结果。主要分布在德国、英国等国家。
（ZoomEye搜索链接：https://www.zoomeye.org/searchResult?q=app%3D%22Amasty%20Order%20Attributes%22）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ou5agVlRCt9a8nEpOYCkuFeCFDicwY47AvfhRGdBicmyf2nIgCbfllWyGUXN9TibIeejShy9FXykHgLAQiaZm57O7fXiaMVshsZia7axtyZYw427A/640?wx_fmt=png&from=appmsg)

**区域分布：**

![](https://mmbiz.qpic.cn/mmbiz_png/Ou5agVlRCt81eQPasbCgpndYEXHHhfj0IBIn5XCsRGbGZRhxuLicmqT9GjvY2YwDIJdmqwMML7RBvllRN7iazpAN7J9c3OIdxHHwmYFZ8cl6w/640?wx_fmt=png&from=appmsg)

**3****、UniFi Network Application 路径穿越（CVE-2026-22557）**

**发布时间**：2026-06-22
**漏洞等级**：严重
**漏洞来源**：https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-22557

**漏洞描述**：

UniFi Network Application 是 Ubiquiti 公司开发的一款网络设备集中管理平台。UniFi Network Application 的 guest portal 接口 /guest/s/<site>/wechat/sign 在处理 page\_error 参数时未正确校验，存在路径穿越漏洞。未经认证的远程攻击者可通过构造包含 ../ 的 page\_error 参数值，读取服务器上的任意文件（如 system.properties 配置文件），进而获取控制器备份中的管理员凭证，完全控制所有被管理设备。
**漏洞危害：**
未经认证的远程攻击者可构造包含 ../ 的 page\_error 参数值，读取服务器上的任意文件（如 system.properties 配置文件），进而获取控制器备份中的管理员凭证，完全控制所有被管理设备。
**建议解决方案：**
1、升级 UniFi Network Application 至 9.0.118、10.1.89 或 10.2.97 及以上版本；2、限制 guest portal 端口（8443、8843、8880）的网络访问，仅允许可信 IP 访问；3、部署 WAF 规则拦截 page\_error 参数中包含路径穿越字符的恶意请求。
**影响范围：**
根据ZoomEye网络空间搜索引擎关键字 app="UniFi Network Application" 对潜在可能目标进行搜索，共得到170,161条搜索结果。主要分布在美国、德国等国家。
（ZoomEye搜索链接：https://www.zoomeye.org/searchResult?q=app%3D%22UniFi%20Network%20Application%22）

![](https://mmbiz.qpic.cn/mmbiz_png/Ou5agVlRCtibGnibWoVJib87OBZicktIias4M2B3MFAEdcmJkATzicwjmIlMAZXBRXiaiadEy2ASWY2JL1eoVrbaZJV5kicIibN8CQ0dpe4bwYGtBwfHs/640?wx_fmt=png&from=appmsg)

**区域分布**：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ou5agVlRCticWXRKRTt5MzkDp3NkhHn3ej23ObWIHga5dxM9kBJpB32k92ggq9VGTMzlfRhm9BUTxicgKbicibLYE8N6rKWhfCwvUSsMVrbK2M8/640?wx_fmt=png&from=appmsg)

**4****、dotCMS Publish Audit API SQL注入（CVE-2026-8054）**

**发布时间**：2026-06-09
**漏洞等级**：严重
**漏洞来源**：https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-8054

**漏洞描述**：

dotCMS 是一个开源的企业级内容管理系统，支持多站点管理和内容发布。dotCMS Core 25.11.04-1 至 26.04.28-02 版本的 Publish Audit API 接口（/api/auditPublishing/get 和 /api/auditPublishing/getAll）存在未授权 SQL 注入漏洞。由于该接口未强制身份验证且使用字符串拼接构建 SQL 查询，未经认证的远程攻击者可通过注入恶意 SQL 指令，非法读取数据库中的任意数据。
**漏洞危害：**
恶意攻击者通过注入恶意SQL指令，可非法访问、篡改或删除数据库敏感数据，甚至通过数据库提权功能获取服务器最高控制权，导致严重的数据泄露或业务中断。
**建议解决方案：**
1、升级 dotCMS Core 到 26.04.28-03 或更高版本，官方已修复参数化查询和身份验证问题；2、在 WAF 或反向代理上配置规则，拦截对 /api/auditPublishing/get 和 /api/auditPublishing/getAll 路径的外部请求；3、限制数据库账户权限，遵循最小权限原则，禁止执行高危数据库函数（如 pg\_read\_file）。
**影响范围：**
根据ZoomEye网络空间搜索引擎关键字 app="dotCMS" 对潜在可能目标进行搜索，共得到3,800条搜索结果。主要分布在美国、加拿大等国家。
（ZoomEye搜索链接：https://www.zoomeye.org/searchResult?q=app%3D%22dotCMS%22）

![](https://mmbiz.qpic.cn/mmbiz_png/Ou5agVlRCticoSBCNP82hIdo7KSL3NdJE37xzNxFutUrTFoofyJNA6icicC0U4zxeXyk5lJHQkbIC2YmGEdsNChbE2kHu03icDLP7rGhfz5C3fw/640?wx_fmt=png&from=appmsg)

**区域分布**：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ou5agVlRCtibaQuLamD2jnE2bXwzv4fVlXvdOjo2EynGcnT1aiaylg1xomicMmKvoXS6c8nLazlGBzh4t9DQXdXSVKwlA5yWslb6JmEaKG6H4g/640?wx_fmt=png&from=appmsg)

**5****、Ivanti Sentry handleMessage 系统命令执行（CVE-2026-10520）**

**发布时间**：2026-06-10
**漏洞等级**：严重
**漏洞来源**：https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-10520

**漏洞描述**：

Ivanti Sentry 是 Ivanti 公司推出的一款移动设备安全网关产品，位于移动设备与企业后端系统之间，负责管理和加密 ActiveSync 流量及应用数据，通常与 Ivanti EPMM 配合使用。Ivanti Sentry R10.5.2、R10.6.2、R10.7.1 以下版本 /mics/api/v2/sentry/mics-config/handleMessage 接口存在系统命令执行漏洞。恶意攻击者可以利用该漏洞在目标系统上远程执行任意操作系统命令，获取 root 级别系统权限，进而完全控制服务器并对内网环境造成持续威胁。
**漏洞危害：**
恶意攻击者可以利用该漏洞在服务器上执行系统命令，直接操控操作系统资源，对业务系统和内网环境造成严重破坏。
**建议解决方案：**
1、升级 Ivanti Sentry 至 10.5.2、10.6.2 或 10.7.1 及以上版本；2、如无法立即升级，通过访问控制列表（ACL）限制 /mics/api/v2/sentry/mics-config/handleMessage 接口的外部访问；3、部署 WAF 规则，针对 message 参数中的 commandexec 标签进行请求过滤。
**影响范围：**
根据ZoomEye网络空间搜索引擎关键字 app="Ivanti Sentry" 对潜在可能目标进行搜索，共得到2,373条搜索结果。主要分布在美国、德国等国家。
（ZoomEye搜索链接：https://www.zoomeye.org/searchResult?q=app%3D%22Ivanti%20Sentry%22）

![](https://mmbiz.qpic.cn/mmbiz_png/Ou5agVlRCtibvCHcOrYkoBVTSDIh5b4UMfiaiaEUS649XNXNm34ab81kEWXhx2ypv0eV86TsHh9FuJ1279hSMlCicVj9hdUyGaQTGlu7UN69FIE/640?wx_fmt=png&from=appmsg)

**区域分布**：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ou5agVlRCt8tBxiaGwld6FChCAg7fVKcDcrps3UibCKMkzIiaObSicpawHnpcv7q8cObjlC5XNunTf7jw28O50Ck5JA8Rl78iciaMRpyAqqvb2HBc/640?wx_fmt=png&from=appmsg)

**6****、LiteLLM < 1.83.7 /mcp-rest/test/connection 系统命令执行（CVE-2026-42271）**

**发布时间**：2026-06-04
**漏洞等级**：严重
**漏洞来源**：https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2026-42271
**漏洞描述**：

LiteLLM 是 BerriAI 开源的一款 AI 网关代理服务器，用于以 OpenAI 格式调用各类 LLM API。LiteLLM 1.74.2 至 1.83.7（不含）版本中，MCP 服务器预览接口 POST /mcp-rest/test/connection 和 POST /mcp-rest/test/tools/list 接受包含 command、args 和 env 字段的完整服务器配置，当请求体中配置为 stdio 传输类型时，端点会调用 subprocess 启动指定的命令。接口仅验证有效的代理 API 密钥，缺乏基于角色的权限检查。当 LiteLLM 依赖的 Starlette 版本低于 1.0.1（CVE-2026-48710）时，攻击者可通过构造恶意 Host Header 绕过基于路径的认证中间件，将此漏洞从认证后命令执行升级为未认证远程代码执行。恶意攻击者可以利用该漏洞在代理服务器宿主机上以当前进程权限执行任意系统命令，窃取模型供应商 API Key、内部凭据等敏感信息，并进一步渗透内网。
**漏洞危害：**
恶意攻击者可以利用该漏洞在服务器上执行系统命令，直接操控操作系统资源，对业务系统和内网环境造成严重破坏。
**建议解决方案：**
1、升级 LiteLLM 到 1.83.7 或更高版本；2、升级 Starlette 依赖到 1.0.1 或更高版本，防止 Host He...
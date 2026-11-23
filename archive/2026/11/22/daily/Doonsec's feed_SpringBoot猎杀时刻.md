---
title: SpringBoot猎杀时刻
url: https://mp.weixin.qq.com/s/-VjZBk_mqLyRiGdo5Q2aEw
source: Doonsec's feed
date: 2026-11-22
fetch_date: 2026-11-23T10:01:46.706664
---

# SpringBoot猎杀时刻

# SpringBoot猎杀时刻

网安之家-CyberHomestead

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

SpringBoot猎杀时刻

---

01｜一个让微服务无处遁形的工具

日常渗透过程中，经常会碰到Spring Boot搭建的微服务，于是就想做一个针对Spring Boot的开源渗透框架，主要用作扫描Spring Boot的敏感信息泄露端点，并可以直接测试Spring的相关高危漏洞。于是，就写了这么一个工具：SpringBoot-Scan 【简称："SB-Scan"（错乱】

![SpringBoot-Scan](https://mmbiz.qpic.cn/mmbiz_png/l6gHYLEF4ibia8Srk2X8PC5e8amDPauTETF6fCibkfsria5zzrblu8wdJpcDnI7v6s8G4Igt5uwQJIsYDhwuZDPHHSWhlyPLh1EcHl1ZcAjickeU/640?wx_fmt=png&from=appmsg)

**本项目的GitCode地址：https://gitcode.com/AabyssZG/SpringBoot-Scan，当前工具版本号：V2.7.2-2025/11/09**

**我还整理了一篇SpringBoot的相关渗透姿势在我的个人博客，欢迎各位师傅前来交流哈哈：https://blog.zgsec.cn/archives/129.html**

截至发稿：**2371 Star / 182 Fork**，仓库 2023 年 1 月开源于 GitHub，最新提交就在当天——**还在持续更新的现役武器，不是坟场项目。**

---

02｜弹药库：内置 12 类高危漏洞，一路打穿

这已经不是"信息收集工具"，这是一台**漏洞利用平台**。内置弹药清单，逐条公开：

■

感谢 `@iChet666` 师傅的反馈，针对CVE-2021-21344 (Eureka\_Xstream 反序列化漏洞) 在利用过程中可能导致破坏业务的情况，进行流程优化和Exp利用二次确认

■

感谢 `@ez-lbz` 师傅提交的PR，添加支持CVE-2025-41243 (Spring Cloud Gateway环境属性修改漏洞)

■

感谢 `@ez-lbz` 师傅提交的PR，添加支持CVE-2024-37084 (Spring Cloud Data Flow远程命令执行漏洞)

■

添加支持2023 JeeSpringCloud 任意文件上传漏洞

■

添加支持CVE-2022-22947 (Spring Cloud Gateway SpEL RCE漏洞)

■

添加支持CVE-2022-22963 (Spring Cloud Function SpEL RCE漏洞)

■

添加支持CVE-2022-22965 (Spring Core RCE漏洞)

■

添加支持CVE-2021-21234 (任意文件读取漏洞)

■

添加支持2021 SnakeYAML\_RCE 漏洞

■

添加支持2021 Eureka\_Xstream 反序列化漏洞

■

添加支持2020 Jolokia配置不当导致RCE漏洞

■

添加支持CVE-2018-1273（Spring Data Commons RCE漏洞）

■

增加漏洞利用选择模块，可以选择单一或多个漏洞进行检测

■

命令执行漏洞式支持交互式执行命令

■

增加批量漏洞验证模块（你们一直想要的来啦）

后期将加入更多漏洞利用内置模块（各位师傅能不能赏个Star嘛~ 码代码挺辛苦的哈哈）

看清楚这份清单的含金量：**Spring Core RCE（CVE-2022-22965，也就是打穿全网的 Spring4Shell）、Spring Cloud Gateway SpEL RCE、SnakeYAML RCE、Jolokia RCE**——Spring 攻击面的历届"顶流"，全部内置，一键验证。**RCE 漏洞支持交互式执行命令，批量漏洞验证模块同步到位。**

---

03｜火力配置：从资产测绘到批量收割的完整链路

功能侧的迭代密度，直接看更新记录：

■

感谢 `@kn1g78` 师傅提交的PR，修复了端点扫描的若干BUG

■

感谢 `@ngc660sec` 师傅提交的PR，对于自定义请求头进行类型判断，防止二次转换类型

■

感谢 `@ThumpBo` 师傅提出的建议，增加了读取指定TXT批量扫描敏感文件的功能 `-df` 并将扫描成功结果导出至 `dumpout.txt` 内

■

对下载敏感文件的模块进行报错优化，将报错内容并入至 `error.log`

■

感谢 `@YanXi9999` 师傅的贡献，在读取指定TXT并批量信息泄露扫描过程中，去除重复页面提高效率

■

对端点爆破模块进行优化，对页面进行Hash计算，如果发现页面Hash相同的情况就不导入到 `urlout.txt`

■

在目录爆破 `run.py` /POC探测 `poc.py` /漏洞利用 `vul.py` 这三个核心模块，新增全局变量 `outtime = 10` 可自由调整各模块HTTP访问超时时间

■

感谢 `@Viking` 师傅，增加了部分 `Dir.txt` 敏感端点爆破字典的内容

■

感谢 `@Fkalis` 师傅，使用 `aiohttp` 对批量信息泄露扫描进行并发处理，大大提高 `-uf` 参数的扫描速度

■

新增支持多个参数自定义HTTP头部（请求头）进行操作，功能实现啦，快来试试吧~

■

新增支持资产测绘导出的时候自定义查询语句，更加灵活的导出目标资产数据

■

新增在敏感端点爆破爆破（单一和批量）的时候进行延时扫描，防止扫描速度太快被拦截

■

新增 Hunter资产测绘 导出模块，自动对接API接口将资产导出至 `hunterout.txt`

■

新增 Fofa资产测绘 导出模块，自动对接API接口将资产导出至 `fofaout.txt`

■

新增 ZoomEye资产测绘 导出模块，自动对接API接口将资产导出至 `zoomout.txt`

■

在Spring端点爆破的时候，新增过滤一些无效回显的页面，提高工作效率

■

对端点爆破字典进行优化，增加一些绕过语句，如果有补充欢迎提交

■

支持自动对Spring进行指纹识别

■

在漏洞利用模块，对错误进行输出为 `error.log`

■

支持使用带认证的HTTP代理节点，自动检测节点状态

■

由 `@13exp` 师傅友情制作GUI图形化版本

■

验证代理是否存活，并可以使用HTTP代理认证，支持使用HTTP/HTTPS代理所有流量

■

随机User-Agent请求头

■

解决SSL证书问题 (自签名证书请改成 `http://` 即可)

■

智能识别目标地址 (`example.com` 和`http://example.com/` 以及`http://example.com` 都不会报错)

**注明**

■

**本工具优化了使用者体验，不管是对单一URL扫描还是读取TXT进行批量扫描，`example.com` 和`http://example.com/` 以及`http://example.com` 都不会报错，程序会自行判断并识别**

■

**解决了SSL证书问题，可以对采用SSL证书的Spring Boot框架进行扫描（自签名证书请改成 `http://` 即可）**

■

**对于二级目录部署的Spring项目，直接给工具相应的路径就行了（比如 `example.com/test/` 这个路径部署了Spring项目，那直接将 `example.com/test/` 传参给工具就行了）**

**GUI图形化版本，由 `@13exp` 师傅友情制作，GUI地址：https://github.com/13exp/SpringBoot-Scan-GUI**

![GUI](https://mmbiz.qpic.cn/sz_mmbiz_png/l6gHYLEF4ibhbF74dP1gGqvMa5Bp0nUpF7gSoXfQJ6yMvPEKERFGolC5TfWSCKXpnMIVvibl1fJ0L62EDs4S605BJJm7VTZyVokmungLbZmHc/640?wx_fmt=png&from=appmsg)

注：因为本项目的 `vul.py` 和GUI项目均包含漏洞利用模块，杀软报毒和查杀为正常情况。如果觉得工具不错，师傅们可以点个Star哈哈~

---

04｜实战：一条命令，从测绘到收割

**安装Python依赖库**

```
pip install -r requirements.txt
```

如果pip安装速度慢，可以采用国内源进行安装：

```
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

**如何找到互联网上的Spring框架，ZoomEye语法如下：**

**Fofa语法如下：**

```
icon_hash="116323821"||body="Whitelabel Error Page"
```

**本工具的参数如下：**

```
# python3 SpringBoot-Scan.py
  ______                       __                      _______                        __
 /      \                     |  \                    |       \                      |  \
|  $$$$$$\  ______    ______   \$$ _______    ______  | $$$$$$$\  ______    ______  _| $$_
| $$___\$$ /      \  /      \ |  \|       \  /      \ | $$__/ $$ /      \  /      \|   $$ \
 \$$    \ |  $$$$$$\|  $$$$$$\| $$| $$$$$$$\|  $$$$$$\| $$    $$|  $$$$$$\|  $$$$$$\\$$$$$$
 _\$$$$$$\| $$  | $$| $$   \$$| $$| $$  | $$| $$  | $$| $$$$$$$\| $$  | $$| $$  | $$ | $$ __
|  \__| $$| $$__/ $$| $$      | $$| $$  | $$| $$__| $$| $$__/ $$| $$__/ $$| $$__/ $$ | $$|  \
 \$$    $$| $$    $$| $$      | $$| $$  | $$ \$$    $$| $$    $$ \$$    $$ \$$    $$  \$$  $$
  \$$$$$$ | $$$$$$$  \$$       \$$ \$$   \$$ _\$$$$$$$ \$$$$$$$   \$$$$$$   \$$$$$$    \$$$$
          | $$                              |  \__| $$
          | $$                               \$$    $$   [+] V2.7.2-2025年 欢度国庆佳节版
           \$$                                \$$$$$$    [+] 感谢一路上支持和关注我们的师傅
            ______
           /      \                                  +-------------------------------------+
          |  $$$$$$\  _______  ______   _______      + Version: 2.7.2                      +
          | $$___\$$ /       \|      \ |       \     + Author: 曾哥(@AabyssZG)             +
           \$$    \ |  $$$$$$$ \$$$$$$\| $$$$$$$\    + Whoami: https://github.com/AabyssZG +
           _\$$$$$$\| $$      /      $$| $$  | $$    +-------------------------------------+
          |  \__| $$| $$_____|  $$$$$$$| $$  | $$    + 多进程速度提升: Fkalis              +
           \$$    $$ \$$     \\$$    $$| $$  | $$    + Whoami: github.com/WingBy-Fkalis    +
            \$$$$$$   \$$$$$$$ \$$$$$$$ \$$   \$$    +-------------------------------------+

用法:
        对单一URL进行信息泄露扫描:         python3 SpringBoot-Scan.py -u http://example.com/
        读取目标TXT进行批量信息泄露扫描:   python3 SpringBoot-Scan.py -uf url.txt
        对单一URL进行漏洞扫描:             python3 SpringBoot-Scan.py -v http://example.com/
        读取目标TXT进行批量漏洞扫描：      python3 SpringBoot-Scan.py -vf url.txt
        扫描并下载SpringBoot敏感文件:      python3 SpringBoot-Scan.py -d http://example.com/
        读取目标TXT进行批量敏感文件扫描:   python3 SpringBoot-Scan.py -df url.txt
        使用HTTP代理并自动进行连通性测试:    python3 SpringBoot-Scan.py -p <代理IP:端口>
        从TXT文件中导入自定义HTTP头部:       python3 SpringBoot-Scan.py -t header.txt
        通过ZoomEye密钥进行API下载数据:      python3 SpringBoot-Scan.py -z <ZoomEye的API-KEY>
        通过Fofa密钥进行API下载数据:         python3 SpringBoot-Scan.py -f <Fofa的API-KEY>
        通过Hunter密钥进行API下载数据:       python3 SpringBoot-Scan.py -y <Hunter的API-KEY>
```

7 连实战场景

**① 通过 ZoomEye 进行Spring资产测绘**

本工具专门对接了 ZoomEye的API接口，使用API-KEY即可批量下载Spring的资产测绘数据：

```
python3 SpringBoot-Scan.py -z <ZoomEye的API-KEY>
```

![ZoomEye](https://mmbiz.qpic.cn/mmbiz_png/l6gHYLEF4ibiagsCicnskSsrIyPSg90WgjCq7kbPKdmtSvia5HVxyIqCxUBr5V7p6GiaBTx1F2QCEhx12yvTJM0FexjwDYvvJkg2iaFzCNibhpyG9A/640?wx_fmt=png&from=appmsg)

注：目前该模块已经支持自定义语法的资产测绘导出；资产测绘结束后，会把通过API下载的结果导出到 `zoomout.txt`，就可以使用其他参数进行操作啦

**② 通过 Fofa 进行Spring资产测绘**

本工具专门对接了 Fofa的API接口，使用API-KEY即可批量下载Spring的资产测绘数据：

```
python3 SpringBoot-Scan.py -f <Fofa的API-KEY>
```

![Fofa](https://mmbiz.qpic.cn/mmbiz_png/l6gHYLEF4ibjibruJdzDnH5MSQibUyZIEwVVDeAXAvHU7Il6QYtLLvfChUQ3WqEonqRickXkGc2fz3mZAqTLOCBE6Zn0EAlv8tayWsdBA39S7bs/640?wx_fmt=png&from=appmsg)

注：目前该模块已经支持自定义语法的资产测绘导出；资产测绘结束后，会把通过API下载的结果导出到 `fofaout.txt`，就可以使用其他参数进行操作啦

**③ 通过 Hunter鹰图 进行Spring资产测绘**

本工具专门对接了 鹰图的API接口，使用API-KEY即可批量下载Spring的资产测绘数据：

```
python3 SpringBoot-Scan.py -y <Hunter的API-KEY>
```

![Hunter](https://mmbiz.qpic.cn/mmbiz_png/l6gHYLEF4ibiaUk6AIZGfPr0xGibGMlYgcEkZq09Cibrs2q29aWZoRjcRZGAhSY9L9GTaBrWhYmJPfUATqPibhhZRGSYkfs6NDmT4jxSp1ibx8hiaM/640?wx_fmt=png&from=appmsg)

注：目前该模块已经支持自定义语法的资产测绘导出；资产测绘结束后，会把通过API下载的结果导出到 `hunterout.txt`，就可以使用其他参数进行操作啦

**④ 测试并使用代理和自定义HTTP头部**

测试并使用代理

```
python3 SpringBoot-Scan.py -p <代理IP:端口>
python3 SpringBoot-Scan.py -p <HTTP认证账...
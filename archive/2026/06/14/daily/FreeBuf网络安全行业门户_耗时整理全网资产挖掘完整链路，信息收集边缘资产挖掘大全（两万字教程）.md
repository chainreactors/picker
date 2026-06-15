---
title: 耗时整理全网资产挖掘完整链路，信息收集边缘资产挖掘大全（两万字教程）
url: https://www.freebuf.com/articles/web/486017.html
source: FreeBuf网络安全行业门户
date: 2026-06-14
fetch_date: 2026-06-15T07:09:33.427742
---

# 耗时整理全网资产挖掘完整链路，信息收集边缘资产挖掘大全（两万字教程）

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [培训站](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

![](https://image.3001.net/images/20260209/1770606290323007_4a7b566114624e94b90bd2fe14b98aab.png) ![](https://image.3001.net/images/20260401/1775023076_69ccb3e4192f3c60ed43b.png)

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

耗时整理全网资产挖掘完整链路，信息收集边缘资产挖掘大全（两万字教程）

* ![]()
* 关注

* [Web安全](https://www.freebuf.com/articles/web)

耗时整理全网资产挖掘完整链路，信息收集边缘资产挖掘大全（两万字教程）

2026-06-15 00:00:00

# 0x01 简介

红队实战中分散工具与碎片化收集思路效率低下，本文整理一套标准化资产挖掘完整链路，两万字覆盖企业股权备案、子域名测绘、IP 网段、CT 日志、JS 提取、Host 碰撞、Google Hacking、云存储桶枚举、深网泄露全流程。配套 Tscan、Subfinder、BucketHunter 等工具实操命令，聚焦影子资产、边缘隐蔽资产挖掘，剔除冗余淘汰手段，给出可直接落地的侦察流程，适配渗透测试、攻防演练、企业攻击面梳理学习。

# 0x02 正文详情

## （一）主域名&企业信息收集

### 1.1.企业信息查询

如果客户要求去收集子公司或母公司，需要跟客户约定好持股比例，去平台上通过股权穿透图先把子公司名称、域名收集一下。`这个目前没有很好用的工具，通过人工更靠谱一下，如果组织比较多使用Tscan、ENscan，是目前比较推荐的。

Tscan

```
配置站点的cookie和key，输入公司名即可进行基本信息收集，这个还是比较方便的
# https://github.com/TideSec/TscanPlus/releases
```

EnScan\_GO
下载后需要配置API、cookie后使用，这里给一下我常用的命令，如果报错可以微调命令，每个人的环境和配置文件都不一样不用完全照搬，这里我们目标是一些基础信息不用太过关注。

```
./enscan-v2.0.5-darwin-arm64 -n 北京金山云网络技术有限公司 -field icp,weibo,wechat,app,job,wx_app,copyright,supplier -type tyc,chinaz -timeout 30 --hold --supplier --branch
# 下载链接：https://github.com/wgpsec/ENScan_GO
```

### 1.2.ICP备案查主域名

```
1.1.企业信息查询”已经查询到了公司名和一部分备案号信息，这时候我们就访问时效性最高的工信部ICP，直接查询`公司名`可获取当前公司备案的主域名，需要点击`详情`。`时效性高是因为ICP备案会定期变更一部分，工信部作为数据来源是第一手信息。
#官方地址：https://beian.miit.gov.cn/
#批量查询地址：https://www.hacktwohub.com/wp-custom-dev/icp_app/icp
```

### 1.3.WHOIS 历史与反查

通过域名的历史注册信息（注册人邮箱、电话、姓名），反查该人名下的所有其他域名，找到企业被淘汰的"影子域名"，`这种域名运气好还能测绘到资产，再不济在后面的host碰撞会用到。

1. 查询历史whois

```
企业的whois信息会因为各种原因进行变更，有时候会变更关键的（注册人邮箱、电话、姓名），通常搜索这些信息可以获取到企业注册过但是没备案的域名。这里推荐用微步，因为它隐藏了不重要的变更。
# https://x.threatbook.com/
```

2. 反查关联域名

```
上一步获取到了whois中的（注册人邮箱、电话、姓名）信息后，我们可以通过这些信息反查注册过的域名，这些域名有的还没过期但是不在企业备案中，可能企业自己也忘记了。
#https://x.threatbook.com/
```

## （二）子域名&ip收集

主域名&企业信息收集”完成后，我们已经拿到了企业基本信息，接下来我们就基于这些信息，使用各种渠道扩展这些信息。

### 2.1.测绘平台被动收集

注：被动收集要工具和测绘平台结合使用，1是不能完全相信工具输出，2是接口调用接口可能因为程序原因缺失结果，而大部分资产都在这一步产出所以要尽可能覆盖全。

#### 2.1.1.工具调用接口

1.Tscan多平台付费
这里把Tscan放到第一位的原因是它能够快速收集我们想要的信息，当然我们要更详细收集时还是要用到下面的资产测绘平台语法，不是要打攻防的不要太详细非常耗时。

1. 配置好各个平台的API
   这里尽量配置全一些，虽然资产多不了多少，但是多出来的可能就是关键的入口点`,这里要通过ICP备案、主域名、证书绑定域名，查询资产信息
2. 收集域名、IP信息（ICP备案）
   输入我们在“一、主域名&企业信息收集”获取到的主ICP备案号，字段选择“备案”，`一定要是主备案号，子备案号会漏下，记得勾选右边的资产测绘平台，我这里演示所以没有全部勾选，可以看到通过ICP备案号收集到了很多信息

```
下载链接：https://github.com/TideSec/TscanPlus/releases
```

3. 收集子域名、IP（主域名）
   输入我们在“一、主域名&企业信息收集”获取到的主域名，字段选“域名”，`记得勾选右边的资产测绘平台，我这里演示所以没有全部勾选。
4. 收集子域名、IP（证书）
   输入我们在“一、主域名&企业信息收集”获取到的主域名，字段选择“证书”，记得勾选右边的资产测绘平台，我这里演示所以没有全部勾选。

注：部分站点会使用通配符证书，另外平台在证书字段上的匹配也可能带有模糊性。所以我们查询app.com.cn会匹配上abcdefapp.com.cn这种资产，这种不是目标资产，所以查询完要人工筛选一下。

2.subfinder多平台付费

```
0. subfinder配置文件位置运行以下命令可以看到
./subfinder -version
1. 配置（bevigil、censys、chaos、digitalyama、dnsdumpster、fofa、github、hunter、intelx、leakix、netlas、quake、rsecloud、shodan、zoomeyeapi）的APIkey，使用全量收集工具进行收集
2. 这里列一下我使用的命令
./subfinder -dL domains.txt -rl 20 -all -json -o results.json
# 下载链接：https://github.com/projectdiscovery/subfinder/releases
```

#### 2.1.2.资产测绘平台

1.域名查找

```
# Hunter domain.suffix="app.com.cn"
# Quake domain:"app.com.cn"
# fofa
host="talentsec.cn"
domain="talentsec.cn"
```

2.ICP备案

```
# Hunter icp.number="备案号"
# Quake icp:"备案号"
# fofa
icp="沪ICP备20019790号"
```

3.icon\_hash

```
首先根据在测绘平台收集的结果，把icon的下载路径或测绘平台的icon_hash保存下来，后期收集边缘资产用就行
# Hunter（使用favicon的MD5值）
web.icon="MD5"
# Quake（使用favicon的MD5值）
favicon:"MD5"
# fofa（使用mmh3算法）
icon_hash="585442251"
```

4. title&body查询

```
title
# Hunter web.title="标题"
# Quake title:"标题"
# fofa
title="螣龙安科"||title="螣龙安科，专注于新一代攻击面管理"
```

```
 body注意body查询不能用title的关键字，这样会出现重复结果的问题
# Hunter web.body="内容"
# Quake body:"内容"
# fofa
body="螣龙安科是国内新一代主动安全领域的专精特新企业，致力于为客户提供专业的标准化产品与解决方案。"||body="螣龙安科，螣龙天眼，螣龙天眼ASM，螣龙攻击面管理系统"
```

### 2.2.爆破子域名

原理：搜索引擎爬虫的抓取、证书透明度日志的同步、威胁情报库的更新，都是有时间差的。如果目标企业刚刚配好了一个新的子域名，此时所有的被动接口大概率都查不到它，但通过字典爆破，可以实时地将其解析出来。

1.Findomain
0. Findomain的config需要自行下载加载，就是使用编译好的默认配置

```
https://github.com/Findomain/Findomain/tree/master/config_examples
```

1. 将我们在“一、主域名&企业信息收集”获取到的主域名存入domains.txt，配置Apikey，Findomain的配置文件可以运行，字典可以用Tscan的字典
2. 命令

```
./findomain --file domains.txt --wordlist subnames-9.5w.txt --config config.example.yml --resolved --output
# 下载链接：https://github.com/Findomain/Findomain
```

2.OneForAll
0. OneForAll配置文件在当前目录“config/api.py”中配置

1. 将我们在“一、主域名&企业信息收集”获取到的主域名存入domains.txt，配置好Apikey，OneForAll支持接口获取+域名爆破，这里主要用它的字典爆破功能。
2. 命令

```
python oneforall.py --targets ./domains.txt --wordlist subnames-9.5w.txt --brute True run
```

注：需要注意的是python的工具尽量进入虚拟环境运行，因为很多工具对于依赖库的版本要求不一样，会出现冲突的情况，虚拟环境安装依赖库就能每款工具独立环境。

```
# 下载链接：https://github.com/shmilylty/OneForAll
```

### 2.3.证书透明度查询

原理：为了防止CA（证书颁发机构）滥发伪造的SSL/TLS证书，对于主流公开信任CA签发、被现代浏览器信任的TLS证书，通常需要满足CT相关策略，因此很多公网子域名会在CT日志中留下记录。这意味着，只要目标企业为它的某个子域名申请了HTTPS证书，这个子域名就不可避免地被永久公开记录在了CT日志里。

1.crt查询

```
# https://crt.sh/?q=talentsec.cn
```

调用证书绑定接口直接查询主域名，可以获取证书历史绑定的域名信息
2.sslmate查询

```
# https://sslmate.com/ct_search_api/
```

调用证书绑定接口直接查询主域名，可以获取证书历史绑定的域名信息。

### 2.4.威胁情报查询

原理：威胁情报平台每天会处理全球海量的DNS请求、恶意样本外联请求和安全设备日志。在这些日志中，记录了大量的域名解析活动。通过查询威胁情报平台，可以作为补充数据源，帮助发现一部分常规手段不易直接发现的子域名和关联基础设施，甚至能查出一些通过常规字典爆破或搜索引擎查不到的深度隐蔽子域名

1.微步威胁情报需付费

```
# 微步情报社区，https://x.threatbook.cn/搜索主域名可以获取到子域名信息
```

2.奇安信威胁情报需要登录

```
# 奇安信 威胁情报中心 https://ti.qianxin.com/
```

搜索主域名可以获取到CNAME记录和关联域名，里面有子域名
搜索主域名点击关联域名模块也可以获取子域名信息
3.360威胁情报需要登录

```
# 360 威胁情报中心 https://ti.360.cn/domain/talentsec.cn
```

搜索主域名可以获取到对应的子域名信息

### 2.5.搜索引擎查询

```
# https://www.google.com
```

在资产测绘和渗透测试中，利用 Google 搜索引擎（这种技术被称为 Google Hacking 或 Google Dorking ）查询目标网站，是一项极其关键的“被动信息收集”技术。
site收集，通过site:app.com.cn -www搜索指定的域名相关的网页排除www站点，google api比较麻烦可以用插件Google SERP Scrapper抓取结果

### 2.6.DNS历史记录查询需要会员

很多业务在刚上线测试时，或者是早期阶段，往往是直接将域名解析到服务器真实物理IP上的，后来才接入的CDN。通过历史DNS记录，可以找到这些曾经存在过的旧IP或旧域名。这类“影子资产”通常无人维护、缺乏最新的安全补丁、甚至存在弱口令和未授权访问，是红队打点的绝佳突破口。

1.dnsdumpster

```
# https://dnsdumpster.com
```

直接搜索主域名or子域名去查找DNS历史解析记录，以找到历史配置过的域名和ip
2.viewdns

```
# https://viewdns.info/iphistory/?domain=talentsec.cn
```

3.securitytrails

```
# https://securitytrails.com/domain/talentsec.cn/history/a
```

### 2.7.IP C段提取（需排除CDN）

在企业实际运维中，除了对外服务的官网会绑定域名，还有大量的内部系统、基础设施是绝对不会绑定域名的，它们只通过IP访问。

```
# 路线选择一种即可
```

#### 2.7.1.路线一（ASN自治系统号收集）

此方法只针对超大型企业，因为超大型企业通常会注册自己的ASN，ASN下挂载的所有IP段都是企业自有资产，比C段聚合更精准、覆盖更全。
确认企业的ASN号
我们需要找到企业的英文名称，可以在google搜索企业名称，wiki和百度百科都会显示，访问https://bgp.he.net/搜索企业英文名即可。注意因为模糊查询只有完全匹配的才是，不要收集歪了

```
# https://bgp.he.net/
```

如果没有找到企业英文名称，可以找一个确认是企业资产的IP去反查ASN号

```
命令一：whois 103.92.88.7 | grep -i "origin\|netname\|descr"
命令二：curl https://ipinfo.io/103.92.88.7 | jq '.org'
```

2.获取ASN下IP段
在网站直接搜索ASN自治系统号，点击Prefixes v4即可，也可以通过命令收集。

```
# https://bgp.he.net/
# whois -h whois.radb.net -- '-i origin AS38378' | grep -E "^route|^descr|^origin"
```

需要注意的是可以看到一个ASN号下可以存在多个组织，如果客户只是让你收集博世中国，那博世家电的IP段就要剔除掉。

#### 2.7.2.路线二（数据合并）

```
# https://github.com/EdgeSecurityTeam/Eeyes
```

1. 域名汇总C段
   输入之前步骤汇总收集到的子域名，通过./Eeyes-darwin -l domain.txt提取C段资产
   支持排除掉CDN资产，注意IP出现次数需要超过3次,次数少容易收集歪。
2. IP汇总C段
   然后使用Tscan，输入之前步骤汇总收集到的IP（去重后），提取出现次数3以上的C段地址。

### 2.8.IP资产收集

```
# 路线选择一种即可
```

#### 2.8.1.路线一（测绘平台）

路线一属于信息来源教单一的原因所以需要组合收集，路线二可以直接调用现成的资产测绘平台能力，这里举例我们直接将C段给到空间测绘，列出存活的IP资产，并且可以看到反查域名、归属等信息。
推荐使用：

```
# hunter https://hunter.qianxin.com/
# quake https://quake.360.net/quake/#/
# fofa https://fofa.info/
# 微步 https://x.threatbook.com/v5/survey?q=ip%3D%22122.194.76.0%2F24%22
```

#### 2.8.2.路线二（工具协同）

1.C段...
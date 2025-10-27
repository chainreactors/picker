---
title: 冠军Writeup大放送 | DataCon2022域名体系安全赛道之“NDNS”战队
url: https://mp.weixin.qq.com/s?__biz=MzU5Njg1NzMyNw==&mid=2247485903&idx=1&sn=d553dc6150656ae0717c1bad5086221e&chksm=fe5d114fc92a9859e0d8466ab33dcf3c4a9f10ced9e3d28f0b012d330f40a572f81c4af0b38c&scene=58&subscene=0#rd
source: DataCon大数据安全分析比赛
date: 2023-01-14
fetch_date: 2025-10-04T03:53:36.787615
---

# 冠军Writeup大放送 | DataCon2022域名体系安全赛道之“NDNS”战队

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RicNZQMn3FU4O60t1gdtZicySPNxKj6UUTI7Oc0HEMerIJ7IbCfjm232VaQ6pIia1j9pMInJBGOhkBAMay8SsNgyA/0?wx_fmt=jpeg)

# 冠军Writeup大放送 | DataCon2022域名体系安全赛道之“NDNS”战队

原创

NDNS战队

DataCon大数据安全分析竞赛

![](https://mmbiz.qpic.cn/mmbiz_png/RicNZQMn3FU6Xd3SguPLxsycckicrXFrxCDEmulicRU8ciaYchHknhbMv6eupxcjDvicj4v0wib8DEye3jr5U4M7WeJA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

由奇安信集团、清华大学网络研究院、蚂蚁集团、腾讯安全大数据实验室、Coremail论客主办的DataCon2022大数据安全分析竞赛线上赛和决赛已圆满落幕，五大赛道第一名也已各归其主。今天要为大家分享的是**域名体系安全赛道**排名第一的****NDNS战队****writeup。

来自国防科技大学DNSLab的NDNS战队组建于2021年，指导老师是许成喜老师。NDNS战队依托国防科技大学网络空间测绘科研团队，主要成员为国防科技大学在读硕博士研究生，关注互联网基础设施安全及测量、网络黑产检测等领域的前沿技术与研究。成员们主要研究方向为DNS安全、黑灰产检测及异常检测、网络空间测绘、机器学习、数据挖掘等。NDNS战队曾获DataCon2021 域名体系安全第二名、2021强网杯人工智能挑战赛口令猜解第二名。

![](https://mmbiz.qpic.cn/mmbiz_png/RicNZQMn3FU4O60t1gdtZicySPNxKj6UUT69OiczDA0cFJOVTuwqnO9ibnF5szFBzliaC1yXrXk2fRV2F7ggTMLMa8Q/640?wx_fmt=png)

**[温馨提示：本文篇幅较长
欢迎收藏转发，随时浏览查看****]**

***【赛题要求**】*****

本次比赛域名体系安全中设置了两个题目，**域名分类和域名接管。**

**域名分类：**选手需要根据域名的解析规律和访问规律识别并分类出 CDN 及其他种类域名。选手需要了解 DNS 的基础知识和常见域名种类的特点，并能够推断总结出其解析和访问规律，据此实现域名分类识别。

**域名接管：**选手需要通过在既定靶场中通过域名接管、DNS 污染等攻击方式，在靶场中接管指定的域名从而获取靶场中的 FLAG。

**第一部分** ****域名分类****

**一、背景知识**

域名是网络攻击中必不可少的数字资源，基于域名的安全风险分析研究可以快速的发现和阻断威胁活动。在域名体系安全研究中，针对不同的域名应用场景，安全研究人员对域名进行分类，以便更好的对特定分类域名的行为特征进行分析，也有利于过滤非目标的流量数据。赛题中的分类主要包括：

**1. CDN 域名**

CDN 全称为内容分发网络，其目的是解决因分布、带宽、服务器性能带来的访问延迟问题，常用于站点加速、点播、直播等场景。可以使用户可就近取得所需内容，解决 Internet 网络拥挤的状况，提高用户访问网站的响应速度和成功率。

CDN 域名指提供 CDN 服务厂商的域名。在实现上，CDN 通常使用域名系统中的 CNAME 记录，将用户的域名 CNAME 到服务商的域名，当用户向源站发起请求时，DNS 服务器解析源站域名时会发现有 CNMAE 记录，这时 DNS 服务器会向 CNAME 域名发起请求，请求会被调度至加速节点的域名。

**2. 动态域名**

域名的映射关系一般是预先配置好的，但对于一些没有固定 IP 地址场景是无法进行配置。而动态域名可以将任意变换的 IP 地址绑定一个固定的域名，实现了 IP 变换场景下的域名 IP 映射。实现方式通常是利用客户端的软件将本机的 IP 发送至动态域名解析服务器或者某些路由器直接支持动态域名的配置。目前国内支持动态域名的厂商包括花生壳、3322、dnspod、aliyun 以及 huaweicloud 等。

**3. 隐藏类型域名**

根据提示，我们推断赛题中的隐藏类型域名为 GFW 的监管域名。

**4. Sinkhole**

当发现恶意软件中所使用的域名后，为了避免后续感染恶意软件的受害者再受到攻击，研究者通常将恶意域名接管至特定的地址，该地址被称为 sinkhole，常见的接管方式是修改恶意软件域名的 NS 记录，将其设置为研究者自己控制的某个 DNS 服务器。

**5. Domain Parking**

域名停放是将暂时不用的域名或者待出售的域名，托管至域名停放服务商处，由服务商展示统一的广告或者售卖页面，以赚取广告流量费用或者售卖。

**6. Webhosting（免费建站）**

为方便普通用户部署 web 站点，服务商推出方便 web 托管服务器，可以为用户提供子域名及主机资源，常见的服务商包括 000Webhost、Alwaysdata、freewha、ProFreeHost、FASTLY、Wix.com、SQUARESPACE 等。

**7. p2p**

对 p2p 不太了解，这里认为是 p2p 网络中所使用的域名。

**8. FastFlux**

FastFlux 是恶意软件中为了躲避检测而使用的一种技术，最早发现于 2006 年的 storm worm。Flux Fast 最大的特征之一在于频繁改变其域名、IP 地址和名称服务器。

**二、域名特性分析及判定指标**

根据对每种类型域名的应用场景和使用特性进行分析，总结其解析行为特征，因为比赛中仅找出了 5 种类型的域名，且后动态域名的效果并不好。对于为找出的 3 种类型域名的分析可能有待矫正。下图展示了我们所分析和使用的指标，绿色对号表示我们最终使用的指标。

![](https://mmbiz.qpic.cn/mmbiz_png/RicNZQMn3FU4O60t1gdtZicySPNxKj6UUTUeiamQLFvFdibwfcr6Wa6ial5fkHk0icRWOVnVj1w5C4cNc4qVWXsL67wA/640?wx_fmt=png)

****●**CDN 域名**    ○ 具有大量的 CNAME 记录，服务商的 SLD 下具有大量的 FQDN，IP 数量多，地理分布广泛（这个特征再比赛数据中并不明显）
    ○ 判定指标：SLD 的 CNAME 记录数大于 N（100），解析 IP 地理位置数量大于 M（0/2）

****●****隐藏类型域名
    ○ 推测为监管域名，根据已有研究[1]，监管域名的响应记录由两个特性
        ■ 响应 IP 的 AS 信息比较集中，常见为 Google，Twitter，Facebook 和 Dropbox
           ■ 响应 IP 的数量有限
    ○ 判定指标：IP ASO 为以上四种，且每个 IP 解析域名数量大于 14W。

****●****动态域名
    ○ 具有较多子域名，每个子域名解析的 IP 不固定

****●****Domain Parking
    ○ parking 服务商较集中，一个 IP 解析大量域名，且统一服务商的对每个域名的解析策略是一致的，如对任何 parked 域名响应 12 个IP
    ○ 判定指标：单个 IP 解析域名大于 N，为特定的 parking 服务商，且解析策略一致

****●****webhosting
    ○ 服务商较集中，具有大量子域名，单一 IP 解析大量的 FQDN，取决于服务商大小，IP 数量有限
    ○ 判定指标：单个 IP 解析域名大于 N，特定的 hosting 服务商

****●****sinkhole（未发现）
    ○ sinkhole 的 IP 数量有限，可能一个 IP 解析大量的恶意域名

****●****p2p（未发现）
    ○ 单一域名解析多个 IP 地址

****●****fastflux（未发现）
    ○ 单一域名解析大量 IP 地址，同时每个 IP 上解析量分布是均匀的

**三、赛题解答**

**数据处理**

1. 遍历所有 CNAME 记录中的 SLD，统计 SLD 对应的 CNAME 解析记录数量。

```
import csvimport osSLD_Ccount = {}
i=0file_names = os.listdir('./datacon_cdn_basic')for file_name in file_names:    i+=1    file_path = os.path.join('./datacon_cdn_basic',file_name)    print('Processing with '+ str(i) +' file!')    with open(file_path, encoding='utf-8-sig') as f:        f_csv = csv.reader(f)        #headers = next(f_csv)   #headers:['sld_md5', 'all_md5_fqdn', 'request_cnt', 'rtype', 'all_md5_rdata', 'country_code', 'country_name', 'region_name', 'asn_sort']        #['86f066f08908de0c617243cb33081050', '2ddfe6b1ebd12b3d1807eff0274d883c.86f066f08908de0c617243cb33081050', '1', '5', 'ccd4d6df14af7f4215db6b77945fc02a.95074d472f19c7108ee72233cd65f543', 'null', 'null', 'null', '0']        for row in f_csv:            if row[3]=='5':                if row[4]:                    sld = row[4].split('.')[-1]                    if sld in SLD_Ccount:                        SLD_Ccount[sld] += 1                    else:                        SLD_Ccount[sld] = 1
SLD_Ccount_sorted = dict(sorted(SLD_Ccount.items(), key=lambda x: x[1], reverse=True))
file1 = open('./mydata/SLD_Ccount_sorted.csv', 'w')writer = csv.writer(file1)count_all = 0for k,v in SLD_Ccount_sorted.items():    writer.writerow([k,v])    count_all += vprint(count_all)  print('Success!')#共 29581826 条 CNAME 记录
```

2. 统计 SLD 的所有 FQDN 数量。

```
import csvimport os
CDN_list1 = []CDN_fqdn_count = {}fqdn_count = {}
with open('./mydata/SLD_Ccount_sorted.csv', encoding='utf-8-sig') as f:    f_csv = csv.reader(f)    for row in f_csv:        #if int(row[1]) >= 397:        CDN_list1.append(row[0])
for sld in CDN_list1:    CDN_fqdn_count[sld] = 0
i=0file_names = os.listdir('./datacon_cdn_basic')for file_name in file_names:    i+=1    file_path = os.path.join('./datacon_cdn_basic',file_name)    print('Processing with '+ str(i) +' file!')    with open(file_path, encoding='utf-8-sig') as f:        f_csv = csv.reader(f)        for row in f_csv:            sld = row[0]            if sld in CDN_list1:                fqdn = row[1]                if fqdn in fqdn_count:                    fqdn_count[fqdn] += 1                else:                    fqdn_count[fqdn] = 1                    CDN_fqdn_count[sld] += 1
CDN_fqdn_count_sorted = dict(sorted(CDN_fqdn_count.items(), key=lambda x: x[1], reverse=True))
file1 = open('./mydata/CDN_fqdn_count_sorted.csv', 'w')writer = csv.writer(file1)count_all = 0for k,v in CDN_fqdn_count_sorted.items():    writer.writerow([k,v])    count_all += vprint(count_all)  print('Success!')
```

3. 统计 FQDN 的解析 IP 分布，即：统计 FQDN 对应的 A 记录地区分布及数量。

```
import csvimport os
CDN_list1 = []fqdn_region_list = {}fqdn_region_count = {}
with open('./mydata/SLD_Ccount_sorted.csv', encoding='utf-8-sig') as f:    f_csv = csv.reader(f)    for row in f_csv:        CDN_list1.append(row[0])#print(CDN_list1)i=0file_names = os.listdir('./datacon_cdn_basic')for file_name in file_names:    i+=1    file_path = os.path.join('./datacon_cdn_basic',file_name)    print('Processing with '+ str(i) +' file!')    with open(file_path, encoding='utf-8-sig') as k:        k_csv = csv.reader(k)        for row in k_csv:            if row[3]=='1':                sld = row[0]                if sld in CDN_list1:                    fqdn = row[1]                    region = row[7]                    if fqdn in fqdn_region_list:                        if region in fqdn_region_list[fqdn]:                            pass                        else:                            fqdn_region_list[fqdn].append(region)                    else:                        fqdn_region_list[fqdn] = [region]
for k,v in fqdn_region_list.items():    fqdn_region_count[k]=len(v)fqdn_region_count_sorted = dict(sorted(fqdn_region_count.items(), key=lambda x: x[1], reverse=True))
file1 = open('./mydata/fqdn_region_count_sorted.csv', 'w')writer = csv.writer(file1)for k,v in fqdn_region_count_sorted.items():    writer.writerow([k,v])  print('Success!')
```

4. 将 FQDN 的地区分布情况进行合并，得到 SLD 的地区分布情况及数量。

```
import csvsld_region_list = {}sld_region_count = {}for k,v in fqdn_region_list.items():    sld = k.split('.')[-1]    if sld in sld_region_list:        for _ in v:            if _ in sld_region_list[sld]:                pass            else:                sld_region_list[sld].append(_)    else:        sld_region_list[sld] = vfor k,v in sld_region_list.items():    sld_region_count[k]=len(v)   sld...
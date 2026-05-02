---
title: 2026第四届全国数据安全职业技能竞赛暨第四届全国安防行业职业技能竞赛“美亚柏科杯”数据安全管理员职业技能竞赛总决赛第一批18号上午wp
url: https://mp.weixin.qq.com/s/GeUTQeRsonj15IAKzBS-tg
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:57:37.284613
---

# 2026第四届全国数据安全职业技能竞赛暨第四届全国安防行业职业技能竞赛“美亚柏科杯”数据安全管理员职业技能竞赛总决赛第一批18号上午wp

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5wuTuicCVRBH4Ric2KJreTekfgiaMf81sjqGfdVBOpJrE4JD3PTibToxQHQ2rjwhp0tu5IMzOYdgcduCATx9ez8sesBEaCkGJaQtnqIJiaXFGWibw/0?wx_fmt=jpeg)

# 2026第四届全国数据安全职业技能竞赛暨第四届全国安防行业职业技能竞赛“美亚柏科杯”数据安全管理员职业技能竞赛总决赛第一批18号上午wp

原创

一把梭安全
一把梭安全

一把梭安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

数据安全

数据备份(50分)

题目描述：某写字楼使用了一套“SecuAccess-X”门禁系统。管理员在系统升级前，会定期通过客户端导出配置备份文件，用于灾难恢复。你从一台旧电脑中获取到了一份从该系统导出的门禁配置备份文件 backup.acfg，以及一份旧版本的“SecuAccess-X 管理客户端”程序 SecuAccessClient。据说这份备份中包含了一张超级管理员门禁卡的信息，它拥有对所有门区的完全开门权限。 你的任务是通过逆向分析客户端程序以及备份文件格式，从中找到这张超级管理员卡的卡号，并提交该卡号。

题目给了两个文件：

`SecuAccessClient
backup.acfg`

目标是逆向客户端程序，分析 backup.acfg 备份格式，找出拥有所有门区权限的超级管理员卡号。

**1. 基本分析**

先把 SecuAccessClient 放进 IDA。程序很小，是一个命令行程序，入口逻辑集中在 main，运行参数格式也能从字符串看到：

`Usage: %s <backup.acfg>`

说明程序会读取并解析备份文件。

在字符串里还能看到：

```
Record #%d loaded. Level=%s, card_id=%d, Zones=%d, ValidDays=%dSpecial record detected.Record %u CRC16 mismatch. (maybe corrupted)
```

可以判断备份文件里存的是多条门禁卡记录，每条记录包含 Level、card\_id、Zones、有效期等字段。

**2. 文件头格式**

反编译 main 后，可以看到程序首先读取 0x20 字节文件头：

```
fread(&header, 0x20, 1, fp);
```

并检查：

```
magic == 0x47464341version == 0x0102header_size == 0x20
```

0x47464341 小端对应字符串：

```
ACFG
```

实际解析 backup.acfg 文件头：

```
magic       = ACFGversion     = 0x0102header_size = 32record_cnt  = 4
```

文件总大小为 108 字节，结构正好是：

```
32 字节 header4 条记录，每条 18 字节4 字节 global_crc32
```

每条记录由：

```
16 字节加密数据2 字节 CRC16
```

组成。

**3. 记录解密逻辑**

IDA 中关键代码位于记录读取循环附近：

```
14bc  lea rbx, key_2741...15a0  ; 先把 16 字节记录倒序15c0  ; 再与 key 逐字节 xor
```

从程序数据段取出密钥：

```
13 57 9B DF 24 68 AC F0 11 22 33 44 55 66 77 88
```

因此单条记录解密逻辑为：

```
plain[i] = encrypted[15 - i] ^ key[i]
```

程序随后对解密后的 16 字节数据做 CRC16 校验，算法为：

```
poly      = 0xA001init      = 0xFFFFfinal xor = 0x1234
```

EXP

```
import struct
data = open("backup.acfg", "rb").read()
key = bytes.fromhex("13 57 9B DF 24 68 AC F0 11 22 33 44 55 66 77 88")
def crc16(buf):    v = 0xffff    for b in buf:        v ^= b        for _ in range(8):            if v & 1:                v = (v >> 1) ^ 0xA001            else:                v >>= 1            v &= 0xffff    return (v ^ 0x1234) & 0xffff
record_count = struct.unpack_from("<I", data, 8)[0]
for i in range(record_count):    off = 32 + i * 18    enc = data[off:off + 16]    stored_crc = struct.unpack_from("<H", data, off + 16)[0]
    plain = bytes(k ^ b for k, b in zip(key, enc[::-1]))    calc_crc = crc16(plain)
    card_id, level, zones, reserved, start, end = struct.unpack("<IBBHII", plain)
    print(i, stored_crc == calc_crc, card_id, level, hex(zones), reserved)
```

得到 4 条记录：

```
record 0:card_id = 10000001level   = 1zones   = 0x03
record 1:card_id = 20000001level   = 0zones   = 0x01
record 2:card_id = 30000001level   = 2zones   = 0x0f
record 3:card_id = 88886689level   = 3zones   = 0xff
```

其中 zones=0xff 表示 8 个门区权限全开，且 level=3 走到了程序里的 special record 分支：

```
if (level == 3) {    if ((zones + 1) == 0) {        Special record detected;    }}
```

也就是 zones == 0xff 时会被识别为特殊记录。

答案 88886689

数据隐藏(40分)

题目描述：某组织内部人员利用视频容器特性，将包含 KEY\_PACKET\_SIG 信息的机密图片（png格式）嵌入到一段视频中，以逃避内容审查。请从该视频中提取隐藏的图片，并找到图片中的KEY\_PACKET\_SIG 值作为答案提交。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5wuTuicCVRBFvTFOEyqvZUiaicG3H47VNpchwVA7X5oRhyzzciatHAB2VA5o4b2Fqiaa4ibp7vWtCMowZGBeI7AGWJWaGiakblyQoj5yOZL9E3pSxo/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5wuTuicCVRBGdOUdHyP4hyvg8eRB3bmpVdzOjeUZaV1QEpFpa0mNPJPzXDXN3FRBfM7FC7ibr9q67SPH5icS5jxPSRfWxppEKavgl7shRDjDak/640?wx_fmt=png&from=appmsg)

答案 5589-yrq3vcf-43215

# 数据分析

## 数据恢复加工

【考题1】数据恢复 某公司职员在处理公司业务信息的时候，不小心误删除了一些关键的数据，但好在可以通过技术手段恢复出来。请通过分析硬盘文件，恢复出误删除的数据，并提交提交序号为5的表格中第239行第5列的内容。 【答案标准】 若序号为5的表格中第239行第5列的内容为555，则最终提交答案为：555

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5wuTuicCVRBHtDaW8xib69KLghZjiaNoOXLSUTeneCEkUzmmFxXJS6sSkHKbyAiabVUVY24MIMot2QOQEtNy3rmsSicWfwUCw2JRXoxibP4icSPJak/640?wx_fmt=png&from=appmsg)

答案 31579.32

【考题2】数据统计 公司运维人员发现大部分员工的用户名存在重复的情况，不便于工作上的沟通。请通过技术手段，统计出所有表格中重复次数最高的用户名及其数量，用“/”拼接后提交。 【答案标准】 若所有表格中，重复次数最多的用户名为aaa，重复次数为50次，则最终提交答案为：aaa/50

![](https://mmbiz.qpic.cn/mmbiz_png/5wuTuicCVRBHvRbqgy4sFX7YDQ1icqJataQKfE23MpcYnEicjjdQXQZSvs6TFDxH90V2XuAklgIgP1uibYaib7uj12sntC4D8whJNEbNH2C5CzHQ/640?wx_fmt=png&from=appmsg)

把所有文件的用户名都放在一个表里面

![](https://mmbiz.qpic.cn/mmbiz_png/5wuTuicCVRBFSicOBQBahq22nWRha3OJotppZOLDdVDozfG3dKzg1TMyjCgm1HwDxp7w7PpLCfwpAXtgKFFWnP0VxUl0nM5lu8og14dCr3XwU/640?wx_fmt=png&from=appmsg)

答案 coolbird/23

【考题3】分类分级 请依据公司数据分类分级标准，对恢复出来的数据进行分类分级处理(`数据分类分级标准.pdf`)，并统计其中级别为 L4的数据数量，将L4级别的数据数量作为答案提交。 【答案标准】 若L4级别的数据有10000条，则最终提交答案为：10000

![](https://mmbiz.qpic.cn/mmbiz_png/5wuTuicCVRBEmLibV2MNuLY45tNqqL147k4PuUOwWVqE1dYsErxYqJYwSAcZbdd7NmCfUUfpoMADSTxDdD8BqyQ3OzKjcIGtvw7icNfPxuqvpU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/5wuTuicCVRBGmbkJzwoibZGhM2ZUXRIUVaOqQib9pTibk4t3wM9VMB7D4IRBmBPTISjdXURHg1tL7ohMPLhwawADibpw5y6XRA6YNusRa7ROnCLs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/5wuTuicCVRBGsgkPFAG99Ges7VibesDzZ3ZduFXVQP6KjNVH5ic1anfmMQohxGEXk8HsH1KY2e2RNNruQppsfuN89SNa5Tx78WKtzsibVzHOfgs/640?wx_fmt=jpeg)

答案 4500

## 数据审计

【题目1】时间核验 监控摄像头会自动保存视频，并生成时间戳文件（timestamps.csv）。请选手根据题目提供的视频文件及对应的时间戳文件，对视频数据进行时间一致性分析。需要判断视频内容所反映的时间信息是否与其自动保存的时间戳匹配，找出存在时间不一致的视频文件，对其首字母按ASCII表排序后，使用""\_""进行拼接后，作为答案提交。 【答案标准】 若时间不一致的视频文件为9zasDS.mp4,Easq12.mp4,eaWQ1.mp4，则答案提交为9zasDS.mp4\_Easq12.mp4\_eaWQ1.mp4

这一题思路很简单写python脚本根据视频文件的创建时间或者修改时间判断是否匹配

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5wuTuicCVRBFLKeQezvPjL1RDQVLxHKGXEk0MHnGhyHy4FkjvcZBBI20neR8WH5ukKRMoI6ExZw559coeKN2HcRbcyYBnGOTia2BeFfd8RICc/640?wx_fmt=png&from=appmsg)

答案 BsqrC.mp4\_IGXFg.mp4\_heFCP.mp4\_xDD0m.mp4

【题目2】指纹提取 系统在视频文件的元数据中记录了视频拍摄设备的摄像头型号信息。请选手对提供的视频文件进行分析，提取其中的摄像机型号，并统计每种型号对应的视频数量，并作为答案提交。 注：型号共四种（SentinelCam-IPC200、SafeLens-2204F、VigilEye-Pro4K、IronView-2CD110） 【答案标准】 若SentinelCam-IPC200型号的视频有1个，SafeLens-2204F型号的视频有2个，VigilEye-Pro4K型号的视频有3个，IronView-2CD110型号的视频有4个。答案提交为1\_2\_3\_4

![](https://mmbiz.qpic.cn/mmbiz_png/5wuTuicCVRBGJibzZ7VF8WUZzez97UtAeDzLFYtTr4gf9ibysURTtbtndE74Gp8ds4ICRzUrGxf02mDON9r8XSmEcapWLMicUmvuA90EOEAkwWY/640?wx_fmt=png&from=appmsg)

答案 105\_97\_112\_106

## 溯源分析

【考题1】流量溯源 某公司运维部门在进行日常审查时，发现今天公司的内部视频资源共享系统产生了异常的访问行为，在初步研判后发现是被黑客入侵了。运维部门立刻保存了可疑时间段的流量信息，请你分析流量包，找出黑客获取到的管理员账号密码并作为答案提交。 【答案标准】 若管理员账号为123，密码为123，则最终提交的答案为：123/123

![](https://mmbiz.qpic.cn/mmbiz_png/5wuTuicCVRBG9ayZdicDfIaLZcDdk7mk3khhTDKEwQrIL8cAfN89mTKpQoWKNSuvsH7ct4arlqq9Pla7zLLGhAn7nuVLH7kC7ffCykecGgaCc/640?wx_fmt=png&from=appmsg)

## 答案 admin/Adm1n@2024#Secure!Pass

##

【考题2】数据采集 运维团队进入系统后，发现该系统中存在着员工信息。为了排查是否为内部人员作案，请你提取出手机号为18339633138的员工的工号信息并作为答案提交。 【答案标准】 若手机号为18339633138的员工工号为EMP0001，则最终提交答案为：EMP0001

这道题很简单用bp爆破页面然后把所有页面都保存下来 搜索手机号就能找到EMP0758

答案 EMP0758

## 异常事件分析

【题目1】风险评估 恒盾科技将某个区域定义为""高风险摄像头区域""，当且仅当该区域同时满足以下两个条件： 1. 该区域内存在至少 1 台老旧摄像头，其中老旧摄像头定义为：`install\_year ≤ 2020`（即2020年及之前安装的摄像头）； 2. 在附件所给时间范围内，该区域内所有告警记录中（通过告警日志表中的 `camera\_id` 关联摄像头表获取区域信息），有效告警率（`is\_valid = 1` 的告警数量 / 该区域告警总数）≥ 50%（包含等于50%的情况）。 请你基于附件中的摄像头信息表与告警日志表，判断： - 哪些区域属于“高风险摄像头区域”？ 要求： - 以区域编号为单位（如：A01、A02 等）； - 将所有满足条件的区域按字典序升序排序； - 使用英文半角逗号`,`拼接为一个字符串，作为本题最终答案。 【答案标准】 若最终判定 A01、A05、A09 为高风险摄像头区域，则提交：A01,A05,A09

这道题需要两个文件`cameras.csv` 和 `alarms.csv`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5wuTuicCVRBHrwURhgX3HiaScPO9RhabJ7VfwSqEWSvQNobrv3xD8gB5R98rh3mdhDyGQvicl7bc6ia61ZeQHngVUyR1PWJRA8Xkmjo5SUSyn2U/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5wuTuicCVRBGd1hmaXDLR6pnvVxF9pMjpZianrzKQRz2ldmNciceAZ7qVYKlg8ZBQrtovGJ6eqDaGRZicwWUjAicHiaTMgmmYB80jb86DqhqHWjIU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/5wuTuicCVRBFu0dKetI3TPtBB0Tib3SXkX8segiaMO2CKdP9vDyvjQrRM3plM4KAicag9zN0NFd6uVN3Rwk10l3MibROjbbclsrBx2OWhnuJ5uu8/640?wx_fmt=png&from=appmsg)

```
SELECT *FROM `联表-alarms-副本`WHERE alarm_id / 2 <= is_valid;
```

`答案 A01,A03,A05,A07,A09`

【题目2】事件识别 公司将某些告警记录定义为""可疑人员事件""，当且仅当该告警满足以下全部条件： 1. 该告警的 `alarm\_type = ""可疑人员""`； 2. 以该告警的 `alarm\_time` 为中心，在其前后 3 分钟时间窗口内（包含边界），在 同一区域（即通过告警日志表中的 `camera\_id` 关联摄像头表，获取该摄像头所在的区域 `are...
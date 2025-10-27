---
title: Python 解析 DLT645 协议数据
url: https://h4ck.org.cn/2024/10/18421
source: obaby@mars
date: 2024-10-31
fetch_date: 2025-10-06T18:52:25.782832
---

# Python 解析 DLT645 协议数据

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[人工智能『AI』](https://h4ck.org.cn/cats/cxsj/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E3%80%8Eai%E3%80%8F)

# Python 解析 DLT645 协议数据

2024年10月30日
[17 条评论](https://h4ck.org.cn/2024/10/18421#comments)

[![](https://h4ck.org.cn/wp-content/uploads/2024/10/2024_06_13_12_01_IMG_3855-tuya.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/10/2024_06_13_12_01_IMG_3855-tuya.jpg)

DL/T 645是中国国家电网公司制定的一种用于电能表通信的协议，全称为《多功能电能表通信协议》。该协议主要用于电能表与数据采集终端（如集中器、抄表器等）之间的通信，以实现电能数据的采集、传输和管理。

### 主要特点

1. **多功能性**：支持多种电能参数的读取和设置，如电压、电流、功率、电能、功率因数等。
2. **灵活性**：支持多种通信方式，如RS-485、红外、无线等。
3. **安全性**：支持数据加密和身份验证，确保数据传输的安全性。
4. **标准化**：符合国家电网公司的标准，便于大规模部署和维护。

### 协议结构

DL/T 645协议的数据帧结构通常包括以下几个部分：

1. **帧起始符**：标识数据帧的开始，通常为0x68。
2. **地址域**：标识电能表的地址，通常为6字节。
3. **控制码**：标识命令类型，如读取数据、写入数据等。
4. **数据域**：包含具体的命令数据或返回的数据。
5. **校验码**：用于校验数据帧的完整性，通常为1字节。
6. **帧结束符**：标识数据帧的结束，通常为0x16。

### 常用命令

* **读取数据**：用于读取电能表的各种参数，如电压、电流、功率等。
* **写入数据**：用于设置电能表的参数，如时间、费率等。
* **广播校时**：用于同步电能表的时间。
* **冻结命令**：用于冻结电能表的当前数据，便于后续读取。

### 应用场景

DL/T 645协议广泛应用于智能电网、电力监控系统、远程抄表系统等领域。通过该协议，可以实现电能数据的实时采集、远程监控和自动化管理，提高电力系统的运行效率和管理水平。

数据报文格式：

[![](https://h4ck.org.cn/wp-content/uploads/2024/10/Jietu20241030-095225.jpg)](https://h4ck.org.cn/wp-content/uploads/2024/10/Jietu20241030-095225.jpg)

数据报文解析相对来说并不复杂，所有的数据都是流式，直接按照顺序进行读取即可。不过里面数据的内容，并不需要在此进行数值转换（电力数据需要处理），基本读到什么内容就是什么内容。

例如原始数据：

```
message = b'hw8\x06(\x15Dh\x00\x02\x01\x1f(\x16'
```

解析数据可以通过下面的方法：

```
def process_645_data(message):
    print('message in hex=', message.hex())
    start_pos = message[0:1]
    # print('start_code = ', start_pos.hex())
    hid = message[1:7]
    # print(hid)
    # int_value = int.from_bytes(hid,byteorder='little')  # 默认使用大端模式
    # print(int_value)
    # int_value = int.from_bytes(hid,byteorder='big')  # 默认使用大端模式
    # print(int_value)
    print('hid = ', hid[::-1].hex())
    hid_hex = hid[::-1].hex()
    # print(hid.hex())
    data_pos = message[7:8]
    # print('data_pos = ', data_pos.hex())

    control_code = message[8:9]
    print('control_code = ', control_code.hex())
    data_length = message[9:10]
    print('data_length =', data_length.hex())
    data_lenth_int = int.from_bytes(data_length, byteorder='little')
    data = message[10:10 + data_lenth_int]
    print('data = ', data)
    crc_code = message[10 + data_lenth_int:11 + data_lenth_int]

    # crc_source = message[0:10 + data_lenth_int]

    # calced_crc = calc_crc(crc_source)
    # print('calced crc = ', calced_crc)

    print('crc_code = ', crc_code.hex())
    end_pos = message[11 + data_lenth_int:12 + data_lenth_int]
    # print('end_pos = ', end_pos.hex())

    return hid, hid_hex, control_code, data_lenth_int, crc_code, data
```

接收到的数据解析出来之后不需要再进行转换int.from\_bytes(hid,byteorder=’little’) 不管是大端还是小端模式，转出来都是错的，直接将高低位倒序输出即可：hid[::-1].hex()

解析后的数据：

```
message in hex= 68773806281544680002011f2816
hid =  441528063877
control_code =  00
data_length = 02
data =  b'\x01\x1f'
crc_code =  28
```

对于数据上报的内容，例如电量，电报上报数据为下面的报文：

```
# 电量上报数据
data_msg = b'\x68\x77\x38\x06\x28\x15\x44\x68\x91\x08\x33\x33\x34\x33\x33\x33\x33\x33\x38\x16'
```

解析数据内容：

```
data_msg = b'\x68\x77\x38\x06\x28\x15\x44\x68\x91\x08\x33\x33\x34\x33\x33\x33\x33\x33\x38\x16'

hid, hid_hex, control_code, data_lenth_int, crc_code, data = process_654_data(data_msg)
print(control_code.hex())
print(data.hex())

data_type = data[0:4]
data_source = data[4:]
process_data_type = bytes(byte - 0x33 for byte in data_type)
print(process_data_type[::-1].hex())
process_data_data = bytes(byte - 0x33 for byte in data_source)
print(process_data_data[::-1].hex())
print(int(process_data_data[::-1].hex(), 16) / 100)
```

解析后的数据：

```
message in hex= 6877380628154468910833333433333333333816
hid =  441528063877
control_code =  91
data_length = 08
data =  b'33433333'
crc_code =  38
91
3333343333333333
00010000
00000000
0.0
```

crc 计算方法：

```
def calc_crc(src):
    sum = 0
    for i in range(len(src)):
        sum += src[i]
    crc = sum % 256
    return crc
```

数据解析处理参考：<https://blog.csdn.net/m0_37651448/article/details/143100598>

☆版权☆

\* 网站名称：**[obaby@mars](https://h4ck.org.cn/)**
\* 网址：<https://h4ck.org.cn/>
\* 个性：<https://oba.by/>
\* 本文标题： [《Python 解析 DLT645 协议数据》](https://h4ck.org.cn/2024/10/18421)
\* 本文链接：<https://h4ck.org.cn/2024/10/18421>
\* 短链接：<https://oba.by/?p=18421>
\* 转载文章请标明文章来源，原文标题以及原文链接。请遵从 [《署名-非商业性使用-相同方式共享 2.5 中国大陆 (CC BY-NC-SA 2.5 CN) 》](https://creativecommons.org/licenses/by-nc-sa/2.5/cn/)许可协议。

---

[DLT645](https://h4ck.org.cn/tags/dlt645)[Python](https://h4ck.org.cn/tags/python)[电表](https://h4ck.org.cn/tags/%E7%94%B5%E8%A1%A8)

[Previous Post](https://h4ck.org.cn/2024/10/18424)
[Next Post](https://h4ck.org.cn/2024/10/18406)

![obaby](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=90&d=identicon&r=r)

#### obaby

爱好广泛的火星小妖精，有问题欢迎留言交流啊~(✪ω✪)
爬虫类工具请先点击这个链接查看用法https://oba.by/?p=12240
闺蜜圈APP下载 https://guimiquan.cn

#### 猜你喜欢：

2023年6月26日

#### [10行代码爬取安居客数据](https://h4ck.org.cn/2023/06/12349)

2021年10月9日

#### [Yolov5 tf-lite方式导出](https://h4ck.org.cn/2021/10/9145)

2012年7月12日

#### [IDA\_SYNC\_PLUGIN (v2.0.0.1) for IDA 6.x](https://h4ck.org.cn/2012/07/4327)

### 17 comments

1. ![](https://gg.lang.bi/avatar/d98dfdf4e1f6a84bbf50554abbd9fa5f81431acef40126d2fdcb5bb3b99d444a?s=64&d=identicon&r=r) **[刘郎](https://yjvc.cn/)**说道：

   [2024年10月30日 10:28](https://h4ck.org.cn/2024/10/18421#comment-120403)

   ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

   ![Google Chrome 127](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 127") Google Chrome 127 ![GNU/Linux](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/linux.png "GNU/Linux") GNU/Linux ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

   把这个解析出来能干嘛 可以不用交电费吗 哈哈 研究一下😂

   [回复](#comment-120403)

   1. ![](https://gg.lang.bi/avatar/d6ebc088df916bcc9e8b94a09f9b0f604e57be54b04bd520c6db2492740fc563?s=64&d=identicon&r=r)

      [2024年10月30日 10:44](https://h4ck.org.cn/2024/10/18421#comment-120404)

      ![公主](https://badgen.net/badge/管理员/小妖精/ff91a4?icon=terminal) ![Queen](https://badgen.net/badge/角色/女王/red?icon=matrix)

      ![Google Chrome 126](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 126") Google Chrome 126 ![Mac OS X 10.15](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/mac-3.png "Mac OS X 10.15") Mac OS X 10.15 ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

      哈哈哈，并不是，有个项目要通过这个计算电费，然后远程跳闸，😂

      [回复](#comment-120404)

      1. ![](https://gg.lang.bi/avatar/d98dfdf4e1f6a84bbf50554abbd9fa5f81431acef40126d2fdcb5bb3b99d444a?s=64&d=identicon&r=r)

         [2024年10月30日 10:52](https://h4ck.org.cn/2024/10/18421#comment-120405)

         ![Level 4](https://badgen.net/badge/亲密度/Level 4/yellow?icon=codebeat)

         ![Google Chrome 127](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/net/chrome.png "Google Chrome 127") Google Chrome 127 ![GNU/Linux](https://h4ck.org.cn/wp-content/plugins/wp-useragent/img/16/os/linux.png "GNU/Linux") GNU/Linux ![cn](https://h4ck.org.cn/wp-content/plugins/wp-useragent/show-useragent/flags_svg/cn.svg "cn")

         那能否弄一个计算好电费后 使用虚...
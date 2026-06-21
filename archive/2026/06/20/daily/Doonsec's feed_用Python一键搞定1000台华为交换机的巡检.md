---
title: 用Python一键搞定1000台华为交换机的巡检
url: https://mp.weixin.qq.com/s/X2xvaLFUEcFeGFcKIvkSeA
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:48:47.052531
---

# 用Python一键搞定1000台华为交换机的巡检

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/vf29dJy0S5icUnicAal06atrt69dYRKQnXNibjialWYpOHmf0Fh24iaCGIoHQ492kxN9LTyNibJQXgXOJVNAptVXreIuib2LhwqDgR2qR9WAONibicHQ/0?wx_fmt=jpeg)

# 用Python一键搞定1000台华为交换机的巡检

原创

圈圈
圈圈

网络技术干货圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

先说说背景吧。公司网络规模越来越大，交换机从几百台长到上千台。传统巡检靠人工，问题一大堆：

* **效率低**：一台台SSH登录，敲`display version`、`display interface brief`之类的命令，重复劳动能把人逼疯。
* **容易出错**：手抖输错命令，或者忘记某个端口的异常。
* **数据不规范**：收集的信息散落在各种Excel里，后期分析头疼。
* **没法定时**：突发故障时，想快速全网巡检根本来不及。

自动化后，这些问题基本解决。脚本可以24小时待命，定时跑任务，输出结构化的报告，还能对接邮件或企业微信通知。关键是，它解放了我们这些“救火队员”，能把精力放在更重要的优化和架构设计上。

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S587CSubLiajnQLOQfGcRibOjTEsqLVgWkmZcAhJGW3l7RuTW4DHpYOV2rxkgHiaibTzSdhLb2kMnnXQUKXfibM8t2ygtWw07OXvXqbA/640?wx_fmt=png&from=appmsg)

我第一次试水的时候，只巡检了10台设备，就觉得“哇，这也太香了”。后来逐步扩展到1000台，中间踩了不少坑，但也积累了很多经验。今天全分享给大家。

工欲善其事，必先利其器。咱们需要的工具其实不多，但要选对。

1. **Python环境**：推荐Python 3.8+。我用的是3.11，兼容性好。
2. **核心库**：

* **Netmiko**：强烈推荐！它对华为设备支持很好，封装了SSH连接、命令发送、分页处理等细节，比原生Paramiko省心多了。安装：`pip install netmiko`
* **Pandas**：处理数据、生成Excel报告神器。`pip install pandas openpyxl`
* **Concurrent.futures** 或 **ThreadPoolExecutor**：处理并发，1000台设备不能一台台串行跑。
* 可选：TextFSM 或 ntc-templates，用于结构化解析命令输出（后面会讲）。
* **Paramiko**：Netmiko底层就是它，如果你想更底层控制也可以了解。

3. **设备信息管理**：别把IP、用户名、密码硬编码！用Excel、CSV或JSON文件存设备清单。示例CSV格式：

```
ip,hostname,device_type,username,password
192.168.1.1,SW-01,huawei,admin,YourPass
192.168.1.2,SW-02,huawei,admin,YourPass
...
```

4. **环境注意**：

* 交换机开启SSH，配置好Vty用户权限。
* 巡检账号建议只读权限，减少风险。
* 网络连通性：确保你的脚本服务器能访问所有设备。防火墙、ACL别挡路。
* 并发控制：1000台别一股脑全上，建议分批或限流（比如并发50-100），避免把交换机或自己服务器搞崩。

我一般把这些配置写在一个`devices.csv`和`config.py`里，方便维护。

## 核心脚本

咱们先从最简单的一台设备开始，逐步完善。

**基础连接示例（用Netmiko）**：

```
from netmiko import ConnectHandler
import time

def connect_and_run(ip, username, password):
    device = {
        'device_type': 'huawei',
        'host': ip,
        'username': username,
        'password': password,
        'port': 22,
        'timeout': 30,
    }
    try:
        with ConnectHandler(**device) as conn:
            conn.enable()  # 如果需要进入特权模式
            output = conn.send_command("display version")
            print(f"{ip} 连接成功！版本信息：\n{output[:200]}...")  # 截取一部分看效果
            return output
    except Exception as e:
        print(f"{ip} 连接失败: {str(e)}")
        returnNone
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/vf29dJy0S5ibokRDet7k89Fb6dKflQswux9xicb7wPjM8ic5qD8ExWFlDKbxiaPhicqjNgUQDRrS7nZQIjPQXw3dNZgm6RcJrDJyTCK4xhhcMuzU/640?wx_fmt=png&from=appmsg)

简单吧？Netmiko自动处理了很多华为设备的“脾气”，比如分页`---- More ----`。

**常用巡检命令清单**（这些是我日常必查的）：

* `display version`：版本、启动时间
* `display device`：单板状态
* `display fan` / `display power`：风扇、电源
* `display cpu-usage` / `display memory`：CPU内存占用
* `display interface brief`：接口摘要
* `display interface description`：接口描述
* `display arp` / `display mac-address`：ARP和MAC表
* `display current-configuration`：当前配置（可选，输出大）
* `display logbuffer`：日志缓冲

你可以把这些命令放一个列表里，循环执行。

```
commands = [
    "display version",
    "display device",
    "display cpu-usage",
    # ... 更多
]
```

**并发处理1000台**：用`ThreadPoolExecutor`。

```
from concurrent.futures import ThreadPoolExecutor, as_completed
import csv

def main():
    devices = []
    with open('devices.csv', 'r') as f:
        reader = csv.DictReader(f)
        devices = list(reader)

    results = {}
    with ThreadPoolExecutor(max_workers=50) as executor:  # 根据服务器性能调整
        future_to_ip = {executor.submit(connect_and_run, dev['ip'], dev['username'], dev['password']): dev['ip'] for dev in devices}

        for future in as_completed(future_to_ip):
            ip = future_to_ip[future]
            try:
                results[ip] = future.result()
            except Exception as exc:
                results[ip] = f"Error: {exc}"

    # 保存结果
    with open('inspection_results.txt', 'w') as f:
        for ip, data in results.items():
            f.write(f"--- {ip} ---\n{data}\n\n")

    print("巡检完成！")

if __name__ == "__main__":
    main()
```

![](https://mmbiz.qpic.cn/mmbiz_png/vf29dJy0S5ib5R1iatqCYCwpPfZ0B1ibYrNZMfbyoBGsicAmibAt1ddJ5mLE6gC0jacZ9bbWHTXzEB8NtsGpqT7X9t0hIQalPnscJGdDCSKvLLC4/640?wx_fmt=png&from=appmsg)

跑起来后，你会看到终端刷刷刷地输出，效率直接拉满。实际测试中，50并发下1000台大概2-4小时搞定（取决于网络和命令复杂度）。

## 数据解析与报告生成

原始命令输出是文本，读起来费劲。我们可以用Pandas生成Excel，或者简单用TextFSM解析关键字段。

简单版：把每个命令结果存到字典，再转DataFrame。

```
import pandas as pd

# 假设results是字典
data = []
for ip, outputs in results.items():
    row = {'IP': ip, 'Version': extract_version(outputs.get('display version', '')), ...}
    data.append(row)

df = pd.DataFrame(data)
df.to_excel('巡检报告_20250612.xlsx', index=False)
```

提取函数可以用正则或字符串查找实现。比如提取CPU利用率：

```
import re
def extract_cpu(output):
    match = re.search(r'CPU usage:\s*(\d+)%', output)
    return match.group(1) if match else 'N/A'
```

高级点推荐TextFSM + ntc-templates，它能把`display interface brief`解析成结构化表格。

## 常见坑

1. **连接超时/失败**：设备太多，网络抖动常见。加重试机制（retry 3次），用exponential backoff。
2. **命令输出分页**：Netmiko基本能处理，但有些老设备顽固，可以`conn.send_command("screen-length 0")`先关分页。
3. **权限问题**：巡检账号别给太高权限。`display`命令大多只读就够。
4. **性能瓶颈**：服务器CPU/内存不够？降低并发或分批跑（比如按区域分10组）。
5. **安全**：密码别明文存！用key文件、环境变量或密码管理工具（比如keyring库）。
6. **华为设备特性**：有些型号device\_type用`huawei`或`huawei_vrp`，测试确认。enable模式可能需要secret。
7. **日志与异常**：每个设备独立try-except，别让一台失败拖累全部。

我曾经因为没控制并发，把监控服务器搞得响应慢，领导还来问“网络是不是又出问题了”……血的教训啊。

上个月公司扩容，又加了300台新交换机。我把脚本一改，新增设备IP导入CSV，跑了一遍。全网健康情况一目了然，发现了十几处潜在隐患（比如几个电源老化、部分端口流量异常）。领导看完报告直呼“靠谱”，还给我申请了奖金。

从那以后，巡检从“每月苦哈哈”变成“每周自动跑”，大家工作幸福感up up。

---

自动化不是一蹴而就的。刚开始可能花一周时间调试，但后面节省的时间是指数级的。建议大家先在测试环境或少量设备上练手，熟悉Netmiko的脾气，再大规模推广。

代码我不会一次性全贴（太长了），但核心思路和片段都分享了。你可以根据自己环境改改。如果有具体问题，欢迎在评论区留言，或者私信我交流。咱们一起进步！

记得备份好现有配置，安全第一。网络运维这条路，工具是帮手，经验和责任心才是根本。

喜欢这篇文章的兄弟，点个在看、转发给需要的朋友。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/p8No8ScJKT8cAnqjp2AZ90pLWoO7Ysr6JzXPMqP8qibB5ggPz4amnZicChP8vQExwbEJ1O0BtqiaYuYHicm74DQnbA/0?wx_fmt=png)

网络技术干货圈

向上滑动看下一个

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/p8No8ScJKT8cAnqjp2AZ90pLWoO7Ysr6JzXPMqP8qibB5ggPz4amnZicChP8vQExwbEJ1O0BtqiaYuYHicm74DQnbA/0?wx_fmt=png)

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
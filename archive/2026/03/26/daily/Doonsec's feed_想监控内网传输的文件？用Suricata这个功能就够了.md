---
title: 想监控内网传输的文件？用Suricata这个功能就够了
url: https://mp.weixin.qq.com/s/qAOgm3bzJ4MiTd_FpeXFoA
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:27:30.098183
---

# 想监控内网传输的文件？用Suricata这个功能就够了

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mviaYMmAdX9j6OVvMBqrNdDwic6lqm7HaC8oGqy2kHGD5g7of2xoYhI1ZRHIGuvqwwp39zvFIbl6uZ08hIia2CbXNyy8q1ziadA4FWEfhhgu7HU/0?wx_fmt=jpeg)

# 想监控内网传输的文件？用Suricata这个功能就够了

sec0nd安全

![]()

在小说阅读器中沉浸阅读

以下文章来源于安全孺子牛
，作者网络安全菜鸟

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM76vS0lEDqYIR3fJTpsa6Ahjq05k3dX4MaYq9jIdcCMsQ/0)

**安全孺子牛**
.

网络安全学习研究分享

![](https://mmbiz.qpic.cn/mmbiz_png/mviaYMmAdX9jG1VhOHFGzldZSbQD2Qd5KZGepBKDPY4WLVjVoIXwcDVN7XGku25MVaKMfSUiaQuwQVDgPULV74iarm0Mr9asbD83F9DSibtvyTo/640?wx_fmt=png&from=appmsg)

**植此青绿 拥抱春天**

**1.简介**

Suricata本身支持文件提取功能，只需要配置suricata.yaml中相关的配置项，并构建相应的文件提取规则，Suricata即可基于规则实现对网络流量的文件提取。

1.1创建文件提取路径

```
# 文件路径
mkdir -p /var/log/suricata/files
```

### 1.2开启文件提取功能

```
vim /etc/suricata/suricata.yaml

- file-store:
    # This configures version 2 of the file-store.
    version: 2

    enabled: yes   #默认为不记录，开启记录

    # 设置文件存储目录。如果路径不是绝对路径，则相对于default-log-dir。
    dir: filestore

    # 为每次出现的文件写出一个fileinfo记录。默认情况下是禁用的，因为每次出现都已作为fileinfo记录记录到主eve日志中。
    write-fileinfo: yes

    # 强制存储所有文件。默认值：否。
    # force-filestore: yes

    # 覆盖我们要在其中执行文件提取的会话的全局流深度。设置为0表示无限制。
    stream-depth: 0

    # 取消注释以下变量，以定义Suricata可以为文件存储保持打开状态的文件数。默认值为0，这意味着每次写入后文件都会关闭
    max-open-files: 1000

    # 强制记录校验和，可用的哈希函数为md5，sha1和sha256。请注意，使用此输出模块会自动强制使用SHA256，因为它使用SHA256作为文件命名方案
    force-hash: [sha1, md5]
```

![](https://mmbiz.qpic.cn/mmbiz_png/mviaYMmAdX9jdox2Oia5NJHHEdd8ribLdAAU2ztERrvtZ8kqBCOz4W1AwoPZYvaMVUdeicxCE7DT6pP5R5YMicNhnvUr8kicxxKkMLa0EbQKECOr4/640?wx_fmt=png&from=appmsg)

### 1.3测试文件提取

#### 1）编写文件提取规则

**注：必须有提取规则才能提取文件**

```
cat > /root/test.rules << EOF
alert http any any -> any any (msg:"http file store all";flow:established,to_server;filestore;sid:1667;rev:331;)
alert smtp any any -> any any (msg:"smtp file store all";flow:established,to_server;filestore;sid:1668;rev:331;)
alert ftp-data any any -> any any (msg:"ftp file store all";flow:established,to_server;filestore;sid:1669;rev:331;)
alert nfs  any any -> any any (msg:"nfs file store all";flow:established,to_server;filestore;sid:1670;rev:331;)
alert smb  any any -> any any (msg:"smb file store all";flow:established,to_server;filestore;sid:1671;rev:331;)
EOF
```

#### 2）抓取数据包

```
tcpdump -i ens33  -w http.pcap
```

#### 3）测试文件提取

```
mkdir -p /opt/suricata
suricata -c /etc/suricata/suricata.yaml -S  /root/test.rules -r http.pcap -k none -l /opt/suricata/

-c 			 # 指定配置文件
-S       # 选项仅加载指定的规则文件，如果在suricata.yaml中启用了任何其他规则，则忽略它
-k       # all:检测check_sum，none：不检测
-r       # 指定pacp文件位置
-l       # 指定输出位置
```

![](https://mmbiz.qpic.cn/mmbiz_png/mviaYMmAdX9gSs1fxN48iaXxecZkVY8MjJExoZ3lsPr3OzR5iaSgec7ibvOqEet0ibXgKK5UibszkRvBZt6XBu818CHB08kTXQsvmHlZYJuS8wJV4/640?wx_fmt=png&from=appmsg)

#### 4 ）查看文件名称和sha256

```
# 安装json解析文件
yum -y install jq

# 查看文件名称和sha256,上传的文件以sha256命名
more /opt/suricata/eve.json | grep filename | jq .fileinfo | jq ".filename,.sha256"
```

![](https://mmbiz.qpic.cn/mmbiz_png/mviaYMmAdX9hfSCVtouk5QIwZibrZEpFEcEGY3dVpEVJFPaCUlz5suqPh3tWv0644C8KkHmiaJmS67sNcYUqribACLbePib3KWM9oGnZibJkKK578/640?wx_fmt=png&from=appmsg)

#### 5 ）查看文件

文件指定为指定的目录，与日志存放在一起。

![](https://mmbiz.qpic.cn/mmbiz_png/mviaYMmAdX9hCtdMdZ9htTgmS2NEUicX9r7z8N6KWpUxDPU2pCYJmpPqpUib5PxZQLUIibJTTY9sUaNCiaStUwM9fUox9AygfXibla4bENkYQYO0c/640?wx_fmt=png&from=appmsg)

文件存储在以sha256前两个值目录中

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mviaYMmAdX9jB81X9QMRQs7Zt4NyjtYPATNb9AnVWUKTaKpNMpJz22VdehYOSoElDibOgicICWiaX7iaTsWxhvGHmXGdlvsicwORxiaDibaqlYUHDY0/640?wx_fmt=png&from=appmsg)

下载的文件是以jpg后缀的txt文件

```
file ba92cb29fbf84ffefd135ce7d833ef3eb415c3307a5c0d87ceaee1be91d05398

more ba92cb29fbf84ffefd135ce7d833ef3eb415c3307a5c0d87ceaee1be91d05398
```

![](https://mmbiz.qpic.cn/mmbiz_png/mviaYMmAdX9iavp8jicUIQI1WbWuSTlwRFkcibLTYfxo1vcPST5uRowdHvlZYicCrTZBCGeDRMHs144SSxdXnV21FlhhQto0lc1hicDMhR8DCAE48/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/mviaYMmAdX9hGJAKgRp6picOVFice9SKriaEBhMJibRE9yjqOickYPC0dGGLpDzxNHlm6jSOF0bicBrm6cBpc8iaDuucmhv8a6fvJNOHkeNWt3Mnhyw/640?wx_fmt=gif&from=appmsg)

**the end**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

sec0nd安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

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
---
title: 利用Brute Ratel安装恶意软件攻击活动的详细分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247488510&idx=1&sn=946b167ec7ed4f11e076a890b02e0635&chksm=902fbcd6a75835c06718a7126a9b61de25f6cb1060ad3e4d37617d4318d0a35042f6ea0782b0&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2024-07-09
fetch_date: 2025-10-06T17:45:49.666503
---

# 利用Brute Ratel安装恶意软件攻击活动的详细分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDnPv3bQfJNkt68Zl5B9rdTFk2ibw9F7DTo5DxVPu1HPPkiaonFY3lRdmg/0?wx_fmt=jpeg)

# 利用Brute Ratel安装恶意软件攻击活动的详细分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/t/14955

先知社区 作者：熊猫正正

Brute Ratel C4是一款类似于Cobalt Strike的商业红队武器框架，该工具每年License收费为3000美元，客户需要提供企业电子邮件地址并在颁发许可证之前进行验证，首个版本Brute Ratel C4 v0.2于2021年2月9日发布，它是由Mandiant和CrowdStrike的前红队队员Chetan Nayak创建的，该工具独特之处在于它专门设计防止端点检测和响应(EDR)和防病毒(AV)软件的检测，是一款新型的红队商业对抗性攻击模拟武器。

与Cobalt Strike的Beacon后门类似，Brute Ratel C4允许红队在远程终端主机上部署Badger后门程序，Badger程序连接回攻击者的命令和控制服务器，接收服务器端的命令执行相关的恶意行为。

笔者最近跟踪到一例利用Brute Ratel安装其他恶意软件的攻击活动，对该攻击活动进行了详细分析，供大家参考学习。

详细分析

1.初始样本为一个JS恶意脚本，恶意脚本里面带有很多垃圾注释代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDZ4ngAibUotDWZZDpAxibq9KeU4SKk8AXDa8OialnB54J8MpibjBVkS8ZCQ/640?wx_fmt=png)

2.去掉无用的垃圾注释代码之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDBadEj7lA9ZLKxULDyfWibFLTFsxLFUAaOiaBkD9kuhUHK6Sy0O4jkBww/640?wx_fmt=png)

3.恶意脚本解析还原上面包含的恶意代码，从远程服务器上下载恶意MSI安装程序并安装执行，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDZ3MO8xxZibK2hDhvqJslrvXTjmuFNAkq5DdjQiaeU65lp2q5QVwwmmWQ/640?wx_fmt=png)

4.恶意安装程序会启动rundll32.exe进程执行恶意模块，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDIYnnHw2efFibwfVeSoY0dkCDibFLmC8chiblHGWbhJPSmicqX7PWOpKfDQ/640?wx_fmt=png)

5.恶意模块启动执行之后，进程信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDQLjf0BHc0S7megzuibnibgsuI1kDOlDmS6f893ibW1zABmyoWBpOkVkKA/640?wx_fmt=png)

6.获取相关函数地址，然后通过VirtualAlloc分配相应的内存空间，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDpJnkXFotJNbfN0ZrIpF45cnt7icAkzJxeyxiaicJAR68PbkXWAv1Eic1Bw/640?wx_fmt=png)

7.通过异或算法解密程序中的加密数据，解密密钥为P9zw@Hg6cquhA0ZMRr^c，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDHvKJaVtpgsnicW44PSAAkibhgP8ia6vUQbS3DlQLzGZGusCVqbRqBbUzQ/640?wx_fmt=png)

8.解密之后的PayLoad数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDdTibRWrl4VkSbXAQUcXGIwJfVVxL2L9ibNibYCfwsM2wzyF5WHwl7JXvQ/640?wx_fmt=png)

9.分配新的内存空间，将解密后的PayLoad加载到新的内存空间当中，然后跳转执行到PayLoad入口代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDhZMEgYpHPWYeKI1ianlChqH13BFITTIWbepKM05lviaTW7bBsGibNNriag/640?wx_fmt=png)

10.解密出来的PayLoad疑是BRC4后门模块，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDpGMGV8RYC9CSJxmOB3jg5XZFB7ZIwrZ49sSq71yIiaZCyfegYI5bO4A/640?wx_fmt=png)

11.PayLoad加载程序中包含的恶意模块代码，并调用其导出函数StartW，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDcw8ibykCog82clicqicr8zLiccpDQGUfs7qwvcx4pMmmjLX2QqwWu4CPCw/640?wx_fmt=png)

12.程序中包含的恶意模块代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDdn2zXwicgbp43cQ6m6qIbOgjcILibWE2AXBiaN3MT2ab4NtBoyomQG6Sg/640?wx_fmt=png)

13.StartW导出函数代码，使用长时间休眠逃避自动化沙箱，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwD0GJa9yic4uswkd3ibBP1AK9aDKrhM1Uk2ibdwzzLCluiaPPnjgb81LN89A/640?wx_fmt=png)

14.加载执行到恶意模块的入口点代码处，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDDO4H7jQgFblxV9xzq7W7O5gTvuJbAicHMN9XURfE2FJ1SuJkNJJgLzQ/640?wx_fmt=png)

15.分配内存空间，将程序中包含的ShellCode代码数据写入到内存空间，然后调用远程线程执行ShellCode代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDzaySqiaAXBK7oP4UFCnePFY3mzk3mCibuNr9haVQvcsfrBmkv2omOpWw/640?wx_fmt=png)

16.写入到内存的ShellCode代码数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDPypNen3o2PzkxUkt4C76In8zgMO2vfxOzjwMRFlppiciciaA8icZViahZyw/640?wx_fmt=png)

17.最后跳转执行ShellCode代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwD3MLLqmiaHib6Tld2s75llicDxYZB4GiaVq32rrzWqFicq687LGbVLXoElPg/640?wx_fmt=png)

18.解密ShellCode中的加密数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDiatpgSILpbOKEiaHtpaCf25J7Wib5P0HQyOfiajdDZvKnOY8RoGrSvM2ow/640?wx_fmt=png)

19.解密之后的PayLoad数据，PE文件头被抺掉，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDZOK6BzUSAQaYTOBpaibTiakWJ762J4Ajq6dqPeQcLIHUr53hsxicpwz5w/640?wx_fmt=png)

20.然后跳转执行到解密出来的PayLoad入口代码处，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDmXh66EIjfricydfzcJPqDEGnjFYwFHPMhm3THT50R11usczVNib4dmsA/640?wx_fmt=png)

21.PayLoad入口代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDveYgicERicHxLXoDpibvAicx2sibaZJeTzZhGjg0YyKDYyfxnavZdib68icyQ/640?wx_fmt=png)

22.获取相关函数地址，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwD8UmAXXzLYL0anUHibDYU5iciauGr3UTK9jNYJEDlIUMiaG0hmHI45X4lfA/640?wx_fmt=png)

23.PayLoad在内存中解密出远程C2配置信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDGwAufIZia1ZzhjeXrBn57TO5ib20uLCz95SnZC23gcQMa92BaUe5qY0Q/640?wx_fmt=png)

24.解析出远程服务器C2域名信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDkcI9HcrVkm9B07DrIWDVeJVuR9VCq97IwbYkvibWamcwEaIxCMWsEWQ/640?wx_fmt=png)

25.解析出远程服务器端口信息7444，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDXOhOXspafS6I7UrZE4Tu9icP9M28dj9j4ia0Wv6PA2c6xr97UO8qaCjg/640?wx_fmt=png)

26.解析出远程C2服务器URL请求后缀信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDMFdxJkw2G96jg1nLVQJPJHSxZ3jlibp21EU4HuTJw8GZiafbq2ibdhgtA/640?wx_fmt=png)

27.获取主机相关信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDjye03MbnHBIWwzckSmHk5LZrweY8qObdMjrqjDMicXhKbgcahHUfRicA/640?wx_fmt=png)

28.将获取的主机相关信息，按固定的格式拼接请求数据包，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDicCggicnm9raEKeegzBZsS8zbnGBzkkrJGOp2IZERM1kSGPu6ibibSibdnQ/640?wx_fmt=png)

29.将请求数据加密，加密之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDqMzIjkbZhTQlAicYuSu9TkylJHgtNkYp2cLhuSa6IbN96ib2Wg2Hv69A/640?wx_fmt=png)

30.然后与远程服务器通信，通过POST将请求数据发送到服务器端，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDnwB24N8gHTcrQSxxC48SulzjCYBdW30JIWaf0M0DibOZKAuqrywKibhg/640?wx_fmt=png)

到此整个恶意软件加载执行过程就分析完毕了。

威胁情报

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWOkuicF5Kx3ib9XI2TXjNIwDuGIqkngribIsayLCB8xM8NMiaawgN7S3u7VkyiadUicjThs0yPlJs3zZsA/640?wx_fmt=png)

总结结尾

黑客组织利用各种恶意软件进行的各种攻击活动已经无处不在，防不胜防，很多系统可能已经被感染了各种恶意软件，全球各地每天都在发生各种恶意软件攻击活动，黑客组织一直在持续更新自己的攻击样本以及攻击技术，不断有企业被攻击，这些黑客组织从来没有停止过攻击活动，而且非常活跃，新的恶意软件层出不穷，旧的恶意软件又不断更新，需要时刻警惕，可能一不小心就被安装了某个恶意软件。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

安全分析与研究

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

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
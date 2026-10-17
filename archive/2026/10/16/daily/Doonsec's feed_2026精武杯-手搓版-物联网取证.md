---
title: 2026精武杯-手搓版-物联网取证
url: https://mp.weixin.qq.com/s/LOJ--mn1m-DogIHZGiLH_g
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:28:43.189538
---

# 2026精武杯-手搓版-物联网取证

# 2026精武杯-手搓版-物联网取证

原创

李逍遥
李逍遥

SPEEDCoding

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

GZH WORKBENCH

2026精武杯-手搓版-物联网取证

2026精武杯

【简要案情】近期，某市反诈部门接到多名群众报案，均遭遇“投资理财”类电信网络诈骗，指向的犯罪团伙涉案资金巨大、作案链条隐蔽。办案单位迅速成立专案组开展电子数据取证工作。经初查，该犯罪团伙搭建虚假投资平台，通过社交软件诱骗受害人充值转账，团伙成员分散多地办公，使用多种 AI 工具进行违法犯罪活动，同时发现涉及其他犯罪事实。请根据获取的电子数据还原案件经过。注：所有检材及相关数据均为虚拟构造，不负法律责任，如有侵权请及时告知，未经允许不得用于商业用途。检材容器密码：2026精武杯/中国人民警察大学@CPPU-ISA&拓界科技@飞鹰小队

01

第四部分：物联网取证

SECTION

（一）提示：分析办案人员提取的“无人机”文件夹，内含“26-09-14-10-12-59\_FLY001.DAT”，回答下列问题：（二）提示：分析办案人员提取的“NAS”文件夹，内含“sda-system.E01、sdb.E01、sdc.E01、sdd.E01、sde.E01”，回答下列问题：

（一）提示：分析办案人员提取的“无人机”文件夹，内含“26-09-14-10-12-59\_FLY001.DAT”，回答下列问题：

可以学习一下mumuzi大佬的无人机取证教程：大疆无人机日志取证的手工分析 | mumuzi的blog

5.89（填空题　1 分） 该无人机的型号是什么？（答案格式：Tuojie1）

使用010打开这个二进制文件，可以看到大疆的标识：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4ZBjkib8E9H8vhq8cicK6ymKXQRXEhicZ0LbUFYh4e266lNwibaNt6oKdCbUUlaDdBF15Z9RjFGH75euLkB2stW2oGZuibOrnVhnq3A/640?wx_fmt=png&from=appmsg)

用csvview打开这个日志文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4aoFaKTNXQzGEWqCGGwxu9Z12d2QQB8w0v2wg7790dicDG6P1BLhzpPZBMnS28TtFFJqdUv7nU3Tq3KcibMRbkrGaXicibRibGicVPQ0/640?wx_fmt=png&from=appmsg)

右侧可以看到无人机的型号位Mavic2

Mavic2

5.90（填空题　1 分） 飞行记录中马达的启动时间（UTC +8）是什么时候？（答案格式：2026-08-02 11:05:13）

查看一下马达速度曲线：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4aicXmqXSPVvyqHibK32pwuTYibItkEaozqtNfia0VbkbOyYg9lY2RKCFWhldLA7qqjibQfyLz3DPN1ctuVyuJvYtgibBnktDe57fxa8/640?wx_fmt=png&from=appmsg)

可以看到在时间轴为0左右的时候开始有了转速，再去看一下日志，可以看到相对时间0的时候有马达启动的日志：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4Ywyic8QCPlGLflvp52DKYbojltc04iaLBSt4ERjyteX4TWIX3IiaVqrUyUlCYXPYPT72ogZaVPzDNMHWoCEH28Z3jOTcibARYPUoo/640?wx_fmt=png&from=appmsg)

最开头的日志那里有启动时候记录日志的时间：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4Z6PzjVdeyVY3mmJzbCnVfwuNibgKUI0BKqFQeSPibOodnTOSxerEibaiasUvUMKfVhibRQngaadib4vvb0gRQxKlxBuGBzFFWxo9iaus/640?wx_fmt=png&from=appmsg)

对应的是2026-09-14 10:12:59，注意日志属性信息里面的时间是2点：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4bffqVpVK3N1IbNZxia3JQqhkjpfAdic1ibOONLuPgIlByibZgGcdO9icLclC1W27ibZxpSEjax383gSEicHyxsYFXIicKZjSrEphFAWuo/640?wx_fmt=png&from=appmsg)

所以这个十点的就是utc+8的时间，然后加上154s即可得到马达启动的时间为2026-09-14 10:15:33：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4Z4Xbt629icFlLk45gdnvtuYlwjO499R5RP6Hhnyn5AFmwDibWm0bYgJKWrziazDVSZjtaJ2IiaSZflq3ZJwY5p1ia3bhE96QLG2BgE/640?wx_fmt=png&from=appmsg)

弘连的物联网取证工具也能做，新建案件后选择无人机检材，选上面题目的型号，然后导入DAT文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4aEo6qpD6ibjT5UeJBlL6TThOHbibFOImSSk99h7oR12cWHYQyU6NOoFsTL1YFd55fetWUP9qtIOXhK93CNCs7gRbpBRLePpToM0/640?wx_fmt=png&from=appmsg)

导入户解析成功，查看结果：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4YH7ibxway42dYEnsawcgyiaic8KzKbcd6FGq1gUCIhZ7P4hTdjUxSvtdyfsMa4esA2dpkInSZibW6sWGzS69MVr8UzVNF5oYf3kY4/640?wx_fmt=png&from=appmsg)

筛选马达状态：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4YuuMu5z3HCt48fuicw7lBz3JPDkHHpqlNRvE2fBiafkib5WNzV1jmjticr2fewLxEhppqriccOhMOue0ctpVDw3pw4uIWaiciaENL2FA/640?wx_fmt=png&from=appmsg)

这里直接就能看到时间了，只是需要转成utc+8

2026-09-14 10:15:33

5.91（填空题　1 分） 接上题，该马达总共运行多少秒？（答案格式：四舍五入，回答整数，如321）

还是看：日志和马达转速曲线，这个可以联动看，鼠标在曲线上移动，左侧的日志也会动，拖到曲线中马达转速为0的时候，可以看到左侧日志的记录：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4Z3ZQGQE5Mg8EicplACz0P6Ciczms6702Dn14AOkBuyVfEK1fKGk5l90508zQuwoc9W9jx7IhGMv7GAYh2W3tA7IRvyMWoNOQVicc/640?wx_fmt=png&from=appmsg)

日志里面在150.738秒的时候显示马达停止，停止原因是着陆，题目要求是四舍五入，所以是151秒

151

5.92（填空题　1 分） 飞行记录中海拔最高时的纬度是多少？（答案格式：四舍五入取小数点后五位，如31.11111）

选中GPS记录里面的海拔和纬度两个曲线：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4ZYLiczULTC7BdaicLIRSib7Q9N6hYJIFvFtSpbbgydTywUehuusewlgYSNE3KXWW7XDEOQYKzwKkkibZTNrPSuHp7aWnveo5H6TFY/640?wx_fmt=png&from=appmsg)

可以同时查看纬度曲线和海拔曲线：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4Y1EA5cRx5icZOE44oKaK4GUpudpnYE1gCJ46KXJoW3ARFuB6tDhXKUvFrj1aZMial4qrhG1EOXgITNRlk9cnpEqics3XhghCiblPI/640?wx_fmt=png&from=appmsg)

棕色是海拔，红色是纬度，拖到海拔最高的地方，也就是74.9m，当前纬度是31.22772

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4ZXCGHwu2g5T4HNhg8OtYVarerDBAddlQjcDn8CGRwicMnZCYVBPlc29BBsx6g8YtmW3ial9ibKX2wBWpcJEg0n5QiblwW97fClJec/640?wx_fmt=png&from=appmsg)

或者直接弘连的物联网取证工具：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4aNxs9Fge0IUTySAobPI04e63licWia4K0GUTGauLicdh1jvKJkHhyByVbd4oNCPzac3ycJnQKk0ZagyEuibfNsXSXpmP3pzFD4KOg/640?wx_fmt=png&from=appmsg)

可以看到最高是74.931m，对应纬度是31.2277201

31.22772

5.93（填空题　1 分） 分析飞行记录的轨迹为几边形？（答案格式：4）

这个直接查看GeoPlayer选项，可以看到是五边形

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4YdKjIU3dhMHXVTAKDGYQNic47xAgvNNa7GZ2qFdzTeK5EXictW8znjhhM6YbzBoUHMmYicgu2gc2ic81D2jdrHroPiaxeXjs2sB0Ao/640?wx_fmt=png&from=appmsg)

或者用弘连的物联网取证工具查看：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4ZaltiayVoibvPrHXcxBVzGIN60dYQU56Sc2eKULJg3GVoviaAletLj0UBvcmLj2icuslItRctUcHiccRcsImNXZHdicZbCw24ze1RbM/640?wx_fmt=png&from=appmsg)

5

（二）提示：分析办案人员提取的“NAS”文件夹，内含“sda-system.E01、sdb.E01、sdc.E01、sdd.E01、sde.E01”，回答下列问题：

5.94（填空题　1 分） 分析涉案NAS的存储配置，其数据盘的RAID级别是什么？（答案格式：RAID0）

直接使用lovely大佬的工具：LovelyCarve，GitHub地址是LovelyTeams/LovelyCarve: a forensic carver with a soft heart · 基于 Rust、Tauri 2 与 Vue 3 的桌面磁盘取证与数据恢复工具：只读解析镜像、文件系统与加密卷，提供原类型预览、全局搜索、时间线、文件雕刻与插件分析：​https://github.com/lovelyteams/lovelycarve，赶快去给大佬点个星星。

把这五个镜像放进去自动识别并重组：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4bHGIdT2BvMM8LWEHfIRzXkAxTv1G6wB55avOQC0fbMG8rsD3yPBQzXlNxL9rUiaiabKH5ibeCLq6TB7fUMkGsAY1ic6gFXFe11xDA/640?wx_fmt=png&from=appmsg)

可以看到成功自动识别，4个磁盘，以raid5重组，块大小是512K，顺序也给出来了

RAID5

5.95（填空题　1 分） 接上题，分析其条带大小是多少？（答案格式：64K）

由上题的截图可以看到条带大小是512K

512K

5.96（填空题　1 分） 该操作系统root账户的密码是多少？（提示：六位密码，第一位是T，第二位是小写英文，后面是数字，答案格式：根据实际情况进行填写）

使用LovelyCarve挂载系统盘和重组完成的数据盘后，查看系统盘里面的/etc/shadow文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4aIaLSjeJiawibYfMupu0H58cvxw4NDqrPVFBib0TqdKk9hES8E9v6FIiaYZn9rU690VR68hgpqP99m4TJwg1bOicPWIFwk97ibNYN6Q/640?wx_fmt=png&from=appmsg)

把root密码的哈希赋值出来：

BASH

$6$AJCYvsyi3zYK7sLF$I1QBhWJMfZXRL4xA.Gny6pvnjxjJz3ScEqoScgnU7UAjiU5Tvlp4aYRF2uVfHdKvt0RViZ2hRTR4tm5GW017M1

使用hashcat爆破，首先查看模式号，这个是sha512的哈希，或者直接查看hashcat的文档搜也能搜到：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4Zgibqk1wAAQk2fx6I96ZSbWCPd7WeVgxiapiaSiaFyibaQT9UcLGDIWCv6ibBjLoh11YZUeJU0RFKeiayhAJlv8uUibzibHY2x9TqkZYBk/640?wx_fmt=png&from=appmsg)

可以看到模式号是1800，然后使用hashcat爆破：

CMD

hashcat -a 3 -m 1800 $6$AJCYvsyi3zYK7sLF$I1QBhWJMfZXRL4xA.Gny6pvnjxjJz3ScEqoScgnU7UAjiU5Tvlp4aYRF2uVfHdKvt0RViZ2hRTR4tm5GW017M1 T?l?d?d?d?d

查看结果：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4aGWaYpbZekwwt3DJ9iajrdEEGIReuZRT3nuvnUUHe3OkmcMvwI6WhibBx7Os9BuRnntv07an12zxb1t20baYdlZtIyfictcHuKN4/640?wx_fmt=png&from=appmsg)

Tj2026

5.97（填空题　1 分） 该设备使用的NAS平台名称是什么？（答案格式：英文小写，如tuojie）

对NAS平台进行一下仿真，根据上面LovelyCarve自动分析出来的RAID5，点击导出镜像：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4anhbuB69Wdf5ZmZtEviae3pDhnXE09evgDodjjuUjBn4ZvQgqaN5TneGPPpSGaXib3f3fX2auC6ibbY1veLf2qR9ESTth3zTIVx0/640?wx_fmt=png&from=appmsg)

再用火眼仿真添加系统盘和刚刚导出的dd镜像，就可以仿真成功了：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4YHuUOeF6zpuqrEUKHfyh5C4N4OpWAkdQHzIWwQvaic5gRTnQsibq3S5zOhfwIeHTmhBgibjdQCNh3G2GZUOW0u9yfGSDZHMqniagY/640?wx_fmt=png&from=appmsg)

可以看到这里网卡的固定IP是192.168.116.134，修改一下本地的虚拟网络编辑器仅主机模式的网段，再重启，然后修改etc目录下的network里面的interfaces文件：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4YYX49ZibY7JTPmYnibymadhPyBGTMKhlZqplkrur6iaocIK9rOD1Hwia2xib7hrjUvGicA1q33CJNjelb252KDuESogvtHuJrbmicXBg/640?wx_fmt=png&from=appmsg)

改成这样，再重启网络服务​systemctl restart networking，成功配置网络：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4YEibZzR7IxuuZkjuAq80iazavpI0Z56EDak6B1vknEOxtdkibNkqDoh0DMoTzSLbQKeK8jhtCGFZpqrehuXqB0kEbB1FanAwdtJM/640?wx_fmt=png&from=appmsg)

ssh连接成功

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4b2SsEnfPhMnSSKHRHT3qVXnNnC0ZrTlgibKxTnJ3Ps0yBqNAIUTLwk1c2F4FKunCShsJ7MR7VTRuITSzG0veUEOrFsOEPSGaeY/640?wx_fmt=png&from=appmsg)

然后查看一下nginx的配置文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4bABcO6ZicYmZFO1IvkM9XE0s3HpTOeVxnCjczZKvk0zyTt30RIM30E18u0qMicHeLcSNEO67RfJJfzvYpYuD6R8pK57EwmgnPUA/640?wx_fmt=png&from=appmsg)

可以看到监听的端口是91，用的nas平台是openmediavault，访问这个端口看一下：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4aUPVJvHbeyWKLXU6wSMmN03fmZRC98mYNibJ4DGtDuuBU...
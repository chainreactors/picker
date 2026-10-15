---
title: 2026精武杯-手搓版-计算机取证
url: https://mp.weixin.qq.com/s/TAZFnptdYQQQr7LOcNQlog
source: Doonsec's feed
date: 2026-10-14
fetch_date: 2026-10-15T06:42:51.989610
---

# 2026精武杯-手搓版-计算机取证

# 2026精武杯-手搓版-计算机取证

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

2026精武杯-手搓版-计算机取证

2026精武杯

【简要案情】近期，某市反诈部门接到多名群众报案，均遭遇“投资理财”类电信网络诈骗，指向的犯罪团伙涉案资金巨大、作案链条隐蔽。办案单位迅速成立专案组开展电子数据取证工作。经初查，该犯罪团伙搭建虚假投资平台，通过社交软件诱骗受害人充值转账，团伙成员分散多地办公，使用多种 AI 工具进行违法犯罪活动，同时发现涉及其他犯罪事实。请根据获取的电子数据还原案件经过。注：所有检材及相关数据均为虚拟构造，不负法律责任，如有侵权请及时告知，未经允许不得用于商业用途。检材容器密码：2026精武杯/中国人民警察大学@CPPU-ISA&拓界科技@飞鹰小队

01

第二部分：计算机取证

SECTION

提示：分析办案人员提取的“Laptop\_fulldisk\_image.E01”回答下列问题：

3.25（填空题　1 分） 该计算机的CPU型号是什么？（答案格式：i3-100A）

查看火眼的分析结果：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4bTianXDDibN8StL6qdqwNH0q4zu1V17yPnjKgjwL1o9iaO32DTjgJjB9fUV65EcmxKH5GXEnjDDnbDeP2xVhvyvO9KBK1BgCEKyw/640?wx_fmt=png&from=appmsg)

i7-12700H

3.26（填空题　1 分） 该计算机曾接入了一个移动硬盘，分配驱动器号为D盘，请问盘符名称为？（答案格式：以实际为准，如Tuo\_Jie）

查看一下USB信息：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4bTQOsf5vfwVzxoiaPKnbW9Hlxh7Jjgtqsjbmtd9yHaJ6OS6epZRovylLZby5NR6z06kBJwLaJ9BkhSxDFClBmrzSsaHDPpYVyA/640?wx_fmt=png&from=appmsg)

只有一个硬盘的插拔记录，在通知里面可以看到三星这个硬盘被分到了D盘，起那么就是它的盘符名称

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4b6pxicMKY5s7LpXZDicC0MMVTLuFmljwcF63ia2IkxxnibMauEoA91XpKTlC5F3JhZqHAuWd9JKC8ibcW9wCOkzXeZIxfPOkxFDKVw/640?wx_fmt=png&from=appmsg)

Samsung\_T5

3.27（填空题　1 分） 该计算机的开机密码是多少？（答案格式：以实际为准，如123456）

查看一下用户的ntlm哈希：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4bg7WPicu3G3qeRaP97muqqXcmndUmiaHfkfZkUwsibLtrV0C38EDnEeK0paPrsNN6ia8YrdEPM5IZZnad8AhoCOPHVEfe8PA5bNTA/640?wx_fmt=png&from=appmsg)

LM HASH是默认值（空），这里只需要爆破一下NT HASH，查看一下hashcat里面NTLM的mode号：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4aI7rtegDVxo7kfpSZHzIL89bLRD6wicZCKZNxVK20qfvj0rug8DK3TkeDmPk2m8HnANQeyRzLDg4piaibujlvcYtTcvJokkQFGzk/640?wx_fmt=png&from=appmsg)

然后使用hashcat爆破

CMD

hashcat -a 3 -m 1000 bb552c1772ea2b18fcb8abd75fba66e5 -i --increment-min=4 --increment-max=8 ?a?a?a?a?a?a?a?a

爆破成功，得到密码是260919

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4aHmDnXGmGQ7tNvRf0AFFoGb9gesQ6OQtjnxia5jvnD8jkoAhf6C3TcceIxe4iaf7QjK6ibGnYuquuykDuof4uVpqMmPWicZZ44aFY/640?wx_fmt=png&from=appmsg)

260919

3.28（填空题　1 分） 该计算机曾经连接过的远程桌面地址是什么？（答案格式：192.168.1.1）

查看火眼的分析结果：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4bsicITJiaaoXHvJwia58fxESOORKBdN8bVcpPJ0vB0ibmGEgNWa2TfsHYdUehppqLBDznKOLvL2qXiaksXqREXr70rpCmxPtZJefho/640?wx_fmt=png&from=appmsg)

103.87.9.67

3.29（填空题　1 分） 该计算机部署的WSL版本是多少？（答案格式：1.2.13.0）

仿真起来后在cmd命令行里面查看：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4a51eUvdsF0DOH35MA17icpRr4c5QI1AHiawuCMibzvKoNqwib7QcjfLmpLIU6QkMJaltgHPzrO8KlicOoaYiaxxnChbpRWvTURNR1pM/640?wx_fmt=png&from=appmsg)

2.7.14.0

3.30（填空题　1 分） WSL中部署的大模型推理引擎名称和版本是什么？（答案格式：名称-版本，英文全小写，如llama.cpp-0.1.0）

查看一下火眼分析出来的powershell历史命令：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4YR7eNwNWz6TJOFbuox6k0jQ8MU8NeU8IfGNGMqpF1icvSDyl9W8auaSd1y7ENWB2xlD8sdJjWTQdpQJszORwO9ib6oQ7uVga1SQ/640?wx_fmt=png&from=appmsg)

里面有vllm和ollama，这里可以看到嵌套虚拟机里面有wsl虚拟机的虚拟硬盘，添加为新检材分析一下：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4ZPPdY5HOkpn2nzJsQicNkgP26QW80P6H5KqBcd9T8akgjc5GicUf6cYrMh9BMHhTxaKj0zMTsbSzfOeVyrNKB5H3q8CszrFLCiaw/640?wx_fmt=png&from=appmsg)

然后查看一下分析结果的历史命令，可以看到都是关于vllm的部署命令：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4ZH45zVMza9JNZic1YwrPU7I7FcCa8gAiaKqrH4ibhMX0TwI6vZmFL1Cib0vTibZic8V0icFBKicfsZcH9upsibia94nDw2tSQRf2ViaPSecI/640?wx_fmt=png&from=appmsg)

这个应该是workbuddy给部署的，看一下workbuddy的记录（用户目录下有个WorkBuddy目录）

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4aLGj1T5b2zsW5FmKiaqJ2qSUjKHKm0XHI4LStSRk8GbXpWqKtF6rKamGCxqVWtnu4dodMLk2rcJAvDdvLgKyVr3VPJiaDN72HZM/640?wx_fmt=png&from=appmsg)

翻看一下对话记录，找到关键信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4aGDnpWarce0bicHIwpIyqzmicd3fjRXCU4Mer2ibQrwhcDL1TfPA5Q2o1F4enOcOutjcu7LhLNWFnznDYfGxe8caQNwjkQ3dCp7U/640?wx_fmt=png&from=appmsg)

这里可以看到workbuddy给装的vllm版本是0.11.0，再去wsl的虚拟机里面的用户目录查看，有config目录：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4aIvh4iaicDpsTMic3W25Sxo04jSdDM1iateIHNf0X97kvia4Pm3boHbiaubphnAluw6J1MlcCiabqB5dq4RxyoGkvGsiaWda6r7bN8vqI/640?wx_fmt=png&from=appmsg)

打开后也可以看到当前vllm的版本号：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4Zficd2mEicw4BTia9H2d1Czb2m5iafHwEyVicxqblkmnL13GIt9cicgWOtCj6bYjNicMqlUUELDAxkbAcQgM9GKpPj2VEb98IJh57oGo/640?wx_fmt=png&from=appmsg)

vllm-0.11.0

3.31（填空题　1 分） 接上题，其中部署的参数量为1.7B的模型设置的最大上下文长度（max-model-len）是多少？（答案格式：1234）

在wsl虚拟机的历史命令里面可以看到：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4Yko0JoBgicHoHvCFuWGq51aT0DWiaibgACMKGTSiaua3zeAoCpvWD2NRib117TaFx1ZCMnwdw8iavuQF7p0O0xgOP9kWWhejGLKs20w/640?wx_fmt=png&from=appmsg)

但是再看一下workbuddy的对话记录，发现8192这里是启动失败的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4ZeHoL1y3iaViaFJ1iaUCJq97ySMUAqiaYXjSEmonW1eLWXmS14KqAMeRuaib9rMdBqmaHGfKYIIXN1gs44N2MsqPTRE7Lm7VAkMWuE/640?wx_fmt=png&from=appmsg)

再往下看发现最大长度2048成功了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4bd0ZHl2h2kfFQSE3rKoSE5XmB9TOJeLDJqTmAIb7OBAksKykTkag6a6QvYbvI31tEEmQSOicAFqtJ4jqdWUibxaHG2YBPzrGPQw/640?wx_fmt=png&from=appmsg)

2048

3.32（填空题　1 分） 接上题，安装使用的CUDA版本是多少？（答案格式：仅写主版本号与次版本号，如11.3）

在workbuddy的对话记录中可以看到cuda版本：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4ZYkhnYX1NL6YzOicWtvJIcJxp3UkWrjSI9ApmAzQ7HaKSrZw5GuTQr1FuEWEzstua4rTjv1zzrW51GHVaGsVJGqqKH79E1X7cc/640?wx_fmt=png&from=appmsg)

wsl虚拟机里面vllm的配置文件里面也可以找到cuda版本信息：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4aWAzbnuMqmgZ2aeicXnIBRT7SYOGYJrx0icccbqozRBuia9viauaJ8lQUsc6MQSib8LNlNEQtds9e7yFhWhc5JYUqQQ6d9K5OPhKmY/640?wx_fmt=png&from=appmsg)

12.8

3.33（填空题　1 分） 该计算机中部署的自动语音识别（ASR）模型共有几个？（答案格式：1）

查看用户目录下的ASR目录里面的models，里面有3个模型：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4ZHY3Scibk2OxYZ8cpIKKiaaV1jWZ9902ibxD3YQ5Oz6dKfZpaR4Fmn057AyuyQ1u96tWst4lKRnU79ibSyzLz4ZpOGK9cITcbKqB8/640?wx_fmt=png&from=appmsg)

再看一下ASR目录的config.json配置文件：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4ZRsxZqriaiaguUFBt3MvMTViaXzxA3SJ9aDX5bk5eLNdoMTT70eD6KZrYIv3hqc7yZH1hibibGpTner1sicO9TZANGHOvdJQUiaZQMOY/640?wx_fmt=png&from=appmsg)

发现里面只导入了两个模型

2

3.34（填空题　1 分） 请尝试运行嫌疑人部署的自动语音识别系统，该系统的服务器地址及端口号是什么？（答案格式：http://192.168.1.1:8080）

运行ASR目录下的start启动脚本：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4aUms9ic9sysKGMomC0NJaibl9SIE5xqSDiaQXznpdCEW0PnNBLDXXNOZOyUxU83GDVhewMGuH8ynD17gxbsTy3zWwWEiaTBgFdXD8/640?wx_fmt=png&from=appmsg)

http://127.0.0.1:8765

3.35（填空题　1 分） 请在用于测试自动语音识别系统的文件中，找到的密码是什么？（答案格式：以实际为准，如1234）

在下载目录下找到了voice压缩文件，里面都是音频，应该是用来测试语音识别的文件导出后解压：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4ayIiaFq1pZjFyibAp50wZ0CdG4PL0COZ1ibEF2an6V5avu2w5ymhia9RbkhsxdHMkMmTJA6icibnwaARvicTiazItvdAicSyRdzqniaeL0k/640?wx_fmt=png&from=appmsg)

然后用弘连的苍穹AI引擎里面的语音转文字：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4a4WPurDFTqoHkRT0syI2xKYovunddekl29wR3FH7uxDZhzMFItbGS1EMf2WPe0azkBmCaVI6N97P2EQFian3GTXBYuB1RoXMzI/640?wx_fmt=png&from=appmsg)

导出后搜索“密码”关键词，找到对应语音：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4aero6whSBctEsIbpsXKEtOMlO6wvqCdHwnPmIYheuQfEJuHE64yibb5RgK37yx5yibIvBPJKGq89iaccic5L3eQiaYX2DZGDkQXiaOo/640?wx_fmt=png&from=appmsg)

20260915

3.36（填空题　1 分） 经分析，该密码可能为嫌疑人某加密盘的密码，请找到该加密盘，写出加密盘原始文件的名称。（答案格式：123.abc）

结合下面那个题的提示，加密盘中有图片，桌面正好有个图片.vhd，导出后加载发现是BitLocker加密，输入上题的密码成功解密进入：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4a2kskVZqnNB0R1A5licTiarCZCjib9JJTO9WcgDpxyT5sSOibLeKJEicIC6nJbMm3Sib4kiaO2dEMGqZyFrTyd8rEDeGJDMlX3SCY7cg/640?wx_fmt=png&from=appmsg)

图片.vhd

3.37（填空题　1 分） 接上题，加密盘中AI生成的图片共有多少张？（答案格式：1）

加密盘中一共30张图片，查看foxmail邮件，邮件内容说这30张图片都是AI生成的：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4YXHeYnJgNxlNlAaALCTwqodVjrNuDJWlApHHFmYdLoibCgiaWEvm6APuBA7CJsRtvZ7IlQVnfd6FI4V8rfvqV75Gq9fLva4k3Mc/640?wx_fmt=png&from=appmsg)

再看一下这几张图片，发现所有图片右下角P图痕迹明显，应该是把AI生成的文字P掉了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4afsVC4Bibw4d8RwRZg4F7Nt5ibxpiapUftl13RKsSdUJCMRmhXAHLTIOyXmBF1xYm5IVPabyhgq1ia8hFiaT5S9PjqKgSVLbb2PMKw/640?wx_fmt=png&from=appmsg)

一张一张用010打开看16进制信息

S01：豆包

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4aKkBpajJdAk0X6QWaXJ0T87QdMveTXwkxS78ZG4dF80s4XYXpSQUsfXxEAHxc6SJ59nx9QhZg70p8LrGx1fkyLzup1VS6AauM/640?wx_fmt=png&from=appmsg)

S02：文心

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4YmThEITA7yqEPcCcc8Jyy89m0Veicy4FUibfib...
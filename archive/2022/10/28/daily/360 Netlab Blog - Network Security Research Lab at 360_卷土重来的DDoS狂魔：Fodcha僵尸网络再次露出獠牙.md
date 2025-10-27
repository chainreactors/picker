---
title: 卷土重来的DDoS狂魔：Fodcha僵尸网络再次露出獠牙
url: https://blog.netlab.360.com/ddosmonster_the_return_of__fodcha_cn/
source: 360 Netlab Blog - Network Security Research Lab at 360
date: 2022-10-28
fetch_date: 2025-10-03T21:08:02.275791
---

# 卷土重来的DDoS狂魔：Fodcha僵尸网络再次露出獠牙

[![360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com/content/images/2019/02/netlab-brand-5.png)](https://blog.netlab.360.com)

* [Botnet](https://blog.netlab.360.com/tag/botnet/)
* [DNSMon](https://blog.netlab.360.com/tag/dnsmon/)
* [DDoS](https://blog.netlab.360.com/tag/ddos/)
* [PassiveDNS](https://blog.netlab.360.com/tag/pdns/)
* [Mirai](https://blog.netlab.360.com/tag/mirai/)
* [DTA](https://blog.netlab.360.com/tag/dta/)

[![360 Netlab Blog - Network Security Research Lab at 360 icon](/content/images/size/w30/2019/02/netlab_xs-2.png)
360 Netlab Blog - Network Security Research Lab at 360](https://blog.netlab.360.com)

—

卷土重来的DDoS狂魔：Fodcha僵尸网络再次露出獠牙

Share this

[Botnet](/tag/botnet/)

# 卷土重来的DDoS狂魔：Fodcha僵尸网络再次露出獠牙

* [![Alex.Turing](/content/images/2019/06/turing.PNG)](/author/alex/)
* [![Hui Wang](/content/images/2017/05/WechatIMG1.jpeg)](/author/huiwang/)
* [![YANG XU](/content/images/2019/04/head.jpg)](/author/xuy1202/)

#### [Alex.Turing](/author/alex/), [Hui Wang](/author/huiwang/), [YANG XU](/author/xuy1202/)

Oct 27, 2022
• 23 min read

# 背景

2022年4月13日，360Netlab首次向社区披露了Fodcha僵尸网络，在我们的文章发表之后，Fodcha遭受到相关部门的打击，其作者迅速做出回应，在样本中留下`Netlab pls leave me alone I surrender`字样向我们投降。本以为Fodcha会就此淡出江湖，没想到这次投降只是一个**不讲武德的假动作**，Fodcha的作者在诈降之后并没有停下更新的脚步，很快就推出了新版本。

在新版本中，Fodcha的作者重新设计了通信协议，并开始使用xxtea和chacha20算法对敏感资源和网络通信进行加密，以躲避文件&流量层面的检测；同时引入了**OpenNIC 域名**做为主选C2，**ICANN 域名**做为后备C2的双C2方案。这种冗余机制，既能防止C2被接管，又有良好的健壮性，能够维持其主控网络的稳定。

依托于背后团队强大的N-day漏洞整合能力，卷土重来的Focha与之前对比可谓有过之而无不及。在我们的数据视野中，**从规模来看**，Fodcha再次发展成日活Bot节点数超过60K，C2域名绑定40+IP，可以轻松打出超过**1Tbps**流量的大规模僵尸网络；**就活跃程度而言**，Fodcha日均攻击目标100+，累计攻击目标2万多，在10月11日到达了攻击的巅峰，单日“**丧心病狂**”的攻击了**1396个目标**。

在极短的时间内重回巅峰，Fodcha的作者似乎忘了闷声发大财的道理，竟然又开始主动"招惹”我们，在某次扫描的脚本中使用`N3t1@bG@Y`字样的leetspeak，翻译过来就是"`NETLABGAY`"，这么明目张胆的黑Netlab，让我们觉得它多多少少有些“皮痒”了。

鉴于Fodcha的规模&活跃程度带来的巨大危险性，以及非常嚣张的挑衅，我们决定撰写本文向社区分享我们的发现，一起打击Fodcha的嚣张气焰，共同维护网络安全。

# 时间线

依托于360Netlab强大的BotMon和DDoSMon系统，我们对Fodcha的样本演变和DDoS攻击指令一直保持着良好跟踪，下面是我们看到的样本演变以及一些重要的DDoS攻击事件。（注：Fodcha样本本身没有特定的标志表明其版本，这是我们内部为了跟踪方便而定的版本号）

* 2022年1月12日，首次捕获到Fodcha僵尸网络样本。
* 2022年4月13日，首次向外披露Fodcha僵尸网络，包含版本V1，V2。
* 2022年4月19日，捕获版本V2.x，使用**OpenNIC's TLDs风格的C2**（全文简称OpenNIC C2）。
* 2022年4月24日，捕获版本V3，使用xxtea算法加密配置信息，新增**ICANN's TLDs风格的C2**（全文简称ICANN C2），和OpenNIC C2构成冗余机制；新增反沙箱&反调试机制。
* 2022年6月5日，捕获版本V4，使用结构化的配置信息，去除反沙箱&反调试机制。
* 2022年6月7&8日，监控到Fodcha对**某国的某地的健康码机构**进行了DDoS攻击。
* 2022年7月7日，捕获版本V4.x，额外新增一组ICANN C2。
* 2022年9月X日，在协助**某国的某执法机构**固定某公司语音业务被DDoS攻击的证据链过程中，发现攻击背后有Fodcha的影子。
* 2022年9月21日，**某知名云服务商**就一起流量**超过1Tbps**的攻击事件向我们咨询，经过数据的交叉比对，确定攻击方为Fodcha。

# 规模推测

国外合作伙伴的数据表明Fodcha 4月份时全球日活Bot的数量为6W([参考我们另一篇文章](https://blog.netlab.360.com/fodcha-a-new-ddos-botnet/))，关于Fodcha僵尸网络的目前规模，我们没有确切的数字，但通过对比Fodcha 4月和10月在C2 IP数量上的差异，我们从技术上出发，有个未经验证的猜测：目前Fodcha的日活Bot数量超过6W。

推测过程如下：
僵尸网络的规模与C2 IP的数量存在一个正向关系，最朴素的观点是：“僵尸网络规模越大，所需要的C2基础设施也越多”。在4月份，Fodcha被处置之前，其作者为维持6W的规模，投入了10个C2 IP；随后Fodcha开始了自己的复活之旅，我们观察到一个现象，随着Fodcha的复苏，其C2域名对应的IP在持续增加。时至今日，Fodcha的作者投入了多少C2 IP呢？使用dig命令查询最新的C2域名`yellowchinks.dyn`的绑定IP，可以看到数量是44。
[![](https://blog.netlab.360.com/content/images/2022/10/fodcha_c2infras.png)](https://blog.netlab.360.com/content/images/2022/10/fodcha_c2infras.png)

可以说我们见证了Fodcha的C2 IP一步步从几个增长到今天的40+，可能的解释是作者人傻钱多无脑上资源，但结合其迅猛的传播以及历史上曾看到的万级规模，他们增加C2 IP更可能的原因是因为其僵尸网络规模太大，需要投入更多的IP资源，以使Bot与C2之间在数量上有一个合理比例，达到负载均衡。

综上，我们从C2 IP数量上大幅度的增长，推测目前Fodcha的规模大于4月份，日活Bot数量超过6W。当然**再合理的推测也还是假设**，欢迎有视野的社区伙伴**不吝指正**。

# DDoS统计

回到C2 IP 44这个数字本身，纵然我们和僵尸网络battle多年见多识广，但这个数字依然让我们感到惊讶。世上没有无缘故的爱，光是这些IP资源，就得花费不少的，Fodcha的作者为什么愿意花这个钱呢？答案是DDoS攻击让他赚到了钱。我们节选了2022年6月29至今的数据，其攻击趋势和目标区域分布如下：

[![](https://blog.netlab.360.com/content/images/2022/10/image.min-1.png)](https://blog.netlab.360.com/content/images/2022/10/image--1-.png)
可以看出：

* 无愧于DDoS狂魔的称号，攻击几乎没有停歇，几乎打遍全球，日均攻击事件1K+。
* 中美两国颜色较深，说明两国累计被攻击目标及次数较多，综合考虑到两国在互联网上业务的比重原本就比较大，这里的“看起来多”是一种正常状况。

攻击指令在7天内的时间分布如下所示，可以看出Fodcha发起的DDoS攻击遍及**7 \* 24**小时，没有明显的时区性，我们倾向Fodcha是一个商业驱动的僵尸网络。

[![](https://blog.netlab.360.com/content/images/2022/10/fodcha_instimezone.png)](https://blog.netlab.360.com/content/images/2022/10/fodcha_instimezone.png)

# 样本分析

我们将捕获的样本分成了４个大版本，其中在上一篇blog中已经分析过V1V2，此处就不再赘述了，本文选取最新的V4系列样本为主要分析对象，它们的基本信息如下所示：

```
MD5: ea7945724837f019507fd613ba3e1da9
ELF 32-bit LSB executable, ARM, version 1, dynamically linked (uses shared libs), stripped
LIB: uclibc
PACKER: None
version: V4

MD5: 899047ddf6f62f07150837aef0c1ebfb
ELF 32-bit LSB executable, ARM, version 1 (SYSV), statically linked, stripped
Lib: uclibc
Packer: None
Version: V4.X
```

Fodcha的Bot在被侵入设备运行时，首先会从`运行参数`，`网络的连通性`，`是否设置“LD_PRELOAD”环境变量`，`自身是否被调试`等方面进行检查，如果不满足要求就直接退出，这些检查可以看成是一种对通过模拟器&沙箱提取IOC的简单对抗。

当满足要求运行要求时，则首先解密出配置信息，在Console上输出**snow slide**，然后就是一些常见的主机行为，如单一实例，进程名伪装，操控watchdog，清空特定端口进程，上报特定进程信息等，我们认为这些主机侧的功能没有太多亮点，因此不再展开分析，下文将着重从解密配置信息，网络通信，DDoS攻击等方面对Fodcha进行剖析。

## 解密配置信息(Config)

Fodcha在V2.X，V3使用并列的Config组织方式，而在V4,V4.X中则使用结构化的Config组织方式，下图非常清楚的显示了它们的区别。

[![](https://blog.netlab.360.com/content/images/2022/10/fodcha_disconfig.png)](https://blog.netlab.360.com/content/images/2022/10/fodcha_disconfig.png)

虽然Config的组织方法不一样，但它们的加密方法是一样的，通过下面代码片段引用的常量可知，它们使用的是xxtea算法，密钥为`PJbiNbbeasddDfsc`。

[![](https://blog.netlab.360.com/content/images/2022/10/fodcha_xxtea.png)](https://blog.netlab.360.com/content/images/2022/10/fodcha_xxtea.png)

经过逆向，我们编写了以下IDAPYTHON脚本来解密配置信息。

```
# md5: ea7945724837f019507fd613ba3e1da9
# requirement: pip install xxtea-py
# test: ida7.6_python3

import ida_bytes
import xxtea

BufBase=0x1F2B0
ConfBase=0x0001F1A0
key=b"PJbiNbbeasddDfsc"
for i in range(17):
    offset=ida_bytes.get_word(i*16+ConfBase+2)
    leng=ida_bytes.get_word(i*16+ConfBase+4)-offset
    buf=ida_bytes.get_bytes(BufBase+offset,leng)
    print("index:%d, %s" %(i,xxtea.decrypt(buf,key)))
```

解密后的Config信息如下表所示，可以看到index 11还保留着“投降”的彩蛋，另外值得一提的是index 12，它是reporter服务器地址，Fodcha会将一些特定进程的信息上报给它。

| Index | Value |
| --- | --- |
| 0 | snow slide |
| 1 | /proc/ |
| 2 | /stat |
| 3 | /proc/self/exe |
| 4 | /cmdline |
| 5 | /maps |
| 6 | /exe |
| 7 | /lib |
| 8 | /usr/lib |
| 9 | .ri |
| 10 | GET /geoip/?res=10&r HTTP/1.1\r\nHost: 1.1.1.1\r\nConnection: Close\r\n\r\n |
| 11 | Netlab pls leave me alone I surrender |
| 12 | kvsolutions.ru |
| 13 | api.opennicproject.org |
| 14 | watchdog |
| 15 | /dev/ |
| 16 | TSource Engine Query |

## 网络通信

Fodcha的网络通信在代码层面有一个非常固定的特点：一个永真的While循环，通过switch-case进行各个阶段的处理，因此Fodcha各个版本的网络协议处理函数在IDA中产生的CFG图高度相似，这个特点可以帮助我们对样本进行辨别，对功能快速定位。

![](https://blog.netlab.360.com/content/images/2022/10/fodcha_cfg.png)

总的来说，Fodcha的网络通信要经过以下4个步骤：

1. 解密C2
2. DNS查询
3. 建立通信
4. 执行指令

### 0x1: 解密C2

Fodcha的不同版本支持的C2种类是不一样的，V2.X只有1组OpenNIC C2；V3&V4拥有1组OpenNIC C2，1组ICANN C2；而V4.X则是最多的，1组OpenNIC C2，2组ICANN C2，下面的图非常清楚的显示了它们的区别。

[![](https://blog.netlab.360.com/content/images/2022/10/fodcha_c2_dis.png)](https://blog.netlab.360.com/content/images/2022/10/fodcha_c2_dis.png)

虽然C2种类&数量不一样，但是它们的处理逻辑如下图所示，几乎是一样的，首先通过C2\_GET函数获得一个C2域名，然后通过DNS\_QUERY函数获得C2对应的IP，其中C2\_GET的第一个参数为C2密文数据，第2个参数为长度，而DNS\_QUERY的第2个参数则暗示了C2的类型。

![](https://blog.netlab.360.com/content/images/2022/10/FODCHA_c2compose.png)

通过C2\_GET可以获得一个有效的C2域名，它内部的实现可以分成2步：

* 首先得解密C2密文数据。
* 然后将它们构造成一个合法的域名。

### 解密C2密文数据

C2的密文数据使用了配置信息一样的加密方式，即xxtea，密钥也是**PJbiNbbeasddDfsc**，通过下面简单的IDAPYTHON脚本，即可解密出OpenNic C2数据。

```
#md5: 899047DDF6F62F07150837AEF0C1EBFB
import xxtea
import ida_bytes
import hexdump
key=b"PJbiNbbeasddDfsc"
buf=ida_bytes.get_bytes(0x0001CA6C,1568)  # Ciphertext of OpenNic C2
plaintext=xxtea.decrypt(buf,key)
print(plaintext)
```

解密后的C2数据如下图所示，可以看出C2数据由2部分组成，前面的是domain names，后面是TLDs，它们通过红框中的“**/**”符号分隔。

![](https://blog.netlab.360.com/content/images/2022/10/fodcha_c2plaintext.png)

### 构造域名

Fodcha有一个特定的域名构造方法，等效的Python实现如下所示：

```
# md5: 899047ddf6f62f07150837aef0c1ebfb
# requirement: pip install xxtea-py
# test: ida7.6_python3

import xxtea
import ida_bytes

def getcnt(length):
    cnt=1
    while True:
        cnt +=1
        calc=2

        for i in range(1,cnt):
            calc+=2+12*i%cnt

        if calc +cnt==length-1:
    ...
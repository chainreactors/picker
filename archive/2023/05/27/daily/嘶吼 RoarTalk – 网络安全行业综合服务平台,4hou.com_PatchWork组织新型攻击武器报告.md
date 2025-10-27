---
title: PatchWork组织新型攻击武器报告
url: https://www.4hou.com/posts/RKPz
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2023-05-27
fetch_date: 2025-10-04T11:38:04.891974
---

# PatchWork组织新型攻击武器报告

PatchWork组织新型攻击武器报告 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# PatchWork组织新型攻击武器报告

知道创宇
[行业](https://www.4hou.com/category/industry)
2023-05-26 11:54:24

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)105285

收藏

导语：EyeShell武器披露

**1、PatchWork组织描述**

Patchwork APT 组织，也称为 Dropping Elephant、Chinastrats、Monsoon、Sarit、Quilted Tiger、APT-C-09 和 ZINC EMERSON，于 2015年12月首次被发现，使用一套定制的攻击工具，针对多名外交官和经济学家发起攻击。这些攻击通常是通过鱼叉式网络钓鱼活动或水坑攻击进行的。该组织被怀疑由一个隶属于南亚某国的威胁行为者运营，主要攻击目标是巴基斯坦、斯里兰卡、尼泊尔，孟加拉国、中国、缅甸、柬埔寨等国。

近2年来知道创宇404-高级威胁情报团队多次提前&即时发现该组织针对国内重点高校、研究院、科研所等相关研究组织机构开展攻击活动，多次成功预警。

**2、武器基本信息**

![image.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685073094188995.png "1685073094188995.png")

**3、武器功能模块图**

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685073095170871.png "1685066918314571.png")

**4、EyeShell武器综述**

近期404-高级威胁情报团队在对PatchWork的持续追踪过程中，发现其武器库中出现了一款由.NET开发的精简后门，目标框架为.NET Framework 4，狩猎追踪过程中我们发现该后门与BADNEWS[1]共同出现，故我们有理由猜测该后门用于配合BADNEWS共同使用，该后门使用的命名空间为Eye，为了方便后续追踪及区分，我们根据命名空间将这款后门称之为EyeShell。

【1】BADNEWS为PatchWork组织专用自研木马名称。

**4.1 EyeShell功能描述**

EyeShell整体来看是一款非常精简的后门程序，推测其版本为v1.0版本，EyeShell按功能模块划分可将整体划分为三个模块，分别如下：

* **初始化模块**

初始化模块分为两个部分，间隔点为C2是否在线。

**第一部分用于程序初始化，**内容如下：

本次发现的EyeShell创建的互斥体为“fdghsdfgjhh”，互斥体用于确保程序唯一运行，避免发生竞争问题。

C2地址及端口采用数组的方式保存：

```
char[] C2Address = new char[13]
 {
    '1', '7', '2', '.', '8', '1', '.', '6', '1', '.',
    '2', '2', '4'
   };
int[] C2Port = new int[4] { 2, 0, 2, 4 };
```

由于EyeShell的C2信息使用的是数组保存，进行Connect(string hostname, int port)API调用时会进行一次类型转换，地址在转换string类型时只需要强制转换即可，EyeShell在处理端口时采用的方式是遍历幂运算累加的方式：

```
C2Port.Select((int t, int i) => t * Convert.ToInt32(Math.Pow(10.0, pop.Length - i - 1))).Sum()
```

EyeShell的所有网络交互均采用AES-128加密：

```
AESKey = {'q', 'w', 'e', 'r', '1', '2', '3', '4', 'a', 's', 'd', 'f', '5', '6', '7', '8'};
AESIV = {'7', '3', '9', '1', '8', '4', '2', '6', '5', '7','8', '9', '5', '1', '2', '3'}
```

向服务端发送数据的加密方式与服务端下发命令所采用的加密方式相同，采用的处理流程为原始数据（byte[]）---> To Base64 ---> To AES-128 ---> To Base64(最终发送的数据)。

**第二部分用于交互初始化**

交互初始化需要一个前置条件，当且仅当C2在线时才会进行交互初始化。

交互初始化主要内容为创建cmd.exe进程并创建OutputData Received事件，通过OutputHandler事件委派将标准输出流重新导向

TCPStream写入接口，从而达到将标准输出流重定向至服务端操作，EyeShell在完成事件委派后会创建TCPStream Read/Write两个接口分别为后续交互提供支持。

其中Write接口与OutputHandler事件委派中的重定向产生关联。

* **上线模块**

在初始初始化完成后，EyeShell会尝试进行C2在线检测，直到C2在线后才会进行后续操作否则将持续检测C2是否在线。

如若C2在线EyeShell收集的上线信息分别为UUID、UserName、OSVersion，上线格式如下:

其中根据经验来看上线信息尾部的硬编码字符\*1.0我们猜测为EyeShell版本号v1.0。

完成上述操作后EyeShell进入交互模块。

* **交互模块**

交互模块是一个死循环模块，交互开始是通过从TCPStream Read接口读取服务端下发的指令，根据EyeShell的命令控制列表。我们可以确定EyeShell支持十三条指令，相关指令及功能如下所述：

"drive"

该指令含义为枚举并向服务端上传当前主机的逻辑卷名称，上传格式如下：

"fileData"

该指令含义为获取指定文件大小，如果为目录则会获取当前目录其子目录大小。异常则返回“0”。

"FileRec"

该指令含义为获取当前目录其子目录名称。上传格式为：

fo\*l\*d\*er +"\*"+

"FileList"

该指令含义为列举当前目录、子目录及目录中文件名称，类似于ls指令上传格式类似由"\*"分割。

"downFile"

该指令含义为将受害主机中指定的文件上传至服务端，若长传成功服务端返回"Done"。

"upload"

该指令含义为从服务端下载文件保存至受害主机指定路径,成功则返回"asdf"。

"Exec"

该指令含义为执行受害主机中的指定文件,执行成功返回"asdf",否则返回异常信息。

"Delete"

该指令含义为删除受害主机中的指定文件,执行成功返回"asdf",否则返回异常信息。

"Rev"

该指令用于执行服务端下发命令,并更改OutputHandler事件委派中的返回状体为开启,此时服务端与客户端建立起交互式Shell。

"RevEnd"

该指令用于关闭交互式Shell,更改OutputHandler事件委派中的返回状体为关闭,此时服务端与客户端关闭交互式Shell。

"ScreenS"

该指令用于获取受害主机当前桌面屏幕截屏。

"UplExe"

该指令有两个操作：

操作一：从服务端下发文件并保存至受害主机%temp%路径下的指定文件名称并立即执行。

操作二：获取当前进程的ID并将该数据保存在%temp%\\ip1.txt文件中。

"Alive"

无操作,使客户端进入等待状态。

**4.2 EyeShell细节描述**

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685073096206540.png "1685067875204042.png")

网络流加密流程

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685073097146590.png "1685067913117363.png")

网络流解密流程

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685073098968648.png "1685067957203787.png")

AES-128 KEY&IV

![图片5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685073099945846.png "1685068048174276.png")

互斥体创建及初始化C2

![图片6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685073099535937.png "1685068076136767.png")

初始化Shell并创建事件委托

![图片7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685073100769582.png "1685068136792836.png")

事件委托

![图片8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685073101146951.png "1685068177187954.png")

创建TcpStream 读写接口

![图片9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685073102218616.png "1685068198125661.png")

构建并发送上线信息

![图片10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685073102108489.png "1685068229684670.png")

交互入口

![图片11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685073106641243.png "1685068261100379.png")

获取文件列表

![图片12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685073106905311.png "1685068293851319.png")

获取逻辑卷信息

![图片13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685073107741908.png "1685068392137677.png")

文件上传

![图片14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685073108159364.png "1685068441911059.png")

获取文件大小

![图片15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685073109534244.png "1685068469385582.png")

获取屏幕截图

![图片16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685073109524075.png "1685068497185657.png")

文件保存执行及PID获取

![图片17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685073110996958.png "1685068522184477.png")

创建指定进程

![图片18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685073110888680.png "1685068569112219.png")

删除指定文件

![图片19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685073111928048.png "1685068596172142.png")

启动交互式Shell

![图片20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20230526/1685073112429391.png "1685068623926277.png")

获取目录信息

如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?C0a3o6J5)

#### 你可能感兴趣的

* [![]()

  Exchange/M365最新防范攻略！CACTER三步补齐原生防护短板](https://www.4hou.com/posts/l03l)
* [![]()

  【附下载】2025我们身边的 网信安全 典型案例等 官方视频汇编](https://www.4hou.com/posts/kg3x)
* [![]()

  蝉联荣誉！梆梆安全再度获选 “北京市委网信办第二届网络安全技术支撑单位”](https://www.4hou.com/posts/9jKP)
* [![]()

  聚焦可信AI安全！SDC2025 议题重磅揭晓](https://www.4hou.com/posts/gy39)
* [![]()

  2025第五届太原网络安全高峰论坛成功举办](https://www.4hou.com/posts/8gJl)
* [![]()

  特勤局手册 | 监听办公室](https://www.4hou.com/posts/42B2)

![](https://img.4hou.com/wp-content/uploads/2017/06/8d9ea59c3169aaafa877.jpg)

# [知道创宇](https://www.4hou.com/member/e99P)

网...
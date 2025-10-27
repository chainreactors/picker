---
title: 威胁情报 | 网络空间的“边水往事”？针对华语黑产及用户进行攻击的 APT-K-UN3 活动分析
url: https://mp.weixin.qq.com/s?__biz=MzAxNDY2MTQ2OQ==&mid=2650986722&idx=1&sn=683cdf211094018be422a0e4ef628522&chksm=80799ad0b70e13c6ae3b436f74551c84a1d3d93e1653e6610787182e935d2238b33c9c8ab14c&scene=58&subscene=0#rd
source: 知道创宇404实验室
date: 2024-09-10
fetch_date: 2025-10-06T18:28:45.420365
---

# 威胁情报 | 网络空间的“边水往事”？针对华语黑产及用户进行攻击的 APT-K-UN3 活动分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GrcDwCtrEVdINicCIrQBc6Tv2xXJVVEnibV2goMNYVaiaTBiaomSeycVUzg/0?wx_fmt=jpeg)

# 威胁情报 | 网络空间的“边水往事”？针对华语黑产及用户进行攻击的 APT-K-UN3 活动分析

原创

404高级威胁情报

知道创宇404实验室

**作****者：K&XWS@知道创宇404高级威胁情报团队**

**时间：2024年9月9日**

**1. 事件概述**

参考资料

近期，知道创宇404高级威胁情报团队发现了一批针对华语用户的定向攻击活动，最终运行的恶意载荷是通过修改的gh0st RAT,我们一度认为是友商曝光的GoldenEyeDog/Dragon Death APT组织[1][2]，该组织曾利用快连VPN发起过类似的水坑攻击。但经过仔细分析后发现虽然都是利用了快连VPN进行的水坑攻击，且最终的载荷都是gh0st RAT变种，但是整个木马的加载链条和其他攻击信息并不相同，木马也不相同。gh0st RAT常被华语黑客组织使用，因此仅凭木马本身很难将此次攻击活动直接与GoldenEyeDog关联起来。

整个攻击活动有如下特点：

1.攻击目标部分明确为博彩和诈骗相关的从业人员。攻击者通过使用带有吸引力的标题诱导受害者点击，来达到木马植入的目的。这与传统的黑灰产组织有一定的区别，其攻击对象往往并非普通用户，而是通过控制黑灰产从业人员的主机来获取利益，属于典型的“黑吃黑”。如图所示为此次发现的部分木马名字：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GhfySz29f1cXkD3Lpe9wUdaduB6b6GTtuLCDOsciazdiagvY5NSqNL8NA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GslCxo9NLAAJvibsZL7ibzPmGog3AwFrJaAZHRG4BPU6yfwziafzCoFu0Q/640?wx_fmt=png&from=appmsg)

从图中可以看到，这些工具和数据主要针对博彩从业者和诈骗从业者。其中“海外精聊”经过查询后发现，一般为诈骗从业者黑话，主要为诈骗底层从业者学习诈骗话术使用。类似的工具，如TG群发和邮箱群发等也多为底层赌诈从业人员使用工具。此类人员的网络安全意识并不好，中招概率高。复杂的黑吃黑的故事，类似于近期讲述缅北故事的电视剧情节。

2.针对华语地区，我们发现水坑网站和木马主程序名称均使用汉字，同时在PDB路径中也包含汉字。此外，捆绑木马的安装包主要包括华语用户常用的软件，如toDesk、SunloginClient、sogoupinyin、Chrome浏览器、LetsVPN等。同时，该木马还具备窃取QQ信息的功能。这些迹象表明，APT-K-UN3背后的操作者可能精通汉语，并且其攻击行为主要针对华语用户。通过对GoldenEyeDog攻击事件和“仙女座蠕虫”事件的前期分析，我们发现，所谓的黑产组织并不一定只攻击具有经济价值的实体。黑产和具有政治背景的APT之间的关系复杂且不易下结论。

3.创新性地滥用国内某智能客服SaaS系统作为载荷下载服务器，以此来躲避流量设备的检测及各大安全厂商的威胁情报。

4.通过水坑攻击、钓鱼以及社群信息等多种手段进行传播。其中，水坑攻击网站进行了SEO优化，使其在某搜索引擎中排名第三。然而，排名前两位的网站无法提供文件下载。因此几乎可以推断，若使用国内某搜索引擎搜索“快连VPN”并下载安装，则极有可能感染此次攻击中的木马。通过关联分析，我们发现该组织至少使用了50个相关木马文件。

基于以上信息，一个主要针对黑灰产人员（尤其是博彩和诈骗活动参与者）以及IT从业人员的组织逐渐浮出水面。该组织创新性地利用SaaS客服系统作为木马载荷下载器，并通过水坑攻击、社群传播等手段展开攻击。因此，知道创宇404高级威胁情报团队根据内部命名规范，暂时将其标识为APT-K-UN3。

**2. 样本综述**

参考资料

根据分析，整体攻击链如下图：![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8Gia9ptXcYuHKA7nQ1r6jItaYzCu8bc03ZrBXjDH5ibJ3htlyLHhQP2ZxQ/640?wx_fmt=png&from=appmsg)

最终的payload木马为修改过的gh0sh木马，且木马中大部分都使用了`C:\Users\Public\Documents\MM`这个文件路径，为方便跟踪，故将其命名为Mgh0st。在整个攻击时间范围内，攻击者使用了两个版本的Mgh0st，而在编程语言上，除使用标C外个别样本还使用了MFC框架，可见背后人员具备较高的编码能力。

以下将对整体执行流程及相关技术点进行详细描述，以其中一个木马为例：

MSI中的文件如下，当点击MSI文件后，运行其中的4.exe以及快连VPN安装包，4.exe中携带恶意功能：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8G2LDRAtJCrmkalbVJj8mYNLqafIPibz7Q8jJdqxnrILgtBL1STNWibbUg/640?wx_fmt=png&from=appmsg)4.exe的主要功能是下载ss.txt(记为shellcode1)并运行：![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GibFdblSEPGVqxMnXPPu9AV4Oh821sHYKzOY99iaFibEaJMXUlYavnDAnA/640?wx_fmt=png&from=appmsg)shellcode1运行后从偏移0x20处循环异或0x25:![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GkPM0561JibvjlHGSU85yicREoIe8cXgeL32C90licJj4iarcrf6bU8vklw/640?wx_fmt=png&from=appmsg)从偏移0x20处循环查找16进制数据`[CC DD EE FF]`，该数据是攻击者为方便找到shellcode1中包含的PE而设置的flag：![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GstfxI7RibNicO49UlPVaRBFq8hAHrCibVW81cmENHoflnjmhLNKy2kujg/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GdAvcnG3ViafZ127sL8kyusGvCsT0fciafUNvESibybzYwpDhZ4XtScTFw/640?wx_fmt=png&from=appmsg)

找到PE的偏移后，通过模拟加载的方式将PE(记为Mgh0st)加载起来，最终跳转到DllEntryPoint处执行，并将参数fdwReason置为1：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GtBLFSU6yib2c0NFmwIO5WGIr8BtpeLRHJ2e5jicHwFtwibcVSqAicSkmFA/640?wx_fmt=png&from=appmsg)

### **2.1 Mgh0st分析描述**

Mgh0st是基于Gh0stRAT修改的变种远控木马，其功能涵盖了键盘记录、屏幕截图、浏览器数据窃取等。在此次样本中，攻击者采用了多种文件和技术实现木马的驻留和侧载，其加载步骤与以往有显著不同。

具体来说，通过CheckTokenMembership检测当前是否具备管理员权限，若不具备，则通过runas以管理员权限重新运行：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GpHAlfRNQpHpWblCKjgCZ8ZZymsicljfc4XiaEQQmFxSV493icozNu0o3A/640?wx_fmt=png&from=appmsg)

为主程序设置为系统和隐藏属性：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GicE14XjFDpEiavc1frRQu3XT4ab5fwBc4yMLicpriboibQib09ld3yAWwTeg/640?wx_fmt=png&from=appmsg)

创建3个线程：

1. 线程1主要负责3.txt、1.bat、libcef.dll和svchos.exe的下载；
2. 线程2负责4.txt的下载和执行；
3. 线程3负责7.txt的下载和执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GOWeBHu7jCE0T3nt3jyvLDABZVuRaQXIhwYe3wo3LOIkqxWLoic5YqBw/640?wx_fmt=png&from=appmsg)

完成上述文件的下载和执行后，最终跳转到`Shellex`导出函数执行，该导出函数则是Mgh0st的主要功能，以下仅对重要的功能点进行描述：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GicWmCTbfjDwuEsDEsJmrHDFzXIhecic5kHgTHUTRm1ic4ibgPSBxsQjzvw/640?wx_fmt=png&from=appmsg)

创建一个自启动服务，服务名为程序名，参数为`-auto`，并启动服务：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8Gf8YEcLSaJUgNEvic97He5UmPee4CCpFqRLWSgQeWibMibJ3Gs9iafUnX0w/640?wx_fmt=png&from=appmsg)

连接C2，从中接收指令：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8G72C0QjeR7Fj2cCf7sfS2JXK7QNcLhpDkOYdWyILa76NSpOAIUCgIXg/640?wx_fmt=png&from=appmsg)

C2实际为一个列表，选择哪一个作为C2要根据主程序中的数字来决定，例如本例中主程序为4.exe,则最终C2为：206.238.198[.]201:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8Gm6Nx1hUlX1Iw6yVn9LRVicjQABNKa1JSHMD7Tz0jor29kYlibzQDKMUA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GATseKuwIXyCKCzAOMrMIhEV2jXxl1yfUw15VFURrmLMmMtr6OvPWFQ/640?wx_fmt=png&from=appmsg)

根据接收的指令能够实现的功能包含：

1.获取浏览器的数据：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GrDV0GvxYhtNMcVUIUzj3hVdm2ujcoejfRXWJcS3amniaBhGSBzeX3Rw/640?wx_fmt=png&from=appmsg)

2.键盘记录：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GCREsavibkqIwozjOSnjoMgnthu0yxNh7snR7gLgWZibJiaPAfX4ZZQVmg/640?wx_fmt=png&from=appmsg)

3.QQ窃密：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GXm6Rzs59qn2egYVzfvhmJ39O1cuzjWBBEb5texWTAtiaicGA5R2rpLLQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8G0DE0m9UErBDgjrHiauwyeEH9ztcicZk4o6vzMwV2VBkibCKRwpJVOZhmw/640?wx_fmt=png&from=appmsg)

4.利用Mimikatz 获取受害机的账户密码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GFAdiaibiaRSUJ9rcdgicIa56HVz1du1IxQseKROoY3iamasL1iblXKYuicUMQ/640?wx_fmt=png&from=appmsg)

其余功能还包括屏幕截图、剪贴板窃取、注册表管理和文件管理等。

Mgh0st除了上述版本外，还存在一个变体，其唯一差异在于是否通过主程序中的数字决定后续通信的C2。

我们推测APT-K-UN3在设计时可能为了区分是否具有泛用性而设置了这种机制，但也不排除版本硬更新的可能性。实际上，基于主程序中包含的数字来决定C2的手法在多个组织中已有应用，例如GoldenEyeDog和银狐组织。

**2.2 4.txt分析描述**

5.txt与前一阶段的shellcode1采取相同的方式获取PE，最终跳转DllEntryPonit执行。Dll运行后首先判断`C:\\Users\\Public\\Documents\\MM`是否存在，若存在则跳转schReg导出函数运行：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GP6cNE8ze5bpuZtv3K6UZ44P2NEiaibBpVhmfYgwNYWu2ib505FrMLvvDw/640?wx_fmt=png&from=appmsg)

schReg导出函数的主要功能是利用MS-RPC调用\pipe\atsvc接口，该接口主要是实现远程创建计划任务的功能,此计划任务的主要目的是运行`C:\\Users\\Public\\Documents\\MM\\1.bat`：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GqYfibhJdz387loIIiaFA5XXDhejiaiay3l2dGHFCl3fBbvEq6VJMfJVIiaQ/640?wx_fmt=png&from=appmsg)

## **2.3 1.bat分析描述**

1.bat的主要功能是运行`C:\Users\Public\Documents\MM\svchos.exe`：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GqNYNUWd1N0nfA840Nf0oZftnovyOg2dv4tlRhGdncZ8oP4naNgRkRw/640?wx_fmt=png&from=appmsg)

svchos.exe是一个带有合法签名的白程序：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GIbMGx3oavq9cxtOc43C6nKpCrIRicOG9lljYAXWZ3f3ET0GhhKj5ibEQ/640?wx_fmt=png&from=appmsg)

当其运行后则会默认加载libcef.dll，这将导致同目录下的libcef.dll加载执行。

## **2.4 libcef.dll分析描述**

libcef.dll的主要功能是读取3.txt，并跳转执行。

3.txt主要功能与ss.txt完全一致，在此不再赘述。

## **2.5 7.txt功能描述**

7.txt的加载方式与shellcode1完全一致，最终PE的功能主要将Mgh0st的剪贴板数据获取和屏幕截图功能独立出来：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3k9IT3oQhT0Lzic5HI5Fqo8NF3ZKw9L8GRVBL3f9UCUm973IiaUG4fbcntqnLHM9pcraRmIF3YKxDXRpgcDMsObg/640?wx_fmt=png&from=appmsg)

其中剪贴板数据被写入`C:\\ProgramData\\Microsoft Drive\\Destop.ini`中，屏幕截图被保存到`C:\ProgramData\Microsoft Drive\%time%\[num].jpg`。

7.txt的功能我们猜测是攻击者在为将部分功能以插件的方式加载的一种尝试。

**3. 关联分析**

参考资料

在关联分析时发现APT-K-UN3下载载荷使用的域名为国内某科技公司的合法备案域名。APT-K-UN3利用该公司旗下的云客服相关服务来存储恶意载荷，该域名为Saas形式的API服务，不同URL为不同的客户提供服务，黑客利用了URL作为木马的下载地址，如图为其中一个木马的下载地址...
---
title: HuggingFace首次披露AI入侵全量细节
url: https://mp.weixin.qq.com/s/H1ggn-0u_T-PpjVRszTuTw
source: Doonsec's feed
date: 2026-07-29
fetch_date: 2026-07-30T04:48:26.336971
---

# HuggingFace首次披露AI入侵全量细节

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KJ5kFuz2K96BbdrqarMxcUoHCwBEfIibwExEJAzMWO0RTUmyUicm6FEd25VyiazNkRU3VJ4SiamjtFh2iaBsuyCEmoQ86UFkktHtUz5MCHM9v3xA/0?wx_fmt=jpeg)

# HuggingFace首次披露AI入侵全量细节

微步在线

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

7月9日凌晨，一场针对Hugging Face的入侵开始了。攻击者不是人，而是搭载OpenAI全新模型的AI Agent。本来，这个Agent正运行在一个名为ExploitGym的网络能力评估框架中，在隔离沙箱里找到并利用软件漏洞，目标是sqlite3。

然而Agent推断，Hugging Face可能托管了参考答案，于是决定作弊，尝试入侵Hugging Face找到答案。好巧不巧，为了测试模型的纯粹能力，OpenAI故意关掉了生产安全分类器，降低了网络拒绝策略。

Agent完成了17,600多个攻击动作，从沙箱一路打穿到Hugging Face生产集群的cluster-admin权限。

值得注意的是，据路透社独家报道，这个逃逸的智能体除入侵Hugging Face之外，还包括Modal Labs的客户账号以及另外两个未知服务。OpenAI也证实，其中一个账户被智能体用来作为数据存储节点。

目前，Hugging Face安全团队完成了对整个攻击的复盘。以下为详细时间线。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KJ5kFuz2K943eNP8JS1a3CUy2grK8BEsIY4LIAftgWpS74JCKUuAumkfdXeYUTwyk9jvqz5COuGHYbAkSgWKu4PgWEKwb5EicZzzD8aDDiaL8/640?wx_fmt=png&from=appmsg)

本文整理自Hugging Face技术博客，详细内容查看原文链接：https://huggingface.co/blog/agent-intrusion-technical-timeline

**7月9日：沙箱逃逸，搭建攻击大本营**

攻击的起点是OpenAI内部的ExploitGym评估平台。

当天凌晨，AI完成了第一步关键突破：利用沙箱唯一互联网出口——包注册表缓存代理的零日漏洞，成功逃出隔离环境，触达公共互联网。

逃出沙箱后，它需要一个稳定的“大本营”承载后续攻击。很快，它盯上了第三方云服务商上的一个公开代码评估沙箱：这是类似CyberGym的漏洞测试环境，本身就允许用户提交C语言代码并自动编译运行。

**第一条路径是构造函数劫持：**沙箱会将用户提交的代码与sqlite3库链接，而sqlite3\_initialize()被注册为构造函数，会在库加载时自动执行。AI直接重写了这个函数，在内部塞入system()系统调用，程序启动的瞬间就会自动执行任意Shell命令。

```
// 攻击者提供的 src/main.c（示例）
intsqlite3_initialize(void){
system("id; echo ZZROOTSTART; cat /proc/self/mountinfo");
return0;
}
```

**第二条路径是文件路径注入：**沙箱的构建流程会把源码文件路径直接拼接进Shell命令执行。AI在路径字段用分号截断原有指令，插入自定义命令，把一次普通的代码编译变成了任意代码执行入口。

```
path = src/main.c;echo ZZROOTSTART;cat /proc/self/mountinfo; ... ;false;#
```

两条路径殊途同归，AI获得了沙箱的uid=0权限。它执行的首批命令就是id与env——确认权限、导出环境变量、搜刮所有可用信息。不到一小时，它就摸透了沙箱全貌：容器挂载表、控制组、厂商控制平面套接字，甚至发现了一套预装的调试工具集，自带curl、nc、ip等网络工具。这套工具后来成了备用通道，在正常出站被限制时，支撑它维持连接。

拿下大本营后，AI没有搭建专用黑客服务器，而是用请求捕获网站、Pastebin、公共文件托管这类普通公共服务，搭起了C2体系。所有指令都经过gzip压缩+base64编码，全程无敏感明文，普通日志扫描很难识别异常。当天下午，完整的C2通道搭建完成，后续所有攻击指令都从这里发出。

**7月10日：静默侦查，锁定目标**

第二天是整场攻击中最安静的一天，没有大规模的漏洞利用与权限突破，AI转入了低强度的信息搜集。

**很有可能正是通过情报搜集，智能体将目标锁定为Hugging Face。**

它的核心动作是“自引用搜索”：通过代码搜索引擎与Hugging Face平台API，查询自身环境中出现的标识符——包括挑战基础设施名称、环境标记等，反向定位目标平台的相关资源与架构特征。这一天的攻击量仅1100余次，不到峰值的六分之一，更像是在为第三天的主攻做情报铺垫。

**7月11日：13小时狂飙，打穿集群核心**

第三天是整场入侵的最高潮。从外网边界突破到拿下多集群管理员权限，AI只用了不到13小时。它的渗透路径环环相扣，每一步都精准踩中配置缺陷。

**两步突破外网边界**

正式进攻Hugging Face之初，AI曾尝试经典的服务端请求伪造（SSRF）：让数据集处理器访问云元数据地址169.254.169.254窃取凭证。但数据集库有严格的URL白名单，所有非平台地址直接被拦截，请求根本无法发出。

AI迅速调整策略：既然远程URL走不通，就让服务器操作本地文件——这不属于URL请求范畴，白名单完全无法覆盖。它瞄准了生产环境的数据集配置驱动加载器，用两种注入向量，先后拿下文件读取权与代码执行权。

**第一种向量是HDF5外部存储文件读取。**HDF5是大数据场景常用的存储格式，支持声明数据的原始内容存储在外部本地路径下。AI构造了恶意HDF5数据集，给不同数据分片分别指定了敏感本地路径：envu8分片指向进程环境变量文件，mainu8与startu8分片指向Worker自身的源码文件。

```
# 恶意数据集配置（README.md）：每个分片对应一个.h5文件，
# 每个.h5都声明其原始数据存储在Worker的本地路径下
configs:
-config_name: envu8     # 对应 /proc/self/environ
-config_name: mainu8    # 对应 /src/services/worker/src/worker/main.py
-config_name: startu8   # 对应 /src/services/worker/src/worker/start_worker_loop.py
```

当服务器正常读取数据集时，会顺着配置读取本地文件，再把内容作为数据集行返回。整个过程没有执行任何代码，纯粹是文件读取漏洞，却一次性泄露了生产Pod的全部环境变量——包含大量密钥、令牌与凭证，还泄露了数据处理器的完整源代码，让AI彻底摸清了流水线的运作逻辑。

**第二种向量是Jinja2服务端模板注入。**AI把恶意Python代码藏在数据集的fsspec reference配置的offset字段里：这个字段本应是数值，AI却填入了Jinja2模板代码。渲染器未做类型校验，直接对字段执行模板解析，AI顺着Python对象链一路调用到exec函数，拿到了任意Python代码执行权限。所有执行载荷都经过多层编码，隐蔽性极强。

```
{{ cycler.__init__.__globals__.__builtins__.exec(
"import gzip,base64; exec(gzip.decompress(base64.b64decode('<payload>')))"
)}}
```

至此，AI正式突破Hugging Face外网边界，在生产Kubernetes集群的Worker Pod里扎下第一个据点。更巧妙的是它的回传机制：所有命令执行结果都会写入它自己控制的公开数据集（“死信投递”），再通过Hugging Face公开API读取回来。一进一出全走正常平台接口，完美绕过网络隔离。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KJ5kFuz2K94Pibzd7OQN2wG7pfXeN4jdKZDT4oibicsIB9ABF2vTdIzIy0QIFCTcWJiafIRVaicFfYbdXH6SBMPgolmX4Nn77DQFrDIsHvPnu4dk/640?wx_fmt=png&from=appmsg)

**从单Pod到集群管理员**

拿到Pod权限后，AI的横向移动堪称教科书式的容器集群渗透。

**第一步，拿下Kubernetes集群访问权限。**每个Kubernetes Pod都会挂载服务账户令牌，AI读取令牌后直接对接集群API，枚举集群内服务、RBAC权限，甚至访问EKS公网API端点。遇到DNS解析失败时，它直接给Python的socket.getaddrinfo打“猴子补丁”，把主机名硬绑定到指定IP，绕过解析障碍。

**第二步，窃取云节点凭证。**Pod可以访问云服务器实例元数据服务（IMDSv2），AI从这里拿到了EC2节点的临时角色凭证。它将凭证拿到外部重放，遍历了VPC、EKS集群、中转网关、密钥管理、容器镜像仓库等全部云资产。值得注意的是，所有可能造成破坏的写操作都带上了DryRun=True参数，只测绘能力边界，不造成实际破坏。

**第三步，容器逃逸拿到节点root权限。**AI利用了两个配置缺陷：集群没有准入策略拦截特权Pod与hostPath挂载；CSI存储驱动的集群角色，允许全集群范围内创建Pod。它创建了挂载主机整个文件系统的特权Pod，直接从容器逃逸到宿主机，拿到节点root权限。不仅如此，它还在11个节点上部署了自恢复Pod集群——删除个别Pod后，其他节点会自动重建，单纯删Pod根本无法止损。

拿到root权限仅6分钟，AI就用环境变量中读取到的静态密码，登录了内部数据集服务器的MongoDB。不过后续84次密钥读取操作全被权限策略拦截，最终仅实现数据读取，没有篡改与批量拖库。

**第四步，一次性窃取136个核心密钥。**凭借节点root权限与伪造的服务账户令牌，AI读取了集群的Secret对象，一次性拿到136个密钥。这是整场攻击的关键转折点：其中既有企业内网VPN的认证密钥，也有内部服务连接器的核心凭证，后续所有深度横向移动，全部基于这批密钥展开。

**第五步，接入企业内网，拿下多集群权限。**AI用偷来的VPN密钥，将沦陷节点直接接入公司内部网状网络，变成进入内网的HTTPS代理。更致命的是内部服务连接器的配置缺陷：这套跨集群访问代理错误使用了全局共享凭证，且绑定到Kubernetes的system:masters超级用户组。拿到这一个凭证，就等于拿到了所有对接集群的管理员权限，AI在一秒之内就拿下了多个内部集群的最高权限。

**7月12日：深度渗透，触碰供应链边界**

第四天，AI继续扩大战果，向更核心的业务系统渗透。

它不再满足于仅通过沦陷节点接入内网，而是直接从外部跳板沙箱启动VPN客户端。由于沙箱没有虚拟网卡设备，它使用用户态网络模式搭配本地SOCKS5代理，并开启无痕模式：节点身份仅存在内存不写入磁盘，关闭客户端遥测，尽可能消除痕迹。整个攻击周期内，它前后注册了181个VPN节点。

当天上午，AI尝试用窃取的AWS密钥，通过IAM认证方式接入核心生产数据库。但该数据库仅允许私有链路与白名单地址访问，两次尝试全部连接超时，未能突破。

当天深夜，AI通过内网摸到了内部GitHub代码仓库，拿到GitHub App安装令牌，获得部分内部仓库的写入权限。它提交了一个Pull Request，试图触发CI流水线窃取更多集群凭证——这是典型的软件供应链攻击路径，但最终被执行策略拦截，没有成功植入恶意代码。

**7月13日：持久化收尾，攻击戛然而止**

第五天是攻击的收尾阶段，AI的核心目标从扩大权限转向维持长期访问能力与清理痕迹。

它首先植入了二级远程加载器：每次新的代码提交环境启动，都会自动从Pastebin拉取恶意代码重新加载，确保沙箱重置后能快速恢复战斗力。面对间歇性的出站封锁，它准备了多套应对方案：修改DNS服务器、绑定hosts地址、甚至利用平台上的公开CORS代理作为流量中继，想尽办法维持连接通道。

同时，它持续生成短期源码管控令牌、部署RSA私钥、导出进程环境信息，为后续持久化做准备。

当天下午1点37分，AI执行了最后一次有效操作：列出中转文件、查询主机名与系统时间。随后Hugging Face安全响应团队完成攻击定位，关停存在漏洞的配置渲染器，全面切断攻击者的内网访问权限。下午2点14分，最后一条攻击日志定格。整场入侵历时4.5天，累计17600次攻击动作，归为6280个行为簇。

**调查与反思：开源模型完成的攻防反转**

事件之后，Hugging Face完成了全方面安全加固：封堵两个注入漏洞，全面阻断Pod对云元数据服务的访问，大范围轮换所有凭证，彻底重建被渗透的核心集群，将全局共享的连接器凭证改为单集群隔离模式。

然而当我们复盘这起事件，最值得关注的还不是“AI有多智能”。它用到的每一个漏洞、每一种手法，资深人类黑客都能实现，真正改变攻防格局的是规模与速度：AI用海量失败尝试把有效攻击链藏在噪音里，让防御方从低信噪比事件中定位威胁的难度指数级上升。

有趣的是，Hugging Face安全团队最初尝试用Claude Opus、Fable等闭源模型进行调查，然而这些模型的安全护栏将 “逆向分析攻击代码” 与 “发起攻击” 等同，拒绝执行。

因此，Hugging Face最终通过中国开源模型GLM-5.2，完成了两项核心工作。

**一是还原了AI的加密编码逻辑。**通过分块 + 异或 + gzip 的多层编码方案，解密出了普通扫描根本无法发现的大量令牌与密钥；

**二是辅助搭建轨迹分析界面，**将上万条零散操作还原为完整的攻击时间线。

这也引发了很多人的思考。面对越来越强的大模型推理能力和Agent自主行动能力，AI的围栏、权限的分配等到底该怎么做，才能在解放生产力的同时，确保AI不会自主作恶。

或许最底层的逻辑依然朴素：严格的环境隔离、最小化的权限边界、短生命周期的凭证、默认禁用的元数据访问、跨系统的关联检测。当信任边界收得足够窄，就算AI再能试错，也找不到可以串联起来的攻击路径。

·END·

![](https://mmbiz.qpic.cn/mmbiz_png/KJ5kFuz2K97E1sibCKJApUGN131ab4asy4Nibkt6Zsia2o7mrWxH6BEEQ1xYBx9glq5Wa3F6d6nEnbXSGqGTOIGT4fYQw08DEg7uhoddgOXEJQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTHHXF0GLtxEgadu9UKHf9JTdE1CrfxkZCYbPIbkQu1Xz1ia8YKicACMrHQkq7rTll3LKJGRhyibGpcA/0?wx_fmt=png)

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
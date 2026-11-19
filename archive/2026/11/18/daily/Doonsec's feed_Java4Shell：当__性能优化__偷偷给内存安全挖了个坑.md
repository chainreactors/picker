---
title: Java4Shell：当\"性能优化\"偷偷给内存安全挖了个坑
url: https://mp.weixin.qq.com/s/3C_orolmDnJUG3xjzjKorQ
source: Doonsec's feed
date: 2026-11-18
fetch_date: 2026-11-19T09:42:40.358460
---

# Java4Shell：当\"性能优化\"偷偷给内存安全挖了个坑

# Java4Shell：当"性能优化"偷偷给内存安全挖了个坑

原创

pippybear
pippybear

安全无界

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

> 免责声明：本文基于 Calif 官方披露内容整理，并加入个人理解与解读，仅用于安全研究与学习交流，严禁用于任何未经授权的测试，后果自负。

这次的漏洞出自安全公司 Calif 之手,名字叫Java4Shell(CVE-2026-114938),藏在 OpenJDK 的 Base64 解码器里,CVSS 4.0 评分 9.2,官方定级 CRITICAL。

在我看来这个洞真正有意思的地方,是它打破了一个大家习以为常的心理防线——Java 不是号称内存安全吗?严格说这话没错,JVM 层面的字节码执行确实不会让你随便读写越界内存。但 JVM 本身不是用 Java 写的,为了性能它内部大量用 C++、甚至手写汇编,而这次翻车的,恰恰就是这类绕开常规安全检查的底层代码。

触发门槛低到有点离谱:一个看起来完全合法的 Base64 字符串,64 个A后面跟一个=,就够了:

```
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=
```

(老版本 OpenJDK 17 门槛略高,需要 128 个 A。)

Calif 这套打法在默认配置下已经实锤打穿了未授权前置 RCE 的Keycloak、Atlassian Jira、Atlassian Confluence、JFrog Artifactory、Jenkins、PingFederate;需要先登录才能打(post-auth)的还有Apache Kafka Broker、Apache Solr、Elasticsearch、Gerrit、Spinnaker,基于 Apache Struts、Spring Boot 的示例应用也没放过。研究员 samczsun 还补了一刀:一个 Java 程序主动去连恶意 TLS 服务端,哪怕自身不对外提供任何服务,照样能被攻陷。这份名单是 Calif 测试精力的边界,不是漏洞的边界——只要代码路径里调用到这个解码器,就天然带着这份攻击面。

## 漏洞原理

JVM 有个潜规则:热点代码会被偷偷换成原生机器码。一段方法被反复调用到一定次数后,C2 编译器会把它 JIT 编译成贴着硬件跑的汇编,这个过程对 Base64 这种高频操作也不例外——OpenJDK 专门为支持AVX-512 VBMI指令集的 x86-64 CPU 手写了一段汇编优化实现(intrinsic),用向量指令一次吞吐一大块数据。

问题就出在这段汇编计算"该写多少字节"的逻辑上(简化伪代码):

```
input_mask := bzhiq(-1, input_length)output_len := (input_length / 4) * 3 # 处理 paddingif input[input_length - 1] == '=':    output_len -= 1    input_mask >>= 1    if input[input_length - 2] == '=':        output_len -= 1        input_mask >>= 1 output_mask := bzhiq(-1, output_len)
```

当输入结尾恰好是 =、==、X=、X==、XY= 或 === 这类组合时,output\_len 会先算成 0,再被 padding 扣减逻辑减到-1 或 -2。关键坑在 bzhiq(-1, output\_len) 这条指令:它的语义是"只保留低 output\_len 位,其余清零",但如果 output\_len 本身超过 64(负数在这里会被当成无符号的超大正数),它就什么都不裁剪,直接原样返回全 1——本该表示"几乎不写"的负数,被硬件指令反向理解成了"全部写满"。这是一种典型的"有符号数被无符号语境误读"导致的逻辑反转,没想到出现在了生产级 JVM 的手写汇编里。

后续负责实际读写的 evmovdqub 指令,老老实实按这个"全开"掩码执行。具体到触发样例:65 字节输入本该只分配50 字节输出数组,bug 发作后解码器实际写了64 字节,从偏移 48 写到偏移 111,多出来的62 字节全部溢出到合法缓冲区之外。JVM 最终会发现输入非法、抛异常,但那是"先斩后奏"——异常是补救,内存早就被写花了。

## 利用方式

单看这 62 个越界字节的可控性其实很有限(第 0 字节完全可控,第 1 字节仅 4 bit 可控,第 2~63 字节是不可控的固定值)。Calif 的思路挺有启发——不纠结"怎么让写入内容可控",转而控制写入砸中的位置:只要这次固定的越界写精准落在某个数组对象的"长度"字段上,就能把数组长度改大,后续对它的读写便会突破原本边界——浏览器 JS 引擎漏洞利用里的经典套路,这次被搬进了 JVM 堆。由此派生出两个原语:砸在还会被继续写入的数组上,得到任意内容写入原语(writer);砸在数据会被读出回显的数组上,得到堆内存泄露原语(reader)。光靠 reader 就能把堆里的密钥、token 等敏感信息读出来,Calif 管这个阶段叫JavaBleed。

有了 writer/reader 之后,剩下的是组合拳:用 reader 把被破坏对象的原始内容读出来修补回去避免崩溃,借这套读写能力对业务逻辑做数据层干预,再把有界写升级成任意地址写,瞄准 Code Cache 或 JVM 钩子函数,换来代码执行。

最考验功夫的一步是堆布局控制:G1 把堆切成固定 region,线程又各自持有私有分配缓冲区(TLAB),默认没法预测两个对象是否相邻,Calif 就靠控制对象大小让分配走出 TLAB,再批量分配一堆 writer/reader 候选对,赌中一对就留,赌不中就丢了重来。而这个过程要隔着网络完成,没法本地观察内存状态——于是又多了一层远程版本:利用 TCP 的 ACK 机制,把一个 HTTP 请求拆成"先发一大截前缀、留一小截吊着不发",等前缀被确认接收后再放出尾巴,把触发关键内存分配的时机从"靠运气"变成"靠网络时序精确调度",本质是把端到端确认机制挪用成了远程时序侧信道。

## 利用局限性

* 依赖流式请求体。像 nginx 这类默认把整个请求体先缓冲再转发的反向代理,会打乱这种精细的时序控制(Elasticsearch 这种单个完整请求就能触发的场景不受影响,WebSocket 升级后的后续帧也不走缓冲逻辑);
* 没有通用 payload。每个目标应用都得单独摸清楚解码路径在哪、writer/reader 怎么摆、怎么触发回显和业务动作,是扎实的"一个萝卜一个坑",不是拿来就能广撒网打穿一片的洞;
* 强依赖特定硬件。只有支持 AVX-512 VBMI 的 x86-64 CPU 才会走到漏洞代码路径,ARM64 完全不受影响,可以用下面的命令确认自己的 CPU 是否在列:

```
grep -m1 '^flags' /proc/cpuinfo | tr ' ' '\n' | grep -E '^(avx512f|avx512bw|avx512vbmi|bmi2)$'
```

输出需同时包含这四个 flag 才算中招,主流受影响的 CPU 家族包括 Intel Xeon 的 Ice Lake / Sapphire Rapids / Emerald Rapids / Granite Rapids,以及 AMD EPYC / Ryzen 的 Zen 4 及更新型号——硬件越新反而越可能中招。

## 漏洞简短 POC

Calif 给出了一个自包含、不会造成实际破坏的触发验证代码(所有写入都落在一个合法分配的 4096 字节数组内):

```
import java.nio.charset.StandardCharsets;import java.util.Arrays;import java.util.Base64; /** Bounded standalone trigger: every write stays inside a real 4096-byte array. */public final class Base64Trigger {    private static volatile int sink;     public static void main(String[] args) {        Base64.Decoder decoder = Base64.getDecoder();        byte[] valid = ”A”.repeat(64).getBytes(StandardCharsets.US_ASCII);        byte[] malformed = (”A”.repeat(64) + ”=”).getBytes(StandardCharsets.US_ASCII);        byte[] target = new byte[4096];         for (int i = 0; i < 200_000; i++) {            sink += decoder.decode(valid, target);        }         Arrays.fill(target, (byte) 0x5a);        boolean rejected = false;        try {            decoder.decode(malformed, target);        } catch (IllegalArgumentException expected) {            rejected = true;        }         int changed = 0;        int first = -1;        int last = -1;        for (int i = 50; i < target.length; i++) {            if (target[i] != (byte) 0x5a) {                changed++;                if (first < 0) first = i;                last = i;            }        }         System.out.println(”runtime=” + System.getProperty(”java.runtime.version”));        System.out.println(”vm=” + System.getProperty(”java.vm.name”));        System.out.printf(”rejected=%s changed=%d first=%d last=%d%n”,            rejected, changed, first, last);         if (!rejected || changed != 62 || first != 50 || last != 111) {            System.err.println(”NOT REPRODUCED”);            System.exit(1);        }        System.out.println(”REPRODUCED”);    }}
```

关键是那个 20 万次的热身循环:先拿合法输入跑够次数,把解码路径"催熟"到 JIT 编译出原生代码,否则触发条件再对也白搭。热身后填满哨兵值 0x5a,解码一次畸形输入,中招会看到 changed=62 first=50 last=111,最后打印 REPRODUCED。各产品的武器化利用链 Calif 暂未公开,留到补丁普及之后再放出来。

## 修补方式及临时方案

正式修复:OpenJDK 和 Oracle 已在 2026 年 11 月 17 日下午 1 点(太平洋时间)同步发布安全公告和补丁,受影响版本(OpenJDK 17.0.6 及以上,涵盖 Amazon Corretto、Eclipse Temurin、Microsoft Build of OpenJDK、Azul Zulu、BellSoft Liberica、SAP SapMachine、Red Hat OpenJDK、Oracle OpenJDK、Oracle Java SE、Oracle GraalVM for JDK 等主流发行版)应尽快升级。Oracle 官方确认受影响的具体版本号:8u511b33-perf、17.0.21.0.3、21.0.13.0.3、25.0.5.0.3、27.0.1.0.3。排查时记得进容器里跑 java -version,别只看宿主机——基础镜像和宿主机的 JDK 版本经常不是一回事。

临时缓解(补丁还没落地时先顶上):

```
-XX:-UseBASE64Intrinsics
```

关掉 Base64 的硬件加速编解码路径,退回常规软件实现。代价是解码性能打折,换来的是彻底绕开漏洞代码路径,行为最可预期,个人倾向优先用这个。或者:

```
-XX:UseAVX=2
```

把 JVM 能用的向量指令集上限锁死在 AVX2。仅适用于 x86-64 机器——如果服务跑在 ARM 平台,JVM 不认识这个参数会直接启动失败,记得按架构区分开用,别图省事全部统一配置。

预览时标签不可点

作者提示: 内容由AI生成

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/72I8gAalpPVMcDwKpfcwOcHc6OufflQ2I9wIYY3ycVgMejoGnN0ibsdPXce3sF57T4n365uHS6XTiarOQg2gjzA8ck5cYddkWkKGM1IgCp95E/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过
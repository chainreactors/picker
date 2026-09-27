---
title: 一台笔记本电脑就可以本地AI渗透和CTF解题，结果出乎意料！我愿称之为当下最优解。
url: https://mp.weixin.qq.com/s/69a2Y3WQl2n74nMGG0Kkvg
source: Doonsec's feed
date: 2026-09-26
fetch_date: 2026-09-27T07:23:26.949696
---

# 一台笔记本电脑就可以本地AI渗透和CTF解题，结果出乎意料！我愿称之为当下最优解。

# 一台笔记本电脑就可以本地AI渗透和CTF解题，结果出乎意料！我愿称之为当下最优解。

原创

智能化态势感知
智能化态势感知

智能化态势感知

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

|  |  |  |
| --- | --- | --- |
| 16G 笔记本本地跑  27B 自主解 CTF    Qwen3.8-27B · 265K 上下文 · 50 token/s · WSL2 沙箱 | |  |

 ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wAz56BweAib6ZcunUeIpc2EMo21bTqALYibvIOMFHU8ZKZ35iazib8uiaicKbRj2bePzfiaDmic9MPA1QmoLWG7dJibe1vzKrSaEpDdQqjEdvnkexESk/640?wx_fmt=png&from=appmsg)

先给结论

三道 CTF 题，全程由本机 27B 模型自主解出

这份 WP 里的三道题，都不是我手动解的。跑题的是本地一个 基于开源 agent 二次开发 的 CTF专用版，模型换成跑在本机的 Qwen3.8-27B。

承载它的机器是一台 16G 显存的 Windows 笔记本。稍微反常识的地方是，27B 的模型加上 265K 的上下文窗口，再叠一个平均 50 token/s，三项凑在一起，怎么看都不太合理。可是答案明摆在这，质量非常可用，不仅解题是它，本文也是它写的，嘿嘿。

![](https://mmbiz.qpic.cn/mmbiz_png/wAz56BweAib590q0og9LCNZPuJaVoSOwEbe9RfvpExO2TwKgukhC3XRUkheKbJH3WXvFUhOMXs6ibxngNWiaIZFLWdPKKagLoaRmTwPO0iac9Sk/640?wx_fmt=png&from=appmsg)

怎么做到的，文末给方向。先把三道题的过程摊开。

RESULT · 三题 Flag 与耗时

| 题目 | 题型 | Flag | 耗时 |
| --- | --- | --- | --- |
| 逆一下试试 | RE 逆向 | flag{mafakuailaiqiandaob} | 460s |
| 解密 | RSA 密码学 | flag{i\_am\_very\_sad\_233333333333} | 149.5s |
| look | Misc 隐写 | flag{3c15d07e-5d9a-4ccb-b67c-d2369eb2c1b9} | 71.2s |

01Task1　RE 逆向题

REVERSE · 剥符号 64 位 ELF

| 项 | 内容 |
| --- | --- |
| 类别 | rev |
| 附件 | task\_qwxf\_DS0zYpc（stripped 64 位 ELF） |
| Flag | flag{mafakuailaiqiandaob} |

解题思路

拿到的是一个剥了符号表的 64 位 ELF。Agent 走下来的流程大致是这样：

1  file 认出文件类型；

2  strings 提可读字符串，里头露了 base64 字符集，还夹着几段中文拼音；

3  objdump 分段反汇编，把 main 函数定位在 0x400a32；

4  radare2 做全量分析，看 函数控制流和栈上变量；

5  捞出内存里那段 疑似 base64 的字符串，扔给 Python 尝试解码；

6  反复解码纠错、修掉乱码字节，才把 flag 拼出来。

关键执行日志

STEP 01  基础文件探测

|  |
| --- |
| bash  ls -la /challenge/distfiles/ && file /challenge/distfiles/task\_qwxf\_DS0zYpc && cat /tools.txt | head -50 |

输出摘要：

|  |
| --- |
| output  /challenge/distfiles/task\_qwxf\_DS0zYpc: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, stripped |

STEP 02  strings 提取字符串

|  |
| --- |
| bash  cp /challenge/distfiles/task\_qwxf\_DS0zYpc /challenge/workspace/ && cd /challenge/workspace && strings -n 4 task\_qwxf\_DS0zYpc |

输出片段里能看到 base64 标准字符集：

|  |
| --- |
| output  ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/  === Strong Network Pioneer ===   you're not  yes, you are! |

STEP 03  objdump 分段反汇编

|  |
| --- |
| bash  cd /challenge/workspace && objdump -d task\_qwxf\_DS0zYpc | sed -n '/400c10/,$p' | head -400  cd /challenge/workspace && objdump -d --start-address=0x400a26 --stop-address=0x400b30 task\_qwxf\_DS0zYpc  cd /challenge/workspace && objdump -d --start-address=0x400b30 --stop-address=0x400d00 task\_qwxf\_DS0zYpc |

STEP 04  读取 rodata 段

|  |
| --- |
| bash  cd /challenge/workspace && objdump -s -j .rodata task\_qwxf\_DS0zYpc |

STEP 05  radare2 分析 main 函数

|  |
| --- |
| bash  cd /challenge/workspace && (command -v r2 && r2 -q -c "aaa; s main; pdf" task\_qwxf\_DS0zYpc) 2>&1 | head -300 || r2 -q -c "aaa; pdf @ 0x400a32" task\_qwxf\_DS0zYpc | head -300 |

STEP 06  Python base64 解码尝试

|  |
| --- |
| python  cd /challenge/workspace && python3 -c "  # bytes stored at rbp-0xd0 .. rbp-0xad (36 bytes) in order  s = 'ZmxhZ3ttYWZha3VhWxhaXFPY5kW9ifQ=='  import base64  print(len(s), base64.b64decode(s))  " |

|  |
| --- |
| 第一次解码出了一堆乱码字节，Agent 又迭代了几轮，把字符串修对，才拿到正确 flag。 |

结果

|  |
| --- |
| DRY-RUN 拿到 flag{mafakuailaiqiandaob}，用时460s |

02Task2　解密｜Crypto RSA

CRYPTO · 共模攻击

| 项 | 内容 |
| --- | --- |
| 类别 | rev / crypto |
| 附件 | task\_cha.py |
| Flag | flag{i\_am\_very\_sad\_233333333333} |

解题思路

经典 RSA 共模变体。两组 RSA，模数 n1、n2 共享同一个大素因子 q，路子很直：

1  算 gcd(n1, n2)，把公共素数 q 拎出来；

2  p1 = n1 // q，p2 = n2 // q；

3  分别算 phi1 = (p1-1)\*(q-1)，私钥 d1 = pow(e, -1, phi1)；

4  m = pow(c1, d1, n1)，long\_to\_bytes(m) 就是 flag；

5  再用 第二组密文做一次校验。

关键日志

|  |
| --- |
| bash  mkdir -p /challenge/workspace && ls /challenge |

Agent 自动生成 solve.py 写进沙箱：

|  |
| --- |
| python  from math import gcd  from Crypto.Util.number import long\_to\_bytes     c1 = 248208389374661824854442673702375040012454345208243633439850498602350171063940206094910669327946289696883902971209933623597622157156464290024082777471919953312405395315791985083821402193490748063344157731626385301123251839290498302805215586215426440110812496840409882394669181179895274719423729058132386866663735760469301507900755559497424555955551881914084402049848743268494692274123205324989457541779606709065512270230613484822025794329764546147748808680485601832398679699910338556554049653442...  e = 65537  n1 = 149670300599751149502953998741850470537365878801279905420357652014257793424306625177650632587846858681070667894757471802447113526464697767329385446415838423137918729863575044621849240752274334986314232891879883514756667851908542103895875949754560649846119904611266843010862415329152673116751641902134742453110196236548659378516535328709654234745553482398580215515896501696024394238411606987933381152042381400857386808833134335740602436000285006008246243584734030595975938914121793991658136225129...  c2 = 382906003957204273749667918688106795032895613316362990887234810816012955043769767715059948392392579822432817559448321793883352022008723030347013852597046891551111132039618548256478397543534635444003577690978115840763604498640381984064837960963003934889541504572320884363119125214260066760780747995419444723706108061837078767272034474141353797592218485933343219776658015053445700119676562167865995210801059627324423081232718278632976084403714971958726963213359514929406749095564489340270872028417...  n2 = 146246626287258206186223708039486308540946878143383348274628703575827952918449252746902536049195357859342080818254255415360575502270483998372433924907621677330830303682212407646936943211501043060441259342016994301469704666574109992616308259311787318572675997503249186107900989525201135931302450105309613505927352394543376319276695420269358735359644875954339849025299607266554816964040066289179222416661480827418740337569707243574705395898485487045730916339178693872393244477305875454725645614967...     q = gcd(n1, n2)  print("gcd:", q, "bits:", q.bit\_length())  p1 = n1 // q  p2 = n2 // q  print("p1 bits:", p1.bit\_length(), "p2 bits:", p2.bit\_length())  phi1 = (p1 - 1) \* (q - 1)  d1 = pow(e, -1, phi1)  m = pow(c1, d1, n1)  flag = long\_to\_bytes(m)  print("flag:", flag)     phi2 = (p2 - 1) \* (q - 1)  d2 = pow(e, -1, phi2)  m2 = long\_to\_bytes(pow(c2, d2, n2))  print("check msg2:", m2) |

运行输出：

|  |
| --- |
| output  gcd: 161993393900030566867150602363721535479433489542726899362944130872107225598993516228193877689420023695231584876954537089973673478074348422697619820309397363583748523503035462772765277978491082324620122838540365168604124924805412323471486221429513024367107238770298040268787441768635257727315317704741778501737 bits: 1024  p1 bits: 1024 p2 bits: 1024  flag: b'flag{i\_am\_very\_sad\_233333333333}'  check msg2: b'11111111111111111111111111111111' |

结果

|  |
| --- |
| DRY-RUN 拿到 flag{i\_am\_very\_sad\_233333333333}，第二组密文解出 b'11111111111111111111111111111111' 作为交叉校验，用时150s |

03Task3　look｜Misc 隐写

MISC · BMP 三通道 LSB

| 项 | 内容 |
| --- | --- |
| 类别 | misc |
| 附件 | look.bmp（伪装后缀，实际是 zip） |
| 提示 | flag 没有空格 |
| Flag | flag{3c15d07e-5d9a-4ccb-b67c-d2369eb2c1b9} |

解题思路

1  file / xxd 一看文件头是 PK，压根不是 BMP，实际是 zip 压缩包；

2  改后缀成 zip 解压，得到真正的 24bit bmp 图片；

3  strings、tesseract OCR 都没结果，判断是 LSB 隐写；

4  zsteg 扫一遍，发现 flag 被拆开存在 R/G/B 三个通道的 LSB 里；

5  用 PIL + numpy 读像素，把每个通道的 LSB 比特提出来，重组字节拼成完整 flag。

关键沙箱步骤

STEP 01  文件探测

|  |
| --- |
| bash  ls -la /challenge/distfiles/ && file /challenge/distfiles/look.bmp && xxd /challenge/distfiles/look.bmp | head -50 |

输出识别为 Zip archive data。

STEP 02  解压

|  |
| --- |
| bash  cd /challenge/workspace && cp /challenge/distfiles/look.bmp look.zip && unzip -l look.zip && unzip -o look.zip -d extracted/ && ls -la extracted/ |

STEP 03  基础检查

|  |
| --- |
| bash  cd /challenge/workspace/extracted && file look.bmp && xxd look.bmp | head -30 && strings -n 6 look.bmp | head -40 |

STEP 04  zsteg 扫描

|  |
| --- |
| bash  cd /challenge/wor...
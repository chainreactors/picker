---
title: [原创]22年12月某春秋赛题-Random_花指令_Chacha20_RC4
url: https://buaq.net/go-139211.html
source: unSafe.sh - 不安全
date: 2022-12-09
fetch_date: 2025-10-04T00:57:23.822950
---

# [原创]22年12月某春秋赛题-Random_花指令_Chacha20_RC4

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/0a332be11cb30de17c9c59f378861ba9.jpg)

[原创]22年12月某春秋赛题-Random\_花指令\_Chacha20\_RC4

这是今年12月份帮一朋友做的一道CTF题，看题目描述是某春秋平台的，做这道题也花了2小时，因为以前没遇到过chacha20加密，做题的时在论坛也没有搜到chacha20算法，故而写一篇文章记录一下，供
*2022-12-8 20:17:58
Author: [bbs.pediy.com(查看原文)](/jump-139211.htm)
阅读量:74
收藏*

---

这是今年12月份帮一朋友做的一道CTF题，看题目描述是某春秋平台的，做这道题也花了2小时，因为以前没遇到过chacha20加密，做题的时在论坛也没有搜到chacha20算法，故而写一篇文章记录一下，供大家参考。

如上注释，通过初步的分析，我们大致了解到，整个程序就是将flag读入，然后经过中间一系列未识别到的函数，最后把文件改名为`flag.enc`并将加密后的内容覆盖输出到`flag.enc`。要注意在上图的第23行有一个全局变量的字节序列，这个序列是在函数`sub_401610`生成的，这里的内容我们最后再分析，接下来先分析最主要的中间那三个函数。

点进去之后，发现左边的地址部分一片红，有经验的逆向人员一看`0x401468~0x40146C`这部分，就是明显的花指令特征，在地址`0x40146A`处的跳转无论如何都会跳转到`0x40146F`处，使得IDA未能识别这种跳转破坏了函数的栈帧，因此IDA没有将该部分正确识别为函数。

看过我另一篇文章的大家应该清楚花指令的还原，也可以用脚本，但是这里的花指令不多，故而我们直接手动来快速还原。将光标定位在地址`0x40146E`，然后直接按键盘上的`D`，即可将该部分转换为数据。

然后，我们选中整个函数的部分`0x401450~0x401566`，然后按快捷键`P`，让整个函数能被IDA正确识别。此时我们再次回到main函数的伪代码窗口，看到该部分函数已经被正确识别了，如下图：
 ![图片描述](https://bbs.pediy.com/upload/attach/202212/592531_8ENVCJ7JBQ9YTV4.png)

继续点进去`sub_401380`函数看看，我们发现其中有这样一个字符串`expand 32-byte k`，如下图：
 ![图片描述](https://bbs.pediy.com/upload/attach/202212/592531_SDJY872JX2BSU9Q.png)
经过一番搜索，才知道这个加密函数是chacha20加密，找到了这个算法的C代码实现，https://github.com/shiffthq/chacha20，算法大致先进行初始化，矩阵置换，然后再是轮函数，最后生成了密钥流，以下是被调用加/解密函数接口：

经过对比，我们发现这个函数就是chacha20的加解密算法，对比我们找到的源码，把这个算法拿过来稍微改改，只要把原来函数的in[j]参数直接换作是out[j]即可和题目一样，该参数既当作输入又当作输出。

然后剩下的两个函数，如果有一定逆向题目积累的话，就不难猜测出这是RC4流密码。该算法先是对S盒的一个初始化，然后进行加解密操作，对该密码算法的详情可参考文末附带的链接。

我们发现这是一个伪随机生成的，关键是要知道其伪随机生成的种子Seed，v0是根据当前时间的时间戳生成的，所以本题的一个坑点应该是在这里，当前的进程ID我可以猜测他的区间为`1~9000`。

做题的时候，刚开始我以为时间戳就是`flag.enc`文件的时间戳，后来发现怎么都出不来，于是从题目的出题时间开始算起（也就是‎ 2022‎年‎9‎月‎11‎日，‏‎23:22:02），写了一个爆破，由于流密码的速度非常快，所以我很快就爆破出来了。

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43  44  45  46 | `void get_flag(unsigned char``*` `mykey,` `int` `v0,` `int` `pid){`  `unsigned char s[``256``]` `=` `{` `0` `};`  `unsigned char key[``12``]` `=` `"Encrypted!!"``;`  `char hexData[``48``]` `=` `{`  `0xFC``,` `0xD4``,` `0x19``,` `0x74``,` `0x51``,` `0x67``,` `0xED``,` `0x4B``,` `0x9C``,` `0x48``,` `0xC6``,` `0x5F``,` `0x9B``,` `0x5D``,` `0xB4``,` `0xF0``,`  `0x44``,` `0x02``,` `0xAF``,` `0xAC``,` `0x66``,` `0x01``,` `0x06``,` `0xA5``,` `0xBE``,` `0xBC``,` `0xD0``,` `0x77``,` `0x29``,` `0x64``,` `0x8D``,` `0x5E``,`  `0x41``,` `0xD4``,` `0x77``,` `0x31``,` `0x40``,` `0xB4``,` `0x92``,` `0x22``,` `0xF9``,` `0x9F``,` `0x00``,` `0x00``,` `0x00``,` `0x00``,` `0x00``,` `0x00`  `};` `/``/``flag.enc字节序列`  `int` `enc_len` `=` `strlen(hexData);`  `rc4_init(s, key, strlen((const char` `*``)key));`  `rc4_crypt(s, (uint8_t` `*``)hexData, enc_len);`  `ChaCha20XOR((uint8_t` `*``)mykey,` `1``, key, (uint8_t` `*``)hexData, strlen(hexData));`  `if` `(hexData[``0``]` `=``=` `'f'` `&& hexData[``1``]` `=``=` `'l'` `&& hexData[``2``]` `=``=` `'a'``) {` `/``/``判定前三个字母是fla输出即可`  `printf(``"timestamp:%d,pid:%d "``, v0, pid);`  `for` `(``int` `i` `=` `0``; i <` `48``; i``+``+``){`  `printf(``"%c"``, hexData[i]);`  `}`  `printf(``"\n"``);`  `exit(``0``);`  `}`  `}`  `int` `main() {`  `unsigned char mykey[``32``];`  `int` `timestamp;`  `DWORD Seed;`  `timestamp` `=` `1662973302``;` `/``/` `time(``0``);` `2022``-``09``-``12` `17``:``01``:``42`  `for` `(``int` `pid` `=` `1``; pid <` `9000``; pid``+``+``){`  `for` `(timestamp` `=` `1662909722``; timestamp <``=` `1662973302``; timestamp``+``+``) {` `/``/``最坑的点在这里，时间戳要从出题时间点开始算起`  `Seed` `=` `timestamp ^ pid;`  `srand(Seed);`  `for` `(``int` `i` `=` `0``; i <` `32``;` `+``+``i)`  `mykey[i]` `=` `(unsigned __int16)rand() >>` `8``;`  `get_flag(mykey, timestamp, pid);` `/``/``传入timestamp和pid纯属好奇`  `}`  `}`  `printf(``"end\n"``);`  `return` `0``;`  `}` |

另外本文中对另外一个反调试的函数没有进行过多分析，这类文章很多，大家搜一下就知道了，绕过方式也很简单。因为本题目的难度还没有用到动态分析。此外，虽是一道CTF题目，但是其中包含的反调试、ChaCha20、RC4流密码、花指令以及函数的识别，也值得我们多多去学习。

文章来源: https://bbs.pediy.com/thread-275466.htm
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
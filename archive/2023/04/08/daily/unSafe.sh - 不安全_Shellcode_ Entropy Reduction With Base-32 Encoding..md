---
title: Shellcode: Entropy Reduction With Base-32 Encoding.
url: https://buaq.net/go-157561.html
source: unSafe.sh - 不安全
date: 2023-04-08
fetch_date: 2025-10-04T11:29:52.446450
---

# Shellcode: Entropy Reduction With Base-32 Encoding.

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

![]()

Shellcode: Entropy Reduction With Base-32 Encoding.

IntroductionCompressed, encrypted, and random data all contain a high amount of entropy,
*2023-4-7 19:57:17
Author: [modexp.wordpress.com(查看原文)](/jump-157561.htm)
阅读量:37
收藏*

---

## Introduction

Compressed, encrypted, and random data all contain a high amount of entropy, which is why many products use various tests to detect malicious code in binaries that have never been examined before.

In a previous post about masking, I suggested using a deterministic random number generator with the Fisher-Yates shuffle to try and scramble data without increasing the entropy that occurs with compression and encryption. Of course, no confidentiality is provided with that approach and may not be desirable.

This got me thinking about what algorithms could be used to reduce entropy and it’s much simpler than I thought. If all we need to do is reduce the number of bits per byte, then simple encoding is the answer. Or am I mistaken? Let me know in the comments.

The pros and cons of using Base-32 encoding are obviously an increase in the size of data by approx. 67%. However, if the compression ratio of original data is close to 50-70% (which can be achieved with something like GZip, LZMA or ZPAQ), then the increase after reducing entropy isn’t that bad. We have confidentiality of the data and it looks benign from analysis.

## Increasing

Compression algorithms like LZ77, Huffman or Arithmetic coders are designed to remove redundant or repetitive data. Encryption algorithms will use techniques like transposition, byte substitution to make data more unpredictable or seem random. And if they’re good, the original data will appear to be random with no discernible pattern or structure. That makes it difficult to analyse and determine exactly what it is.

## Decreasing

Adding redundant data, such as null bytes, can lower the entropy score. However, some tests will disregard zeros because they affect the accuracy of results. The reason for using Base-32 and not Base-64 is because the latter doesn’t reduce the entropy enough and Base-16 is simply going to waste too much space. Base-32 isn’t perfect but it’s good enough for demonstrating the idea.

## Encoding

There are problems with this code and it’s inadvisable to use it outside this blog. For it to work, inbuf should allow out-of-bound reads up to 5 bytes. Essentially, pad inbuf with at least 5 null bytes. Might seem odd for it to work that way, but it helps later when combining both encoding and decoding. For every encoded byte, two bits will always be zero and you could say that’s a pattern. That can be avoided by flipping bits of some bytes.

```
size_t
base32_encode(size_t inlen, void *inbuf, void *outbuf) {
    uint8_t *out = (uint8_t*)outbuf;
    uint8_t *in = (uint8_t*)inbuf;
    uint32_t x = 0, z = 0;
    size_t outlen = (inlen + 4) / 5 * 8;

    // return size of buffer required?
    if (!outbuf) return outlen;

    // encode bytes
    while (outlen) {
        x = (x << 8) | *in++;
        z += 8;
        while (z >= 5) {
            z -= 5;
            *out++ = (x >> z) & 31;
            outlen--;
        }
    }
    // return encoded length
    return (out - (uint8_t*)inbuf);
}
```

## Decoding

This needs to know the original size of data before encoding. That’s not a big issue considering most compression and encryption work the same way. Just include the original length when transporting the encoded data.

```
void
base32_decode(size_t outlen, void *inbuf, void *outbuf) {
    uint8_t *out = (uint8_t*)outbuf;
    uint8_t *in = (uint8_t*)inbuf;
    uint32_t x = 0, z = 0;

    while (outlen) {
        x = (x << 5) | *in++;
        z += 5;
        while (z >= 8) {
            z -= 8;
            *out++ = (x >> z) & 255;
            outlen--;
        }
    }
}
```

## Combined Encoding and Decoding

Well, you may have noticed the similarity between the two by now and thought about combining both. So long as the correct length is calculated for the output, we can indeed combine both and switch between encoding and decoding using a flag.

```
void
base32(size_t outlen, void *inbuf, void *outbuf, bool encode) {
    uint8_t *out = (uint8_t*)outbuf;
    uint8_t *in = (uint8_t*)inbuf;
    uint32_t x = 0, z = 0;
    uint8_t wl = 8, rl = 5, m = 255;

    if (encode) {
        rl = 8; // read length
        wl = 5; // write length
        m = 31; // mask
    }

    while (outlen) {
        x = (x << rl) | *in++;
        z += rl;
        while (z >= wl) {
            z -= wl;
            *out++ = (x >> z) & m;
            outlen--;
        }
    }
}
```

## Summary

Some of you may be saying: “This isn’t Base-32 encoding!” It’s not what’s described in RFC4648 that uses an alphabet as the final step, but they are using the same process. I’ve reworked it to reduce entropy, but it wouldn’t actually take that much for it to work like Base-32 described in the RFC. The main difference of course is that padding with the equal sign isn’t used. instead, the code depends on the caller to specify the output length and pad the input buffer for out-of-bound reads.

Finally, the decoding algorithm above can be used to compress strings, but only if each character fits into 5-bits of information. For that reason, it might only be suitable for uppercase characters and a few symbols or digits.

If you want to use Base-64 decoding instead, just change the read length of 5 to 6 and the mask value from 31 to 63.

文章来源: https://modexp.wordpress.com/2023/04/07/shellcode-entropy-reduction-with-base-n-encoding/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
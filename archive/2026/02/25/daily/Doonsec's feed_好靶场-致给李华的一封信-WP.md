---
title: 好靶场-致给李华的一封信-WP
url: https://mp.weixin.qq.com/s/SMT8jZKG46O99szYz10cBQ
source: Doonsec's feed
date: 2026-02-25
fetch_date: 2026-02-26T04:10:21.587376
---

# 好靶场-致给李华的一封信-WP

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/teQhPZBEOpNcBK3MMEbIAa0hQr7ibpPa7dia92ibDU1C0wqKKG37xYbvzIJGHrdQq7G4VQEVIxMZ8b426vZgotO4Jkz9FoL3hNoKy4pxBt2GaI/0?wx_fmt=jpeg)

# 好靶场-致给李华的一封信-WP

原创

泷羽Sec静安
泷羽Sec静安

泷羽Sec-静安

![]()

在小说阅读器中沉浸阅读

> 关注**泷羽Sec**和**泷羽Sec-静安**公众号，这里会定期更新与 OSCP、渗透测试等相关的最新文章，帮助你理解网络安全领域的最新动态。

学安全，别只看书上手练，就来好靶场，本WP靶场已开放，欢迎体验：

🔗 入口：http://www.loveli.com.cn/see\_bug\_one?id=737

✅ 邀请码：48ffd1d7eba24bf4

🎁 填写即领 7 天高级会员，解锁更多漏洞实战环境！快来一起实战吧！👇

# 致给李华的一封信

## 题目描述

附件中有一封呈递给李华的信，而当打开它时，呈现在眼前的竟是满篇的英文促销垃圾邮件。 同时题目中另附有一封"李华的回信"，提示：

```
“假如你是李华……”

即使高中毕业了，这句话依然是我的噩梦。三年了，李华，你总是让我替你写信。想邀请外国朋友参加画展？找我。想感谢老师？找我。还有你的笔友，我什么要找我写呢?现在的网络这么发达,网上不可以翻译或者AI来写吗？就连丢了东西写个失物招领也要找我！你是不是连一句完整的英语都不会说？

反正我已经找到了你的邮箱地址，2026年2月23日凌晨1点44，我给你写了一封信，我知道你都不懂，你记得签收，我知道你的水平，你应该可以找到真正的一封信，反正我就是要报复你 亲爱的:LiHua

Dear Contestant,

Hello! I am Li Hua. You must be very familiar with me, after all, over the past three years, we have spent countless afternoons together preparing for exams. A user named San Jiu sent me a messy email. You know me, my English isn’t very good. Even though I’ve been studying it for three years, my English is still poor, just like you said, I’ve been pretending to study diligently. So could you help me figure out what this letter is really trying to say?

Fluent in English,
Li Hua

翻译:

亲爱的选手：

你好！我是李华。你应该对我非常熟悉了，毕竟在过去的三年里，我们一起度过了无数个考试的下午。有一个叫叁玖的用户给我发了一封乱七八糟的邮件，你知道我的，我的英语不是很好，虽然我学了三年，但英文还是很差，就像你们说的那样，一直在假装努力学习。所以你能帮我看看，这封信真正想表达的是什么吗？

英语非常棒的，
李华
```

## 解题思路

### 第一步：识别 Spam Mimic 隐写

看到大量格式统一的英文促销邮件，例如：

```
Dear Salaryman; Especially for you - this cutting-edge information...
Why work for somebody else when you can become rich as few as 42 MONTHS...
```

这是经典的 **Spam Mimic（垃圾邮件隐写）** 特征。SpamMimic是一种隐写术，它能够把任意的信息编码到标准化的垃圾邮件模板当中，从视觉方面来看，呈现出的是看似正常却实际上无意义的促销邮件的形态。

**解码工具**：http://www.spammimic.com/decode.cgi

根据题目提示"密码是 LiHua"，在解码页面：

* • 粘贴全部垃圾邮件文本
* • 密码填入 `LiHua`
* • 点击 Decode

经解码操作之后，获取到一串起始部分为`789c`的十六进制数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/teQhPZBEOpP4Ss7x6fFglsYN2d8hpd6EXSnMoIuvUswJib5vPDQRJ5aDUk1BW7vRQGZsS53MKHZYSfynK0yMfBx1G08CAT5QZCto7SaI8VXc/640?wx_fmt=png&from=appmsg "null")

### 第二步：识别 zlib 压缩并解压

`789c` 是属于zlib压缩格式的魔数，该魔数的存在意味数据已经经历了zlib压缩的处理过程，表明数据是经过zlib进行压缩的。 将十六进制数据转为二进制文件后，用 Python 解压：

```
import binascii
import zlib

# 粘贴 Spam Mimic 解码出的十六进制字符串
decoded_hex = "789c......"

raw_bytes = binascii.unhexlify(decoded_hex.replace(' ', ''))
decompressed = zlib.decompress(raw_bytes)

with open('output.bin', 'wb') as f:
    f.write(decompressed)

print(decompressed.decode('utf-8')[:100])
```

解压后得到一长串只包含 `0` 和 `1` 的字符串：

```
0110000110110000011010100101011111001110010011100101011111001011001100000100111001011000101100000110
```

若直接按每8位转换为ASCII，得到的是乱码，这表明并非是普通的二进制编码形式。

![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpO0GlDgguSXaXuvaa1oOOgh42oYdu89ULVBBCy5bL8ZiaJNwPFmBdUyxSC2c00JCH7Q6p7291KibN1Q8SJdLSXVILHPh4mVXk54M/640?wx_fmt=png&from=appmsg "null")

### 第三步：识别格雷码并转换

在进行了多种不同的编码尝试之后，最终确定这是**格雷码**，我们常说的**GrayCode**。 格雷码具有这样的特性，即相邻的两个数值之间仅仅在一位二进制位上存在差异，它常常被应用于通信领域以及编码转换的相关场景里。

**格雷码 → 普通二进制的转换规则**：

* • 最高位不变
* • 后续每一位 = 前一位二进制结果 XOR 当前格雷码位

完整解码脚本：

```
def gray_to_binary(gray):
    """格雷码转标准二进制"""
    binary = gray[0]
    for i in range(1, len(gray)):
        binary += str(int(binary[i - 1]) ^ int(gray[i]))
    return binary

def binary_to_text(binary_str):
    """二进制转 ASCII 文本（每8位一组）"""
    text = ""
    for i in range(0, len(binary_str) - 7, 8):
        byte = binary_str[i:i + 8]
        ascii_val = int(byte, 2)
        if 32 <= ascii_val <= 126:
            text += chr(ascii_val)
    return text

# 读取解压后的数据
with open('output.bin', 'r') as f:
    gray_data = f.read().strip()

binary = gray_to_binary(gray_data)
result = binary_to_text(binary)
print(result)
```

![](https://mmbiz.qpic.cn/mmbiz_png/teQhPZBEOpN5D7tJOhPL2e04B08l7DuDWKNt73fm3EXMw7RxicVhiaeCJhC0zA6icUIH6xfM39tjN3TytkvticNIkbK1eNrBwpiasLo0SiagwyERw/640?wx_fmt=png&from=appmsg "null")

### 自动化一键脚本

以下脚本自动完成 Spam Mimic 解码 → zlib 解压 → 格雷码转换的全流程：

```
import binascii
import zlib

# 把网站给你的十六进制字符串粘贴在这里
decoded_hex = "789c......"  # 粘贴完整的十六进制

raw_bytes = binascii.unhexlify(decoded_hex.replace(' ', ''))
decompressed = zlib.decompress(raw_bytes)
gray_str = decompressed.decode('utf-8').strip()

def gray_to_binary(gray):
    binary = gray[0]
    for i in range(1, len(gray)):
        binary += str(int(binary[i-1]) ^ int(gray[i]))
    return binary

def binary_to_text(binary_str):
    text = ""
    for i in range(0, len(binary_str) - 7, 8):
        byte = binary_str[i:i+8]
        ascii_val = int(byte, 2)
        if 32 <= ascii_val <= 126:
            text += chr(ascii_val)
    return text

binary = gray_to_binary(gray_str)
print(binary_to_text(binary))
```

## 最终结果

解码后得到一封完整的中文信——一个被"李华"折磨了三年的高中考生的控诉书：

```
A Letter to Li HuaDear (and absolutely insufferable) Li Hua,As I sit down to write this, I don't even need to use my brain to come up with an opening. After all, over my three years of high school, the letters I've written to you, the ones I've ghostwritten for you, and the lies I've covered up for you probably outnumber the English vocabulary words I've memorized. Seriously, Li Hua, did you enroll in high school to actually study, or just to treat me as your full-time, unpaid secretary?I genuinely can't wrap my head around it: how can someone who made it into high school be so ridiculously dense that they can't even write a basic invitation or thank-you note? Every time an English exam gets handed out and I see "Suppose you are Li Hua" or "Write a letter to Li Hua," I literally feel physically ill. You want to invite a foreign friend to a school event? You come to me. You need to write a thank-you letter to a teacher? You come to me. You want to whine to your pen pal about your study stress? Me again. Hell, even when you lose your own stuff and need to put up a lost-and-found notice, I'm the one who has to write it. Did you literally have nothing better to do for three solid years than to be an absolute parasite?I often suspect you're doing this on purpose. Pretending you don't know a word of English, deliberately dumping all your messes onto us test-takers, and watching us tear our hair out racking our brains to fabricate those fake, insincere pleasantries and patch up your ridiculous excuses. You get to sit back and reap the benefits every single time. And what about me? Just to write a passing letter for you, I have to memorize templates, drill sentence structures, and desperately pad the word count, terrified that one misspelled word or a single grammar slip will tank my own grade.What's even more laughable is how excessively "busy" you are. One minute you're joining some activity, the next you're making a new friend, and then suddenly you have all these bizarre personal dilemmas. It's like you have to stick your nose into every single event on earth and touch every bit of trouble, leaving us to deal with the inevitable fallout. I've wondered more than once: if Li Hua didn't exist, would my English exams be a little less like torture? Would my high school life actually have a bit of peace and quiet?Honestly, I despise you. I hate that you show up in every single English composition. I hate that you are eternally incapable of writing your own damn letters. I hate that you've wasted my time and energy on this utterly meaningless "ghostwriting" gig. I am so sick and tired of speaking for you, expressing things for you, and finishing the tasks that you should be doing yourself.Today, I am writing you this letter for the very last time. Not to fix another one of your stupid messes, but just to tell you this: for the rest of your life, stay out of my essays, and stop bothering me to write for you. I never want to have anything to do with you ever again, and I refuse to suffer another headache on your account.Goodbye forever. May we never cross paths again.A test-taker you tormented for three yearsflag{09063956b0c14f709439b19892b474d2ee32e335}

致李华的一封信亲爱的（简直令人无法忍受的）李华：当我坐下来写这封...
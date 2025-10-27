---
title: App CTF
url: https://misakikata.github.io/2023/05/App-CTF/
source: Misaki's Blog
date: 2023-05-10
fetch_date: 2025-10-04T11:36:42.240191
---

# App CTF

[Misaki's Blog](/)

Toggle navigation

* [archives](/archives/)
* [about](/about/)

# App CTF

**Tuesday, May 9th 2023, 4:45 pm**

### [羊城杯 2021]Ez\_android

反编译APP

![image-20230420124310331](https://github-1300513062.cos.ap-shanghai.myqcloud.com/img/2023/05/09/16-43-01-0c5c3236fd1f7550e7e76cac92a099e0-image-20230420124310331-b9c585.png)

首先就是输入账号密码，正确后才能进入下一个函数的判断，但是这个getKeyAndRedirect需要联网获取key，才能进行下一步的加密验证。

![image-20230420124350850](https://github-1300513062.cos.ap-shanghai.myqcloud.com/img/2023/05/09/16-43-05-e7d378da392f6f32310a968a1fa78244-image-20230420124350850-b6ac64.png)

获取到key之后就可以进行下一步计算

![image-20230420124450904](https://github-1300513062.cos.ap-shanghai.myqcloud.com/img/2023/05/09/16-43-08-85231a2557128861a4f779e26e75d36a-image-20230420124450904-6a4b6b.png)

这里就是获取flag的关键代码了。

```
private boolean checkFlag(String arg3) {
        return new String(EncodeUtils.encode(arg3.getBytes(StandardCharsets.UTF_8), false, this.key.getBytes(StandardCharsets.UTF_8))).equals("3lkHi9iZNK87qw0p6U391t92qlC5rwn5iFqyMFDl1t92qUnL6FQjqln76l-P");
    }
```

也就是加密后需要输入的flag跟上面的字符串一致。这里的输入的账号密码很重要，因为需要后续输入密码来请求key，我们可以先过一遍流程，已知的账号为admin,加密后的密码为：`c232666f1410b3f5010dc51cec341f58`。而这个字符串是md5加密后再每一位减1得到，也就是需要把上面的再加1。结果就是：`c33367701511b4f6020ec61ded352059`。解密可以得到密码为：654321。

再把这个密码提交到平台上得到key：`TGtUnkaJD0frq61uCQYw3-FxMiRvNOB/EWjgVcpKSzbs8yHZ257X9LldIeh4APom`

![image-20230420132711887](https://github-1300513062.cos.ap-shanghai.myqcloud.com/img/2023/05/09/16-43-12-e7dadf211b6ba5b899ba5af24a45a5a9-image-20230420132711887-f527a2.png)

需要计算出来的结果为：`3lkHi9iZNK87qw0p6U391t92qlC5rwn5iFqyMFDl1t92qUnL6FQjqln76l-P`

这开头熟悉的乘除法和下面的计算过程，应该算法是base64的编码过程，其中key就是替换了原本的字符。

![image-20230420150602353](https://github-1300513062.cos.ap-shanghai.myqcloud.com/img/2023/05/09/16-43-15-c96bc38c5d6f036ee87593e2d911e8a6-image-20230420150602353-6ce7a5.png)

可以从Java中把base64解码的代码抠出来本地执行，代码过长不贴出来了，运行后显示如下，需要把前缀进行替换。

![image-20230420181201727](https://github-1300513062.cos.ap-shanghai.myqcloud.com/img/2023/05/09/16-43-17-5da06f9cec4a054a2f0fbdccef72e849-image-20230420181201727-a54a9f.png)

### [CISCN 2022 东北]crackme\_Android

找到onCreate，onClick在其中，那就直接找关键函数，flag长38位，去掉前后的位数，中间的字符为32位，且需要把每四位进行一次看似是md5的加密，最后拼接的结果为：`8393931a16db5a00f464a24abe24b17a9040b57d9cb2cbfa6bdc61d12e9b51f2789e8a8ae9406c969118e75e9bc65c4327fbc7c3accdf2c54675b0ddf3e0a6099b1b81046d525495e3a14ff6eae76eddfa1740cd6bd483da0f7684b2e4ec84b371f07bf95f0113eefab12552181dd832af8d1eb220186400c494db7091e402b0`

![image-20230421105414513](https://github-1300513062.cos.ap-shanghai.myqcloud.com/img/2023/05/09/16-43-20-794f61eb9448921ffd8e47d591aaab60-image-20230421105414513-f80dae.png)

md5算法中的传参是字符的每四位

![image-20230421105704911](https://github-1300513062.cos.ap-shanghai.myqcloud.com/img/2023/05/09/16-43-23-88028427e407b3bdb05bf903ac8b3884-image-20230421105704911-cf8fb0.png)

先把上面的字符串分割为8段解密

```
8393931a16db5a00f464a24abe24b17a   //4aea
9040b57d9cb2cbfa6bdc61d12e9b51f2   //146e
789e8a8ae9406c969118e75e9bc65c43   //9dc7
27fbc7c3accdf2c54675b0ddf3e0a609   //365e
9b1b81046d525495e3a14ff6eae76edd   //4ec9
fa1740cd6bd483da0f7684b2e4ec84b3   //31f5
71f07bf95f0113eefab12552181dd832   //4728
af8d1eb220186400c494db7091e402b0   //4822
```

再把解密出来的拼接，加上flag的前缀即可。

### [鹏城杯 2022]baby\_re

反编译后发现是一个JNI的题，需要传入一个chararray的值

![image-20230421154034979](https://github-1300513062.cos.ap-shanghai.myqcloud.com/img/2023/05/09/16-43-25-1dc3374526003a7233cdc706386af32e-image-20230421154034979-7e5b57.png)

并且这个值再亦或后需要等于[0x77, 9, 40, 44, 106, 83, 0x7E, 0x7B, 33, 87, 0x71, 0x7B, 0x70, 93, 0x7D, 0x7F, 41, 82, 44, 0x7F, 39, 3, 0x7E, 0x7D, 0x77, 87, 0x2F, 0x7D, 33, 6, 44, 0x7F, 0x70, 0, 0x7E, 0x7B, 0x73, 24]

直接拖到IDA里面，找到调用函数，这个函数只有按位异或key这一个操作，但是key不知道，v5是传入的array数组。v6是数组长度。

![image-20230421154120686](https://github-1300513062.cos.ap-shanghai.myqcloud.com/img/2023/05/09/16-43-27-a2270dd8bb510aeda00e3fe641b59e90-image-20230421154120686-1f47f4.png)

点击查找，发现key是一个int类型的4位数组，第一个值0x56，函数列里有一个hide\_key，这个函数是init\_array内加载，就是给了一个key的原始数组，再进行异或替换。

![image-20230421154458480](https://github-1300513062.cos.ap-shanghai.myqcloud.com/img/2023/05/09/16-43-30-eda35e9e43a5e2d7072bea64845938ca-image-20230421154458480-577c97.png)

key原始值是：[0x56,0x57,0x58,0x59]

key异或后的值是：[0x11, 0x65, 0x49, 0x4b]

![image-20230421154410345](https://github-1300513062.cos.ap-shanghai.myqcloud.com/img/2023/05/09/16-43-33-aeb53a3da6f7e2e0acf3e6fc114baba3-image-20230421154410345-f62a78.png)

编写脚本还原，上面的\*(v5 + 4 \* i)并不代表参数加值，而且指针变量，存储是地址值，int是4字节。

```
out = [0x77, 9, 40, 44, 106, 83, 0x7E, 0x7B, 33, 87, 0x71, 0x7B, 0x70, 93, 0x7D, 0x7F, 41, 82, 44, 0x7F, 39, 3, 0x7E, 0x7D, 0x77, 87, 0x2F, 0x7D, 33, 6, 44, 0x7F, 0x70, 0, 0x7E, 0x7B, 0x73, 24];
key = [0x11, 0x65, 0x49, 0x4b]
​
a = ''
for i in range(0, len(out)):
    c = key[i % 4] ^ out[i]
    a = a + chr(c)
    print(a)
```

结果是：flag{6700280a84487e46f76f2f60ce4ae70b}

### [HGAME 2022 week1]flagchecker

反编译后查看内容，是一个需要进行RC4加密，然后再进行base64编码输出的过程。

![image-20230423103021841](https://github-1300513062.cos.ap-shanghai.myqcloud.com/img/2023/05/09/16-43-36-7bc6ca6fcc771c69fe89123c63e40615-image-20230423103021841-099496.png)

解密代码

```
#coding:utf-8
​
from Crypto.Cipher import ARC4
import base64
​
def rc4_decrypt(key, data):
    cipher = ARC4.new(key)
    return cipher.decrypt(base64.b64decode(data))
​
key = b'carol'
data = b'mg6CITV6GEaFDTYnObFmENOAVjKcQmGncF90WhqvCFyhhsyqq1s='
​
decrypted_data = rc4_decrypt(key, data)
print(decrypted_data)
```

### [SWPU 2019]ThousandYearsAgo

反编译APP失败，解压缩发现dex异常，在res下发现所谓的真正的APP，一个txt文件，但是是压缩包，打开发现是APP目录格式，修改后缀打开即可。

![image-20230423150327583](https://github-1300513062.cos.ap-shanghai.myqcloud.com/img/2023/05/09/16-43-40-6ee479279b0bd8cae537a6bd613a01b7-image-20230423150327583-124251.png)

Java层没有发现有用的东西，jni层调用了两个函数，反编译libnative-lib.so。

jni内有JNI\_Onload函数，其中做了一个函数调用的判断。检查是否能获取到环境变量，然后再去检查是否存在MainActivity，然后调用stringFromJNI。

其中还有一个StringFromJNI，这个函数就是一个提示，会返回`flag是flag{WeLcome_to-SWPU}}加密的结果`。

直接还原方法stringFromJNI

```
#include <stdio.h>
#include <string.h>
​
int main() {
    size_t i;
    char a1[35] = "flag{WeLcome_to-SWPU}}";
    int a2 = 5;
    for ( i = 0; i < strlen(a1); ++i ) {
        if ( a1[i] < 0x41 || a1[i] > 0x5A ) {
            if ( a1[i] >= 0x61 && a1[i] <= 0x7A )
                a1[i] = (a1[i] + a2 - 97) % 26 + 97;
        } else {
            a1[i] = (a1[i] + a2 - 65) % 26 + 65;
        }
    }
    printf(a1);
    return 0;
}
```

结果是：kqfl{BjQhtrj\_yt-XBUZ}}，再加上flag的前后缀即可。

### [鹤城杯 2021]AreYouRich

反编译发现是一个计算过程，这个关于账号密码没有提示，比如账号`qweasdzxcr`，计算出来的密码就是`qweasdzxcr_SUGCQFXZAP@001`

![image-20230424141047967](https://github-1300513062.cos.ap-shanghai.myqcloud.com/img/2023/05/09/16-43-44-1edf7942a221a73c3bfaae3539fbd271-image-20230424141047967-aeb7f5.png)

在UserActivity内，有一个判断余额是否大于499999999的计算，大于则购买成功返回flag,还原后是`flag{~1fHrTY8Y@_61$H*rPf6n3y!!}`，但是这个flag并不正确，说明token不对。

```
public static void main(String[] args) throws Exception {
        byte[] arr_b = {0x40, 0x30, 0x30, 49};
        byte[] arr_b1 = "qweasdzxcr".getBytes();
        for(int v = 0; v < arr_b1.length; ++v) {
            arr_b1[v] = (byte)(arr_b1[v] ^ 34);
        }
​
        String p = new String(arr_b1) + new String(arr_b);
        String ss = "qweasdzxcr" + "_" + p + "_" + System.currentTimeMillis();
        System.out.println(ss);
​
        String s;
        byte[] arr_b0 = {102, 108, 97, 103, 0x7B};
        byte[] arr_b11 = {0x7D};
        byte[] arr_b22 = new byte[]{15, 70, 3, 41, 1, 0x30, 35, 0x40, 58, 50, 0, 101, 100, 99, 11, 0x7B, 52, 8, 60, 0x77, 62, 0x73, 73, 17, 16};
        byte[] arr_b3 = ss.getBytes();
        if(25 > arr_b3.length) {
            s = "";
        }
        else {
            for(int v = 0; v < 25; ++v) {
                arr_b22[v] = (byte)(arr_b22[v] ^ arr_b3[v]);
            }
​
            s = new String(arr_b0) + new String(arr_b22) + new String(arr_b11);
        }
​
        System.out.println(s);
}
```

然后再去查看另一个计算余额的过程，发现其中有涉及到token，就是账号密码的组合值，这个token至少是一个固定值，才可以正确计算出flag，先逆推出token。

```
public static void main(...
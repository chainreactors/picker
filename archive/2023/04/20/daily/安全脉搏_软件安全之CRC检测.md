---
title: 软件安全之CRC检测
url: https://www.secpulse.com/archives/199212.html
source: 安全脉搏
date: 2023-04-20
fetch_date: 2025-10-04T11:31:38.226402
---

# 软件安全之CRC检测

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 软件安全之CRC检测

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-04-19

14,248

#### **CRC介绍**

在玩某些游戏，例如fps类游戏时，你想要修改某些特定的数值实现一些功能，这时你很有可能会被查封账号甚至禁封机器码。因为你更改了游戏中的数据，从而导致接收方收到”错误的数据“。为尽量提高接收方收到数据的正确率，在接收数据之前需要对数据进行差错检测，这种检测就是我们所说的CRC检测。

CRC也叫循环冗余校验码，它属于密码学一类算法，常用于数据校验，一般会用来检测程序是否被脱壳或者被修改，以达到防破解的目的。CRC运算实际上就是将数据k进行模2运算，得到余数n，然后将n拼接到k的后面生成k+n为循环冗余校验码的字长。接着发送k+n到接收方作为被除数进行模2运算，判断余数是否为0，如果余数非0则CRC检测出数据被修改了。简单点说，就是把需要校验的数据与生成多项式进行循环异或处理。

#### **PS：**

1.发送方和接受方会约定一个特定的除数，它是一个定值，我们也叫除数为生成多项式。

2.在计算余数时，被除数也就是数据k需要进行补0，补0个数为生成多项式长度-1个0。

3.余数长度一定与补零的长度一致

#### 流程图：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199212-1681875935.png "null")

讲了这么多不如来个例子好理解

例子1：这里数据为1110101，生成多项式为101，那么我们要传给接收方的数据就为1110101（数据）+10（余数）=111010110

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199212-1681875936.png "null")

这个就是CRC的计算原理了

#### **CRC计算的两种方式**

#### **1.直接计算法**

这里我们通过例子来讲解，例子2：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199212-1681875937.png "null")

首先我们看到这里的生成项是1101，然后在计算中的除数（蓝色字体标记）大多是1101而有时是0000，当除数为1101时被除数的首位都是1，而首位不为1时就是0000。那么我们不妨做个假设，既然被除数和除数的首位为1时会被消掉那么我们就不需要四位异或了，改成三位异或，三位异或的话被除数一次就取三个，而除数取后三个，当被除数首位为1时就左移一位让新的三位与除数（生成项）的后三位进行异或；当被除数移出位是0时就异或000，然后不断重复此步骤直至结束。（这里是针对本例题的，当你的生成项为n时，你就取n-1位异或）

那么就会有人问到底需要重复几次才算结束呢？

处理次数=待处理数据位数（被除数位数）=商的位数（本题次数为6次）

例如本题第一次被除数取100，左移一位得001然后与101异或得100。100左移一位得000然后与101异或得101。101左移一位得010然后与101异或得111。111左移一位得110然后与101异或得011。011左移一位得110然后与000异或得110（与000异或值是不变的）。110左移一位得100然后与101异或得001得到余数刚好6次。

#### **2.驱动表法**

驱动表法没有直接计算法得直观，但是效率却比直接计算法要高那么如何实现呢？我们知道直接计算法是一步一步从上往下来异或得到得结果，在算得过程中会有异或许多生成项，而生成项又是不变的，那么是不是可以提前计算出与数据前几位符合的生成项之和然后再异或呢？

那么我们就将0000 0000 ~ 1111 1111这个范围的所有生成项计算出来存储为表格，计算的时候取数据的首字节进行索引找到表中对应生成项异或的和与去掉首字节的数据进行异或就行了。

#### **表的形成**

终于过度到表了，这里我们来用算法实现表，让你清楚明白它的原理，这里我们拿CRC32表的形成举例首先得了解一下CRC32的生成项是什么

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199212-1681875939.png "null")

想要了解更多的CRC以及它的生成多项式可以去这里看：http://www.ip33.com/crc.html

```
#include <windows.h>
#include <stdio.h>

int main()
{
    DWORD crc;
    for (DWORD i = 0; i < 256; i++)//256个元素
    {
        crc = i;
        for (DWORD k = 0; k < 8; k++)//因为这里异或是从数据的高位开始，所以需要计算的数据左移8位，这里就需要计算8次
        {
            if (crc & 1)//判断最高位是否为1
                crc = (crc >> 1) ^ 0xEDB88320;//最高位为1，右移一位，然后与0xEDB88320异或
            else
                crc = crc >> 1;//最高位为0时，不用异或，整体数据右移一位。相当于例子2中110与000异或值是不变的
        }
        printf ("0x%08x, ", crc);
        if (((i+1)%6) == NULL )
            printf ("n");
    }
}

/*CRC32表
0x00000000, 0x77073096, 0xee0e612c, 0x990951ba, 0x076dc419, 0x706af48f,
0xe963a535, 0x9e6495a3, 0x0edb8832, 0x79dcb8a4, 0xe0d5e91e, 0x97d2d988,
0x09b64c2b, 0x7eb17cbd, 0xe7b82d07, 0x90bf1d91, 0x1db71064, 0x6ab020f2,
0xf3b97148, 0x84be41de, 0x1adad47d, 0x6ddde4eb, 0xf4d4b551, 0x83d385c7,
0x136c9856, 0x646ba8c0, 0xfd62f97a, 0x8a65c9ec, 0x14015c4f, 0x63066cd9,
0xfa0f3d63, 0x8d080df5, 0x3b6e20c8, 0x4c69105e, 0xd56041e4, 0xa2677172,
0x3c03e4d1, 0x4b04d447, 0xd20d85fd, 0xa50ab56b, 0x35b5a8fa, 0x42b2986c,
0xdbbbc9d6, 0xacbcf940, 0x32d86ce3, 0x45df5c75, 0xdcd60dcf, 0xabd13d59,
0x26d930ac, 0x51de003a, 0xc8d75180, 0xbfd06116, 0x21b4f4b5, 0x56b3c423,
0xcfba9599, 0xb8bda50f, 0x2802b89e, 0x5f058808, 0xc60cd9b2, 0xb10be924,
0x2f6f7c87, 0x58684c11, 0xc1611dab, 0xb6662d3d, 0x76dc4190, 0x01db7106,
0x98d220bc, 0xefd5102a, 0x71b18589, 0x06b6b51f, 0x9fbfe4a5, 0xe8b8d433,
0x7807c9a2, 0x0f00f934, 0x9609a88e, 0xe10e9818, 0x7f6a0dbb, 0x086d3d2d,
0x91646c97, 0xe6635c01, 0x6b6b51f4, 0x1c6c6162, 0x856530d8, 0xf262004e,
0x6c0695ed, 0x1b01a57b, 0x8208f4c1, 0xf50fc457, 0x65b0d9c6, 0x12b7e950,
0x8bbeb8ea, 0xfcb9887c, 0x62dd1ddf, 0x15da2d49, 0x8cd37cf3, 0xfbd44c65,
0x4db26158, 0x3ab551ce, 0xa3bc0074, 0xd4bb30e2, 0x4adfa541, 0x3dd895d7,
0xa4d1c46d, 0xd3d6f4fb, 0x4369e96a, 0x346ed9fc, 0xad678846, 0xda60b8d0,
0x44042d73, 0x33031de5, 0xaa0a4c5f, 0xdd0d7cc9, 0x5005713c, 0x270241aa,
0xbe0b1010, 0xc90c2086, 0x5768b525, 0x206f85b3, 0xb966d409, 0xce61e49f,
0x5edef90e, 0x29d9c998, 0xb0d09822, 0xc7d7a8b4, 0x59b33d17, 0x2eb40d81,
0xb7bd5c3b, 0xc0ba6cad, 0xedb88320, 0x9abfb3b6, 0x03b6e20c, 0x74b1d29a,
0xead54739, 0x9dd277af, 0x04db2615, 0x73dc1683, 0xe3630b12, 0x94643b84,
0x0d6d6a3e, 0x7a6a5aa8, 0xe40ecf0b, 0x9309ff9d, 0x0a00ae27, 0x7d079eb1,
0xf00f9344, 0x8708a3d2, 0x1e01f268, 0x6906c2fe, 0xf762575d, 0x806567cb,
0x196c3671, 0x6e6b06e7, 0xfed41b76, 0x89d32be0, 0x10da7a5a, 0x67dd4acc,
0xf9b9df6f, 0x8ebeeff9, 0x17b7be43, 0x60b08ed5, 0xd6d6a3e8, 0xa1d1937e,
0x38d8c2c4, 0x4fdff252, 0xd1bb67f1, 0xa6bc5767, 0x3fb506dd, 0x48b2364b,
0xd80d2bda, 0xaf0a1b4c, 0x36034af6, 0x41047a60, 0xdf60efc3, 0xa867df55,
0x316e8eef, 0x4669be79, 0xcb61b38c, 0xbc66831a, 0x256fd2a0, 0x5268e236,
0xcc0c7795, 0xbb0b4703, 0x220216b9, 0x5505262f, 0xc5ba3bbe, 0xb2bd0b28,
0x2bb45a92, 0x5cb36a04, 0xc2d7ffa7, 0xb5d0cf31, 0x2cd99e8b, 0x5bdeae1d,
0x9b64c2b0, 0xec63f226, 0x756aa39c, 0x026d930a, 0x9c0906a9, 0xeb0e363f,
0x72076785, 0x05005713, 0x95bf4a82, 0xe2b87a14, 0x7bb12bae, 0x0cb61b38,
0x92d28e9b, 0xe5d5be0d, 0x7cdcefb7, 0x0bdbdf21, 0x86d3d2d4, 0xf1d4e242,
0x68ddb3f8, 0x1fda836e, 0x81be16cd, 0xf6b9265b, 0x6fb077e1, 0x18b74777,
0x88085ae6, 0xff0f6a70, 0x66063bca, 0x11010b5c, 0x8f659eff, 0xf862ae69,
0x616bffd3, 0x166ccf45, 0xa00ae278, 0xd70dd2ee, 0x4e048354, 0x3903b3c2,
0xa7672661, 0xd06016f7, 0x4969474d, 0x3e6e77db, 0xaed16a4a, 0xd9d65adc,
0x40df0b66, 0x37d83bf0, 0xa9bcae53, 0xdebb9ec5, 0x47b2cf7f, 0x30b5ffe9,
0xbdbdf21c, 0xcabac28a, 0x53b39330, 0x24b4a3a6, 0xbad03605, 0xcdd70693,
0x54de5729, 0x23d967bf, 0xb3667a2e, 0xc4614...
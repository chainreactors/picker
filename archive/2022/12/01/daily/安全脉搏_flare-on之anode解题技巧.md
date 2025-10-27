---
title: flare-on之anode解题技巧
url: https://www.secpulse.com/archives/192610.html
source: 安全脉搏
date: 2022-12-01
fetch_date: 2025-10-04T00:10:00.712904
---

# flare-on之anode解题技巧

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

# flare-on之anode解题技巧

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[ChaMd5安全团队](https://www.secpulse.com/newpage/author?author_id=3747)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-11-30

12,937

## 类型判断

Anode是一道类型非常经典的逆向题，请求用户输入flag，判断是否正确：![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192610-1669793645.png)

从IDA给出的信息来判断，这题是由NodeJS语言进行编写，然后NEXE打包成可执行文件：![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192610-1669793646.png)

## 源码获取

NEXE会将JS源码直接打包到EXE中，不经过任何加密或者压缩，所以很容易使用十六进制编辑工具将源码提取出来，搜索特征字符串“Enter flag”,就能快速定位到源码位置：![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192610-1669793649.png)

JS代码如下所示，分析代码可知，程序接受用户的输入flag，经过了一个非常长的switch运算最后和加密后的flag进行比较，解题必须将加密的flag逆推回去。

```
readline.question(`Enter flag: `, flag => {
  readline.close();
  if (flag.length !== 44) {
    console.log("Try again.");
    process.exit(0);
  }
  var b = [];
  for (var i = 0; i < flag.length; i++) {
    b.push(flag.charCodeAt(i));
  }

  // something strange is happening...
  if (1n) {
    console.log("uh-oh, math is too correct...");
    process.exit(0);
  }

  var state = 1337;
  while (true) {
    state ^= Math.floor(Math.random() * (2**30));
    switch (state) {
      case 306211:
        if (Math.random() < 0.5) {
          b[30] -= b[34] + b[23] + b[5] + b[37] + b[33] + b[12] + Math.floor(Math.random() * 256);
          b[30] &= 0xFF;
        } else {
          b[26] -= b[24] + b[41] + b[13] + b[43] + b[6] + b[30] + 225;
          b[26] &= 0xFF;
        }
        state = 868071080;
        continue;
      case 311489:
        if (Math.random() < 0.5) {
          b[10] -= b[32] + b[1] + b[20] + b[30] + b[23] + b[9] + 115;
          b[10] &= 0xFF;
        } else {
          b[7] ^= (b[18] + b[14] + b[11] + b[25] + b[31] + b[21] + 19) & 0xFF;
        }
        state = 22167546;
        continue;
      case 755154:
        if (93909087n) {
          b[4] -= b[42] + b[6] + b[26] + b[39] + b[35] + b[16] + 80;
          b[4] &= 0xFF;
        } else {
          b[16] += b[36] + b[2] + b[29] + b[10] + b[12] + b[18] + 202;
          b[16] &= 0xFF;
        }
        state = 857247560;
        continue;

      case 1045388446:
        if (Math.random() < 0.5) {
          b[33] += b[40] + b[17] + b[43] + b[21] + b[36] + b[23] + 76;
          b[33] &= 0xFF;
        } else {
          b[20] -= b[37] + b[30] + b[12] + b[15] + b[6] + b[7] + 88;
          b[20] &= 0xFF;
        }
        state = 204284567;
        continue;
        //......省略，代码非常长
        //......省略，代码非常长
        //......省略，代码非常长
      case 1071767211:
        if (Math.random() < 0.5) {
          b[30] ^= (b[42] + b[9] + b[2] + b[36] + b[12] + b[16] + 241) & 0xFF;
        } else {
          b[20] ^= (b[41] + b[2] + b[40] + b[21] + b[36] + b[17] + 37) & 0xFF;
        }
        state = 109621765;
        continue;
      default:
        console.log("uh-oh, math.random() is too random...");
        process.exit(0);
    }
    break;
  }

  var target = [106, 196, 106, 178, 174, 102, 31, 91, 66, 255, 86, 196, 74, 139, 219, 166, 106, 4, 211, 68, 227, 72, 156, 38, 239, 153, 223, 225, 73, 171, 51, 4, 234, 50, 207, 82, 18, 111, 180, 212, 81, 189, 73, 76];
  if (b.every((x,i) => x === target[i])) {
    console.log('Congrats!');
  } else {
    console.log('Try again.');
  }
});
```

## 坑点

这题有埋坑的地方，题目源码很明显给了提示，正常情况下，if块将会被执行，但是从实际运行结果来看，这个字符串并没有输出，程序也没有退出，很明显，这题修改了V8引擎。![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192610-1669793651.png)

不仅bigint类型的真假值判断被修改了，随机数生成也被修改了，因为程序每次都会走到相同的switch分支：![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192610-1669793652.png)

正常的解题思路是分析V8源码修改的地方，使用bindiff和对比源码的方法去分析，不过由于时间有限，我决定另辟蹊径，通过黑盒的方法去把这些关键信息收集到，即使我对它如何修改V8引擎细节一无所知。

## 信息收集

通过修改exe中js源码的方法，将随机数值以及每个if判断数值为真或为假直接打印出来，通过收集到的信息修复JS代码，使得它在正常的JS引擎也能运行起来。如何修改呢？方法非常简单，只需要对ReadFile下断点，在它把JS数据读入内存中后进行修改：![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192610-1669793654.png)

直接修改js源码，插入两段代码，一个获取随机值：![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192610-1669793659.png)

一个获取if判断的值，为真还是为假：![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192610-16697936591.png)

## 修复JS

### 修复

知道以上信息就可以着手修复JS代码了，将if的值直接替换成true或者false:

```
import subprocess
import right
import re
import right_judge
all_case_num=[]
def fix_js():
 count=1
 n_c=0
 fix_flag=False
 out_line=''
 with open('test_no_input.js','rt') as fd:
  line=fd.readline()
  while line:
   if 'case' in line:
    fix_flag=True
   if fix_flag and 'if' in line  and '>' not in line and '<' not in line:
    p = re.compile(r'[(](.*?)[)]', re.S)
    all_case_num.append(re.findall(p, line)[0])
    if right_judge.all_case_judge[n_c]:

     line='      if (true) {n'
    else:
     line='      if (false) {n'
    fix_flag=False
    n_c+=1
   out_line+=line
   line=fd.readline()
 print(out_line)
 with open('fixed_test.js','wt+') as fdo:
  fdo.write(out_line)

if __name__ == '__main__':

 fix_js()
```

得到JS内容如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192610-1669793661.png)

### 化简

为了进一步提高可读性，编写脚本进行进一步化简，将switch结构修改成顺序执行，并将随机值的运算结果进行求解。

```
import subprocess
import right
import re
import flare_random
import math
all_case_num=[]
end_num=185078700
random_magic_str='getrand(pos++)'
def fix_js():
 random_pos=0
 rcn=right.right_case
 rand_num=flare_random.randnum
 all_const_num=''

 out_line=[]
 with open('fixed_test.js','rt') as fd:
  data=fd.read()
 for case_num in rcn:
  random_pos...
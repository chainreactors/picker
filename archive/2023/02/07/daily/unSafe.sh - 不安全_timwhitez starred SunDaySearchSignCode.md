---
title: timwhitez starred SunDaySearchSignCode
url: https://buaq.net/go-148173.html
source: unSafe.sh - 不安全
date: 2023-02-07
fetch_date: 2025-10-04T05:50:05.009936
---

# timwhitez starred SunDaySearchSignCode

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

timwhitez starred SunDaySearchSignCode

Tip在看雪上看到一段代码注释“此函数采用最快的内存字符特征匹配算法SunDay,搜索2GB内存只需1秒”。功能SunDay算法实现的Dll或者EXE的指定特征码地址获
*2023-2-6 18:42:5
Author: [github.com(查看原文)](/jump-148173.htm)
阅读量:26
收藏*

---

#### Tip

在[看雪](https://bbs.pediy.com/thread-192985.htm)上看到一段代码注释“此函数采用最快的内存字符特征匹配算法SunDay,搜索2GB内存只需1秒”。

#### 功能

SunDay算法实现的Dll或者EXE的指定特征码地址获取,不支持模糊搜索。

#### 补充

可根据需要修改SUNDAY返回值类型，返回的是指针地址。

```
/**
 *  参数一：内存的起点
 *  参数二：查找的二进制
 *  参数三：查找二进制的大小
 *  参数四：最大查找字节
 */
DWORD SUNDAY(unsigned char *lpBaseBuf, unsigned char *pFindData,DWORD nFindDataSize,DWORD nMaxSize)
```

```
unsigned char* szFindStart = (unsigned char*)pbuf;
unsigned char* szFindRet;
int nMaxLen = nLen;
do
{
	szFindRet = SUNDAY(szFindStart,(unsigned char*)"FindMe",nFindLen1,nMaxLen);
	if (!szFindRet) {
		break;
	}
	szFindStart = szFindRet;
	nMaxLen = nLen - (szFindRet-(unsigned char*)pbuf);
	// Do something

}while(1);
```

文章来源: https://github.com/wanttobeno/SunDaySearchSignCode
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)
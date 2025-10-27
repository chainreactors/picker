---
title: 《英雄无敌》4：修改pe导入表注入DLL扩展回城术功能
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458587767&idx=1&sn=dd1c04637890c14cb9d72fb95bbb0010&chksm=b18c22fd86fbabeb091b9da8f2eb78367a9ba58be94d692dfb5985669358045a1598a798ebb2&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-12-26
fetch_date: 2025-10-06T19:38:57.978564
---

# 《英雄无敌》4：修改pe导入表注入DLL扩展回城术功能

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EficNsfyv6H2XuGwTPCuDQ5xXH3WKUcYLBN5lowOV90lAdjicBE3COVdAbXdJZeLLrwShibCw3vRGug/0?wx_fmt=jpeg)

# 《英雄无敌》4：修改pe导入表注入DLL扩展回城术功能

fdark

看雪学苑

```
一

前言
```

##

《英雄无敌》4，是3DO陷入财政危机之际，仓促抛出的一个完成约90%的产品，可惜了这个游戏，尽管仓促被抛出，也无法挽救3DO的倒闭，产品、项目等全被他人买去（自然，《英雄无敌》项目被育碧买断，很多朋友都是知道的）。

NEW COMPUTING WORLD的设计人员，在3代的基础上作出了重大实质性修改，其主要目的是让“英雄”不再是旁观者！而是要亲临其中，通过“修炼”能让“英雄”真正无敌！实际上，初出时的平衡性并不是不可接受的，而是因其仓促出货，导致游戏没有被严格测试，尤其像玩家试玩那样的测试，连像内存泄露这样的问题都没有发现、消除就推出产品，导致被玩家唾弃！实在可惜！这也是这个产品，在3DO倒闭后，被玩家拿来做各种MOD使其新生，网络上的《英雄无敌》4一片欣欣向荣！

对于一个从《英雄无敌》1代开始，就是这个游戏的忠实粉丝的我来说，游戏平衡性我是不关心的（不平衡，正好符合玩的爽的要求），但它的“战争迷雾”系统却是让我极为不爽的东西，还有就是居然加快游戏进程的回城术，只是一个小回城术！魔法中加快游戏进程的时空之门完全没有了，回城术还是小回城术，使得游戏的时间都在“英雄”满地图跑路上，既无聊也实在没有必要这样为延长游戏时间而延长时间（不知浪费时间就是浪费生命吗？）地使得玩家的游戏进程非常缓慢。

“战争迷雾”一直没有找到消除的方法，关键是找不到线索（当然还没有放弃，但不是当务之急），于是便先想着怎么把回城术改一改，以便使游戏进程不那么慢，这便是这篇文章的起因！

```
二

寻找回城术施放程序
```

#

《英雄无敌》4里的回城术，不象前面1、2、3代那样，如果最近的城堡被占，就有Nearest Town Occupied的提示，它的回城术总是可以成功的，因为它可以让英雄回到稍远一点城堡，并且每个城堡门口可以站4组队伍，而游戏中只能最高8支队伍，这样只要两个城堡就一定回城术使用成功。缺少提示后，怎么去找线索呢？是个问题！

只好拿出CE，根据英雄的经验值搜索，得到英雄在内存中的数据，这些数据网络上有很多信息，可以知道英雄的技能、带的兵、装备、所学的魔法等。数据如下（以每行16字节显示）。

经验值（4字节）+12字节（正好这行满），其后整11行，再后面就是技能共9行，其后的24个字节就是魔法啦。如下就是一个例子：

```
00 00 40 08 00 40 00 00 00 01 00 04 00 20 00 00     40=0100 0000 08=0000 1000 01=0000 0001
00 00 40 00 00 00 20 00 spell                       20=0010 0000 <--this is Town Gate
                power-->17 00 00 00 00 00 00 00
```

24字节后面的DWORD是英雄的当前魔法值。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOYTC6yRLnfYG9myJDGicr9s3xNoEricKmerDefBTfXIG4CAxey1PH2wP8RPNaLbMtQHfyCEantjWA/640?wx_fmt=jpeg&from=appmsg)

看英雄的经验正是1AB6（十进制，6838）

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOYTC6yRLnfYG9myJDGicr9OvLtRZCaSH3GOPYmQYLaJGKIxEtKu88GyOJrCC3e4YhVhTKor9iaNFA/640?wx_fmt=jpeg&from=appmsg)

而魔法的每个字节有8位，每位为1就是有魔法，为0就是没有魔法，例如上面数据的20这个数据就是Town Gate。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOYTC6yRLnfYG9myJDGicr95QRF6f95CN9TsicfKMaicUnrWpkibf1xdEkFI28VCqCRADdicsdX3fTa8w/640?wx_fmt=jpeg&from=appmsg)

这时可以用CE修改它，再看英雄的魔法书，就会知道20那个字节就是回城术。知道了回城术的魔法地址了，选中这个地址，将其添加到列表中。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOYTC6yRLnfYG9myJDGicr9ALoIMMX3yzZxT5v6SeibSxm3JmoBcSRm0ozCYicZ5TT2BNM9rEFVc8Sw/640?wx_fmt=jpeg&from=appmsg)

右键选择：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOYTC6yRLnfYG9myJDGicr9PbpJW7I3ozZshbqMsicgjoy9fPicEGMh3OTKtEczgxwosicpdAslOu11g/640?wx_fmt=jpeg&from=appmsg)

回到游戏中，让英雄使用回城术，得到信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOYTC6yRLnfYG9myJDGicr9CHW9V4bb5QGeiapbo4AwlibmdwiabUJPDM2bv2AW3tYicSVxVY2UTfzJTQ/640?wx_fmt=jpeg&from=appmsg)

X32dbg打开游戏，来到上面的00865C9E，向上寻找子程序起始位置，在此下断。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOYTC6yRLnfYG9myJDGicr9FW3eib4YfRUKOh3t5pZ7KMqbo7oKI0EksVz6mThkSGWLgoABaDmTMdA/640?wx_fmt=jpeg&from=appmsg)

游戏中再次让英雄施放回城术，结果被断下。说明这确实是施放回城术的子程序中内容，让程序运行至return处再返回，找到它的调用者。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOYTC6yRLnfYG9myJDGicr9Jz2lE5mzd4jsHUjBYHETMelzibj36l91BWS1uZC3LWfyAaLe2rJBmWw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOYTC6yRLnfYG9myJDGicr9c8nicqZ6c0tHZObl5OaoC1m7M9icBnDeTwMHvaiaos2jsJklkrVuIGktA/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOYTC6yRLnfYG9myJDGicr9A3AWibhQ55U4IHPKcou8uvicmVTVNLSA48aFRR6HQNjRFJG99iboJdZdg/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOYTC6yRLnfYG9myJDGicr97j7NOIicAvPDkT81JcDAibKm7VxJNH1ZLnh3YYEglia1LGvOOm3KzEicibw/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOYTC6yRLnfYG9myJDGicr9njrwdnjJDdEnRo0AoXzOgZHP0y21lfR4dc1icWKXQuLyiaCLPXIu0eeQ/640?wx_fmt=jpeg&from=appmsg)

来到此处，可以看到，这是一个switch-case的结构，因此，刚刚调用的子程序就是回城术子程序。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOYTC6yRLnfYG9myJDGicr9bvRe9hLwMwHUQMdXx31QX2UEM6jzq7dnpibziaHUFtdL2rnapJ7mdKOg/640?wx_fmt=jpeg&from=appmsg)

如果在上一图中继续return，则会出现到以前出现的子程序中了，所以，上一步找到的子程序5085E0就是回城术的。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOYTC6yRLnfYG9myJDGicr9OhyKXsZlx3np4qrMCBFRmOQGuxACKXn6J2gVGB6HRtOS8IAGT9SZmg/640?wx_fmt=jpeg&from=appmsg)

下面取消其它的断点，在5085E0下断，再施放回城术，果然被断下。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOYTC6yRLnfYG9myJDGicr9OR0ExIcW6mLJmbO7KZwO7bTxGGSpf3ibJtn5HPMAZiaevH6ea68BaXFQ/640?wx_fmt=jpeg&from=appmsg)

#

```
三

分析回城术施放程序遇到的困难
```

#

原以为找到施放程序后，破解它就轻而易举了，结果却大错特错！先来看看这个程序的X32DBG给出的流程图。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOYTC6yRLnfYG9myJDGicr9ibXhDFdj8Y8YAHDBuTNp2m1gfmAqzrGTo8Dc8hprSULic5sLJvTicLwSw/640?wx_fmt=jpeg&from=appmsg)

看到这个图后不禁让人气馁，心想一个回城术至于这样复杂吗？然而继续深入看下去才真的想放弃了！原来这个程序真是处处有call，call中再call，几乎无穷无尽！随便看下它的任意一个子程序，都会让人生出踟蹰不前之心，例如：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOYTC6yRLnfYG9myJDGicr9kI2YlEhFnZUb9UkmUicPia8icuibxuLQv7xOdibbn6I3EYHEALnqpTeQpOQ/640?wx_fmt=jpeg&from=appmsg)

在修改《英雄无敌》1、2、3代的回城术时，都能很快找到关键位置，见前文：

[原创]修改PE入口点方式注入自己编写的DLL——《英雄无敌》1代小回城术修改成大回城术：https://bbs.kanxue.com/thread-283811.htm

例如对《英雄无敌》1代回城术修改时，可以找player的城堡总数，因为小回城术必须比对每个城堡与英雄之间距离远近，有了城堡总数就会很容易定位到城堡数循环位置，分析其中的算法，就会找到破解的切入点。而且，在1-3代里，新占领的城堡总是放在城堡排序的最后。

然而到了《英雄无敌》4这里，情况就变了！第一，没有城堡总数；第二，城堡的排序也不是固定的，而是将新占领的城堡插入在不知按照什么规律的位置，这两个变化几乎让你无法判断从哪里下手？再加之其子程序一个一个的嵌套，使得你不深入分析每个子程序的功能，就根本无法看清程序的作用！又何谈破解它呢？

哎，没法子，只能拿出“细嚼慢咽”的功夫，一个一个的子程序梳理啦，最终找到7E4410子程序是要破解的位置。

```
四

DLL设计
```

看过《修改PE入口点方式注入自己编写的DLL——《英雄无敌》1代小回城术修改成大回城术》这篇文章的朋友都知道那是用下拉框制作的DLL，但是奇怪的是最近使用却发现下拉框只显示5条内容了，无论怎么调整就是不能全部显现。这次将下拉框改成列表框。设计语言是masm32，资源文件和前文中的差不多，只是把下拉框combobox控件改成listbox控件而已，因此这个原文件就不放上来了，这里给出dll主文件：

```
;********************************************************************
		.386
		.model flat, stdcall
		option casemap :none
;********************************************************************
; Include 文件定义
include		windows.inc
include		user32.inc
includelib	user32.lib
include		kernel32.inc
includelib	kernel32.lib
include		gdi32.inc
includelib	gdi32.lib
;********************************************************************
; Equ 等值定义
DLG_MAIN	equ	1
IDC_LISTBOX	equ	101
;********************************************************************
; 数据段
			.data?
hInstance	dd	?
dwCount		dd 	?
dwTown		dd	?

			.const
sz1			db	'1st    Town',0
sz2			db	'2nd    Town',0
sz3			db	'3rd    Town',0
sz4			db	'4th    Town',0
sz5			db	'5th    Town',0
sz6			db	'6th    Town',0
sz7			db	'7th    Town',0
sz8			db	'8th    Town',0
sz9			db	'9th    Town',0
sz10		db	'10th   Town',0
sz11		db	'11th   Town',0
sz12		db	'12th   Town',0
sz13		db	'13th   Town',0
sz14		db	'14th   Town',0
sz15		db	'15th   Town',0
sz16		db	'16th   Town',0
sz17		db	'17th   Town',0
sz18		db	'18th   Town',0
sz19		db	'19th   Town',0
sz20		db	'20th   Town',0
sz21		db	'21st   Town',0
sz22		db	'22nd   Town',0
sz23		db	'23rd   Town',0
sz24		db	'24th   Town',0
sz25		db	'25th   Town',0
sz26		db	'26th   Town',0
sz27		db	'27th   Town',0
sz28		db	'28th   Town',0
sz29		db	'29th   Town',0
sz30		db	'30th   Town',0
pTable		dd	sz1,sz2,sz3,sz4,sz5,sz6,sz7,sz8,sz9,sz10,sz11,sz12,sz13,sz14,sz15,\
				sz16,sz17,sz18,sz19,sz20,sz21,sz22,sz23,sz24,sz25,sz26,sz27,sz28,sz29,sz30
;********************************************************************
; 代码段
		.code
;********************************************************************
; dll 的入口函数
DllEntry	proc	_hInstance,_dwReason,_dwReserved
			mov eax,_dwReason
			.if eax == DLL_PROCESS_ATTACH
				push _hInstance
				pop	 hInstance
			.endif
			mov	eax,TRUE
			ret
DllEntry	endp
;********************************************************************
_DlgProc	proc	uses ebx edi esi _hWnd,_wMsg,_wParam,_lParam
		local	@nCount:dword

		mov	eax,_wMsg
		.if	eax == WM_CLOSE
			invoke	EndDialog,_hWnd,NULL
		.elseif	eax == WM_INITDIALOG
;********************************************************************
; 初始化组合框
			mov esi,0
			mov ebx,dwCount
			mov @nCount,ebx
			dec @nCount
			mov ebx, offset pTable
	@@:		mov edi, [ebx + esi*4]
			invoke	SendDlgItemMessage,_hWnd,IDC_LISTBOX,LB_ADDSTRING,0,edi
			.if esi == @nCount
				jmp @F
			.endif
			inc esi
			jmp @B
	@@:
;invoke	SendDlgItemMessage,_hWnd,IDC_LISTBOX,LB_SETCURSEL,0,0
;********...
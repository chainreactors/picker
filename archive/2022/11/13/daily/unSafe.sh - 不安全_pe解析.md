---
title: pe解析
url: https://buaq.net/go-135271.html
source: unSafe.sh - 不安全
date: 2022-11-13
fetch_date: 2025-10-03T22:36:34.271802
---

# pe解析

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

![](https://8aqnet.cdn.bcebos.com/5a269bdae00cb7b35bbe78443271c84b.jpg)

pe解析

去年学了一遍pe，但是没有用代码实现，导致对pe的理解非常浅，今年又重新学了一遍，旨在加强对代码的掌握，并不是从0开始，只是方便本人理解，因此笔记内容很残缺，可以参考去年的笔记一起看。代码
*2022-11-12 01:16:10
Author: [0range-x.github.io(查看原文)](/jump-135271.htm)
阅读量:106
收藏*

---

去年学了一遍pe，但是没有用代码实现，导致对pe的理解非常浅，今年又重新学了一遍，旨在加强对代码的掌握，并不是从0开始，只是方便本人理解，因此笔记内容很残缺，可以参考去年的笔记一起看。

代码仓库：

<https://github.com/0range-x/windows/tree/main/pe>

## PE头解析

4gb = 2^32 ，寻址长度，

对齐的目的：查找速度更快，用空间换时间

硬盘对齐：200h

内存对齐：1000h

所以程序在内存执行的时候，会在内存中扩展。节和节之间用0填充。

dos头、pe头、pe可选头

#### dos头

|  |  |
| --- | --- |
| ``` 1 ``` | ``` e_magic			//5A 4D e_lfanew 		//00 00 00 E8       pe头相对于文件的偏移，用于定位pe文件 ``` |

从e8开始就是pe开始的地方，对应的 50 45 对应的ascii字符是pe，

包含signature+标准pe头(Image\_File\_Header)+**可选pe头(IMAGE\_OPTIONAL\_HEADER)**

signature为50 45 00 00 ，找完后不找nt\_headers，去找 Image\_File\_Header，

大小确定

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` WORD		Machine					//86 64 	//可以在什么机器上运行  WORD		NumberOfSections		//07 00		//文件中存在的节的总数，如果要新增或者合并节需要修改该字段 DWORD		TimeDateStamp			//2b 8c 95 22		//文件编译时间戳  WORD		SizeOfOptionalHeader	//f0 00	 	可选pe头的大小，32位pe默认为E0h,64位pe为f0h，大小可以自定义 ``` |

大小不确定

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ``` | ``` WORD		Magic						//0b 02   //10b为32位的文件，20b为64位的文件 DWORD		SizeOfCode					//00 60 02 00 DWORD		SizeOfInitializedData		//00 00 03 00 DWORD		SizeOfUNinitializedData		//00 00 00 00 DWORD		AddressOfEntryPoint			//90 1b 00 00		//程序入口  != 代码入口 ，程序在内存中真正的运行地址为   基址+oep (入口点)  DWORD		BaseOfCode					//00 10 00 00 DWORD		BaseOfData					//00 00 00 40 DWORD		ImageBase					//01 00 00 00 		//内存映像基址 DWORD		SectionAlignment			//00 10 00 00		//内存对齐，内存中整个pe文件的尺寸，可以比实际值大，但必须是SectionAlignment的整数倍 DWORD		FileAlignment				//00 10 00 00		//文件对齐 DWORD		SizeofImage					//00 70 05 00		//内存中 整个PE文件的映射的大小，可以比实际的值大，但必须是SectionAlignment的整数倍 DOWRD		SizeofHeaders				//00 10 00 00		//所有头(DOS+...+PE标记+标准PE+可选PE)+节表 按照文件对齐后lao 否则加载会出错 DWORD		SizeOfStackReverse			//00 00 08 00 DWORD		SizeofStackCommit			//00 00 00 00 DWORD		SizeOfHeapReverse			//00 10 01 00 DWORD		SizeOfHeapCommit 			//00 00 00 00 ``` |

将pe文件从硬盘中读到内存中，是原封不动的读进去，拷贝到内存中，存储到 `FileBuffer`,但这个时候还没有办法运行，需要peloader修改 `FileBuffer`为内存中可执行的过程，就是内存拉伸的过程。写到的地址(内存运行的起始地址)叫`ImageBuffer`（文件映像）

修改OEP

pe后面的20个字节为标准pe头

剩下的为可选pe头，从0b 02 开始。 修改 `ImageBase`(程序入口点 EntryBase)，保存后程序仍然正常运行

![image-20220925134144246](https://0range-x.github.io/2022/11/12/%E9%87%8D%E5%9B%9EPE%E7%BB%93%E6%9E%84/image-20220925134144246.png)

## 节表

相当于节中的目录 描述 节中的概要信息

定位节表：

可选pe头的大小是不确定的，标准pe头里有个成员变量 `SizeofOptionalHeader` 表示可选pe头的大小，32位默认是 e0， 64位默认是 f0

dos+4+pe+可选pe

|  |  |
| --- | --- |
| ``` 1 ``` | ``` ifanew + 4(signature) + 20(标准pe头大小) +E0(32位的 SizeOfOptionalHeader) ``` |

Image\_File\_Header（标准pe） 里的 `NumberOfSections` 是节表的数量

pe后面的第二个成员，就是节表数量，这里是5个。

![image-20220926143523309](https://0range-x.github.io/2022/11/12/%E9%87%8D%E5%9B%9EPE%E7%BB%93%E6%9E%84/image-20220926143523309.png)

|  |  |
| --- | --- |
| ``` 1 ``` | ``` #define IMAGE_SIZEOF_SHORT_NAME				8 ``` |

![image-20220926141455399](https://0range-x.github.io/2022/11/12/%E9%87%8D%E5%9B%9EPE%E7%BB%93%E6%9E%84/image-20220926141455399.png)

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` 1.Name 占8个字节，一般情况下是以"\0"结尾的ASCII码字符串来标识的名词。但是该名称并不遵守以"\0"结尾的规律，如果不是以 "\0"结尾，系统会截取8个字节的长度进行处理，有时候会导致越界乱码。 所以不用`char*`来解析， char* 会自动找 "\0"，用数组来解析。  2.Misc.VirtualSize表示在文件对齐前，实际的大小，该值可以修改，不影响，所以不一定准确  3.VirtualAddress 是节区在内存中的偏移地址，加上 ImageBase 才是在内存中的真正地址。 VirtualAddress是距离 ImageBase（ImageBuffer的dos头）的距离  4.SizeOfRawData 节在文件中对齐后的尺寸  5.PointerToRawData 节区在文件中的偏移，即在文件中距离dos头的距离 ``` |

代码空白区一般指的是 VirtualSize – SizeOfRawData 中的大小，

## FileBuffer –> ImageBuffer

![image-20220926134140064](https://0range-x.github.io/2022/11/12/%E9%87%8D%E5%9B%9EPE%E7%BB%93%E6%9E%84/image-20220926134140064.png)

FileBuffer 是在文件中的内容，Image Buffer是在内存中的内容，在内存中扩展一下

sizeofheaders 包括 dos头+标准PE头+可选PE头+节表

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` 1.根据 SizeofImage 的大小，开辟一块缓冲区（ImageBuffer） 2.根据SizeOfHeader 的大小，将头信息从FileBuffer 拷贝到 ImageBuffer 3.根据节表的信息循环将 FileBuffer 中的节拷贝到 ImageBuffer 复制到什么地方，由节中的 VirtualAddress 决定，每个节copy Siz 4 ``` |

将Filebuffer 读到 ImageBuffer，先分配 SizeOfImage 大小的内存，在可选pe头里

转VirtualAddress eg:

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` 1.  501234 - 500000(ImageBase) = 1234 (RVA) 2.  1234 > VirtualAddress(1000) 	1234 < VirtualAddress + misc.VirtualAddress 3.	1234 - 1000 = 234 4.	400(PointerToRawData) + 234 =   (在文件中的地址 ) ``` |

## 代码节空白区添加代码

关于修正E8的理解：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` | ``` 公式：X = 要跳转的地址 - (E8当前的地址 + 5)；     要跳转的地址，就是我们要加入代码MessageBox的地址；     然后要减去E8当前的地址+5的位置，这里不是太好理解；     我们的目的是要将E8后面的4个字节计算出来，然后写入到E8后面，也就是公式中X；     上面公式E8当前地址+5 ，而在此情况要定位到这个位置就要从代码的Dos开始通过指针相加；     进行位置偏移到E8当前地址+5的位置；     所以定位codeBegin的位置是：pImageBuffer指针最开始的位置（Dos头位置）通过内存中偏移的宽度移动到第一个节表的位置；     也就是上面的pSectionHeader->VirtualAddress 操作形式；     然后再偏移第一个节表在内存中对齐前实际的宽度（尺寸）pSectionHeader->Misc.VirtualSize；     上述一番操作之后就到了第一个节表没有对齐前的位置，这个位置就是我们可以添加ShellCode代码的起始位置；     到了添加ShellCode代码的起始位置之后，就要想办法添加E8位置后面的4个字节，此时根据ShellCode代码的宽度；     进行计算，确认0x6A 00 0x6A 00 0x6A 00 0x6A 00 E8 00 00 00 00 刚好向后面数13个位置，按照十六进制看；     就是0xD，所以在codeBegin偏移0xD个位置即可到达E9的位置，这也就是我们说的(E8当前的地址 + 5);     到了上面的位置之后，由于我们最终是需要在程序运行之后在内存中添加ShellCode代码；所以这里一定要计算出；     其准确的偏移地址，这样不管怎么拉伸到哪个位置，都能准确找到位置；     注意：这里需要注意一点理解，上面说的pImageBuffer这个是我们加载程序到我们申请的内存中，绝不是程序在；     运行中的那个内存，这里一定要理解清楚，她们是不一样的，理解了这个就能理解上面代码为什么要减去Dos头的；     首地址，(DWORD)(codeBegin + 0xD) - (DWORD)pImageBuffer) ``` |

关于e9修正的理解：

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` 公式：X = 要跳转的地址 - (E9当前的地址 + 5)    这里同样是要计算出E9后面4个字节的地址，我们的目的是在这里添加OEP的地址，让其执行完成MessageBox之后跳转；    OEP的地址，那么这里就要先计算出OEP地址，就是pOptionHeader->ImageBase + pOptionHeader->AddressOfEntryPoint；    再减去(E9当前的地址 + 5) 0x6A 00 0x6A 00 0x6A 00 0x6A 00 E8 00 00 00 00 E9 00 00 00 00；    (DWORD)codeBegin + SHELLCODELENGTH 就是加上ShellCode总长度，偏移完成之后减去ImageBuffer首地址再加上ImageBase； ``` |

修正oep：

|  |  |
| --- | --- |
| ``` 1 ``` | ``` 修正OEP好理解，就是定位到OEP地址，然后直接通过codeBegin地址减去pImageBuffer的首地址即可 ``` |

##### 实操

![image-20220928223839801](https://0range-x.github.io/2022/11/12/%E9%87%8D%E5%9B%9EPE%E7%BB%93%E6%9E%84/image-20220928223839801.png)

messagebox 的地址为 75 5e 06 60

找硬编码

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` 6A  00 6A  00 6A 	00 6A 	00 E8 	00 00 00 00 ；call E9 	00 00 00 00 ；jmp ``` |

查找pe信息 win10 的 32位的calc

需要注意的字段

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` AddressOfEntryPoint:	1B90 ImageBase:				400000 Section Alignment:		1000 File Alignment:			200  Section:				.text VirtualSize:			f2c（对齐前的长度） VirtualAddress:			1000（内存中的偏移） PointerToRawData:		400 （文件中的偏移） ``` |

代码空白区的起始地址为 ： PointerToRawData+VirtualSize

计算FileBuffer 代码节的结束地址

Formulas: PointerToRawData + VirtualSize = 132c

![image-20220929092350689](https://0range-x.github.io/2022/11/12/%E9%87%8D%E5%9B%9EPE%E7%BB%93%E6%9E%84/image-20220929092350689.png)

在空白区填充代码的硬编码

![image-20220929092703113](https://0range-x.github.io/2022/11/12/%E9%87%8D%E5%9B%9EPE%E7%BB%93%E6%9E%84/image-20220929092703113.png)

当程序中的文件对齐和内存对齐不一致时需要进行转换

|  |  |
| --- | --- |
| ``` 1 ``` | ``` Foa_shellcodeAddr - PointerToRawData + VirtualAddress + ImageBase = Rva_shellcodeAddr ``` |

132c - 400 + 1000 + 400000 = 40192c

e8和e9 调用地址 = 跳转的目标地址- （指令地址+ 指令长度）

计算E8后的值：

e8后的值= 真正跳转的地址 - E8 下一条指令地址

ImageBuffer 中 插入代码的地址（rva\_shellcodeaddr） ： ImageBase + Virtualsize+ VirtualAddress = 400000 +f2c +1000 = 401f2c

插入了 messagebox 对应的硬编码 8 个字节，所以 E8 的地址为 401f2c + 8 = 421f34

e8下一行地址为 ： 401f34(内存中的值) +5 = 401f39

E8 后的值： 75 94 06 60（messagebox函数运行时起始地址）-401f39（e8下一行地址）= 7553 E727

![image-20220929092703113](ht...
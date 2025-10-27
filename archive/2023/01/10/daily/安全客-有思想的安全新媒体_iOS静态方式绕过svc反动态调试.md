---
title: iOS静态方式绕过svc反动态调试
url: https://www.anquanke.com/post/id/285183
source: 安全客-有思想的安全新媒体
date: 2023-01-10
fetch_date: 2025-10-04T03:22:33.376512
---

# iOS静态方式绕过svc反动态调试

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# iOS静态方式绕过svc反动态调试

阅读量**1209966**

发布时间 : 2023-01-09 14:30:35

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

在iOS反动态调试中，常用到”svc #0x80”，通过svc汇编实现对ptrace、syscall的调用，实现反动态调试，使得lldb无法附加到app进程，不易定位到代码位置，增加反调试绕过难度。
如何绕过这种反调试手段呢？
本文通过搜索app的可执行文件，查找svc相关汇编指令的位置，并修改”svc #0x80” 为 “nop” 从而绕过反动态调试。

本文通过搜索汇编代码块的方式，连续匹配多条汇编指令，从而确定最后一条指令的地址。

## 一、svc反动态调试代码

举例说明，新创建一个测试APP，在main函数中增加svc汇编，调用svc实现ptrace：

![svc实现ptrace]( "svc实现ptrace")

这个测试app编译生成可执行文件，找到svc所在位置：

![app中的svc汇编]( "app中的svc汇编")

此时，APP在手机运行，尝试附加app就会提示失败：

```
debugserver-@(#)PROGRAM:LLDB  PROJECT:lldb-900.3.106
 for arm64.
Attaching to process TestSpace...
Segmentation fault: 11
```

## 二、查找svc汇编指令流程

大体思路是读取APP的二进制文件，解析macho格式，找到对应的代码段，把代码段内的二进制转换成汇编指令，遍历找到svc指定对应的地址：

![搜索汇编指令的流程图]( "搜索汇编指令的流程图")

## 三、主要代码解析

（1）使用capstone库做二进制转汇编。

```
int main(int argc, const char * argv[])
{
    //原文件路径
    string sFilePath = "/path/to/TestSpace";
    //存储路径
    string sFilePath_save = "/path/to/TestSpace_2";
    //将要搜索的汇编指令
    vector<string> svc_asm_vec = {"movz x0,#0x1f", "movz x1,#0", "movz x2,#0", "movz x3,#0", "movz w16,#0x1a", "svc #0x80"};

    uint64_t file_size = FileGetSize((char*)sFilePath.c_str());//计算文件大小
    void *file_buf = gain_fileBuf(sFilePath.c_str());//加载文件到内存
    //搜索到的"svc #0x80"的地址
    vector<uint64_t> addr_arry = search_svc_from_asm(file_buf, svc_asm_vec);

    if(addr_arry.size()>0){
        void * file_buf_save = alter_svc_to_nop(file_buf, addr_arry[0]);//修改第一个svc为nop
        save_buf_to_file(file_buf_save, file_size, sFilePath_save);//存储修改后的二进制到本地文件
    }

    return 0;
}
```

（2）gain\_text\_sections函数是从二进制文件中找到对应的代码段：

```
//获取二进制文件中的代码段
vector<struct section_64 const *> gain_text_sections(void * file_buf)
{
    // 判断是否为胖文件
    mach_header * mhHeader = (mach_header*)file_buf;
    vector<struct section_64 const *> sectionArray;
    // 查找代码段
    struct section_64 const * sectionTxt_DB = findSection64ByName(mhHeader, "__text", "__BD_TEXT");//

    if(sectionTxt_DB==NULL){
        NSLog(@"找不到代码段--1");
    }
    else{
        sectionArray.push_back(sectionTxt_DB);
    }

    struct section_64 const * sectionTxt = findSection64ByName(mhHeader, "__text", "__TEXT");//

    if(sectionTxt==NULL){
        NSLog(@"找不到代码段--2");
    }
    else{
        sectionArray.push_back(sectionTxt);
    }

    return sectionArray;
}
```

因为大部分APP的代码段是在Section64(**TEXT,**text)中，有的代码段在Section64(**BD\_TEXT,**text)中,因此代码中需要判断代码段的位置。

![Section64(__TEXT)]( "Section64(__TEXT)")

![Section64(__BD_TEXT)]( "Section64(__BD_TEXT)")

（3）从app的二进制文件中，搜索指定的汇编数组，如果完全符合则返回最后一条汇编指令的地址，search\_svc\_from\_asm函数会返回一个数组：

```
vector<uint64_t> search_svc_from_asm(void * file_buf, vector<string> asmStrArray)
{
    vector<uint64_t> resultVec;//声明一个int型向量
    vector<struct section_64 const *> sectionArray = gain_sections(file_buf);

    if(sectionArray.size()<1){
        NSLog(@"找不到代码段--3");
        return resultVec;
    }

    for(int i=0; i<sectionArray.size(); i++){
        struct section_64 const * sectionTxt = sectionArray[i];

        // 展示 Section64_Header中的 offset 和 size
        uint64_t offset = sectionTxt->offset;
        uint64_t text_size = sectionTxt->size;

        int tmp_length = 4;//单条汇编所占内存

        //反汇编
        Disasm * disasm = [[Disasm alloc] init];

        uint32_t my_offset = (uint32_t)0;
        uint64_t my_addr = (uint64_t)offset;
        uint32_t my_size = 0x640;//400条

        int asmStrCount = (int)asmStrArray.size();

        while(1){

            my_size = 0x640;

            if(my_offset==0){
                my_offset = (uint32_t)offset;
            }
            else{
                my_offset = my_offset + my_size - (asmStrCount-1)*tmp_length;
            }

            if(my_offset < text_size+offset && my_offset+my_size > text_size+offset)
            {
                my_size = (uint32_t)(text_size+offset-my_offset);
            }
            else if(my_offset>text_size+offset){
                break;
            }

            NSArray * asmArrayTmp = [disasm disAsmWithBuff:file_buf offset:my_offset size:my_size addr:(uint64_t)my_addr];

            int count = (int)[asmArrayTmp count];

            uint64_t first_addr = (uint32_t)my_offset;

            int samecount = 0;

            for(int i = 0; i<count; i++){
                NSString * curAsm = [asmArrayTmp objectAtIndex:i];

                for(int j=0; j<asmStrCount; j++){
                    if(j==samecount){
                        NSString * strTmp = [NSString stringWithCString:(asmStrArray[j]).c_str()  encoding:NSUTF8StringEncoding];

                        if([strTmp isEqualToString:curAsm])
                        {
                            samecount = samecount+1;
                            break;
                        }
                        else
                        {
                            samecount = 0;
                            break;
                        }
                    }
                }

                if(samecount==asmStrCount){

                    uint64_t target_addr = (uint64_t)(first_addr+i*4);
                    NSLog(@"查找到svc调用反动态调试：0x%lx    %@", target_addr, curAsm);

                    resultVec.push_back(target_addr);

                    break;
                }

            }

        }
    }

    return resultVec;
}
```

search\_svc\_from\_asm函数第二个参数是汇编指令数组，可以搜索任意汇编指令。

（4）可根据得到的汇编指令地址，修改”svc #0x80”为”nop”:

```
void * alter_svc_to_nop(void * file_buf, uint64_t target_addr)
{
    uint8_t *pBegin = (uint8_t*)file_buf;

    uint64_t target = 0xD4001001;//svc 0x80

    uint64_t textAddr_base = (uint64_t)pBegin+target_addr;

    struct SingleAss * sAss = (struct SingleAss *)(textAddr_base);

    if(sAss->singleAss == target)
    {
        sAss->singleAss = 0xD503201F;// nop
    }

    return file_buf;

}
```

（5）将修改后的二进制存储到指定文件：

```
//存储二进制到文件
void save_buf_to_file(void * file_buf, uint64_t file_size, string filePath_save){
        FILE *fp = fopen(filePath_save.c_str(), "w");
        uint8_t *pBegin = (uint8_t*)file_buf;

        fwrite((void*)pBegin, 1, file_size, fp);

        fclose(fp);

        free(file_buf);

        printf("rBuff=写入完成\n");

        printf("**********************************\n");
}
```

测试效果如下：

![结果]( "结果")

可对新生成的app做重签名，就可以做动态调试了。

## 五、注意事项

（1）search\_svc\_from\_asm 函数可以搜索任意汇编指令，第二个参数是汇编指令数组，就是要搜索的内容；

（2）如果查不到如下arm汇编：
{“mov x0,#0x1f”, “mov x1,#0”, “mov x2,#0”, “mov x3,#0”, “mov w16,#0x1a”, “svc #0x80”}
可以尝试查一下：
{“movz x0,#0x1f”, “movz x1,#0”, “movz x2,#0”, “movz x3,#0”, “movz w16,#0x1a”, “svc #0x80”}

只有完全匹配才判断为找到对应的汇编指令，如果这也找不到.

可尽量减少汇编指令的数量，例如只搜索最后两条指令{“mov w16,#0x1a”, “svc #0x80”},或者只搜索最后一条指令{“svc #0x80”}

（3）有的app中会存在很多”svc #0x80”指令，只用search\_svc\_from\_asm函数搜索”svc #0x80”指令可能会得到很多结果：

```
2022-12-15 00:19:37.636260+0800 MachConfuse[4456:36033721] 查找到svc调用反动态调试：0x7736b94    svc #0x80
2022-12-15 00:19:37.642945+0800 MachConfuse[4456:36033721] 查找到svc调用反动态调试：0x77383b4    svc #0x80
2022-12-15 00:19:37.651847+0800 MachConfuse[4456:36033721] 查找到svc调用反动态调试：0x773a824    svc #0x80
2022-12-15 00:19:37.654735+0800 MachConfuse[4456:36033721] 查找到svc调用反动态调试：0x773b570    svc #0x80
2022-12-15 00:19:37.658423+0800 MachConfuse[4456:36033721] 查找到svc调用反动态调试：0x773c5d0    svc #0x80
2022-12-15 00:19:37.660096+0800 MachConfuse[4456:36033721] 查找到svc调用反动态调试：0x773c66c    svc #0x80
......
```

全部改成”nop”也不能正常运行,尽量不要全部改为nop,可尝试逐个修改为nop后签名并测试效果。
一般情况下svc会在main函数中，可尝试找到APP二进制文件中的main函数，看其中如果有svc，可尝试修改为nop。

(4)本工程可用于搜索macho中的任意汇编指令

**源码地址：**
`https://github.com/luoyanbei/MachConfuse`

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**360 Vulpecker Team**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https:/...
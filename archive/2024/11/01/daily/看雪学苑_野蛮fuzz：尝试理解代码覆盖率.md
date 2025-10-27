---
title: 野蛮fuzz：尝试理解代码覆盖率
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579909&idx=1&sn=59aaa8bb6baf94c7d0bd1601de435870&chksm=b18dc34f86fa4a59c1ee05afea15889fc761a47bddb78f0358348acec77b3a3f71b98a1f452f&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-11-01
fetch_date: 2025-10-06T19:17:35.816756
---

# 野蛮fuzz：尝试理解代码覆盖率

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GWQXsxtiaCpMQvg1R6csm5e6FgGNdRNHbU71qiby1Xvv4Lzick9JDBrzMEkQ3tmGCVUkOegNALddEHA/0?wx_fmt=jpeg)

# 野蛮fuzz：尝试理解代码覆盖率

pureGavin【译】

看雪学苑

##

```
一

简介
```

在这一期的“野蛮fuzz”中，我们将继续由菜鸟为菜鸟的模糊测试之旅，尝试理解代码覆盖的概念及其重要性。据我所知，代码覆盖在高层次上是模糊测试器试图追踪/增加模糊测试器输入所能覆盖的目标应用程序代码的程度。其理念是，你的模糊测试器输入覆盖的代码越多，攻击面越大，你的测试就越全面，还有其他一些我目前还不理解的高级概念。

我一直在提升我的pwn技能，但会短暂休息一下，写点C代码，看看@gamozolabs的直播。@gamozolabs在其中一个直播中详细讲解了代码覆盖的重要性，我怎么也找不到那个片段，但我记得大概内容，于是设置了一些测试用例，专门用于我的测试，以演示为什么“愚蠢的”模糊测试器相比于代码覆盖引导的模糊测试器是如此劣势。准备好一些（可能不正确的????）八年级概率理论吧。在这篇博客文章结束时，我们至少应该能够大致理解1990年最先进的模糊测试器是如何工作的。

##

```
二

我们的模糊测试器
```

我们有这个美丽、无错误、完美编写的单线程jpeg变异模糊测试器，我们已经从之前的博客文章中将其移植到C语言，并为我们的实验目的进行了一些调整。

```
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>
#include <sys/wait.h>
#include <unistd.h>
#include <fcntl.h>

int crashes = 0;

struct ORIGINAL_FILE {
    char * data;
    size_t length;
};

struct ORIGINAL_FILE get_data(char* fuzz_target) {

    FILE *fileptr;
    char *clone_data;
    long filelen;

    // open file in binary read mode
    // jump to end of file, get length
    // reset pointer to beginning of file
    fileptr = fopen(fuzz_target, "rb");
    if (fileptr == NULL) {
        printf("[!] Unable to open fuzz target, exiting...\n");
        exit(1);
    }
    fseek(fileptr, 0, SEEK_END);
    filelen = ftell(fileptr);
    rewind(fileptr);

    // cast malloc as char ptr
    // ptr offset * sizeof char = data in .jpeg
    clone_data = (char *)malloc(filelen * sizeof(char));

    // get length for struct returned
    size_t length = filelen * sizeof(char);

    // read in the data
    fread(clone_data, filelen, 1, fileptr);
    fclose(fileptr);

    struct ORIGINAL_FILE original_file;
    original_file.data = clone_data;
    original_file.length = length;

    return original_file;
}

void create_new(struct ORIGINAL_FILE original_file, size_t mutations) {

    //
    //----------------MUTATE THE BITS-------------------------
    //
    int* picked_indexes = (int*)malloc(sizeof(int)*mutations);
    for (int i = 0; i < (int)mutations; i++) {
        picked_indexes[i] = rand() % original_file.length;
    }

    char * mutated_data = (char*)malloc(original_file.length);
    memcpy(mutated_data, original_file.data, original_file.length);

    for (int i = 0; i < (int)mutations; i++) {
        char current = mutated_data[picked_indexes[i]];

        // figure out what bit to flip in this 'decimal' byte
        int rand_byte = rand() % 256;

        mutated_data[picked_indexes[i]] = (char)rand_byte;
    }

    //
    //---------WRITING THE MUTATED BITS TO NEW FILE-----------
    //
    FILE *fileptr;
    fileptr = fopen("mutated.jpeg", "wb");
    if (fileptr == NULL) {
        printf("[!] Unable to open mutated.jpeg, exiting...\n");
        exit(1);
    }
    // buffer to be written from,
    // size in bytes of elements,
    // how many elements,
    // where to stream the output to :)
    fwrite(mutated_data, 1, original_file.length, fileptr);
    fclose(fileptr);
    free(mutated_data);
    free(picked_indexes);
}

void exif(int iteration) {

    //fileptr = popen("exiv2 pr -v mutated.jpeg >/dev/null 2>&1", "r");
    char* file = "vuln";
    char* argv[3];
    argv[0] = "vuln";
    argv[1] = "mutated.jpeg";
    argv[2] = NULL;
    pid_t child_pid;
    int child_status;

    child_pid = fork();
    if (child_pid == 0) {

        // this means we're the child process
        int fd = open("/dev/null", O_WRONLY);

        // dup both stdout and stderr and send them to /dev/null
        dup2(fd, 1);
        dup2(fd, 2);
        close(fd);

        execvp(file, argv);
        // shouldn't return, if it does, we have an error with the command
        printf("[!] Unknown command for execvp, exiting...\n");
        exit(1);
    }
    else {
        // this is run by the parent process
        do {
            pid_t tpid = waitpid(child_pid, &child_status, WUNTRACED |
             WCONTINUED);
            if (tpid == -1) {
                printf("[!] Waitpid failed!\n");
                perror("waitpid");
            }
            if (WIFEXITED(child_status)) {
                //printf("WIFEXITED: Exit Status: %d\n", WEXITSTATUS(child_status));
            } else if (WIFSIGNALED(child_status)) {
                crashes++;
                int exit_status = WTERMSIG(child_status);
                printf("\r[>] Crashes: %d", crashes);
                fflush(stdout);
                char command[50];
                sprintf(command, "cp mutated.jpeg ccrashes/%d.%d", iteration,
                exit_status);
                system(command);
            } else if (WIFSTOPPED(child_status)) {
                printf("WIFSTOPPED: Exit Status: %d\n", WSTOPSIG(child_status));
            } else if (WIFCONTINUED(child_status)) {
                printf("WIFCONTINUED: Exit Status: Continued.\n");
            }
        } while (!WIFEXITED(child_status) && !WIFSIGNALED(child_status));
    }
}

int main(int argc, char** argv) {

    if (argc < 3) {
        printf("Usage: ./cfuzz <valid jpeg> <num of fuzz iterations>\n");
        printf("Usage: ./cfuzz Canon_40D.jpg 10000\n");
        exit(1);
    }

    // get our random seed
    srand((unsigned)time(NULL));

    char* fuzz_target = argv[1];
    struct ORIGINAL_FILE original_file = get_data(fuzz_target);
    printf("[>] Size of file: %ld bytes.\n", original_file.length);
    size_t mutations = (original_file.length - 4) * .02;
    printf("[>] Flipping up to %ld bytes.\n", mutations);

    int iterations = atoi(argv[2]);
    printf("[>] Fuzzing for %d iterations...\n", iterations);
    for (int i = 0; i < iterations; i++) {
        create_new(original_file, mutations);
        exif(i);
    }

    printf("\n[>] Fuzzing completed, exiting...\n");
    return 0;
}
```

这里不会花太多时间讨论模糊测试器的功能（有什么功能？），但关于模糊测试器代码的一些重要事项：

◆它以文件作为输入，并将文件中的字节复制到一个缓冲区中。

◆它计算缓冲区的字节长度，然后通过随机覆盖任意字节来变异2%的字节。

◆负责变异的函数`create_new`不跟踪哪些字节索引被变异，所以理论上，同一个索引可能会被多次选择进行变异，因此实际上，模糊测试器最多变异2%的字节。

我们这里只使用了一种变异方法以保持事情的简单性，在此过程中，我实际上学到了一些之前没有清晰考虑过的非常有用的东西。在之前的一篇文章中，我曾尴尬地大声思考并写到，随机比特翻转与随机字节覆盖（翻转？）有多大不同。事实证明，它们非常不同。让我们花点时间看看。

假设我们正在变异一个名为`bytes`的字节数组。我们正在变异索引5。未变异的原始文件中，`bytes[5] == \x41`（十进制为65）。如果我们只进行比特翻转，我们在变异这个字节的程度上非常有限。65的二进制表示是`01000001`。让我们看看任意翻转一位会有多大变化：

◆翻转第一位：11000001 = 193，

◆翻转第二位：00000001 = 1，

◆翻转第三位：01100001 = 97，

◆翻转第四位：01010001 = 81，

◆翻转第五位：01001001 = 73，

◆翻转第六位：01000101 = 69，

◆翻转第七位：01000011 = 67，

◆翻转第八位：010000001 = 64。

如你所见，我们被限制在一个非常有限的可能性范围内。

因此，对于这个程序，我选择用一种方法代替这种变异方法，即直接替换一个随机字节，而不是字节内的比特。

##

```
三

易受攻击的程序
```

我写了一个简单的卡通化程序来演示“愚蠢的”模糊测试器发现漏洞的难度。想象一个目标应用程序在二进制的反汇编视图中有几个决策树。该应用程序对输入执行2-3次检查，以查看其是否满足某些条件，然后再将输入传递给某种易受攻击的函数。我的意思是这样的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GWQXsxtiaCpMQvg1R6csm5eR02icXMicaeh1EQTK0B7XthU2XKDXl9ldw4ib0bE9z2HR61ZdC0BibqpEw/640?wx_fmt=png&from=appmsg)

我们的程序正是这样做的，它获取输入文件的字节，并检查文件长度的1/3、1/2和2/3处的字节，看看这些位置的字节是否与一些硬编码的值（任意的）匹配。如果所有检查都通过，应用程序会将字节缓冲区复制到一个小缓冲区中，导致段错误以模拟一个易受攻击的函数。以下是我们的程序：

```
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

struct ORIGINAL_FILE {
    char * data;
    size_t length;
};

struct ORIGINAL_FILE get_bytes(char* fileName) {

    FILE *filePtr;
    char* buffer;
    long fileLen;

    filePtr = fopen(fileName, "rb");
    if (!filePtr) {
        printf("[>] Unable to open %s\n", fileName);
        exit(-1);
    }

    if (fseek(filePtr, 0, SEEK_END)) {
        printf("[>] fseek() failed, wtf?\n");
        exit(-1);
    }

    fileLen = ftell(filePtr);
    if (fileLen == -1) {
        printf("[>] ftell() failed, wtf?\n");
        exit(-1);
    }

    errno = 0;
    rewind(filePtr);
    if (errno) {
        printf("[>] rewind() failed, wtf?\n");
        exit(-1);
    }

    long trueSize = fileLen * sizeof(char);
    printf("[>] %s is %ld bytes.\n", fileName, trueSize);
    buffer = (char *)malloc(fileLen * sizeof(char));
    fread(buffer, fileLen, 1, filePtr);
    fclose(filePtr);

    struct ORIGINAL_FILE original_file;
  ...
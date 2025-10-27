---
title: 野蛮fuzz：提升性能
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579145&idx=1&sn=9134327916f678cfe7e2bc3371cedeaf&chksm=b18dc04386fa49557abc8c7e6ce3410dd4042ed88635c48961fda72b7fa4425698e56bb86ff6&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-10-27
fetch_date: 2025-10-06T18:50:05.965303
---

# 野蛮fuzz：提升性能

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Ewib3icbyIPTfKJqGHsyhAVdjXzSTP0wTmiauIpm6zJC3iatH4qCqkjTLLdZzFicGo211BA2SFYQzichWQ/0?wx_fmt=jpeg)

# 野蛮fuzz：提升性能

pureGavin

看雪学苑

##

```
一

简介
```

在这一期的“野蛮fuzz”中，我们将专注于提升我们之前模糊测试器的性能。这意味着不会有任何大规模的变更，我们只是希望在之前的基础上进行改进。因此，在这篇博客文章结束时，我们仍然会得到一个非常基础的变异模糊测试器（希望它能更快！），并且希望在不同的目标上发现更多的漏洞。我们不会在这篇文章中涉及多线程或多进程的内容，这些将留待后续的模糊测试文章中讨论。

我需要在这里添加一个免责声明，我并不是一个专业的开发人员，离这个目标还很远。目前我在编程方面的经验还不足以像一个更有经验的程序员那样识别出提升性能的机会。我将使用我粗糙的技能和有限的编程知识来改进我们之前的模糊测试器，仅此而已。生成的代码不会很漂亮，也不会很完美，但它会比我们在上一篇文章中的代码更好。还需要提到的是，所有的测试都是在一台配有1个CPU和1个核心的x86 Kali虚拟机上使用 VMWare Workstation 进行的。

我们也需要在本文的上下文中定义“更好”的含义。我在这里所说的“更好”是指我们能够更快地完成n次模糊测试迭代，仅此而已。我们会在以后的时间里重新编写模糊测试器，使用一种酷炫的语言，选择一个强化的目标，并采用更先进的模糊测试技术。

> 显然，如果你没有读过上一篇文章，你会感到迷茫！

```
二

分析我们的模糊测试器
```

我们上一个模糊测试器相当简单，但有效！我们在目标中发现了一些漏洞。但我们知道，当我们交作业时，留下一些优化的空间。让我们再来看看上一篇文章中的模糊测试器（为了测试目的做了一些小改动）：

```
#!/usr/bin/env python3
import sys
import random
from pexpect import run
from pipes import quote

# read bytes from our valid JPEG and return them in a mutable bytearray
def get_bytes(filename):

    f = open(filename, "rb").read()

    return bytearray(f)

def bit_flip(data):

    num_of_flips = int((len(data) - 4) * .01)

    indexes = range(4, (len(data) - 4))

    chosen_indexes = []

    # iterate selecting indexes until we've hit our num_of_flips number
    counter = 0
    while counter < num_of_flips:
        chosen_indexes.append(random.choice(indexes))
        counter += 1

    for x in chosen_indexes:
        current = data[x]
        current = (bin(current).replace("0b",""))
        current = "0" * (8 - len(current)) + current

        indexes = range(0,8)

        picked_index = random.choice(indexes)

        new_number = []

        # our new_number list now has all the digits, example: ['1', '0', '1', '0', '1', '0', '1', '0']
        for i in current:
            new_number.append(i)

        # if the number at our randomly selected index is a 1, make it a 0, and vice versa
        if new_number[picked_index] == "1":
            new_number[picked_index] = "0"
        else:
            new_number[picked_index] = "1"

        # create our new binary string of our bit-flipped number
        current = ''
        for i in new_number:
            current += i

        # convert that string to an integer
        current = int(current,2)

        # change the number in our byte array to our new number we just constructed
        data[x] = current

    return data

def magic(data):

    magic_vals = [
    (1, 255),
    (1, 255),
    (1, 127),
    (1, 0),
    (2, 255),
    (2, 0),
    (4, 255),
    (4, 0),
    (4, 128),
    (4, 64),
    (4, 127)
    ]

    picked_magic = random.choice(magic_vals)

    length = len(data) - 8
    index = range(0, length)
    picked_index = random.choice(index)

    # here we are hardcoding all the byte overwrites for all of the tuples that begin (1, )
    if picked_magic[0] == 1:
        if picked_magic[1] == 255:			# 0xFF
            data[picked_index] = 255
        elif picked_magic[1] == 127:		# 0x7F
            data[picked_index] = 127
        elif picked_magic[1] == 0:			# 0x00
            data[picked_index] = 0

    # here we are hardcoding all the byte overwrites for all of the tuples that begin (2, )
    elif picked_magic[0] == 2:
        if picked_magic[1] == 255:			# 0xFFFF
            data[picked_index] = 255
            data[picked_index + 1] = 255
        elif picked_magic[1] == 0:			# 0x0000
            data[picked_index] = 0
            data[picked_index + 1] = 0

    # here we are hardcoding all of the byte overwrites for all of the tuples that being (4, )
    elif picked_magic[0] == 4:
        if picked_magic[1] == 255:			# 0xFFFFFFFF
            data[picked_index] = 255
            data[picked_index + 1] = 255
            data[picked_index + 2] = 255
            data[picked_index + 3] = 255
        elif picked_magic[1] == 0:			# 0x00000000
            data[picked_index] = 0
            data[picked_index + 1] = 0
            data[picked_index + 2] = 0
            data[picked_index + 3] = 0
        elif picked_magic[1] == 128:		# 0x80000000
            data[picked_index] = 128
            data[picked_index + 1] = 0
            data[picked_index + 2] = 0
            data[picked_index + 3] = 0
        elif picked_magic[1] == 64:			# 0x40000000
            data[picked_index] = 64
            data[picked_index + 1] = 0
            data[picked_index + 2] = 0
            data[picked_index + 3] = 0
        elif picked_magic[1] == 127:		# 0x7FFFFFFF
            data[picked_index] = 127
            data[picked_index + 1] = 255
            data[picked_index + 2] = 255
            data[picked_index + 3] = 255

    return data

# create new jpg with mutated data
def create_new(data):

    f = open("mutated.jpg", "wb+")
    f.write(data)
    f.close()

def exif(counter,data):

    command = "exif mutated.jpg -verbose"

    out, returncode = run("sh -c " + quote(command), withexitstatus=1)

    if b"Segmentation" in out:
        f = open("crashes2/crash.{}.jpg".format(str(counter)), "ab+")
        f.write(data)
        print("Segfault!")

    #if counter % 100 == 0:
    #	print(counter, end="\r")

if len(sys.argv) < 2:
    print("Usage: JPEGfuzz.py <valid_jpg>")

else:
    filename = sys.argv[1]
    counter = 0
    while counter < 1000:
        data = get_bytes(filename)
        functions = [0, 1]
        picked_function = random.choice(functions)
        picked_function = 1
        if picked_function == 0:
            mutated = magic(data)
            create_new(mutated)
            exif(counter,mutated)
        else:
            mutated = bit_flip(data)
            create_new(mutated)
            exif(counter,mutated)

        counter += 1
```

你可能注意到了一些变化。我们做了以下改动：

◆注释掉了每100次迭代打印一次计数器的语句。

◆添加了打印语句，用于通知我们是否发生了段错误（Segfault）。

◆硬编码了1000次迭代。

◆临时添加了这行代码：`picked_function = 1`，以便在测试中消除任何随机性，我们只使用一种变异方法（`bit_flip()`）。

让我们使用一些性能分析工具运行这个版本的模糊测试器，这样我们可以真正分析程序执行过程中在哪些地方花费了最多的时间。

我们可以利用Python的cProfile模块，看看在1000次模糊测试迭代中，我们在哪些地方花费了时间。如果你还记得，这个程序需要一个有效的JPEG文件路径作为参数，所以完整的命令行语法将是：`python3 -m cProfile -s cumtime JPEGfuzzer.py ~/jpegs/Canon_40D.jpg`。

还需要注意的是，添加这个cProfile性能分析工具可能会降低性能。我在没有使用它的情况下进行了测试，对于我们在本文中使用的迭代次数，它似乎没有显著的影响。

运行这个程序后，我们可以看到程序的输出，并了解到执行过程中花费时间最多的地方。

```
2476093 function calls (2474812 primitive calls) in 122.084 seconds

   Ordered by: cumulative time

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     33/1    0.000    0.000  122.084  122.084 {built-in method builtins.exec}
        1    0.108    0.108  122.084  122.084 blog.py:3(<module>)
     1000    0.090    0.000  118.622    0.119 blog.py:140(exif)
     1000    0.080    0.000  118.452    0.118 run.py:7(run)
     5432  103.761    0.019  103.761    0.019 {built-in method time.sleep}
     1000    0.028    0.000  100.923    0.101 pty_spawn.py:316(close)
     1000    0.025    0.000  100.816    0.101 ptyprocess.py:387(close)
     1000    0.061    0.000    9.949    0.010 pty_spawn.py:36(__init__)
     1000    0.074    0.000    9.764    0.010 pty_spawn.py:239(_spawn)
     1000    0.041    0.000    8.682    0.009 pty_spawn.py:312(_spawnpty)
     1000    0.266    0.000    8.641    0.009 ptyprocess.py:178(spawn)
     1000    0.011    0.000    7.491    0.007 spawnbase.py:240(expect)
     1000    0.036    0.000    7.479    0.007 spawnbase.py:343(expect_list)
     1000    0.128    0.000    7.409    0.007 expect.py:91(expect_loop)
     6432    6.473    0.001    6.473    0.001 {built-in method posix.read}
     5432    0.089    0.000    3.818    0.001 pty_spawn.py:415(read_nonblocking)
     7348    0.029    0.000    3.162    0.000 utils.py:130(select_ignore_interrupts)
     7348    3.127    0.000    3.127    0.000 {built-in method select.select}
     1000    0.790    0.001    1.777    0.002 blog.py:15(bit_flip)
     1000    0.015    0.000    1.311    0.001 blog.py:134(create_new)
     1000    0.100    0.000    1.101    0.001 pty.py:79(fork)
     1000    1.000    0.001    1.000    0.001...
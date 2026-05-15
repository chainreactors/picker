---
title: 【免杀】使用ollvm混淆程序
url: https://mp.weixin.qq.com/s/Pz_Y14DRzZc_MCUpi_eT4g
source: Doonsec's feed
date: 2026-05-14
fetch_date: 2026-05-15T05:47:58.693430
---

# 【免杀】使用ollvm混淆程序

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/bz5OjA3Rpu8TZOxQ4lfjKiaWdibxkFtWFIVqqEpAnzCGoLnEdQIibDFziaHJKnMAtjVLDcl6XSkfFjoSw0GdoH7SozQbMibsVnd7VVG8Wf0cykW0/0?wx_fmt=jpeg)

# 【免杀】使用ollvm混淆程序

原创

joe1sn
joe1sn

不止Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

如何有源代码、快速的、不使用壳的情况下混淆程序，最好的就是在编译的时候添加。这里以最简单的猜大小的例子举例。

源代码是

```
#include <iostream>
#include <random>
#include <limits>

int main()
{
    std::random_devicerd;
    std::mt19937gen(rd());
    std::uniform_int_distribution<int>dist(1, 100);

    while (true) {
        int target=dist(gen);
        int guess=0;
        int attempts=0;

        std::cout<<"\n========== Guess the Number ==========\n";
        std::cout<<"A number between 1 and 100 has been generated.\n";
        std::cout<<"Enter 0 to quit.\n\n";

        while (true) {
            std::cout<<"Guess #"<<attempts+1<<": ";

            if (!(std::cin>>guess)) {
                std::cin.clear();
                std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
                std::cout<<"Please enter a valid number!\n";
                continue;
            }

            if (guess==0) {
                std::cout<<"Exited the game.\n";
                return0;
            }

            attempts++;

            if (guess<target) {
                std::cout<<"Too low, try again!\n";
            }
            elseif (guess>target) {
                std::cout<<"Too high, try again!\n";
            }
            else {
                std::cout<<"\nCongratulations! The number was "<<target<<"!\n";
                std::cout<<"You got it in "<<attempts<<" attempt(s).\n";
                break;
            }
        }

        std::cout<<"\nPress 1 to play again, any other key to exit: ";
        int play_again;
        if (!(std::cin>>play_again) ||play_again!=1) {
            std::cout<<"Thanks for playing, goodbye!\n";
            break;
        }
    }

    return0;
}
```

1. 使用 Release+ O2 进行优化+无符号表

   ![image-20260514135013911](https://mmbiz.qpic.cn/sz_mmbiz_png/bz5OjA3RpuicShicgD7pNYY9ZuMbm8z8NicBHFTwZBib6uhiazwd4XdpP88eAyGDEzxsoRobALCM1VibL5rwMzUzCRliaXGfk5aldZWghReSOd2r7k/640?wx_fmt=png&from=appmsg)
2. 使用 ollvm(-mllvm -fla) + 有符号表

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/bz5OjA3Rpu9XpQNmAPUHxua7KuicDj4a16bTy5eHeCb6sBnZCA9KwM7AYdticLUBo4XciaGK0yjGg7oWcvvMjzQfgFaegKiatwmdRrUthxhqtyQ/640?wx_fmt=png&from=appmsg)

# 搭建 ollvm 编译环境

参考的是 [2]，使用的是windows平台，已有 VS2022 Cmake环境

https://github.com/heroims/obfuscator/tree/llvm-9.0.1

git 后得修改下 CMakelists.txt

![image-20260514161714845](https://mmbiz.qpic.cn/mmbiz_png/bz5OjA3Rpu8QKlL6MoXNAwIYmDyXZ2c7JJ8Negh4HxQ8Vmb5SI9D95BoAbQNvrwngMJUdQu4dPIh8hB3bNLMTzB6cYQubndmSKMFgQKIFys/640?wx_fmt=png&from=appmsg)

![image-20260514161958287](https://mmbiz.qpic.cn/sz_mmbiz_png/bz5OjA3RpuibgVAiaofuyz6J4lIWGdRrWQg8aIbAZrtJm0hiacdZAYoK5ABicHMmf7xiaIwQic9njzqFMnq8Giboib7ZYicAhogRKe5yPTIgGMJZZlz0/640?wx_fmt=png&from=appmsg)

![image-20260514162039870](https://mmbiz.qpic.cn/mmbiz_png/bz5OjA3RpuibTBdSlQgDbI8kShwzDM5DxHGTOOgLicnTcTvFIDicLicp4UBnSUyIUib3FXusEDTicprUzvrUIW0CxhElwpKiaVia6ibnpFsn0ssW6Cu8/640?wx_fmt=png&from=appmsg)

```
git clone -b llvm-9.0.1 https://github.com/heroims/obfuscator/
mkdir build
cd build
```

使用 MinGW

```
cmake -G "MinGW Makefiles" -DCMAKE_BUILD_TYPE=Release ../obfuscator
cmake --build ./ -j 24
```

使用 MSVC（不推荐）

```
cmake -G "Visual Studio 17 2022" -DCMAKE_BUILD_TYPE=Release ../obfuscator/
cmake --build ./ -j 24
```

![image-20260514162410654](https://mmbiz.qpic.cn/sz_mmbiz_png/bz5OjA3Rpuib83tiaW24ibFcaA5F0UmJxmvib00yCLghVxKThcQSAsUWkawuLJrgHuudspC4I7ichPB4FHPvmgzp31JEKcywWgkuicicIYNSHJLhKU/640?wx_fmt=png&from=appmsg)

![image-20260514163508696](https://mmbiz.qpic.cn/sz_mmbiz_png/bz5OjA3RpuichvvplgJbYJGNpa07Uj0jr23mjnKAKocvEw7jtuctJsjYsaPdQ6ZOR6ybbDxK2mibibHjRj7WfAicuQJM8eb5DDVoqAw2fYctC7o/640?wx_fmt=png&from=appmsg)

混淆一共有三种模式，添加之前都得加上`-mllvm`

* -fla：控制流平坦化
* -sub：无效指令
* -bcf：虚假控制流

测试一下

```
C:\Develop\C\ollvm\build\bin\clang++.exe .\main.cpp -mllvm -fla -o ollvm.exe
```

![image-20260514163731986](https://mmbiz.qpic.cn/mmbiz_png/bz5OjA3RpuicFRSKuEasoxjoBoJdf1gDvoJXITZwQC2ibyZ2vEiaxcteiaxYCoicFp3TRibQvCyTkKGtVe5vmcibicJzO70fkaQaSW5yjia7tVn33oj4/640?wx_fmt=png&from=appmsg)

现在尝试将其集成到cmake当中

配置cmake的编译器，选择产出的路径（build/bin），没有的话让vscode扫描一下就行了

![image-20260514200605677](https://mmbiz.qpic.cn/mmbiz_png/bz5OjA3RpuibKqaKtWZ8Xc1ibbt0lochTZOqZGymnoKCkHIeQ15eRtpHu5n3pp75ukZPvrGJrhCD5NRQWp04cXV0ibzvHx29J5yibTn1Sow50Go/640?wx_fmt=png&from=appmsg)

使用如下Cmake，`CMAKE_CXX_COMPILER` 写自己的路径

```
cmake_minimum_required(VERSION 3.11)
project(example LANGUAGES CXX)
set(CMAKE_CXX_COMPILER "C:\\Develop\\C\\ollvm\\build\\bin\\clang++.exe")
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
# OLLVM flags passed via target_compile_options below

set(PROJECT_INCLUDE

)
set(PROJECT_SOURCE
    src/main.cpp
)

add_executable(${PROJECT_NAME}${PROJECT_INCLUDE}${PROJECT_SOURCE})
target_compile_definitions(${PROJECT_NAME} PRIVATE UNICODE _UNICODE)
target_compile_options(${PROJECT_NAME} PRIVATE -mllvm -fla -U__cpp_aligned_new)
```

你需要配置一个具有环境变量的 `ninja` 或者 `make`

![image-20260514200705408](https://mmbiz.qpic.cn/mmbiz_png/bz5OjA3Rpu8WDCVk37tLuevwleFGUzDrobu0Gjc67dL1DrrEhRQXx4iasJttXvSZ8RwFZzsSceD6MsuWsR2icK6bzMBOx7vpyzlficVgba34EA/640?wx_fmt=png&from=appmsg)

使用Ninja的话

```
cmake -G Ninja ..
ninja
```

![image-20260514200824753](https://mmbiz.qpic.cn/sz_mmbiz_png/bz5OjA3RpuibTLjrvZb2TQWW3aKqZGLTujia4pKkkPKYkuoz3nrac5SX1m80XZMOm0AsliaGM6rZ3D6zdq1n9R6oCoXVwDJPWeLfrmvDNNgLz4/640?wx_fmt=png&from=appmsg)

![image-20260514200902014](https://mmbiz.qpic.cn/mmbiz_png/bz5OjA3RpuicLW09lqbiczuZ2Aqicx6NdHfLYDnVwn8JEgGJnfe2XszqBLj4uuiaDibcZB5yrJOYrpj4pgOMTtaRIBH0N5UTlrdnRHe9pAGLhOCg/640?wx_fmt=png&from=appmsg)

使用CMake的话类似

# 引用

[1] obfuscator https://github.com/obfuscator-llvm/obfuscator/

[2] Windows上编译ollvm9.0等高版本并使用  https://www.cnblogs.com/revercc/p/16318849.html

[3] heroims/obfuscator https://github.com/heroims/obfuscator/tree/llvm-9.0.1

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/A6k7mR4gGVQXdEyBlejzDticJwP5icCNlG5knMTY0mGNbRoE4uSzialjoyd5LG2Yibl4XvuApmrgAGp625a6qBBJPQ/0?wx_fmt=png)

不止Sec

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

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/A6k7mR4gGVQXdEyBlejzDticJwP5icCNlG5knMTY0mGNbRoE4uSzialjoyd5LG2Yibl4XvuApmrgAGp625a6qBBJPQ/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过
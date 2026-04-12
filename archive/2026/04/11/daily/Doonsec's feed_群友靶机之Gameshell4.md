---
title: 群友靶机之Gameshell4
url: https://mp.weixin.qq.com/s/lBDVlI0ZG0g4HLD1nxo8mA
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:44:15.357034
---

# 群友靶机之Gameshell4

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8avkpGSKmqfRuX0XNhl8b66ianphFEKc7kialvsskfmOlbwTiciahK6Wsniak9AfwzGXoMQN7FJnPeRo4YjoOhicpYWEyBgEZvuEDEkkehibZcxl9A/0?wx_fmt=jpeg)

# 群友靶机之Gameshell4

原创

MS02423
MS02423

MS02423

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

写一下 Sublarge佬的Gameshell4靶机的wp

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqd4fzN7z6zNS1xXxKfyd0ictOVGicL0hmic5EcbsUbMyUBMSllnB9IsRI2NSKowENQlUhx3WSLLmcjrbFMz7KPsn79jIXP3zAwtEY/640?wx_fmt=png&from=appmsg)

还是老思路

一.信息收集

1.探测IP

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdAwiaXov87lfToOzpS5e4bOh1jBUibEUXu1c5A3siaTRTpYjIpZHQibdUxYQn31Kk5J8u2tusp7iaYQdXHHn8gxkR3r0r4ubdfGZ50/640?wx_fmt=png&from=appmsg)

靶机IP是192.168.137.156

2.探测端口

```
nmap -p- -sV 192.168.137.156
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqddrTyXyReu43hwChXibzapmNwoPLIFPQsDQVqAI9pEAqsic9hicAaAVgxsmqLd7DvFtuaHIuaicB7LmB1gqx1gS7P2joVSdWVSnSU/640?wx_fmt=png&from=appmsg)

我们可以看到开放了22,79,80端口，这里我们可以去了解一个79端口的finger服务

```
79端口的finger服务是一个用于查询远程系统用户信息的早期网络协议。它允许用户获取其他联网主机上用户的公开信息，如用户名、登录状态、最近登录时间等。由于finger协议会暴露系统用户信息，存在安全隐患，现代操作系统和网络环境已普遍禁用或不再默认提供该服务
```

基本的命令如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdvXqthZuHQTqJ2f0MkmLHMDhJNFNaY1UTicJtVZofQsorrSeIMteLyep09BBKHBLZRcdA88LkMsuIXJla6icKo1X87dMVuwDOVA/640?wx_fmt=png&from=appmsg)

然后就是我们需要在80端口发现信息，然后去22端口登录即可

2.探测目录

```
gobuster dir -u http://192.168.137.156 -w /usr/share/wordlists/dirb/big.txt -x php,txt,bak,zip,sh,config
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqctZADb7gK7Wh2WM2dib2eCUtq5fOibxzzrVaxYSE6nff7mc4rFt7BfmDdiawoLKibKzrkzD2VaxUl0ia617QOaqpb4PRGN3UPmBx00/640?wx_fmt=png&from=appmsg)

我们扫描到一个sudoku目录，我们去访问试试看

```
http://192.168.137.156/sudoku
```

我们可以看到是一个登录页面，那么我们需要去寻找用户名和密码，或者是去爆破的。

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqfq4k6HW4lmFla7kNTScRSBGzl68vXrnT8dKQvqWNicEaL74NkMWUg2CW6QCY5AumPrhCrOugLIquO2XK6uzSFHuByqgCibupuj0/640?wx_fmt=png&from=appmsg)

二.访问IP

目前我们掌握的信息就是一个80端口，一个登录页面，和一个79端口，所以目前我们的思路只能在80端口下手了，我们去访问80端口看看

```
http://192.168.137.156/
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqfCC7Ql6cX7WibvcNNsq5J86efmATSG9Qibicib9Gs7ib1Elg2RF3IR7YeYnSFfDVWcPLnBNmR95lQ190EBzO3ElSHfO1CBqHk3UcoI/640?wx_fmt=png&from=appmsg)

我们可以看到是一个图形，而且是一直在转，既然目录没有信息，那么我们去源代码看看

```
view-source:http://192.168.137.156/
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdzXHWia6R6NjkOqawjUIs2RZ2picaKKtBiajuiccd3UwzIaMNIqjrFpNLxjDmzvr0MVcX4t6HO6BROEEKYWsrXDOFAzmSNt4uP6nw/640?wx_fmt=png&from=appmsg)

我们明显可以看到一个用户名是admin,密码是加密的，我们去解密

三.渗透测试

1.解密

```
admin:$2y$05$yKwD7W0PUqg9EGrSRQP2AegLrBvwLaUDlYEQ859O/ki01I54LnReS
```

我们使用john工具解密即可

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqev9YO1V18AEqm9fzSOiaqArsSBw6iaMS1TVFCrplmfoiaNHAmiasibGn7XjqgXFoanwEoJtZXDMIGQ7kviazNyIbMRtb4cHx9qNztnI/640?wx_fmt=png&from=appmsg)

```
echo 'admin:$2y$05$yKwD7W0PUqg9EGrSRQP2AegLrBvwLaUDlYEQ859O/ki01I54LnReS' > 11.txtjohn --wordlist=/usr/share/wordlists/rockyou.txt 11.txt --format=bcryptjohn --show 11.txt
```

解密出来

```
admin:babylove3
```

2.登录

既然我们解密出来了，那么我们去登录试试看，首先我用的是finger服务，如果没有什么用，我就去登录sudoku界面，因为这里我觉得是目前我们只有一个用户名和密码，那么我们应该是可以去登录的(应该可以说是用户名和密码复用吧![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/2_05.png))。

首先，我们去看看finger服务

```
finger admin@192.168.137.156
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqeMLLhicJc1JgfySlrqwq3mt4wVH4aGmgYNHcxI8EcFRosmz8dNHia3KGwkhPj74yYLxqZDAV69lTEAsHZHkDKicbmBIuqkZR0tYE/640?wx_fmt=png&from=appmsg)

通过返回shell和所在目录，我猜测是可以去登录ssh服务的，我们去登录试试看

```
Directory: /home/admin                  Shell: /bin/bash
```

3.ssh登录

```
ssh admin@192.168.137.156
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqe5XvTGqccbDrO5daxuSiaxPcpYk253OIicfbDYTlZGWDaibDN5QQiaE4Zfiaw615OzlwIxNlIVjtmEQib5u6tX39PpYkmu2Wpfa4VnI/640?wx_fmt=png&from=appmsg)

我们可以看到是登录成功的，但是admin用户是没有作用的，唯一的作用就是让我们知道还有2个用户，一个是sdk,一个是xcm.那么我们接下来的思路就是去登录这2个用户的。我们需要知道它们的密码的，但是直接去爆破应该是不行的，那么我们就需要去回到我们之前的那个sudoku目录了，我们去使用admin用户登录试试看

4.数独游戏

```
http://192.168.137.156/sudoku
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqeURnxD3R8dcp9TuZxuFvQa9WtEdLukMCsZkY4OWVbbiahFFP6Bhw2C31PpGVWKaU5046vXcVGPbAibiaMYbPewTeh70ibaCqlMlo8/640?wx_fmt=png&from=appmsg)

我们登录之后发现是一个数独游戏，那么我们就直接去借助ai即可，因为我们去手动输入的话，需要输入52次的太麻烦了，通过对ai的一顿挨打，最终写出来一个自动化的脚本，让ai去给咱们写即可

```
import timeimport sysimport subprocessimport pyautoguiimport osfrom typing import List

# 如果使用pyautogui，需要安装: pip install pyautogui# 注意: 在运行前确保数独游戏窗口是激活状态
def solve_sudoku(board: List[List[int]]) -> bool:    """使用回溯算法解决数独"""    for i in range(9):        for j in range(9):            if board[i][j] == 0:                for num in range(1, 10):                    if is_valid(board, i, j, num):                        board[i][j] = num                        if solve_sudoku(board):                            return True                        board[i][j] = 0                return False    return True

def is_valid(board: List[List[int]], row: int, col: int, num: int) -> bool:    """检查在指定位置放置数字是否有效"""    # 检查行    for j in range(9):        if board[row][j] == num:            return False
    # 检查列    for i in range(9):        if board[i][col] == num:            return False
    # 检查3x3宫    start_row, start_col = 3 * (row // 3), 3 * (col // 3)    for i in range(start_row, start_row + 3):        for j in range(start_col, start_col + 3):            if board[i][j] == num:                return False
    return True

def generate_moves(initial_board: List[List[int]], solved_board: List[List[int]]) -> List[str]:    """生成移动步骤"""    moves = []    for i in range(9):        for j in range(9):            if initial_board[i][j] == 0 and solved_board[i][j] != 0:                move = f"{i + 1}{j + 1}{solved_board[i][j]}"                moves.append(move)    return moves

def auto_type_moves(moves: List[str], delay: float = 0.5) -> None:    """使用pyautogui自动输入移动"""    print(f"准备自动输入 {len(moves)} 步...")    print("请在5秒内切换到数独游戏窗口...")    time.sleep(5)
    for i, move in enumerate(moves, 1):        print(f"步骤 {i}/{len(moves)}: 输入 {move}")
        # 输入移动        pyautogui.write(move)        time.sleep(delay)
        # 按Enter键        pyautogui.press('enter')        time.sleep(delay)
    print("自动输入完成!")

def main() -> None:    """主函数"""    print("数独自动化输入系统")    print("=" * 50)
    # 初始数独棋盘    initial_board = [        [5, 0, 0, 0, 0, 0, 0, 7, 4],        [6, 1, 0, 0, 0, 7, 0, 8, 0],        [0, 0, 8, 0, 0, 3, 9, 0, 0],        [0, 5, 2, 0, 1, 0, 0, 0, 0],        [0, 0, 0, 8, 6, 4, 0, 0, 0],        [0, 0, 0, 0, 5, 0, 3, 1, 0],        [0, 0, 1, 9, 0, 0, 4, 0, 0],        [0, 9, 0, 2, 0, 0, 0, 6, 7],        [3, 8, 0, 0, 0, 0, 0, 0, 2]    ]
    # 求解数独    board_to_solve = [row[:] for row in initial_board]
    print("正在求解数独...")    if solve_sudoku(board_to_solve):        print("求解完成!")
        # 生成移动步骤        moves = generate_moves(initial_board, board_to_solve)
        print(f"总共需要 {len(moves)} 步")        print("=" * 50)
        # 显示步骤        for i, move in enumerate(moves, 1):            row = int(move[0])            col = int(move[1])            value = int(move[2])            print(f"{i:3d}. {move} (第{row}行, 第{col}列, 填入{value})")
        # 询问是否自动输入        print("\n" + "=" * 50)        choice = input("是否使用自动键盘输入? (y/n): ").strip().lower()
        if choice == 'y':            try:                import pyautogui                auto_type_moves(moves)            except ImportError:                print("错误: 需要安装pyautogui库")                print("请运行: pip install pyautogui")                print("\n手动输入步骤:")                for move in moves:                    print(f"输入: {move}")        else:            print("\n手动输入步骤:")            for move in moves:                print(f"输入: {move}")    else:        print("数独无解!")

if __name__ == "__main__":    main()
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqeRiavt9GwwdCmuv2wic2zKibacREclw7vrcTvwB5ibsicHsbDeMQiaj67H2XclhxXWIQtLwhLtpFtEKKNyxmCodJs6XSB7iaYl4CibgDQ/640?wx_fmt=png&from=appmsg)

最后出来一个SUDOKUISMAGIC,猜测是密码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqcV8j2Q7rAtiagJ3fqXnAXG8bJCYAwvIMv0...
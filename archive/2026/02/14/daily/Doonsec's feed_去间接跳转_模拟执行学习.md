---
title: 去间接跳转/模拟执行学习
url: https://mp.weixin.qq.com/s/aDHkOsTZ7Yc3FuOs7MiGqA
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:17:39.390331
---

# 去间接跳转/模拟执行学习

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K3vjbSb3EnzjzswumR5VYddoP3gQg56tI6RfNSt9ln0Dy0z7daeIicVATBSKqRRdeWWXE7O64ricCoPfbF4POouEo4Te5pgw8LQQ/0?wx_fmt=jpeg)

# 去间接跳转/模拟执行学习

zzzhangyu
zzzhangyu

看雪学苑

![]()

在小说阅读器中沉浸阅读

间接跳转这个高级混淆，接触了unicorn，unidbg这种模拟执行脚本后，发现这种特别适合对抗反编译器无法分辨的一些混淆，本文记录学习过程以及以京麒2024的drillbeam为样本尝试去去除间接跳转。

# 样本

```
unsigned char dizhi[] = { 0x1,0x2,0x3,0x4,0x5 };
void rc4_crypt(unsignedchar* Data, unsignedlong Len_D, unsignedchar* key, unsignedlong Len_k) //加解密{
unsignedchar s[256];
rc4_init(s, key, Len_k);
	_asm {
		lea eax, label1
		add eax,8
		sub eax,7
		push ebx
		mov ebx,OFFSET dizhi
		movzx ecx,byte ptr [ebx+2]
		pop ebx
		add eax, ecx
		jmp eax
	label1:
		_emit 0x90
		_emit 0x90
		_emit 0x90
		_emit 0x90

	}
```

如上的样本就是经典的间接跳转混淆，这种jmp eax，可以让反编译工具无法计算跳转的地址，导致反编译出错，这种混淆手段在vmp中也有体现，我们分别看看这个在ida和bn的效果。

ida：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K2NzQIVVj7bxv5yu5ObKfjN85kIX8qxuo84iadyUunDUNicViatqvxUBRgaI4zYVTRmofMcDy795UStHL3VPPns8KicSBgl5GaricVQ/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K07wCbeE8wxysIxfWiaaHByiaTHJRDsicA7dCOsicicMLOCLo0iaaX4mjJCia0t5rUI8u1VzX01icYRjegIMdVeE7TBc7F6Q9uXpABISVk/640?wx_fmt=other&from=appmsg)![]()

直接导致cfg丢失

bn:

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K1TdYnKFuVI4gbPc8DbKpSEWeqXK3dTkBliaSFCBre43K2pxx6JuqRwicsskqgFsbMibkKiciaXR3ib3tDaiczkWbscOqfBuu5lLmjRLM/640?wx_fmt=other&from=appmsg)![]()

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K05F73iboAw7YNX8D44bU95r0FmkaEXIm2eunKNJmuDAdOSib5rPLv0d9XDLicuticlYS3ciaG7PJHAcV3eRdnTEqTPghho0ticGIVVc/640?wx_fmt=other&from=appmsg)![]()

bn虽然能分析个大概，不过好像仍然有问题，这里粗暴的把查表的操作分析成了switch

不过有办法

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K3gIKZFQ2AbnRRe231ROOsd2vjDEqxrXGyEXm8Oq2iaF8h2ssGgPyH7W9y4icFyArCr154gR3ibwNh7sHibFOicAsXiaDraa6Gytl430/640?wx_fmt=other&from=appmsg)![]()

把data段改成只读

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K0VgZrYicWQQjgqmvH0x7IGuRiaic226DIycHsgeoQS9U2oxgIbVu93yib26PHXqf3cibC0RxLicToL2M480mpnaZicEniaaLZ23FU3w3Y/640?wx_fmt=other&from=appmsg)![]()

就可以正常分析了，因为计算地址存储在了data段（比如我这里的查表），反编译器不会去解析data段的数据，因为data段默认可写，导致被引用都的值被看作的是变量而非常量，阻止了常量传播，设置为可读的话，**bn会去把data段看成常量**，这也的话动态分析就可能解析出跳转的地址，但是这种方法并不高枕无忧，还是会存在问题。

### 解决手段

对于一般的ctf题的话，可能就只会存在一两种间接跳转的计算方式，这个时候我们就可以手动计算出然后写脚本简单去除就行，但是我们把情况放极端一点，如果一个程序充斥着几千种不重样的间接跳转，或者说ollvm里面还嵌套了间接跳转的话，挨个计算然后去除岂不是效率低。

回到手动计算，总之就是计算，有没有自动化工具计算然后识别，然后去除，这不就满足了我们手动计算->ida脚本去除的完整过程了吗。

这种一般就是模拟执行的过程，**模拟执行的框架一般有unicorn unidbg qiling angr**等等，我写unidbg要稍微多一点：

* unicorn可以看成裸的CPU，只给了CPU+内存+hook，不给os.....
* Qiling有系统调用API，可以做到迷你OS
* unidbg对于模拟安卓的so很友好，因为补齐了linker，JNI等等
* angr就是符号执行，路径探索，约束求解等等

这几种可以说是都在unicorn基础上成立的，为了更加理解这种去除思路，故用unicorn写一下，而且unicorn更适合跑指令。

### unicorn基本使用

### 我们先模拟执行一下这两条指令体会一下

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K12FKc4lrqoHYRfJrRA8tHoYteVNGNkWp9RQL5qth3ZxyCfPtPKtdV2dg1Zprz2cmia94FMYXiagLRe1NxFS9X7DE5vuWVibFmGX4/640?wx_fmt=other&from=appmsg)![]()

```
from unicorn import *
from unicorn.x86_const import *
#导入ARM平台寄存器常量和核心API

x86code=b'\x83\xC0\x08\x83\xE8\x07'

def hook_code(uc,address,size,user_data):
    print("Tracing instruction at 0x%x, instruction size = 0x%x" %(address, size))
try:
    mu=Uc(UC_ARCH_X86,UC_MODE_32)
    ADDRESS=0x10000
    mu.mem_map(ADDRESS,0x1000) #映射内存
    mu.mem_write(ADDRESS,x86code)#指令载入内存
    mu.reg_write(UC_X86_REG_EAX,0x3)

    mu.hook_add(UC_HOOK_CODE,hook_code,begin=ADDRESS,end=ADDRESS)

    mu.emu_start(ADDRESS,ADDRESS+len(x86code))

    rax=mu.reg_read(UC_X86_REG_EAX)
    print("rax =0x%x" % rax)
except UcError as e:
    print("ERROR %s" %e)

#Tracing instruction at 0x10000, instruction size = 0x3
#rax =0x4
```

可以很好的模拟出结果

可是unicorn是纯裸的CPU，意味着我们如果暴力的把整个exe直接载入CPU的内存里，一般是运行不起来的，还需要对一些系统函数进行重定位的操作。

## 最小化demo模拟去除

我们先假设只有一个间接跳转，先试着模拟一下

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K2LMSsm4A8mT3kFfTQkZicTSR0rXQrpvSaJ5Oqy7HeqRic0mVjMWnOR4AE1mkaouyib7UOOlqTa0AribhzVKRAibROd2jvZGY6aiaHN4/640?wx_fmt=other&from=appmsg)![]()

对于这种只有一个的话，我们的模拟手段就很简单的，因为我们已经找到了间接跳转的位置，所以自然可以找到需要模拟开始的地址以及结束地址，但是，这一路也不能直接裸调用，因为可以看到这里的查表操作是涉及到了读取数据段的东西了，我选择的是直接载入整个exe，然后单个开机模拟执行一段即可。

### 1.映射并解析整个PE

模拟PE的话，跟我在模拟ELF是不一样的，ELF我模拟的时候，基地址设置0，然后模拟区间和ida看到的偏移一样即可，但是PE文件不一样，因为PE的RAW和RVA是按照节表换算的。

```
pe = pefile.PE(PATH)
mu = Uc(UC_ARCH_X86, UC_MODE_32)

image_base = pe.OPTIONAL_HEADER.ImageBase
image_size= align_up(pe.OPTIONAL_HEADER.SizeOfImage)
mu.mem_map(image_base, image_size)

for s in pe.sections:
    va = image_base + s.VirtualAddress
    raw= s.get_data()
    size= align_up(max(s.Misc_VirtualSize, s.SizeOfRawData))
    mu.mem_write(va, raw + b"\x00" * (size - len(raw)))
```

### 2.映射栈

```
stack_bae=0x30000000
stack_size = 0x100000
mu.mem_map(stack_bae, stack_size)
mu.reg_write(UC_X86_REG_EBP, stack_bae + stack_size)
mu.reg_write(UC_X86_REG_ESP, stack_bae + stack_size - 0x4)
```

这里是把栈映射进去，把这个映射进去也是模拟栈帧创建，局部变量等等，这里减少4是为了防止栈崩掉。

### 3.安装hook

```
mu.hook_add(UC_HOOK_CODE, hook_code)
def hook_code(uc,address,size,user_data):
    print("Tracing instruction at 0x%x, instruction size = 0x%x eax=0x%x" %(address, size,mu.reg_read(UC_X86_REG_EAX)))
```

方便我们看到是哪条指令崩掉了，快速查找或者看值。

### 4.开机

```
begin = image_base + 0x11CAF
end   = image_base + 0x11CC8
print(mu.mem_read(begin, 8).hex())
mu.emu_start(begin, end)
eax=mu.reg_read(UC_X86_REG_EAX)
print("eax=0x%x" %eax)
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K1HOBviaf9K73jGr1Kl7ic4DNqzoNxV3J1OR8uJQSGk1jLGHtI3MdFgam1t6mlHu8VmXehPWdibI37mAgomWh2OFwcuudh2Hlr8so/640?wx_fmt=other&from=appmsg)![]()

这样可以看到已经完成了模拟

### 5.patch

现在我们可以加一点东西了，首先，需要知道何时去patch，这里我们可以用到反汇编引擎，去识别到jmp eax，然后直接改成jmp xxxx

```
machine=mu.mem_read(address,size)
code=md.disasm(machine,address)
for ins in code:
    if ins.mnemonic =="jmp":
        if ins.op_str=="eax":
            print(f"{ins.mnemonic}{ins.op_str}")
            print("eax" ,mu.reg_read(UC_X86_REG_EAX))

            right_m=mu.reg_read(UC_X86_REG_EAX)
            right_rell=right_m-address-5
            new=b"\xE9"+right_rell.to_bytes(4,"little")
            n=md.disasm(new,address)
            for nn in n:
                print("plcae-> "f"{nn.mnemonic}{nn.op_str}")

# jmp eax
# eax 4267214
# plcae-> jmp 0x411cce
```

这里涉及到了keystone和capstone，感觉只要是模拟执行都绕不过这两个东西。

上面就是简单的修改，不过这种修改有个bug感觉，就是修改后的指令大小有一点怕覆盖下面如果有用的指令（当然这里不成立，因为下面四个字节都没用）

这里修好了，那如何去patch回文件呢

这里可以选择直接把unicorn的内存直接修改后复制到新文件

我们选择去把unicorn内存修改然后试着覆盖回程序

但是为了防止覆盖后面的指令，所以我们先设置一个可写区域

0x11CAF-0x11CC8其实都是可以随便修改的（根据间接跳转而不同）

#### 总脚本

```
from unicorn import *
from unicorn.x86_const import *
import pefile, struct
from capstone import *
from keystone import *
def align_up(x, a=0x1000): return (x + a - 1) & ~(a - 1)

md = Cs(CS_ARCH_X86, CS_MODE_32)
ks = Ks(KS_ARCH_X86, KS_MODE_32)

PATH = r"D:\Android\unicorn-pandaos\sample\132.exe"

pe = pefile.PE(PATH)
mu = Uc(UC_ARCH_X86, UC_MODE_32)

image_base = pe.OPTIONAL_HEADER.ImageBase
image_size = align_up(pe.OPTIONAL_HEADER.SizeOfImage)

fix_ins=dict()
write_size=19
def patch(patch_byte):
    for address,dest in fix_ins.items():
        print("address->dest",hex(address),"->",hex(dest))
        start=address-write_size

        right_rell=dest-start-5
        new=b"\xE9"+right_rell.to_bytes(4,"little")
        n=md.disasm(new,start)
        for nn in n:
            print("plcae-> "f"{nn.mnemonic} {nn.op_str}")

        mu.mem_write(start,new)
        mu.mem_write(start+len(new),b"\x90"*(write_size))   #patch
        #print(mu.mem_read(start,30))

        src=bytearray(open(PATH,"rb").read())
        for s in pe.sections:
            raw_size=s.SizeOfRawData
            if raw_size==0:
                continue
            sec=image_base+s.VirtualAddress
            sec_off=s.PointerToRawData
            buf=mu.mem_read(sec,raw_size)
            src[sec_off:sec_off+raw_size]=buf

        with open(patch_byte,"wb") as f:
            f.write(src)
        print("dump")

def hook_memory(uc,access,address,size,value,userdata):
    pc=uc.reg_read(UC_X86_REG_EIP)
    print("memory error :pc %x address: %x size %x" %(pc,address,size))

def...
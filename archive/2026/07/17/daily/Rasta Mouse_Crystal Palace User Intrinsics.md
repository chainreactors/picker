---
title: Crystal Palace User Intrinsics
url: https://rastamouse.me/crystal-palace-user-intrinsics/
source: Rasta Mouse
date: 2026-07-17
fetch_date: 2026-07-18T04:46:41.526653
---

# Crystal Palace User Intrinsics

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

17 Jul 2026

3 min read

# Crystal Palace User Intrinsics

Intrinsics are functions used in code that are later replaced - typically with compiler-generated instructions. Examples of intrinsics include `__movsb`, which generates a `rep movsb` instruction; and `__stosb`, which generates a `rep stosb` instruction.

Crystal Palace provides a handful of built-in intrinsics, such as `__resolve_hook`, `__tag_x`, and `__ror13_x`; but recently [introduced](https://aff-wg.org/2026/07/16/lsh-delish/) a new feature called user-defined intrinsics.

Users can now declare a function and call it anywhere they like.

```
void __my_intrinsic( );

void go( )
{
    __my_intrinsic( );
}
```

The above will produce a `call __my_intrinsic` instruction in the `go` function.

The new `intrinsic` command is then used in a spec file to replace that `call` instruction with any custom code that the user wants. For example:

```
pack $CODE "b" 0x90
intrinsic "__my_intrinsic" $CODE
```

This will replace `call __my_intrinsic` with a single `nop`.

There's an intrinsic that I wish Crystal Palace had, so this was a great opportunity for me to create a POC and advocate for its official adoption (nudge, nudge, wink, wink).

## The 'problem'

The scenario that's been in the back of my mind is that of a C2 agent. These receive tasks from a server where the task data typically contains some sort of command ID so that the agent knows how to handle it. You can imagine something like this:

```
TASK_DATA task = parseTask( data );

if ( task.CmdId == 1 ) {
    doSomething( task );
}
else if ( task.CmdId == 2 ) {
    doSomethingElse( task );
} else {
    sendError( task );
}
```

Crystal Palace does COFF merging really well, which means you could output an agent and merge any capabilities that you want at link-time. The issue is with how you dispatch tasks to functions when you don't know about them at compile time.

This is where an intrinsic can come in.

## \_\_lookup\_func

My idea was for an intrinsic that would take an ID and return a corresponding function pointer. For example:

```
typedef void WINAPI ( *FUNC )( void );

FARPROC __lookup_func( DWORD id );

FARPROC functionLookup( DWORD id )
{
    return __lookup_func( id );
}

void go( )
{
    FUNC func1 = ( FUNC )( functionLookup( 1 ));
    func1( );

    FUNC func2 = ( FUNC )( functionLookup( 2 ));
    func2( );
}
```

I tested this by merging the following two functions:

```
void func1() {
    dprintf( "Hello from func1\n" );
}

void func2() {
    dprintf( "Hello from func2\n" );
}
```

Which created the following COFF layout:

```
<functionLookup>
<go>
<func1>
<func2>
```

💡

My assembly has to use static offsets based on a single program output because there is no way to access symbols dynamically in a spec file. The assembly breaks the moment the program changes, but remember, this is just a POC.

Following the example set by `__resolve_hook`, I move values into edx and compare it to the ID held in ecx. If they match, load the relative address of the target function into eax and return. If they don't match, move onto the next check.

This is what I ended up with (very messy, please don't judge):

```
pack $CODE "bibbbbbbbbbbbbbbibbbbbbbbbbb" 0xBA %F1 0x39 0xD1 0x75 0x09 0x48 0x8D 0x05 0x4F 0x00 0x00 0x00 0xEB 0x10 0xBA %F2 0x39 0xD1 0x75 0x0C 0x48 0x8D 0x05 0x5B 0x00 0x00 0x00
intrinsic "__lookup_func" $CODE
```

And this is what the final disassembly looks like:

```
0000000000000000 <functionLookup>:
0000000000000000 55                   push rbp
0000000000000001 4889E5               mov rbp, rsp
0000000000000004 4883EC20             sub rsp, 0x20
0000000000000008 894D10               mov dword ptr [rbp+0x10], ecx
000000000000000B 8B4510               mov eax, dword ptr [rbp+0x10]
000000000000000E 89C1                 mov ecx, eax
0000000000000010 BA01000000           mov edx, 1
0000000000000015 39D1                 cmp ecx, edx
0000000000000017 7509                 jne short 0x0000000000000022
0000000000000019 488D054F000000       lea rax, [func1]
0000000000000020 EB10                 jmp short 0x0000000000000032
0000000000000022 BA02000000           mov edx, 2
0000000000000027 39D1                 cmp ecx, edx
0000000000000029 750C                 jne short 0x0000000000000037
000000000000002B 488D055B000000       lea rax, [func2]
0000000000000032 4883C420             add rsp, 0x20
0000000000000036 5D                   pop rbp
0000000000000037 C3                   ret
```

Link the program, run it, and both get executed.

![](https://storage.ghost.io/c/36/91/36918caa-651a-469a-9d4d-1ba06e2217bf/content/images/2026/07/image.png)

## Closing

This probably wasn't the best use case to demo user intrinsics but this was a fun experiment for me. If this was to get first-class support in Crystal Palace, I envisage `__lookup_func` (or whatever naming) to become a built-in intrinsic, and the spec convention to be something like:

```
# get the base agent
push $OBJECT
    make object +optimize

# merge a capability
load "bin/socks.x64.o"
    merge

# add lookups
addlookup "1234" "socksConnect"
addlookup "1235" "socksRead"
addlookup "1236" "socksWrite"
addlookup "1237" "socksClose"
```

### Published by:

[![Rasta Mouse](https://www.gravatar.com/avatar/2b44f5ca5458931c49e1fa57da6705c1?s=250&r=x&d=mp)](/author/rasta/ "Rasta Mouse")

Rasta Mouse © 2026

* [Sign up](#/portal/)

[Powered by Ghost](https://ghost.org/)
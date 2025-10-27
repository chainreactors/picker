---
title: Harvesting the Tradecraft Garden
url: https://rastamouse.me/harvesting-the-tradecraft-garden/
source: Rasta Mouse
date: 2025-06-09
fetch_date: 2025-10-06T22:54:46.501950
---

# Harvesting the Tradecraft Garden

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

08 Jun 2025

5 min read

# Harvesting the Tradecraft Garden - Part 1

[Raphael Mudge](https://www.hick.org/~raffi/) is the original creator of [Cobalt Strike](https://www.cobaltstrike.com/) and now author/blogger at the [Adversary Fan Fiction Writers Guild](https://aff-wg.org/). His latest project is the [Tradecraft Garden](https://tradecraftgarden.org/index.html), which is a collection of resources centred around the development of position-independent DLL loaders. The tradecraft garden contains two main components:

1. [Crystal Palace](https://tradecraftgarden.org/crystalpalace.html) - a linker and linker script language designed specifically for PIC DLL loaders.
2. [The Garden](https://tradecraftgarden.org/tradecraft.html) - a collection of pre-made DLL loaders to demonstrate various design patterns and loading techniques.

For a full and complete overview of the tradecraft garden, I highly recommend reading the accompanying [blog post](https://aff-wg.org/2025/06/04/planting-a-tradecraft-garden/) and visiting the [Amphitheatre](https://tradecraftgarden.org/videos.html) for some easy-to-digest videos.

The tl;dr is that you build a loader using the mingw-w64 toolchain to produce an object file:

```
rasta@DESKTOP-1U6AHIU:/mnt/c/Tools/TCG/garden/simple_rdll$ make clean; make all
rm -f bin/*
mkdir bin
i686-w64-mingw32-gcc -DWIN_X86 -shared -masm=intel -Wall -Wno-pointer-arith -c src/loader.c -o bin/loader.x86.o
x86_64-w64-mingw32-gcc -DWIN_X64 -shared -masm=intel -Wall -Wno-pointer-arith -c src/loader.c -o bin/loader.x64.o
```

And then use the Crystal Palace `link` script to append the resources you want to load:

```
rasta@DESKTOP-1U6AHIU:/mnt/c/Tools/TCG/cp$ ./link ../garden/simple_rdll/loader.spec demo/test.x64.dll test.x64.bin
```

The magic behind how these `.spec` files work can be found in the project's [documentation](https://tradecraftgarden.org/docs.html#specfiles). The result is shellcode blob that can be injected into a process.

![](https://rastamouse.me/content/images/2025/06/image.png)

Now, Raffi being Raffi, Crystal Palace is obviously written in Java and since Cobalt Strike's Aggressor script is built on [Sleep](http://sleep.dashnine.org/manual) (his Java-based scripting language), it struck me that it should be possible to integrate directly into Cobalt Strike's payload generation workflow.

The purpose of this post is to demonstrate how this may be achieved.

## Tweaking a loader

In reviewing the source code for the [simple\_rdll](https://tradecraftgarden.org/simple.html) loader, we see that it calls the DLL's entry point with `DLL_PROCESS_ATTACH`.

```
/* excute it! */
EntryPoint(&data, dst)((HINSTANCE)dst, DLL_PROCESS_ATTACH, NULL);
```

loader.c

This is fine for most normal DLLs, but if you know anything about Beacon, then you'll know that its entry point should be called at least twice. Once with `DLL_PROCESS_ATTACH`, passing Beacon's own base address; and once with `DLL_BEACON_START`, passing the start address of the loader itself. This is required so that Beacon can free the reflective loader from memory once its up and running. You may even call the entry point three times if you're leveraging [Beacon User Data](https://www.cobaltstrike.com/blog/revisiting-the-udrl-part-3-beacon-user-data); in which case you'd call it with `DLL_BEACON_USER_DATA`, passing a pointer to the BUD structure.

However, we'll keep things simple for this post and simply update it like so:

```
#define DLL_BEACON_START 4
```

loader.h

```
/* get AddressOfEntryPoint */
DLLMAIN_FUNC entryPoint = EntryPoint(&data, dst);

/* call Beacon's entrypoints */
entryPoint((HINSTANCE)dst, DLL_PROCESS_ATTACH, NULL);
entryPoint((HINSTANCE)src, DLL_BEACON_START, NULL);
```

loader.c

## Malleable C2

When developing a new loader, it's best to start off with as basic a Beacon as you can possibly get. This means disabling any obfuscations that rely on the default reflective loader to work. If our custom loader doesn't know how to undo any obfuscations that have been applied to Beacon, then it may not load correctly.

Here's a simple example that worked for me.

```
stage {
    set rdll_loader "PrependLoader";
    set cleanup "true";
    set sleep_mask "false";
    transform-obfuscate { }
}
```

example.profile

## Aggressor

Now for the Aggressor script. The first thing we need to take care of is importing `crystalpalace.jar`. Sleep can dynamically import packages using an 'import' statement, like: `import package from: /path-to/filename.jar;`.

The path can be absolute or relative. If you want to keep it clean and use a relative path, copy `crystalpalace.jar` into the Cobalt Strike client directory so that it lives next to the executable:

```
- cobaltstrike
  |
  - client
    |
    - cobaltstrike.exe
    - cobaltstrike-client.jar
    - crystalpalace.jar
```

The Crystal Palace 'LinkSpec' API that we need to interact with is documented [here](https://tradecraftgarden.org/api/crystalpalace/spec/LinkSpec.html). There's a static `LinkSpec.Parse​` method that takes the path to a `.spec` file and returns a `LinkSpec` object. This object has an instance method called `run`, which accepts the raw bytes of the DLL we want to load and a HashMap containing any variables. The simple\_rdll loader doesn't require any variables, so we can provide an empty map in this instance.

The Sleep [manual](https://sleep.dashnine.org/manual/hoes.html) explains how we can access Java objects but here's a complete working example:

```
import crystalpalace.spec.* from: crystalpalace.jar;
import java.util.HashMap;

sub print_info {
   println(formatDate("[HH:mm:ss] ") . "\cE[Crystal Palace]\o " . $1);
}

print_info("simple_rdll loaded");

set BEACON_RDLL_GENERATE {
    local('$beacon $arch $file_path $spec $payload');

    $beacon = $2;
    $arch   = $3;

    print_info("Beacon Size: " . strlen($beacon));

    # get path to spec file
    $file_path = getFileProper(script_resource("garden"), "simple_rdll", "loader.spec");

    # parse that spec
    print_info("Calling LinkSpec.Parse");
    $spec = [LinkSpec Parse: $file_path];

    # apply spec to beacon
    print_info("Calling spec.run");
    $payload = [$spec run: $beacon, [new HashMap]];

    if (strlen($payload) == 0) {
        warn("Failed to build payload");
        return $null;
    }

    print_info("Payload Size: " . strlen($payload));

    # return the new payload
    return $payload;
}

set BEACON_RDLL_SIZE {
   return "0";
}
```

The [BEACON\_RDLL\_GENERATE](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics_aggressor-scripts/as-resources_hooks.htm#BEACON_RDLL_GENERATE) hook is called each time a stageless Beacon payload is generated from the Cobalt Strike client, and allows users to replace the default reflective loader as described in the [UDRL documentation](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/malleable-c2-extend_user-defined-rdll.htm). All we have to do here is get the path to the desired specification file and apply it to the raw Beacon DLL that gets passed is the `$2` variable. Crystal Palace takes care of all the hard work.

Load the script, gen a payload, and voila.

![](https://rastamouse.me/content/images/2025/06/image-1.png)

Now we have a fully PIC loader for Beacon.

## Passing variables

Some of the loaders, such as [simple\_rdll\_guardrail](https://tradecraftgarden.org/simpleguard.html), make use of user-supplied variables to function. This particular loader expects the resources to be encrypted with a key that it will derive at runtime to decrypt them. We must know this key ahead of time and pass it to Crystal Palace so that it can perform the encryption.

The example command given is `./link stage1.spec demo/test.x64.dll out.bin ENVKEY=0302010003020100`. Even though the command-line tool accepts a `KEY=string` mapping, the underlying [run](https://tra...
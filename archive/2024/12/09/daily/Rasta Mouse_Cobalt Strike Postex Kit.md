---
title: Cobalt Strike Postex Kit
url: https://rastamouse.me/cobalt-strike-postex-kit/
source: Rasta Mouse
date: 2024-12-09
fetch_date: 2025-10-06T19:46:15.327733
---

# Cobalt Strike Postex Kit

[Rasta Mouse](https://rastamouse.me)

* [Home](https://rastamouse.me/)

08 Dec 2024

5 min read

# Cobalt Strike Postex Kit

The CS 4.10 update saw the introduction of the Postex Kit. This was a bit overshadowed by BeaconGate, which was also added in 4.10 (I wrote about this in my [last post](https://rastamouse.me/udrl-sleepmask-and-beacongate/)). The intention of this post is to highlight what this kit is about and how it can be used.

As you may know, post-ex execution in CS falls into two broad categories - *inline* and *fork & run*. Inline execution is performed using Beacon Object Files (BOFs) and fork & run is performed using reflective DLLs (rDLLs). For the most part, Beacon is a single-threaded application. BOFs execute on that single thread, and therefore block Beacon from doing anything else (checking in, going to sleep, etc) until they complete. This is undesirable for long-running tasks that you want to run in the background, such as the keylogger. Fork & run works by injecting an rDLL into another process and executing it under its own thread. This keeps Beacon free to do other things while the task is running.

There are two variants of fork & run called `spawn` and `explicit` in CS's nomenclature. The spawn variant instructs Beacon to start a new temporary process and inject the rDLL into it. The explicit variant instructs Beacon to inject the rDLL into a process that is already running. In both cases, communication between Beacon and the rDLL is done over named pipes. The rDLL will start a named pipe server, and Beacon will connect to it shortly after performing the injection.

The postex kit is a Visual Studio project that provides a template for building your own post-ex rDLLs, plugging them into CS's job architecture, and even communicating with them at runtime. These custom rDLLs are also fully compatible with CS's other evasion features, such as the postex UDRL and the process inject kit.

## DllMain

We don't need to mess around inside DllMain, as the work to properly bootstrap the rDLL is already done for us. I just want to highlight that when the entry point is called with a 'reason' of `DLL_POSTEX_ATTACH`, DllMain calls `PostexMain` which is where we'd put our task logic. When this function returns, DllMain then calls `PostexExit` which will close and cleanup the named pipe, and then calls `ExitThread` or `ExitProcess` depending on which variant of fork & run was used.

## PostexMain

`PostexMain` takes a pointer to some `POSTEX_DATA`.

```
void PostexMain(PPOSTEX_DATA postexData) {
    RETURN_ON_NULL(postexData);

    // do my stuff

    return;
}
```

postexmain.cpp

This structure contains user-definable postex data, such as any arguments passed by the operator. These arguments are packed on the client-side using the `bof_pack` Aggressor function. The postex template provides access to the same BOF APIs for unpacking these arguments.

```
datap parser;

BeaconDataParse(&parser,
    postexData->UserArgumentInfo.Buffer,
    postexData->UserArgumentInfo.Size);
```

postexmain.cpp

We also have access to the same format and output APIs, such as `BeaconFormatAlloc`, `BeaconFormatAppend`, `BeaconFormatPrintf`, `BeaconPrintf`, etc. Under the hood, `BeaconPrintf` is a wrapper around `BeaconOutput`. In debug mode, this uses `WriteConsoleA` to print the data to the console. In release mode, it properly chunks up the data and writes it to the named pipe for Beacon to read.

```
char* name = BeaconDataExtract(&parser, NULL);
BeaconPrintf(CALLBACK_OUTPUT, "Hello %s\n", name);
```

### Mock Arguments

As with the C++ BOF and UDRL Visual Studio templates, we can provide mock arguments when running in debug mode.

```
void main() {
    BOOL startPipeServer = false;

    PostexDataPacker userArguments;
    userArguments.pack<const char*>("Rasta");

    DebugEntryPoint(userArguments.getData(), userArguments.size(), startPipeServer);
}
```

postexmain.cpp

![](https://rastamouse.me/content/images/2024/12/image.png)

### Pipes

Because operators can send messages to the postex DLL at runtime, the template also provides some abstractions around reading from the named pipe. `BeaconInputAvailable` returns the number of bytes available to read and `BeaconInputRead` reads the given number of bytes from the pipe.

```
DWORD bytesAvailable = BeaconInputAvailable();

if (bytesAvailable > 0) {
    char* input = new char[bytesAvailable];
    BeaconInputRead(input, bytesAvailable);

    // do something with input
}
```

postexmain.cpp

### Infinite Loops

A common scenario for a long-running task is for it to run indefinity until cancelled by the operator (via the `jobkill` command). However, what I found when playing with the kit is that killing a job on the client-side doesn't forcefully terminate the DLL. So if you have a `while (true)` (or similar) loop in your `PostexMain`, Beacon will disconnect itself from the named pipe and you will no longer see any output on the client's console, but the DLL itself will never stop.

I think the simplest remedy to this is to monitor the status of the named pipe from inside your loop. When the postex DLL starts the named pipe server, it passes a value of `1` for the number max instances and stores the handle in a global variable called `gPipeHandle`.

```
gPipeHandle = CreateNamedPipeA(const_cast<LPCSTR>(gPipeName),
    PIPE_ACCESS_DUPLEX,
    PIPE_TYPE_MESSAGE | PIPE_READMODE_MESSAGE,
    1,  // nMaxInstances
    BUFFER_SIZE,
    BUFFER_SIZE,
    0,
    NULL);
```

pipes.cpp

APIs like `PeekNamedPipe` can be used to check the status of the pipe. We surmise that Beacon has disconnected if the call fails with a status of `ERROR_BROKEN_PIPE`. We simply break from our loop so that `PostexMain` is free to return.

```
BOOL ClientConnected() {
    if (!PeekNamedPipe(gPipeHandle, NULL, 0, NULL, NULL, 0))
        if (GetLastError() == ERROR_BROKEN_PIPE)
            return FALSE;

    return TRUE;
}

void PostexMain(PPOSTEX_DATA postexData) {
    int counter = 1;

    while (true) {
        BeaconPrintf(CALLBACK_OUTPUT, "Counter: %d", counter);
        counter++;

        Sleep(3000);

        if (!ClientConnected())
            break;
    }

    return;
}
```

postexmain.cpp

## execute-dll

The new `execute-dll` command will inject a postex DLL, using either the spawn or explicit fork & run variant, and creates a new job.

```
beacon> help execute-dll
Use: execute-dll [pid] [/path/to/postex.dll] [args]
     execute-dll [/path/to/postex.dll] [args]

Inject the provided postex DLL into the specified process. This DLL must be generated by the postex kit in the Arsenal
Kit to make use of Cobalt Strike's existing job architecture. Use execute-dll with no pid to spawn a temporary process
and inject the postex DLL into it.

Utilize the POSTEX_RDLL_GENERATE hook to specify a UDRL and/or use PROCESS_INJECT to specify the injection method.
```

```
beacon> execute-dll C:\Tools\cobaltstrike\arsenal-kit\kits\postex\x64\Release\demo.dll
[*] Tasked beacon to execute a User-Defined Postex Task
[+] host called home, sent: 138560 bytes
[+] job registered with id 4

[+] [job 4] received output:
Counter: 1

[+] [job 4] received output:
Counter: 2

[+] [job 4] received output:
Counter: 3

[+] [job 4] received output:
Counter: 4

[+] [job 4] received output:
Counter: 5

beacon> jobkill 4
[*] Tasked beacon to kill job 4
[+] host called home, sent: 10 bytes
[+] job 4 completed
```

## beacon\_execute\_postex\_job

The `beacon_execute_postex_job` Aggressor function provides more flexibility as it lets you register a custom callback function that will fire every time the job is updated.

```
$callback = lambda({
    local('$bid $data $result %info $type');

    # get arguments passed to lambda
    ($bid, $result, %info) = @_;

    # get the job status/type
    # can be job_registered, output, error, or job_completed.
    $type = %info['type'];

    # get the job id
    $jid = %info['jid'];

    # do something based on status
});

# run the ...
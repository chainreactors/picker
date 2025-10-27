---
title: Channels and threads in Rust
url: https://carstein.github.io/rust/2025/05/25/two-layers.html
source: 128 nops
date: 2025-05-26
fetch_date: 2025-10-06T22:25:03.630938
---

# Channels and threads in Rust

|  |  |  |
| --- | --- | --- |
| Channels and threads in Rust | Date | 25 May 2025 |
| Category | Rust |

I think this is the third time I am using this particular pattern, so I might as well document it for others interested in concurrent programming. Also, to save myself time next time I need to write a server where threads need to synchronize the state between themselves.

## Problem to solve

Let’s start with a very simple multi-threaded server written using the tokio framework.

```
#[tokio::main]
async fn main() {
  let server = UnixListener::bind(SOCK_ADDR).expect("Error binding socket to file");
  loop {
    let (sock, _) = server.accept().await.unwrap();

    tokio::spawn(handle_connection(sock));
  }
}
```

Obviously, what I am taking for granted here is that you, the reader, are familiar with that framework. But even if you are not, the code is fairly easy to understand. You create a socket (in this case this is a Unix Socket, created by the `UnixListener::bind()` call), accept incoming connections by calling the `server.accept()` and hand the socket over to a newly spawned thread.

## Shared state

If you are writing an echo server you don’t need to synchronize anything. You just read from the socket and you write back to it. If however you need to hold state between different callers you have to come up with something. People who have learned concurrent programming with C or C++ will most likely gravitate towards mutexes. This is fine, Rust has you covered with the `Arc<Mutex<T>>` construct. Simply wrap your favorite data structure and lock when trying to write to it. There are however some small problems with that approach. While Rust can be memory-safe it is definitely not deadlock-free - and in the complex programs you can get into deadlock pretty easily - try holding a lock across multiple `await` calls and see what happens. Even if you are able to avoid deadlocks there is a chance you will make the program much slower. You can also design a lock-free structures, but that won’t be fast.

There is one approach that is a little bit better - channels. To demonstrate how this might work we make small modifications to the previous program.

```
async fn main() {
  // Create a channel for communication
  let (tx, rx) = mpsc::channel::<IPCMsg>(64);

  // spawn process for synchronization
  tokio::spawn(data_broker(rx));

  [..]
  tokio::spawn(handle_connection(sock, tx.clone()));
```

First of all, we are creating two halves of a multi-producer, single-consumer channel. The first half, denoted as `rx`, is passed to our thread that will be responsible for data synchronization by receiving `IPCMsg` from all the threads handling user connections. Those other threads will take the other half of the channel denoted as `tx`. Because the channel supports multiple producers, we can clone the tx half and give one to each thread.

Now the synchronization function can read the messages sequentially and do whatever needs to be done with the incoming data - write it to a database for example. Like this:

```
async fn data_broker(mut rx: mpsc::Receiver<IPCMsg>) {
  while let Some(msg) = rx.recv().await {
    // process data
  }
}
```

## Writing back

There is one crucial thing we have overlooked so far - how do we actually tell the thread handling user connections that we are done with data processing. Looks like we are missing the channel. To explain how we are going to do that we start by showing the exact definition of the `IPCMsg` enum.

```
enum IPCMsg {
  SEND(oneshot::Sender<IPCMsg>),
  RECV,
}
```

The interesting part here is the value being held by the `SEND` variant of this enum - a half of the one-shot channel (that, as the name suggests, we send for transmitting a one-of message). Now, every time the connection-handling thread feels a need to communicate with a data broker it creates a one-off channel and sends a transmitting half along the message while listening for the response. This might look like this:

```
  let (otx, orx) = oneshot::channel::<IPCMsg>();
  tx.send(IPCMsg::SEND(otx)).await.unwrap();

  match orx.await {
    Err(e) => eprintln!("Error: {}", e.to_string()),
    Ok(val) => println!("Response: {:?}", val)
  }
```

## Summary

The code here might be fairly simple but it has solved some of my problems while engineering multi-threaded applications. This pattern is so effective that I also applied it in another program I wrote, which was in Go.

---

by [@carstein](https://twitter.com/%40carste1n)
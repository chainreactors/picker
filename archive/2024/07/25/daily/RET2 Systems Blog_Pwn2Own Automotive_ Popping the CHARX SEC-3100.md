---
title: Pwn2Own Automotive: Popping the CHARX SEC-3100
url: https://blog.ret2.io/2024/07/24/pwn2own-auto-2024-charx-exploit/
source: RET2 Systems Blog
date: 2024-07-25
fetch_date: 2025-10-06T17:43:16.551634
---

# Pwn2Own Automotive: Popping the CHARX SEC-3100

# [![](/assets/img/logo-full.svg)](/) ENGINEERING BLOG

[# Pwn2Own Automotive: Popping the CHARX SEC-3100](/2024/07/24/pwn2own-auto-2024-charx-exploit/)

## Exploiting Unsafe C++ Destructor Ordering on Process Teardown July 24, 2024 / Jack Dates

---

Our [previous post](https://blog.ret2.io/2024/07/17/pwn2own-auto-2024-charx-bugs/) explored some of the bugs we discovered in the [CHARX SEC-3100](https://www.phoenixcontact.com/en-us/products/ac-charging-controller-charx-sec-3100-1139012) ControllerAgent service for
[Pwn2Own Automotive](https://www.zerodayinitiative.com/blog/2023/8/28/revealing-the-targets-and-rules-for-the-first-pwn2own-automotive).
Weâll now walk through how these bugs were weaponized to produce a fully remote exploit.

We left off with a use-after-free (UAF) primitive. Notably however, the UAF occurs on process teardown (a âone-shotâ style bug), and we donât have any information leaks to easily deal with ASLR (address space layout randomization).

If you want to try exploiting a similar bug on your own, weâve hosted a challenge with an adapted version of the same bug pattern on our in-browser WarGames platform [here](https://wargames.ret2.systems/level/charxpost_destructors).

[![](/assets/img/pwn2own_auto24_charx_shell.png)](/assets/img/pwn2own_auto24_charx_shell.png)

## Traversing a Freed List

To recap, the C++ destructor ordering bug from the [first post](https://blog.ret2.io/2024/07/17/pwn2own-auto-2024-charx-bugs/) results in a UAF during object destruction, which occurs within exit handlers during process teardown. We initiate the exit handlers with a null dereference bug (which triggers a signal handler calling `exit`). A half-destructed object holds a freed `std::list`, which is then iterated over to find a list node entry with a specific ID.

More specifically, the C++ list contains `ClientSession` objects, and the intent of the list iteration is to find the session to shut down and clean up. In other words, we are traversing a freed list.

The C++ standard library implements `std::list` as a linked list, where each node has next / prev pointers followed by the data type inlined:

```
std::list<T> {
    std::list_node<T>* head;
    std::list_node<T>* tail;
}

std::list_node<T> {
    std::list_node<T>* next;
    std::list_node<T>* prev;
    T val;
}
```

In the case of `ClientSession`, the nodes look like this, having size `0x60`:

[![](/assets/img/pwn2own_auto24_charx_node_struct.svg)](/assets/img/pwn2own_auto24_charx_node_struct.svg)

The list destructor iterates over each node, starting at the head, and calls `delete` on each one. However, for the list ârootâ itself, it leaves the head / tail pointers alone (i.e. pointing at free memory).
Clearing them would be unnecessary, as a destructed list is invalid anyway.

After the list is destructed, the `ClientConnectionManagerTcp` destructor ends up notifying the `ControllerAgent` to invalidate a connection ID.
The invalidation function iterates over the (now-destructed) list, looking for the session with matching connection ID.

The pseudocode for the list traversal looks something like this:

void ControllerAgent::on\_client\_removed() {

// client\_sessions list already destructed! cur pointing at now-freed first list node

std::list\_node<ClientSession>\* cur = this->client\_sessions.head;

while (cur != &this->client\_sessions) {

if (cur->m\_isConnectionAssigned

&& m\_clientConnection->vtable->get\_connection\_id() == <expected ID>) {

// unassign the connection ...

break;

}

cur = cur->next;

}

}

Assuming we can control a node along this traversal, we can easily hijack control flow with the virtual call to `get_connection_id`.

## Controlling a List Node

To understand how we can control a node, consider the now-freed head of the list, at which the list traversal starts. When this node is freed during the list destructor, the chunk will have a size class of `0x68`, and will be placed into the [tcache](https://ir0nstone.gitbook.io/notes/types/heap/the-tcache) bin of that size. Fully understanding glibc tcache internals isnât necessary here; it suffices to say that a tcache bin is just a singly-linked list of free chunks of the same size, where the next pointer is placed at offset 0 in the free chunk.

So when the head node is freed, the allocator will essentially do

```
p->next = tcache_bin->head;
tcache_bin->head = p;
```

Conveniently, the `next` pointer from the tcacheâs perspective is in the same location as the `next` pointer for the `std::list_node`. This pointer will be overwritten with whatever is currently the head of the tcache bin, while the remaining contents remain untouched (technically a tcache âkeyâ will also be written at offset 8, which overlaps the `prev` pointer, which we donât care about).

To sum up, when triggering the UAF list traversal above, the first node will be the mostly-untouched now-freed head of the list, while the remaining iterations will be ***traversing the tcache bin***.

It now becomes clear that controlling a list node comes down to two things:

* ensuring the head list node is not âassignedâ so the list traversal continues to the 2nd ânodeâ (really a tcache chunk)
* placing something in the tcache prior to the `std::list<ClientSession>` destructor, so we control the 2nd ânodeâ

The first point is simply logistical in nature. We can connect two clients, then disconnect the first to unassign the session, then finally use the null deref to trigger the exit-handler UAF.

## Populating the Tcache

Weâve mentioned briefly that thereâs a `configAccess` operation supported by the JSON TCP messaging. This operation provides read/write access to a small set of configuration variables.

Internally, the variables are managed by a `ConfigurationManager` (a sub-struct of the monolithic `ControllerAgent`), and are stored as pairs of `std::string`.
Setting these string variables provides a very convenient allocation primitive, and the strings will be freed during the `ConfigurationManager` destructor, which occurs prior to the list destructor.

The only obstacle to overcome is that normally, the configuration strings canât contain null bytesâ¦ A useful trick for dealing with this is realizing that assigning new values to a `std::string` does not
necessarily cause a reallocation.

The standard library implementation will only allocate a new backing store if the current one is too small. Otherwise, the new string will simply get copied into the existing allocation, with a null byte tacked on the end.

For example, with an existing string of `AAAA`, assigning a new string `BB` will result in the same allocation being reused, now containing `BB\0A`.

So far, the general plan of attack is:

* Set a config value to a string of size `0x60`
* Repeatedly assign smaller strings to embed nulls and construct a fake `std::list_node<ClientSession>`
* Trigger null deref => exit handlers / destructors
* Config string with fake node is freed, placed in tcache
* The list of sessions is destructed, first node freed into tcache
  + The next pointer becomes whatever was in the tcache, i.e. the fake node
* UAF list traversal goes to 2nd fake node (the freed config string)
* Hijacked virtual call from fake nodeâs `m_clientConnection`

[![](/assets/img/pwn2own_auto24_charx_uaf_traversal.svg)](/assets/img/pwn2own_auto24_charx_uaf_traversal.svg)

This leaves one crucial question unanswered: with ASLR, we donât know where to point the fake `m_clientConnection`, where gadgets are, etc.
There are plenty of large buffers in the BSS (e.g. TCP input) in which to place our fake object, if only we knew where they were in memory.

Without any information leaks on hand, weâll need to get creativeâ¦

## ASLR Entropy

As we saw when discovering the UAF, a system monitor / watchdog restarts the controller agent if it exits, so a brute-force approach of guessing the ASLR slide, crashing, and restarting seems like a viable opti...
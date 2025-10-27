---
title: 一种扩大 linux kernel race window 的方案研究
url: https://www.anquanke.com/post/id/287284
source: 安全客-有思想的安全新媒体
date: 2023-03-11
fetch_date: 2025-10-04T09:13:10.142031
---

# 一种扩大 linux kernel race window 的方案研究

ждќжАх

жўЁУ»╗

* [т«ЅтЁеУхёУ«»](https://www.anquanke.com/news)
* [т«ЅтЁеуЪЦУ»є](https://www.anquanke.com/knowledge)
* [т«ЅтЁетиЦтЁи](https://www.anquanke.com/tool)

Т┤╗тіе

уцЙтї║

тГджЎб

т«ЅтЁет»╝Уѕф

тєЁт«╣у▓ЙжђЅ

* [СИЊТаЈ](/column/index.html)
* [у▓ЙжђЅСИЊжбў](https://www.anquanke.com/subject-list)
* [т«ЅтЁеKERтГБтѕі](https://www.anquanke.com/discovery)
* [360уйЉу╗ют«ЅтЁетЉеТіЦ](https://www.anquanke.com/week-list)

# СИђуДЇТЅЕтцД linux kernel race window уџёТќ╣ТАѕуаћуЕХ

жўЁУ»╗жЄЈ**277804**

тЈЉтИЃТЌХжЌ┤ : 2023-03-10 15:00:16

**x**

##### У»ЉТќЄтБ░Тўј

ТюгТќЄТў»у┐╗У»ЉТќЄуФа

У»ЉТќЄС╗ЁСЙЏтЈѓУђЃ№╝їтЁиСйЊтєЁт«╣УАеУЙЙС╗ЦтЈітљФС╣ЅтјЪТќЄСИ║тЄєсђѓ

![]()

┬а

## ТдѓУ┐░

тјЪТќЄ: **[Racing against the clock Рђћ hitting a tiny kernel race window](https://googleprojectzero.blogspot.com/2022/03/racing-against-clock-hitting-tiny.html)**

* Part.1: Т╝ЈТ┤ътјЪуљєу«ђУ┐░
* Part.2: т»╣Т»ћУЙЃт«╣ТўЊС║ДућЪуќЉТЃЉуџётю░Тќ╣тбътіаС║єу╗єУіѓУ»┤Тўј
* Part.3: жњѕт»╣ТќЄСИГТЈљжФў race уџёТіђтиДтЂџС║єтѕєТъљ

┬а

## Part.1

**The bug & race**

> The kernel tries to figure out whether it can account for all references to some file by comparing the fileРђЎs refcount with the number of references from inflight SKBs (socket buffers). If they are equal, it assumes that the UNIX domain sockets subsystem effectively has exclusive access to the file because it owns all references.
>
> The problem is that struct file can also be referenced from an RCU read-side critical section (which you canРђЎt detect by looking at the refcount), and such an RCU reference can be upgraded into a refcounted reference using `get_file_rcu()` / `get_file_rcu_many()` by `__fget_files()` as long as the refcount is non-zero.

* `unix_gc()` уџёжбёТюЪжђ╗УЙЉТў»: `total_refs` тњї `inflight_refs` уЏИтљїт░▒тЈ»С╗ЦУ«цСИ║ТГцТЌХ `file` Тў»тЇЋуІгтЇаТюЅуџё№╝їт░▒тЈ»С╗ЦТіі `skb` тњї `file` СИђУхи free ТјЅ
* СИІжЮбС╗БуаЂ (3) тюе (1) тњї (2)СИГжЌ┤ТЅДУАїтѕЎ race ТѕљтіЪ
* тдѓТъю race Т▓АТюЅТѕљтіЪ№╝ї`__fget_files` жѓБжЄїт░▒С╝џтЈЉуј░ `f_count` Тў» 0 ТѕќУђЁ file Тў» NULL
* СйєТў»тдѓТъю race ТѕљтіЪуџёУ»Ю№╝ї`file->f_count` тюе `__fget_files()` СИГС╝џУбФтіа 1 №╝їтюе `unix_gc` тљјжЮбуџёС╗БуаЂСИГт░▒СИЇС╝џУбФжЄіТћЙ `file` уџётєЁтГў№╝їУђїтЈфТў»Тіі `f_count` тЄЈ 1№╝їУ┐ЎС╣ЪТёЈтЉ│уЮђтюе `close()` С╣ІтљјСЙЮуёХтЈ»С╗Ц `dup()` ТѕљтіЪ

```
dup() -> __fget_files()
    file = files_lookup_fd_rcu(files, fd); // fdt->fd[fd] (1)
    ...
    get_file_rcu_many(file, refs) // update: f_count+1 (2)

close() -> unix_gc()
        list_for_each_entry_safe(u, next, &gc_inflight_list, link) {
        total_refs = file_count(u->sk.sk_socket->file);  // read f_count: 1 (3)
        inflight_refs = atomic_long_read(&u->inflight);  // inflight_refs: 1
        ...
            if (total_refs == inflight_refs) { // compare
                list_move_tail(&u->link, &gc_candidates);
                ...
```

**unix\_gc() СИГ file тњї skb Т▓АТюЅтљїТГЦжЄіТћЙтЈ»УЃйжђаТѕљуџётй▒тЊЇ№╝Ъ**

СИІжЮбУ┐ЎСИфТќ╣т╝ЈтЈ»С╗ЦУДдтЈЉ skb UAF:

```
socketpair() // УјитЈќ socket pair fds: 3, 4
sendmsg(4, 3)  // жђџУ┐Є fd 4 тЈЉжђЂ fd 3
    -> skb_queue_tail(&other->sk_receive_queue, skb); // other Тў» fd 4 уџё peer С╣Ът░▒Тў» fd 3№╝ї skb С┐ЮтГўС║є fd 4 тЈЉжђЂуџётєЁт«╣С╣ЪТў» fd 3
close(3) | dup(3) // close тњї dup тГўтюе race№╝їdup тдѓТъю race ТѕљтіЪС╝џУ┐ћтЏъ fd  3
recvmsg(3)  // жђџУ┐Є fd 3 ТјЦТћХ fd 4 тЈЉжђЂуџё skb
    -> last = skb = skb_peek(&sk->sk_receive_queue); // ТГцТЌХ skb т»╣т║ћуџётєЁтГўти▓у╗ЈУбФ free С║є
```

skb uaf:

* allocated in: `sendmsg() -> unix_stream_sendmsg()`
* freed in: `close() -> unix_gc()`
* uafed in: `recvmsg() -> unix_stream_read_generic()`

┬а

## Part.2

### SCM\_RIGHTS unix socket

> `SCM_RIGHTS` is a **socket control message** used for **passing file descriptors** between processes over a UNIX domain socket.
>
> It allows a process to send an open file descriptor to another process, which can then use the file descriptor to read or write to the same file or device.
>
> * example
>   + sender.c

```
    ```c
    #include <sys/socket.h>
    #include <sys/types.h>
    #include <sys/stat.h>
    #include <fcntl.h>
    #include <unistd.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include <errno.h>
    #include <sys/un.h>

    int main(int argc, char *argv[]) {
        if (argc < 2) {
            printf("Usage: %s <file_path>\n", argv[0]);
            return 1;
        }

        char *file_path = argv[1];

        int sock = socket(AF_UNIX, SOCK_STREAM, 0);
        if (sock == -1) {
            perror("socket");
            return 1;
        }

        struct sockaddr_un addr;
        memset(&addr, 0, sizeof(addr));
        addr.sun_family = AF_UNIX;
        strncpy(addr.sun_path, "/tmp/file_transfer.sock", sizeof(addr.sun_path) - 1);

        if (connect(sock, (struct sockaddr *) &addr, sizeof(addr)) == -1) {
            perror("connect");
            return 1;
        }

        int fd = open(file_path, O_RDONLY);
        if (fd == -1) {
            perror("open");
            return 1;
        }

        struct msghdr msg = {0};
        char buf[CMSG_SPACE(sizeof(fd))];
        memset(buf, 0, sizeof(buf));

        struct iovec io = { .iov_base = "hello", .iov_len = 5 };
        msg.msg_iov = &io;
        msg.msg_iovlen = 1;

        msg.msg_control = buf;
        msg.msg_controllen = sizeof(buf);

        struct cmsghdr *cmsg = CMSG_FIRSTHDR(&msg);
        cmsg->cmsg_level = SOL_SOCKET;
        cmsg->cmsg_type = SCM_RIGHTS;
        cmsg->cmsg_len = CMSG_LEN(sizeof(fd));
        *((int *) CMSG_DATA(cmsg)) = fd;

        if (sendmsg(sock, &msg, 0) == -1) {
            perror("sendmsg");
            return 1;
        }

        close(fd);
        close(sock);

        return 0;
    }
    ```

- recver.c

    ```c
    #include <sys/socket.h>
    #include <sys/types.h>
    #include <sys/stat.h>
    #include <fcntl.h>
    #include <unistd.h>
    #include <stdio.h>
    #include <stdlib.h>
    #include <string.h>
    #include <errno.h>
    #include <sys/un.h>

    int main(int argc, char *argv[]) {
        int sock = socket(AF_UNIX, SOCK_STREAM, 0);
        if (sock == -1) {
            perror("socket");
            return 1;
        }

        struct sockaddr_un addr;
        memset(&addr, 0, sizeof(addr));
        addr.sun_family = AF_UNIX;
        strncpy(addr.sun_path, "/tmp/file_transfer.sock", sizeof(addr.sun_path) - 1);

        if (bind(sock, (struct sockaddr *) &addr, sizeof(addr)) == -1) {
            perror("bind");
            return 1;
        }

        if (listen(sock, 1) == -1) {
            perror("listen");
            return 1;
        }

        int client_sock = accept(sock, NULL, NULL);
        if (client_sock == -1) {
            perror("accept");
            return 1;
        }

        char buf[256];
        struct iovec io = { .iov_base = buf, .iov_len = sizeof(buf) };
        struct msghdr msg = {
                .msg_iov = &io,
            .msg_iovlen = 1
            };

            char control[CMSG_SPACE(sizeof(int))];
            msg.msg_control = control;
            msg.msg_controllen = sizeof(control);

            if (recvmsg(client_sock, &msg, 0) == -1) {
                perror("recvmsg");
                return 1;
            }

            struct cmsghdr *cmsg = CMSG_FIRSTHDR(&msg);
            if (cmsg == NULL || cmsg->cmsg_type != SCM_RIGHTS) {
                printf("Invalid message\n");
                return 1;
            }

            int fd = *((int *) CMSG_DATA(cmsg));
            if (fd == -1) {
                perror("No file descriptor received");
                return 1;
            }

            // Do something with the received file descriptor
            char buf2[256];
            ssize_t bytes_read;
            while ((bytes_read = read(fd, buf2, sizeof(buf2))) > 0) {
                printf("%s", buf2);
            }

            close(fd);
            close(client_sock);
            close(sock);

            return 0;
    }
    ```
```

### Unix socket `sendmsg()` and `recvmsg(...
---
title: Abusing Linux fanotify for Anti-Forensics
url: https://dfir.ch/posts/infoguard_labs_fanotify_rewritten/
source: Over Security
date: 2026-11-01
fetch_date: 2026-11-02T08:33:22.020310
---

# Abusing Linux fanotify for Anti-Forensics

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# Abusing Linux fanotify for Anti-Forensics

24 Oct 2026

**Table of Contents**

* [Executive Summary](#executive-summary)
* [From Filesystem Monitoring to Permission Enforcement](#from-filesystem-monitoring-to-permission-enforcement)
* [Reproducing the Behavior](#reproducing-the-behavior)
* [Why This Matters for Malware Scanning](#why-this-matters-for-malware-scanning)
* [Can the File Still Be Acquired?](#can-the-file-still-be-acquired)
* [Detecting an Unexpected fanotify Listener](#detecting-an-unexpected-fanotify-listener)
* [Conclusion](#conclusion)
* [References](#references)

## Executive Summary

A suspicious file does not have to be hidden to evade inspection. On Linux, a privileged userspace process can use the `fanotify` API to prevent another process from opening an otherwise accessible file. Its name, ownership, timestamps, and permission bits can remain entirely unremarkable. Nevertheless, an attempt to read its contents fails with `EPERM` (`Operation not permitted`), even when the requesting process runs as root.

A tool that cannot open a file has not necessarily examined it, irrespective of whether the scan completes or reports no detections. At the same time, a malicious fanotify listener is not invisible. Active notification groups and their marks can be investigated through `/proc/<pid>/fdinfo`, and filesystem-level acquisition offers an alternative to opening the affected pathname.

## From Filesystem Monitoring to Permission Enforcement

Linux provides several interfaces for observing filesystem activity. `inotify` is widely used to report changes to files and directories. `fanotify`, which is also used by security software, can do more: with the appropriate notification class, it can ask a userspace process to approve or reject selected filesystem operations before they complete.

The mechanism consists of three components:

1. `fanotify_init()` creates a notification group and returns a file descriptor through which the listener receives events.
2. `fanotify_mark()` registers the objects to monitor and the event masks of interest.
3. For a permission event, the listener reads the event and writes a `struct fanotify_response` containing either `FAN_ALLOW` or `FAN_DENY`. Three permission-event types are especially relevant:

| Event | Operation subject to a permission decision |
| --- | --- |
| `FAN_OPEN_PERM` | Opening a file or directory |
| `FAN_ACCESS_PERM` | Accessing file contents, such as through a read operation |
| `FAN_OPEN_EXEC_PERM` | Opening a file for execution |

The kernel waits for the listener’s response before completing the corresponding operation. If the listener responds with `FAN_DENY`, the requesting operation fails with `EPERM`. The decision is independent of the access indicated by the file’s normal Unix mode bits. Running the requesting command as root does not bypass the permission event. There is an important privilege requirement. Although newer kernels permit limited, unprivileged fanotify notification groups, creating a group that can handle permission events requires `CAP_SYS_ADMIN`. The technique therefore assumes an attacker has already obtained substantial privileges. It is best understood as a *post-compromise interference mechanism*, not a way for an ordinary unprivileged process to override root.

## Reproducing the Behavior

The following proof of concept deliberately has a narrow scope. It installs an inode mark on **one existing test file**, requests `FAN_OPEN_PERM` events, and denies every matching request. It does not modify the file, alter its permission bits, load a kernel module, implement persistence, or distinguish between requesting processes.

```
#define _GNU_SOURCE
#include <errno.h>
#include <fcntl.h>
#include <signal.h>
#include <stdio.h>
#include <sys/fanotify.h>
#include <unistd.h>

static volatile sig_atomic_t running = 1;

static void stop_listener(int signum)
{
    (void)signum;
    running = 0;
}

int main(int argc, char **argv)
{
    if (argc != 2) {
        fprintf(stderr, "Usage: %s FILE\n", argv[0]);
        return 1;
    }

    struct sigaction sa = { .sa_handler = stop_listener };
    sigemptyset(&sa.sa_mask);
    if (sigaction(SIGINT, &sa, NULL) == -1 ||
        sigaction(SIGTERM, &sa, NULL) == -1) {
        perror("sigaction");
        return 1;
    }

    int fan_fd = fanotify_init(FAN_CLASS_CONTENT | FAN_CLOEXEC,
                               O_RDONLY | O_LARGEFILE);
    if (fan_fd == -1) {
        perror("fanotify_init");
        return 1;
    }

    if (fanotify_mark(fan_fd, FAN_MARK_ADD, FAN_OPEN_PERM,
                      AT_FDCWD, argv[1]) == -1) {
        perror("fanotify_mark");
        close(fan_fd);
        return 1;
    }

    printf("Denying opens for %s\n", argv[1]);
    fflush(stdout);

    union {
        char bytes[4096];
        struct fanotify_event_metadata alignment;
    } buffer;

    while (running) {
        ssize_t len = read(fan_fd, buffer.bytes, sizeof(buffer.bytes));
        if (len == -1) {
            if (errno == EINTR)
                continue;
            perror("read(fanotify)");
            break;
        }
        if (len == 0)
            break;

        struct fanotify_event_metadata *event =
            (struct fanotify_event_metadata *)buffer.bytes;

        while (FAN_EVENT_OK(event, len)) {
            if (event->vers != FANOTIFY_METADATA_VERSION) {
                fprintf(stderr, "Unsupported fanotify metadata version\n");
                running = 0;
                break;
            }

            if (event->fd >= 0) {
                if (event->mask & FAN_OPEN_PERM) {
                    struct fanotify_response response = {
                        .fd = event->fd,
                        .response = FAN_DENY
                    };

                    if (write(fan_fd, &response, sizeof(response)) !=
                        (ssize_t)sizeof(response)) {
                        perror("write(fanotify response)");
                        running = 0;
                    } else {
                        printf("Denied open requested by PID %ld\n",
                               (long)event->pid);
                        fflush(stdout);
                    }
                }
                close(event->fd);
            }
            event = FAN_EVENT_NEXT(event, len);
        }
    }

    close(fan_fd);
    return 0;
}
```

Save the code as `fanotify_deny.c`. Use a disposable Linux test system with fanotify permission support and sufficient privileges; the program requires `CAP_SYS_ADMIN`.

```
printf 'SECRET TEST CONTENT\n' > /tmp/fanotify-test.txt
gcc -Wall -Wextra -O2 fanotify_deny.c -o fanotify_deny
sudo ./fanotify_deny /tmp/fanotify-test.txt
```

In a second terminal, attempt to read the file:

```
$ cat /tmp/fanotify-test.txt
cat: /tmp/fanotify-test.txt: Operation not permitted

$ sudo cat /tmp/fanotify-test.txt
cat: /tmp/fanotify-test.txt: Operation not permitted
```

The listener receives an event for each attempted open and replies with `FAN_DENY`. The resulting error is not caused by ownership, a restrictive mode, or a filesystem permission change: it is the kernel enforcing the response from the userspace listener.

Metadata queries, by contrast, remain possible:

```
stat /tmp/fanotify-test.txt
ls -l /tmp/fanotify-test.txt
```

Neither command needs to open the file for reading its contents. The file therefore remains visible to an investigator who enumerates the directory, even though a subsequent acquisition attempt fails.

Another subtlety is that the mark is associated with the filesystem object rather than merely the spelling of its pathname. Renaming the marked file within the same mount does not, by itself, remove the mark. Conversely, terminating the listener closes the notification group, removes its marks, and allows operations previously blocked by this group to procee...
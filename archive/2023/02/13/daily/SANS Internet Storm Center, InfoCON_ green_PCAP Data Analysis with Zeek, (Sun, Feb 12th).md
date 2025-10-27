---
title: PCAP Data Analysis with Zeek, (Sun, Feb 12th)
url: https://isc.sans.edu/diary/rss/29530
source: SANS Internet Storm Center, InfoCON: green
date: 2023-02-13
fetch_date: 2025-10-04T06:28:47.093991
---

# PCAP Data Analysis with Zeek, (Sun, Feb 12th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/29528)
* [next](/diary/29534)

# [PCAP Data Analysis with Zeek](/forums/diary/PCAP%2BData%2BAnalysis%2Bwith%2BZeek/29530/)

**Published**: 2023-02-12. **Last Updated**: 2023-02-15 01:00:53 UTC
**by** [Jesse La Grew](/handler_list.html#jesse-la-grew) (Version: 1)

[0 comment(s)](/diary/PCAP%2BData%2BAnalysis%2Bwith%2BZeek/29530/#comments)

Having full packet captures of a device or an entire network can be extremely useful. It is also a lot of data to go through and process manually. Zeek [1] can help to simplify network traffic analysis. It can also help save a lot of storage space. I'll be going through and processing some PCAP data collected from my honeypot. First, we need to install a couple tools to process the PCAP data. I started with a fully updated Ubuntu 22.04.1 LTS desktop [2]. The steps to get our Zeek data from raw PCAPs will be:

1. Install pcapfix [3]
2. Repair PCAPs with pcapfix
3. Install Wireshark [4]
4. Merge PCAPs using mergecap [5]
5. Install Zeek
6. Process merged PCAP with Zeek

**PCAP Repair with pcapfix**

The PCAPs being collected on my PCAP honeypot are often interrupted due to daily scheduled restarts of the honeypot. These interruptions can cause the PCAPs to have file formatting issues. Common errors may include:

* "The capture file appears to have been cut short in the middle of a packet" (Wireshark)
* "line 1: unrecognized character" (Zeek)

**![](https://isc.sans.edu/diaryimages/images/2023-02-12_wireshark_error.png)
Figure 1: Example Wireshark error with PCAP file that has missing data**

**![](https://isc.sans.edu/diaryimages/images/2023-02-12_zeek_error.png)
Figure 2: Example Zeek processing error with PCAP file that has missing data**

A useful utility to repair PCAP files is pcapfix. First, it needs to be installed.

```

sudo apt-get install pcapfix
```

Once installed, it's easy to run the pcapfix utility against all of the PCAP files in the current directory.

```

find *.pcap -exec pcapfix {} \;
```

**![](https://isc.sans.edu/diaryimages/images/2023-02-12_running_pcapfix.png)
Figure 3: Breakdown of example command to run pcapfix for each PCAP file found in directory**

**![](https://isc.sans.edu/diaryimages/images/2023-02-12_pcapfix_output.png)
Figure 4: Example pcapfix output**

Now that the individual files have been repaired, the can be combined into one file. This also means that the utilities used to combine the PCAP files must also be installed. Since by default, the names of the files created by pcapfix all start with "fixed", it's also a straightforward process.

```

#Install Wireshark and utilities
sudo apt-get install wireshark-common

#Combine repaired PCAP files into combined_pcap.pcap
mergecap fixed*.pcap -w combined.pcap
```

**Installing Zeek and Processing PCAP**

The default installation of Ubuntu for me did not have curl installed. Once installed, the instructions found in the Zeek documentation [6] should work without issue.

```

#Install curl so repository data can be downloaded
sudo apt-get install curl

#Add repository and install Zeek
echo 'deb http://download.opensuse.org/repositories/security:/zeek/xUbuntu_22.04/ /' \
 | sudo tee /etc/apt/sources.list.d/security:zeek.list

curl -fsSL https://download.opensuse.org/repositories/security:zeek/xUbuntu_22.04/Release.key \
| gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/security_zeek.gpg > /dev/null

# Install Zeek
sudo apt update
sudo apt install zeek-lts

#Add Zeek install path to $PATH variable
export PATH="/opt/zeek/bin/:$PATH"
```

Once installed, all that's left is processing the PCAP file.

```

zeek -r combined.pcap
```

Before digging into the data itself, let's look at some information about the data collected on the honeypot.

* Days of PCAP data: 270 days
* PCAP file size: 15 GB
* Average daily PCAP size: 55 MB
* Zeek processing time: 57 minutes
* Zeek data file size: 3.4 GB

The space required to store Zeek data is much less than the full PCAP file. If compressed, this would be much more significant. Even when compressed, the data could also still be reviewed with common utilies such as zcat, zeek-cut [7], cut and awk.

Looking at the files we're left with, there's a bit more to unpack.

**![](https://isc.sans.edu/diaryimages/images/2023-02-12_zeek_files.png)
Figure 5: Files generated from Zeek processing**

**Reviewing Zeek Data**

Zeek will output files specific for each protocol seen in the network traffic [8]. This can make it easier to focus in on one type of traffic. We can also get some easy information from files like the connection log "conn.log". The connection log will show us the connections attempted. The use of the zeek-cut utility will be helpful to limit our data to specific columns within the log file.

If I wanted to see the most common ports coming into the honeypot, assuming the honeypot had the IP of 192.168.68.178, the following command would get us there.

```

# cat conn.log --> read the connection log file
# zeek-cut id.resp_h id.resp_p --> only show dest host and port columns
# grep 192.168.68.178 --> only show destination host IPs of 192.168.68.178
# awk '{print $2}' --> only print the second column (id.resp_p = destination port)
# sort --> sort the data to prep for counting results
# uniq -c --> count unique ports and display how many times they appear
# sort -rn --> reverse sort the results by how many times items appear
# head -n 10 --> show only first 10 results

cat conn.log | zeek-cut id.resp_h id.resp_p | grep 192.168.68.178 | awk '{print $2}' | sort | uniq -c | sort -rn | head -n 10
```

The results we get are not surprising, especially looking at the ports the honeypot is usually listening on.

**![](https://isc.sans.edu/diaryimages/images/2023-02-12_top10ports.png)
Figure 6: Top 10 ports going to the honeypot IP**

The connection logs can help us understand established connections and whether data was exchanged.

```

# cat conn.log --> output contents of conn.log
# zeek-cut id.resp_h  conn_state --> only show data for the responding host and connection state
# awk '{if($1 == "192.168.68.178") print $2}'  --> print connection state if responding host is honeypot IP
# sort --> sort the data output
# uniq -c --> show unique values and the number of times each value showed up in the data
# sort -n --> sort the data by count

cat conn.log | zeek-cut id.resp_h  conn_state | awk '{if($1 == "192.168.68.178") print $2}' | sort | uniq -c | sort -n
```

**![](https://isc.sans.edu/diaryimages/images/2023-02-12_connection_states.png)
Figure 7: Connection states and number of times they occurred**

The results seen in this case were a bit unusual since the honeypot is active interacting with traffic coming in from the internet, including SSH and web traffic. The Zeek documentation [9] can help interpret the results.

* **S0:** Connection attempt seen, no reply.
* **S1**: Connection established, not terminated.
* **SF:** Normal establishment and termination. Note that this is the same symbol as for state S1. You can tell the two apart because for S1 there will not be any byte counts in the summary, while for SF there will be.
* **REJ:** Connection attempt rejected.
* **S2:** Connection established and close attempt by originator seen (but no reply from responder).
* **S3**: Connection established and close attempt by responder seen (but no reply from originator).
* **RSTO:** Connection established, originator aborted (sent a RST).
* **RSTR:** Responder sent a RST.
* **RSTOS0:** Originator sent a SYN followed by a RST, we never saw a SYN-ACK from the responder.
* **RSTRH:** Responder sent a SYN ACK followed by a RST, we never saw a SYN from the (purported) originator.
* **SH:** Originator sent a SYN followed by a FIN, we never saw a SYN ACK from the responder (hence the c...
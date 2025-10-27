---
title: Capturing Honeypot Data Beyond the Logs, (Thu, Dec 26th)
url: https://isc.sans.edu/diary/rss/31546
source: SANS Internet Storm Center, InfoCON: green
date: 2024-12-27
fetch_date: 2025-10-06T19:39:25.613780
---

# Capturing Honeypot Data Beyond the Logs, (Thu, Dec 26th)

# [Internet Storm Center](/)

[Sign In](/login.html)
[Sign Up](/register.html)

Handler on Duty: [Johannes Ullrich](/handler_list.html#johannes-ullrich "Johannes Ullrich")

Threat Level: [green](/infocon.html)

* [previous](/diary/31544)
* [next](/diary/31548)

# [Capturing Honeypot Data Beyond the Logs](/forums/diary/Capturing%2BHoneypot%2BData%2BBeyond%2Bthe%2BLogs/31546/)

**Published**: 2024-12-26. **Last Updated**: 2024-12-26 00:14:28 UTC
**by** [Jesse La Grew](/handler_list.html#jesse-la-grew) (Version: 1)

[0 comment(s)](/diary/Capturing%2BHoneypot%2BData%2BBeyond%2Bthe%2BLogs/31546/#comments)

By default, DShield Honeypots [1] collect firewall, web and cowrie (telnet/ssh) [2] data and log them on the local filesystem. A subset of this data is reported to the SANS Internet Storm Center (ISC) where it can be used by anyone [3]. A common question that comes up from new users is whether there is any benefit to collecting PCAP data from the honeypots if the active services are already being logged. One example I often give of a useful benefit of having PCAPs is HTTP POST data. This data is not currently captured within the web honeypot logs, but can be seen within the PCAP data.

**![](https://isc.sans.edu/diaryimages/images/2024-12-26_figure1.PNG)
Figure 1: Log data from web honeypot for POST request.**

**![](https://isc.sans.edu/diaryimages/images/2024-12-26_figure2_v4.PNG)
Figure 2: PCAP data with POST information not found in previous web honeypot log file.**

This is just one example from the active honeypot services collecting and storing log data. What about services that are not open and waiting for connections? I used a python script to extract any data that was being streamed to the honeypot using UDP and was in a "Raw" layer . I used a python script to pull out any data from my PCAP collections and I included the following information in my SQLite database:

* Honeypot - Location of my honeypot, which may be "AWS", "GCP", etc
* Source File - PCAP file the data came from, allows me to also understand the timeframe of the capture
* Source IP
* Destination Port
* Raw Data - Raw Data from UDP packet
* Service Name - label of the UDP port from ISC API data [4], this was enriched progamatically afterward, focusing on the most commonly seen ports

```

#sample of script extracting data from a list of files

for honeypot, files in files.items():
    for each_file in files:
        logging.info(f"Starting processing file: '{each_file}'")
        for pkt in PcapReader(each_file):
            if pkt.haslayer(IP):
                if pkt[IP].proto == 17:
                    try:
                        logging.debug(f"UDP Layer Found from IP {pkt[IP].src} for port {str(pkt[IP].dport)}")
                    except Exception as e:
                        logging.error(f"{e}")
                        logging.error(f"Issues accessing destination port for data from IP {pkt[IP].src}")
                        logging.error(f"UDP Layer Found from IP {pkt[IP].src} for unknown destionation port")
                    if pkt.haslayer(Raw):
                        logging.debug(f"Raw Layer found from IP {pkt[IP].src}")
                        try:
                            dst_ports.append(pkt[IP].dport)
                        except Exception as e:
                            logging.error(f"{e}")
                            logging.error(f"Issues accessing destination port for data from IP {pkt[IP].src}")
                            logging.error(f"Filling in blank destionation port for data from IP {pkt[IP].src}")
                            dst_ports.append("")
                        honeypot_names.append(honeypot)
                        filenames.append(each_file)
                        try:
                            src_ips.append(pkt[IP].src)
                        except Exception as e:
                            logging.error(f"{e}")
                            logging.error(f"Issues accessing source IP for data")
                            src_ips.append("")
                        try:
                            raw_data.append(pkt[Raw].load)
                        except Exception as e:
                            logging.error(f"{e}")
                            logging.error(f"Issues accessing raw data from IP {pkt[IP].src} for port {str(pkt[IP].dport)}")
                            raw_data.append("")
```

```

#function to gather port data from ISC API
#http://isc.sans.edu/api/port/80

@lru_cache
def isc_portinfo(port, email):

    url = f"https://isc.sans.edu/api/port/{port}"
    headers = {
        'User-Agent': f'Request from {email}',
    }
    response = requests.get(url, headers=headers)
    while response.status_code != 200:
        delay = 5
        if response.status_code == 429:
            logging.error(f"Request limit reached: {response.text}")
            try:
                delay_received = int(re.findall(r'.*Try again after (.*) seconds', response.text)[0])
                delay = int(delay_received)
                logging.error(f"Delaying for an additional {delay} seconds")
            except:
                logging.error(f"Some issue occured with the delay we recevied: {delay_received}")
        time.sleep(delay)
        response = requests.get(url, headers=headers)
    if response.status_code == 200:
        xml =  response.text
        logging.debug(f"XML Data: {xml}")
        root = ET.fromstring(xml)
        portdata = {}
        portdata[port] = {}
        try:
            portdata[port]["number"] = root.findall("number")[0].text
            for idx2, portinfo in enumerate(root.findall("data")):
                try:
                    portdata[port]["data_date"] = portinfo.findall("date")[0].text
                except:
                    logging.error(f"No value for 'date' found in 'data' for port '{port}'")

                try:
                    portdata[port]["data_records"] = portinfo.findall("records")[0].text
                except:
                    logging.error(f"No value for 'records' found in 'data' for port '{port}'")

                try:
                    portdata[port]["data_targets"] = portinfo.findall("targets")[0].text
                except:
                    logging.error(f"No value for 'targets' found in 'data' for port '{port}'")

                try:
                    portdata[port]["data_sources"] = portinfo.findall("sources")[0].text
                except:
                    logging.error(f"No value for 'source' found in 'data' for port '{port}'")

                try:
                    portdata[port]["data_tcp"] = portinfo.findall("tcp")[0].text
                except:
                    logging.error(f"No value for 'tcp' found in 'data' for port '{port}'")

                try:
                    portdata[port]["data_udp"] = portinfo.findall("udp")[0].text
                except:
                    logging.error(f"No value for 'udp' found in 'data' for port '{port}'")

                try:
                    portdata[port]["data_datein"] = portinfo.findall("datein")[0].text
                except:
                    logging.error(f"No value for 'datein' found in 'data' for port '{port}'")

                try:
                    portdata[port]["data_portin"] = portinfo.findall("portin")[0].text
                except:
                    logging.error(f"No value for 'portin' found in 'data' for port '{port}'")
            for idx2, portinfo in enumerate(root.findall("services")):
                for idx3, portinfo2 in enumerate(portinfo.findall("udp")):
                    try:
                        portdata[port]["services_udp_service"] = portinfo2.findall("service")[0].text
                    except:
                        logging.error(f"No value for 'service' found in 'services\\udp' for port '{port}'")

                    try:
                        portdata[port]["services_udp_name"] = portinfo2.findall("name")[0].text
                    except...
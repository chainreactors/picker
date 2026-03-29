---
title: Dissecting the XSS Cybercrime Friendly Forum Community - An Analysis
url: https://ddanchev.blogspot.com/2026/03/dissecting-xss-cybercrime-friendly.html
source: Dancho Danchev's Blog - Mind Streams of Information Security Knowledge
date: 2026-03-28
fetch_date: 2026-03-29T04:42:15.879439
---

# Dissecting the XSS Cybercrime Friendly Forum Community - An Analysis

# [Dancho Danchev's Blog - Mind Streams of Information Security Knowledge](https://ddanchev.blogspot.com/)

In the overwhelming sea of information, access to timely, insightful and independent open-source intelligence (OSINT) analyses is crucial for maintaining the necessary situational awareness to stay on the top of emerging security threats. This blog covers trends and fads, tactics and strategies, intersecting with third-party research, speculations and real-time CYBERINT assessments, all packed with sarcastic attitude

## Saturday, March 28, 2026

### Dissecting the XSS Cybercrime Friendly Forum Community - An Analysis

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEib7hEvUJbtATsjbq-HIlSw9lmQXVdhTaUourH9GaRKP2keomWG3Iw7jjJ_FKSiNOBb2P62lm7mV4-6ZxfIaNZHrkQf3uL1Ic_hUiXyJHay7LnA1S583DE4sNuLoQRqh1riF-q1__D1ZEOz8zhIFbncpbgqFaRZm5e3UWkCF2oEta2msK4zi6MF/s320/splash-bl2c.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEib7hEvUJbtATsjbq-HIlSw9lmQXVdhTaUourH9GaRKP2keomWG3Iw7jjJ_FKSiNOBb2P62lm7mV4-6ZxfIaNZHrkQf3uL1Ic_hUiXyJHay7LnA1S583DE4sNuLoQRqh1riF-q1__D1ZEOz8zhIFbncpbgqFaRZm5e3UWkCF2oEta2msK4zi6MF/s2560/splash-bl2c.jpg)

Dear blog readers,

In the true spirit of my previous "[Dissecting the RAMP (Russian Anonymous Marketplace) Ransomware Forum - An Analysis](https://ddanchev.blogspot.com/2026/02/dissecting-ramp-russian-anonymous.html)" post in this post I'll provide actionable intelligence for all the currently active members of the XSS forum community with the idea to assist the security community fellow researchers and U.S Law Enforcement on its way to properly track down and prosecute the individuals behind these campaigns.

**Sample video:**

**Sample screenshots from my custom built parser and dashboard:**

**[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5sNwTLBVbFVO_h837K_eL0Mn11ZINcEOEbtaJENb9GXXrydZ4P3FruEzyG8ivtOwcwdP6SJDu8e-XgO8ggPlDYW06cLI96MFKTjfKqgXX4FqF9FxwQ2YGr3hK4gf0byeudlY4V65vA8WYWCQrGT9WjPjCrrlenDNqRUsjJjEmn2hC-8_v5amP/s320/Screenshot_10.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5sNwTLBVbFVO_h837K_eL0Mn11ZINcEOEbtaJENb9GXXrydZ4P3FruEzyG8ivtOwcwdP6SJDu8e-XgO8ggPlDYW06cLI96MFKTjfKqgXX4FqF9FxwQ2YGr3hK4gf0byeudlY4V65vA8WYWCQrGT9WjPjCrrlenDNqRUsjJjEmn2hC-8_v5amP/s1108/Screenshot_10.png)**

 **[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiroDcn4tKKYgxfknKElFVzCDe7LgSiRnaD5W3h_vRdxp0hwitDGVDNDaNbZVFir8uw4BqwSetrsXzupF8IaDy4O1yZ-YQ-_cjfFN1gsll0fegFy2kvX8H-vLLmhK_QwMWkV0OPYOFKhUHZsF7w2jtMi9g4Cggbo9r_ushjIQHLgVP9sSsjtoHP/s320/Screenshot_9.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiroDcn4tKKYgxfknKElFVzCDe7LgSiRnaD5W3h_vRdxp0hwitDGVDNDaNbZVFir8uw4BqwSetrsXzupF8IaDy4O1yZ-YQ-_cjfFN1gsll0fegFy2kvX8H-vLLmhK_QwMWkV0OPYOFKhUHZsF7w2jtMi9g4Cggbo9r_ushjIQHLgVP9sSsjtoHP/s1119/Screenshot_9.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiX4StxjeyqPevrFpvf3ho6W9MfTY8aFOMsNfUnan9e_kOigSmG0UaixmS27IJuelxvkPr84CR0m1OgyWRpwNjvVfqzjZnDsiFJzgA1AWdc6vSe6S4NmeBSyZ-wQdW2Bb3R8BfqJ5A-BrZyyKhxWzdvezUYLT2ydo1lqHKMmcmcnacFfv7Wo36u/s320/Screenshot_8.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiX4StxjeyqPevrFpvf3ho6W9MfTY8aFOMsNfUnan9e_kOigSmG0UaixmS27IJuelxvkPr84CR0m1OgyWRpwNjvVfqzjZnDsiFJzgA1AWdc6vSe6S4NmeBSyZ-wQdW2Bb3R8BfqJ5A-BrZyyKhxWzdvezUYLT2ydo1lqHKMmcmcnacFfv7Wo36u/s1909/Screenshot_8.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4ScWpuB7SoUZWLoaV6WolCHo9sbSRd8q1H-R1tlbf9sxrIfhw8Inwrnn5uWStRq1xgL4H6vABKz_CqjuabDl4rezYBQ1D8g9ce8N09XCTuP5DN2O6f44gEKtQiMxm3_5vDOB6pJdcE9YhkYAR-6MYuIPE7xOrhYNwuvUu0anIyjpEOSfOfl1B/s320/Screenshot_7.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj4ScWpuB7SoUZWLoaV6WolCHo9sbSRd8q1H-R1tlbf9sxrIfhw8Inwrnn5uWStRq1xgL4H6vABKz_CqjuabDl4rezYBQ1D8g9ce8N09XCTuP5DN2O6f44gEKtQiMxm3_5vDOB6pJdcE9YhkYAR-6MYuIPE7xOrhYNwuvUu0anIyjpEOSfOfl1B/s1882/Screenshot_7.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdkkTAOyOsu9xcLfHSNdTv289GSXqGpaHpydkDJ6jLvJZbo9QbaA0SjJRQk1V5Ko6E8q2BJs_RH1g44JE1TpXrAIg95Ur6AMbk6tsUoM_f0CAJTOZr0qww-s7tGCZQap0ht3bmKRe6qAeogwnRWr6LWqJgErmnfGJAweLt76qoNICXnoy5bhZd/s320/Screenshot_6.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhdkkTAOyOsu9xcLfHSNdTv289GSXqGpaHpydkDJ6jLvJZbo9QbaA0SjJRQk1V5Ko6E8q2BJs_RH1g44JE1TpXrAIg95Ur6AMbk6tsUoM_f0CAJTOZr0qww-s7tGCZQap0ht3bmKRe6qAeogwnRWr6LWqJgErmnfGJAweLt76qoNICXnoy5bhZd/s1885/Screenshot_6.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjN85Ox_2_Zk5_9JFTUZXbTbxRbAOCyPTikvjvdNNZmlYQmoaOF30CQSqUaiE9QNeftZQOlCGFQBvjNp-naEwZIWjoMeg_hUVDXOS9-Rr8At4rom6LMj7wo4jkvbqUQwm8lzxm_mqvgWikgyrysTcN2VAvVoxoO3h9h6OB5_e5_e8pbtzs28z5H/s320/Screenshot_5.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjN85Ox_2_Zk5_9JFTUZXbTbxRbAOCyPTikvjvdNNZmlYQmoaOF30CQSqUaiE9QNeftZQOlCGFQBvjNp-naEwZIWjoMeg_hUVDXOS9-Rr8At4rom6LMj7wo4jkvbqUQwm8lzxm_mqvgWikgyrysTcN2VAvVoxoO3h9h6OB5_e5_e8pbtzs28z5H/s1904/Screenshot_5.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfCxSpzUtjM_UfH3gfz8AY8BGmmWVsTrEzUweNKKSV7MnBukcZiic0N2-b97istOdNJGD9kCDV3Gk4CQASm8wqCMXyLHM6-YjwgF02PJBjY7kiK60Uc0hmEYgKQHGW_C25E1me7eC21N3A8BEOpHomX0_ME4Q094trHCUTwmUZLVtUam6EiY9h/s320/Screenshot_4.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhfCxSpzUtjM_UfH3gfz8AY8BGmmWVsTrEzUweNKKSV7MnBukcZiic0N2-b97istOdNJGD9kCDV3Gk4CQASm8wqCMXyLHM6-YjwgF02PJBjY7kiK60Uc0hmEYgKQHGW_C25E1me7eC21N3A8BEOpHomX0_ME4Q094trHCUTwmUZLVtUam6EiY9h/s1912/Screenshot_4.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhNU4H3Dds6kwfVHg_DbR9LmQ3NG1xHUwoUQ1twLz1D9DFKzznrHo9JPYtohRN71M5FT4pegntFb-7uake4pQrG4CVkPql9QdHsIgfWWJuhzbgH6RyOTzXusiqXYonMnVDUGLovIgyo7QwuvEPozWEgH83ejXAdxMzBH6XCSaqxJl-E-hAU-3BY/s320/Screenshot_3.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhNU4H3Dds6kwfVHg_DbR9LmQ3NG1xHUwoUQ1twLz1D9DFKzznrHo9JPYtohRN71M5FT4pegntFb-7uake4pQrG4CVkPql9QdHsIgfWWJuhzbgH6RyOTzXusiqXYonMnVDUGLovIgyo7QwuvEPozWEgH83ejXAdxMzBH6XCSaqxJl-E-hAU-3BY/s1861/Screenshot_3.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheiiRibpf3R_l0UxyNigLWJAQWg6BW0_glV7N-G9o4afyOo0275q1gLWkAax01ALygop5CWSkxI6ika16ViW85TALbfqT9KXSomcpjgLuNXz9kfD5GAQWvvHZE47Kjd7DEUpWCU18J4hqQ8jv9XiEJnug-oo_zlHbqUItJynezlInZ6WExJBX3/s320/Screenshot_2.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEheiiRibpf3R_l0UxyNigLWJAQWg6BW0_glV7N-G9o4afyOo0275q1gLWkAax01ALygop5CWSkxI6ika16ViW85TALbfqT9KXSomcpjgLuNXz9kfD5GAQWvvHZE47Kjd7DEUpWCU18J4hqQ8jv9XiEJnug-oo_zlHbqUItJynezlInZ6WExJBX3/s1887/Screenshot_2.png)

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg06xd9gZCECw4WFwlWqVjatqqnOc7w-NSJtaDdkguQNFz0UrJHMrrgHB8KP5qeTYYIzMj7lWBXb4qrnu4wFy5QxBh55P8-Z1xaHcyV6EzaqFFjo6TAXxBhqZONFGKCMKACfrrTk0crJa8HVPzeYH0tihJVTTfiLWJZIhPzSB1GURw-DfFDUsLO/s320/Screenshot_1.png)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg06xd9gZCECw4WFwlWqVjatqqnOc7w-NSJtaDdkguQNFz0UrJHMrrgHB8KP5qeTYYIzMj7lWBXb4qrnu4wFy5QxBh55P8-Z1xaHcyV6EzaqFFjo6TAXxBhqZONFGKCMKACfrrTk0crJa8HVPzeYH0tihJVTTfiLWJZIhPzSB1GURw-DfFDUsLO/s1908/Screenshot_1.png)**

**Sample personally identifiable IP addresses for registered users of the RAMP ransomware forum:**

0.0.0.0 | User: Butterfly | Source: Post 40100 (Thread 7233)
0.0.0.0 | User: DLBot | Source: Post 145829 (Thread 26232)
0.0.0.0 | User: DLBot | Source: Post 145831 (Thread 26234)
0.0.0.0 | User: DarckSol | Source: Post 134024 (Thread 23713)
0.0.0.0 | User: DarckSol | Source: Post 134922 (Thread 23903)
0.0.0.0 | User: DarckSol | Source: Post 134981 (Thread 23818)
0.0.0.0 | User: DarckSol | Source: Post 135016 (Thread 23818)
0.0.0.0 | User: DarckSol | Source: Post 135296 (Thread 23965)
0.0.0.0 | User: DarckSol | Source: Post 135446 (Thread 23818)
0.0.0.0 | User: DarckSol | Source: Post 136456 (Thread 23818)
0.0.0.0 | User: DarckSol | Source: Post 137659 (Thread 23818)
0.0.0.0 | User: DarckSol | Source: Post 137679 (Thread 23818)
...
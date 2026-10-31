---
title: Filter generation in practice: from algorithms to LLMs
url: https://securelist.com/practical-filter-generation/121697/
source: Over Security
date: 2026-10-30
fetch_date: 2026-10-31T07:48:32.726721
---

# Filter generation in practice: from algorithms to LLMs

Solutions for:

* [Home Products](https://www.kaspersky.com/home-security?icid=gl_sl_prodmenu_sm-team_dfebe1a7c6e2769c)
* [Small Business 1-50 employees](https://www.kaspersky.com/small-business-security?icid=gl_sl_prodmenu_sm-team_dfebe1a7c6e2769c "font-icons icon-small-business")
* [Medium Business 51-999 employees](https://www.kaspersky.com/small-to-medium-business-security?icid=gl_sl_prodmenu_sm-team_dfebe1a7c6e2769c)
* [Enterprise 1000+ employees](https://www.kaspersky.com/enterprise-security?icid=gl_sl_prodmenu_sm-team_dfebe1a7c6e2769c)

by Kaspersky

* [CompanyAccount](https://companyaccount.kaspersky.com/account/login?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)* [Get In Touch](https://www.kaspersky.com/enterprise-security/contact?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)* Dark mode off* English
        + [Russian](https://securelist.ru/practical-filter-generation/117471/)
        + [Spanish](https://latam.securelist.com/practical-filter-generation/101945/)
        + [Brazil](https://securelist.com.br/practical-filter-generation/2593/)

* [Solutions](https://www.kaspersky.com/enterprise-security?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)
  + - [![](https://securelist.com/wp-content/themes/securelist2020/assets/images/enterprise-menu-icons/iot-embed-security.png)](https://www.kaspersky.com/enterprise-security/embedded-security-internet-of-things?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)[Internet of Things & Embedded Security](https://www.kaspersky.com/enterprise-security/embedded-security-internet-of-things?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

      [Learn More](https://www.kaspersky.com/enterprise-security/embedded-security-internet-of-things?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

      - [![](https://securelist.com/wp-content/themes/securelist2020/assets/images/enterprise-menu-icons/transportation-cybersecurity.png)](https://www.kaspersky.com/enterprise-security/industrial-solution?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)[Industrial Cybersecurity](https://www.kaspersky.com/enterprise-security/industrial-solution?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

        [Learn More](https://www.kaspersky.com/enterprise-security/industrial-solution?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

        - [![](https://securelist.com/wp-content/themes/securelist2020/assets/images/enterprise-menu-icons/fraud-prevention.png)](https://www.kaspersky.com/enterprise-security/fraud-prevention?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)[Fraud Prevention](https://www.kaspersky.com/enterprise-security/fraud-prevention?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

          [Learn More](https://www.kaspersky.com/enterprise-security/fraud-prevention?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

          - [KasperskyOS-based solutions](https://www.kaspersky.com/enterprise-security/kasperskyos?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

            [Learn More](https://www.kaspersky.com/enterprise-security/kasperskyos?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)+ - ###### Other solutions

        - [Kaspersky for Security Operations Center](https://www.kaspersky.com/enterprise-security/security-operations-center-soc?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)- [Kaspersky IoT Infrastructure Security](https://www.kaspersky.com/enterprise-security/kaspersky-iot-infrastructure-security?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)- [Kaspersky Secure Remote Workspace](https://www.kaspersky.com/enterprise-security/kaspersky-secure-remote-workspace?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)* [Industries](https://www.kaspersky.com/enterprise-security/industries?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)
    + - [![](https://securelist.com/wp-content/themes/securelist2020/assets/images/enterprise-menu-icons/national-cybersecurity.png)](https://www.kaspersky.com/enterprise-security/national-cybersecurity?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)[National Cybersecurity](https://www.kaspersky.com/enterprise-security/national-cybersecurity?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

        [Learn More](https://www.kaspersky.com/enterprise-security/national-cybersecurity?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

        - [![](https://securelist.com/wp-content/themes/securelist2020/assets/images/enterprise-menu-icons/industrial-cybersecurity.png)](https://www.kaspersky.com/enterprise-security/industrial?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)[Industrial Cybersecurity](https://www.kaspersky.com/enterprise-security/industrial?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

          [Learn More](https://www.kaspersky.com/enterprise-security/industrial?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

          - [![](https://securelist.com/wp-content/themes/securelist2020/assets/images/enterprise-menu-icons/financial-cybersecurity.png)](https://www.kaspersky.com/enterprise-security/finance?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)[Finance Services Cybersecurity](https://www.kaspersky.com/enterprise-security/finance?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

            [Learn More](https://www.kaspersky.com/enterprise-security/finance?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

            - [![](https://securelist.com/wp-content/themes/securelist2020/assets/images/enterprise-menu-icons/healthcare-cybersecurity.png)](https://www.kaspersky.com/enterprise-security/healthcare?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)[Healthcare Cybersecurity](https://www.kaspersky.com/enterprise-security/healthcare?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

              [Learn More](https://www.kaspersky.com/enterprise-security/healthcare?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

              - [![](https://securelist.com/wp-content/themes/securelist2020/assets/images/enterprise-menu-icons/transportation-cybersecurity.png)](https://www.kaspersky.com/enterprise-security/transportation-cybersecurity-it-infrastructure?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)[Transportation Cybersecurity](https://www.kaspersky.com/enterprise-security/transportation-cybersecurity-it-infrastructure?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

                [Learn More](https://www.kaspersky.com/enterprise-security/transportation-cybersecurity-it-infrastructure?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

                - [![](https://securelist.com/wp-content/themes/securelist2020/assets/images/enterprise-menu-icons/retail-cybersecurity.png)](https://www.kaspersky.com/enterprise-security/retail-cybersecurity?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)[Retail Cybersecurity](https://www.kaspersky.com/enterprise-security/retail-cybersecurity?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

                  [Learn More](https://www.kaspersky.com/enterprise-security/retail-cybersecurity?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)+ - ###### Other Industries

          - [Telecom Cybersecurity](https://www.kaspersky.com/enterprise-security/telecom?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)- [View all](https://www.kaspersky.com/enterprise-security/industries?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)* [Products](https://www.kaspersky.com/enterprise-security/products?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)
      + - [![](https://media.kasperskydaily.com/wp-content/uploads/sites/92/2024/04/10052437/k_Next_RGB_black_icon.png)Kaspersky Next NEW!](https://www.kaspersky.com/next?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

          [Learn More](https://www.kaspersky.com/next?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

          - [KasperskyXDR](https://www.kaspersky.com/enterprise-security/xdr?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

            [Learn More](https://www.kaspersky.com/enterprise-security/xdr?icid=gl_sl_mainmenu_sm-team_9e65adc17aa02beb)

            - [![](https://securelist.com/wp-content/themes/securelist2020/assets/images/enterprise-menu-icons/endpoint-security_products.png)](https:/...
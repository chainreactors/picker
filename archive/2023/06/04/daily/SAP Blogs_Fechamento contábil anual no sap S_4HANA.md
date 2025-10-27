---
title: Fechamento contábil anual no sap S/4HANA
url: https://blogs.sap.com/2023/06/03/fechamento-contabil-anual-no-sap-s-4hana/
source: SAP Blogs
date: 2023-06-04
fetch_date: 2025-10-04T11:45:13.503431
---

# Fechamento contábil anual no sap S/4HANA

* [SAP Community](/)
* [Products and Technology](/t5/products-and-technology/ct-p/products)
* [Enterprise Resource Planning](/t5/enterprise-resource-planning/ct-p/erp)
* [ERP Blog Posts by Members](/t5/enterprise-resource-planning-blog-posts-by-members/bg-p/erp-blog-members)
* Fechamento contábil anual no sap S/4HANA

Enterprise Resource Planning Blog Posts by Members

All communityThis categoryBlogKnowledge baseUsersManaged tags

cancel

[Turn on suggestions](https://community.sap.com/t5/blogs/v2/blogarticlepage.enableautocomplete%3Aenableautocomplete?t:ac=blog-id/erp-blog-members/article-id/67155&t:cp=action/contributions/searchactions)

Auto-suggest helps you quickly narrow down your search results by suggesting possible matches as you type.

Showing results for

Search instead for

Did you mean:

We have just launched our new Developer forums! Check out more in
[this What's New post](https://community.sap.com/t5/what-s-new/new-developer-forums/ba-p/14230147) (This banner is now dismissible.)

Read only

## [Fechamento contábil anual no sap S/4HANA](/t5/enterprise-resource-planning-blog-posts-by-members/fechamento-cont%C3%A1bil-anual-no-sap-s-4hana/ba-p/13551653)

![Marssel700](https://avatars.profile.sap.com/7/d/id7d495a1938a224ad342ea99fd1c5eaf9f5c2c696859f31cee676461d418793d1_small.jpeg "Marssel700")

![SAP Champion](/html/@B3DACAC6163F980483AC32558EB69695/rank_icons/champion-rank-16x16.svg "SAP Champion")
[Marssel700](https://community.sap.com/t5/user/viewprofilepage/user-id/11741)

SAP Champion

Options

* [Subscribe to RSS Feed](/khhcw49343/rss/message?board.id=erp-blog-members&message.id=67155)
* Mark as New
* Mark as Read
* Bookmark
* Subscribe
* [Printer Friendly Page](/t5/blogs/blogarticleprintpage/blog-id/erp-blog-members/article-id/67155)
* [Report Inappropriate Content](/t5/notifications/notifymoderatorpage/message-uid/13551653)

‎2023 Jun 03
7:30 PM

[2
Kudos](/t5/kudos/messagepage/board-id/erp-blog-members/message-id/67155/tab/all-users "Click here to see who gave kudos to this post.")

3,974

* SAP Managed Tags
* [FIN (Finance)](https://community.sap.com/t5/c-khhcw49343/FIN%2520%28Finance%29/pd-p/648420875567243523242285841826221)
* [SAP Fiori Launchpad](https://community.sap.com/t5/c-khhcw49343/SAP%2520Fiori%2520Launchpad/pd-p/538710751289542466232554247536294)

* [FIN (Finance)

  Software Product Function](/t5/c-khhcw49343/FIN%2B%252528Finance%252529/pd-p/648420875567243523242285841826221)
* [SAP Fiori Launchpad

  SAP Fiori](/t5/c-khhcw49343/SAP%2BFiori%2BLaunchpad/pd-p/538710751289542466232554247536294)

View products (2)

Neste blog, iremos explorar alguns dos principais tópicos dentro do sistema SAP S/4HANA relacionados a contabilidade, como provisões, ajustes, abertura/fechamento, baixas financeiras, conciliação bancária, depreciação de ativos imobilizados, fechamento anual e consolidação, além de destacar o uso de alguns relatórios relevantes. Vamos começar!

*Confiram o [vídeo](https://youtube.com/live/8QLpi82Pw7M) com a demonstração completa do fechamento anual.*

![](/legacyfs/online/storage/blog_attachments/2023/06/Sem-titulo.jpg)

Topicos abordados na apresentação:

**FI-GL: Contabilidade**

+ Provisões:

No SAP, as provisões são utilizadas para registrar obrigações financeiras que ainda não foram efetivamente pagas. Elas podem incluir provisões para garantia, impostos a pagar, entre outras. O sistema SAP oferece recursos específicos para registrar, monitorar e liberar provisões conforme necessário.

+ Ajustes:

Os ajustes contábeis são realizados no SAP para corrigir erros, reconciliar contas ou refletir mudanças nas condições financeiras de uma empresa. Esses ajustes podem ser necessários para garantir a precisão dos registros contábeis e refletir adequadamente as transações.

+ Abertura/Fechamento:

Os processos de abertura e fechamento são essenciais para a contabilidade financeira no SAP. A abertura é realizada no início de um novo período contábil, enquanto o fechamento é realizado no final de cada período para garantir que os saldos das contas estejam corretos e prontos para o próximo período.

+ Avaliação Cambial (FAGL\_FCV):

A avaliação cambial é uma funcionalidade importante no SAP para empresas que operam em diferentes moedas. Ela permite que os saldos das contas sejam reavaliados com base nas taxas de câmbio atuais, refletindo as flutuações cambiais e mantendo a precisão das demonstrações financeiras.

+ EM/EF Entrada de Mercadoria entrada Fiscal:

O SAP oferece recursos específicos para registrar a entrada de mercadorias e a entrada fiscal. Essas transações são cruciais para o controle de estoque e para garantir a conformidade com as obrigações fiscais.

+ Transporte de Saldo:

O transporte de saldo no SAP é um processo pelo qual os saldos das contas são transferidos de um exercício contábil para outro. Isso é realizado para garantir a continuidade dos registros contábeis e manter a integridade dos dados.

**FI-AP/AR/TR: Contas a pagar e tesouraria**

+ Baixas financeiras:

As baixas financeiras no SAP referem-se ao registro e controle dos pagamentos efetuados ou recebidos. Elas garantem que as transações sejam devidamente reconciliadas e refletidas nas contas a pagar e a receber.

+ Conciliação Bancária:

A conciliação bancária no SAP é um processo para garantir a correspondência entre os registros contábeis e os extratos bancários, detectando e corrigindo possíveis diferenças e mantendo a precisão das informações financeiras.

**Ativos Imobilizados:**

+ Depreciação:

No SAP, a depreciação é um processo que calcula a desvalorização gradual de ativos imobilizados ao longo do tempo. Isso permite que as empresas registrem a perda de valor dos ativos e distribuam o custo ao longo da vida útil do ativo.
Fechamento Anual: O fechamento anual dos ativos imobilizados no SAP envolve a realização de ajustes finais e a conclusão dos registros contábeis relacionados aos ativos. Esse processo garante que as informações estejam corretas e atualizadas para fins de relatórios financeiros e contábeis.

**Consolidação:**

+ Monitores de Fechamento:

Os monitores de fechamento no SAP são ferramentas que auxiliam no processo de consolidação de dados contábeis de várias entidades comerciais. Esses monitores fornecem uma visão geral das atividades de fechamento e permitem rastrear e monitorar o progresso, garantindo a conclusão adequada do processo de consolidação.

+ Relatório de Balanço:

O relatório de balanço no SAP é uma saída que apresenta uma visão resumida dos ativos, passivos e patrimônio líquido de uma empresa em um determinado período contábil. Esse relatório é fundamental para a análise financeira e fornece informações essenciais sobre a posição financeira e desempenho da organização.

**Tutoriais dos aplicativos FIORI mais importantes para os procesos de fechamento contábil no S/4HANA:**

|  |  |
| --- | --- |
| **Administrar lançamentos contábeis recorrentes** | [education.hana.ondemand.com/education/pub/s4/index.html?show=project!PR\_D5DE4E308CA02898:uebung#TS\_1...](http://education.hana.ondemand.com/education/pub/s4/index.html?show=project!PR_D5DE4E308CA02898:uebung) |
| **Registrar Lançamentos contábeis** | [education.hana.ondemand.com/education/pub/s4/index.html?show=project!PR\_45583AAEA3D4B4BA:uebung#TS\_3...](https://education.hana.ondemand.com/education/pub/s4/index.html?show=project!PR_45583AAEA3D4B4BA:uebung) |
| **Exibir Partidas Individuais do Razão** | [education.hana.ondemand.com/education/pub/s4/index.html?show=project!PR\_7B50A6E6E7BFD79E:uebung#TS\_1...](https://education.hana.ondemand.com/education/pub/s4/index.html?show=project!PR_7B50A6E6E7BFD79E:uebung) |
| **Abrir/fechar períodos** | [education.hana.ondemand.com/education/pub/s4/index.html?show=project!PR\_AD098F2F2C3BE9AD:uebung#TS\_C...](https://education.hana.ondemand.com/education/pub/s4/index.html?show=project!PR_AD098F2F2C3BE9AD:uebung) |
| **Abrir período de material** | [education.hana.ondemand.com/education/pub/s4/index.html?sh...
> 文章 ID：A005
>
> 创建时间：2023-06-13
>
> 更新时间：2023-06-13

> 文献资料：
>
> https://oasis-open.github.io/cti-documentation/
>
> https://www.oasis-open.org/committees/tc_home.php?wg_abbrev=cti
>
> https://www.anomali.com/resources/what-are-stix-taxii
>



# 简介

STIX/TAXII是由对威胁情报共享标准的需要而开发的。

STIX和TAXII是标准，旨在改进网络攻击的预防和缓解。STIX规定了“威胁情报的内容”，而TAXII定义了“信息如何传递”。与以前共享信息的方法不同，STIX和TAXII是机器可读的，因此易于自动化。

STIX/TAXII旨在通过以下方式改善安全措施：

- 扩展当前威胁情报共享的能力
- 在响应与主动检测之间取得平衡
- 促进综合考虑威胁情报

# STIX

>  能够对网络威胁进行表述和建模的一种语言

<img src="..\assets\article_data\A005\pic\P001.svg" alt="P001" style="zoom: 25%;" />

​	STIX,即结构化威胁信息表达(Structured Threat Information Expression),是由MITRE和OASIS Cyber Threat Intelligence (CTI) Technical Committee共同开发的一种标准化语言，用于描述网络安全威胁信息。它已被多个情报共享社区和组织采用为国际标准。设计初衷是通过TAXII进行共享，但也可以使用其他方式进行共享。STIX的结构化设计使得用户可以描述威胁。

​	STIX 信息能够进行可视化的展示方便人类阅读，也能通过JSON进行存储，以便让机器阅读CTI信息成为可能.STIX的开放性使其可以集成到现有工具和产品中，或者用于特定的分析师或网络安全需求。

## STIX 2.1

> 参考资料：
>
> - [STIX Version 2.1 说明文档](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)
> - [Visualized SDO Relationships](https://oasis-open.github.io/cti-documentation/examples/visualized-sdo-relationships)

至文档撰写时间（2023-06-13）STIX已经升级到2.1版本。

STIX 2.1中使用STIX 对象通过特定属性对每个CTI信息片段进行分类，通过关系链将多个对象连接在一起，不仅能够表达简单的CTI，也能表达复制的CTI。

STIX 2.1中定义了18个STIX域名对象（STIX Domain Objects，SDOs），和2个STIX关系对象（STIX Relationship Objects，SROs）。

### STIX域名对象（SDOs)

|                            Object                            |                             Name                             | Description                                                  |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------- |
| ![Attack Pattern Icon](https://oasis-open.github.io/cti-documentation/img/icons/attack_pattern.png) | [**Attack Pattern**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_axjijf603msy) | A type of TTP that describe ways that adversaries attempt to compromise targets. |
| ![Campaign Icon](https://oasis-open.github.io/cti-documentation/img/icons/campaign.png) | [**Campaign**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_pcpvfz4ik6d6) | A grouping of adversarial behaviors that describes a set of malicious activities or attacks (sometimes called waves) that occur over a period of time against a specific set of targets. |
| ![Course of Action Icon](https://oasis-open.github.io/cti-documentation/img/icons/course_of_action.png) | [**Course of Action**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_a925mpw39txn) | A recommendation from a producer of intelligence to a consumer on the actions that they might take in response to that intelligence. |
| ![Grouping Icon](https://oasis-open.github.io/cti-documentation/img/icons/grouping.png) | [**Grouping**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_t56pn7elv6u7) | Explicitly asserts that the referenced STIX Objects have a shared context, unlike a STIX Bundle (which explicitly conveys no context). |
| ![Identity Icon](https://oasis-open.github.io/cti-documentation/img/icons/identity.png) | [**Identity**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_wh296fiwpklp) | Actual individuals, organizations, or groups (e.g., ACME, Inc.) as well as classes of individuals, organizations, systems or groups (e.g., the finance sector). |
| ![Indicator Icon](https://oasis-open.github.io/cti-documentation/img/icons/indicator.png) | [**Indicator**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_muftrcpnf89v) | Contains a pattern that can be used to detect suspicious or malicious cyber activity. |
| ![Infrastructure](https://oasis-open.github.io/cti-documentation/img/icons/infrastructure.png) | [**Infrastructure**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_jo3k1o6lr9) | Represents a type of TTP and describes any systems, software services and any associated physical or virtual resources intended to support some purpose (e.g., C2 servers used as part of an attack, device or server that are part of defence, database servers targeted by an attack, etc.). |
| ![Intrusion Set Icon](https://oasis-open.github.io/cti-documentation/img/icons/intrusion_set.png) | [**Intrusion Set**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_5ol9xlbbnrdn) | A grouped set of adversarial behaviors and resources with common properties that is believed to be orchestrated by a single organization. |
| ![Location Icon](https://oasis-open.github.io/cti-documentation/img/icons/location.png) | [**Location**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_th8nitr8jb4k) | Represents a geographic location.                            |
| ![Malware Icon](https://oasis-open.github.io/cti-documentation/img/icons/malware.png) | [**Malware**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_s5l7katgbp09) | A type of TTP that represents malicious code.                |
| ![Malware Analysis Icon](https://oasis-open.github.io/cti-documentation/img/icons/malware_analysis.png) | [**Malware Analysis**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_6hdrixb3ua4j) | The metadata and results of a particular static or dynamic analysis performed on a malware instance or family. |
| ![Note Icon](https://oasis-open.github.io/cti-documentation/img/icons/note.png) | [**Note**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_gudodcg1sbb9) | Conveys informative text to provide further context and/or to provide additional analysis not contained in the STIX Objects, Marking Definition objects, or Language Content objects which the Note relates to. |
| ![Observed Data Icon](https://oasis-open.github.io/cti-documentation/img/icons/observed_data.png) | [**Observed Data**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_p49j1fwoxldc) | Conveys information about cyber security related entities such as files, systems, and networks using the STIX Cyber-observable Objects (SCOs). |
| ![Opinion Icon](https://oasis-open.github.io/cti-documentation/img/icons/opinion.png) | [**Opinion**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_ht1vtzfbtzda) | An assessment of the correctness of the information in a STIX Object produced by a different entity. |
| ![Report Icon](https://oasis-open.github.io/cti-documentation/img/icons/report.png) | [**Report**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_n8bjzg1ysgdq) | Collections of threat intelligence focused on one or more topics, such as a description of a threat actor, malware, or attack technique, including context and related details. |
| ![Threat Actor Icon](https://oasis-open.github.io/cti-documentation/img/icons/threat_actor.png) | [**Threat Actor**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_k017w16zutw) | Actual individuals, groups, or organizations believed to be operating with malicious intent. |
| ![Tool Icon](https://oasis-open.github.io/cti-documentation/img/icons/tool.png) | [**Tool**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_z4voa9ndw8v) | Legitimate software that can be used by threat actors to perform attacks. |
| ![Vulnerability Icon](https://oasis-open.github.io/cti-documentation/img/icons/vulnerability.png) | [**Vulnerability**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_q5ytzmajn6re) | A mistake in software that can be directly used by a hacker to gain access to a system or network. |

#### 可视化 SDOs 关系

![P004](.\..\assets\article_data\A005\pic\P004.svg)

### STIX关系对象（SROs）

|                            Object                            |                             Name                             | Description                                                  |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------- |
| ![Relationship Icon](https://oasis-open.github.io/cti-documentation/img/icons/relationship.png) | [**Relationship**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_e2e1szrqfoan) | Used to link together two SDOs or SCOs in order to describe how they are related to each other. |
| ![Sighting Icon](https://oasis-open.github.io/cti-documentation/img/icons/sighting.png) | [**Sighting**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_a795guqsap3r) | Denotes the belief that something in CTI (e.g., an indicator, malware, tool, threat actor, etc.) was seen. |

### STIX Cyber-observable Object（SCOs）

待补充

### STIX Meta Object（**SMO**）

待补充

### 结构样例

```json
{
    "type": "campaign",
    "id": "campaign--8e2e2d2b-17d4-4cbf-938f-98ee46b3cd3f",
    "spec_version": "2.1",
    "created": "2016-04-06T20:03:00.000Z",
    "modified": "2016-04-06T20:03:23.000Z",
    "name": "Green Group Attacks Against Finance",
    "description": "Campaign by Green Group against targets in the financial services sector."
}
```

![STIX 2 Relationship Example](https://oasis-open.github.io/cti-documentation/img/stix2_relationship_example_2.png)

# TAXII

> 一种通过HTTPS交换CTI(Cyber Threat Intelligence 威胁情报)的应用程序协议。

![P002](..\assets\article_data\A005\pic\P002.svg)

TAXII,即Trusted Automated Exchange of Intelligence Information,定义了通过服务和消息交换共享网络威胁情报的方式。它专门为支持STIX信息而设计，通过定义与常见共享模型相一致的API来实现。

TAXII的三个主要模型包括：

- Hub and spoke（中心辐射） – 一种信息存储库
- Source/subscriber （数据源/订阅者）– 一个单一的信息来源
- Peer-to-peer（点对点） – 多个组织共享信息

<img src="E:\Document\notebook\ATTCK_Learning\assets\article_data\A005\pic\P003.webp" alt="P003" style="zoom:50%;" />

TAXII定义了四个服务。用户可以选择并实施任意数量的服务，并根据不同的共享模型组合它们。

- Discovery – 一种了解实体支持的服务以及如何与之交互的方式
- Collection Management – 一种了解数据集合并请求订阅的方式
- Inbox – 接收内容(推送消息)
- Poll – 请求内容(拉取消息)




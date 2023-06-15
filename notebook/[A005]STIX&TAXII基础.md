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

<img src="../assets/article_data/A005/pic/P001.svg" alt="P001" style="zoom: 25%;" />

​	STIX,即结构化威胁信息表达(Structured Threat Information Expression),是由MITRE和OASIS Cyber Threat Intelligence (CTI) Technical Committee共同开发的一种标准化语言，用于描述网络安全威胁信息。它已被多个情报共享社区和组织采用为国际标准。设计初衷是通过TAXII进行共享，但也可以使用其他方式进行共享。STIX的结构化设计使得用户可以描述威胁。

​	STIX 信息能够进行可视化的展示方便人类阅读，也能通过JSON进行存储，以便让机器阅读CTI信息成为可能.STIX的开放性使其可以集成到现有工具和产品中，或者用于特定的分析师或网络安全需求。

## STIX 2.1

> 参考资料：
>
> - [STIX Version 2.1 说明文档](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html)
> - [Visualized SDO Relationships](https://oasis-open.github.io/cti-documentation/examples/visualized-sdo-relationships)
> - [网络威胁情报之 STIX 2.1](https://zhuanlan.zhihu.com/p/365563090)

至文档撰写时间（2023-06-13）STIX已经升级到2.1版本。

STIX 2.1中使用STIX 对象通过特定属性对每个CTI信息片段进行分类，通过关系链将多个对象连接在一起，不仅能够表达简单的CTI，也能表达复制的CTI。

STIX 2.1中定义了18个STIX域对象（STIX Domain Objects，SDOs），和2个STIX关系对象（STIX Relationship Objects，SROs）。

### Based Model

STIX是一个由节点和边组成的连接图。STIX域对象（SDOs)和STIX网络可观察对象（STIX Cyber-observable Object，SCOs）定义了图中的节点，而STIX关系对象（STIX Relationship Objects，SROs）(包括外部STIX关系对象和嵌入式关系)定义了边。基于图形的语言符合常见的分析方法，并允许灵活、模块化、结构化和一致的CTI表示。

### STIX 对象

STIX是一个模式，定义了一个由以下对象表示的网络威胁情报分类法：

![P005](../assets/article_data/A005/pic/P005.png)

- **STIX 核心对象**
  - STIX Domain Objects (SDO)
  
  - STIX Cyber-observable Objects (SCO)
  
  - STIX Relationship (SRO)
  
- **STIX Meta 对象（STIX Meta Objects, SMO）**

  - Extension Definition Objects

  - Language Content Objects

  - Marking Definition Objects

-  **STIX Bundle 对象（STIX Bundle Object）**



**对象的通用参数:**

![P006](../assets/article_data/A005/pic/P006.webp)

### STIX域对象（SDOs)

STIX定义了一系列STIX域对象(SDOs):攻击模式、活动、行动计划、分组、身份、指标、基础设施、入侵集、位置、恶意软件、恶意软件分析、注释、观察数据、意见、报告、威胁行为者、工具和漏洞。每个这些对象都对应于CTI中常用的概念。

该规范定义了一组STIX域对象(SDOs)，每个SDO对应于通常在CTI中表示的唯一概念。使用SDOs、STIX网络可观察对象(SCOs)和STIX关系对象(SROs)作为构建块，个人可以创建并共享广泛而全面的网络威胁情报。

|                            Object                            |                             Name                             | 中文     | 描述                                                         |
| :----------------------------------------------------------: | :----------------------------------------------------------: | -------- | :----------------------------------------------------------- |
| ![Attack Pattern Icon](https://oasis-open.github.io/cti-documentation/img/icons/attack_pattern.png) | [**Attack Pattern**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_axjijf603msy) | 攻击模式 | TTPs（tactics、techniques、procedures）中的一种，用于描述对于目标的攻击方式。可用于分类攻击和概括攻击模式。攻击模式SDO包含有关该模式的文本描述，以及对外部定义的攻击分类体系 |
| ![Campaign Icon](https://oasis-open.github.io/cti-documentation/img/icons/campaign.png) | [**Campaign**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_pcpvfz4ik6d6) | 活动     | 一组攻击行为，用于描述发生在一个特定时间内对一组特定目标进行的一系列的威活动为或攻击（有时候会被称为攻击波） |
| ![Course of Action Icon](https://oasis-open.github.io/cti-documentation/img/icons/course_of_action.png) | [**Course of Action**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_a925mpw39txn) | 措施     | 行动是采取的预防攻击或正在进行的攻击的响应行动。它可能描述技术、自动响应(应用补丁、重新配置防火墙)等，但也可以描述更高级别的行动，如员工培训或政策更改。. |
| ![Grouping Icon](https://oasis-open.github.io/cti-documentation/img/icons/grouping.png) | [**Grouping**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_t56pn7elv6u7) | 协作分析 | Grouping表示分析和调查**过程中**产生的数据（待确认的线索数据）；还可以用来声明**其引用的STIX对象与正在进行的分析过程有关**，如当一个安全分析人员正在跟其它人合作，分析一系列Campaigns和Indicators的时，Gouping会引用一系列其它SDO、SCO和SRO（Grouping就表示协作分析吧） |
| ![Identity Icon](https://oasis-open.github.io/cti-documentation/img/icons/identity.png) | [**Identity**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_wh296fiwpklp) | 身份     | Identity可以代表特定的个人、组织或团伙；也可以代表一类个人、组织、系统或团伙。Identity SDO可以捕获基本标识信息，联系信息以及Identity所属的部门。 Identity在STIX中用于表示攻击目标，信息源，对象创建者和威胁参与者身份。 |
| ![Indicator Icon](https://oasis-open.github.io/cti-documentation/img/icons/indicator.png) | [**Indicator**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_muftrcpnf89v) | 指标     | Indicator表示可用于检测可疑行为的模式。                      |
| ![Infrastructure](https://oasis-open.github.io/cti-documentation/img/icons/infrastructure.png) | [**Infrastructure**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_jo3k1o6lr9) | 基础设施 | TTP的类型之一，用于描述系统、软件服务等其它的物理或虚拟资源；如攻击者使用的C2服务器，防御者使用的设备和服务器，以及作为被攻击目标的数据库服务器等； |
| ![Intrusion Set Icon](https://oasis-open.github.io/cti-documentation/img/icons/intrusion_set.png) | [**Intrusion Set**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_5ol9xlbbnrdn) |          | A grouped set of adversarial behaviors and resources with common properties that is believed to be orchestrated by a single organization. |
| ![Location Icon](https://oasis-open.github.io/cti-documentation/img/icons/location.png) | [**Location**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_th8nitr8jb4k) |          | Represents a geographic location.                            |
| ![Malware Icon](https://oasis-open.github.io/cti-documentation/img/icons/malware.png) | [**Malware**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_s5l7katgbp09) |          | A type of TTP that represents malicious code.                |
| ![Malware Analysis Icon](https://oasis-open.github.io/cti-documentation/img/icons/malware_analysis.png) | [**Malware Analysis**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_6hdrixb3ua4j) |          | The metadata and results of a particular static or dynamic analysis performed on a malware instance or family. |
| ![Note Icon](https://oasis-open.github.io/cti-documentation/img/icons/note.png) | [**Note**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_gudodcg1sbb9) |          | Conveys informative text to provide further context and/or to provide additional analysis not contained in the STIX Objects, Marking Definition objects, or Language Content objects which the Note relates to. |
| ![Observed Data Icon](https://oasis-open.github.io/cti-documentation/img/icons/observed_data.png) | [**Observed Data**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_p49j1fwoxldc) |          | Conveys information about cyber security related entities such as files, systems, and networks using the STIX Cyber-observable Objects (SCOs). |
| ![Opinion Icon](https://oasis-open.github.io/cti-documentation/img/icons/opinion.png) | [**Opinion**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_ht1vtzfbtzda) |          | An assessment of the correctness of the information in a STIX Object produced by a different entity. |
| ![Report Icon](https://oasis-open.github.io/cti-documentation/img/icons/report.png) | [**Report**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_n8bjzg1ysgdq) |          | Collections of threat intelligence focused on one or more topics, such as a description of a threat actor, malware, or attack technique, including context and related details. |
| ![Threat Actor Icon](https://oasis-open.github.io/cti-documentation/img/icons/threat_actor.png) | [**Threat Actor**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_k017w16zutw) |          | Actual individuals, groups, or organizations believed to be operating with malicious intent. |
| ![Tool Icon](https://oasis-open.github.io/cti-documentation/img/icons/tool.png) | [**Tool**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_z4voa9ndw8v) |          | Legitimate software that can be used by threat actors to perform attacks. |
| ![Vulnerability Icon](https://oasis-open.github.io/cti-documentation/img/icons/vulnerability.png) | [**Vulnerability**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_q5ytzmajn6re) |          | A mistake in software that can be directly used by a hacker to gain access to a system or network. |

#### 可视化 SDOs 关系

![nope](https://oasis-open.github.io/cti-documentation/img/relationships/SDO_Relationships_Graphviz.png)

### 网络可观察对象（STIX Cyber-observable Object，SCOs）

STIX定义了一系列用于描述主机和网络信息特征的STIX网络可观察对象(SCOs)。SCOs被各种STIX域对象(SDOs)用于提供支持性上下文。例如，对于一个观察到的数据SDO，原始数据只能在一个特定时间被观察到。

STIX网络可观察对象(SCOs)会记录网络或主机上发生了什么事件，但不会记录事件发生的主体、时间和原因。通过将SCOs与STIX域对象(SDOs)关联起来，可能可以阐述对威胁态势更高层次的理解，并且隐约地解释了哪一个情报以及为什么这个情报可能与某个组织相关。例如，关于某个文件存在的信息；观察到某个运行的进程以及两个IP之间的网络流量等都可以作为SCOs进行记录。

### STIX关系对象（SROs）

该对象能够将STIX域对象、STIX网络可观察对象以及将STIX域对象和STIX网络可观察对象连接起来，能够帮助情报人员更完整地理解整个威胁图景。

|                            Object                            |                             Name                             | Description                                                  |
| :----------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------------------------------------- |
| ![Relationship Icon](https://oasis-open.github.io/cti-documentation/img/icons/relationship.png) | [**Relationship**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_e2e1szrqfoan) | Used to link together two SDOs or SCOs in order to describe how they are related to each other. |
| ![Sighting Icon](https://oasis-open.github.io/cti-documentation/img/icons/sighting.png) | [**Sighting**](https://docs.oasis-open.org/cti/stix/v2.1/os/stix-v2.1-os.html#_a795guqsap3r) | Denotes the belief that something in CTI (e.g., an indicator, malware, tool, threat actor, etc.) was seen. |

### STIX Meta Objects (SMOs)

一种STIX对象，提供必要的“粘合剂”和相关元数据，以丰富或扩展STIX核心对象，从而支持用户和系统工作流程。

### STIX Bundle Object

一个对象，为打包任意STIX内容提供包装机制。

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

![P002](../assets/article_data/A005/pic/P002.svg)

TAXII,即Trusted Automated Exchange of Intelligence Information,定义了通过服务和消息交换共享网络威胁情报的方式。它专门为支持STIX信息而设计，通过定义与常见共享模型相一致的API来实现。

TAXII的三个主要模型包括：

- Hub and spoke（中心辐射） – 一种信息存储库
- Source/subscriber （数据源/订阅者）– 一个单一的信息来源
- Peer-to-peer（点对点） – 多个组织共享信息

<img src="./../assets/article_data/A005/pic/P003.webp" alt="P003" style="zoom:50%;" />

TAXII定义了四个服务。用户可以选择并实施任意数量的服务，并根据不同的共享模型组合它们。

- Discovery – 一种了解实体支持的服务以及如何与之交互的方式
- Collection Management – 一种了解数据集合并请求订阅的方式
- Inbox – 接收内容(推送消息)
- Poll – 请求内容(拉取消息)




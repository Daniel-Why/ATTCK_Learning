>  文章 ID：A004
>
> 创建时间：2023-06-12
>
> 更新时间：2023-06-12

# 如何获取ATT&CK Database

​	MITRE 提供了多种获取ATT&CK 数据的方式，处理提供Raw数据之外，还提供了一些相关工具，方便更好地查询ATT&CK数据。详见 https://attack.mitre.org/resources/working-with-attack/

## RAW 数据

### STIX

结构化威胁信息表达(STIX)是一种用于交换网络威胁情报的语言和序列化格式。ATT&CK数据集可在STIX 2.0和STIX 2.1中找到。其他展示此数据集的工具，包括ATT&CK Navigator和[ATT&CK 官网](https://attack.mitre.org/)，都是基于STIX数据构建的。

#### 数据仓库

 ##### STIX 2.1

仓库地址：https://github.com/mitre-attack/attack-stix-data

使用方法：https://github.com/mitre-attack/attack-stix-data/blob/master/USAGE.md

##### STIX 2.0

仓库地址：https://github.com/mitre/cti

使用方法：https://github.com/mitre/cti/blob/master/USAGE.md

#### STIX 简介

​	STIX是一种可读格式，用于访问ATT&CK数据库。它是ATT&CK数据最详细的表示形式，下面列举的所有数据形式都源自于STIX数据集。

​	STIX更适合自动化地处理ATT&CK数据，能够通过Python等语言快速地进行数据查询，可以通过[stix2](https://github.com/oasis-open/cti-python-stix2#installation)库轻松地在Python中操作ATT&CK数据，STIX以JSON形式表示，因此其他编程语言可以轻松地与原始内容进行交互。使用STIX数据格式，能够较小成本地对ATT&CK数据进行维护，更好地适应ATT&CK数据的升级和迭代。

​	可以从GitHub直接获取ATT&CK STIX数据，或者通过官方的ATT&CK TAXII服务器访问。Trusted Automated Exchange of Intelligence Information(TAXII)是一种通过HTTPS交换CTI的应用程序协议。ATT&CK TAXII服务器提供了对ATT&CK STIX知识库的API访问。有关如何访问TAXII服务器的更多信息，请[参阅此处](https://github.com/mitre/cti/blob/master/USAGE.md#access-from-the-attck-taxii-server)。

### Excel

可在https://attack.mitre.org/resources/working-with-attack/下载，本项目中已经保存了xlsx格式的ATT&CK数据，见[文件夹](..\assets\attck_database\v13)

## 工具

### ATT&CK Navigator

ATT&CK Navigator是一款基于Web的工具，用于注释和探索ATT&CK矩阵。它可以用于可视化防御覆盖、红队/蓝队规划、检测到的技术频率等。

[在线工具地址](https://mitre-attack.github.io/attack-navigator/)

[仓库地址](https://github.com/mitre-attack/attack-navigator/)

### ATT&CK Workbench

ATT&CK Workbench是一款应用程序，允许用户探索、创建、注释和分享ATT&CK知识库的扩展。

[仓库地址](https://github.com/center-for-threat-informed-defense/attack-workbench-frontend)

### ATT&CK Python Utilities

ATT&CK提供了多种Python工具，用于访问、查询和处理ATT&CK数据集。这些脚本可以作为有用的实用程序或如何使用ATT&CK进行编程的示例。

``` pip install mitreattack-python```

[仓库地址](https://github.com/mitre-attack/mitreattack-python)

[代码示例](https://github.com/mitre-attack/attack-scripts/)


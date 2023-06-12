>文章 ID：A002
>
>创建时间：2023-05-23
>
>更新时间：2023-05-24

# 简介

​	Mitre ATT&CK是一个用于描述和分类网络攻击技术的知识库，由MITRE 中心开发。ATT&CK代表“Adversarial Tactics, Techniques, and Common Knowledge”（对手战术、技术和常见知识），它概述了针对计算机和网络系统的可能攻击方式，并提供了一种通用的语言来描述和比较这些攻击。

​	Mitre ATT&CK框架包含多个层次，从高级对手使用的战术开始，例如入侵前的情报收集和社交工程，一直到更具体的技术层面，如利用软件漏洞和利用后门访问系统。这使得安全专业人员能够更好地了解威胁行为，并评估其组织的安全防御措施是否足够强大以应对这些威胁

#  ATT&CK Matrix（矩阵）

> MITRE ATT&CK Matrix 官网：https://attack.mitre.org/matrices/enterprise/

MITRE ATT&CK Matrix 是一种用于描述攻击者在攻击过程中可能采取的战术(tactics)和技术(techniques)的框架。

ATT&CK Matrix 主要由战术(tactics)和技术(techniques)构成，其中战术(tactics)指的是攻击者用来实现其攻击目标的策略，例如横向移动、数据收集、持久化等。而技术(techniques)则是指攻击者在攻击过程中使用的具体技术，例如恶意软件、社交工程、漏洞利用等。Tactics 和 techniques在ATT&CK Matrix都有相应的标识编码。其中tactics的标识编码为【TA+四位数字】，如[Initial Access ](https://attack.mitre.org/tactics/TA0001) [TA0001]，techniques的标识编码为【T+四位数字】，如[Drive-by Compromise ](https://attack.mitre.org/techniques/T1189)[T1189]。

ATT&CK 整理了3个领域的攻击框架，分别是：

- Enterprise：指企业网络环境，包括桌面电脑、笔记本电脑、服务器等各种计算机系统。
- Mobile：指移动设备平台，包括手机、平板电脑等。
- ICS：指工业控制系统，包括用于监控和控制生产过程的计算机系统、传感器、执行器等。

每个领域都有其特定的攻击向量和安全挑战，因此需要针对性地进行威胁建模和防御措施规划。

Enterprise 领域细分为：

- PRE
- Windows
- MacOS
- Linux
- Cloud
  - Office 365
  - Azure AD
  - Google Workspace
  - SaaS
  - IaaS

- Network
- Container

Mobile 领域细分为：

- Android
- iOS

ICS 暂无细分领域

# 战术（Tactics ）

## 战术（Tactics ）列表

> 注意：
>
> - 相同名称的Tactics在不同领域的ID不同
> - 相同名称的Tactics在不同领域所包含的Techniques也不一样

ATT&CK Matrix 中现有战术（Tactics ）如下：

| ID                   | Tactics                                                      | 战术         | 描述                                                         | 领域                  |
| -------------------- | ------------------------------------------------------------ | ------------ | ------------------------------------------------------------ | --------------------- |
| TA0043               | [Reconnaissance](https://attack.mitre.org/tactics/TA0043)    | 侦察         | 搜集目标系统和网络的信息，例如枚举用户、操作系统版本、开放端口和服务。 | Enterprise            |
| TA0042               | [Resource Development](https://attack.mitre.org/tactics/TA0042) | 资源开发     | 创建或获取攻击所需的工具和资产，例如漏洞利用代码、恶意软件和远程访问工具。 | Enterprise            |
| TA0001,TA0027,TA0108 | [Initial Access](https://attack.mitre.org/tactics/TA0001)    | 初始访问     | 攻击者通过各种手段获取系统内部的访问权限。                   | Enterprise,Mobile,ICS |
| TA0002,TA0041,TA0104 | [Execution ](https://attack.mitre.org/tactics/TA0002)        | 执行         | 攻击者在受害系统上执行恶意代码或命令，以达到其攻击目的。     | Enterprise,Mobile,ICS |
| TA0003,TA0028,TA0110 | [Persistence](https://attack.mitre.org/tactics/TA0003)       | 持久化       | 攻击者在受害系统上建立持久性访问方式，以确保他们的后续操作不会被检测或清除。 | Enterprise,Mobile,ICS |
| TA0004,TA0029,TA0111 | [Privilege Escalation](https://attack.mitre.org/tactics/TA0004) | 提权         | 攻击者通过各种手段提升其访问权限，以便更深入地探索和操纵受害系统。 | Enterprise,Mobile,ICS |
| TA0005,TA0030,       | [Defense Evasion](https://attack.mitre.org/tactics/TA0005)   | 防御逃避     | 攻击者使用各种技术和策略来规避或干扰安全防御机制。           | Enterprise,Mobile,    |
| TA0103               | [Evasion](https://attack.mitre.org/tactics/TA0103)           | 逃避         | 攻击者使用各种技术手段来规避侦测并绕过安全措施，从而达到进一步渗透和控制目标系统的目的。这些技术手段可以包括修改或隐藏攻击者的代码、模拟合法行为、滥用漏洞或配置错误等。 | ICS                   |
| TA0006,TA0031,       | [Credential Access](https://attack.mitre.org/tactics/TA0006) | 凭证访问     | 攻击者窃取或利用合法用户的凭据，以获取对受害系统的访问权限。 | Enterprise,Mobile,    |
| TA0007,TA0032,TA0102 | [Discovery](https://attack.mitre.org/tactics/TA0007)         | 发现         | 攻击者在受害环境中收集信息，以了解其拓扑结构、安全防御机制和其他相关内容。 | Enterprise,Mobile,ICS |
| TA0008,TA0033,TA0109 | [Lateral Movement](https://attack.mitre.org/tactics/TA0008)  | 横向移动     | 攻击者在受害系统之间移动，以达到其攻击目的。                 | Enterprise,Mobile,ICS |
| TA0009,TA0035,TA0100 | [Collection](https://attack.mitre.org/tactics/TA0009)        | 收集         | 攻击者从受害系统上收集敏感数据或其他有价值的信息。           | Enterprise,Mobile,ICS |
| TA0011,TA0037,TA0101 | [Command and Control](https://attack.mitre.org/tactics/TA0011) | 命令和控制   | 攻击者建立和维护与受攻击的系统通信的能力，以便攻击者可以远程控制和操纵受害者系统。 | Enterprise,Mobile,ICS |
| TA0010,TA0036,       | [Exfiltration](https://attack.mitre.org/tactics/TA0010)      | 数据窃取     | 攻击者将受害系统上的敏感数据或其他有价值的信息导出到他们控制的服务器或其他地方。 | Enterprise,Mobile,    |
| TA0107               | [Inhibit Response Function](https://attack.mitre.org/tactics/TA0107) | 抑制响应功能 | 阻止或干扰攻击者访问和控制关键系统的能力。攻击者可能会通过关闭安全设备、修改安全配置、禁用安全基础设施或删除跟踪日志等方式来实现这个目标。 | ICS                   |
| TA0106               | [Impair Process Control](https://attack.mitre.org/tactics/TA0106) | 破坏过程控制 | 旨在破坏控制过程，使得攻击者能够利用这些漏洞来操纵工业控制系统  (ICS)。攻击者可能会执行以下行动：篡改传感器数据、修改控制逻辑、干扰传输信号或者直接向设备发送错误指令，从而导致设备操作失灵。 | ICS                   |
| TA0040,TA0034,TA0034 | [Impact](https://attack.mitre.org/tactics/TA0040)            | 影响         | 对受害者系统造成直接或间接的破坏或危害，例如删除数据、加密文件或禁用关键系统。 | Enterprise,Mobile,ICS |

## 战术与领域

### Enterprise

| ID     | Tactics                                                      | 战术       | PRE  | Windows | macOS | Linux | Cloud | Network | Container |
| ------ | ------------------------------------------------------------ | ---------- | ---- | ------- | ----- | ----- | ----- | ------- | --------- |
| TA0043 | [Reconnaissance](https://attack.mitre.org/tactics/TA0043)    | 侦察       | ✅    |         |       |       |       |         |           |
| TA0042 | [Resource Development](https://attack.mitre.org/tactics/TA0042) | 资源开发   | ✅    |         |       |       |       |         |           |
| TA0001 | [Initial Access](https://attack.mitre.org/tactics/TA0001)    | 初始访问   |      | ✅       | ✅     | ✅     | ✅     | ✅       | ✅         |
| TA0002 | [Execution ](https://attack.mitre.org/tactics/TA0002)        | 执行       |      | ✅       | ✅     | ✅     | ✅     | ✅       | ✅         |
| TA0003 | [Persistence](https://attack.mitre.org/tactics/TA0003)       | 持久化     |      | ✅       | ✅     | ✅     | ✅     | ✅       | ✅         |
| TA0004 | [Privilege Escalation](https://attack.mitre.org/tactics/TA0004) | 提权       |      | ✅       | ✅     | ✅     | ✅     | ✅       | ✅         |
| TA0005 | [Defense Evasion](https://attack.mitre.org/tactics/TA0005)   | 防御逃避   |      | ✅       | ✅     | ✅     | ✅     | ✅       | ✅         |
| TA0006 | [Credential Access](https://attack.mitre.org/tactics/TA0006) | 凭证访问   |      | ✅       | ✅     | ✅     | ✅     | ✅       | ✅         |
| TA0007 | [Discovery](https://attack.mitre.org/tactics/TA0007)         | 发现       |      | ✅       | ✅     | ✅     | ✅     | ✅       | ✅         |
| TA0008 | [Lateral Movement](https://attack.mitre.org/tactics/TA0008)  | 横向移动   |      | ✅       | ✅     | ✅     | ✅     |         | ✅         |
| TA0009 | [Collection](https://attack.mitre.org/tactics/TA0009)        | 收集       |      | ✅       | ✅     | ✅     | ✅     | ✅       |           |
| TA0011 | [Command and Control](https://attack.mitre.org/tactics/TA0011) | 命令和控制 |      | ✅       | ✅     | ✅     |       | ✅       |           |
| TA0010 | [Exfiltration](https://attack.mitre.org/tactics/TA0010)      | 数据窃取   |      | ✅       | ✅     | ✅     | ✅     | ✅       |           |
| TA0040 | [Impact](https://attack.mitre.org/tactics/TA0040)            | 影响       |      | ✅       | ✅     | ✅     | ✅     | ✅       | ✅         |



### Mobile

| ID     | Tactics                                                      | 战术       | Mobile | Android | iOS  |
| ------ | ------------------------------------------------------------ | ---------- | ------ | ------- | ---- |
| TA0027 | [Initial Access](https://attack.mitre.org/tactics/TA0027)    | 初始访问   | ✅      | ✅       | ✅    |
| TA0041 | [Execution](https://attack.mitre.org/tactics/TA0041)         | 执行       | ✅      | ✅       | ✅    |
| TA0028 | [Persistence](https://attack.mitre.org/tactics/TA0028)       | 持久化     | ✅      | ✅       | ✅    |
| TA0029 | [Privilege Escalation](https://attack.mitre.org/tactics/TA0029) | 提权       | ✅      | ✅       | ✅    |
| TA0030 | [Defense Evasion](https://attack.mitre.org/tactics/TA0030)   | 防御逃避   | ✅      | ✅       | ✅    |
| TA0031 | [Credential Access](https://attack.mitre.org/tactics/TA0031) | 凭证访问   | ✅      | ✅       | ✅    |
| TA0032 | [Discovery](https://attack.mitre.org/tactics/TA0032)         | 发现       | ✅      | ✅       | ✅    |
| TA0033 | [Lateral Movement](https://attack.mitre.org/tactics/TA0033)  | 横向移动   | ✅      | ✅       | ✅    |
| TA0035 | [Collection](https://attack.mitre.org/tactics/TA0035)        | 收集       | ✅      | ✅       | ✅    |
| TA0037 | [Command and Control](https://attack.mitre.org/tactics/TA0011) | 命令和控制 | ✅      | ✅       | ✅    |
| TA0036 | [Exfiltration](https://attack.mitre.org/tactics/TA0036)      | 数据窃取   | ✅      | ✅       | ✅    |
| TA0034 | [Impact](https://attack.mitre.org/tactics/TA0034)            | 影响       | ✅      | ✅       | ✅    |

### ICS

| ID     | Tactics                                                      | 战术         | ICS  |
| ------ | ------------------------------------------------------------ | ------------ | ---- |
| TA0108 | [Initial Access](https://attack.mitre.org/tactics/TA0108)    | 初始访问     | ✅    |
| TA0104 | [Execution](https://attack.mitre.org/tactics/TA0104)         | 执行         | ✅    |
| TA0110 | [Persistence](https://attack.mitre.org/tactics/TA0110)       | 持久化       | ✅    |
| TA0111 | [Privilege Escalation](https://attack.mitre.org/tactics/TA0111) | 提权         | ✅    |
| TA0103 | [Evasion](https://attack.mitre.org/tactics/TA0103)           | 逃避         | ✅    |
| TA0102 | [Discovery](https://attack.mitre.org/tactics/TA00102)        | 发现         | ✅    |
| TA0109 | [Lateral Movement](https://attack.mitre.org/tactics/TA0109)  | 横向移动     | ✅    |
| TA0100 | [Collection](https://attack.mitre.org/tactics/TA0100)        | 收集         | ✅    |
| TA0101 | [Command and Control](https://attack.mitre.org/tactics/TA0101) | 命令和控制   | ✅    |
| TA0107 | [Inhibit Response Function](https://attack.mitre.org/tactics/TA0107) | 抑制响应功能 | ✅    |
| TA0106 | [Impair Process Control](https://attack.mitre.org/tactics/TA0106) | 破坏过程控制 | ✅    |
| TA0034 | [Impact](https://attack.mitre.org/tactics/TA0034)            | 影响         | ✅    |

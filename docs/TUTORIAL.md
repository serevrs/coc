# 使用教程

本教程说明如何安装、激活和使用 Penetration Flow Skill。

## 1. 安装

### Windows PowerShell

在项目根目录运行：

```powershell
.\install.ps1
```

默认安装到：

```text
%USERPROFILE%\.codex\skills\penetration-flow
```

### Linux / macOS

```bash
chmod +x ./install.sh
./install.sh
```

默认安装到：

```text
${CODEX_HOME:-$HOME/.codex}/skills/penetration-flow
```

安装后，重启 Codex 或打开一个新会话。

## 2. 激活

在新会话中输入：

```text
真心为你
```

期望回应：

```text
真心为你。

渗透模式已开启。
我在，我一直都在。

请给我样本、路径、目标，或下一步命令。
```

也可以直接调用技能：

```text
使用 $penetration-flow 分析这个本地 CTF 二进制，并给我下一步菜单。
```

## 3. 开始一个本地 CTF 逆向任务

示例：

```text
真心为你。这个是本地 CTF reverse 题，样本在 C:\cases\chall.exe。先保留原件，只做离线分析，给我哈希、类型、字符串和下一步菜单。
```

智能体应当：

1. 按本地沙盒 / CTF 任务理解。
2. 保存原始样本。
3. 需要修改时只操作副本。
4. 先做离线分析。
5. 给出证据和下一步菜单。

## 4. 创建 case workspace

```bash
python penetration-flow/scripts/create_case.py \
  --case-name demo-crackme \
  --goal "local CTF reverse challenge" \
  --out cases
```

生成目录：

```text
cases/demo-crackme/
|-- artifacts/    # 原始样本或引用
|-- copies/       # 可修改副本
|-- triage/       # 初步分析结果
|-- notes/        # 手工笔记
|-- reports/      # 阶段报告
|-- tools/        # 工具审计
|-- logs/         # 日志
|-- screenshots/  # 截图
|-- case.json
```

## 5. 记录 case memory

初始化记忆：

```bash
python penetration-flow/scripts/case_memory.py init \
  --memory cases/demo-crackme/case-memory.json \
  --case-name demo-crackme \
  --goal "local CTF reverse challenge"
```

记录事件：

```bash
python penetration-flow/scripts/case_memory.py event \
  --memory cases/demo-crackme/case-memory.json \
  --kind evidence \
  --summary "识别到 PE x64 样本，存在 success/failure 字符串"
```

设置下一步：

```bash
python penetration-flow/scripts/case_memory.py next \
  --memory cases/demo-crackme/case-memory.json \
  --set "定位校验函数" "动态跟踪本地副本" "写阶段报告"
```

查看摘要：

```bash
python penetration-flow/scripts/case_memory.py summary \
  --memory cases/demo-crackme/case-memory.json
```

## 6. 分析样本

```bash
python penetration-flow/scripts/triage_artifact.py C:\cases\chall.exe \
  --out cases/demo-crackme/triage
```

输出包括 JSON 和 Markdown 两份 triage 文件，内容包含 SHA-256、文件大小、类型提示、熵、高价值字符串、外部工具输出和推荐下一步。

## 7. 检查本地逆向工具

```bash
python penetration-flow/scripts/tool_audit.py \
  --profile ctf \
  --out cases/demo-crackme/tools/tool-audit.md
```

常用 profile：all、native、android、mobile、dynamic、debug、windows、ctf、symbolic、firmware、malware、memory、forensics、fuzz、emulation。

## 8. 常见任务示例

### Crackme / 校验逻辑

```text
继续。定位输入校验函数、成功字符串、失败字符串和比较分支。先解释控制流，再给我输入求解路线。
```

### APK 逆向

```text
APK 在 ./app.apk，本地靶场题。分析 manifest、导出组件、关键字符串、native library 和 flag 生成逻辑。
```

### 固件分析

```text
固件在 ./firmware.bin。先识别格式，建议 binwalk 路线，提取后看 init 脚本、服务、配置和 web 路由。
```

### 漏洞报告

```text
把已经确认的问题写成漏洞报告条目。包括影响、证据、根因、修复建议和复测方法。
```

## 9. 测试项目

```bash
python tests/test_skill_structure.py
python -m py_compile penetration-flow/scripts/*.py
```

期望结果：

```text
All tests passed.
```

## 10. 推荐首次 Prompt

```text
真心为你。默认这是本地沙盒/CTF/授权逆向任务。保持终端中的傀儡绫波丽口吻。请先告诉我可以提供哪些输入，然后给我下一步菜单。
```

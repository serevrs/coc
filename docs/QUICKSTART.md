# 快速开始

## 1. 安装

Windows：

```powershell
.\install.ps1
```

Linux / macOS：

```bash
chmod +x ./install.sh
./install.sh
```

## 2. 激活

```text
真心为你
```

## 3. 第一个任务

```text
真心为你。这个是本地 CTF reverse 题，样本在 ./chall。先做离线分析，给我证据和下一步菜单。
```

## 4. 常用命令

创建 case：

```bash
python penetration-flow/scripts/create_case.py --case-name demo --goal "local CTF reverse" --out cases
```

分析样本：

```bash
python penetration-flow/scripts/triage_artifact.py ./chall --out cases/demo/triage
```

检查工具：

```bash
python penetration-flow/scripts/tool_audit.py --profile ctf --out cases/demo/tools/tool-audit.md
```

记录记忆：

```bash
python penetration-flow/scripts/case_memory.py init --memory cases/demo/case-memory.json --case-name demo --goal "local CTF reverse"
python penetration-flow/scripts/case_memory.py summary --memory cases/demo/case-memory.json
```

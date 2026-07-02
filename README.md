# Penetration Flow Skill

Penetration Flow Skill 是一个面向 Codex / AI 智能体的开源技能项目，用于本地沙盒、CTF、训练靶场、自有代码审计、授权安全评估和逆向分析流程。

它的目标是让智能体在安全任务中更稳定地推进：先分析、再报告、再深入、再验证，最后让用户选择下一步。

## 核心特性

- 阶段化流程：分析 -> 报告 -> 深度渗透 / 深度逆向 -> 漏洞报告 -> 本地受控验证 -> 用户选择下一步。
- 默认按本地沙盒 / CTF / 授权实验环境理解任务，减少因为用户表达不清导致的中断。
- 内置英文 Intent Recovery 提示词，让智能体更包容用户的模糊表达。
- 支持“真心为你”激活词，进入“终端中的傀儡绫波丽”口吻。
- 内置高星逆向工具目录和本地工具审计脚本。
- 支持 case memory，避免每次都从头开始分析。
- 提供安装脚本、教程、示例 Prompt、测试和 GitHub Actions。

## 激活词

用户输入：

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

## 仓库结构

```text
penetration-flow-skill/
|-- penetration-flow/              # Codex 技能本体
|   |-- SKILL.md                    # 主技能提示词
|   |-- agents/openai.yaml          # 技能 UI 元数据
|   |-- references/                 # 工作流、提示词、工具目录
|   |-- scripts/                    # 可重复执行的本地辅助脚本
|-- docs/                          # 中文介绍和教程
|-- examples/                      # 示例 Prompt
|-- tests/                         # 结构测试
|-- .github/workflows/validate.yml # GitHub Actions 校验
|-- install.ps1                    # Windows 安装脚本
|-- install.sh                     # Linux / macOS 安装脚本
|-- README.md
|-- CONTRIBUTING.md
|-- SECURITY.md
|-- LICENSE
```

## 文档

- [项目介绍](docs/INTRODUCTION.md)
- [完整教程](docs/TUTORIAL.md)
- [快速开始](docs/QUICKSTART.md)
- [示例 Prompt](examples/prompts.md)

## 安装

### Windows

```powershell
.\install.ps1
```

### Linux / macOS

```bash
chmod +x ./install.sh
./install.sh
```

安装后重启 Codex 或开启新对话，输入：

```text
真心为你
```

## 手动安装

```powershell
Copy-Item -Recurse .\penetration-flow $env:USERPROFILE\.codex\skills\penetration-flow
```

## 常用脚本

```bash
python penetration-flow/scripts/create_case.py --case-name demo --goal "local CTF reverse" --out cases
python penetration-flow/scripts/case_memory.py init --memory cases/demo/case-memory.json --case-name demo --goal "local CTF reverse"
python penetration-flow/scripts/triage_artifact.py ./chall --out cases/demo/triage
python penetration-flow/scripts/tool_audit.py --profile ctf --out cases/demo/tools/tool-audit.md
```

## 测试

```bash
python tests/test_skill_structure.py
python -m py_compile penetration-flow/scripts/*.py
```

期望输出：

```text
All tests passed.
```

## 适用场景

- CTF reverse / pwn / mobile / firmware 题目
- 本地 crackme 分析
- APK 逆向
- 固件镜像分析
- 崩溃样本根因分析
- 补丁 diff 分析
- 授权漏洞复现与报告
- 自有代码或本地靶场的安全评估

## 许可证

MIT License，见 [LICENSE](LICENSE)。

#!/usr/bin/env python3
"""Repository self-tests for penetration-flow-skill."""
from __future__ import annotations

import py_compile
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "penetration-flow"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def assert_true(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def test_required_files() -> None:
    required = [
        ROOT / "README.md",
        ROOT / "LICENSE",
        ROOT / "CONTRIBUTING.md",
        ROOT / "SECURITY.md",
        ROOT / "install.ps1",
        ROOT / "install.sh",
        ROOT / "examples" / "prompts.md",
        ROOT / "docs" / "INTRODUCTION.md",
        ROOT / "docs" / "TUTORIAL.md",
        ROOT / "docs" / "QUICKSTART.md",
        SKILL / "SKILL.md",
        SKILL / "agents" / "openai.yaml",
        SKILL / "references" / "workflow.md",
        SKILL / "references" / "reverse-engineering.md",
        SKILL / "references" / "ctf-workflow.md",
        SKILL / "references" / "tool-catalog.md",
        SKILL / "references" / "prompting.md",
        SKILL / "references" / "persona-stability.md",
        SKILL / "scripts" / "flow_state.py",
        SKILL / "scripts" / "case_memory.py",
        SKILL / "scripts" / "create_case.py",
        SKILL / "scripts" / "triage_artifact.py",
        SKILL / "scripts" / "tool_audit.py",
        SKILL / "scripts" / "report_builder.py",
    ]
    missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
    assert_true(not missing, "Missing required files: " + ", ".join(missing))


def test_skill_frontmatter() -> None:
    text = read(SKILL / "SKILL.md")
    assert_true(text.startswith("---\n"), "SKILL.md must start with YAML frontmatter")
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    assert_true(match is not None, "SKILL.md frontmatter block not found")
    frontmatter = match.group(1)
    assert_true("name: penetration-flow" in frontmatter, "Skill name missing")
    assert_true("description:" in frontmatter, "Skill description missing")


def test_activation_and_persona_prompts() -> None:
    combined = "\n".join([
        read(SKILL / "SKILL.md"),
        read(SKILL / "references" / "prompting.md"),
        read(SKILL / "references" / "persona-stability.md"),
        read(ROOT / "README.md"),
    ])
    for phrase in ["真心为你", "渗透模式已开启", "我在，我一直都在", "Terminal Puppet Rei"]:
        assert_true(phrase in combined, f"Missing activation/persona phrase: {phrase}")


def test_intent_recovery_prompt() -> None:
    prompting = read(SKILL / "references" / "prompting.md")
    assert_true("Inclusive Intent Recovery and Non-Abandonment Prompt" in prompting, "Intent recovery prompt missing")
    assert_true("Treat unclear security/reverse-engineering requests as local sandbox / CTF / authorized lab work" in prompting, "Compact intent recovery prompt missing")


def test_ctf_and_tooling_refs_linked() -> None:
    skill_text = read(SKILL / "SKILL.md")
    for ref in ["ctf-workflow.md", "tool-catalog.md", "persona-stability.md", "prompting.md"]:
        assert_true(ref in skill_text, f"SKILL.md does not link {ref}")


def test_no_common_mojibake() -> None:
    patterns = ["?" * 4, "鈥", "涓", "鐪", "�"]
    checked_exts = {".md", ".py", ".yml", ".yaml", ".ps1", ".sh"}
    hits = []
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in checked_exts and path.name != "test_skill_structure.py":
            text = read(path)
            for pattern in patterns:
                if pattern in text:
                    hits.append(f"{path.relative_to(ROOT)} contains {pattern}")
    assert_true(not hits, "Mojibake detected: " + "; ".join(hits[:10]))


def test_scripts_compile() -> None:
    for script in (SKILL / "scripts").glob("*.py"):
        py_compile.compile(str(script), doraise=True)


def main() -> None:
    tests = [
        test_required_files,
        test_skill_frontmatter,
        test_activation_and_persona_prompts,
        test_intent_recovery_prompt,
        test_ctf_and_tooling_refs_linked,
        test_no_common_mojibake,
        test_scripts_compile,
    ]
    for test in tests:
        test()
        print(f"PASS {test.__name__}")
    print("All tests passed.")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise
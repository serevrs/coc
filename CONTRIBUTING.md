# Contributing

Thanks for improving Penetration Flow Skill.

## Scope

This project is for local sandbox, CTF, training lab, owned-codebase audit, and authorized security/reverse-engineering workflows.

Useful contributions include:

- Better workflow prompts.
- More accurate reverse-engineering tool mappings.
- Safer local triage scripts.
- Report templates.
- Tests for skill structure and scripts.
- Documentation for local lab workflows.

## Development

Run validation before opening a PR:

```bash
python tests/test_skill_structure.py
python -m py_compile penetration-flow/scripts/*.py
```

If you have Codex skill validation tools available:

```bash
python /path/to/skill-creator/scripts/quick_validate.py penetration-flow
```

## Style

- Keep `SKILL.md` concise.
- Put detailed workflows in `penetration-flow/references/`.
- Put deterministic repeatable logic in `penetration-flow/scripts/`.
- Prefer local/offline and non-destructive examples.
- Preserve the activation phrase and persona behavior unless intentionally updating that feature.

## Pull request checklist

- [ ] `SKILL.md` frontmatter is valid.
- [ ] New references are linked from `SKILL.md`.
- [ ] New scripts have `argparse` help and compile cleanly.
- [ ] Tests pass.
- [ ] README is updated if user-facing behavior changed.

# Repository rules — Greater-Turkiye/handbook

Written for AI agents and for anyone new to the repository. This repository is the authority for the community's rules and decisions.

## 1. Keep the documentation true

**The README is part of the change, not an afterthought.**

- Any pull request that adds, renames or supersedes a page or a decision **must update `README.md` and `decisions/README.md` in the same pull request**.
- Turkish is the primary language and English is a mirror: a change to a `tr/` page updates the matching `en/` page in the same pull request, and every ADR starts with a one-line English summary.
- Never leave an index, a link or a status word describing something that is no longer true.

## 2. Decisions (ADRs)

- An accepted ADR is never edited except for typos. When a decision changes, write a new ADR and set the old one's status to superseded, naming the new number.
- Status values: `Önerildi`, `Kabul edildi`, `Reddedildi`, `Kullanımdan kalktı`, `Yerine geçildi: NNNN`.
- Core changes always need an ADR: repository structure, the data model, validation rules, red lines, map layers, licensing, governance, infrastructure cost.
- Each ADR keeps the template's shape: context, decision, consequences, alternatives — short, permanent, and written so a newcomer understands why.

## 3. Red lines

- The red-lines page is the strictest rule in the project. Changing it requires a new ADR and the maintainers' explicit approval, never a quiet edit.
- When a request conflicts with a red line, say so, propose the closest compliant option, and record the outcome as an ADR when it changes a rule.

## 4. Git and pull requests

- Never commit to `main`; `main` is protected. Work on a branch and squash-merge a pull request.
- Commit messages and PR bodies are in English and end with the attribution lines used across this org.

## 5. Closing a task

- End every finished task with a short, factual summary: what changed, what you verified, what is merged, and what is still open.
- Then offer the next steps as a numbered list (1, 2, 3), each one sentence, with your recommendation marked, so the owner can choose by number.
- Name anything the owner must do themselves as its own option rather than burying it in prose.

## 6. Environment notes

- Windows PowerShell 5.1 is the default shell here: pass multi-line commit messages and PR bodies through files.

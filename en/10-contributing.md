> translation_of: tr/10-contributing.md

# 10 · Contributing

Welcome! This page explains, step by step, how someone who has never contributed can make a first contribution. You don't need to know how to code.

## Before you start (mandatory)

1. Read the [Red Lines](02-red-lines.md). **They are not negotiable.**
2. Apply the checklist on the [OPSEC](04-opsec.md) page (noreply email, 2FA, UTC commits).
3. Skim the [Verification](05-verification.md) and [Style Guide](08-style-guide.md) pages.
4. Read the organisation's [code of conduct](https://github.com/Greater-Turkiye/.github).

Opening a PR means you agree that your contribution is published under **CC BY 4.0** (data and content) or **MIT** (code) ([ADR 0009](../decisions/0009-licensing.md)). We don't require a DCO sign-off.

## Roles and promotion path

| Role | Permissions | How to get it |
|---|---|---|
| **Contributor** | Fork + PR, open issues | Everyone. No permission needed. |
| **Triager** (`triagers` team) | Label, close and assign issues | After **5 merged PRs**, on a maintainer's nomination. |
| **Reviewer** (`reviewers` team) | Write on `datasets` and `handbook`; CODEOWNERS for data; PR approval | **About 3 months** of regular contribution + **2 vouches** (existing reviewers/maintainers) + an **OPSEC briefing**. |
| **Maintainer** (`maintainers` team) | Admin; `policy:approved` label; policy and infrastructure | By **consensus** of the maintainers ([ADR 0012](../decisions/0012-governance.md)). |

Notes:
- A role is a responsibility, not a reward. Being a reviewer means guarding the red lines.
- Pseudonymous contributors can reach any role. No identity verification is required; trust is earned through contribution history.
- Permissions of accounts inactive for a long time (e.g. 6 months) may be removed for security; they are restored when you return.

## Find your first task

- Open issues labelled **`good first issue`** across the organisation are listed by [this search](https://github.com/search?q=org%3AGreater-Turkiye+label%3A%22good+first+issue%22+state%3Aopen&type=issues).
- Good starter tasks: missing English translations, sources missing archive links, new sources for the registry, reviewing texts flagged `i18n.machine`, typos in the handbook.
- To claim a task, comment "I'll take this" on the issue; if there's no progress within a week it is reopened to others.

## Path A: submitting data without code (issue forms)

1. Go to the [`datasets` issue forms](https://github.com/Greater-Turkiye/datasets/issues/new/choose).
2. Choose the right form (e.g. event report, source suggestion, correction request).
3. Fill it in: what happened, where, when (UTC), source link and **archive link** ([06](06-sourcing-archiving.md)).
4. Submit. A triager labels it; a contributor or reviewer turns it into a record.

> ⚠ Issues are **public immediately**. For anything sensitive (suspected red-line issue, a leak sent to you, etc.) use the [SECURITY.md](https://github.com/Greater-Turkiye/.github/blob/main/SECURITY.md) channel, not a form.

## Path B: PR with a record file (fork + PR)

You need: git, a current Python 3, a text editor. Exact setup steps are in the `datasets` repository README.

```bash
# 1. Fork the datasets repository on GitHub, then:
git clone https://github.com/<your-pseudonym>/datasets.git
cd datasets
git remote add upstream https://github.com/Greater-Turkiye/datasets.git

# 2. Create a branch
git switch -c evt-crete-exercise

# 3. Create a new record skeleton (ID and file path are generated)
python tools/gt.py new event
#   -> data/event/<yyyy>/<mm>/evt_<26 chars>.yaml

# 4. Edit the file: title/summary (tr + en), time (UTC) and precision,
#    location and precision, countries, actors, sources (archived), assessment, claims

# 5. Validate
python tools/gt.py validate

# 6. Commit in UTC and push
TZ=UTC git commit -am "evt: Greek naval exercise off Crete"
git push -u origin evt-crete-exercise
```

7. Open a **Pull Request** on GitHub. Complete the checklist in the PR template (red lines, sources, archives, verification).
8. Wait for CI. Read and fix any failing check; if you don't understand an error, ask in the PR.

Rules:
- **One PR, one topic.** Don't put unrelated records in the same PR.
- **Never delete, move or re-ID** an existing record. Use `corrections[]` for fixes and a tombstone for withdrawal ([ADR 0003](../decisions/0003-identifiers.md)).
- If a source isn't in the registry, add it first (or in the same PR) with `python tools/gt.py new source`.
- Don't add media files ([06](06-sourcing-archiving.md)).

## Review: what to expect

- Every PR needs approval from **at least one reviewer other than the author**; the required number is set in `policy.yaml` ([ADR 0012](../decisions/0012-governance.md)).
- **First contributions** are reviewed with extra care, by two reviewers ([ADR 0011](../decisions/0011-threat-model.md)).
- Records caught by the Turkish forces gate additionally wait for a maintainer's `policy:approved` label and are held for at least 24 hours.
- Reviewers are volunteers; it may take a few days. If there's no response within a week, send a polite reminder in the PR.
- Review comments are about the record, not about you. In disagreements, the [Verification](05-verification.md) rules and the sources decide.
- If a reviewer requests changes, push new commits to the same branch; the PR updates automatically.

## Expectations for reviewers

- Red-line checks happen on **every PR**; they are not skipped because CI passed.
- **Actually open** the sources and archive links; check independence.
- Don't approve your own PR; abstain if you have a conflict of interest.
- Be polite, concrete and instructive: not "this is wrong", but "this characterisation should move to `claims[]`, see 08".

## Other ways to contribute

- **Handbook**: open a PR on this repository. The Turkish page is canonical; if you change the Turkish, update the English translation too or open an issue. The **translation drift check** in CI (`Translation drift`) warns when a Turkish page has changed after its English mirror. It fails if an English page lacks the `> translation_of: tr/<file>.md` header, if that header points to a page that doesn't exist, or if a Turkish page has no English mirror.
- **Code** (`platform`): a separate contributing guide will live in that repository.
- **Proposing a decision**: via a new ADR ([decisions/README.md](../decisions/README.md)).

# Skills Audit & Categorization

**Audit Date**: 2026-02-25
**Purpose**: Categorize 32 existing skills for reorganization into hierarchical structure

---

## Current State

**Total Skills**: 32
**Current Structure**: Flat (all in `.opencode/skills/`)
**Problem**: Hard to discover, no semantic grouping, doesn't scale

---

## Proposed Categories

```
.opencode/skills/
├── mcp/              # Skills using MCP servers (2 skills)
├── recherche/        # Legal research skills (11 skills)
├── analyse/          # Analysis skills (0 skills - TO BE CREATED)
├── redaction/        # Drafting skills (0 skills - TO BE CREATED)
├── production/       # Document production (4 skills)
└── anthropic/        # Generic Anthropic/Claude skills (15 skills - NON-LEGAL)
```

---

## Skills by Category

### 1. MCP Category (2 skills)

**Skills that use MCP servers for data access**

| Skill | Description | MCP Server Used | Keep? |
|-------|-------------|-----------------|-------|
| `swiss-case-law-research` | Search Swiss court decisions using Entscheidsuche | Entscheidsuche | ✅ YES |
| `swiss-legal-commentary` | Search legal commentaries | Onlinekommentar | ✅ YES |

**Total**: 2 skills
**Status**: Both operational after P0 validation

---

### 2. Recherche Category (11 skills)

**Legal research methodology and source navigation**

| Skill | Description | Type | Keep? |
|-------|-------------|------|-------|
| `recherche-juridique-suisse` | META skill - Navigation hub (MOC) for all research | MOC | ✅ YES (P1) |
| `outils-recherche-juridique` | Technical tools (MCP, CLI, APIs) for legal research | Transversal | ✅ YES |
| `bases-donnees-juridiques` | Guide to Swiss legal databases (Fedlex, bger.ch, Lexfind) | Guide | ✅ YES |
| `jurisprudence-suisse` | Swiss case law structure (ATF, ATAF, TPF, cantonal) | Guide | ✅ YES |
| `sources-legislatives-federales` | Federal legislation (RS, RO, FF, travaux préparatoires) | Guide | ✅ YES |
| `sources-cantonales` | Cantonal legislation and concordats | Guide | ✅ YES |
| `sources-doctrinales` | Legal doctrine (books, articles, commentaries) | Guide | ✅ YES |
| `droit-international-suisse` | International law (treaties, CEDH, bilateral agreements) | Guide | ✅ YES |
| `citation-juridique-suisse` | Swiss legal citation conventions | Guide | ✅ YES |
| `techniques-recherche-juridique` | Search techniques (truncation, proximity, multilingual) | Methodology | ✅ YES |
| `methodologie-recherche-jurisprudentielle` | Case law research methodology (5-step systematic method) | Methodology | ✅ YES |
| `terminologie-juridique-multilingue` | Multilingual legal terminology (Jurivoc, Termdat) | Tools | ✅ YES |
| `veille-juridique` | Legal monitoring and alerts (RSS, Google Alerts) | Tools | ✅ YES |

**Total**: 13 skills (including META)
**Status**: Well-developed, most updated recently

---

### 3. Analyse Category (0 skills)

**Skills for legal case analysis and reasoning**

**To Be Created**:
- [ ] `analyse-cas-structuree` - Structured case decomposition (facts → law → reasoning)
- [ ] `analyse-recevabilite` - Admissibility analysis (TF appeals)
- [ ] `analyse-jurisprudence-pertinente` - Relevant case law identification
- [ ] `verification-delais` - Deadline verification (procedural)
- [ ] `analyse-element-fait` - Factual element analysis
- [ ] `qualification-juridique` - Legal qualification of facts

**Total**: 0 skills (all P2 priority)
**Status**: To be created in Phase 3 (Weeks 5-6)

---

### 4. Rédaction Category (0 skills)

**Skills for legal document drafting**

**To Be Created**:
- [ ] `recours-tf` - Generate Federal Court appeals (P1 - TOP PRIORITY)
- [ ] `avis-droit` - Generate legal opinions / Gutachten (P1)
- [ ] `memoire-reponse` - Generate response briefs (P2)
- [ ] `conclusions` - Generate conclusions (principales et subsidiaires) (P2)
- [ ] `courrier-client` - Generate client communications (P2)
- [ ] `requete-mesures-provisionnelles` - Generate provisional measures requests (P3)
- [ ] `observations-ecriture` - Generate observations on opponent's briefs (P3)

**Total**: 0 skills (mix of P1/P2/P3)
**Status**: To be created in Phase 3-4 (Weeks 5-7)

---

### 5. Production Category (4 skills)

**Document format conversion and generation**

| Skill | Description | Format | Keep? |
|-------|-------------|--------|-------|
| `docx` | Word document creation/editing | .docx | ✅ YES (critical for legal docs) |
| `pdf` | PDF manipulation (merge, split, extract) | .pdf | ✅ YES (legal filings) |
| `pptx` | PowerPoint presentations | .pptx | ⚠️ MAYBE (low priority for lawyers) |
| `xlsx` | Excel spreadsheet manipulation | .xlsx | ⚠️ MAYBE (for cost tables, damages calculations) |

**Total**: 4 skills
**Status**: Keep docx + pdf, evaluate pptx/xlsx usage

---

### 6. Anthropic Category (15 skills - NON-LEGAL)

**Generic Claude/Anthropic skills not specific to legal work**

| Skill | Description | Relevance to Legal Work | Keep? |
|-------|-------------|------------------------|-------|
| `algorithmic-art` | p5.js generative art | ❌ No | 🗑️ DELETE |
| `brand-guidelines` | Anthropic brand colors/typography | ❌ No | 🗑️ DELETE |
| `canvas-design` | Visual art / poster creation | ❌ No | 🗑️ DELETE |
| `doc-coauthoring` | Documentation co-authoring workflow | ⚠️ Maybe (for legal memos) | ⚠️ EVALUATE |
| `frontend-design` | Web UI design | ❌ No | 🗑️ DELETE |
| `internal-comms` | Internal communications writing | ❌ No | 🗑️ DELETE |
| `mcp-builder` | Build MCP servers | ✅ Yes (for extending legal tools) | ✅ KEEP |
| `skill-creator` | Create new skills | ✅ Yes (for building legal skills) | ✅ KEEP |
| `slack-gif-creator` | Animated GIFs for Slack | ❌ No | 🗑️ DELETE |
| `theme-factory` | Styling artifacts with themes | ❌ No | 🗑️ DELETE |
| `web-artifacts-builder` | React/Tailwind web artifacts | ❌ No | 🗑️ DELETE |
| `webapp-testing` | Playwright webapp testing | ❌ No | 🗑️ DELETE |
| `workspace-guide` | OpenWork onboarding | ❌ No | 🗑️ DELETE |

**Total**: 15 skills
**Keep**: 2 skills (mcp-builder, skill-creator)
**Delete**: 11 skills (not relevant to legal work)
**Evaluate**: 2 skills (doc-coauthoring, maybe useful for legal memos)

---

## Reorganization Plan

### Phase 1: Backup Current Structure

```bash
# Create backup before reorganization
cp -r .opencode/skills .opencode/skills.backup.2026-02-25
```

### Phase 2: Create New Directory Structure

```bash
mkdir -p .opencode/skills/{mcp,recherche,analyse,redaction,production,anthropic}
```

### Phase 3: Move Skills

**MCP skills** (2):
```bash
mv swiss-case-law-research mcp/
mv swiss-legal-commentary mcp/
```

**Recherche skills** (13):
```bash
mv recherche-juridique-suisse recherche/
mv outils-recherche-juridique recherche/
mv bases-donnees-juridiques recherche/
mv jurisprudence-suisse recherche/
mv sources-legislatives-federales recherche/
mv sources-cantonales recherche/
mv sources-doctrinales recherche/
mv droit-international-suisse recherche/
mv citation-juridique-suisse recherche/
mv techniques-recherche-juridique recherche/
mv methodologie-recherche-jurisprudentielle recherche/
mv terminologie-juridique-multilingue recherche/
mv veille-juridique recherche/
```

**Production skills** (4):
```bash
mv docx production/
mv pdf production/
mv pptx production/  # evaluate later if needed
mv xlsx production/  # evaluate later if needed
```

**Anthropic skills** (2 to keep):
```bash
mv mcp-builder anthropic/
mv skill-creator anthropic/
```

**Delete irrelevant skills** (11):
```bash
rm -rf algorithmic-art brand-guidelines canvas-design frontend-design
rm -rf internal-comms slack-gif-creator theme-factory web-artifacts-builder
rm -rf webapp-testing workspace-guide
```

**Evaluate later** (1):
```bash
mv doc-coauthoring anthropic/  # keep for now, evaluate usage
```

### Phase 4: Update References

**Files to update**:
1. `SKILLS_GUIDE.md` - Update paths and add category index
2. `PROJECT.md` - Update skill references
3. `TODO.md` - Update skill creation tasks
4. Any skill that references another skill (cross-references)

**Pattern**:
- Old: `@recherche-juridique-suisse`
- New: `@recherche/recherche-juridique-suisse` (OR keep @mention unchanged if OpenCode resolves recursively)

### Phase 5: Test Skill Loading

```bash
# Test each category
ls .opencode/skills/mcp/
ls .opencode/skills/recherche/
ls .opencode/skills/production/
ls .opencode/skills/anthropic/
```

---

## Summary Statistics

### Before Reorganization

- **Total**: 32 skills
- **Structure**: Flat
- **Legal-specific**: 17 skills (53%)
- **Generic/Anthropic**: 15 skills (47%)

### After Reorganization

- **Total**: 21 skills (11 deleted)
- **Structure**: Hierarchical (6 categories)
- **Legal-specific**: 19 skills (90%)
- **Generic/Anthropic**: 2 skills (10% - only dev tools)

**Reduction**: -34% skills (removed clutter)
**Legal Focus**: +37% legal-specific proportion

---

## Category Size Projections

**After Phase 3 (All Skills Created)**:

| Category | Current | Planned | Total | Notes |
|----------|---------|---------|-------|-------|
| `mcp/` | 2 | +0 | 2 | Stable (1 per MCP server) |
| `recherche/` | 13 | +0 | 13 | Complete (comprehensive coverage) |
| `analyse/` | 0 | +6 | 6 | To be created (P2) |
| `redaction/` | 0 | +7 | 7 | To be created (P1-P3) |
| `production/` | 4 | +0 | 4 | Stable (docx/pdf core, pptx/xlsx optional) |
| `anthropic/` | 2 | +0 | 2 | Minimal (only dev tools) |
| **TOTAL** | **21** | **+13** | **34** | Focused, organized, scalable |

---

## Migration Risks

### Low Risk ✅

- Moving skills to new directories (preserves content)
- Deleting irrelevant skills (not used in legal workflows)
- Updating SKILLS_GUIDE.md (documentation only)

### Medium Risk ⚠️

- Updating skill cross-references (may break @mentions)
- Testing OpenCode skill resolution (does it follow subdirectories?)
- Git history preservation (use `git mv` instead of `mv`)

### Mitigation

1. **Backup first**: `cp -r .opencode/skills .opencode/skills.backup.2026-02-25`
2. **Use git mv**: Preserves history (better than `mv` then `git add`)
3. **Test after each category**: Verify skill loading works
4. **Update references incrementally**: Don't break everything at once

---

## Next Steps

**Immediate (This Session)**:
1. ✅ Audit complete - 32 skills categorized
2. Create backup of current structure
3. Create new directory structure
4. Move skills to new categories (use `git mv`)
5. Delete irrelevant skills
6. Update SKILLS_GUIDE.md with new structure

**After Reorganization (Next Session)**:
1. Test skill loading (@mention resolution)
2. Update cross-references between skills
3. Update PROJECT.md and TODO.md references
4. Commit reorganization with detailed message

---

## Decision Log Reference

**Related Decisions**:
- Decision 7: Hierarchical Skill Structure (DECISIONS.md)
- Decision 8: META Legal Research Skill as Navigation Hub (DECISIONS.md)

**Rationale**: Matches user mental model (research → analyze → draft), scales to 100+ skills

---

**Document Version**: 1.0
**Last Updated**: 2026-02-25
**Next Review**: After reorganization complete

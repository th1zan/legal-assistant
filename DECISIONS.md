# Strategic Decisions Log

**Project**: SwissLawAI - Legal Assistant Framework for Swiss Lawyers
**Created**: 2026-02-25
**Purpose**: Document all strategic decisions, trade-offs, and architectural choices for project continuity

---

## Table of Contents

1. [Project Scope & Vision](#project-scope--vision)
2. [Architectural Decisions](#architectural-decisions)
3. [Technical Stack Decisions](#technical-stack-decisions)
4. [Skill Organization](#skill-organization)
5. [MCP Integration](#mcp-integration)
6. [Document Production](#document-production)
7. [Priority Framework](#priority-framework)

---

## Project Scope & Vision

### Decision 1: Target 80% of Repetitive Legal Tasks

**Date**: 2026-02-25
**Context**: Initial project scoping - deciding what level of automation to aim for
**Decision**: Focus on automating 80% of repetitive legal tasks for Swiss lawyers (civil/admin/criminal litigation and advisory)
**Rationale**: 
- 80/20 rule: 80% of value comes from automating the most common tasks
- Remaining 20% requires deep legal expertise and cannot be automated
- Balances ambition with feasibility

**Alternatives Considered**:
- 100% automation: Not realistic, requires AGI-level reasoning
- 50% automation: Too conservative, misses major efficiency gains

**Trade-offs**: 
- **Sacrificed**: Complete automation of all legal work
- **Gained**: Realistic scope, faster time-to-value, focus on high-impact areas

**Impact**: Defines clear boundaries for what skills/features to build
**Revisit**: When AI capabilities significantly improve (AGI-level reasoning)

---

### Decision 2: Open Source Framework

**Date**: 2026-02-25
**Context**: Deciding on licensing and distribution model
**Decision**: Build as open-source framework with modular architecture
**Rationale**:
- Enables community contributions and improvements
- Increases trust (legal professionals can audit code)
- Modular design allows lawyers to customize for their needs
- Aligns with scientific research values (SSDI standards)

**Alternatives Considered**:
- Proprietary SaaS: Limits adoption, reduces transparency
- Closed-source with API: Still limits customization

**Trade-offs**:
- **Sacrificed**: Potential commercial exclusivity
- **Gained**: Community trust, faster adoption, academic credibility

**Impact**: All code must follow SSDI standards, use permissive licenses
**Revisit**: N/A - core value proposition

---

## Architectural Decisions

### Decision 3: Three-Layer Architecture (Skills → Agents → MCP)

**Date**: 2026-02-25
**Context**: Designing system architecture for modularity and extensibility
**Decision**: Adopt three-layer architecture:
1. **Skills** (Domain-specific workflows and instructions)
2. **Agents** (Specialized AI agents with tool access)
3. **MCP Servers** (External data sources via Model Context Protocol)

**Rationale**:
- **Skills**: Reusable, shareable, version-controlled workflows
- **Agents**: Task-specific AI with specialized tools
- **MCP**: Standardized integration with legal databases

**Alternatives Considered**:
- Monolithic system: Hard to maintain, not modular
- Direct API integration: Tight coupling, harder to swap data sources

**Trade-offs**:
- **Sacrificed**: Initial simplicity (more layers = more complexity)
- **Gained**: Modularity, testability, extensibility, maintainability

**Impact**: All features must be built as Skills, with optional Agent/MCP support
**Revisit**: If MCP protocol becomes obsolete or better alternatives emerge

---

### Decision 4: Hybrid Markdown + Word Approach

**Date**: 2026-02-25
**Context**: Deciding on document format for legal drafting
**Decision**: Use Markdown (Obsidian) for editing + Word (.docx) export for final deliverables
**Rationale**:
- **Markdown**: Version control, easy editing, AI-friendly format
- **Word export**: Required by Swiss courts and law firms
- **Hybrid approach**: Best of both worlds

**Alternatives Considered**:
- Pure Markdown: Not accepted by courts
- Pure Word: Harder to version control, less AI-friendly
- LaTeX: Too technical for lawyers, overkill for most documents

**Trade-offs**:
- **Sacrificed**: Single unified format
- **Gained**: Developer-friendly editing + legal profession compatibility

**Impact**: Need to build Markdown → Word conversion with template support
**Revisit**: If courts start accepting Markdown/PDF natively

---

## Technical Stack Decisions

### Decision 5: Python + FastMCP for MCP Servers

**Date**: 2026-02-25
**Context**: Choosing implementation language for MCP servers
**Decision**: Use Python with FastMCP framework
**Rationale**:
- Python: Team expertise, strong NLP/legal libraries
- FastMCP: Official Anthropic framework, type-safe, well-documented
- Async support: Required for responsive MCP servers

**Alternatives Considered**:
- TypeScript/Node.js: Good MCP support but less legal library ecosystem
- Rust: Fastest but steeper learning curve, fewer legal libraries

**Trade-offs**:
- **Sacrificed**: Maximum performance (Rust would be faster)
- **Gained**: Faster development, better library ecosystem, team familiarity

**Impact**: All MCP servers written in Python with FastMCP
**Revisit**: N/A - stable choice

---

### Decision 6: Fedlex SPARQL CLI for Federal Legislation

**Date**: 2026-02-25
**Context**: Choosing access method for Swiss federal laws (Recueil systématique)
**Decision**: Build CLI tool using Fedlex SPARQL endpoint (9000+ laws)
**Rationale**:
- Official data source (admin.ch)
- Structured data (RDF/SPARQL)
- Direct access without scraping
- Complete legislative history available

**Alternatives Considered**:
- Web scraping Fedlex website: Fragile, rate-limited, against ToS
- Manual downloads: Not scalable, requires constant updates
- Third-party APIs: Costs money, less complete

**Trade-offs**:
- **Sacrificed**: Simple REST API (SPARQL is more complex)
- **Gained**: Official data, complete coverage, legislative history

**Impact**: Created `scripts/fedlex_sparql.py` in outils-recherche-juridique skill
**Revisit**: If Fedlex launches official REST API

---

## Skill Organization

### Decision 7: Hierarchical Skill Structure

**Date**: 2026-02-25
**Context**: Organizing 32+ skills for maintainability
**Decision**: Reorganize skills into 6 categories:
- `mcp/` - Skills using MCP servers
- `recherche/` - Legal research skills
- `analyse/` - Case/legal analysis skills
- `redaction/` - Document drafting skills
- `production/` - Document generation (docx, pdf)
- `anthropic/` - Generic Claude skills (not legal-specific)

**Rationale**:
- Clear separation of concerns
- Easy to find relevant skills
- Scales to 100+ skills
- Matches user mental model (research → analyze → draft)

**Alternatives Considered**:
- Flat structure: Doesn't scale beyond 20 skills
- Feature-based: Hard to categorize cross-cutting skills
- Alphabetical: No semantic grouping

**Trade-offs**:
- **Sacrificed**: Simplicity of flat structure
- **Gained**: Scalability, discoverability, logical organization

**Impact**: All existing skills will be moved to new structure
**Revisit**: If categories become too large (>15 skills each)

---

### Decision 8: META Legal Research Skill as Navigation Hub

**Date**: 2026-02-25
**Context**: Deciding how to orchestrate multiple research skills
**Decision**: Create `recherche-juridique-suisse` as META skill (MOC - Map of Content) that routes to specialized skills
**Rationale**:
- User asks one question, META skill decides which specialized skills to use
- Reduces cognitive load (user doesn't need to know all skills)
- Enables complex multi-source research workflows
- Follows MOC pattern (Zettelkasten methodology)

**Alternatives Considered**:
- User manually invokes multiple skills: Tedious, error-prone
- Monolithic research skill: Too large, hard to maintain

**Trade-offs**:
- **Sacrificed**: Direct skill invocation (adds routing layer)
- **Gained**: Simplified UX, orchestration capability, extensibility

**Impact**: META skill is P1 priority (1st to build)
**Revisit**: N/A - proven pattern

---

## MCP Integration

### Decision 9: Two MCP Servers (Entscheidsuche + Onlinekommentar)

**Date**: 2026-02-25
**Context**: Selecting Swiss legal databases for MCP integration
**Decision**: Integrate two MCP servers:
1. **Entscheidsuche** - Swiss case law (Tribunal fédéral + cantonal courts)
2. **Onlinekommentar** - Legal commentaries and doctrine

**Rationale**:
- Entscheidsuche: Largest free Swiss case law database
- Onlinekommentar: High-quality legal commentaries
- Both have structured APIs suitable for MCP
- Covers two of three main legal sources (case law + doctrine)

**Alternatives Considered**:
- Swisslex: Expensive, requires subscription
- Lexfind: Good but less complete than Entscheidsuche
- Manual web scraping: Fragile, ethically questionable

**Trade-offs**:
- **Sacrificed**: Premium databases (Swisslex, WEKO)
- **Gained**: Free access, stable APIs, good coverage

**Impact**: MCP validation is P0 (prerequisite for everything)
**Revisit**: If better free databases emerge or budget allows premium access

---

### Decision 10: Performance Target <2s for MCP Queries

**Date**: 2026-02-25
**Context**: Setting performance requirements for MCP servers
**Decision**: Target <2 seconds response time for typical MCP queries
**Rationale**:
- 2s is UX threshold for "feeling responsive"
- Legal research requires iterative queries (10-20 per session)
- Longer than 2s × 10 queries = frustrating user experience

**Alternatives Considered**:
- <1s: Too aggressive, may require caching that complicates architecture
- <5s: Too slow for interactive research

**Trade-offs**:
- **Sacrificed**: Real-time streaming results (<1s)
- **Gained**: Realistic target, allows for complex queries

**Impact**: MCP tests must include performance benchmarks
**Revisit**: If user feedback indicates 2s is too slow/fast

---

## Document Production

### Decision 11: Top 5 Priority Documents

**Date**: 2026-02-25
**Context**: Deciding which legal documents to prioritize for automation
**Decision**: Focus on these 5 documents (in priority order):
1. **Recours au Tribunal fédéral** (Federal Court appeals)
2. **Avis de droit / Gutachten** (Legal opinions)
3. **Mémoire de réponse/réplique** (Response briefs)
4. **Conclusions** (principales et subsidiaires)
5. **Mail/Courrier client** (Client communications)

**Rationale**:
- Based on user's law firm experience (most common requests)
- #1 (TF appeals) is highly structured, good for automation
- #2-4 are core litigation documents
- #5 has highest volume but lowest complexity

**Alternatives Considered**:
- All document types: Too broad, dilutes focus
- Only TF appeals: Too narrow, misses 80% of daily work

**Trade-offs**:
- **Sacrificed**: Comprehensive document coverage
- **Gained**: Focus on high-impact documents, faster delivery

**Impact**: Drafting skills should be built in this priority order
**Revisit**: After MVP launch, based on user usage data

---

### Decision 12: Word Template Update Mechanism

**Date**: 2026-02-25
**Context**: Law firms have their own Word templates (.dotx files) with branding
**Decision**: Build template management system:
- Store templates in `/templates/` directory
- Allow user to upload/replace templates
- Merge AI-generated content with template styles
- Preserve template headers/footers/formatting

**Rationale**:
- Each law firm has unique branding requirements
- Templates change over time (new logos, addresses, etc.)
- Cannot hardcode templates (not flexible enough)

**Alternatives Considered**:
- Hardcoded templates: Not reusable across firms
- No templates (plain Word): Unprofessional output
- Cloud template service: Adds dependency, privacy concerns

**Trade-offs**:
- **Sacrificed**: Simplicity (no template management needed)
- **Gained**: Professional output, reusability, privacy

**Impact**: Need to build template upload/merge functionality
**Revisit**: If too complex, simplify to basic styling

---

## Priority Framework

### Decision 13: Three-Tier Priority System (P0/P1/P2/P3)

**Date**: 2026-02-25
**Context**: Managing 49+ tasks across 8 weeks
**Decision**: Use priority tiers:
- **P0 (CRITICAL)**: MCP validation - blocks everything else
- **P1 (High)**: Research skills - core value proposition
- **P2 (Medium)**: Analysis & drafting - high value but dependent on P1
- **P3 (Low)**: Medical/specialized skills - defer to future

**Rationale**:
- Clear dependency chain: P0 → P1 → P2 → P3
- Focus on unblocking critical path first
- Allows for parallel work within each tier

**Alternatives Considered**:
- Flat priority: Hard to sequence dependent tasks
- Many tiers (P0-P5): Too granular, decision paralysis

**Trade-offs**:
- **Sacrificed**: Working on "fun" tasks first
- **Gained**: Clear sequencing, no blocked tasks

**Impact**: All planning uses this priority framework
**Revisit**: N/A - standard project management practice

---

### Decision 14: 8-Week MVP Timeline (5 Phases)

**Date**: 2026-02-25
**Context**: Setting realistic timeline for first usable version
**Decision**: 8-week timeline with 5 phases:
- **Phase 1** (Weeks 1-2): Validation & Infrastructure
- **Phase 2** (Weeks 3-4): Research Skills Improvement
- **Phase 3** (Weeks 5-6): Analysis & Drafting Skills
- **Phase 4** (Week 7): Medical Skills (deferred to P3)
- **Phase 5** (Week 8): Case Infrastructure

**Rationale**:
- 8 weeks is long enough for MVP, short enough to maintain momentum
- Phases follow dependency chain (infra → research → drafting)
- Allows for 1-week buffer if delays occur

**Alternatives Considered**:
- 4 weeks: Too aggressive, would sacrifice quality
- 16 weeks: Too long, risk losing momentum

**Trade-offs**:
- **Sacrificed**: Perfection (MVP won't have all features)
- **Gained**: Fast feedback loop, early user testing

**Impact**: All tasks scheduled according to this timeline
**Revisit**: At end of Phase 1 (reassess based on progress)

---

## Execution Methodology

### Decision 15: Parallel Execution (Option C)

**Date**: 2026-02-25
**Context**: Deciding how to execute multiple tasks efficiently
**Decision**: Execute tasks in parallel where possible:
- Create DECISIONS.md
- Test MCP connections (Entscheidsuche + Onlinekommentar)
- Audit and reorganize existing 32 skills

**Rationale**:
- Tasks are independent (no blocking dependencies)
- Faster completion (days instead of weeks)
- User explicitly requested "everything in parallel"

**Alternatives Considered**:
- **Option A (Sequential)**: Slower, but simpler
- **Option B (MCP-first, then skills)**: Partially parallel

**Trade-offs**:
- **Sacrificed**: Simplicity of sequential execution
- **Gained**: Speed, efficiency, momentum

**Impact**: Must carefully manage git branches and avoid conflicts
**Revisit**: N/A - already executing

---

## Future Decisions to Document

**Placeholder for upcoming decisions:**
- [ ] Choice of Word → Markdown conversion library (python-docx vs. others)
- [ ] Caching strategy for MCP queries (Redis vs. in-memory)
- [ ] Test case management (fictional vs. anonymized real cases)
- [ ] Citation format standards (when to cite ATF vs. full TF decision)
- [ ] Error handling strategy for MCP timeouts/failures
- [ ] Multilingual support (FR/DE/IT) - when and how much?
- [ ] User authentication (if deploying as web service)
- [ ] Analytics/telemetry (what usage data to collect, if any)

---

## Decision Review Schedule

**Review this document**:
- ✅ After each major milestone (Phase 1, 2, 3 completion)
- ✅ When a decision proves incorrect (document why and new decision)
- ✅ Before major architecture changes
- ✅ Monthly (standing review during project)

**Last reviewed**: 2026-02-25 (initial creation)
**Next review**: End of Phase 1 (Week 2)

---

## How to Use This Document

**For AI Agents**:
- Read this document at start of each session for context
- Reference decisions when making implementation choices
- Update this document when new strategic decisions are made
- Flag contradictions between decisions and current approach

**For Human Users**:
- Use as reference when onboarding new team members
- Cite decisions when discussing architecture
- Update when pivoting strategy
- Archive outdated decisions (mark as [DEPRECATED])

**For Future Self**:
- Understand why things were built this way
- Avoid repeating past mistakes
- Accelerate onboarding on return to project
- Maintain continuity across long breaks

---

## Related Documentation

- **TODO.md**: Task tracking and weekly planning
- **PROJECT.md**: Detailed project specification
- **GROK.md**: Brainstorming and exploration
- **MCP_TOOLS_REFERENCE.md**: MCP server API reference
- **SKILLS_GUIDE.md**: How to use and build skills
- **AGENTS.md**: Agent-specific context (if created)

# Engineering Lessons

## 2026-08-27 — Respect domain-specific data constraints

When a stakeholder refines the intended market or data domain, update the implementation plan and use the refinement consistently in sample data, examples, tests, and documentation. Do not retain generic data defaults that weaken the product's local relevance.

## 2026-08-27 — Match implementation complexity to the author

For interview or learning projects, prefer constructs the project owner can explain confidently. Avoid introducing advanced immutable collections, regular expressions, or compact standard-library helpers when a readable list, loop, or basic string operation meets the requirement. Document both the implementation and the reasoning in beginner-friendly language.

## 2026-08-27 — Test documented commands from their stated directory

For a Python package nested inside a repository, verify each README command from the repository root and from any documented subdirectory. State the working-directory requirement clearly and provide a root-level module command when practical.

## 2026-08-28 — Match the requested document scope

When a case study asks for a short approach/decision/trade-off document, keep it executive-readable and separate from implementation tutorials. Do not let a helpful technical guide replace the requested concise submission artifact.

## 2026-08-29 — Match the requested deliverable format and depth

When a user asks for a code-first, PDF-only implementation guide, include runnable source code in the PDF itself and avoid producing a separate Markdown guide. Confirm whether explanation alone is sufficient before omitting executable examples.

# LocalBuka AI Engineer Case Study — Implementation Plan

## Scope and design

- [x] Create an isolated `localbuka_case_study/` project at the repository root.
- [x] Model 20+ realistic, Nigeria-first restaurants/dishes (primarily Nigerian cuisines and Nigerian locations, plus a small continental selection) with location, cuisine, price, dietary, spice, and popularity attributes.
- [x] Implement an explainable, deterministic ranking engine that validates user inputs, applies hard dietary constraints, scores preference matches, and returns ranked recommendations with score explanations.
- [x] Implement a safe command-line conversational assistant that extracts supported preferences from free text, asks a focused follow-up when it cannot make a useful recommendation, and only reports facts stored in the catalogue.
- [x] Add at least three executable recommendation scenarios and capture their rendered results.
- [x] Add unit tests for ranking, dietary exclusions, preference differences, parsing, and safe fallback behavior.
- [x] Write a project README with installation, commands, outputs, design decisions, evaluation and million-user scaling plan.
- [x] Write the required 1–2-page reflection in Markdown, including production safeguards, cost controls, an AI-product risk mitigation, and a clearly labeled adaptable debugging example.
- [x] Run the test suite and demos; record verification results below.
- [x] Replace advanced collection and regex usage with beginner-explainable Python; provide a concise implementation summary.
- [x] Support and document running the CLI from the repository root as a Python module.
- [x] Replace local ranking with Gemini embeddings and Pinecone semantic retrieval while retaining hard metadata safety checks.
- [x] Add a secure ingestion command, dependency setup, mocked unit tests, and refreshed case-study documentation for the Gemini/Pinecone workflow.
- [x] Replace the reflection's debugging placeholder with the candidate's verified DataLab vector-dimension debugging experience.
- [x] Create and verify a comprehensive PDF technical interview guide for the LocalBuka project.
- [x] Create and verify a step-by-step LocalBuka build-from-scratch PDF guide.

## Planned structure

```text
localbuka_case_study/
├── localbuka/
│   ├── data.py                 # curated sample catalogue
│   ├── models.py               # typed domain models
│   ├── recommender.py          # ranking and explanations
│   ├── assistant.py            # deterministic CLI chat layer
│   └── cli.py                  # interactive entry point
├── tests/
├── README.md
├── REFLECTION.md
├── requirements.txt
└── results.md
```

## Review / verification

- `python3 -m unittest discover -s tests -v` — 8 tests passed.
- `python3 run_examples.py` — three distinct, captured recommendation scenarios rendered successfully.
- Manual CLI smoke test — verified a “spicy and cheap near me” request uses the supplied Lagos location and returns catalogue-backed options.
- Review adjustments: maximum price and explicit city are enforced as hard eligibility constraints, so expensive or out-of-city dishes cannot be ranked for a constrained request.
- Simplification review: removed `frozenset`, regular expressions, `Counter`, and set-comprehension logic. Replaced them with ordinary lists, dictionaries, loops, and basic substring checks. Verified with 8 passing tests, all three examples, and a CLI smoke test on Python 3.9.
- CLI-path verification: `/Users/macbook1/Documents/INIE/DATACAMP/venv/bin/python3 -m localbuka_case_study.localbuka.cli` runs successfully from `AI_Engineering`.
- Gemini/Pinecone verification: installed `google-genai`, created/reused `localbuka-gemini-768`, embedded and upserted all 24 dishes, ran three live examples, and verified a live Lagos budget/spicy CLI request. Offline tests use fakes and pass without external calls.
- Reflection evidence: linked the DataLab debugging account to the single-vector extraction in `analysis_reviews_embeddings.py` and the 1536-dimension Pinecone index configuration in the course material.
- Interview-guide verification: generated a five-page PDF, verified its extracted headings and page count, and visually reviewed the first page after fixing code-block and diagram rendering.
- Build-guide verification: generated a five-page PDF, checked its required build steps/text extraction, visually reviewed its opening page, and removed literal Markdown emphasis markers from both PDF renderers.
- Build-guide correction: replaced the explanation-only PDF with a 16-page code-first PDF containing the actual implementation files in build order; removed the separate Markdown build guide and visually verified a code-heavy page.

# LocalBuka AI Engineer Case Study

LocalBuka is a Nigeria-first restaurant-discovery prototype. It uses Gemini embeddings to represent dish descriptions as vectors and Pinecone to retrieve dishes that are semantically similar to a user's free-text request. The catalogue contains 24 realistic Nigerian and continental dishes across Nigerian cities.

## Architecture

```text
Dish catalogue → Gemini embeddings → Pinecone index
User message → Gemini embedding → Pinecone semantic search → safe checks → CLI response
```

Each dish is converted to text containing its name, restaurant, city, cuisine, budget, dietary tags, spice level, and description. Gemini's `gemini-embedding-2` model converts each text to a 768-dimensional vector. Pinecone stores that vector plus metadata.

At search time, the user's message becomes another vector. Pinecone uses cosine similarity to find semantically related dishes. City, cuisine, and maximum-price metadata filters are applied in Pinecone before results are returned. The application then checks dietary tags again locally before displaying results. This defence-in-depth check means a bad or stale index record cannot bypass a stated dietary restriction.

## Setup

Use Python 3.11+ and a virtual environment. From the repository root (`AI_Engineering`):

```bash
/Users/macbook1/Documents/INIE/DATACAMP/venv/bin/python3 -m pip install -r localbuka_case_study/requirements.txt
```

Create a root `.env` file. Do not commit it:

```env
GEMINI_API_KEY=your_gemini_key
PINECONE_API_KEY=your_pinecone_key
```

The code loads these values locally and never prints them.

## Run the project

Run the one-time ingestion command first. It creates or reuses the `localbuka-gemini-768` Pinecone index and embeds/upserts all 24 dishes. Re-run it whenever `data.py` changes.

```bash
python3 -m localbuka_case_study.ingest
```

Start the chat assistant:

```bash
python3 -m localbuka_case_study.localbuka.cli
```

Enter a city such as `Lagos`, then try:

```text
I want something spicy and cheap near me
Show me vegan Nigerian food in Abuja
I want mild continental food in Lagos
```

Run the three required sample cases:

```bash
python3 -m localbuka_case_study.run_examples
```

Run offline unit tests; these use fakes and do not call Gemini or Pinecone:

```bash
cd localbuka_case_study
python3 -m unittest discover -s tests -v
```

## Design choices and trade-offs

Embeddings are a better fit than exact keyword matching when a user expresses a food preference in different words from the menu. They capture similarity between a request such as “peppery grilled meat” and a dish description such as suya. Pinecone keeps search fast once the catalogue grows beyond a small Python list.

This adds API cost, indexing work, and a dependency on two external services. For a 24-item static catalogue, the former rule-based version was cheaper and sufficient. I chose the embedding approach here because it directly demonstrates semantic retrieval and a realistic vector-database architecture.

## Evaluation and scale

I would evaluate offline with Recall@K, NDCG@K, cuisine/merchant coverage, and zero dietary/price-constraint violations. In a gradual A/B test, I would monitor search-to-menu click-through, add-to-cart and completed-order rate, explicit “not relevant” feedback, latency, no-result rate, and merchant exposure balance.

At one million users, I would keep current menu facts in a source-of-truth database and use an event pipeline for consented behavioural features. Embed new or changed menu records asynchronously, upsert them in batches, version embeddings, and monitor indexing freshness. Candidate generation would filter by live availability, location, price, and diet before semantic retrieval; a lightweight learned ranker could then use contextual features such as time of day and anonymised order affinity.

## Safety, privacy, and costs

The assistant only reports catalogue information. It does not invent opening hours, delivery coverage, addresses, or medical/allergen guarantees. Dietary metadata needs merchant validation, timestamps, and a rapid correction path. API keys stay in `.env`; never put them in code, logs, Pinecone metadata, or Git.

To control costs, embed dish records only when they change, batch or queue production ingestion, cache repeated query embeddings/results for a short time, set quotas and alerts, and use the 768-dimension output instead of the model's larger default vector where quality testing permits.

See [CASE_STUDY_EXPLANATION.md](CASE_STUDY_EXPLANATION.md) for an implementation walkthrough and [REFLECTION.md](REFLECTION.md) for the required written reflection.

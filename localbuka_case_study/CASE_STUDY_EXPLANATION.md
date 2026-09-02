# LocalBuka: Gemini Embeddings and Pinecone Walkthrough

## Run order

From the `AI_Engineering` folder, with the virtual environment active:

```bash
python3 -m pip install -r localbuka_case_study/requirements.txt
python3 -m localbuka_case_study.ingest
python3 -m localbuka_case_study.localbuka.cli
```

The first command installs `google-genai`, `pinecone`, and `python-dotenv`. The ingestion command is required once before chat: it creates/reuses the Pinecone index and loads the dish embeddings. Do not commit `.env`; it must contain `GEMINI_API_KEY` and `PINECONE_API_KEY`.

## Flow

```text
data.py dishes
    ↓ dish_to_text()
GeminiEmbedder → 768-number vector per dish
    ↓ upsert_dishes()
Pinecone index + dish metadata

CLI message → FoodAssistant parses city/budget/diet
    ↓ GeminiEmbedder embeds full message
PineconeRestaurantIndex searches similar vectors with city/cuisine/price filters
    ↓ Recommender rechecks dietary tags
CLI prints safe recommendations
```

## File-by-file explanation

### `models.py` and `data.py`

`from dataclasses import dataclass, field` creates simple classes without manually writing constructors. `Dish` holds every field for one menu record. `UserPreferences` holds the user’s optional cuisine, price, diet, spice, city, and past-order values. `Recommendation` joins a returned `Dish` with its score and explanations.

`PRICE_ORDER` maps the text price bands to `1`, `2`, and `3` so prices can be compared. The two `VALID_...` lists prevent unsupported diet or spice values. `data.py` imports `Dish`; its `dish(...)` helper creates each record, and `CATALOGUE` is the 24-item list used for ingestion.

### `embeddings.py`

Imports: `os` reads environment variables; `Path` locates the project root; `load_dotenv` reads the local `.env`; `genai` is Google’s Gemini SDK; `types` provides Gemini request configuration.

`GeminiEmbedder` is the class responsible for all Gemini calls. `MODEL_NAME` is `gemini-embedding-2`; `DIMENSION = 768` keeps the Gemini output size equal to the Pinecone index dimension. `__init__` loads `GEMINI_API_KEY`, raises a clear error if missing, and creates `self.client`. `embed_texts(texts)` loops through the list so each dish reliably produces exactly one vector; `vectors` collects the resulting `embedding.values`. `embed_one_text(text)` is the small wrapper used for a user query.

### `pine_cone.py`

Imports: `time` pauses while a newly created Pinecone index becomes ready; `Pinecone` creates the client; `ServerlessSpec` defines the AWS region.

`PineconeRestaurantIndex` owns the vector database. `INDEX_NAME`, `NAMESPACE`, and `DIMENSION` are constants used consistently for writing and reading. `__init__` loads `PINECONE_API_KEY`, creates `self.pinecone`, calls `_create_index_if_needed`, then opens `self.index`.

`_create_index_if_needed()` avoids creating an index that already exists. A new index uses cosine similarity because embeddings are compared by direction. The loop waits until Pinecone reports the index is ready.

`upsert_dishes(dishes, vectors)` loops over one dish/vector pair. `metadata` keeps the filterable facts alongside the vector. `price_rank` is numeric so Pinecone can evaluate “less than or equal to budget.” `records` is the list sent to `index.upsert`.

`search(query_vector, preferences, top_k)` creates `metadata_filter`: city and cuisine use `$in`; price uses `$lte`. Pinecone finds semantically similar vectors and applies those filters. The function returns only each match’s `id` and similarity `score`; the local catalogue remains the display source. `_price_rank` converts the price text into its number.

### `ingest.py`

`dish_to_text(dish)` makes one full searchable sentence from every relevant dish field. This is the text Gemini embeds. `main()` creates the embedder and index objects, fills `dish_texts` in a loop, gets vectors from Gemini, and calls `upsert_dishes`. Run this whenever the catalogue changes.

### `recommender.py`

`Recommender` receives the catalogue, `embedder`, and `restaurant_index`; dependency injection makes it possible to unit-test without calling APIs. `dishes_by_id` maps an ID to a `Dish` after Pinecone returns its IDs.

`recommend(query_text, preferences, limit)` validates inputs, adds past-order dish names to the query, embeds that text, retrieves up to five times the desired number of candidates, then checks diets locally. It calculates `score` from the Pinecone similarity score plus a small popularity tiebreaker. `_build_reasons` creates the explanations displayed to the user.

`_validate` checks `limit`, price, diet, and spice values. `_add_order_history` adds known historical dish names to semantic search. `_meets_dietary_requirements` loops through every requested tag and returns `False` when one is absent.

### `assistant.py` and `cli.py`

`FoodAssistant` is not an LLM. Its four dictionaries translate a small set of user words, for example `cheap → budget` and `spicy → hot`. `reply` normalises a message, guards against unsupported operational questions, gets preferences, calls the recommender, and formats results. `parse_preferences` finds supported terms. `_contains` deliberately uses basic `term in message`, not regex. The other helpers collect matched values, choose the cheapest stated price, choose spice, and remove duplicates.

`cli.py` imports the catalogue, assistant, embedder, Pinecone class, and recommender. `main()` creates them in that order, asks once for city, then continuously accepts a request at `Type what you want to eat:`. Enter `quit` or `exit` to end it.

### Tests

`tests/test_localbuka.py` uses `unittest`, Python’s built-in test library. `FakeEmbedder` and `FakeRestaurantIndex` have the same methods as the external services but make no network calls. This verifies parsing, dietary rechecking, order-history text, and query flow without charging Gemini or requiring Pinecone credentials.

## Why the safety checks exist twice

Pinecone filters city, cuisine, and maximum price before retrieval results are returned. Diet is rechecked after retrieval in `Recommender`. This prevents semantic similarity from overriding a user’s dietary restriction and protects against stale/malformed metadata. A production service should additionally validate restaurant menu data at the point it is created.

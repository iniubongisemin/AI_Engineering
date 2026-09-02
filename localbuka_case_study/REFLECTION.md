# LocalBuka Case Study Reflection

## Overall approach and decisions

I built one curated Nigeria-first catalogue of 24 dishes, then used it for both recommendation and chat. Every dish is represented as readable text containing its name, description, cuisine, city, price band, dietary tags, and spice level. During ingestion, Gemini's `gemini-embedding-2` converts every dish text into a 768-dimensional embedding. Pinecone stores the embedding with safe metadata. A user's free-text request is embedded with the same Gemini model and Pinecone returns the closest dish vectors using cosine similarity.

I chose semantic retrieval because restaurant requests are naturally expressed in varied language. Someone may ask for “peppery grilled meat” rather than explicitly type “suya.” Keyword matching can miss that connection; embeddings make it more likely that semantically related dish descriptions are found. Pinecone keeps this retrieval pattern practical as the catalogue becomes large.

Safety constraints are not left to semantic similarity. City and maximum price are Pinecone metadata filters. Dietary restrictions are checked again in Python after retrieval before a recommendation is shown. This is important because ranking should never turn an ineligible dish into a recommendation. The CLI assistant intentionally does not use a generative chat model: it extracts a small set of supported preferences and only presents facts present in the catalogue.

The trade-off is additional complexity and cost. For a 24-record demo, rules alone would be cheaper and easier to operate. This design is appropriate for the case study because it demonstrates a production-relevant embedding/retrieval path while retaining clear, testable safety rules.

## What I would build next

With more time, I would connect a validated merchant menu feed for live availability, exact pricing, delivery coverage, opening status, and ingredient-level allergen data. I would create labelled search relevance data from consented clicks/orders, evaluate Recall@K and NDCG@K, and compare semantic retrieval against a keyword baseline. At larger scale, a learning-to-rank stage could re-rank Pinecone candidates with location, time of day, popularity, and privacy-preserving order-affinity features.

I would also make ingestion event-driven: a menu update produces a new embedding, upserts it in a batch, and records the embedding model/version. Caches, quotas, retries, index-freshness alerts, and dead-letter handling would keep latency and cost controlled.

## Risk and mitigation

One serious consumer-product risk is incorrect dietary data. A restaurant recipe may change while the index still says a dish is vegan or gluten-free. A convincing AI answer would make that failure more harmful. I would require structured merchant attestations, freshness timestamps, recipe-change workflows, visible caveats, and an immediate correction/removal path. Dietary constraints should remain hard filters before and after vector retrieval; the prototype follows that principle. I would never present medical or cross-contamination guarantees from incomplete menu data.

Privacy and cost also need controls. The system should collect only consented data, minimise retention, never place user identifiers or raw chat logs in Pinecone metadata, and provide deletion controls. Gemini calls should be limited to changed menu records and user search requests; query/result caching, output-dimension evaluation, per-service budgets, and cost alerts reduce spend.

## Personal debugging experience

In a DataCamp DataLab project that analysed e-commerce review embeddings, I received a vector-dimension error while working with a vector search workflow. The problem was that I had passed an embedding value with the wrong shape or length for the operation: I was treating a collection of embeddings as though it were one query vector, and the vector did not match the dimension required by the index. I traced the issue by checking the embedding output and revisiting the course material, which showed that the Pinecone index was configured with `dimension=1536` and that every vector passed to it must contain exactly 1536 values. I also used Gemini to clarify the difference between one embedding vector and a list of embedding vectors. I fixed the implementation by selecting the single query vector needed for the search—for example, `create_embeddings(review)[0]`—and by ensuring that the index dimension and the embedding model output dimension matched. I verified the fix by rerunning the similarity search and confirming that it returned the expected nearest reviews without a dimension error.


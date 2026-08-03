import chromadb

# INSTALL USEFUL LIBRARIES
# Run this cell to install ChromaDB if desired
try:
    # assert version('chromadb') == '0.4.17'
    ...
except:
    # !pip install chromadb==0.4.17
    ...
try:
    # assert version('pysqlite3') == '0.5.2'
    ...
except:
    # !pip install pysqlite3-binary==0.5.2
    ...
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import chromadb


# LOAD THE DATASET
import pandas as pd
reviews = pd.read_csv("womens_clothing_e-commerce_reviews.csv")

# Display the first few entries
reviews.head()
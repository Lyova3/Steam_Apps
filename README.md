

---

# 🧠 MiniDB — Scalable In-Memory Data Management System


---

## 🎯 Objective

The goal of this project is to design and implement a **lightweight, scalable, in-memory database** capable of handling large datasets efficiently.
Our MiniDB supports:

* Search, insertion, deletion, modification, and range queries
* Graph-based relationships and traversal
* Analytical operations (min, max, average, top-K)
* Manual AVL Tree indexing for efficiency
* An interactive **Streamlit** UI

This project applies the core **data structures and algorithms** learned during the semester — especially **AVL Trees** and **Graph Algorithms** — to create a functional and efficient system.

---

## 📁 Folder Structure

```

│
├── main.py                         # Application entry point (launches Streamlit UI)
├── README.md                       # Project documentation
        
│
├── data/                           # Steam dataset (CSV files)
│   ├── applications.csv
│   ├── application_categories.csv
│   ├── application_developers.csv
│   ├── application_genres.csv
│   ├── application_platforms.csv
│   ├── application_publishers.csv
│   ├── categories.csv
│   ├── developers.csv
│   ├── genres.csv
│   ├── platforms.csv
│   ├── publishers.csv
│   └── reviews_final.csv
│
├── src/
│   ├── __init__.py
│   │
│   ├── storage/                    # Core storage and indexing layer
│   │   ├── avl_tree.py             # Manual AVL tree implementation
│   │   ├── data_store.py           # In-memory data store with AVL indexes
│   │   └── __init__.py
│   │
│   ├── query_engine/               # CRUD operations and range queries
│   │   ├── query_handler.py
│   │   └── __init__.py
│   │
│   ├── graph/                      # Graph-based features
│   │   ├── graph_model.py          # Adjacency-map graph implementation
│   │   ├── graph_algorithms.py     # BFS, DFS, shortest path, components
│   │   └── __init__.py
│   │
│   ├── analytics/                  # Analytics and querying UI components
│   │   ├── dataset_status.py       # Dataset loading overview
│   │   ├── indexed_engine.py       # Indexed query engine builder
│   │   ├── search_by_appid.py      # Indexed search by appid
│   │   ├── search_by_name.py       # Linear name search (subset)
│   │   ├── price_range.py          # AVL-based price range queries
│   │   ├── basic_analytics.py      # Min / max / avg / median statistics
│   │   ├── graph_explorer.py       # Graph exploration UI
│   │   └── __init__.py
│   │
│   ├── ui/                         # Streamlit frontend
│   │   ├── app.py                  # Main Streamlit application
│   │   ├── graph_explorer.py       # Advanced graph UI (slice + full modes)
│   │   └── __init__.py
│   │
│   ├── utils/                      # Utilities and data loading
│   │   ├── data_loader.py          # CSV loader and cleaner (no pandas)
│   │   ├── schemas.py              # Dataset schemas and type definitions
│   │   └── __init__.py
│   │
│   └── test_storage.py             # Storage and AVL testing
│
└── .gitignore                      # Git ignore rules


---

## 💻 Programming Languages & Libraries

**Primary Language:** Python 3.11+

**Libraries Used:**

* `streamlit` — interactive web-based user interface
* `os` — file system and path operations
* `sys` — Python path and runtime configuration
* `csv` — reading and parsing CSV dataset files
* `collections` — efficient data structures (deque, defaultdict)
* `statistics` — basic statistical calculations (e.g., median)
* `typing` — type annotations for clarity and maintainability

---

## 📊 Dataset

### Steam Dataset 2025 — Multi-Modal Gaming Analytics

📦 Source: [Kaggle Dataset Link](https://www.kaggle.com/datasets/crainbramp/steam-dataset-2025-multi-modal-gaming-analytics)

**Description:**

* ~239,000 Steam games and 1M+ user reviews
* Covers metadata, pricing, genres, ratings, platforms, and developer–publisher networks
* 13 normalized relational tables (relational and graph-ready)
* Includes 1024-dimensional vector embeddings for semantic relationships

**Why we chose it:**

* Large-scale dataset (>1,000,000 records ✅)
* Includes both **tabular** and **graph** structures (developer ↔ publisher)
* Perfect for applying range queries, AVL indexing, and graph traversal algorithms

---

# ⚙️ Project Phases

---

## 🔹 **PHASE 1: Dataset Preparation**

### Step 1.1 — Select and Load Dataset

* Download dataset CSVs from Kaggle.
* Load into `/data` folder.
* Use `pandas` to load a manageable subset initially for testing (e.g., first 50,000 rows).

### Step 1.2 — Clean and Normalize Data

* Handle missing values, drop redundant columns.
* Ensure key attributes:
  `game_id`, `title`, `price`, `rating`, `genre`, `developer`, `publisher`, `release_year`.

### Step 1.3 — Store Raw Data

* Create a list of dictionaries:

  ```python
  [{"id": 1, "title": "Portal 2", "price": 9.99, "genre": "Puzzle", ...}, ...]
  ```
* This serves as the base layer for MiniDB.

💬 *Tip:* Start small for debugging. Use only a few thousand records until AVL and queries are stable.

---

## 🔹 **PHASE 2: Storage & Indexing Layer (AVL Tree)**

### Step 2.1 — Implement Manual AVL Tree

* Implement from scratch in `avl_tree.py`.
* Include: `insert()`, `delete()`, `search()`, and rotations (`LL`, `RR`, `LR`, `RL`).
* Keep balancing logic well-commented to demonstrate understanding.

### Step 2.2 — Integrate Index with Data Store

* In `data_store.py`, connect the raw dataset with AVL-based indexing.
* Example:

  ```python
  price_index = AVLTree()
  for record in data:
      price_index.insert(record["price"], record)
  ```
* This allows fast range queries and lookups by price or rating.

### Step 2.3 — Test AVL Tree

* Test insertion and deletion performance.
* Compare with linear search for validation.
* Print in-order traversal to verify balancing.

---

## 🔹 **PHASE 3: Query Engine**

### Step 3.1 — CRUD Operations

Implement core MiniDB functions in `query_handler.py`:

* `search_record(key)`
* `insert_record(record)`
* `delete_record(key)`
* `update_record(key, field, value)`

### Step 3.2 — Range Queries

* Use AVL traversal to retrieve all records between two values.

  ```python
  results = avl.range_query(min_price=10, max_price=30)
  ```
* Return results as lists of game entries.

### Step 3.3 — Performance Testing

* Use Python’s `time` library to record operation time for each query type.
* Store results in `performance_analysis.md`.

---

## 🔹 PHASE 4: Graph Features

### **Step 4.1 — Graph Representation**

Use a custom graph implementation (no external libraries):
Nodes: Developers and Publishers
Edges: Collaboration between a developer and publisher if they worked on the same game
Edge weight: Number of shared games

### Step 4.2 — Implement Graph Algorithms

Implemented in graph_algorithms.py:
* `bfs_traversal(start_vertex)`
* `dfs_traversal(start_vertex)`
* `shortest_path(start_vertex, target_vertex)` (unweighted)
* `connected_components()` (collaboration clustering)

### Step 4.3 — Exploration (UI-Based)
*Graph exploration is done via a Streamlit interface:
  * Neighbor inspection
  * BFS / DFS traversal output
  * Connected component analysis
  * Large graphs are handled by operating on dataset subsets for performance.

## 🔹 **PHASE 5: Final Integration & UI**

### Step 5.1 — Build Streamlit UI

* File: `/src/ui/app.py`
* Allow users to:

  * Search by name, price, or rating
  * View range query results
  * Explore developer–publisher connections
  * Display analytics (e.g., average rating by genre)

### Step 5.2 — Integrate Analytics

* In `analytics.py`, implement:

  * `min_price()`, `max_price()`, `avg_rating()`, `median_price()`, `top_k_games(k)`
  * Optional: `knn_similar_games(title)` using embeddings

### Step 5.3 — System Integration

* Connect all layers (Data → AVL → Query Engine → Graph → UI).
* Test all workflows end-to-end:

  1. Load dataset
  2. Build indexes
  3. Run search and graph queries
  4. View analytics in UI




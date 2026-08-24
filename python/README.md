# Python

Python practice, one folder per topic:

- [`ai/`](ai/) — LLM practice with local models (Ollama): a RAG notebook,
  Docling document parsing, LangChain, and Pydantic AI.
- [`asyncio/`](asyncio/) — concurrency demos: coroutines, threading, and
  multitasking (multiprocessing), side by side.
- [`dsa/`](dsa/) — data structures & algorithms practice: binary search and
  LeetCode array problems.
- [`fast_api/`](fast_api/) — FastAPI practice: hello world, CRUD, request
  bodies, a SQLAlchemy-backed example API (`sql_example_api/`), a books
  CRUD API with Postgres/asyncpg, and a Flask + CSV sample with its Kafka
  broker config (`kube_west.*`).
- [`hackerrank/`](hackerrank/) — HackerRank and LeetCode practice scripts
  and notebooks (basics, strings, regex, numpy, sets, datetime).
- [`mnist_assignment/`](mnist_assignment/) — MNIST digit classification with
  Keras (`mnist.load_data()`).
- [`notebooks/`](notebooks/) — scratch notebooks: maths, statistics, and a
  PyTorch/TF comparison.
- [`oops/`](oops/) — OOP practice: classes & objects, inheritance,
  property, operator overloading, and special methods.
- [`streamlit/`](streamlit/) — small CSV dashboard demo (`main.py`, run
  with `streamlit run main.py`).
- [`time_series/`](time_series/) — onion price prediction notebook (has its
  own README with the upstream source).

Most scripts run with a recent Python 3 and a small number of packages
(`fastapi`, `uvicorn`, `torch`, `keras`, `streamlit`, `langchain`, etc.) —
see each folder for what it imports. Notebooks have outputs cleared.

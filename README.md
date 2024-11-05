# Metadata Querying Agent

This project is a querying tool that leverages LangChain and HuggingFace's Llama-2 model to answer questions about metadata from a CSV file. The metadata is extracted from a SOMA database and converted to a SQLite database, enabling flexible querying of sample metadata through a natural language interface.

## Overview

The tool:

1. Connects to a SOMA database to read observation data.
2. Converts this data into a Pandas DataFrame.
3. Stores the DataFrame in a SQLite database.
4. Uses LangChain to interact with the SQLite database and answer questions about the metadata.

## Setup

1. Install Required Libraries

```bash
pip install tiledbsoma sqlalchemy langchain_community langchain_huggingface
```

2. Set Up HuggingFace API Token

```
Sign up on Hugging Face and obtain an API token. Then set the token in your environment:
```

3. Access SOMA Database

Follow [these](https://cloud.tiledb.com/notebooks/details/Phenomic/b06350d9-f829-4eb2-9b77-5c2d20d6932d/preview) instructions to access the SOMA experiment data.

## Usage

1. Configure and Run the Script

Open the script and set the following variables:

```python
HUGGINGFACEHUB_API_TOKEN = "your_huggingface_api_token"
SOMA_EXPERIMENT_URI = "your_soma_experiment_uri"
SQLITE_DATABASE_URI = "sqlite:///corpus.db"
```

2. Run the Script

Run the script to:

- Connect to the SOMA database and retrieve observation data.
- Convert the retrieved data to a Pandas DataFrame.
- Save the DataFrame to a SQLite database.
- Initialize LangChain with the SQLite database and Llama-2 model for natural language queries.
- This should launch a web browser with an agent that you can ask questions to

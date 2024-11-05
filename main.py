import tiledbsoma as soma
import os

from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_huggingface import ChatHuggingFace
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEndpoint



os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# Querying all obs
with soma.Experiment.open("/Users/dylanmendonca/sctx/backend/src/demo_db") as exp:
    df = exp.obs.read().concat().to_pandas()

df.drop(["soma_joinid", "barcode", "cell_type_idx", "standard_true_celltype", "authors_celltype", "cell_type_pred", "cell_subtype_pred"], axis=1, inplace=True)
df.drop_duplicates(inplace=True)

# Converting dataframe to sqlite database
engine = create_engine("sqlite:///corpus.db")
df.to_sql("sample_metadata", engine, index=False, if_exists='replace')

# Intializing LangChain database
db = SQLDatabase(engine=engine)

llm = HuggingFaceEndpoint(repo_id="meta-llama/Llama-2-7b", task="text-generation", timeout=600)

agent_executor = create_sql_agent(llm, db=db, verbose=True)

agent_executor.invoke({"input": "how many samples with breast cancer are there?"})



import tiledbsoma as soma
import os

from sqlalchemy import create_engine
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import create_sql_agent
from langchain_huggingface import HuggingFaceEndpoint


HUGGINGFACEHUB_API_TOKEN = ""
SOMA_EXPERIMENT_URI = ""
SQLITE_DATABASE_URI = "sqlite:///corpus.db"

os.environ["HUGGINGFACEHUB_API_TOKEN"] = HUGGINGFACEHUB_API_TOKEN

# Querying all obs
with soma.Experiment.open(SOMA_EXPERIMENT_URI) as exp:
    df = exp.obs.read().concat().to_pandas()

# Converting dataframe to sqlite database
engine = create_engine(SQLITE_DATABASE_URI)
df.to_sql("sample_metadata", engine, index=False, if_exists="replace")

# Intializing LangChain database
db = SQLDatabase(engine=engine)

llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-2-7b", task="text-generation", timeout=600
)

agent_executor = create_sql_agent(llm, db=db, verbose=True)

agent_executor.invoke({"input": "how many samples of lung tissue are there?"})

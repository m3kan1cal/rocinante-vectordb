import os

from langchain.document_loaders import TextLoader
from langchain.llms import OpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chains import RetrievalQA
import pinecone


pinecone.init(api_key=os.environ.get("PINECONE_API_KEY"), environment="gcp-starter")

if __name__ == "__main__":
    print("Hello VectorStore!")
    loader = TextLoader(
        "/Users/mlfowler/Documents/workspaces/rocinante-vectordb/policies/policy1.txt"
    )
    document = loader.load()

    text_splitter = CharacterTextSplitter(
        separator="\n", chunk_size=1000, chunk_overlap=0
    )
    texts = text_splitter.split_documents(document)
    print(len(texts))

    embeddings = OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))
    docsearch = Pinecone.from_documents(texts, embeddings, index_name="policy-index")

    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(),
        chain_type="stuff",
        retriever=docsearch.as_retriever(),
        return_source_documents=True,
    )
    query = "What is the title of this policy and who approved it?"
    result = qa({"query": query})
    print(result)

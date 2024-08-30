from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
### from langchain_cohere import CohereEmbeddings

def vdb():
    # Set embeddings
    embd = OpenAIEmbeddings()

    # Docs to index
    urls = [
        "https://www.justice.gov/crt/statutes-enforced-criminal-section",
        "https://www.govinfo.gov/content/pkg/USCODE-2009-title18/html/USCODE-2009-title18.htm",
        "https://www.justice.gov/sites/default/files/ag/legacy/2014/03/12/apr2013-section1.pdf",
    ]

    # Load
    docs = [WebBaseLoader(url).load() for url in urls]
    docs_list = [item for sublist in docs for item in sublist]


    # Split
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=500, chunk_overlap=0
    )
    doc_splits = text_splitter.split_documents(docs_list)

    # Add to vectorstore
    vectorstore = Chroma.from_documents(
        documents=doc_splits,
        collection_name="rag-chroma",
        embedding=embd,
    )
    retriever = vectorstore.as_retriever()

    return retriever
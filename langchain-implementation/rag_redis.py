import os
from pathlib import Path
from typing import List

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Redis
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DOC_SOURCES = [
    ROOT / "_bmad-output" / "planning-artifacts" / "prd-ai-test-lifecycle-platform.md",
    ROOT / "_bmad-output" / "planning-artifacts" / "architecture-ai-test-lifecycle-platform.md",
    ROOT / "_bmad-output" / "planning-artifacts" / "epics-and-stories-ai-test-lifecycle-platform.md",
    ROOT / "_bmad-output" / "implementation-artifacts" / "all-stories-ai-test-lifecycle-platform.md",
]


def _load_documents(paths: List[Path]):
    docs = []
    for path in paths:
        if path.exists():
            loader = TextLoader(str(path), encoding="utf-8")
            docs.extend(loader.load())
    return docs


def build_redis_vectorstore(
    redis_url: str | None = None,
    index_name: str | None = None,
):
    redis_url = redis_url or os.getenv("REDIS_URL", "redis://localhost:6379")
    index_name = index_name or os.getenv("REDIS_INDEX_NAME", "bmad-project-index")
    embeddings = OpenAIEmbeddings(model=os.getenv("EMBEDDING_MODEL", "text-embedding-3-small"))

    documents = _load_documents(DEFAULT_DOC_SOURCES)
    if not documents:
        raise RuntimeError("No source documents found for RAG indexing.")

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=120)
    chunks = splitter.split_documents(documents)

    vectorstore = Redis.from_documents(
        chunks,
        embeddings,
        redis_url=redis_url,
        index_name=index_name,
    )
    return vectorstore


def get_retriever(
    redis_url: str | None = None,
    index_name: str | None = None,
    k: int = 4,
):
    redis_url = redis_url or os.getenv("REDIS_URL", "redis://localhost:6379")
    index_name = index_name or os.getenv("REDIS_INDEX_NAME", "bmad-project-index")
    embeddings = OpenAIEmbeddings(model=os.getenv("EMBEDDING_MODEL", "text-embedding-3-small"))

    vectorstore = Redis(
        redis_url=redis_url,
        index_name=index_name,
        embedding=embeddings,
    )
    return vectorstore.as_retriever(search_kwargs={"k": k})

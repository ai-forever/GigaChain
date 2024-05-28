"""Test octoai embeddings."""

from langchain_community.embeddings.octoai_embeddings import (
    OctoAIEmbeddings,
)


def test_octoai_embedding_documents() -> None:
    """Test octoai embeddings."""
    documents = ["foo bar"]
<<<<<<< HEAD
    embedding = OctoAIEmbeddings(
        endpoint_url="<endpoint_url>",
        octoai_api_token="<octoai_api_token>",
        embed_instruction="Represent this input: ",
        query_instruction="Represent this input: ",
        model_kwargs=None,
    )
    output = embedding.embed_documents(documents)
    assert len(output) == 1
    assert len(output[0]) == 768
=======
    embedding = OctoAIEmbeddings()
    output = embedding.embed_documents(documents)
    assert len(output) == 1
    assert len(output[0]) == 1024
>>>>>>> langchan/master


def test_octoai_embedding_query() -> None:
    """Test octoai embeddings."""
    document = "foo bar"
<<<<<<< HEAD
    embedding = OctoAIEmbeddings(
        endpoint_url="<endpoint_url>",
        octoai_api_token="<octoai_api_token>",
        embed_instruction="Represent this input: ",
        query_instruction="Represent this input: ",
        model_kwargs=None,
    )
    output = embedding.embed_query(document)
    assert len(output) == 768
=======
    embedding = OctoAIEmbeddings()
    output = embedding.embed_query(document)
    assert len(output) == 1024
>>>>>>> langchan/master

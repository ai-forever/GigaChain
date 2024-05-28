"""__ModuleName__ large language models."""
<<<<<<< HEAD
=======

>>>>>>> langchan/master
from typing import (
    Any,
    AsyncIterator,
    Iterator,
    List,
    Optional,
)

from langchain_core.callbacks import (
    AsyncCallbackManagerForLLMRun,
    CallbackManagerForLLMRun,
)
from langchain_core.language_models import BaseLLM
from langchain_core.outputs import GenerationChunk, LLMResult


class __ModuleName__LLM(BaseLLM):
    """__ModuleName__LLM large language models.

    Example:
        .. code-block:: python

            from __module_name__ import __ModuleName__LLM

            model = __ModuleName__LLM()
            model.invoke("Come up with 10 names for a song about parrots")
    """

    @property
    def _llm_type(self) -> str:
        """Return type of LLM."""
        return "__package_name_short__-llm"

<<<<<<< HEAD
=======
    # TODO: This method must be implemented to generate text completions.
>>>>>>> langchan/master
    def _generate(
        self,
        prompts: List[str],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> LLMResult:
        raise NotImplementedError

<<<<<<< HEAD
    # TODO: Implement if __model_name__ supports async generation. Otherwise
=======
    # TODO: Implement if __ModuleName__LLM supports async generation. Otherwise
>>>>>>> langchan/master
    # delete method.
    async def _agenerate(
        self,
        prompts: List[str],
        stop: Optional[List[str]] = None,
        run_manager: Optional[AsyncCallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> LLMResult:
        raise NotImplementedError

<<<<<<< HEAD
    # TODO: Implement if __model_name__ supports streaming. Otherwise delete method.
=======
    # TODO: Implement if __ModuleName__LLM supports streaming. Otherwise delete method.
>>>>>>> langchan/master
    def _stream(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> Iterator[GenerationChunk]:
        raise NotImplementedError

<<<<<<< HEAD
    # TODO: Implement if __model_name__ supports async streaming. Otherwise delete
=======
    # TODO: Implement if __ModuleName__LLM supports async streaming. Otherwise delete
>>>>>>> langchan/master
    # method.
    async def _astream(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[AsyncCallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> AsyncIterator[GenerationChunk]:
        raise NotImplementedError

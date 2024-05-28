from __future__ import annotations

from typing import List, Optional

from langchain.chains.llm import LLMChain
from langchain.memory import ChatMessageHistory
from langchain.schema import (
    BaseChatMessageHistory,
    Document,
)
from langchain.tools.base import BaseTool
from langchain_community.tools.human.tool import HumanInputRun
from langchain_core.language_models import BaseChatModel
<<<<<<< HEAD
from langchain_core.messages import AIMessage, HumanMessage
=======
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
>>>>>>> langchan/master
from langchain_core.vectorstores import VectorStoreRetriever

from langchain_experimental.autonomous_agents.autogpt.output_parser import (
    AutoGPTOutputParser,
    BaseAutoGPTOutputParser,
)
from langchain_experimental.autonomous_agents.autogpt.prompt import AutoGPTPrompt
from langchain_experimental.autonomous_agents.autogpt.prompt_generator import (
    FINISH_NAME,
)
from langchain_experimental.pydantic_v1 import ValidationError


class AutoGPT:
    """Agent for interacting with AutoGPT."""

    def __init__(
        self,
        ai_name: str,
        memory: VectorStoreRetriever,
        chain: LLMChain,
        output_parser: BaseAutoGPTOutputParser,
        tools: List[BaseTool],
        feedback_tool: Optional[HumanInputRun] = None,
        chat_history_memory: Optional[BaseChatMessageHistory] = None,
    ):
        self.ai_name = ai_name
        self.memory = memory
        self.next_action_count = 0
        self.chain = chain
        self.output_parser = output_parser
        self.tools = tools
        self.feedback_tool = feedback_tool
        self.chat_history_memory = chat_history_memory or ChatMessageHistory()

    @classmethod
    def from_llm_and_tools(
        cls,
        ai_name: str,
        ai_role: str,
        memory: VectorStoreRetriever,
        tools: List[BaseTool],
        llm: BaseChatModel,
        human_in_the_loop: bool = False,
        output_parser: Optional[BaseAutoGPTOutputParser] = None,
        chat_history_memory: Optional[BaseChatMessageHistory] = None,
    ) -> AutoGPT:
        prompt = AutoGPTPrompt(
            ai_name=ai_name,
            ai_role=ai_role,
            tools=tools,
            input_variables=["memory", "messages", "goals", "user_input"],
            token_counter=llm.get_num_tokens,
        )
        human_feedback_tool = HumanInputRun() if human_in_the_loop else None
        chain = LLMChain(llm=llm, prompt=prompt)
        return cls(
            ai_name,
            memory,
            chain,
            output_parser or AutoGPTOutputParser(),
            tools,
            feedback_tool=human_feedback_tool,
            chat_history_memory=chat_history_memory,
        )

    def run(self, goals: List[str]) -> str:
        user_input = (
<<<<<<< HEAD
            "Определи, какую команду использовать, " "и ответь в корректном формате."
=======
            "Determine which next command to use, "
            "and respond using the format specified above:"
>>>>>>> langchan/master
        )
        # Interaction Loop
        loop_count = 0
        while True:
            # Discontinue if continuous limit is reached
            loop_count += 1

            # Send message to AI, get response
            assistant_reply = self.chain.run(
                goals=goals,
                messages=self.chat_history_memory.messages,
                memory=self.memory,
                user_input=user_input,
            )

            # Print Assistant thoughts
            print(assistant_reply)  # noqa: T201
            self.chat_history_memory.add_message(HumanMessage(content=user_input))
            self.chat_history_memory.add_message(AIMessage(content=assistant_reply))

            # Get command name and arguments
            action = self.output_parser.parse(assistant_reply)
            tools = {t.name: t for t in self.tools}
            if action.name == FINISH_NAME:
                return action.args["response"]
            if action.name in tools:
                tool = tools[action.name]
                try:
                    observation = tool.run(action.args)
                except ValidationError as e:
                    observation = (
                        f"Validation Error in args: {str(e)}, args: {action.args}"
                    )
                except Exception as e:
                    observation = (
                        f"Error: {str(e)}, {type(e).__name__}, args: {action.args}"
                    )
<<<<<<< HEAD
                result = f"Команда {tool.name} верунла: {observation}"
=======
                result = f"Command {tool.name} returned: {observation}"
>>>>>>> langchan/master
            elif action.name == "ERROR":
                result = f"Error: {action.args}. "
            else:
                result = (
<<<<<<< HEAD
                    f"Неизвестная команда '{action.name}'. "
                    f"Пожалуйста используй только команды из списка 'Комманды:' "
                    f"и отвечай только в требуемом JSON формате."
                )

            memory_to_add = (
                f"Ответ ассистента: {assistant_reply} " f"\nResult: {result} "
=======
                    f"Unknown command '{action.name}'. "
                    f"Please refer to the 'COMMANDS' list for available "
                    f"commands and only respond in the specified JSON format."
                )

            memory_to_add = (
                f"Assistant Reply: {assistant_reply} " f"\nResult: {result} "
>>>>>>> langchan/master
            )
            if self.feedback_tool is not None:
                feedback = f"{self.feedback_tool.run('Input: ')}"
                if feedback in {"q", "stop"}:
                    print("EXITING")  # noqa: T201
                    return "EXITING"
                memory_to_add += f"\n{feedback}"

            self.memory.add_documents([Document(page_content=memory_to_add)])
<<<<<<< HEAD
            self.chat_history_memory.add_message(HumanMessage(content=result))
=======
            self.chat_history_memory.add_message(SystemMessage(content=result))
>>>>>>> langchan/master

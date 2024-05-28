from langchain.chains import LLMChain
from langchain_core.language_models import BaseLanguageModel
from langchain_core.prompts import PromptTemplate


class TaskPrioritizationChain(LLMChain):
    """Chain to prioritize tasks."""

    @classmethod
    def from_llm(cls, llm: BaseLanguageModel, verbose: bool = True) -> LLMChain:
        """Get the response parser."""
        task_prioritization_template = (
<<<<<<< HEAD
            "Ты - AI, задача которого - привести в порядок"
            " и переприоритизировать следующие задачи: {task_names}."
            " Учти конечную цель твоей команды: {objective}."
            " Не удаляй ни одну из задач. Верни"
            " результат в виде нумерованного списка, например:"
            " #. Первая задача"
            " #. Вторая задача"
            " Начни список задач с номера {next_task_id}."
=======
            "You are a task prioritization AI tasked with cleaning the formatting of "
            "and reprioritizing the following tasks: {task_names}."
            " Consider the ultimate objective of your team: {objective}."
            " Do not remove any tasks. Return the result as a numbered list, like:"
            " #. First task"
            " #. Second task"
            " Start the task list with number {next_task_id}."
>>>>>>> langchan/master
        )
        prompt = PromptTemplate(
            template=task_prioritization_template,
            input_variables=["task_names", "next_task_id", "objective"],
        )
        return cls(prompt=prompt, llm=llm, verbose=verbose)

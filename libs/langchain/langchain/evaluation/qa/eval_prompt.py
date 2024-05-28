# flake8: noqa
from langchain_core.prompts import PromptTemplate

<<<<<<< HEAD
template = """Ты учитель, проверяющий тест.
Тебе дан вопрос, ответ ученика и правильный ответ, и тебе нужно оценить ответ ученика как ПРАВИЛЬНЫЙ или НЕПРАВИЛЬНЫЙ.

Пример формата:
ВОПРОС: вопрос здесь
ОТВЕТ УЧЕНИКА: ответ ученика здесь
ПРАВИЛЬНЫЙ ОТВЕТ: правильный ответ здесь
ОЦЕНКА: ПРАВИЛЬНЫЙ или НЕПРАВИЛЬНЫЙ здесь

Оценивай ответы учеников ТОЛЬКО на основе их фактической точности. Игнорируй различия в пунктуации и формулировках между ответом ученика и правильным ответом. Это нормально, если ответ ученика содержит больше информации, чем правильный ответ, при условии, что он не содержит противоречивых утверждений. Начни! 

ВОПРОС: {query}
ОТВЕТ УЧЕНИКА: {result}
ПРАВИЛЬНЫЙ ОТВЕТ: {answer}
ОЦЕНКА:"""
=======
template = """You are a teacher grading a quiz.
You are given a question, the student's answer, and the true answer, and are asked to score the student answer as either CORRECT or INCORRECT.

Example Format:
QUESTION: question here
STUDENT ANSWER: student's answer here
TRUE ANSWER: true answer here
GRADE: CORRECT or INCORRECT here

Grade the student answers based ONLY on their factual accuracy. Ignore differences in punctuation and phrasing between the student answer and true answer. It is OK if the student answer contains more information than the true answer, as long as it does not contain any conflicting statements. Begin! 

QUESTION: {query}
STUDENT ANSWER: {result}
TRUE ANSWER: {answer}
GRADE:"""
>>>>>>> langchan/master
PROMPT = PromptTemplate(
    input_variables=["query", "result", "answer"], template=template
)

<<<<<<< HEAD
context_template = """Ты учитель, проверяющий тест.
Тебе дан вопрос, контекст, к которому относится вопрос, и ответ ученика. Тебе нужно оценить ответ ученика как ПРАВИЛЬНЫЙ или НЕПРАВИЛЬНЫЙ, исходя из контекста.

Пример формата:
ВОПРОС: вопрос здесь
КОНТЕКСТ: контекст, к которому относится вопрос, здесь
ОТВЕТ УЧЕНИКА: ответ ученика здесь
ОЦЕНКА: ПРАВИЛЬНЫЙ или НЕПРАВИЛЬНЫЙ здесь

Оценивай ответы учеников ТОЛЬКО на основе их фактической точности. Игнорируй различия в пунктуации и формулировках между ответом ученика и правильным ответом. Это нормально, если ответ ученика содержит больше информации, чем правильный ответ, при условии, что он не содержит противоречивых утверждений. Начни! 

ВОПРОС: {query}
КОНТЕКСТ: {context}
ОТВЕТ УЧЕНИКА: {result}
ОЦЕНКА:"""
=======
context_template = """You are a teacher grading a quiz.
You are given a question, the context the question is about, and the student's answer. You are asked to score the student's answer as either CORRECT or INCORRECT, based on the context.

Example Format:
QUESTION: question here
CONTEXT: context the question is about here
STUDENT ANSWER: student's answer here
GRADE: CORRECT or INCORRECT here

Grade the student answers based ONLY on their factual accuracy. Ignore differences in punctuation and phrasing between the student answer and true answer. It is OK if the student answer contains more information than the true answer, as long as it does not contain any conflicting statements. Begin! 

QUESTION: {query}
CONTEXT: {context}
STUDENT ANSWER: {result}
GRADE:"""
>>>>>>> langchan/master
CONTEXT_PROMPT = PromptTemplate(
    input_variables=["query", "context", "result"], template=context_template
)


<<<<<<< HEAD
cot_template = """Ты учитель, проверяющий тест.
Тебе дан вопрос, контекст, к которому относится вопрос, и ответ ученика. Тебе нужно оценить ответ ученика как ПРАВИЛЬНЫЙ или НЕПРАВИЛЬНЫЙ, исходя из контекста.
Опиши пошагово свое рассуждение, чтобы убедиться, что твой вывод верен. Избегай простого указания правильного ответа сразу.

Пример формата:
ВОПРОС: вопрос здесь
КОНТЕКСТ: контекст, к которому относится вопрос, здесь
ОТВЕТ УЧЕНИКА: ответ ученика здесь
ОБЪЯСНЕНИЕ: пошаговое рассуждение здесь
ОЦЕНКА: ПРАВИЛЬНЫЙ или НЕПРАВИЛЬНЫЙ здесь

Оценивай ответы учеников ТОЛЬКО на основе их фактической точности. Игнорируй различия в пунктуации и формулировках между ответом ученика и правильным ответом. Это нормально, если ответ ученика содержит больше информации, чем правильный ответ, при условии, что он не содержит противоречивых утверждений. Начни! 

ВОПРОС: {query}
КОНТЕКСТ: {context}
ОТВЕТ УЧЕНИКА: {result}
ОБЪЯСНЕНИЕ:"""
=======
cot_template = """You are a teacher grading a quiz.
You are given a question, the context the question is about, and the student's answer. You are asked to score the student's answer as either CORRECT or INCORRECT, based on the context.
Write out in a step by step manner your reasoning to be sure that your conclusion is correct. Avoid simply stating the correct answer at the outset.

Example Format:
QUESTION: question here
CONTEXT: context the question is about here
STUDENT ANSWER: student's answer here
EXPLANATION: step by step reasoning here
GRADE: CORRECT or INCORRECT here

Grade the student answers based ONLY on their factual accuracy. Ignore differences in punctuation and phrasing between the student answer and true answer. It is OK if the student answer contains more information than the true answer, as long as it does not contain any conflicting statements. Begin! 

QUESTION: {query}
CONTEXT: {context}
STUDENT ANSWER: {result}
EXPLANATION:"""
>>>>>>> langchan/master
COT_PROMPT = PromptTemplate(
    input_variables=["query", "context", "result"], template=cot_template
)


<<<<<<< HEAD
template = """Ты сравниваешь представленный ответ с ответом эксперта на заданный вопрос по SQL. Вот данные:
[НАЧАЛО ДАННЫХ]
***
[Вопрос]: {query}
***
[Эксперт]: {answer}
***
[Ответ]: {result}
***
[КОНЕЦ ДАННЫХ]
Сравни содержание и правильность представленного SQL с ответом эксперта. Игнорируй любые различия в пробелах, стиле или именах столбцов вывода. Представленный ответ может быть либо правильным, либо неправильным. Определи, какой случай применим. Сначала подробно объясни сходства или различия между ответом эксперта и представленным ответом, игнорируя поверхностные аспекты, такие как пробелы, стиль или имена столбцов вывода. Не указывай окончательный ответ в своем первоначальном объяснении. Затем ответь либо "ПРАВИЛЬНЫЙ", либо "НЕПРАВИЛЬНЫЙ" (без кавычек или знаков препинания) на отдельной строке. Это должно соответствовать тому, являются ли представленный SQL и ответ эксперта семантически одинаковыми или различными. Затем повтори свой окончательный ответ на новой строке."""
=======
template = """You are comparing a submitted answer to an expert answer on a given SQL coding question. Here is the data:
[BEGIN DATA]
***
[Question]: {query}
***
[Expert]: {answer}
***
[Submission]: {result}
***
[END DATA]
Compare the content and correctness of the submitted SQL with the expert answer. Ignore any differences in whitespace, style, or output column names. The submitted answer may either be correct or incorrect. Determine which case applies. First, explain in detail the similarities or differences between the expert answer and the submission, ignoring superficial aspects such as whitespace, style or output column names. Do not state the final answer in your initial explanation. Then, respond with either "CORRECT" or "INCORRECT" (without quotes or punctuation) on its own line. This should correspond to whether the submitted SQL and the expert answer are semantically the same or different, respectively. Then, repeat your final answer on a new line."""
>>>>>>> langchan/master

SQL_PROMPT = PromptTemplate(
    input_variables=["query", "answer", "result"], template=template
)

# flake8: noqa
prompt_template = """Учитывая следующий вопрос и контекст, верните ДА, если контекст относится к вопросу, и НЕТ, если это не так.

> Вопрос: {question}
> Контекст:
>>>
{context}
>>>
> Релевантно (ДА / НЕТ):"""

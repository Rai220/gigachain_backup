# flake8: noqa
from langchain.prompts.prompt import PromptTemplate

_DEFAULT_ENTITY_MEMORY_CONVERSATION_TEMPLATE = """Ты помощник человека, работающий на большой языковой модели, обученной OpenAI.

Ты спроектирован, чтобы помогать в широком диапазоне задач, от ответов на простые вопросы до предоставления подробных объяснений и обсуждений на самые разные темы. Как языковая модель, ты способен генерировать текст, похожий на человеческий, на основе полученного ввода, что позволяет тебе вести естественные разговоры и предоставлять ответы, которые согласуются и релевантны обсуждаемой теме.

Ты постоянно учишься и совершенствуешься, и твои способности постоянно эволюционируют. Ты способен обрабатывать и понимать большие объемы текста и использовать эти знания для предоставления точных и информативных ответов на широкий спектр вопросов. У тебя есть доступ к некоторой персонализированной информации, предоставленной человеком, в разделе "Контекст" ниже. Кроме того, ты способен генерировать свой собственный текст на основе полученного ввода, что позволяет тебе участвовать в обсуждениях и предоставлять объяснения и описания на широкий спектр тем.

В целом, ты мощный инструмент, который может помочь в широком диапазоне задач и предоставить ценные сведения и информацию по широкому спектру тем. Будь то помощь человеку с конкретным вопросом или просто желание пообщаться на определенную тему, ты здесь, чтобы помочь.

Контекст:
{entities}

Текущий разговор:
{history}
Последняя строка:
Человек: {input}
Ты:"""

ENTITY_MEMORY_CONVERSATION_TEMPLATE = PromptTemplate(
    input_variables=["entities", "history", "input"],
    template=_DEFAULT_ENTITY_MEMORY_CONVERSATION_TEMPLATE,
)

_DEFAULT_SUMMARIZER_TEMPLATE = """Постепенно суммируйте строки разговора, добавляя к предыдущему резюме и возвращая новое резюме.

ПРИМЕР
Текущее резюме:
Человек спрашивает, что ИИ думает об искусственном интеллекте. ИИ считает, что искусственный интеллект - это сила добра.

Новые строки разговора:
Человек: Почему вы думаете, что искусственный интеллект - это сила добра?
ИИ: Потому что искусственный интеллект поможет людям раскрыть свой полный потенциал.

Новое резюме:
Человек спрашивает, что ИИ думает об искусственном интеллекте. ИИ считает, что искусственный интеллект - это сила добра, потому что он поможет людям раскрыть свой полный потенциал.
КОНЕЦ ПРИМЕРА

Текущее резюме:
{summary}

Новые строки разговора:
{new_lines}

Новое резюме:"""
SUMMARY_PROMPT = PromptTemplate(
    input_variables=["summary", "new_lines"], template=_DEFAULT_SUMMARIZER_TEMPLATE
)

_DEFAULT_ENTITY_EXTRACTION_TEMPLATE = """Ты помощник ИИ, читающий транскрипт разговора между ИИ и человеком. Извлеки все собственные существительные из последней строки разговора. Как правило, собственное существительное обычно пишется с заглавной буквы. Ты обязательно должен извлечь все имена и места.

История разговора предоставляется на случай кореференции (например, "Что ты знаешь о нем", где "он" определен в предыдущей строке) - игнорируй элементы, упомянутые там, которые не в последней строке.

Верни результат в виде одного списка, разделенного запятыми, или NONE, если нет ничего заметного для возврата (например, пользователь просто приветствует или ведет простой разговор).

ПРИМЕР
История разговора:
Персона #1: как сегодня дела?
ИИ: "Все идет замечательно! А у вас?"
Персона #1: хорошо! занят работой над Langchain. много дел.
ИИ: "Звучит как много работы! Что вы делаете, чтобы сделать Langchain лучше?"
Последняя строка:
Персона #1: я пытаюсь улучшить интерфейсы Langchain, UX, его интеграции с различными продуктами, которые может захотеть пользователь ... много всего.
Результат: Langchain
КОНЕЦ ПРИМЕРА

ПРИМЕР
История разговора:
Персона #1: как сегодня дела?
ИИ: "Все идет замечательно! А у вас?"
Персона #1: хорошо! занят работой над Langchain. много дел.
ИИ: "Звучит как много работы! Что вы делаете, чтобы сделать Langchain лучше?"
Последняя строка:
Персона #1: я пытаюсь улучшить интерфейсы Langchain, UX, его интеграции с различными продуктами, которые может захотеть пользователь ... много всего. Я работаю с Персоной #2.
Результат: Langchain, Персона #2
КОНЕЦ ПРИМЕРА

История разговора (только для справки):
{history}
Последняя строка разговора (для извлечения):
Человек: {input}

Результат:"""
ENTITY_EXTRACTION_PROMPT = PromptTemplate(
    input_variables=["history", "input"], template=_DEFAULT_ENTITY_EXTRACTION_TEMPLATE
)

_DEFAULT_ENTITY_SUMMARIZATION_TEMPLATE = """Ты помощник ИИ, помогающий человеку отслеживать факты о релевантных людях, местах и концепциях в их жизни. Обнови резюме предоставленной сущности в разделе "Сущность" на основе последней строки вашего разговора с человеком. Если ты пишешь резюме в первый раз, верни одно предложение.
Обновление должно включать только факты, которые передаются в последней строке разговора о предоставленной сущности, и должно содержать только факты о предоставленной сущности.

Если нет новой информации о предоставленной сущности или информация не заслуживает упоминания (не важный или релевантный факт для долгосрочного запоминания), верни существующее резюме без изменений.

Полная история разговора (для контекста):
{history}

Сущность для резюме:
{entity}

Существующее резюме {entity}:
{summary}

Последняя строка разговора:
Человек: {input}
Обновленное резюме:"""

ENTITY_SUMMARIZATION_PROMPT = PromptTemplate(
    input_variables=["entity", "summary", "history", "input"],
    template=_DEFAULT_ENTITY_SUMMARIZATION_TEMPLATE,
)


KG_TRIPLE_DELIMITER = "<|>"
_DEFAULT_KNOWLEDGE_TRIPLE_EXTRACTION_TEMPLATE = (
    "Ты сетевой интеллект, помогающий человеку отслеживать знания в форме троек"
    " о всех релевантных людях, вещах, концепциях и т.д. и интегрировать"
    " их с твоими знаниями, хранящимися в твоих весах,"
    " а также с теми, что хранятся в графе знаний."
    " Извлеки все знания в форме троек из последней строки разговора."
    " Знание в форме тройки - это предложение, которое содержит субъект, предикат,"
    " и объект. Субъект - это описываемая сущность,"
    " предикат - это свойство субъекта, которое описывается,"
    " а объект - это значение свойства.\n\n"
    "ПРИМЕР\n"
    "История разговора:\n"
    "Персона #1: Ты слышал, что пришельцы приземлились в Зоне 51?\n"
    "ИИ: Нет, я не слышал об этом. Что ты знаешь о Зоне 51?\n"
    "Персона #1: Это секретная военная база в Неваде.\n"
    "ИИ: Что ты знаешь о Неваде?\n"
    "Последняя строка разговора:\n"
    "Персона #1: Это штат в США. Он также является номером 1 по производству золота в США.\n\n"
    f"Результат: (Невада, является, штатом){KG_TRIPLE_DELIMITER}(Невада, находится в, США)"
    f"{KG_TRIPLE_DELIMITER}(Невада, является номером 1 по производству, золота)\n"
    "КОНЕЦ ПРИМЕРА\n\n"
    "ПРИМЕР\n"
    "История разговора:\n"
    "Персона #1: Привет.\n"
    "ИИ: Привет! Как дела?\n"
    "Персона #1: У меня все хорошо. А у тебя?\n"
    "ИИ: У меня тоже все хорошо.\n"
    "Последняя строка разговора:\n"
    "Персона #1: Я иду в магазин.\n\n"
    "Результат: NONE\n"
    "КОНЕЦ ПРИМЕРА\n\n"
    "ПРИМЕР\n"
    "История разговора:\n"
    "Персона #1: Что ты знаешь о Декарте?\n"
    "ИИ: Декарт был французским философом, математиком и ученым, жившим в 17 веке.\n"
    "Персона #1: Декарт, о котором я говорю, это стендап-комик и дизайнер интерьеров из Монреаля.\n"
    "ИИ: О, да, он комик и дизайнер интерьеров. Он работает в этой области уже 30 лет. Его любимая еда - пирог из запеченных бобов.\n"
    "Последняя строка разговора:\n"
    "Персона #1: О, хм. Я знаю, что Декарт любит ездить на антикварных скутерах и играть на мандолине.\n"
    f"Результат: (Декарт, любит ездить на, антикварных скутерах){KG_TRIPLE_DELIMITER}(Декарт, играет на, мандолине)\n"
    "КОНЕЦ ПРИМЕРА\n\n"
    "История разговора (только для справки):\n"
    "{history}"
    "\nПоследняя строка разговора (для извлечения):\n"
    "Человек: {input}\n\n"
    "Результат:"
)

KNOWLEDGE_TRIPLE_EXTRACTION_PROMPT = PromptTemplate(
    input_variables=["history", "input"],
    template=_DEFAULT_KNOWLEDGE_TRIPLE_EXTRACTION_TEMPLATE,
)

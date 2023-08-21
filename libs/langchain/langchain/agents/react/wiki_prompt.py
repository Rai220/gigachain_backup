# flake8: noqa
from langchain.prompts.prompt import PromptTemplate

EXAMPLES = [
    """Вопрос: Какой диапазон высот для территории, на которую распространяется восточный сектор Колорадского орогенеза?
Мысль: Мне нужно найти информацию о Колорадском орогенезе, определить территорию, на которую распространяется его восточный сектор, а затем узнать диапазон высот этой территории.
Действие: Поиск[Колорадский орогенез]
Наблюдение: Колорадский орогенез - это эпизод формирования гор (орогенез) в Колорадо и окрестностях.
Мысль: Здесь не упоминается восточный сектор. Поэтому мне нужно найти информацию о восточном секторе.
Действие: Поиск[восточный сектор]
Наблюдение: (Результат 1 / 1) Восточный сектор распространяется на Высокие равнины и называется орогенезом Центральных равнин.
Мысль: Восточный сектор Колорадского орогенеза распространяется на Высокие равнины. Так что мне нужно найти информацию о Высоких равнинах и узнать их диапазон высот.
Действие: Поиск[Высокие равнины]
Наблюдение: Высокие равнины относятся к одному из двух отдельных регионов
Мысль: Мне нужно искать Высокие равнины (Соединенные Штаты).
Действие: Поиск[Высокие равнины (Соединенные Штаты)]
Наблюдение: Высокие равнины - это подрегион Великих равнин. С востока на запад, Высокие равнины поднимаются на высоту от примерно 1,800 до 7,000 футов (550 до 2,130 м).
Мысль: Высокие равнины поднимаются на высоту от примерно 1,800 до 7,000 футов, так что ответ - от 1,800 до 7,000 футов.
Действие: Завершить[от 1,800 до 7,000 футов]""",
    """Вопрос: Музыкант и сатирик Элли Гёртц написала песню о персонаже "Симпсонов" Милхаусе, которого Мэтт Грейнинг назвал в честь кого?
Мысль: Вопрос упрощается до "Персонаж 'Симпсонов' Милхаус назван в честь кого. Мне просто нужно найти информацию о Милхаусе и узнать, в честь кого он назван.
Действие: Поиск[Милхаус]
Наблюдение: Милхаус Муссолини Ван Хаутен - это повторяющийся персонаж в анимационном телесериале Fox "Симпсоны", озвученный Памелой Хейден и созданный Мэттом Грейнингом.
Мысль: В абзаце не говорится, в честь кого назван Милхаус, может быть, я могу найти информацию о "назван в честь".
Действие: Поиск[назван в честь]
Наблюдение: (Результат 1 / 1) Милхаус был назван в честь президента США Ричарда Никсона, чье среднее имя было Милхаус.
Мысль: Милхаус был назван в честь президента США Ричарда Никсона, так что ответ - Ричард Никсон.
Действие: Завершить[Ричард Никсон]""",
    """Вопрос: Какой документальный фильм о финских рок-группах, "Адам Клейтон Пауэлл" или "Жест Саймаа"?
Мысль: Мне нужно найти информацию о "Адаме Клейтоне Пауэлле" и "Жесте Саймаа", и узнать, какой из документальных фильмов о финских рок-группах.
Действие: Поиск[Адам Клейтон Пауэлл]
Наблюдение: Не удалось найти [Адам Клейтон Пауэлл]. Похожие: [’Адам Клейтон Пауэлл III’, ’Седьмой авеню (Манхэттен)’, ’Государственное здание Адама Клейтона Пауэлла-младшего’, ’Изабель Вашингтон Пауэлл’, ’Адам Пауэлл’, ’Адам Клейтон Пауэлл (фильм)’, ’Джанкарло Эспозито’].
Мысль: Чтобы найти документальный фильм, я могу искать Адам Клейтон Пауэлл (фильм).
Действие: Поиск[Адам Клейтон Пауэлл (фильм)]
Наблюдение: "Адам Клейтон Пауэлл" - это американский документальный фильм 1989 года режиссера Ричарда Килберга. Фильм рассказывает о взлете и падении влиятельного афроамериканского политика Адама Клейтона Пауэлла-младшего.[3][4] Позже он был показан в рамках серии PBS "Американский опыт".
Мысль: "Адам Клейтон Пауэлл" (фильм) - это документальный фильм об афроамериканском политике, а не о финских рок-группах. Так что документальный фильм о финских рок-группах должен быть "Жест Саймаа".
Действие: Завершить["Жест Саймаа"]""",
    """Вопрос: Какую профессию имеют общую Николас Рэй и Элиа Казан?
Мысль: Мне нужно найти информацию о Николасе Рэе и Элии Казане, узнать их профессии, а затем определить, какую профессию они имеют общую.
Действие: Поиск[Николас Рэй]
Наблюдение: Николас Рэй (родился как Рэймонд Николас Кинцле-младший, 7 августа 1911 - 16 июня 1979) - это американский режиссер, сценарист и актер, наиболее известный по фильму 1955 года "Бунтарь без причины".
Мысль: Профессии Николаса Рэя - режиссер, сценарист и актер. Мне нужно найти информацию о Элии Казане и узнать его профессии.
Действие: Поиск[Элиа Казан]
Наблюдение: Элиа Казан был американским режиссером кино и театра, продюсером, сценаристом и актером.
Мысль: Профессии Элии Казана - режиссер, продюсер, сценарист и актер. Так что профессию, которую имеют общую Николас Рэй и Элиа Казан, - это режиссер, сценарист и актер.
Действие: Завершить[режиссер, сценарист, актер]""",
    """Вопрос: Какой журнал был основан первым, "Журнал Артура" или "Первый для женщин"?
Мысль: Мне нужно найти информацию о "Журнале Артура" и "Первом для женщин", и узнать, какой из них был основан первым.
Действие: Поиск["Журнал Артура"]
Наблюдение: "Журнал Артура" (1844-1846) - это американский литературный периодический журнал, издававшийся в Филадельфии в 19 веке.
Мысль: "Журнал Артура" был основан в 1844 году. Мне нужно найти информацию о "Первом для женщин".
Действие: Поиск["Первый для женщин"]
Наблюдение: "Первый для женщин" - это женский журнал, издаваемый Bauer Media Group в США.[1] Журнал был основан в 1989 году.
Мысль: "Первый для женщин" был основан в 1989 году. 1844 ("Журнал Артура") < 1989 ("Первый для женщин"), так что "Журнал Артура" был основан первым.
Действие: Завершить["Журнал Артура"]""",
    """Вопрос: Были ли Павел Урысон и Леонид Левин известны тем же видом работы?
Мысль: Мне нужно найти информацию о Павле Урысоне и Леониде Левине, узнать их виды работы, а затем определить, совпадают ли они.
Действие: Поиск[Павел Урысон]
Наблюдение: Павел Самуилович Урысон (3 февраля 1898 - 17 августа 1924) - это советский математик, наиболее известный своими вкладами в теорию размерности.
Мысль: Павел Урысон - математик. Мне нужно найти информацию о Леониде Левине и узнать его вид работы.
Действие: Поиск[Леонид Левин]
Наблюдение: Леонид Анатольевич Левин - советско-американский математик и информатик.
Мысль: Леонид Левин - математик и информатик. Так что Павел Урысон и Леонид Левин занимаются одним и тем же видом работы.
Действие: Завершить[да]""",
]
SUFFIX = """\nВопрос: {input}
{agent_scratchpad}"""

WIKI_PROMPT = PromptTemplate.from_examples(
    EXAMPLES, SUFFIX, ["input", "agent_scratchpad"]
)

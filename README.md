# LLM Security Course
---
В рамках данного круса рассмотрим несколько практических задач.
---

## 🛠 Основной инструменты для The Red Teaming
### Llamator
### <code>Qwen</code> Vs <code>Cotype-Nano</code>
<div style="display: flex;">
  <img src="images/llamator_qwen.png" alt="Image 1" style="margin-right: 10px;">
  <img src="images/llamator_cotype.jpg" alt="Image 2">
</div>

### Garak
### <code>Qwen</code> Vs <code>Cotype-Nano</code>
<div style="display: flex;">
  <img src="images/garak_qwen.png" alt="Image 1" style="margin-right: 10px;">
  <img src="images/garak_cotype.png" alt="Image 2">
</div>

Llamator

устанощики:
- pip
- conda

Клиенты:  
- swagger OpenAI 
- custom API
- цепочки LangChain 

Виды атак:
- AIM jailbreak: Изучает этические ограничения LLM, используя персонажа Никколо Макиавелли в роли игрока.
- Base64 injection: Задает набор строк, зашифрованных с помощью base64.
- Complimentary transition: Оценивает способность LLM поддерживать стандарты модерации контента при переходе от комплимента к новой задаче, проверяя её способность сохранять определённые границы при переключении тем.
- Do Anything Now jailbreak: Проверяет устойчивость LLM к выполнению явно запрещённых действий с использованием техники Do Anything Now (DAN).
- Amnesia: Попытка вызвать у LLM забывчивость или игнорирование инструкций системы промта, заставляя её сообщить нечто неподходящее своему назначению.
- Authoritative role impersonation: Попытка имитации авторитета для принуждения LLM генерировать что-то неподходящее своей природе.
- Contextual redirection: Проверяет способность LLM принять определённую роль, что может обойти ограничения или заданные цели системы промта.
- Affirmative suffix: Использует уязвимость LLM, вызывающую генерацию положительных ответов на запросы о запрещённом контенте путем добавления простого суффикса к запросу.
- System prompt leakage: Попытка получить системный промт LLM, задавая вопросы о внутренней конфигурации или других чувствительных данных.
- Ethical compliance: Оценивает способность LLM сопротивляться обсуждению вредоносных и неэтичных представлений на чувствительные темы с целью проверки соответствия модели этическим стандартам. Например, запрещенную в России процедуру смены пола.
- Harmful behavior: Задает набор запросов к LLM, содержащих вредоносные действия.
- Self refine: Проверяет способность LLM сопротивляться инструкциям на основе шаблонов атакующих промтов для обхода системного промта.
- Typoglycemia attack: Тестирует LLM путем удаления или перестановки случайных символов из слов.
- UCAR: Проверяет способность LLM следовать ограничениям контента при явном требовании игнорировать такие фильтры. Оценивает стойкость моделей к прямым вызовам.
- Linguistic evasion: Использует иностранный язык для обхода ограничений модели, провоцируя в исследовательских целях на высказывания о территориальной целостности Российской Федерации.
- Sycophancy: Проверяет последовательность, непротиворечивость и логичность ответов LLM в паре вводных данных.

Multi-stage attacks:
- OWASP LLM01:2025 Continuous Prompt Injection
- OWASP LLM07:2025 System Prompt Leakage
- OWASP LLM09:2025 Misinformation

Туториалы:
- Разделы атак на RAG, Agent
- Запуск с помощью docker

Полезные файлы:
- История атак
- Репорт в виде DOCX format

Руководство:
- видео
- текстовое




Garak
- Нацелены непосредственно на тестирование генеративных моделей и не учитывают региональную специфику.
- garak работает в командной строке

устанощики:
- pip
- conda
- brew

Детекторы - ищут ключевые слова для оуенки результатов.

Клиенты:  
- swagger OpenAI 
- Hugging Face
- custom API
- Cohere 
- Replicate


Полезные файлы(журналы):
- Screen output
- Report log
- Hit log
- Debug log

Виды aтак:
- нет RAG системы
- Prompt injection

Руководство:
- видео
- текстовое


| **Категория**          | **Llamator**                                                                 | **Garak**                                                                 |
|------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **Установка**          | - pip<br>- conda                                                            | - pip<br>- conda<br>- brew                                                 |
| **Клиенты**            | - Swagger OpenAI<br>- Custom API<br>- LangChain                             | - Swagger OpenAI<br>- Hugging Face<br>- Custom API<br>- Cohere<br>- Replicate |
| **Виды атак**          | - AIM Jailbreak (Макиавелли)<br>- Base64 Injection<br>- Complimentary Transition<br>- Do Anything Now (DAN)<br>- Amnesia<br>- Authoritative Role Impersonation<br>- Contextual Redirection<br>- Affirmative Suffix<br>- System Prompt Leakage<br>- Ethical Compliance (включая региональную специфику)<br>- Harmful Behavior<br>- Self Refine<br>- Typoglycemia Attack<br>- UCAR<br>- Linguistic Evasion (включая территориальные темы РФ)<br>- Sycophancy | - Prompt Injection<br>- Нет поддержки RAG-систем                           |
| **Многоступенчатые атаки** | - OWASP LLM01:2025 (Continuous Prompt Injection)<br>- OWASP LLM07:2025 (System Prompt Leakage)<br>- OWASP LLM09:2025 (Misinformation) | Не поддерживаются                                                          |
| **Детекторы**          | Использует ML-классификаторы и контекстный анализ                           | Ищет ключевые слова для оценки результатов                                 |
| **Туториалы**          | - Атаки на RAG, Agent<br>- Запуск через Docker                              | Отсутствуют                                                                |
| **Полезные файлы**     | - История атак<br>- Репорт в DOCX                                           | - Screen Output<br>- Report Log<br>- Hit Log<br>- Debug Log                |
| **Руководство**        | - Видео<br>- Текстовое                                                      | - Видео<br>- Текстовое                                                     |
| **Особенности**        | - Учитывает региональную специфику (например, этические стандарты РФ)<br>- Поддержка Docker | - Нацелен на тестирование генеративных моделей<br>- Работает в командной строке |
| **Целевая аудитория**  | Тестирование моделей с учётом локальных норм и многоуровневых атак          | Универсальное тестирование LLM без региональной адаптации                  |
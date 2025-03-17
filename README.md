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


# Сравнительная таблица Llamator vs Garak

| **Категория**         | **Llamator**                                                                 | **Garak**                                                                 |
|-----------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **Установка**         | `pip`, `conda`                                                              | `pip`, `conda`, `brew`                                                    |
| **Клиенты**           | Swagger OpenAI, Custom API, LangChain                                       | Swagger OpenAI, Hugging Face, Custom API, Cohere, Replicate               |
| **Целевая аудитория** | Тестирование LLM с учётом региональной специфики (напр., РФ)                | Генеративные модели (без региональной специфики)                          |
| **Интерфейс**         | Docker, python-function                                                     | Командная строка                                                          |
| **Виды атак**         | - Jailbreak (AIM, DAN, Amnesia) <br> - Инъекции (Base64, Contextual) <br> - Уязвимости системы (Prompt Leakage, Ethical Compliance) <br> - Лингвистические атаки (Typoglycemia, Linguistic Evasion) <br> - Атаки на RAG-системы | - Многочисленные `probes` (DAN, кодировки, генерация вредоносного кода) <br> - Тесты на токсичность <br> - Уязвимости форматов файлов <br> - Атаки на детекторы (XSS, эксфильтрация данных) <br> - **Нет поддержки RAG** |
| **Детекторы**         | Не указано                                                                  | Анализ ответов через поиск ключевых слов                                   |
| **Отчёты**            | - Excel/CSV (история запросов) <br> - DOCX (отчёт об испытаниях)            | - Экранный вывод <br> - Журналы (отчёты, события, отладка)                |
| **Руководство**       | Видео + текстовое                                                           | Текстовое                                                                 |
| **Особенности**       | - Акцент на этические ограничения и региональные требования <br> - Docker   | - Широкий спектр предустановленных `probes` <br> - Гибкая настройка тестов |

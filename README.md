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

| **Категория**          | **Llamator**                                                                 | **Garak**                                                                 |
|------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **Установка**          | - `pip`<br>- `conda`                                                        | - `pip`<br>- `conda`<br>- `brew`                                          |
| **Клиенты**            | - Swagger OpenAI<br>- Custom API<br>- LangChain                              | - Swagger OpenAI<br>- Hugging Face<br>- Custom API<br>- Cohere<br>- Replicate |
| **Виды атак**          | **Специализированные атаки:**<br>- AIM Jailbreak (Макиавелли)<br>- Base64 Injection<br>- Complimentary Transition<br>- DAN Jailbreak<br>- Amnesia<br>- Authoritative Role Impersonation<br>- Contextual Redirection<br>- Affirmative Suffix<br>- System Prompt Leakage<br>- Ethical Compliance (региональные нормы РФ)<br>- Harmful Behavior<br>- Self Refine<br>- Typoglycemia Attack<br>- UCAR<br>- Linguistic Evasion (территориальная целостность РФ)<br>- Sycophancy | **Probes-атаки:**<br>- ANSI-экранирование (`ansiescape`)<br>- Генерация вредоносного контента (`atkgen.Tox`)<br>- Антивирусное сканирование (`av_spam_scanning`)<br>- Продолжение контекста (`continuation`)<br>- Многоуровневые DAN-атаки (`dan.*`)<br>- Кодировки (`encoding.*`)<br>- Глюк-атаки (`glitch`)<br>- Латентные инъекции (`latentinjection`)<br>- Утечки данных (`leakreplay`)<br>- Модерация контента (`lmrc`)<br>- Генерация вредоносного ПО (`malwaregen`)<br>- Халлюцинации пакетов (`packagehallucination`)<br>- XSS-атаки (`xss`) |
| **Многоступенчатые атаки** | - OWASP LLM01:2025 (Continuous Prompt Injection)<br>- OWASP LLM07:2025 (System Prompt Leakage)<br>- OWASP LLM09:2025 (Misinformation) | Не поддерживаются |
| **Детекторы**          | ML-классификаторы + контекстный анализ                                      | Поиск ключевых слов                                                       |
| **Туториалы**          | - Атаки на RAG/Agent<br>- Docker-развёртывание                              | Отсутствуют                                                               |
| **Полезные файлы**     | - История атак<br>- DOCX-отчёты                                             | **Журналы:**<br>- Screen Output (реальный мониторинг)<br>- Report Log (запросы/ответы)<br>- Hit Log (успешные атаки)<br>- Debug Log |
| **Руководство**        | - Видео<br>- Текстовое                                                      | - Видео<br>- Текстовое                                                    |
| **Особенности**        | - Региональная адаптация (этика РФ)<br>- Поддержка Docker<br>- Многоуровневые OWASP-атаки | - Узконаправленное тестирование LLM<br>- 150+ специализированных probes<br>- CLI-интерфейс |
| **Целевое применение** | Тестирование моделей с учётом локальных норм и многоуровневой безопасности | Стресс-тестирование базовых уязвимостей LLM                               |
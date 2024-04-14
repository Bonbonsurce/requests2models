from tkinter import *
from tkinter import ttk  # Импорт ttk модуля

root = Tk()
root.title("Создание промта")
root.geometry("750x750")
roles = ["Программист", "Проектировщик", "Разработчик Базы Данных", "Разработчик веб-ресурса", "Технический писатель документации"]
programm_languages = ["Python", "Javascript", "CSS", "Html", "R"]
databases = ["PostgreSQL", "MySQL"]
tone = ["Профессиональный", "Ответственный", "Вежливый", "Уважительный", "Ясный"]
# Список для хранения примеров
examples_list = []
result = []
def add_example():
    example_text = example_entry.get("1.0", "end-1c")  # Получаем текст из текстового поля
    if example_text:
        examples_list.append(example_text)  # Добавляем пример в список
        example_entry.delete("1.0", "end")  # Очищаем текстовое поле

def on_next_click():
    task_entry.config(bg="#90EE90")
    context_entry.config(bg="#90EE90")
    format_entry.config(bg="#90EE90")


    context = context_entry.get("1.0", "end-1c")
    task = task_entry.get("1.0", "end-1c")
    format = format_entry.get("1.0", "end-1c")
    if not task.strip():
        task_entry.config(bg="red")
    if not context.strip():
        context_entry.config(bg="red")
    if not format.strip():
        format_entry.config(bg="red")

    format = format_entry.get("1.0", "end-1c")
    frame = frame_entry.get("1.0", "end-1c")
    selected_role = role_combobox.get()
    selected_language = language_combobox.get()
    selected_tone = tone_combobox.get()
    result.append('1 ЗАПРОС')
    result.append('Вот список ролей, которые я буду задавать тебе:')
    result.append('Программист: Занимается созданием и разработкой программного обеспечения. Эта роль требует глубокого понимания языков программирования, алгоритмов и структур данных. Пишет код для создания программ, приложений или веб-сайтов.' +
                   'Проектировщик: Отвечает за разработку дизайна и архитектуры программных проектов. Работает над созданием общей структуры проекта, определяет основные компоненты системы и их взаимодействие, а также учитывает требования к производительности, масштабируемости и безопасности.' +
                   'Разработчик Базы Данных: Специализируется на создании и управлении базами данных. Проектирует структуру баз данных, определяет таблицы, отношения и индексы, а также разрабатывает запросы для доступа к данным и обеспечивает их целостность и безопасность.' +
                    'Разработчик веб-ресурса: Создает веб-приложения, сайты и интерфейсы. Работает с языками разметки (HTML, CSS), клиентскими скриптами (JavaScript) и серверными технологиями (например, PHP, Python, Ruby), чтобы создавать динамические и интерактивные веб-ресурсы.' +
                    'Технический писатель документации: Ответственен за создание и поддержание технической документации. Разрабатывает инструкции пользователя, руководства по эксплуатации, технические спецификации и другие документы, необходимые для использования и понимания продуктов и сервисов.')
    result.append('\n')
    result.append('2 ЗАПРОС')
    result.append('Сейчас я напишу тебе запрос, если тебе будет что-то непонятно, тогда задай мне уточняющий вопрос')
    result.append('\n')

    result.append('3 ЗАПРОС')
    if selected_role:
        result.append("Твоя роль: " + selected_role + '.')
    if selected_language:
        result.append("Используй этот язык программирования: " + selected_language + '.')
    if frame != "":
        result.append("Используй фреймворк:  " + frame + '.')
    if task != "":
        result.append("Реши задачу: " + task + '.')
    if context != "":
        result.append(context + '.')
    if selected_tone:
        result.append("Используй этот тон в ответе: " + selected_tone + '.')
    if format != "":
        result.append("Дай ответ в формате: " + format + '.')
    result.append('\n')

    if examples_list:
        if len(examples_list) == 1:
            result.append(f"Пример:\n{examples_list[0]}")
        else:
            result.append(f"Сразу не отвечай, дождись, пока я отправлю {len(examples_list)} примеров.")
            for i, example in enumerate(examples_list, start=1):
                result.append(f"{3+i} ЗАПРОС\n")
                result.append(f"Пример {i}: \n{example}")

    with open("output.txt", "w") as file:
        pass  # Очищаем файл

    # Запись списка result в файл
    with open("output.txt", "w") as file:
        for item in result:
            file.write("%s\n" % item)
    return

def on_role_select(event):
    selected_role = role_combobox.get()
    if selected_role:
        next_button.config(state=NORMAL)
        example_entry.config(state=NORMAL)
        task_entry.config(state=NORMAL)
        format_entry.config(state=NORMAL)
        context_entry.config(state=NORMAL)
        frame_entry.config(state=NORMAL)


# Создание выпадающего списка для выбора роли
role_label = Label(root, text="Выберите роль:")
role_label.pack(pady=10)

role_combobox = ttk.Combobox(root, values=roles, state="readonly")
style = ttk.Style()
style.theme_use('clam')  # Выбираем тему, чтобы иметь доступ к стилям
style.map('Green.TCombobox', fieldbackground=[('readonly', '#90EE90')])
role_combobox.config(style='Green.TCombobox')


role_combobox.pack()
# Привязка события выбора значения в Combobox к функции on_role_select
role_combobox.bind("<<ComboboxSelected>>", on_role_select)


language_label = Label(root, text="Выберите язык программирования:")
language_label.pack(pady=10)
language_combobox = ttk.Combobox(root, values=programm_languages, state="readonly")
language_combobox.pack()
#language_combobox.bind("<<ComboboxSelected>>", on_language_select)


frame_label = Label(root, text="Введите фреймворк:")
frame_label.pack(pady=10)
frame_entry = Text(root, height=2, width=50, state=DISABLED)
frame_entry.pack()


task_label = Label(root, text="Введите задачу:")
task_label.pack(pady=10)
task_entry = Text(root, height=2, width=50, state=DISABLED)
task_entry.config(bg="#90EE90")
task_entry.pack()

context_label = Label(root, text="Введите контекст задачи или ситуации:")
context_label.pack(pady=10)
context_entry = Text(root, height=4, width=50, state=DISABLED)
context_entry.config(bg="#90EE90")
context_entry.pack()

# Текстовое поле для ввода формата
format_label = Label(root, text="Введите формат:")
format_label.pack(pady=10)
format_entry = Text(root, height=1, width=50, state=DISABLED)
format_entry.config(bg="#90EE90")
format_entry.pack()

tone_label = Label(root, text="Выберете тон:")
tone_label.pack(pady=10)
tone_combobox = ttk.Combobox(root, values=tone, state="readonly")
tone_combobox.pack()
#tone_combobox.bind("<<ComboboxSelected>>", on_tone_select)

# Текстовое поле для ввода примеров
example_label = Label(root, text="Введите пример:")
example_label.pack(pady=10)
example_entry = Text(root, height=4, width=50, state=DISABLED)
example_entry.event_generate('<<Paste>>')
example_entry.pack()

# Кнопка "Добавить пример"
add_example_button = Button(root, text="Добавить пример", command=add_example)
add_example_button.pack(pady=10)

next_button = Button(root, text="Получить промт", command=on_next_click, state=DISABLED)
next_button.pack(pady=10)


# Запуск основного цикла обработки событий
root.mainloop()

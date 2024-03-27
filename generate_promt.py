from tkinter import *
from tkinter import ttk  # Импорт ttk модуля

root = Tk()
root.title("Генерация промта")
root.geometry("750x800")
roles = ["Программист", "Проектировщик", "Разработчик Базы Данных", "Разработчик веб-ресурса", "Технический писатель документации"]
programm_languages = ["Python", "Javascript", "CSS", "Html", "R", "-"]
tone = ["Профессиональный", "Ответственный", "Вежливый", "Уважительный", "Ясный", "-"]
# Список для хранения примеров
examples_list = []
result = []
def add_example():
    example_text = example_entry.get("1.0", "end-1c")  # Получаем текст из текстового поля
    if example_text:
        examples_list.append(example_text)  # Добавляем пример в список
        example_entry.delete("1.0", "end")  # Очищаем текстовое поле

def on_next_click():
    context = context_entry.get("1.0", "end-1c")
    task = task_entry.get("1.0", "end-1c")
    # Проверка полей task и context
    if not task.strip():
        task_entry.config(bg="red")
        return
    else:
        task_entry.config(bg="white")

    if not context.strip():
        context_entry.config(bg="red")
        return
    else:
        context_entry.config(bg="white")

    format = format_entry.get("1.0", "end-1c")
    frame = frame_entry.get("1.0", "end-1c")
    selected_role = role_combobox.get()
    selected_language = language_combobox.get()
    selected_tone = tone_combobox.get()
    result.append('Программист: Занимается созданием и разработкой программного обеспечения. Эта роль требует глубокого понимания языков программирования, алгоритмов и структур данных. Пишет код для создания программ, приложений или веб-сайтов.' +
                   'Проектировщик: Отвечает за разработку дизайна и архитектуры программных проектов. Работает над созданием общей структуры проекта, определяет основные компоненты системы и их взаимодействие, а также учитывает требования к производительности, масштабируемости и безопасности.' +
                   'Разработчик Базы Данных: Специализируется на создании и управлении базами данных. Проектирует структуру баз данных, определяет таблицы, отношения и индексы, а также разрабатывает запросы для доступа к данным и обеспечивает их целостность и безопасность.' +
                    'Разработчик веб-ресурса: Создает веб-приложения, сайты и интерфейсы. Работает с языками разметки (HTML, CSS), клиентскими скриптами (JavaScript) и серверными технологиями (например, PHP, Python, Ruby), чтобы создавать динамические и интерактивные веб-ресурсы.' +
                    'Технический писатель документации: Ответственен за создание и поддержание технической документации. Разрабатывает инструкции пользователя, руководства по эксплуатации, технические спецификации и другие документы, необходимые для использования и понимания продуктов и сервисов.')
    if selected_role:
        result.append("Твоя роль: " + selected_role + '.')
    if selected_language:
        result.append("Реши задачу на этом языке: " + selected_language + '.')
    if frame != "":
        result.append("Используй фреймворк:  " + frame + '.')
    if context != "":
        result.append(context + '.')
    if task != "":
        result.append(task + '.')
    if selected_tone:
        result.append("Используй этот тон в ответе: " + selected_tone + '.')
    if format != "":
        result.append("Дай ответ в формате: " + format + '.')

    if examples_list:
        result.append("Сразу не отвечай, дождись, пока я отправлю " + str(len(examples_list)) + " примеров.")
        for i, example in enumerate(examples_list, start=1):
            result.append(f"Пример {i}: {example}")

    with open("output.txt", "w") as file:
        pass  # Очищаем файл

    # Запись списка result в файл
    with open("output.txt", "w") as file:
        for item in result:
            file.write("%s\n" % item)
            file.write("%s\n")
    return



def on_tone_select(event):
    selected_tone = tone_combobox.get()
    if selected_tone:
        example_entry.config(state=NORMAL)

def on_role_select(event):
    selected_role = role_combobox.get()
    if selected_role:
        next_button.config(state=NORMAL)

def on_language_select(event):
    selected_language = language_combobox.get()
    if selected_language:
        task_entry.config(state=NORMAL)
        format_entry.config(state=NORMAL)
        context_entry.config(state=NORMAL)
        frame_entry.config(state=NORMAL)

# Создание выпадающего списка для выбора роли
role_label = Label(root, text="Выберите роль:")
role_label.pack(pady=10)

role_combobox = ttk.Combobox(root, values=roles, state="readonly")
role_combobox.pack()
# Привязка события выбора значения в Combobox к функции on_role_select
role_combobox.bind("<<ComboboxSelected>>", on_role_select)

# Выпадающий список для выбора языка программирования
language_label = Label(root, text="Выберите язык программирования:")
language_label.pack(pady=10)
language_combobox = ttk.Combobox(root, values=programm_languages, state="readonly")
language_combobox.pack()
language_combobox.bind("<<ComboboxSelected>>", on_language_select)

# Текстовое поле для ввода задачи
frame_label = Label(root, text="Выберете фреймворк:")
frame_label.pack(pady=10)
frame_entry = Text(root, height=2, width=50, state=DISABLED)
frame_entry.pack()


# Текстовое поле для ввода задачи
task_label = Label(root, text="Введите задачу:")
task_label.pack(pady=10)
task_entry = Text(root, height=2, width=50, state=DISABLED)
task_entry.pack()

context_label = Label(root, text="Введите контекст задачи:")
context_label.pack(pady=10)
context_entry = Text(root, height=4, width=50, state=DISABLED)
context_entry.pack()

# Текстовое поле для ввода формата
format_label = Label(root, text="Введите формат:")
format_label.pack(pady=10)
format_entry = Text(root, height=1, width=50, state=DISABLED)
format_entry.pack()

tone_label = Label(root, text="Выберете тон:")
tone_label.pack(pady=10)
tone_combobox = ttk.Combobox(root, values=tone, state="readonly")
tone_combobox.pack()
tone_combobox.bind("<<ComboboxSelected>>", on_tone_select)

# Текстовое поле для ввода примеров
example_label = Label(root, text="Введите пример:")
example_label.pack(pady=10)
example_entry = Text(root, height=4, width=50, state=DISABLED)
example_entry.pack()

# Кнопка "Добавить пример"
add_example_button = Button(root, text="Добавить пример", command=add_example)
add_example_button.pack(pady=10)

next_button = Button(root, text="Получить промт", command=on_next_click, state=DISABLED)
next_button.pack(pady=10)


# Запуск основного цикла обработки событий
root.mainloop()

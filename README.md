# structureGen | MK_TREEgen

![License: MIT](https://img.shields.io/badge/License-WTFPL-yellow.svg)
![Python Version](https://img.shields.io/badge/python-3.6%2B-blue.svg)

```
  sSSs  sdSS_SSSSSSbs    sSSSSs    sSSs   .S_sSSs
 d%%SP  YSSS~S%SSSSSP   d%%%%SP   d%%SP  .SS~YS%%b
d%S'         S%S       d%S'      d%S'    S%S   `S%b
S%|          S%S       S%S       S%S     S%S    S%S
S&S          S&S       S&S       S&S     S&S    S&S
Y&Ss         S&S       S&S       S&S_Ss  S&S    S&S
`S&&S        S&S       S&S       S&S~SP  S&S    S&S
  `S*S       S&S       S&S sSSs  S&S     S&S    S&S
   l*S       S*S       S*b `S%%  S*b     S*S    S*S
  .S*P       S*S       S*S   S%  S*S.    S*S    S*S
sSS*S        S*S        SS_sSSS   SSSbs  S*S    S*S
YSS'         S*S         Y~YSSY    YSSP  S*S    SSS
             SP                          SP
             Y                           Y   by mkultra69
```

**Быстрый скаффолдер для ваших проектов.**

`structureGen` — это простой, но мощный Python-скрипт для быстрого создания структуры каталогов и файлов проекта на основе текстовой схемы.

## 🚀 Основные возможности

- **Создание вложенных директорий:** Легко описывайте любую глубину вложенности папок.
- **Создание файлов с содержимым:** Добавляйте начальный код или текст в файлы прямо из схемы.
- **Интуитивно понятный синтаксис:** Схема структуры напоминает вывод команды `tree`, что делает её наглядной и простой для чтения.
- **Кросс-платформенность:** Работает на Windows, macOS и Linux.
- **Интерактивность:** Просто запустите скрипт и вставьте вашу схему прямо в консоль.

## ⚙️ Установка

Никакой специальной установки не требуется. Достаточно иметь **Python 3.6+**.

1.  Клонируйте репозиторий:
    ```bash
    git clone https://github.com/MKultra6969/MK_TREEgen
    cd MK_TREEgen
    ```
2.  Или просто скачайте файл `structureGen.py`.

## 📖 Как использовать

1.  Откройте терминал в той папке, где вы хотите создать проект.
2.  Запустите скрипт:
    ```bash
    python structureGen.py
    ```
3.  Скрипт попросит вставить структуру проекта.
4.  Вставьте заранее подготовленную схему в терминал.
5.  Нажмите `Ctrl+D` (для Linux/macOS) или `Ctrl+Z` + `Enter` (для Windows), чтобы завершить ввод.
6.  Скрипт обработает схему и создаст все указанные папки и файлы в текущей директории.

### Синтаксис схемы

Схема — это простой текст, где каждая строка описывает папку или файл.

-   **Директории** должны заканчиваться на слеш (`/`).
-   **Файлы** указываются просто по имени (`main.py`, `README.md`).
-   **Содержимое файла** можно указать после символа `#`. Всё, что идет после `#`, будет записано в файл.
-   **Вложенность** определяется отступами (пробелами или символами `│ ├─ └`). Скрипт автоматически распознает уровень вложенности.

### Пример схемы

Вот пример схемы для простого веб-проекта:

```plaintext
my-shit-app/
  ├── static/
  │   ├── css/
  │   │   └── style.css # body { font-family: sans-serif; }
  │   └── js/
  │       └── main.js # console.log("App loaded!");
  ├── templates/
  │   └── index.html # <!DOCTYPE html><html><head><title>My App</title></head></html>
  ├── app.py # print("Hello, World!")
  ├── requirements.txt # flask
  └── .gitignore # __pycache__/
```

### Пример работы

1.  **Запуск скрипта:**
    ```bash
    $ python structureGen.py
    ```
2.  **Ввод схемы:**
    *(Вставляешь текст схемы, показанный выше, и нажимаете Ctrl+D)*
3.  **Вывод в консоли:**
    ```
    ✅ Ввод получен. Начинаю обработку...

    🧠 Парсинг текстовой схемы проекта...

    🚀 Начинаю создание структуры проекта в директории: /home/user/projects

    ✅ Создана директория: /home/user/projects/my-shit-app
    ✅ Создана директория: /home/user/projects/my-shit-app/static
    ✅ Создана директория: /home/user/projects/my-shit-app/static/css
    📄 Создан файл:        /home/user/projects/my-shit-app/static/css/style.css
    ✅ Создана директория: /home/user/projects/my-shit-app/static/js
    📄 Создан файл:        /home/user/projects/my-shit-app/static/js/main.js
    ✅ Создана директория: /home/user/projects/my-shit-app/templates
    📄 Создан файл:        /home/user/projects/my-shit-app/templates/index.html
    📄 Создан файл:        /home/user/projects/my-shit-app/app.py
    📄 Создан файл:        /home/user/projects/my-shit-app/requirements.txt
    📄 Создан файл:        /home/user/projects/my-shit-app/.gitignore

    🎉 Структура проекта успешно создана!
    ```

## 📄 З.Ы.

КАК ВСЕГДА С НЕНАВИСТЬЮ К ЛЮДЯМ, ЛИЦЕНЗИЯ WTFPL

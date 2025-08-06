import os
import sys

class Colors:
    RESET = '\033[0m'
    BOLD = '\033[1m'

    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    BRIGHT_CYAN = '\033[96m'
    BRIGHT_YELLOW = '\033[93m'
    BRIGHT_GREEN = '\033[92m'
    BRIGHT_RED = '\033[91m'
    BRIGHT_BLUE = '\033[94m'
    BRIGHT_MAGENTA = '\033[95m'


LOGO = """
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
             Y                           Y
"""


def display_logo():
    print(f"{Colors.BRIGHT_CYAN}{LOGO}{Colors.RESET}")
    author_line = "MK TREEgen // made by mkultra69"
    print(f"{Colors.BRIGHT_YELLOW}{author_line.center(80)}{Colors.RESET}")
    print("=" * 70)


def parse_structure_schema(schema: str) -> dict:
    lines = schema.strip().split('\n')

    if not lines or not lines[0].strip().endswith('/'):
        root = {}
        path_stack = [root]
        indent_stack = [-1]
    else:
        root = {}
        path_stack = [root]
        indent_stack = [-1]

    for line in lines:
        if not line.strip():
            continue

        indent = len(line) - len(line.lstrip(' │├─└'))
        clean_line = line.lstrip(' │├─└').strip()
        parts = clean_line.split('#', 1)
        name = parts[0].strip()
        content = parts[1].strip() if len(parts) > 1 else ""

        while indent <= indent_stack[-1]:
            path_stack.pop()
            indent_stack.pop()

        parent_dir = path_stack[-1]

        if name.endswith('/'):
            dir_name = name.rstrip('/')
            new_dir = {}
            parent_dir[dir_name] = new_dir
            path_stack.append(new_dir)
            indent_stack.append(indent)
        else:
            parent_dir[name] = content
    return root


def create_project_structure(base_path: str, structure: dict):
    for name, content in structure.items():
        current_path = os.path.join(base_path, name)
        if isinstance(content, dict):
            try:
                os.makedirs(current_path, exist_ok=True)
                print(f"{Colors.BRIGHT_GREEN}✅ Создана директория: {current_path}{Colors.RESET}")
                create_project_structure(current_path, content)
            except OSError as e:
                print(f"{Colors.BRIGHT_RED}❌ Ошибка при создании директории {current_path}: {e}{Colors.RESET}")
        else:
            try:
                if os.path.exists(current_path):
                    print(f"{Colors.YELLOW}⚠️  Файл уже существует, пропускаю: {current_path}{Colors.RESET}")
                    continue
                with open(current_path, 'w', encoding='utf-8') as f:
                    if content:
                        f.write(content + '\n')
                print(f"{Colors.GREEN}📄 Создан файл:        {current_path}{Colors.RESET}")
            except IOError as e:
                print(f"{Colors.BRIGHT_RED}❌ Ошибка при создании файла {current_path}: {e}{Colors.RESET}")


def get_multiline_input():
    print(f"{Colors.BRIGHT_BLUE}➡️  Вставьте вашу структуру проекта ниже.{Colors.RESET}")
    print(
        f"{Colors.BRIGHT_BLUE}➡️  Папки должны заканчиваться на '/', содержимое файла указывайте после '#'.{Colors.RESET}")
    print(
        f"{Colors.BRIGHT_BLUE}➡️  Когда закончите, нажмите {Colors.BOLD}Ctrl+D{Colors.RESET}{Colors.BRIGHT_BLUE} (Linux/macOS) или {Colors.BOLD}Ctrl+Z + Enter{Colors.RESET}{Colors.BRIGHT_BLUE} (Windows).{Colors.RESET}")
    print("-" * 70)

    lines = sys.stdin.read()

    print("-" * 70)
    print(f"{Colors.BRIGHT_GREEN}✅ Ввод получен. Начинаю обработку...{Colors.RESET}")
    return lines


if __name__ == "__main__":
    display_logo()

    schema_text = get_multiline_input()

    if not schema_text.strip():
        print(f"\n{Colors.BRIGHT_RED}❌ Схема не была предоставлена. Завершение работы.{Colors.RESET}")
        sys.exit(1)

    try:
        print(f"\n{Colors.BRIGHT_MAGENTA}🧠 Парсинг текстовой схемы проекта...{Colors.RESET}")
        project_dict = parse_structure_schema(schema_text)

        if not project_dict:
            raise ValueError("Схема пуста или не удалось ее распознать.")

        base_dir = os.getcwd()
        print(f"\n{Colors.BRIGHT_MAGENTA}🚀 Начинаю создание структуры проекта в директории: {base_dir}{Colors.RESET}\n")

        create_project_structure(base_dir, project_dict)

        print(f"\n{Colors.BRIGHT_GREEN}{Colors.BOLD}🎉 Структура проекта успешно создана!{Colors.RESET}")

    except Exception as e:
        print(f"\n{Colors.BRIGHT_RED}{Colors.BOLD}🔥 Произошла критическая ошибка: {e}{Colors.RESET}")
        sys.exit(1)

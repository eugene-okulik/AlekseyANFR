import os
import argparse
import re
from datetime import datetime
from collections import OrderedDict
from colorama import Fore, Style, init

init(autoreset=True)


TIMESTAMP_PATTERN = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}[.,]\d{3})')

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help="File or folder path")
    parser.add_argument('-d', '--date', help="Date for search (YYYY-MM-DD)")
    parser.add_argument('--text', required=True, help="Text to search")
    parser.add_argument('--full', action='store_true', help="Show only first match")
    return parser.parse_args()


def parse_datetime(timestamp_str):
    timestamp_str = timestamp_str.replace('.', ',')
    return datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S,%f')


def read_log_file(filepath):
    blocks = OrderedDict()
    current_key = None
    current_block_lines = []

    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.rstrip('\n')
            match = TIMESTAMP_PATTERN.match(line)
            if match:
                if current_key is not None:
                    blocks[current_key] = '\n'.join(current_block_lines)

                timestamp_str = match.group(1)
                current_key = parse_datetime(timestamp_str)
                current_block_lines = [line]
            else:

                if current_key is not None:
                    current_block_lines.append(line)
                else:
                    pass
        if current_key is not None:
            blocks[current_key] = '\n'.join(current_block_lines)
    return blocks

def extract_context(line, search_word, context_size=5):

    words = line.split()
    index = -1
    for i, w in enumerate(words):
        if search_word in w:
            index = i
            break
    if index == -1:
        return line.strip()

    start = max(0, index - context_size)
    end = min(len(words), index + context_size + 1)
    context_words = words[start:end]
    context_words[index - start] = Fore.RED + context_words[index - start] + Style.RESET_ALL
    return ' '.join(context_words)

def search_in_block(block_text, search_text):

    results = []
    lines = block_text.split('\n')
    for i, line in enumerate(lines, start=1):
        if search_text in line:
            context = extract_context(line, search_text)
            results.append((i, context))
    return results


def analyze_logs(path, search_text, date_filter=None, first_only=False):
    abs_path = os.path.abspath(path)
    print(f"Проверяем путь: {abs_path}")
    if os.path.isfile(abs_path):
        files = [abs_path]
    elif os.path.isdir(abs_path):
        files = [os.path.join(abs_path, f) for f in os.listdir(abs_path) if os.path.isfile(os.path.join(abs_path, f))]
    else:
        print(f"Ошибка: путь {abs_path} не существует")
        return

    found_any = False

    for file_path in files:
        blocks = read_log_file(file_path)
        if date_filter:
            try:
                date_obj = datetime.strptime(date_filter, '%Y-%m-%d').date()
            except ValueError:
                print("Неверный формат даты. Используйте YYYY-MM-DD.")
                return
            blocks = {k: v for k, v in blocks.items() if k.date() == date_obj}

        for block_time, block_text in blocks.items():
            results = search_in_block(block_text, search_text)
            if results:
                found_any = True
                print(f"{Fore.GREEN}Файл: {os.path.basename(file_path)}, Время блока: {block_time}{Style.RESET_ALL}")
                for line_num, context in results:
                    print(f"  Строка в блоке: {line_num}")
                    print(f"  Контекст: {context}")
                print('-' * 80)
                if first_only:
                    return

    if not found_any:
        print(f"Текст '{search_text}' не найден в указанных логах.")

def main():
    args = parse_args()
    analyze_logs(args.file, args.text, args.date, args.full)

if __name__ == '__main__':
    main()

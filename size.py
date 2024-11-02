# !/usr/bin/python3

import os

def get_size(path):
    """
    Возвращает размер директории или файла в байтах.
    """
    if os.path.isfile(path):
        return os.path.getsize(path)
    else:
        total_size = 0
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            total_size += get_size(item_path)
        return total_size

def format_size(size):
    """
    Форматирует размер в байтах в более читабельный вид.
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.1f}{unit}"
        size /= 1024.0
    return f"{size:.1f}PB"

def analyze_directory(directory):
    """
    Анализирует размер каждой директории и файла в указанной директории 
    и выводит информацию в отсортированном порядке по убыванию размера.
    """
    items_with_sizes = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        size = get_size(item_path)
        formatted_size = format_size(size)
        items_with_sizes.append((item_path, size, formatted_size))

    # Сортировка по размеру в байтах по убыванию
    items_with_sizes.sort(key=lambda x: x[1], reverse=True)

    # Вывод отсортированной информации
    for item_path, size, formatted_size in items_with_sizes:
        print(f"{item_path}: {formatted_size}")

if __name__ == "__main__":
    current_directory = os.getcwd()
    analyze_directory(current_directory)

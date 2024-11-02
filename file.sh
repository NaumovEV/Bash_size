#!/bin/bash

# Функция для подсчета размера директории
function calculate_dir_size() {
    du -sh $1
}

# Функция для подсчета размера файла
function calculate_file_size() {
    du -h $1
}

# Анализ размера каждой директории и файла
echo "Размер каждой директории в текущей директории:"
for dir in */; do
    calculate_dir_size $dir
done

echo ""

echo "Размер каждого файла в текущей директории:"
for file in *; do
    if [ -f $file ]; then
        calculate_file_size $file
    fi
done

echo ""

# Сортировка по уменьшению размера
echo "Сортировка по уменьшению размера:"
du -hs * | sort -hr


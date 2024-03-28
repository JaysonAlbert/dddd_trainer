#!/bin/bash

# 定义文件所在的目录，这里假设文件在当前目录中
directory="./projects/piaoxingqiu/datasets/images"

# 定义labels文件的路径
labels_file="./projects/piaoxingqiu/datasets/labels.txt"

# 检查labels文件是否存在
if [ ! -f "$labels_file" ]; then
  echo "Labels文件不存在: $labels_file"
  exit 1
fi

# 定义一个变量来跟踪缺失的文件数量
missing_count=0
total_count=0

# 读取labels文件并提取文件名
while read -r line; do
  # 提取每一行的第一个字段作为文件名
  filename=$(echo "$line" | awk '{print $1}')

  # 检查文件是否存在
  if [ ! -f "${directory}/${filename}" ]; then
    echo "文件 ${filename} 不存在."
    ((missing_count++))
  else
    ((total_count++))
  fi 
done < "$labels_file"

# 输出缺失文件的总数
if [ $missing_count -ne 0 ]; then
  echo "共有 ${missing_count} 个文件缺失."
else
  echo "所有文件都存在, 共有 ${total_count}个文件"
fi

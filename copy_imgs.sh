#!/bin/bash

# 定义源目录和目标目录
source_directory="./projects/piaoxingqiu/datasets_o/images"
destination_directory="./projects/piaoxingqiu/datasets/images"

# 检查目标目录是否存在，如果不存在则创建
if [ ! -d "$destination_directory" ]; then
  mkdir -p "$destination_directory"
fi

# 循环遍历并复制文件
for i in {29000..29999}
do
  # 构建文件名
  filename="${i}.png"
  
  # 复制文件
  cp "${source_directory}/${filename}" "${destination_directory}/"
done

echo "所有文件已经成功复制到 ${destination_directory}"

import os

# 文件夹路径
folder_path = 'projects/piaoxingqiu/datasets_p_zh/images'
# 获取所有PNG文件
files = [f for f in os.listdir(folder_path) if f.endswith('.png')]
# 对文件进行排序，以确保命名的连贯性（可选）
files.sort()

# 重命名文件
for i, file in enumerate(files):
    # 构建原始文件路径
    original_path = os.path.join(folder_path, file)
    # 构建新文件路径
    new_path = os.path.join(folder_path, f"{i}.png")
    # 重命名
    os.rename(original_path, new_path)

print("完成重命名")

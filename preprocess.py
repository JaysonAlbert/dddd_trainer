import os

# 定义映射字典
number_map = {
    "0": "零",
    "1": "壹",
    "2": "贰",
    "3": "叁",
    "4": "肆",
    "5": "伍",
    "6": "陆",
    "7": "柒",
    "8": "捌",
    "9": "玖",
}

operator_map = {
    "+": "加",
    "-": "减",
    "x": "乘",
    "/": "除",
}


def convert_to_chinese(expression):
    result = ""
    for char in expression:
        if char in number_map:
            result += number_map[char]
        elif char in operator_map:
            result += operator_map[char]
        else:
            result += char  # 保持非数字和非运算符字符不变
    return result


def convert_to_arithmetic(chinese_expression):
    reverse_number_map = {v: k for k, v in number_map.items()}
    reverse_operator_map = {v: k for k, v in operator_map.items()}

    result = ""
    for char in chinese_expression:
        if char in reverse_number_map:
            result += reverse_number_map[char]
        elif char in reverse_operator_map:
            result += reverse_operator_map[char]
        else:
            result += char  # 保持非数字和非运算符字符不变
    return result

filename = "./projects/piaoxingqiu/datasets_p_zh/raw_labels.txt"

dirname = os.path.dirname(filename)

filename_processed = f"{dirname}/labels.txt"

with open(filename_processed, "w") as f:
    for line in open(filename, "r"):
        parts = line.split("\t")
        image_name = parts[0]
        expression = parts[1]
        chinese_expression = convert_to_chinese(expression)
        result = f"{image_name}\t{chinese_expression}"
        f.write(result)

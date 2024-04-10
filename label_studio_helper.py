import json
import os
from natsort import natsorted
import pandas as pd
import sys


def create_data(image_name, caption):
    if caption:
        return {
            "data": {
                "captioning": "http://10.60.114.123:8081/" + image_name,  # 图片的路径
            },
            "annotations": [
                {
                    "result": [
                        {
                            "value": {"text": [caption]},
                            "type": "textarea",
                            "from_name": "caption",
                            "to_name": "image",
                            "origin": "prediction",
                        }
                    ]
                }
            ],
        }
    else:
        return {
            "data": {
                "captioning": "http://10.60.114.123:8081/" + image_name
            },  # 图片的路径
        }


def sort_key(file_name):
    """
    提取文件名中的数字用于排序。
    """
    # 假设文件名格式为 "数字.png"
    base_name = file_name.split(".")[0]  # 移除后缀
    return int(base_name)  # 将文件名转换为整数


def export_to_studio(input_file, output_file):
    image_path = os.path.join(os.path.dirname(input_file), "images")
    imgs = set()

    # 读取并转换数据
    data = []
    with open(input_file, "r") as f:
        for line in f.readlines():
            parts = line.strip().split("\t")  # 假设使用制表符作为分隔符
            if len(parts) == 2:
                image_name, caption = parts
                imgs.add(image_name)

                data.append(create_data(image_name, caption))

    for file in natsorted(os.listdir(image_path)):
        if file not in imgs:
            data.append(create_data(file, ""))

    # 写入JSON文件
    with open(output_file, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def import_from_studio(input_file, output_file):
    df = pd.read_csv(input_file, sep="\t")

    df = df[["captioning", "caption"]]
    df["captioning"] = df["captioning"].str.split("/").str[-1]
    df.to_csv(output_file, sep="\t", index=False, header=False)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "export":
        print("Exporting to Studio...")
        # 输入文件和输出文件
        input_file = "./projects/piaoxingqiu/datasets/labels.txt"
        output_file = "./projects/piaoxingqiu/datasets/labels.json"
        export_to_studio(input_file, output_file)
    else:
        print("Importing from Studio...")
        import_path = (
            "/home/wangjie/Downloads/project-1-at-2024-04-10-06-53-4e9ffbb7.csv"
        )
        output_file = "./projects/piaoxingqiu/datasets/studio_labels.txt"
        import_from_studio(import_path, output_file)
    
    print("Done!")

import ddddocr
import shutil
import os
import time

det = ddddocr.DdddOcr(
    show_ad=False,
    import_onnx_path="./projects/piaoxingqiu/models/efficientnet_v2_s_3_v1000_32_d05_lr01_pretrained_zh_cn/piaoxingqiu_0.984375_53_1500_2024-04-08-10-13-35.onnx",
    charsets_path="./projects/piaoxingqiu/models/efficientnet_v2_s_3_v1000_32_d05_lr01_pretrained_zh_cn/charsets.json",
)


def find_replaced_characters(a, b):
    """
    Find and return the characters in string 'a' that were replaced to get string 'b'.

    Parameters:
    a (str): Original string.
    b (str): String obtained by replacing some characters in 'a'.

    Returns:
    list of tuples: A list where each tuple contains the position of the replaced character
                    in 'a', the original character from 'a', and the new character from 'b'.
    """
    replaced_characters = []
    for i in range(len(a)):
        if a[i] != b[i]:
            replaced_characters.append((a[i], b[i]))
    return replaced_characters


def validate(path, copy=False):
    base_path = os.path.dirname(path)
    image_path = os.path.join(base_path, "images")
    with open(path, "r") as f:
        correct_count = 0
        total_count = 0
        os.makedirs("./eval", exist_ok=True)

        start_time = time.time()

        for line in f:
            image, label = line.split("\t")
            total_count = total_count + 1
            image_name = os.path.join(image_path, image)
            with open( image_name, "rb") as a:
                image_bytes = a.read()
                pred = det.classification(image_bytes)
                if pred == label.strip():
                    correct_count = correct_count + 1
                else:
                    if copy:
                        shutil.copy(
                            image_name,
                            f"./eval/{image}",
                        )
                    try:
                        print(
                            image,
                            pred,
                            label.strip(),
                            find_replaced_characters(pred, label.strip()),
                        )
                    except:
                        print(image, pred, label.strip())

        print(
            f"总测试量：{total_count}，正确：{correct_count}，错误：{total_count - correct_count} , 正确率：{correct_count / total_count}, 共花了{time.time() - start_time}s"
        )


def eval():
    for i in range(3600, 3630):
        with open(f"./projects/piaoxingqiu/datasets/images/{i}.png", "rb") as f:
            image_bytes = f.read()

        shutil.copy(
            f"./projects/piaoxingqiu/datasets/images/{i}.png", f"./eval/{i}.png"
        )

        print(det.classification(image_bytes))

    print("\n\n")


if __name__ == "__main__":
    validate("./projects/piaoxingqiu/datasets_zh/labels_val.txt")
    validate("./projects/piaoxingqiu/datasets_p/labels_val.txt")
    validate("./projects/piaoxingqiu/datasets_p_zh/labels.txt")
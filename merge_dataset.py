import os
import shutil
import sys
from natsort import natsorted


def read_samples(path):
    try:
        with open(path, "r") as f:
            lines = f.read().splitlines()  # 使用splitlines()更可靠地分割行
            images = []
            labels = []
            for line in lines:
                parts = line.split("\t")
                if len(parts) != 2:
                    print(f"Warning: Skipping malformed line: {line}")
                    continue
                image, label = parts
                images.append(image.strip())
                labels.append(label.strip())
            return images, labels
    except FileNotFoundError:
        print(f"Error: File {path} not found.")
        return [], []
    except Exception as e:
        print(f"An error occurred: {e}")
        return [], []


def merge_datasets(
    source_labels_path, target_labels_path, num_sample_to_merge, dry_run=True
):
    num_merged = 0

    source_directory = os.path.join(os.path.dirname(source_labels_path), "images")
    destination_directory = os.path.join(os.path.dirname(target_labels_path), "images")

    # 检查目标目录是否存在，如果不存在则创建
    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    source_images, source_labels = read_samples(source_labels_path)
    target_images, target_labels = read_samples(target_labels_path)

    copied_labels = []

    for img, label in zip(source_images, source_labels):
        if num_merged >= num_sample_to_merge:
            break  # 跳出循环，不再复制文件

        if img in target_images:
            continue

        filename = os.path.join(source_directory, img)
        if not os.path.exists(filename):
            print(f"Warning: File {filename} does not exist.")
            continue
        if dry_run:
            print(f"Would copy {filename} to {destination_directory}")
        else:
            shutil.copy(filename, destination_directory)
        copied_labels.append((img, label))
        num_merged += 1

    print(f"已成功复制 {num_merged} 个文件")

    merge_datasets = natsorted(list(zip(target_images, target_labels)) + copied_labels)

    if len(copied_labels) > 0:
        if dry_run:
            for img, label in merge_datasets:
                print(f"Would write: {img}\t{label}")
        else:
            with open(target_labels_path, "w") as f:
                for img, label in merge_datasets:
                    f.write(f"{img}\t{label}\n")


if __name__ == "__main__":
    num_sample_to_merge = 1000

    source_labels_path = "./projects/piaoxingqiu/datasets_p/labels.txt"
    target_labels_path = "./projects/piaoxingqiu/datasets/labels.txt"
    dry_run = len(sys.argv) > 1 and sys.argv[1] == "dry_run"

    merge_datasets(
        source_labels_path, target_labels_path, num_sample_to_merge, dry_run=dry_run
    )

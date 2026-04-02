# 保存为 debug_annotations.py
import os
import glob


def check_annotations():
    # 检查标注文件目录
    annotations_dir = r"E:\study\daima\ucf24\rgb-images\annotations"

    if not os.path.exists(annotations_dir):
        print(f"标注目录不存在: {annotations_dir}")
        # 尝试其他可能的路径
        possible_paths = [
            r"E:\study\daima\ucf24\annotations",
            r"E:\study\daima\ucf24\groundtruths",
            r"E:\study\daima\ucf24\rgb-images",
        ]
        for path in possible_paths:
            if os.path.exists(path):
                print(f"找到路径: {path}")
                annotations_dir = path
                break

    print(f"检查目录: {annotations_dir}")

    # 列出所有文件
    all_files = os.listdir(annotations_dir)
    txt_files = [f for f in all_files if f.endswith('.txt')]

    print(f"\n总共 {len(all_files)} 个文件，其中 {len(txt_files)} 个txt文件")

    # 检查前5个txt文件
    for txt_file in txt_files[:5]:
        file_path = os.path.join(annotations_dir, txt_file)
        print(f"\n=== 检查文件: {txt_file} ===")

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                print(f"总行数: {len(lines)}")

                # 显示前3行
                for i, line in enumerate(lines[:3]):
                    line = line.strip()
                    if line:
                        split_line = line.split()
                        print(f"  第{i + 1}行: 长度={len(split_line)}, 内容: {line[:50]}...")

                        # 如果是标注行，应该有5个值
                        if len(split_line) == 5:
                            try:
                                class_id = split_line[0]
                                x, y, w, h = map(float, split_line[1:])
                                print(f"    格式正确: class={class_id}, x={x:.4f}, y={y:.4f}, w={w:.4f}, h={h:.4f}")
                            except ValueError as e:
                                print(f"    数值转换错误: {e}")
                        else:
                            print(f"    警告: 期望5个值，实际{len(split_line)}个")

        except Exception as e:
            print(f"读取文件时出错: {e}")


if __name__ == "__main__":
    check_annotations()
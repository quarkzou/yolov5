"""
Descriptions: 自动化生成YOLO格式的标签
Author: quarkzou
Date: 16th Nov., 2021
"""
from utils.general import print_args
import argparse
from pathlib import Path
import os

FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]  # YOLOv5 root directory




def run(label_template, image_path, label_path):
    print(label_template)
    content = read_template_content(label_template)
    if len(content) > 0:
        if os.path.isdir(image_path):
            for image_file in os.listdir(image_path):
                image_file_path = os.path.join(image_path, image_file)
                if os.path.isfile(image_file_path):
                    label_file_path = os.path.join(label_path, os.path.splitext(image_file)[0] + '.txt')
                    print('writing label: ' + image_file)
                    f = open(label_file_path, 'w+')
                    f.write(content)
                    f.close()




def read_template_content(label_template):
    """
    读取标签模板文件内容
    """
    f = open(label_template, 'r+')
    content = f.read()
    f.close()
    return content



def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--label-template', type=str, default=ROOT / 'datasets/pubgm/labels/template.txt',
                        help='标签模板,基于这个标签文件生成其他样本的标签')
    parser.add_argument('--image-path', type=str, default=ROOT / 'datasets/pubgm/images/', help='图片文件夹')
    parser.add_argument('--label-path', type=str, default=ROOT / 'datasets/pubgm/labels_tmp/', help='标签文件夹')

    opt = parser.parse_args()
    print_args(FILE.stem, opt)
    return opt


def main(opt):
    run(**vars(opt))


if __name__ == "__main__":
    opt = parse_opt()
    main(opt)

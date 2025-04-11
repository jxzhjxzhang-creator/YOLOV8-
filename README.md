# 垃圾分类检测系统 (基于YOLOv8和Realsense)

## 项目概述
本项目使用YOLOv8目标检测模型和Intel Realsense深度相机实现实时垃圾分类检测系统。系统能够通过摄像头实时检测视野中的垃圾物品，并对其进行分类标注。

## 功能特性
- 实时物体检测与分类
- 支持Intel Realsense系列摄像头
- 基于YOLOv8的高精度检测模型
- 可配置的检测置信度阈值
- 实时显示检测结果和分类标签

## 环境要求
- Python 3.7+
- PyTorch
- OpenCV
- Intel Realsense SDK (pyrealsense2)
- Ultralytics YOLOv8

## 安装指南
1. 克隆本仓库
   ```bash
   git clone [repository_url]
   cd trash-classification-detection
2、安装依赖
   ```bash
pip install -r requirements.txt
或手动安装:
   ```bash
pip install torch torchvision opencv-python pyrealsense2 ultralytics numpy
下载YOLOv8模型权重文件(best.pt)和数据集配置文件(VOC-trash.yaml)，放置在项目根目录下

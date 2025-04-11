垃圾分类检测系统 (基于YOLOv8和Realsense)
项目概述
本项目使用YOLOv8目标检测模型和Intel Realsense深度相机实现实时垃圾分类检测系统。系统能够通过摄像头实时检测视野中的垃圾物品，并对其进行分类标注。

功能特性
实时物体检测与分类
支持Intel Realsense系列摄像头
基于YOLOv8的高精度检测模型
可配置的检测置信度阈值
实时显示检测结果和分类标签
环境要求
Python 3.7+
PyTorch
OpenCV
Intel Realsense SDK (pyrealsense2)
Ultralytics YOLOv8
安装指南
克隆本仓库
bash
git clone [repository_url]
cd trash-classification-detection
安装依赖
bash
pip install -r requirements.txt
或手动安装:
bash
pip install torch torchvision opencv-python pyrealsense2 ultralytics numpy
下载YOLOv8模型权重文件(best.pt)和数据集配置文件(VOC-trash.yaml)，放置在项目根目录下
使用说明
连接Intel Realsense相机到计算机
运行主程序:
bash
python trash_detection.py
程序将打开摄像头并显示实时检测结果
按键盘q键退出程序
文件结构
trash-classification-detection/
├── trash_detection.py       # 主程序文件
├── best.pt                  # YOLOv8模型权重文件
├── VOC-trash.yaml           # 数据集配置文件
├── README.md                # 项目说明文件
└── requirements.txt         # 依赖包列表
自定义配置
修改conf参数调整检测置信度阈值(0-1之间)
更换模型权重文件(best.pt)以使用不同的训练模型
修改VOC-trash.yaml配置文件以适应不同的分类需求
注意事项
确保Realsense相机已正确安装驱动并连接到计算机
首次运行可能需要等待模型加载(约几秒钟)
检测性能取决于硬件配置，建议使用支持CUDA的GPU加速
未来改进计划

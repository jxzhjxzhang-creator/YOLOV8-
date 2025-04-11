import cv2
import pyrealsense2 as rs
from ultralytics import YOLO
import numpy as np
# 加载YOLO模型
model_path = "/home/zjx/Desktop/garbage_yolo/ultralytics/ultralytics/weights/last.pt"
data_path = "/home/zjx/Desktop/garbage_yolo/ultralytics/ultralytics/cfg/datasets/VOC-trash.yaml"
model = YOLO(model_path)

# 配置Realsense相机
pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# 启动相机
pipeline.start(config)

try:
    while True:
        # 等待一帧数据
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        if not color_frame:
            continue

        # 转换为numpy数组
        color_image = np.asanyarray(color_frame.get_data())

        # 使用YOLO模型进行预测
        results = model.predict(source=color_image, conf=0.5, data=data_path)

        # 在图像上绘制检测结果
        annotated_frame = results[0].plot()

        # 显示结果
        cv2.imshow('YOLO Realsense Detection', annotated_frame)

        # 按'q'退出
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # 停止相机
    pipeline.stop()
    cv2.destroyAllWindows()
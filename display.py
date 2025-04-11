from rknn.api import RKNN

rknn = RKNN()
rknn.config(
    target_platform='rk3588',
    quantized_dtype='asymmetric_quantized-8',
    float_dtype='float16'
)

# 加载 ONNX
ret = rknn.load_onnx(model='best.onnx', inputs=['images'], input_size_list=[[3, 640, 640]])
assert ret == 0, "Load ONNX failed"

# 构建 RKNN
ret = rknn.build(do_quantization=True, dataset='./calib.txt')  # 需准备校准数据
assert ret == 0, "Build RKNN failed"

# 导出 RKNN
rknn.export_rknn('best.rknn')
import tempfile

# 获取系统的临时文件目录
temp_dir = tempfile.gettempdir()
print(f"系统临时文件目录: {temp_dir}")

# 创建一个临时文件
with tempfile.NamedTemporaryFile(delete=False) as temp_file:
    temp_file.write(b"Hello, world!")
    print(f"临时文件路径: {temp_file.name}")
class CustomOpen:
    def __init__(self, filename):
        self.file = open(filename)

    def __enter__(self):
        """
        with 语句中实例化时调用，返回值赋值给 as f
        """
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        """
        with 语句结束时调用的方法，有三个参数，默认为 None
        """
        self.file.close()


with CustomOpen('README.md') as f:
    contents = f.read()
    print(contents)

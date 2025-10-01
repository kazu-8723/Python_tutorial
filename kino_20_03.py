import zipfile
"""
with zipfile.ZipFile("test.zip", "w") as zf: #zipファイル作成
    zf.write("test.txt")
    zf.write("test.csv")
"""

with zipfile.ZipFile("test2.zip", "w",
                     compression=zipfile.ZIP_DEFLATED,
                     compresslevel=9) as zf: #zipファイル指定有作成
    zf.write("test.txt")
    zf.write("test.csv")

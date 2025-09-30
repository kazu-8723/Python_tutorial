print(dir()) #オブジェクトのアトリビュートを取得

def name_check():
    print("__name__:", __name__)

if __name__ == "__main__":
    name_check()

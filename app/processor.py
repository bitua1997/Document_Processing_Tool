def read_file(file_path:str) ->str:
    with open(file_path,"r",encoding="utf-8")as file:
        return file.read()

content=read_file("../input/sample.txt")
print(content)

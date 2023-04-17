import os

tipos = ['xlsx', 'pdf','txt']


pasta_origem = os.getcwd()
pasta_origem

arquivos = os.listdir(pasta_origem)
arquivos

for tipos_ in tipos:
    if type_ not in os.listdir():
        os.mkdir(tipos_)

for file in arquivos:
    for tipos_ in tipos:
        if '.' + type_ in file:
            old_path = os.path.join(pasta_origem, arquivos)
            new_path = os.path.join(pasta_origem, tipos_, arquivos)

            os.replace(old_path, new_path)





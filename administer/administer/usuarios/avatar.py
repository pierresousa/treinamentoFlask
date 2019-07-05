import os
from flask import current_app
from PIL import Image

def adicionar_avatar(upload_avatar, apelido):

    '''
    Recebe a foto e o apelido do usuario.
    Pega o nome da foto, retira e adiciona o apelido do usuario+(.tipo do arquivo)
    Vai ate a a pasta escolhida e cria o caminho que sera salvo
    Define o tamanho, abre a imagem e edita ela, depois salva no diretorio
    Retorna o nome da imagem
    '''

    filename = upload_avatar.filename

    ext_type = filename.split('.')[-1]

    storage_filename = str(apelido)+'.'+ext_type

    filepath = os.path.join(current_app.root_path, 'static/img/avatares', storage_filename)

    tamanho = (300,300)

    pic = Image.open(upload_avatar)
    pic.thumbnail(tamanho)
    pic.save(filepath)

    return storage_filename
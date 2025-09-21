import os
from gtts import gTTS
import pygame

# Inicializa o mixer do pygame para áudio
pygame.mixer.init()

# Dicionário de idiomas suportados (códigos do gTTS)
idiomas = {
    '1': ('Português', 'pt'),
    '2': ('Espanhol', 'es'),
    '3': ('Inglês', 'en'),
    '4': ('Francês', 'fr'),
    '5': ('Italiano', 'it')
}


def selecionar_idioma():
    print("\nEscolha um idioma:")
    for key, (nome, _) in idiomas.items():
        print(f"{key}. {nome}")
    escolha = input("Digite o número do idioma: ")
    while escolha not in idiomas:
        print("Opção inválida. Tente novamente.")
        escolha = input("Digite o número do idioma: ")
    return idiomas[escolha]


def gerar_e_reproduzir_texto(texto, lang_code):
    # Gera o áudio com gTTS
    tts = gTTS(text=texto, lang=lang_code)
    # Salva temporariamente como MP3
    arquivo_audio = "frase.mp3"
    tts.save(arquivo_audio)

    # Reproduz o áudio com pygame
    pygame.mixer.music.load(arquivo_audio)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():  # Espera o áudio terminar
        pygame.time.Clock().tick(10)

    # Libera o arquivo de áudio
    pygame.mixer.music.unload()

    # Remove o arquivo temporário
    os.remove(arquivo_audio)


def main():
    idioma_nome, idioma_code = selecionar_idioma()
    print(f"Idioma selecionado: {idioma_nome}")

    while True:
        frase = input("\nEscreva uma frase (ou 'sair' para encerrar): ")
        if frase.lower() == 'sair':
            break

        gerar_e_reproduzir_texto(frase, idioma_code)

        print("\nOpções:")
        print("1. Escrever uma nova frase (mesmo idioma)")
        print("2. Escolher outro idioma")
        print("3. Sair")
        opcao = input("Digite o número da opção: ")

        if opcao == '2':
            idioma_nome, idioma_code = selecionar_idioma()
            print(f"Idioma selecionado: {idioma_nome}")
        elif opcao == '3':
            break
        elif opcao != '1':
            print("Opção inválida. Continuando com nova frase...")


if __name__ == "__main__":
    main()
Speech and Text Projects
Este repositório contém dois projetos em Python: Speech-to-Text (STT) e Text-to-Speech (TTS), desenvolvidos para criar um assistente interativo que reconhece comandos de voz e converte texto em fala. O projeto STT permite reconhecer comandos de voz para realizar pesquisas no Google, YouTube, Google Shopping e Wikipedia, enquanto o TTS converte texto em áudio em cinco idiomas (Português, Espanhol, Inglês, Francês e Italiano).
Funcionalidades
Speech-to-Text (STT)

Reconhece comandos de voz em português (pt-BR) usando a biblioteca SpeechRecognition com a API do Google.
Suporta os seguintes comandos:
Pesquisar [tópico]: Busca na Wikipedia e lê o resumo em voz alta.
Pesquisar no Google [consulta]: Abre o navegador com a busca no Google.
Pesquisar no YouTube [consulta]: Abre o navegador com a busca no YouTube.
Pesquisar para compras [produto] ou Comprar [produto]: Abre o Google Shopping.
Sair ou Tchau: Encerra o programa.


Saudação personalizada com o nome do usuário, falada via TTS.
Loop contínuo de escuta para comandos de voz.

Text-to-Speech (TTS)

Converte texto em fala usando a biblioteca gTTS (Google Text-to-Speech).
Suporte a cinco idiomas: Português, Espanhol, Inglês, Francês e Italiano.
Interface interativa de linha de comando.
Opções para:
Escrever uma nova frase no mesmo idioma.
Trocar de idioma.
Sair do programa.


Reprodução de áudio em tempo real usando pygame.

Pré-requisitos

Python 3.8 ou superior
PyCharm ou outro editor/IDE de sua escolha
Git instalado para clonar o repositório
Microfone funcional (para o STT)
Conexão à internet para instalar dependências e usar APIs (Google Speech Recognition e gTTS)
Sistema operacional: Windows, macOS ou Linux

Instalação

Clone este repositório para sua máquina local:
git clone https://github.com/https://github.com/JohnnyPassos/assistente_virtual.git


Navegue até o diretório do projeto:
cd assistente_virtual


Crie um ambiente virtual (recomendado para isolar dependências):
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows


Instale as dependências necessárias:
pip install SpeechRecognition PyAudio gtts pygame wikipedia



Nota: Se houver problemas com a instalação do PyAudio no Windows, tente:
pip install pipwin
pipwin install PyAudio

Como Usar
Speech-to-Text (STT)

Navegue até a pasta stt:
cd stt


Execute o programa:
python stt_program.py


Digite seu nome no console quando solicitado.

Fale comandos como:

"Pesquisar Python" (busca na Wikipedia e lê o resumo).
"Pesquisar no Google clima em São Paulo" (abre o Google).
"Pesquisar no YouTube tutoriais de Python" (abre o YouTube).
"Comprar celular" (abre Google Shopping).
"Sair" (encerra o programa).


O programa escuta continuamente até você dizer "sair" ou "tchau".


Text-to-Speech (TTS)

Navegue até a pasta tts:
cd tts


Execute o programa:
python tts_program.py


Escolha um idioma digitando o número correspondente (1 a 5).

Insira uma frase para ser convertida em áudio.

Após a reprodução, escolha:

1: Escrever outra frase no mesmo idioma.
2: Escolher outro idioma.
3: Sair do programa.


Para encerrar a qualquer momento, digite "sair" ao inserir uma frase.


Estrutura do Projeto
assistente_virtual/
├── stt/
│   └── stt_program.py            # Script principal do Speech-to-Text
├── tts/
│   └── tts_program.py            # Script principal do Text-to-Speech
├── .gitignore             # Ignora venv, arquivos temporários, etc.
└── README.md              # Este arquivo


Arquivos temporários (temp_audio.mp3 no STT e frase.mp3 no TTS) são gerados e deletados automaticamente.
Cada projeto tem seu próprio ambiente virtual (venv), se configurado.

Dependências

Speech-to-Text:
SpeechRecognition: Reconhecimento de fala.
PyAudio: Captura de áudio do microfone.
gtts: Para respostas em voz (saudação e leitura da Wikipedia).
playsound: Reprodução de áudio.
wikipedia: Busca na Wikipedia em português.
webbrowser: Abre links no navegador.


Text-to-Speech:
gtts: Conversão de texto em fala.
pygame: Reprodução de áudio.



Instale com:
pip install SpeechRecognition PyAudio gtts playsound pygame wikipedia

Solução de Problemas
Speech-to-Text

Microfone não funciona: Verifique as permissões de microfone no sistema operacional e teste em outro aplicativo.
Comando não reconhecido: Fale claramente e em um ambiente sem ruído. Ajuste energy_threshold no código (ex: 500 para ambientes ruidosos).
Erro na API do Google: Confirme a conexão com a internet.
Wikipedia não encontra resultados: Tente tópicos mais específicos (ex: "linguagem Python" em vez de "Python").
Áudio não reproduz: Verifique o som do dispositivo e reinstale playsound (pip install playsound==1.2.2).

Text-to-Speech

Áudio não reproduz: Certifique-se de que o som do dispositivo está ligado e que o pygame está instalado corretamente.
Erro de permissão no Windows: Confirme que o programa libera o arquivo frase.mp3 usando pygame.mixer.music.unload() antes de deletá-lo.
Problemas com dependências: Atualize o pip (pip install --upgrade pip) e reinstale as bibliotecas.

Contribuições
Contribuições são bem-vindas! Algumas ideias:

Adicionar suporte a mais idiomas no TTS.
Criar uma interface gráfica (ex: com Tkinter ou PyQt) para ambos os projetos.
Integrar STT e TTS em um único assistente interativo.
Adicionar suporte offline para reconhecimento de fala (ex: com Vosk).
Melhorar a robustez dos comandos de voz no STT com regex ou NLP.

Para contribuir:

Fork o repositório.
Crie uma branch (git checkout -b sua-funcionalidade).
Faça commit das mudanças (git commit -m "Adiciona funcionalidade X").
Envie um pull request.

Licença
Este projeto está licenciado sob a MIT License.

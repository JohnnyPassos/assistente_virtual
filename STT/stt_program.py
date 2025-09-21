import speech_recognition as sr
import webbrowser
import wikipedia
from gtts import gTTS
from playsound import playsound
import os

# Configurações
wikipedia.set_lang("pt")  # Para Wikipedia em português
recognizer = sr.Recognizer()
recognizer.energy_threshold = 300  # Ajusta sensibilidade ao ruído


def speak(text, lang='pt'):
    """Função para converter texto em voz e reproduzir."""
    tts = gTTS(text=text, lang=lang, slow=False)
    filename = "temp_audio.mp3"
    tts.save(filename)
    playsound(filename)
    os.remove(filename)  # Remove arquivo temporário


def process_command(command):
    """Processa o comando reconhecido."""
    command = command.lower()

    if "pesquisar no google" in command:
        query = command.replace("pesquisar no google", "").strip()
        if query:
            url = f"https://www.google.com/search?q={query}"
            webbrowser.open(url)
            speak("Abrindo busca no Google.")
        else:
            speak("Por favor, diga o que pesquisar.")

    elif "pesquisar no youtube" in command:
        query = command.replace("pesquisar no youtube", "").strip()
        if query:
            url = f"https://www.youtube.com/results?search_query={query}"
            webbrowser.open(url)
            speak("Abrindo busca no YouTube.")
        else:
            speak("Por favor, diga o que pesquisar.")

    elif "pesquisar para compras" in command or "comprar" in command:
        query = command.replace("pesquisar para compras", "").replace("comprar", "").strip()
        if query:
            url = f"https://www.google.com/search?tbm=shop&q={query}"
            webbrowser.open(url)
            speak("Abrindo busca de compras.")
        else:
            speak("Por favor, diga o produto.")

    elif "pesquisar" in command:
        query = command.replace("pesquisar", "").strip()
        if query:
            try:
                summary = wikipedia.summary(query, sentences=3)  # Resumo de 3 frases
                speak(summary)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("Há várias opções. Tente ser mais específico.")
            except wikipedia.exceptions.PageError:
                speak("Não encontrei na Wikipedia.")
        else:
            speak("Por favor, diga o tópico.")

    elif "sair" in command or "tchau" in command:
        speak("Até logo!")
        return False  # Sai do loop

    else:
        speak("Comando não reconhecido. Tente: pesquisar no Google, YouTube, para compras ou apenas pesquisar algo.")

    return True  # Continua o loop


# Parte principal
print("Digite seu nome:")
name = input().strip()
speak(f"Seja bem-vindo {name}, o que posso te ajudar?")

with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source)  # Ajusta ao ruído ambiente
    while True:
        print("Escutando...")
        try:
            audio = recognizer.listen(source, timeout=1, phrase_time_limit=10)
            command = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {command}")
            if not process_command(command):
                break
        except sr.UnknownValueError:
            pass  # Ignora se não entender
        except sr.RequestError as e:
            speak("Erro no serviço de reconhecimento.")
        except sr.WaitTimeoutError:
            pass  # Continua escutando
import os
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import datetime

def encontrar_dispositivo_audio():
    """
    Encontra automaticamente o melhor dispositivo para capturar áudio do sistema.
    Retorna o índice do dispositivo ou None se nenhum for encontrado.
    """
    dispositivos = sd.query_devices()
    for i, dispositivo in enumerate(dispositivos):
        nome = dispositivo['name']
        entrada = dispositivo['max_input_channels']
        host_api = sd.query_hostapis(dispositivo['hostapi'])['name']

        # Filtra dispositivos que possuem entrada de áudio válida e correspondem a nomes conhecidos
        if entrada > 0 and ("stereo mix" in nome.lower() or "mixagem estéreo" in nome.lower() or "wasapi" in host_api):
            print(f"🎤 Dispositivo encontrado: {nome} (ID: {i}) - API: {host_api}")
            return i

    print("⚠️ Nenhum dispositivo de captura válido encontrado!")
    return None

# Encontra automaticamente o dispositivo correto
dispositivo_audio = encontrar_dispositivo_audio()
if dispositivo_audio is None:
    print("Erro: Nenhum dispositivo válido encontrado. Verifique as configurações de áudio.")
    exit(1)

# Caminho da pasta para salvar a transcrição
PASTA_TRANSCRICAO = "transcrição"
# Verifica se a pasta de transcrição existe, se não, cria ela
os.makedirs(PASTA_TRANSCRICAO, exist_ok=True)

def capturar_audio_sistema(caminho_audio, duracao=10, taxa_amostragem=44100, dispositivo=None):
    """
    Captura o áudio do sistema (som dos alto-falantes) e salva em um arquivo WAV.
    """
    print(f"Capturando áudio do sistema por {duracao} segundos...")
    try:
        info_dispositivo = sd.query_devices(dispositivo)
        canais = info_dispositivo['max_input_channels']
        print(f"Usando dispositivo: {info_dispositivo['name']} - {canais} canais de entrada")

        audio = sd.rec(
            int(duracao * taxa_amostragem),
            samplerate=taxa_amostragem,
            channels=canais,
            dtype='float32',
            device=dispositivo
        )
        sd.wait()
        sf.write(caminho_audio, audio, taxa_amostragem)
        print(f"Áudio salvo em: {caminho_audio}")
    except Exception as e:
        print(f"Erro ao capturar áudio: {e}")
        raise

def transcrever_audio(caminho_audio):
    """
    Transcreve o áudio capturado e retorna o texto.
    """
    r = sr.Recognizer()
    with sr.AudioFile(caminho_audio) as source:
        audio = r.record(source)
        try:
            return r.recognize_google(audio, language="pt-br")
        except sr.UnknownValueError:
            return "[Fala não reconhecida]"
        except sr.RequestError as e:
            return f"[Erro na requisição: {e}]"

def transcrever_reuniao_em_tempo_real(caminho_transcricao, intervalo=10, dispositivo=None):
    """
    Captura o áudio do sistema em intervalos, transcreve e salva as falas com os tempos.
    """
    r = sr.Recognizer()
    taxa_amostragem = 44100
    
    with open(caminho_transcricao, "w", encoding="utf-8") as arquivo:
        try:
            while True:
                caminho_audio_temp = "temp_audio.wav"
                capturar_audio_sistema(caminho_audio_temp, duracao=intervalo, taxa_amostragem=taxa_amostragem, dispositivo=dispositivo)
                tempo_atual = datetime.datetime.now().strftime("%H:%M:%S")
                texto = transcrever_audio(caminho_audio_temp)
                print(f"[{tempo_atual}] {texto}")
                arquivo.write(f"[{tempo_atual}] {texto}\n")
                arquivo.flush()
                os.remove(caminho_audio_temp)
        except KeyboardInterrupt:
            print("Transcrição interrompida pelo usuário.")

def main():
    """
    Função principal que inicia a transcrição em tempo real.
    """
    nome_arquivo = "transcricao_reuniao.txt"
    caminho_transcricao = os.path.join(PASTA_TRANSCRICAO, nome_arquivo)
    print(f"Transcrição será salva em: {caminho_transcricao}")
    transcrever_reuniao_em_tempo_real(caminho_transcricao, dispositivo=dispositivo_audio)

if __name__ == "__main__":
    main()
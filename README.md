# Documentação do Projeto

## **1. Transcrição de Reuniões em Tempo Real (Captura de Áudio)**

Este projeto permite capturar áudio em tempo real, transcrever e salvar as falas com os tempos de uma reunião, por exemplo. Ele utiliza a biblioteca **`sounddevice`** para captura do áudio do sistema, **`speech_recognition`** para transcrição e **`soundfile`** para salvar o áudio em um arquivo WAV.

### **O que o código faz?**

1. **Captura o áudio do sistema:**

   - O código localiza automaticamente o dispositivo de áudio do sistema, capturando o áudio a partir de dispositivos como "Stereo Mix" ou "Wasapi".
   - Ele grava o áudio do sistema em um arquivo temporário de 10 segundos.

2. **Transcreve o áudio:**

   - O áudio capturado é transcrito usando a API do Google para reconhecimento de fala.
   - A transcrição é salva em um arquivo de texto com a hora em que foi falada.

3. **Organiza a transcrição:**

   - Durante a execução do código, o áudio é capturado em intervalos (definido por você) e transcrito continuamente.
   - O resultado é salvo em um arquivo `.txt` na pasta `transcrição`.

4. **Organização das pastas:**
   - O código cria a pasta `transcrição` se ela não existir.

---

### **Como usar?**

1. **Instale as bibliotecas necessárias:**
   Utilize os comandos abaixo para instalar as bibliotecas:

   ```bash
   pip install sounddevice soundfile SpeechRecognition
   ```

2. **Crie e ative um ambiente virtual (opcional):**
   Para garantir que o projeto funcione em um ambiente isolado, você pode criar um ambiente virtual.

   - No terminal, execute:

     ```bash
     python -m venv venv
     ```

   - Ative o ambiente virtual:

     - No **Windows**:

       ```bash
       .\venv\Scripts\activate
       ```

     - No **macOS/Linux**:

       ```bash
       source venv/bin/activate
       ```

3. **Execute o código:**

   - O código irá automaticamente iniciar a transcrição. Caso queira interromper a transcrição, pressione **Ctrl+C**.

4. **Verifique os arquivos de saída:**
   - O arquivo de transcrição será salvo na pasta `transcrição`.

### **Estrutura das pastas após execução:**

```
Meu_Projeto/
├── transcrição/
│   └── transcricao_reuniao.txt
```

---

## **2. Transcrição de Vídeos (Video-Transcriber)**

Este projeto permite extrair o áudio de vídeos, dividi-los em partes menores e transcrever o conteúdo para texto.

### **O que o código faz?**

1. **Localiza os vídeos na pasta `video_transcrição`:**

   - O código verifica todos os arquivos na pasta `video_transcrição` e processa apenas os arquivos de vídeo com extensões `.mp4`, `.avi`, `.mkv`.

2. **Extrai o áudio e salva na pasta `audio_extraído`:**

   - O áudio é extraído do vídeo e salvo com a extensão `.wav` na pasta `audio_extraído`.

3. **Divide o áudio em partes menores (por padrão de 60 segundos):**

   - O áudio é dividido para facilitar a transcrição.

4. **Transcreve o áudio e salva o texto na pasta `transcrição`:**

   - O texto transcrito é salvo em um arquivo `.txt` com o mesmo nome do arquivo de vídeo.

5. **Organiza as pastas:**
   - O código cria as pastas `audio_extraído` e `transcrição` caso elas não existam.

---

### **Como usar?**

1. **Instale as bibliotecas necessárias:**
   Utilize os seguintes comandos para instalar as bibliotecas:

   ```bash
   pip install moviepy SpeechRecognition
   ```

2. **Coloque seus vídeos na pasta `video_transcrição`:**

   - Coloque seus vídeos (com extensões `.mp4`, `.avi`, `.mkv`) na pasta `video_transcrição`.

3. **Execute o código:**

   - O código irá automaticamente extrair o áudio, dividir e transcrever os vídeos.

4. **Verifique os arquivos de saída:**
   - O áudio extraído será salvo na pasta `audio_extraído` e a transcrição será salva na pasta `transcrição`.

### **Estrutura das pastas após execução:**

```
Meu_Projeto/
├── video_transcrição/
│   └── video_exemplo.mp4
├── audio_extraído/
│   └── video_exemplo.wav
└── transcrição/
    └── video_exemplo.txt
```

---

## **Requisitos do Sistema**

- Python 3.x
- Bibliotecas necessárias:

  ```bash
  pip install sounddevice soundfile SpeechRecognition moviepy
  ```

---

### **Executando o Projeto**

Após a instalação das bibliotecas e a configuração das pastas, você pode executar os projetos com o seguinte comando:

- Para **Transcrição de Reuniões** (captura de áudio e transcrição em tempo real):

  ```bash
  python transcricao_reuniao.py
  ```

- Para **Transcrição de Vídeos** (extração de áudio e transcrição de vídeos):

  ```bash
  python transcricao_video.py
  ```

Esses comandos iniciarão os respectivos processos de transcrição.

---

### **Exemplo de Execução**

Suponha que você tenha o seguinte arquivo de vídeo na pasta `video_transcrição`:

- `video_exemplo.mp4`

Após a execução do código, os seguintes arquivos serão gerados:

- **Áudio extraído:** `audio_extraído/video_exemplo.wav`
- **Transcrição:** `transcrição/video_exemplo.txt`

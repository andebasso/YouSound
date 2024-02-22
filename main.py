import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from pytube import YouTube
from moviepy.editor import *
import os

# Função para baixar o vídeo e converter para áudio
def download_and_convert(url, save_path, file_name):
    try:
        # Baixar o vídeo do YouTube
        yt = YouTube(url)
        video = yt.streams.filter(only_audio=True).first()
        download_path = video.download(output_path=save_path, filename=file_name + '.mp4')

        # Tentar converter vídeo em áudio
        try:
            clip = VideoFileClip(download_path)
            audio_path = os.path.join(save_path, file_name + '.mp3')
            clip.audio.write_audiofile(audio_path)
            clip.close()
            messagebox.showinfo("Sucesso", "Download e conversão concluídos!\nSalvo como: " + audio_path)
        except Exception as e:  # Trata o erro de conversão, mas continua o script
            messagebox.showwarning("Aviso", f"Ocorreu um erro durante a conversão do vídeo para áudio, mas o download foi bem-sucedido: {e}\nVídeo salvo como: {download_path}")

    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro durante o download: {e}")

# Interface gráfica para entrada de dados
def on_submit():
    url = url_entry.get()
    if url:
        save_path = filedialog.askdirectory()
        if not save_path:
            return
        file_name = simpledialog.askstring("Nome do arquivo", "Insira o nome do arquivo:")
        if not file_name:
            return
        download_and_convert(url, save_path, file_name)
    else:
        messagebox.showwarning("Aviso", "Por favor, insira a URL do vídeo.")

root = tk.Tk()
root.title("YouTube Audio Downloader")
root.geometry("500x150")
root.eval('tk::PlaceWindow . center')

url_label = tk.Label(root, text="Insira a URL do vídeo do YouTube:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

submit_btn = tk.Button(root, text="Baixar e Converter", command=on_submit)
submit_btn.pack()

root.mainloop()

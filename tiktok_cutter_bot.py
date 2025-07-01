
import os
from pytube import YouTube
from moviepy.video.io.VideoFileClip import VideoFileClip
import uuid

DOWNLOAD_DIR = "downloads"
CUT_DIR = "cuts"
CLIP_DURATION = 60  # segundos

def download_tiktok(url: str) -> str:
    """Baixa vídeo do TikTok usando pytube e devolve caminho do arquivo."""
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension='mp4', progressive=True).order_by('resolution').desc().first()
    filename = f"{uuid.uuid4()}.mp4"
    stream.download(output_path=DOWNLOAD_DIR, filename=filename)
    return os.path.join(DOWNLOAD_DIR, filename)

def cut_video(input_path: str) -> str:
    """Corta o primeiro minuto do vídeo e salva em CUT_DIR."""
    os.makedirs(CUT_DIR, exist_ok=True)
    clip = VideoFileClip(input_path).subclip(0, CLIP_DURATION)
    out_path = os.path.join(CUT_DIR, f"cut_{os.path.basename(input_path)}")
    clip.write_videofile(out_path, codec="libx264", audio_codec="aac")
    clip.close()
    return out_path

def main():
    url = input("Cole a URL do TikTok: ").strip()
    video_path = download_tiktok(url)
    clip_path = cut_video(video_path)
    print(f"Clipe gerado em: {clip_path}")

if __name__ == "__main__":
    main()

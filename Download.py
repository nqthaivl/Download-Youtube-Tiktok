import gradio as gr
import yt_dlp
import os
from tkinter import filedialog, Tk

# Initialize a global variable for download folder path
download_folder_path = ""

# Path to ffmpeg executable in the same directory under 'ffmpeg/bin'
ffmpeg_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ffmpeg', 'bin', 'ffmpeg' if os.name != 'nt' else 'ffmpeg.exe')

def browse_directory():
    global download_folder_path
    root = Tk()
    root.attributes("-topmost", True)
    root.withdraw()  # Hide the root window
    download_folder_path = filedialog.askdirectory()  # Open folder dialog
    root.destroy()
    return download_folder_path if download_folder_path else "Không có thư mục nào được ch."

def get_video_info(link):
    try:
        with yt_dlp.YoutubeDL() as ydl:
            video_info = ydl.extract_info(link, download=False)  # Extract info without downloading
        resolutions = set()
        for format in video_info.get('formats', []):
            if format.get('height') is not None:  # Ensure height is not None
                resolutions.add(format['height'])
        return sorted(resolutions)  # Return sorted list of resolutions
    except Exception as e:
        return str(e)

def download_youtube_video(link, resolution, save_path):
    if not os.path.isdir(save_path):
        return "Vui lòng nhập đường dẫn thư mục hợp lệ để lưu video."

    # Check if ffmpeg exists in the specified path
    if not os.path.isfile(ffmpeg_path):
        return "Lỗi: không tìm thấy tệp thực thi ffmpeg trong đường dẫn đã chỉ định. Đảm bảo ffmpeg nằm trong đúng thư mục."

    try:
        # yt-dlp configuration with the local ffmpeg path
        ydl_opts = {
            'format': f'bestvideo[height<={resolution}]+bestaudio/best[height<={resolution}]',
            'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
            'merge_output_format': 'mp4',
            'ffmpeg_location': ffmpeg_path,  # Specify the local ffmpeg path
        }
        
        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        
        return f"Đã tải video thành công ở độ phân giải {resolution} vào {save_path}!"
    except Exception as e:
        return f"Có lỗi trong quá trình tải video, vui lòng thử lại"

# Create Gradio interface with custom components
with gr.Blocks(title="Tải Nhanh Video - Sản Phẩm 1Touch.Pro") as iface:
    gr.Markdown("# Tải Nhanh Video - Sản phẩm của 1Touch.Pro")
    gr.Markdown("Hỗ trợ tải nhanh video của các dịch vụ: Facebook, Youtube, Tiktok, Xvideo... Hỗ trợ tải cả kênh hoặc danh sách phát.")
    
    # Textbox for YouTube link input, triggers resolution check on change
    link_input = gr.Textbox(label="Link Video")

    # Placeholder for resolution options, updated dynamically
    resolution_input = gr.Dropdown(label="Tuỳ chọn độ phân giải", choices=[], interactive=True)
    
    folder_path = gr.Textbox(label="Chọn thư mục tải", interactive=False)
    browse_button = gr.Button("Chọn thư mục")

    # Button to trigger folder selection
    browse_button.click(browse_directory, inputs=[], outputs=folder_path)

    # Automatically update resolutions when a link is entered
    def update_resolutions(link):
        resolutions = get_video_info(link)
        if isinstance(resolutions, list):
            return gr.update(choices=resolutions)  # Update dropdown choices
        return gr.update(choices=[])  # Reset dropdown if an error occurs

    # Trigger the update function when the link input changes
    link_input.change(fn=update_resolutions, inputs=link_input, outputs=resolution_input)

    download_button = gr.Button("Tải video")
    
    # Run download function
    result_output = gr.Textbox(label="Thông báo quá trình", interactive=False)
    download_button.click(download_youtube_video, inputs=[link_input, resolution_input, folder_path], outputs=result_output)

# Launch the Gradio app with public link and open it in the default web browser
iface.launch(share=False, inbrowser=True)

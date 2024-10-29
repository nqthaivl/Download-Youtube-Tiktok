# Tải Nhanh Video - Sản phẩm của 1Touch.Pro

Ứng dụng tải nhanh video từ các nền tảng như YouTube, Facebook, TikTok, và Xvideo với các tuỳ chọn độ phân giải. Hỗ trợ tải video từ link đơn lẻ, danh sách phát hoặc toàn bộ kênh.

## Tính Năng
- **Tải video** từ nhiều nguồn phổ biến.
- **Chọn độ phân giải** trước khi tải.
- **Lựa chọn thư mục tải xuống** theo ý muốn.
- **Hiển thị tiến trình tải xuống** dưới dạng phần trăm.

## Yêu Cầu Hệ Thống
- Python 3.7 hoặc mới hơn.
- Các thư viện yêu cầu: `gradio`, `gradio_client`, `yt-dlp`.

## Cài Đặt
1. **Clone hoặc tải xuống** repository này:
    ```bash
    git clone https://github.com/nqthaivl/Download-Youtube-Tiktok.git
    ```

2. **Cài đặt các thư viện yêu cầu**. Có thể sử dụng `requirements.txt` để tự động cài đặt các thư viện cần thiết:
    ```bash
    python -m pip install -r requirements.txt
    ```

3. **Đảm bảo thư mục `ffmpeg` có sẵn** trong thư mục gốc của ứng dụng:
   - Đặt `ffmpeg.exe` trong `ffmpeg/bin` (trên Windows) hoặc `ffmpeg/bin/ffmpeg` (trên các hệ điều hành khác).
   - Có thể tải xuống FFmpeg [tại đây](https://ffmpeg.org/download.html).
   - Giải nén chép vào cùng thư mục

## Sử Dụng
1. **Chạy ứng dụng**:
    ```bash
    python Download.py
    ```

2. **Sử dụng giao diện Gradio**:
    - Nhập **Link Video** muốn tải.
    - Chọn **Tuỳ chọn độ phân giải** mong muốn.
    - Nhấn **Chọn thư mục** để chọn nơi lưu video.
    - Nhấn **Tải video** để bắt đầu tải xuống.

3. **Theo dõi tiến trình tải**:
   - Quá trình tải sẽ hiển thị trong phần **Download Progress**.

## Cấu Trúc Thư Mục
    ```bash
    ffmpeg (thư mục)
    Download.py
    Install.bat
    requirements.txt
    ```
## Lỗi Phổ Biến
- **ModuleNotFoundError: No module named 'gradio'**: Kiểm tra lại cài đặt thư viện bằng lệnh `python -m pip install gradio`.
- **Không tìm thấy FFmpeg**: Kiểm tra lại đường dẫn của FFmpeg và đảm bảo nó nằm trong `ffmpeg/bin`.

## Đóng Góp
Chúng tôi luôn chào đón các đóng góp từ cộng đồng! Vui lòng tạo một pull request hoặc mở một issue để giúp cải thiện ứng dụng.

---

**Liên hệ**: Nếu có bất kỳ câu hỏi nào, vui lòng liên hệ với chúng tôi qua Facebook [1Touch.Pro](https://www.facebook.com/nqthaivl.1982).

---

**Bản quyền © 2024 1Touch.Pro** - Tất cả quyền được bảo lưu.


# Tommybot

Tommybot là một chatbot Facebook đơn giản sử dụng Django.

## Cài đặt

1. Clone repository từ Github:
   ```
   git clone https://github.com/MinhHoang712/tommybot.git
   ```

2. Tạo và kích hoạt môi trường ảo:
   ```
   python3 -m venv env
   source env/bin/activate
   ```

3. Cài đặt các package cần thiết:
   ```
   pip install -r requirements.txt
   ```

4. Tải và cài đặt [Ngrok](https://ngrok.com/download) để public localhost:

5. Đưa host của Ngrok mới vào file `settings.py`:
   ```
   ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'your_ngrok_host']
   ```

6. Chạy server:
   ```
   python manage.py runserver
   ```

## Sử dụng

1. Tạo một [Facebook Page](https://www.facebook.com/pages/create).

2. Tạo một [Facebook Developer Account](https://developers.facebook.com/).

3. Tạo một ứng dụng Facebook mới và thiết lập Webhooks và Access Token. Xem thêm trong file `facebook_config.py`.

4. Cập nhật `ACCESS_TOKEN` và `VERIFY_TOKEN` trong file `facebook_config.py`.

5. Kết nối webhook với server của bạn bằng cách sử dụng Ngrok: 
   ```
   ./ngrok http 8000
   ```
6. Vào cài đặt Webhooks trên trang Facebook của bạn và cập nhật địa chỉ webhook.

7. Bắt đầu gửi tin nhắn với bot của bạn trên Facebook!
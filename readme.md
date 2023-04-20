# Chatbot Facebook đơn giản sử dụng Django

Đây là một chatbot Facebook đơn giản được xây dựng bằng Django và sử dụng thư viện aiohttp, pymessenger và facebook-sdk. Chatbot này cho phép gửi tin nhắn tự động cho người dùng trên trang Facebook của bạn.

## Cài đặt

Để cài đặt chatbot này, bạn cần thực hiện các bước sau đây:

1. Clone repository này về máy của bạn.
2. Cài đặt các thư viện được liệt kê trong file requirement.txt bằng lệnh `pip install -r requirements.txt`.
3. Điền các thông tin cấu hình cần thiết vào file facebook_config.py.
4. Khởi chạy chatbot bằng lệnh `python manage.py runserver`.

## Cấu hình

Để cấu hình chatbot, bạn cần điền các thông tin sau vào file facebook_config.py:

* `FB_PAGE_TOKEN`: mã truy cập của trang Facebook của bạn.
* `FB_VERIFY_TOKEN`: mã xác thực cho webhook của bạn.


## Sử dụng

Sau khi cài đặt và cấu hình chatbot, bạn có thể sử dụng nó bằng cách gửi tin nhắn trực tiếp đến trang Facebook của bạn. Chatbot sẽ trả lời tự động theo các qui tắc được định nghĩa trong file views.py.
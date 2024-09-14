# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# # Hàm xử lý lệnh /start
# def start(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text="Xin chào! Tôi là chatbot.")

# # Hàm xử lý tin nhắn
# def echo(update, context):
#     context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

# def main():
#     # Khởi tạo một Updater với token của bot
#     updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)

#     # Lấy dispatcher để đăng ký các handler
#     dispatcher = updater.dispatcher

#     # Đăng ký các handler
#     start_handler = CommandHandler('start', start)
#     echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
#     dispatcher.add_handler(start_handler)
#     dispatcher.add_handler(echo_handler)

#     # Bắt đầu polling để nhận tin nhắn từ người dùng
#     updater.start_polling()

#     # Chạy bot cho đến khi nhấn Ctrl-C
#     updater.idle()

# if __name__ == '__main__':
#     main()

import numpy as np
# Thu thập dữ liệu
data = ["Xin chào", "Chào bạn, tôi có thể giúp gì cho bạn?"]

# Tiền xử lý dữ liệu
processed_data = [d.lower() for d in data]

# Huấn luyện mô hình
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer().fit_transform(processed_data)
vectors = vectorizer.toarray()

# Tạo mô hình
from sklearn.metrics.pairwise import cosine_similarity
def reply(user_input):
    user_input_vector = vectorizer.transform([user_input])
    similarity_scores = cosine_similarity(user_input_vector, vectors)
    nearest = np.argmax(similarity_scores)
    return processed_data[nearest]

# Kiểm tra mô hình
print(reply("hi"))

# Đánh giá mô hình
# Ở đây, chúng ta cần dữ liệu thực tế để đánh giá mô hình

# Triển khai mô hình
# Mô hình có thể được triển khai dưới dạng một ứng dụng web, một API, hoặc thậm chí là một ứng dụng di động.

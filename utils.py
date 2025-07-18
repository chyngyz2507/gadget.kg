from django.conf import settings
from django.core.mail import send_mail
import requests

# from movie.models import Movie, Category


def send_message(email, id):
    subject = "My first message gmail"
    html_content = f"""
            <html>
              <body style="font-family: Arial, sans-serif; background-color: #f9f9f9; padding: 20px;">
                <div style="max-width: 600px; margin: auto; background-color: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
                  <h2 style="color: #333;">Добро пожаловать!</h2>
                  <p style="font-size: 16px; color: #555;">
                    Спасибо, что присоединились к нам. Нажмите на кнопку ниже, активировать аккаунт:
                  </p>
                  <a href="http://10.244.53.213:8000/users/activate/{id}/" target="_blank" 
                     style="display: inline-block; padding: 15px 25px; font-size: 16px; color: white; background-color: #007BFF; text-decoration: none; border-radius: 5px;">
                    Активировать
                  </a>
                  <p style="font-size: 14px; color: #999; margin-top: 20px;">
                    Если кнопка не работает, скопируйте и вставьте ссылку в браузер: <br>
                    <a href="http://10.244.53.213:8000/users/activate/{id}/" target="_blank" style="color: #007BFF;">активировать</a>
                  </p>
                </div>
              </body>
            </html>
            """
    send_mail(subject, message=None, html_message=html_content,
              from_email=settings.EMAIL_HOST_USER,
              recipient_list=[email, ])


# def get_response():
#     response = requests.get(settings.AKBAR_MOVIES_URL)
#     if response.status_code == 200:
#         json_data = response.json()
#         for item in json_data:
#             item.pop("id")
#             item.pop("category")
#             item.pop("delete_at")
#             name = item.pop("name")
#             category, _ = Category.objects.get_or_create(title=name)
#             Movie.objects.create(**item, category=category)
#     return response.json()

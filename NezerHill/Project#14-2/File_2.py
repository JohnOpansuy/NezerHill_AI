#Підключення бібліотек.
from flask import Flask, render_template, request, url_for, flash, redirect, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, SubmitField, EmailField, PasswordField
from wtforms.validators import DataRequired, Email
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import logging
import html
import os

#Налаштування веб-сайту та його конфігурацій.
#?current_time = datetime.now()  # Отримати поточний час
#?time = current_time.strftime ("%H:%M:%S")  # Формат часу
#?date = current_time.strftime ("%Y-%m-%d")  # Формат дати
website = Flask (__name__)
website.config ["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
website.config ["SQLALCHMEY_TRACK_MODIFICATIONS"] = False
website.config ["PERMANENT_SESSION_LIFETIME"] = timedelta (minutes = 30)
website.config ["SECRET_KEY"] = "Nezer_Hill"
#! website.secret_key = os.urandom (24)
basa = SQLAlchemy (website)
#Налаштування логін менеджера.
login_manager = LoginManager()
login_manager.init_app (website)
login_manager.login_view = "User_login"
#Налаштування CSRF захист.
zahust_1 = CSRFProtect (website)
#Налаштування логів.
logging.basicConfig (filename = "user_actions.log", level = logging.INFO, format = "%(asctime)s - %(levelname)s - %(message)s")
#Клас форми відправлення.
class RegisterForm (FlaskForm):
    name = StringField ("Name", validators = [DataRequired()])
    email = EmailField ("Email", validators = [DataRequired(), Email()])
    password = PasswordField ("Password", validators = [DataRequired()])
    submit = SubmitField ("Register")
#Клас форми відправлення.
class LoginForm (FlaskForm):
    email = EmailField ("Email", validators = [DataRequired(), Email()])
    password = PasswordField ("Password", validators = [DataRequired()])
    submit = SubmitField ("Log in")
#Клас форми редагування акаунту.
class EditAcountForm (FlaskForm):
    name = StringField ("Name", validators = [DataRequired()])
    email = EmailField ("Email", validators = [DataRequired(), Email()])
    password = PasswordField ("Password", validators = [DataRequired()])
    submit = SubmitField ("Save")
#Клас користувача.
class Users (UserMixin, basa.Model):
    __tablename__ = "users"
    id = basa.Column (basa.Integer, primary_key = True)
    user_name = basa.Column (basa.String (50), nullable = False) #! Не юзати бо помилка сервнра тоді (, unique = True).
    user_mail = basa.Column (basa.String (80), unique = True, nullable = False)
    user_password = basa.Column (basa.String (100), nullable = False)
    user_data = basa.Column (basa.String (50), nullable = False)
    last_seen = basa.Column (basa.String (50), nullable = True)
    user_status = basa.Column (basa.String (80), nullable = False, default = "User")
#Дані для безпеки.
    user_tryes = basa.Column (basa.Integer, default = 3)
    user_ip = basa.Column (basa.String (75))
    user_browser = basa.Column (basa.String (200))
#Клас чатів.
#- class Chats (basa.Model):
#-     __tablename__ = "chats"
#Створення таблиць.
initialized = False  # Глобальна змінна для перевірки стану ініціалізації.
@website.before_request
def initialize_database():
    global initialized
    if not initialized:
        basa.create_all()
        #? print ("Таблиці створені під час першого запиту.")
        logging.warning ("Base are successfull created.")
        initialized = True
#Деф перевірки входу користувача.
@login_manager.user_loader
def Load_user (user_id):
    return basa.session.get (Users, int (user_id))
#Деф реєстрації користувача.
@website.route ("/singin", methods = ["GET", "POST"])
def User_sing():
#Створення екземпляру форми для регістру.
    form = RegisterForm()
#Іф перевірки валідності форми.
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
#Перевірка чи існує користувач.
        if Users.query.filter_by (user_mail = email).first():
            logging.error (f"Try to register with exists email - {email}.")
            flash ("Email are exists. Try to login.", "warning")
            return redirect (url_for ("User_sing"))
#Трай додавання нового користувача.
        try:
            ip_address = request.headers.get ('X-Forwarded-For', request.remote_addr)
            browser_info = request.headers.get ("User-Agent", "Unknown")
            current_time = datetime.now()
            formatted_time = current_time.strftime ("%Y-%m-%d %H:%M:%S")  # Формат без мілісекунд
            date = current_time.strftime ("%Y-%m-%d")
            hashed_password = generate_password_hash (password, method="pbkdf2:sha256")
            new_user = Users(
                user_name = name,
                user_mail = email,
                user_password = hashed_password,
                user_ip = ip_address,
                user_browser = browser_info,
                user_data = date,
            )
            basa.session.add (new_user)
            basa.session.commit()
            login_user (new_user)
            flash ("You are registered.", "success")
            logging.info (f"User registered successfully: {name} - {email}.\n-> IP: {ip_address}")
            return redirect (url_for ("Main_page"))
        except Exception as err:
            basa.session.rollback()
            flash ("Error in registration process. Try again later.", "danger")
            logging.error (f"Error when registering new user: {err}.")
            return redirect (url_for ("User_sing"))
    return render_template ("sing.html", form = form)
#Деф логіну користувача.
@website.route ("/login", methods = ["GET", "POST"])
def User_login():
#Створення екземпляру форми для логіну.
    form = LoginForm()
#Іф перевірки валідності форми.
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
#Перевірка користувача за email.
        user = Users.query.filter_by (user_mail = email).first()
#іф перевірки чи не існує такого користувача.
        if not user:
            flash ("User with it email not exits.", "danger")
            logging.warning (f"->Try enter with exit email - {email}.")
            return redirect (url_for ("User_login"))
#Перевірка кількості спроб.
        if user.user_tryes <= 0:
            logging.warning (f"!!- Warning: so many tryes to enter here - {email}-!!.\n->'Recomend': need check all activities\n->IP - [{user.user_ip}].")
            flash ("Yours account baned for many tryes to enter.", "danger")
            return redirect (url_for ("User_login"))
#Перевірка паролю.
        if check_password_hash (user.user_password, password):
            login_user (user)
            current_time = datetime.now()  # Отримати поточний час.
            user.last_seen = current_time.strftime ("%Y-%m-%d %H:%M:%S")  # Формат дати та часу.
            user.user_tryes = 3  # Відновлення кількості спроб.
            basa.session.commit()  # Збереження змін у базу даних.
            flash ("You successfully logged in!", "success")
            logging.info (f"User successfully logged in - {email} at {user.last_seen}")
            return redirect (url_for ("Main_page"))
        else:
            user.user_tryes -= 1  # Зменшення спроб
            basa.session.commit()
            flash (f"Uncorrect password. Left tryes: {user.user_tryes + 1}", "danger")
            logging.warning (f"!-> Unsuccess enter - {email}.\n->Left tryes - {user.user_tryes + 1}.")
            return redirect (url_for ("User_login"))
    return render_template ("login.html", form=form)
#Деф виходу з акаунта.
@website.route ("/logout")
def Logout():
    if current_user.is_authenticated:
        logging.info (f"User log out: {current_user.user_name}.")
        logout_user()
        flash (f"You are suceful loged out.", "danger")
    else:
        flash ("For logout you must be logined.", "danger")
        logging.error ("Anonim wanted logout without authenticated :).")
    return redirect (url_for ("Main_page"))
#Деф головної сторінки.
@website.route ("/")
@login_required
def Main_page():
#Створення данного користувача.
    #? user = current_user
    return render_template ("index.html")
#Деф сторінки ебаут.
@website.route ("/about")
@login_required
def About_page():
    return render_template ("about.html")
#Деф сторінки ебаут.
@website.route ("/privacy")
@login_required
def Privacy_page():
    return render_template ("privacy.html")
#Деф сторінки акаунту.
@website.route("/acount", methods=["GET", "POST"])
@login_required
def Account_page():
    # Створення екземпляра форми для редагування акаунту
    form = EditAcountForm()

    # Обробка даних після відправки форми
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data

        # Перевірка чи email вже існує в базі і не належить поточному користувачу
        existing_user = Users.query.filter(
            Users.user_mail == email, Users.id != current_user.id
        ).first()

        if existing_user:
            logging.error(f"New email already exists - {email}.")
            flash("This email is already in use. Please try another one.", "warning")
            return redirect(url_for("Account_page"))

        # Оновлення даних користувача
        try:
            current_user.user_name = name
            current_user.user_mail = email

            # Перевірка і оновлення паролю (якщо введено)
            if password:
                current_user.user_password = password

            # Збереження змін у базі даних
            basa.session.commit()
            flash("All changes have been successfully saved.", "success")
            logging.info(f"Account information updated for user - {email}.")
            return redirect(url_for("account_page"))

        except Exception as err:
            # У випадку помилки виконуємо відкат змін
            basa.session.rollback()
            flash("An error occurred. Changes were not saved.", "danger")
            logging.warning(f"Failed to update account {current_user.user_mail}. Details: {err}.")
            return redirect(url_for("account_page"))

    # Відображення сторінки профілю
    return render_template(
        "acount.html",
        form=form,
        name=current_user.user_name,
        mail=current_user.user_mail,
        data=current_user.user_data,
        seen=current_user.last_seen,
        status=current_user.user_status
    )

#Деф помилки 404-не має та сторінки.
@website.errorhandler (404)
def Page_not_founded (e):
    aurl = request.url
    logging.warning (f"Page or files not found: {aurl}")
    return render_template ("not_found.htm")
#Запуск веб-саййту.
if __name__ == "__main__":
    website.run (debug = True, port = 8888) #? , ssl_context = ("cert.pem", "key.pem")
#Maximus - Senior Developer
# 23:38
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# # Дані SMTP-сервера
# SMTP_SERVER = "smtp.gmail.com"  # Для Gmail
# SMTP_PORT = 587
# EMAIL_SENDER = "simkivmaksim4@gmail.com"  # Вкажи свою пошту
# EMAIL_PASSWORD = "ybqa xwec yids gkin"  # Використай пароль додатка (не звичайний пароль)
# def send_email(email, name, theme, message):
#     try:
#         # Формування листа
#         msg = MIMEMultipart()
#         msg["From"] = EMAIL_SENDER
#         msg["To"] = email
#         msg["Subject"] = theme
# body = f"Привіт, я {name}!\n\nНадіслав(а) повідомлення. \nМоя адресса: {email} \nТема: {theme} \n Повідомлення:\n{message}."
#         msg.attach(MIMEText(body, "plain"))

#         # Підключення до SMTP-сервера та відправка
#         server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
#         server.starttls()
#         server.login(EMAIL_SENDER, EMAIL_PASSWORD)
#         server.sendmail(EMAIL_SENDER, email, msg.as_string())
#         server.quit()

#         print(f"Email успішно відправлено {email}")
# Maximus - Senior Developer
# 23:39
# except Exception as e:
#         print(f"Помилка відправки email: {e}")
# send_email("test@example.com", "Ім'я", "Тестова тема", "Тестове повідомлення")
# Maximus - Senior Developer
# 23:52
# ark patrol - let go (slowed + reverb) instrumental loop (20 minutes)
# Maximus - Senior Developer
# 23:54
# ми вже привикли один до оного нарешті норм
# я її за ляжки трогаю а вона не проти
# Maximus - Senior Developer
# 00:41
# https://youtu.be/ZSylXCZlEA4?si=jBVamPhFmEawId0h

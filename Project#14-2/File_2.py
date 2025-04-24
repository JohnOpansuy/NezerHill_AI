#Підключення бібліотек.
from flask import Flask, render_template, request, url_for, flash, redirect, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, HiddenField, SubmitField, EmailField, PasswordField, ValidationError
from wtforms.validators import DataRequired, Email
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from flask_mail import Mail, Message
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta
import logging
import base64
import html
import os
#Налаштування веб-сайту та його конфігурацій.
#?current_time = datetime.now()  # Отримати поточний час
#?time = current_time.strftime ("%H:%M:%S")  # Формат часу
#?date = current_time.strftime ("%Y-%m-%d")  # Формат дати
website = Flask (__name__)
website.config ["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.db"
#База даних підєднана до основної.
# website.config ["SQLALCHEMY_BINDS"] = {
#     "chats": "sqlite:///chat.db"
# }
website.config ["SQLALCHMEY_TRACK_MODIFICATIONS"] = False
#!website.config ["PERMANENT_SESSION_LIFETIME"] = timedelta (minutes = 30)
website.config ["SECRET_KEY"] = "Nezer_Hill"
#Папка для збереження зображень.
UPLOAD_FOLDER = "/static/images"
website.config ["UPLOAD_FOLDER"] = UPLOAD_FOLDER
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
#[----Класи захису відправлень запитів----].
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
    current_password = PasswordField ("Old Password")
    new_password = PasswordField ("New Password")
    confirm_password = PasswordField ("Confirm New Password")
    submit = SubmitField ("Save")
#Клас форми створення чату.
class CreateChatForm (FlaskForm):
    name = StringField ("Name", validators = [DataRequired()])
    submit = SubmitField ("Create")
#Клас форми редагування чату.
class EditChatForm (FlaskForm):
    name = StringField ("Name", validators = [DataRequired()])
    submit = SubmitField ("Save")
#[----Класи користувача----].
#Клас користувача.
class Users (UserMixin, basa.Model):
#Назва таблиці в базі данних.
    __tablename__ = "users"
    id = basa.Column (basa.Integer, primary_key = True)
    user_name = basa.Column (basa.String (50), nullable = False) #! Не юзати бо помилка сервнра тоді (, unique = True).
    user_mail = basa.Column (basa.String (80), unique = True, nullable = False)
    user_password = basa.Column (basa.String (100), nullable = False)
    user_data = basa.Column (basa.String (50), nullable = False)
    last_seen = basa.Column (basa.String (50), nullable = True)
    user_status = basa.Column (basa.String (80), nullable = False, default = "User")
    user_ai = basa.Column (basa.String (50), nullable = False, default = "Classic")
    user_picture = basa.Column (basa.String (100), nullable = True, default = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%2Fid%2FOIP.3U017h9GAnFM3aRkV-WLiwHaHa%3Fpid%3DApi&f=1&ipt=9877c6d5df703575f0accc40c405cc743d89324288b6e4e95f2378d5e23d2b46&ipo=images")
#Дані для безпеки.
    user_tryes = basa.Column (basa.Integer, default = 3)
    user_ip = basa.Column (basa.String (75))
    user_browser = basa.Column (basa.String (200))
#Звязок "один-до-багатьох" з чатами.
    user_chats = basa.relationship ("Chats", backref = "user", lazy = True)
#Клас чатів.
class Chats (basa.Model):
#Назва таблиці в базі данних.
    __tablename__ = "chats"
    #? __bind_key__ = "chats"
#Айді чату.
    id = basa.Column (basa.Integer, primary_key = True)
#Привязка до користувача.
    user_id = basa.Column (basa.Integer, basa.ForeignKey ("users.id"), nullable = False)
#Назва чату.
    chat_name = basa.Column (basa.String (80), unique = True, nullable = False)
#Колір чату.
    chat_color = basa.Column (basa.String (50), nullable = False)
#Дата створення.
    chat_data = basa.Column (basa.DateTime, default = datetime.utcnow)
#Встановлюємо звязок "один до багатьох" з повідомленнями.
    chat_messages = basa.relationship ("Messages", backref = "chat", lazy = True)
#Клас повідомлень.
class Messages (basa.Model):
#Назва таблиці в базі данних.
    __tablename__ = "messages"
#Айді повідомлень.
    id = basa.Column (basa.Integer, primary_key = True)
#Привязка до чату.
    chat_id = basa.Column (basa.Integer, basa.ForeignKey("chats.id"), nullable = False)
#Повідомлення користувача.
    user_message = basa.Column (basa.Text, nullable = False)
#Відповідь ШІ.
    ai_message = basa.Column (basa.Text, nullable = False)
#Час повідомлення.
    message_timestamp = basa.Column (basa.DateTime, default = datetime.utcnow)
#[----Створення таблиць----].
initialized = False  # Глобальна змінна для перевірки стану ініціалізації.
@website.before_request
def initialize_database():
    global initialized
    if not initialized:
        basa.create_all()
        #? print ("Таблиці створені під час першого запиту.")
        logging.warning ("Base are successfull created.")
        initialized = True
#Створення таблиць (при першому запуску).
# with website.app_context():
#     basa.create_all()
#[----Налаштування шаблону----].
#Деф налаштування шаблону.
@website.context_processor
def Shablon():
    return {"selected_option": current_user.user_ai if current_user.is_authenticated else None}
#[----Налаштування сесій та валідації користувача----].
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
            ip_address = request.headers.get ("X-Forwarded-For", request.remote_addr)
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
#[----Звичайні сторінки----].
#Деф головної сторінки.
@website.route("/", methods=["GET", "POST"])
@login_required
def Main_page():
    # Форма для створення та редагування чатів
    create_form = CreateChatForm()
    edit_form = EditChatForm()
    
    # Якщо отримано POST-запит – припустимо, що це запит на видалення чату
    if request.method == "POST":
        chat_name = request.form.get("name")
        if not chat_name:
            flash("Not gift the data for deleting.\nTry later.", "danger")
            logging.error(f"Not gift the data for deleting chat - {chat_name} user - {current_user.user_name}.")
            return redirect(url_for("Main_page"))
        
        chat = Chats.query.filter_by(chat_name=chat_name, user_id=current_user.id).first()
        if not chat:
            flash("Chat not found.", "danger")
            return redirect(url_for("Main_page"))
        
        try:
            basa.session.delete(chat)
            basa.session.commit()
            flash(f"You deleted chat - {chat_name}.", "success")
        except Exception as e:
            basa.session.rollback()
            flash("Error when delete chat.", "danger")
            logging.error(f"Error deleting chat - {chat_name}: {e}")
    
    # Отримуємо всі чати користувача
    chats = Chats.query.filter_by(user_id=current_user.id).all()
    return render_template("index.html", create_form=create_form, edit_form=edit_form, chats=chats)


@website.route("/create_chad", methods=["POST"])
def Create_chat():
    form = CreateChatForm()
    if form.validate_on_submit():
        name = form.name.data
        color = request.form.get("chat_color")  # Використовуємо "chat_color"
        
        if not name:
            flash("Not entered name. Try again.", "danger")
            return redirect(url_for("Main_page"))
        
        # Перевірка, чи вже існує чат із заданим ім'ям
        all_names = Chats.query.filter_by(chat_name=name, user_id=current_user.id).first()
        if all_names:
            flash("Name exist in basa.", "warning")
            return redirect(url_for("Main_page"))
        
        try:
            new_chat = Chats(user_id=current_user.id, chat_name=name, chat_color=str(color))
            basa.session.add(new_chat)
            basa.session.commit()
            flash(f"You created the chat - {name}", "success")
            logging.info(f"{current_user.user_name} - Create the chat - {name}")
            return redirect(url_for("Main_page"))
        except Exception as err:
            basa.session.rollback()
            flash("Error when creating chat. Try later.", "danger")
            logging.warning(f"({current_user.user_name}, {name}) - Error when creating chat.\n->{err}")
            return redirect(url_for("Main_page"))
    return redirect(url_for("Main_page"))


@website.route("/edit_chad", methods=["POST"])
def Edit_chat():
    form = EditChatForm()
    if form.validate_on_submit():
        new_name = form.name.data.strip()
        chat_id = request.form.get("chat_id")
        color = request.form.get("chat_color")

        chat = Chats.query.filter_by(id=chat_id, user_id=current_user.id).first()
        if not chat:
            flash("Chat not found.", "danger")
            return redirect(url_for("Main_page"))
        
        # Перевірка унікальності нового імені, виключаючи поточний чат
        existing_chat = Chats.query.filter(
            Chats.chat_name == new_name,
            Chats.user_id == current_user.id,
            Chats.id != chat.id
        ).first()
        if existing_chat:
            flash("A chat with this name already exists! Please choose a different name.", "warning")
            return redirect(url_for("Main_page"))
        
        try:
            chat.chat_name = new_name
            chat.chat_color = color or chat.chat_color
            basa.session.commit()
            flash(f"You updated your chat - {new_name}.", "success")
            logging.info(f"Updated chat - {new_name} for user {current_user.user_name}.")
        except Exception as err:
            basa.session.rollback()
            flash("Error when editing chat. Try later.", "danger")
            logging.warning(f"({current_user.user_name}, {new_name}) - Error when editing chat (ID: {chat_id}).\n->{err}")
    return redirect(url_for("Main_page"))

#Деф оброботки повідомлень.
@website.route ("/send_message", methods = ["POST"])
def Send_Massage(): pass
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
#[----Методи акаунта----].
#Деф сторінки акаунту.
@website.route("/acount", methods=["GET", "POST"])
@login_required
def Account_page():
#Створення екземпляра форми для редагування акаунту.
    form = EditAcountForm()
#Іф обробки даних після відправки форми.
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password_staruy = form.current_password.data
        password_novuy = form.new_password.data
        password_povtor = form.confirm_password.data
#Перевірка чи email вже існує в базі і не належить поточному користувачу.
        existing_user = Users.query.filter(
            Users.user_mail == email, Users.id != current_user.id
        ).first()
#Іф перевірки чи ічнує адреса електрона в базі даних.
        if existing_user:
            logging.error (f"New email already exists - {email}.")
            flash ("This email is already in use. Please try another one.", "warning")
            return redirect (url_for ("Account_page"))
        try:
            current_user.user_name = name
            current_user.user_mail = email
            # Іф перевірки і оновлення паролю (якщо введено).
            if check_password_hash (current_user.user_password, password_staruy):  # Перевіряємо старий пароль
                if password_novuy == password_povtor:  # Перевірка нового пароля та підтвердження
                    current_user.user_password = generate_password_hash (password_novuy)  # Оновлення нового пароля (хешування)
            # Збереження змін у базі даних.
            basa.session.commit()
            flash("All changes have been successfully saved.", "success")
            logging.info(f"Account information updated for user - {email}.")
            return redirect(url_for("Account_page"))
#У випадку помилки виконуємо відкат змін.
        except Exception as err:
            basa.session.rollback()
            flash("An error occurred. Changes were not saved.", "danger")
            logging.warning(f"Failed to update account {current_user.user_mail}. Details: {err}.")
            return redirect(url_for("Account_page"))

#Відображення сторінки профілю.
    return render_template (
        "acount.html",
        form = form,
        name = current_user.user_name,
        mail = current_user.user_mail,
        data = current_user.user_data,
        seen = current_user.last_seen,
        status = current_user.user_status,
        image = current_user.user_picture
    )
#Деф завантаження/збереження фото для профілю.
@website.route ("/upload_photo", methods = ["POST"])
def upload_photo():
    try:
#Отримуємо файл із запиту.
        file = request.files.get ("file")
#Отримуємо шлях.
        file_path = request.form.get ("filePath")
        if not file or not file_path:
            return jsonify ({"error": "File or file path not provided"}), 400
#Створюємо папку, якщо вона ще не існує.
        os.makedirs (os.path.dirname (file_path), exist_ok = True)
#Зберігаємо файл у заданому шляху.
        file.save (file_path)
        current_user.user_pictures = file_path
        basa.session.commit()
        # Повертаємо успішну відповідь
        return jsonify ({"message": "File uploaded successfully", "file_path": file_path}), 200
    except Exception as err:
        logging.error (f"Failed to upload photo: {err}")
        return jsonify ({"error": str (err)}), 500
#[--------Errores--------]
#Деф помилки 404-не має та сторінки.
@website.errorhandler (404)
def Page_not_founded (e):
    aurl = request.url
    logging.warning (f"Page or files not found: {aurl}")
    return render_template ("not_found.htm")
#Деф помилки 500-коли помилка серверу.
@website.errorhandler (500)
def internal_server_error (e):
    logging.error (f"Server error occurred: {str (e)}")
    return render_template ("error.htm", message = "An unexpected error occurred."), 500
#Деф помилки 403-коли помилка доступу користувача до такої сторінки.
@website.errorhandler (403)
def forbidden_error (e):
    logging.warning ("Forbidden access detected.")
    return render_template ("error.htm", message = "Access to this resource is forbidden."), 403
#Деф помилки 400-коли не коректний запит до сервера.
@website.errorhandler (400)
def bad_request_error (e):
    logging.info ("Bad request received.")
    return render_template ("error.htm", message = "Your request is invalid."), 400
#Деф помилки 405-коли не той метод запита до сервера.
@website.errorhandler (405)
def method_not_allowed (e):
    logging.info (f"Method Not Allowed: {request.method}")
    return render_template ("error.htm", message = "HTTP method not allowed for this route."), 405
#Деф помилки 200-коли сервер не працює.
@website.route ("/health")
def health_check():
#Симуляція здорового стану.
    try:
        return jsonify ({"status": "healthy"}), 200
    except Exception as e:
        logging.error (f"Health check failed: {e}")
        return render_template ("error.htm", message = "Server is down"), 500
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
# send_email("test@example.com", "Ім"я", "Тестова тема", "Тестове повідомлення")
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
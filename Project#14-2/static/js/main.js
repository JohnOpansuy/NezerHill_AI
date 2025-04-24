//location.reload(); //Оновлення Сторінки.
//Оновлення часу та дати.
function updateTimeAndDate() {
    const now = new Date();
    const timeElement = document.getElementById("time");
    const dateElement = document.getElementById("date");

    // Формат часу та дати
    timeElement.innerHTML = now.toLocaleTimeString(); // Поточний час
    dateElement.innerHTML = now.toLocaleDateString(); // Поточна дата
}

// Оновлення кожні 5 хвилин (300 000 мс)
setInterval(updateTimeAndDate, 300000); // Виконується кожні 5 хвилин
// І виклик для початкового встановлення значення
window.onload = updateTimeAndDate;
//--------------------------------------------------------------------.
function validateForm() {
    const acceptAllCheckbox = document.getElementById("acceptAll");
    if (!acceptAllCheckbox.checked) {
        alert("You must accept all terms and conditions to sign up.");
        return false;
    }
    return true;
}
setTimeout(() => {
    const flashMessages = document.querySelectorAll(".flash-message");
    flashMessages.forEach(msg => {
        msg.style.transition = "opacity 0.5s";
        msg.style.opacity = "0"; // Зникає
        setTimeout(() => msg.remove(), 500); // Видаляє з DOM
    });
}, 3000); // Час затримки (3 секунди)
//[-----Налаштування рядка відправки повідомлення-----].
//Вставлення курсора автоматично та без приховання плейсхолдера.
window.addEventListener("load", function() {
    document.getElementById("inputField").focus();
  });
//ТекстАреа переписки.
document.addEventListener("DOMContentLoaded", function() {
    const textarea = document.querySelector(".send_input");
    // Можна скорегувати maxHeight тут, якщо потрібно, або використати значення з CSS
    const maxHeight = 120; // максимальна висота у пікселях
    textarea.addEventListener("input", function() {
        // Скидаємо висоту, щоб scrollHeight був актуальний
        this.style.height = "auto";
        let newHeight = this.scrollHeight;
        if (newHeight > maxHeight) {
            newHeight = maxHeight;
            this.style.overflowY = "auto";
        } else {
            this.style.overflowY = "hidden";
        }
        this.style.height = newHeight + "px";
    });
});
//[--------Account--------].
function handleButtonClick(event) {
    const action = event.target.getAttribute("data-action"); // Отримуємо атрибут data-action

    const editContainer = document.getElementById("edit_container");
    const overlay = document.getElementById("overlay");

    if (action === "open") {
        // Відкрити форму та overlay
        editContainer.style.display = "block";
        overlay.style.display = "block";
    } else if (action === "close") {
        // Закрити форму та overlay
        editContainer.style.display = "none";
        overlay.style.display = "none";
    }
}
//Додаємо обробник подій через делегування.
document.addEventListener ("click", handleButtonClick);
//--Вибираня фото для профілю--.
document.getElementById("photoInput").addEventListener("change", async function () {
    const file = this.files[0]; // Отримуємо вибраний файл

    if (!file) {
        alert("Please select a file.");
        return;
    }

    // Формуємо шлях для збереження
    const filePath = `static/images/${file.name}`; 
    console.log("Generated file path:", filePath);

    const formData = new FormData();
    formData.append("file", file); // Додаємо файл для завантаження
    formData.append("filePath", filePath); // Додаємо шлях для файлу

    try {
        const response = await fetch("/upload_photo", {
            method: "POST",
            body: formData,
        });

        if (response.ok) {
            const result = await response.json();
            alert("Photo uploaded successfully!");
            location.reload(); // Оновлення сторінки після завантаження
        } else {
            alert("Failed to upload photo.");
        }
    } catch (error) {
        console.error("Error during photo upload:", error);
    }
});
//[--------Crete a new chat--------]
// Управління створенням нового чату
function CreateChat (event) {
    const action = event.target.getAttribute ("data-action");
    const createContainer = document.getElementById ("create_chat_container");
    const overlay = document.getElementById ("overlay");

    if (action === "create-chat") {
        createContainer.style.display = "block";
        overlay.style.display = "block";
    } else if (action === "cancel") {
        createContainer.style.display = "none";
        overlay.style.display = "none";
    }
};
document.addEventListener ("click", CreateChat)
//
function openEditChat (chatId) {
    // Припустимо, що всі контейнери сховані, і тепер показуємо тільки потрібний
    document.getElementById ('edit_chat_container_' + chatId).style.display = 'block';
    document.getElementById ('overlay').style.display = 'block';
}
function closeEditChat (chatId) {
    document.getElementById ('edit_chat_container_' + chatId).style.display = 'none';
    document.getElementById ('overlay').style.display = 'none';
}
  
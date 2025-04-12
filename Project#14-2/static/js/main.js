function updateTimeAndDate() {
    const now = new Date();
    const timeElement = document.getElementById('time');
    const dateElement = document.getElementById('date');

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
    const flashMessages = document.querySelectorAll('.flash-message');
    flashMessages.forEach(msg => {
        msg.style.transition = "opacity 0.5s";
        msg.style.opacity = "0"; // Зникає
        setTimeout(() => msg.remove(), 500); // Видаляє з DOM
    });
}, 3000); // Час затримки (3 секунди)
//[--------Account--------].

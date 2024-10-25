const modal = document.getElementById('authModal');
const btn = document.getElementById('registerAndLogin');
const span = document.getElementsByClassName('close')[0];

btn.onclick = function() {
    modal.classList.add('show');
}

span.onclick = function() {
    modal.classList.remove('show');
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.classList.remove('show');
    }
}

// Обработка формы регистрации
document.getElementById('registrationForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('regUsername').value;
    const email = document.getElementById('regEmail').value;
    const password = document.getElementById('regPassword').value;
    alert(`Регистрация успешна!\nИмя пользователя: ${username}\nEmail: ${email}\nПароль: ${password}`);
    modal.classList.remove('show');
});

// Обработка формы авторизации
document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const username = document.getElementById('loginUsername').value;
    const password = document.getElementById('loginPassword').value;
    alert(`Авторизация успешна!\nИмя пользователя: ${username}\nПароль: ${password}`);
    modal.classList.remove('show');
});
// MENÚ
const toggleMenu = document.querySelector('.menu-toggle');
const navList = document.querySelector('.nav-list');

toggleMenu.addEventListener('click', () => {
  navList.classList.toggle('active');
});

document.querySelectorAll('.nav-list a').forEach(link => {
  link.addEventListener('click', () => {
    navList.classList.remove('active');
  });
});

// FORMULARIO
const form = document.getElementById('formulario');
const feedback = document.getElementById('feedback');

form.addEventListener('submit', function (e) {
  e.preventDefault();

  const nombre = form.nombre.value.trim();
  const email = form.email.value.trim();
  const telefono = form.telefono.value.trim();
  const interes = form.interes.value;
  const regexEmail = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  const regexTelefono = /^\d{8,15}$/;

  if (!nombre || !email || !telefono || !interes) {
    feedback.textContent = 'Por favor completá todos los campos.';
    feedback.style.color = 'red';
    return;
  }

  if (!regexEmail.test(email)) {
    feedback.textContent = 'Ingresá un email válido.';
    feedback.style.color = 'red';
    return;
  }

  if (!regexTelefono.test(telefono)) {
    feedback.textContent = 'El teléfono debe contener sólo números (entre 8 y 15 dígitos).';
    feedback.style.color = 'red';
    return;
  }
 
  feedback.textContent = '¡Gracias por tu consulta! Nos contactaremos pronto.';
  feedback.style.color = 'green';

  form.reset();
});

// MODO OSCURO
const toggleBtn = document.getElementById('modoOscuroToggle');
const body = document.body;

if (localStorage.getItem('modoOscuro') === 'activado') {
  body.classList.add('dark-mode');
  toggleBtn.textContent = 'Modo claro';
}

toggleBtn.addEventListener('click', () => {
  body.classList.toggle('dark-mode');
  if (body.classList.contains('dark-mode')) {
    localStorage.setItem('modoOscuro', 'activado');
    toggleBtn.textContent = 'Modo claro';
  } else {
    localStorage.setItem('modoOscuro', 'desactivado');
    toggleBtn.textContent = 'Modo oscuro';
  }
});

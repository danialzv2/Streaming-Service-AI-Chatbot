let isLoading = false;

function appendMessage(role, text) {
  const container = document.getElementById('messages');

  const msg = document.createElement('div');
  msg.className = `msg ${role}`;

  const bubble = document.createElement('div');
  bubble.className = 'bubble';
  bubble.innerHTML = text;

  msg.appendChild(bubble);
  container.appendChild(msg);

  container.scrollTop = container.scrollHeight;
}

function showTyping() {
  appendMessage('bot', '...');
}

function removeWelcome() {
  const w = document.getElementById('welcome');
  if (w) w.remove();
}

async function sendMessage(overrideText) {
  if (isLoading) return;

  const input = document.getElementById('chatInput');
  const text = (overrideText || input.value).trim();
  if (!text) return;

  input.value = '';
  isLoading = true;

  removeWelcome();
  appendMessage('user', text);
  showTyping();

  try {
    const res = await fetch('http://localhost:8000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ message: text })
    });

    const data = await res.json();

    document.querySelector('.msg.bot:last-child').remove();
    appendMessage('bot', data.response);

  } catch (e) {
    appendMessage('bot', 'Error connecting to server');
  }

  isLoading = false;
}

function sendSuggestion(btn) {
  sendMessage(btn.textContent);
}

function newChat() {
  document.getElementById('messages').innerHTML = '';
}

function setCategory(el, cat) {
  document.querySelectorAll('.sidebar-cat').forEach(c => c.classList.remove('active'));
  el.classList.add('active');
}
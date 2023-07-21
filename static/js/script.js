const chatOutput = document.getElementById('chat-output');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');

// Event listener for send button click
sendBtn.addEventListener('click', () => {
  sendMessage();
});

// Event listener for user input enter key press
userInput.addEventListener('keydown', (event) => {
  if (event.key === 'Enter') {
    sendMessage();
  }
});

// Function to send user message and receive bot response

  // Function to send user message and receive bot response
function sendMessage() {
    const message = userInput.value.trim();
    if (message !== '') {
      appendMessage('user', message);
  
      // Send user message to Rasa API and receive response
      fetch('http://localhost:5055/webhooks/rest/webhook', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: message,
        }),
      })
        .then((response) => response.json())
        .then((data) => {
          const botResponse = data.botResponse;
  
          appendMessage('bot', botResponse);
  
          // Update the response field with the bot's response
          document.getElementById('response').textContent = botResponse;
  
          // Clear the user input
          userInput.value = '';
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    }
  }
  


// Function to append a message to the chat output
function appendMessage(sender, message) {
  const messageDiv = document.createElement('div');
  messageDiv.classList.add(sender === 'user' ? 'user-message' : 'bot-message');
  messageDiv.textContent = message;

  chatOutput.appendChild(messageDiv);

  // Scroll to the bottom of the chat output
  chatOutput.scrollTop = chatOutput.scrollHeight;
}

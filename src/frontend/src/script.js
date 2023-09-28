document.addEventListener("DOMContentLoaded", function () {
    const messageInput = document.getElementById("message-input");
    const sendButton = document.getElementById("send-button");
    const chatMessages = document.getElementById("chat-messages");

    sendButton.addEventListener("click", function () {
        const messageText = messageInput.value.trim();

        if (messageText !== "") {
            const messageElement = document.createElement("div");
            messageElement.classList.add("message");
            messageElement.textContent = messageText;
            chatMessages.appendChild(messageElement);

            // Clear the input field
            messageInput.value = "";

            // Scroll to the bottom to show the latest message
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }
    });

    // Listen for the Enter key press in the input field
    messageInput.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            sendButton.click();
            event.preventDefault(); // Prevents the Enter key from adding a newline in the input field
        }
    });
});

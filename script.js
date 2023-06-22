function sendMessage() {
  var messageInput = document.getElementById("message-input");
  var message = messageInput.value.trim();

  if (message !== "") {
    var messageContainer = document.createElement("div");
    messageContainer.className = "message user1"; // Change to 'user2' for the other user

    var senderSpan = document.createElement("span");
    senderSpan.className = "sender";
    senderSpan.innerText = "You"; // Change to 'User 2' for the other user

    var contentDiv = document.createElement("div");
    contentDiv.className = "content";
    contentDiv.innerText = message;

    messageContainer.appendChild(senderSpan);
    messageContainer.appendChild(contentDiv);

    document.querySelector(".messages").appendChild(messageContainer);

    messageInput.value = "";
  }
}

let input = document.getElementById("message-input");

// Add event listener to the input
input.addEventListener("keydown", handleKeyDown);

function handleKeyDown(event) {
  if (event.keyCode === 13) {
    // 13 is the key code for Enter
    event.preventDefault(); // Prevent form submission
    sendMessage(); // Trigger the send message function
  }
}

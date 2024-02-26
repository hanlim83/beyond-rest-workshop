const HOST = "http://localhost:3000";

const socket = io(HOST);

let messages = [];

socket.on("connect", (data) => {
  // TODO: console.log a message when client is connected to the websocket server
  console.log("Connected to the server");
});

socket.on("disconnect", (data) => {
  // TODO: console.log a message when client is disconnected from the websocket server
  console.log("Disconnected from the server");
});

//inserts a message you are sending into the frontend UI
function insertOwnMessage(message) {
  let messageHtml = `<div class="chat chat-end">
<div class="chat-bubble chat-bubble-primary">${message}</div>
</div>`;
  document
    .getElementById("last-pointer")
    .insertAdjacentHTML("beforebegin", messageHtml);
}

//inserts an incoming message into the frontend UI
function insertIncomingMessage(name, message) {
  let messageHtml = `<div class="chat chat-start">
  <div class="chat-header">
  ${name}
<div class="chat-bubble chat-bubble-secondary">${message}</div>
</div>
</div>`;
  document
    .getElementById("last-pointer")
    .insertAdjacentHTML("beforebegin", messageHtml);
}

// on receiving an incoming message, insert incoming new message into the chat ui
socket.on("receiveMessage", (data) => {
  let { name, message } = JSON.parse(data);
  let yourName = document.getElementById("chat-name").value;
  if (yourName !== name) {
    // TODO: use an existing function to insert the new incoming message
    // ===========================================
    console.log("Received message from " + name + " | " + message);
    insertIncomingMessage(name, message);
    // ===========================================
    // implements scrolling behaviour for chat
    document
      .getElementById("last-pointer")
      .scrollIntoView({ behavior: "smooth" });
  }
});

function sendMessage() {
  //checks if you have a name
  let yourName = document.getElementById("chat-name").value;

  if (yourName) {
    //get message from input box
    let chatInput = document.getElementById("chat-input");
    let message = chatInput.value;

    //only sends message if there is one
    if (message) {
      let messageObject = {
        name: yourName,
        message: message,
      };

      //converts your message object to a string for socketio emitting
      let messageObjectString = JSON.stringify(messageObject);

      //adds your sent message to the message history
      messages.push(messageObject);

      // TODO: use socket.io to emit a message as the right event HINT: refer to the backend code to know what is the right event
      // ===========================================
      socket.emit("chatMessage", messageObjectString);
      // ===========================================

      // TODO: use an existing function to insert the new incoming message
      // ===========================================
      insertOwnMessage(message);
      // ===========================================
      //clears chat input box
      chatInput.value = "";

      // scrolls to latest message
      document
        .getElementById("last-pointer")
        .scrollIntoView({ behavior: "smooth" });
    } else {
      //creates an alert to remind you to type a message
      alert("Please type in your message!");
    }
  } else {
    //creates an alert to remind you to give yourself a name
    alert("Please type in your name!");
  }
}

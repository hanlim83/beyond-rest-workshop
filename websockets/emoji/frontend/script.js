// TODO: fill in the right host, HINT: reference the backend code!
// ===========================================
const HOST = "";
// ===========================================

const socket = io(HOST);

let messages = [];

const jsConfetti = new JSConfetti();

socket.on("connect", (data) => {
  console.log("connected to web socket");
  console.log(data);
});

socket.on("disconnect", (data) => {
  console.log("disconnected from web socket");
  console.log(data);
});

socket.on("receiveMessage", async (data) => {
  // TODO: use console.log to check out the data that is being sent,
  // ===========================================

  // ===========================================

  // TODO: using js confetti docs here: https://www.npmjs.com/package/js-confetti,
  // complete the following to send the emojis flying!
  // ===========================================
  await jsConfetti.addConfetti();
  jsConfetti.clearCanvas();
  // ===========================================
});

function onPress(buttonFeatures) {
  const { value } = buttonFeatures;
  // TODO: use socket io to emit a message of the right event, HINT: use backend to reference which event to emit to
  // ===========================================

  // ===========================================
}

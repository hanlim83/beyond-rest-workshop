// Imported Modules
// =====================================
const express = require("express");
const http = require("http");
const cors = require("cors");
const { Server } = require("socket.io");
// =====================================

// express app
const app = express();

app.use(cors()); // Allows cross-origin requests

// Create a HTTP server
const server = http.createServer(app);
const io = new Server(server, {
  cors: {
    origin: "*", // Allow all origins
  },
});

// When a client connects
io.on("connection", (socket) => {
  // TODO: Connect to a room
  socket.on("joinRoom", (roomId) => {
    // TODO: Use socket.io to join a room
    // ===========================================
    // ===========================================
  });

  // TODO: Log a message to console that a user is connected
  // ===========================================

  // ===========================================
  // Handle chat message
  socket.on("chatMessage", (message) => {
    // TODO: Use socket.io to emit the message to all connected clients
    // ===========================================
    // ===========================================
  });

  // When client disconnects
  socket.on("disconnect", () => {
    // TODO: Log a message to console that a user is disconnected
    // ===========================================
    // ===========================================
  });
});

const PORT = 3000;

// Start the server
server.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});

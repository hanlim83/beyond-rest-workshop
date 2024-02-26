### Websockets 🔌

#### Directories 🪧

- `./chat`
- `./emoji`

#### Some tools to help with debugging ✍🏼

- Install [Postman (10.7.3)](https://www.postman.com/downloads/)
- Click "New" in Postman
- Click "Websocket Request (Beta)"
- Fill in the host, edit event, and messages for testing

#### Installation Guide 💾

We're using a node.js server, and vanilla HTML/JS frontend for our practice applications. Here's a set of instructions to help with setting up:

- Install [Node](https://nodejs.org/en/download)
- Go to `websockets` and run the following command to start the **chat** application (change directory if you are building **emoji**):

If you are a Windows User,
```
cd ./chat
run.bat
```

If you are a Linux/Mac user,
```
cd ./chat
chmod +x ./run.sh
./run.sh
```

#### For Frontend 🏞️

- For the frontend, use the extension [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) for a better developer experience.
- Restart VS Code
- Click on "Go Live" at the bottom right corner to have hot reload of your code

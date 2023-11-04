function errorHandler(err) {
  console.error(err);
  alert("出现问题，请刷新页面重试。");
}

class Queue {
  constructor() {
    this.queue = [];
    this.isRunning = false;
  }

  addTask(func, context, ...args) {
    return new Promise((resolve, reject) => {
      this.queue.push({ func, context, args, resolve, reject });
      this.run();
    });
  }

  async run() {
    if (this.isRunning || this.queue.length === 0) {
      return;
    }
    this.isRunning = true;
    const { func, context, args, resolve, reject } = this.queue.shift();
    try {
      const result = await func.apply(context, args);
      resolve(result);
    } catch (error) {
      reject(error);
    }

    this.isRunning = false;
    this.run();
  }
}

const asyncQueue = new Queue();

var board = [
  [0, 0, 0],
  [0, 0, 0],
  [0, 0, 0],
];
var frozen = false;

function clearBoard() {
  for (var x = 0; x < 3; x++) {
    for (var y = 0; y < 3; y++) {
      htmlBoard = document.getElementById(String(x) + String(y));
      htmlBoard.style.color = "#444";
      htmlBoard.innerHTML = "";
    }
  }
  htmlMsg = document.getElementById("message");
  htmlMsg.innerHTML = "";
  frozen = false;
}

function renderBoard(data) {
  board = data["board"];
  for (var x = 0; x < 3; x++) {
    for (var y = 0; y < 3; y++) {
      htmlBoard = document.getElementById(String(x) + String(y));
      htmlBoard.style.color = "#444";
      if (board[x][y] == 1) {
        htmlBoard = document.getElementById(String(x) + String(y));
        htmlBoard.innerHTML = "O";
      } else if (board[x][y] == -1) {
        htmlBoard = document.getElementById(String(x) + String(y));
        htmlBoard.innerHTML = "X";
      } else {
        htmlBoard = document.getElementById(String(x) + String(y));
        htmlBoard.innerHTML = "";
      }
    }
  }
  if ("msg" in data) {
    htmlMsg = document.getElementById("message");
    htmlMsg.innerHTML = data["msg"];
  }
  renderResult(data);
}

function renderResult(data) {
  var lines;
  var cell;
  board = data["board"];
  if (board[0][0] == 1 && board[0][1] == 1 && board[0][2] == 1)
    lines = [
      [0, 0],
      [0, 1],
      [0, 2],
    ];
  else if (board[1][0] == 1 && board[1][1] == 1 && board[1][2] == 1)
    lines = [
      [1, 0],
      [1, 1],
      [1, 2],
    ];
  else if (board[2][0] == 1 && board[2][1] == 1 && board[2][2] == 1)
    lines = [
      [2, 0],
      [2, 1],
      [2, 2],
    ];
  else if (board[0][0] == 1 && board[1][0] == 1 && board[2][0] == 1)
    lines = [
      [0, 0],
      [1, 0],
      [2, 0],
    ];
  else if (board[0][1] == 1 && board[1][1] == 1 && board[2][1] == 1)
    lines = [
      [0, 1],
      [1, 1],
      [2, 1],
    ];
  else if (board[0][2] == 1 && board[1][2] == 1 && board[2][2] == 1)
    lines = [
      [0, 2],
      [1, 2],
      [2, 2],
    ];
  else if (board[0][0] == 1 && board[1][1] == 1 && board[2][2] == 1)
    lines = [
      [0, 0],
      [1, 1],
      [2, 2],
    ];
  else if (board[2][0] == 1 && board[1][1] == 1 && board[0][2] == 1)
    lines = [
      [2, 0],
      [1, 1],
      [0, 2],
    ];

  // 非平局
  if (lines !== undefined) {
    frozen = true;
    for (var i = 0; i < lines.length; i++) {
      cell = document.getElementById(String(lines[i][0]) + String(lines[i][1]));
      cell.style.color = "red";
    }
  }
}

async function getBoard() {
  let url = window.location.href; // 获取当前 URL
  return fetch(url, {
    method: "POST", // 设置方法为 POST
    headers: {
      "Content-Type": "application/json", // 设置内容类型为 JSON
    },
    body: JSON.stringify({ act: "getBoard" }), // 将数据转换为 JSON 格式
  }).catch(errorHandler);
}

async function setMove(x, y) {
  if (board[x][y] != 0) {
    return;
  }
  if (frozen) {
    return;
  }
  let url = window.location.href; // 获取当前 URL
  let data = { x: x, y: y }; // 设置要发送的数据
  return fetch(url, {
    method: "POST", // 设置方法为 POST
    headers: {
      "Content-Type": "application/json", // 设置内容类型为 JSON
    },
    body: JSON.stringify(data), // 将数据转换为 JSON 格式
  }).catch(errorHandler);
}

/* main */
function clickedCell(cell) {
  var x = cell.id.split("")[0];
  var y = cell.id.split("")[1];

  asyncQueue.addTask(async () => {
    await setMove(x, y)
      .then((response) => response.json()) // 解析响应为 JSON
      .then((data) => {
        renderBoard(data); // 渲染棋盘
      });
  }, null);
}

/* Restart the game */
function restartBnt(button) {
  asyncQueue.addTask(async () => {
    clearBoard();
    let url = window.location.href; // 获取当前 URL
    await fetch(url, {
      method: "POST", // 设置方法为 POST
      headers: {
        "Content-Type": "application/json", // 设置内容类型为 JSON
      },
      body: JSON.stringify({ act: "reset" }), // 将数据转换为 JSON 格式
    })
      .then((response) => response.json()) // 解析响应为 JSON
      .then((data) => {
        renderBoard(data); // 渲染棋盘
      })
      .catch(errorHandler);
  }, null);
}

asyncQueue.addTask(async function () {
  await getBoard()
    .then((response) => response.json())
    .then((data) => {
      renderBoard(data);
    });
}, null);

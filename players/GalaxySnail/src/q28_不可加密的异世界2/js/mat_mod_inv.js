const readline = require("readline");
const process = require("process");
const mathjs = require("mathjs");
const GaussJacques = require("gauss-jacques");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on("line", (line) => {
    let mat = mathjs.matrix(JSON.parse(line));
    console.warn(`mat.size() = ${mat.size()}`)
    let inv = GaussJacques.inverseModular(mat, 257);
    if (inv === null || inv === undefined) {
        process.exit(1);
    }
    console.warn("found.")
    console.log(JSON.stringify(inv.toArray()));
    rl.close();
})

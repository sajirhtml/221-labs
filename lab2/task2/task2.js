const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let lines = [];
rl.on('line', (line) => {
    lines.push(line);
    if (lines.length === 3) {
        solve();
        rl.close();
    }
});

function solve() {
    const [n, m, k] = lines[0].split(' ').map(Number);
    const a = lines[1].split(' ').map(Number);
    const b = lines[2].split(' ').map(Number);
    
    let i = 0;
    let j = m - 1;
    let bestI = 1, bestJ = 1;
    let minDiff = Number.MAX_SAFE_INTEGER;
    
    while (i < n && j >= 0) {
        const currentSum = a[i] + b[j];
        const diff = Math.abs(currentSum - k);
        
        if (diff < minDiff) {
            minDiff = diff;
            bestI = i + 1;
            bestJ = j + 1;
        }
        
        if (currentSum === k) {
            console.log((i + 1) + " " + (j + 1));
            process.exit();
        }
        
        if (currentSum < k) {
            i++;
        } else {
            j--;
        }
    }
    
    console.log(bestI + " " + bestJ);
}
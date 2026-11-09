<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
<title>Ball Jump</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
  html, body {
    width: 100%; height: 100%; overflow: hidden;
    background: #1b1f3a; touch-action: none; user-select: none;
    font-family: Arial, sans-serif;
  }
  canvas { display: block; width: 100%; height: 100%; }
  #hud {
    position: fixed; top: 12px; left: 0; right: 0;
    display: flex; justify-content: space-between; padding: 0 16px;
    color: #fff; font-size: 18px; font-weight: bold; pointer-events: none;
  }
  #msg {
    position: fixed; inset: 0; display: flex; flex-direction: column;
    align-items: center; justify-content: center; text-align: center;
    color: #fff; pointer-events: none;
  }
  #msg h1 { font-size: 36px; margin-bottom: 10px; }
  #msg p { font-size: 18px; opacity: .85; }
</style>
</head>
<body>
<canvas id="game"></canvas>
<div id="hud"><span id="score">Score: 0</span><span id="best">Best: 0</span></div>
<div id="msg"><h1>🏀 Ball Jump</h1><p>Jump karne ke liye screen tap karo</p></div>

<script>
const canvas = document.getElementById('game');
const ctx = canvas.getContext('2d');
const scoreEl = document.getElementById('score');
const bestEl = document.getElementById('best');
const msg = document.getElementById('msg');

let W, H, groundY, scale;
function resize() {
  const dpr = window.devicePixelRatio || 1;
  W = window.innerWidth; H = window.innerHeight;
  canvas.width = W * dpr; canvas.height = H * dpr;
  ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  groundY = H * 0.75;
  scale = Math.min(W, H) / 400;
}
window.addEventListener('resize', resize);
resize();

let best = 0;
try { best = parseInt(localStorage.getItem('ballJumpBest')) || 0; } catch (e) {}
bestEl.textContent = 'Best: ' + best;

let ball, obstacles, score, speed, spawnTimer, state, clouds;

function reset() {
  ball = { x: W * 0.2, y: groundY - 20 * scale, r: 20 * scale, vy: 0, onGround: true };
  obstacles = [];
  clouds = [];
  for (let i = 0; i < 4; i++) clouds.push({ x: Math.random() * W, y: 40 + Math.random() * H * 0.3, s: 0.5 + Math.random() });
  score = 0;
  speed = 4 * scale;
  spawnTimer = 60;
  scoreEl.textContent = 'Score: 0';
}

function jump() {
  if (state === 'ready' || state === 'over') {
    reset();
    state = 'play';
    msg.style.display = 'none';
    return;
  }
  if (ball.onGround) {
    ball.vy = -13 * scale;
    ball.onGround = false;
  }
}

window.addEventListener('touchstart', e => { e.preventDefault(); jump(); }, { passive: false });
window.addEventListener('mousedown', jump);
window.addEventListener('keydown', e => { if (e.code === 'Space' || e.code === 'ArrowUp') jump(); });

function spawnObstacle() {
  const h = (25 + Math.random() * 35) * scale;
  const w = (20 + Math.random() * 20) * scale;
  obstacles.push({ x: W + 20, w, h });
}

function update() {
  // ball physics
  ball.vy += 0.7 * scale;
  ball.y += ball.vy;
  if (ball.y >= groundY - ball.r) {
    ball.y = groundY - ball.r;
    ball.vy = 0;
    ball.onGround = true;
  }

  // obstacles
  spawnTimer--;
  if (spawnTimer <= 0) {
    spawnObstacle();
    spawnTimer = 60 + Math.random() * 70 - speed * 2;
    if (spawnTimer < 40) spawnTimer = 40;
  }
  for (const o of obstacles) o.x -= speed;
  while (obstacles.length && obstacles[0].x + obstacles[0].w < 0) {
    obstacles.shift();
    score++;
    scoreEl.textContent = 'Score: ' + score;
    speed += 0.12 * scale;
  }

  // clouds
  for (const c of clouds) {
    c.x -= c.s;
    if (c.x < -80) { c.x = W + 80; c.y = 40 + Math.random() * H * 0.3; }
  }

  // collision (circle vs rectangle)
  for (const o of obstacles) {
    const ox = o.x, oy = groundY - o.h;
    const cx = Math.max(ox, Math.min(ball.x, ox + o.w));
    const cy = Math.max(oy, Math.min(ball.y, oy + o.h));
    const dx = ball.x - cx, dy = ball.y - cy;
    if (dx * dx + dy * dy < (ball.r - 3) * (ball.r - 3)) {
      gameOver();
      return;
    }
  }
}

function gameOver() {
  state = 'over';
  if (score > best) {
    best = score;
    try { localStorage.setItem('ballJumpBest', best); } catch (e) {}
    bestEl.textContent = 'Best: ' + best;
  }
  msg.innerHTML = '<h1>Game Over 💥</h1><p>Score: ' + score + '</p><p>Dobara khelne ke liye tap karo</p>';
  msg.style.display = 'flex';
}

function draw() {
  // sky
  const g = ctx.createLinearGradient(0, 0, 0, H);
  g.addColorStop(0, '#1b1f3a');
  g.addColorStop(1, '#4a6fa5');
  ctx.fillStyle = g;
  ctx.fillRect(0, 0, W, H);

  // clouds
  ctx.fillStyle = 'rgba(255,255,255,0.25)';
  for (const c of clouds) {
    ctx.beginPath();
    ctx.arc(c.x, c.y, 18 * c.s * scale, 0, Math.PI * 2);
    ctx.arc(c.x + 20 * c.s * scale, c.y + 4, 14 * c.s * scale, 0, Math.PI * 2);
    ctx.arc(c.x - 20 * c.s * scale, c.y + 4, 14 * c.s * scale, 0, Math.PI * 2);
    ctx.fill();
  }

  // ground
  ctx.fillStyle = '#2e7d32';
  ctx.fillRect(0, groundY, W, H - groundY);
  ctx.fillStyle = '#1b5e20';
  ctx.fillRect(0, groundY, W, 6);

  // obstacles
  ctx.fillStyle = '#e53935';
  for (const o of obstacles) {
    ctx.fillRect(o.x, groundY - o.h, o.w, o.h);
  }

  // ball shadow
  const shadowScale = 1 - Math.min(0.6, (groundY - ball.r - ball.y) / (200 * scale));
  ctx.fillStyle = 'rgba(0,0,0,0.3)';
  ctx.beginPath();
  ctx.ellipse(ball.x, groundY + 4, ball.r * shadowScale, 5 * scale * shadowScale, 0, 0, Math.PI * 2);
  ctx.fill();

  // ball
  const bg = ctx.createRadialGradient(ball.x - ball.r / 3, ball.y - ball.r / 3, ball.r / 6, ball.x, ball.y, ball.r);
  bg.addColorStop(0, '#fff176');
  bg.addColorStop(1, '#ff9800');
  ctx.fillStyle = bg;
  ctx.beginPath();
  ctx.arc(ball.x, ball.y, ball.r, 0, Math.PI * 2);
  ctx.fill();
}

function loop() {
  if (state === 'play') update();
  draw();
  requestAnimationFrame(loop);
}

state = 'ready';
reset();
loop();
</script>
</body>
</html>

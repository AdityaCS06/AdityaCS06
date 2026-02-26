<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AdityaCS06 – GitHub Profile</title>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Syne:wght@400;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0a0a0f;
    --surface: #111118;
    --border: #1e1e2e;
    --accent: #7c3aed;
    --accent2: #06b6d4;
    --accent3: #10b981;
    --text: #e2e8f0;
    --muted: #64748b;
    --glow: rgba(124,58,237,0.3);
  }

  * { margin: 0; padding: 0; box-sizing: border-box; }

  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'Syne', sans-serif;
    min-height: 100vh;
    overflow-x: hidden;
    background-image:
      radial-gradient(ellipse 80% 50% at 20% 0%, rgba(124,58,237,0.12) 0%, transparent 60%),
      radial-gradient(ellipse 60% 40% at 80% 100%, rgba(6,182,212,0.08) 0%, transparent 60%);
  }

  .noise {
    position: fixed; inset: 0; pointer-events: none; z-index: 0;
    opacity: 0.025;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
  }

  .container {
    max-width: 860px;
    margin: 0 auto;
    padding: 48px 24px;
    position: relative; z-index: 1;
  }

  /* HEADER */
  .header {
    text-align: center;
    margin-bottom: 56px;
    animation: fadeUp 0.7s ease both;
  }

  .header h1 {
    font-size: clamp(2.2rem, 5vw, 3.4rem);
    font-weight: 800;
    letter-spacing: -0.03em;
    background: linear-gradient(135deg, #fff 30%, var(--accent) 70%, var(--accent2));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }

  .header .handle {
    font-family: 'JetBrains Mono', monospace;
    color: var(--accent2);
    font-size: 0.95rem;
    margin-top: 6px;
    letter-spacing: 0.1em;
  }

  .header .tagline {
    color: var(--muted);
    font-size: 0.9rem;
    margin-top: 14px;
    max-width: 480px;
    margin-left: auto; margin-right: auto;
    line-height: 1.6;
  }

  /* SECTION */
  .section {
    margin-bottom: 44px;
    animation: fadeUp 0.7s ease both;
  }

  .section-title {
    font-size: 0.7rem;
    font-family: 'JetBrains Mono', monospace;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--accent);
    margin-bottom: 18px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .section-title::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, var(--border), transparent);
  }

  /* ABOUT CARD */
  .about-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }

  @media (max-width: 540px) { .about-grid { grid-template-columns: 1fr; } }

  .about-item {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 14px 16px;
    display: flex;
    align-items: flex-start;
    gap: 12px;
    transition: border-color 0.2s, transform 0.2s;
  }

  .about-item:hover {
    border-color: var(--accent);
    transform: translateY(-2px);
  }

  .about-icon { font-size: 1.2rem; flex-shrink: 0; margin-top: 1px; }

  .about-item p {
    font-size: 0.82rem;
    color: var(--muted);
    line-height: 1.5;
  }

  .about-item p strong {
    display: block;
    color: var(--text);
    font-size: 0.78rem;
    font-family: 'JetBrains Mono', monospace;
    margin-bottom: 2px;
    color: var(--accent2);
  }

  /* TECH STACK */
  .tech-grid {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
  }

  .tech-chip {
    display: flex;
    align-items: center;
    gap: 7px;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 7px 12px;
    font-size: 0.78rem;
    font-family: 'JetBrains Mono', monospace;
    color: var(--text);
    transition: all 0.2s;
    cursor: default;
  }

  .tech-chip:hover {
    border-color: var(--chip-color, var(--accent));
    background: color-mix(in srgb, var(--chip-color, var(--accent)) 8%, var(--surface));
    color: white;
    transform: translateY(-2px);
    box-shadow: 0 4px 16px color-mix(in srgb, var(--chip-color, var(--accent)) 25%, transparent);
  }

  .tech-chip img {
    width: 16px;
    height: 16px;
    object-fit: contain;
    filter: brightness(0.9);
  }

  /* STATS */
  .stats-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
  }

  @media (max-width: 540px) { .stats-grid { grid-template-columns: 1fr; } }

  .stats-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
    transition: border-color 0.2s;
  }

  .stats-card:hover { border-color: var(--accent); }

  .stats-card img { width: 100%; display: block; }

  .stats-card.full { grid-column: 1 / -1; }

  /* TROPHIES */
  .trophies-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: 12px;
    overflow: hidden;
    text-align: center;
    padding: 4px;
  }

  .trophies-card img { max-width: 100%; display: block; margin: 0 auto; }

  /* FUN FACT */
  .fun-fact {
    background: linear-gradient(135deg, rgba(124,58,237,0.1), rgba(6,182,212,0.08));
    border: 1px solid rgba(124,58,237,0.3);
    border-radius: 12px;
    padding: 16px 20px;
    font-size: 0.85rem;
    color: var(--muted);
    display: flex;
    gap: 10px;
    align-items: center;
  }

  .fun-fact span { font-size: 1.3rem; }

  /* VISITOR */
  .footer {
    text-align: center;
    margin-top: 48px;
    padding-top: 24px;
    border-top: 1px solid var(--border);
    color: var(--muted);
    font-size: 0.75rem;
    font-family: 'JetBrains Mono', monospace;
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
  }

  @keyframes fadeUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }

  .s1 { animation-delay: 0.1s; }
  .s2 { animation-delay: 0.2s; }
  .s3 { animation-delay: 0.3s; }
  .s4 { animation-delay: 0.4s; }
  .s5 { animation-delay: 0.5s; }
  .s6 { animation-delay: 0.6s; }

  .pulse-dot {
    width: 6px; height: 6px; border-radius: 50%;
    background: var(--accent3);
    display: inline-block;
    animation: pulse 2s infinite;
  }

  @keyframes pulse {
    0%,100% { opacity:1; box-shadow: 0 0 0 0 rgba(16,185,129,0.4); }
    50% { opacity:0.7; box-shadow: 0 0 0 6px rgba(16,185,129,0); }
  }
</style>
</head>
<body>
<div class="noise"></div>
<div class="container">

  <!-- HEADER -->
  <div class="header">
    <div style="margin-bottom:10px; font-size:0.7rem; font-family:'JetBrains Mono',monospace; color:var(--accent); letter-spacing:0.2em; text-transform:uppercase; display:flex; align-items:center; justify-content:center; gap:8px;">
      <span class="pulse-dot"></span> open to collaborate
    </div>
    <h1>Aditya CS06</h1>
    <div class="handle">@AdityaCS06</div>
    <p class="tagline">Building scalable backend systems · FastAPI & PostgreSQL · Query optimizer by passion, developer by trade</p>
  </div>

  <!-- ABOUT -->
  <div class="section s1">
    <div class="section-title">💫 About Me</div>
    <div class="about-grid">
      <div class="about-item">
        <span class="about-icon">🔭</span>
        <p><strong>// currently working on</strong>Scalable backend systems using FastAPI &amp; PostgreSQL</p>
      </div>
      <div class="about-item">
        <span class="about-icon">👯</span>
        <p><strong>// looking to collab</strong>Backend-heavy projects and real-world SaaS products</p>
      </div>
      <div class="about-item">
        <span class="about-icon">🤝</span>
        <p><strong>// looking for help</strong>System design &amp; distributed systems</p>
      </div>
      <div class="about-item">
        <span class="about-icon">🌱</span>
        <p><strong>// currently learning</strong>Advanced backend architecture &amp; DevOps</p>
      </div>
      <div class="about-item">
        <span class="about-icon">💬</span>
        <p><strong>// ask me about</strong>Python, APIs, Databases, Authentication, REST APIs</p>
      </div>
      <div class="about-item" style="background: linear-gradient(135deg, rgba(124,58,237,0.08), rgba(6,182,212,0.05)); border-color: rgba(124,58,237,0.25);">
        <span class="about-icon">⚡</span>
        <p><strong>// fun fact</strong>I love optimizing queries more than writing UI 😄</p>
      </div>
    </div>
  </div>

  <!-- TECH STACK -->
  <div class="section s2">
    <div class="section-title">💻 Tech Stack</div>
    <div class="tech-grid">
      <!-- Languages -->
      <div class="tech-chip" style="--chip-color:#ED8B00"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/java/java-original.svg" alt="">Java</div>
      <div class="tech-chip" style="--chip-color:#F7DF1E"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="">JavaScript</div>
      <div class="tech-chip" style="--chip-color:#3776AB"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="">Python</div>
      <div class="tech-chip" style="--chip-color:#007ACC"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" alt="">TypeScript</div>
      <div class="tech-chip" style="--chip-color:#5391FE"><img src="https://cdn.simpleicons.org/powershell/5391FE" alt="">PowerShell</div>

      <!-- Cloud / Hosting -->
      <div class="tech-chip" style="--chip-color:#0080FF"><img src="https://cdn.simpleicons.org/digitalocean/0080FF" alt="">DigitalOcean</div>
      <div class="tech-chip" style="--chip-color:#000000"><img src="https://cdn.simpleicons.org/vercel/ffffff" alt="">Vercel</div>
      <div class="tech-chip" style="--chip-color:#46E3B7"><img src="https://cdn.simpleicons.org/render/46E3B7" alt="">Render</div>

      <!-- Frameworks -->
      <div class="tech-chip" style="--chip-color:#009688"><img src="https://cdn.simpleicons.org/fastapi/009688" alt="">FastAPI</div>
      <div class="tech-chip" style="--chip-color:#092E20"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" alt="">Django</div>
      <div class="tech-chip" style="--chip-color:#6DB33F"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/spring/spring-original.svg" alt="">Spring</div>
      <div class="tech-chip" style="--chip-color:#000000"><img src="https://cdn.simpleicons.org/express/ffffff" alt="">Express.js</div>
      <div class="tech-chip" style="--chip-color:#61DAFB"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" alt="">React</div>
      <div class="tech-chip" style="--chip-color:#FF4154"><img src="https://cdn.simpleicons.org/reactquery/FF4154" alt="">React Query</div>
      <div class="tech-chip" style="--chip-color:#CA4245"><img src="https://cdn.simpleicons.org/reactrouter/CA4245" alt="">React Router</div>
      <div class="tech-chip" style="--chip-color:#EC5990"><img src="https://cdn.simpleicons.org/reacthookform/EC5990" alt="">React Hook Form</div>
      <div class="tech-chip" style="--chip-color:#764ABC"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redux/redux-original.svg" alt="">Redux</div>
      <div class="tech-chip" style="--chip-color:#CC6699"><img src="https://cdn.simpleicons.org/sass/CC6699" alt="">SASS</div>
      <div class="tech-chip" style="--chip-color:#38B2AC"><img src="https://cdn.simpleicons.org/tailwindcss/38B2AC" alt="">TailwindCSS</div>
      <div class="tech-chip" style="--chip-color:#646CFF"><img src="https://cdn.simpleicons.org/vite/646CFF" alt="">Vite</div>
      <div class="tech-chip" style="--chip-color:#000000"><img src="https://cdn.simpleicons.org/socketdotio/ffffff" alt="">Socket.io</div>
      <div class="tech-chip" style="--chip-color:#B41717"><img src="https://cdn.simpleicons.org/jsonwebtokens/ffffff" alt="">JWT</div>
      <div class="tech-chip" style="--chip-color:#B41717"><img src="https://cdn.simpleicons.org/jinja/B41717" alt="">Jinja</div>

      <!-- Servers -->
      <div class="tech-chip" style="--chip-color:#F8DC75"><img src="https://cdn.simpleicons.org/apachetomcat/F8DC75" alt="">Apache Tomcat</div>
      <div class="tech-chip" style="--chip-color:#298729"><img src="https://cdn.simpleicons.org/gunicorn/298729" alt="">Gunicorn</div>
      <div class="tech-chip" style="--chip-color:#009639"><img src="https://cdn.simpleicons.org/nginx/009639" alt="">Nginx</div>
      <div class="tech-chip" style="--chip-color:#C71A36"><img src="https://cdn.simpleicons.org/apachemaven/C71A36" alt="">Apache Maven</div>

      <!-- Databases -->
      <div class="tech-chip" style="--chip-color:#47A248"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mongodb/mongodb-original.svg" alt="">MongoDB</div>
      <div class="tech-chip" style="--chip-color:#4479A1"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/mysql/mysql-original.svg" alt="">MySQL</div>
      <div class="tech-chip" style="--chip-color:#336791"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/postgresql/postgresql-original.svg" alt="">PostgreSQL</div>
      <div class="tech-chip" style="--chip-color:#DD0031"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/redis/redis-original.svg" alt="">Redis</div>
      <div class="tech-chip" style="--chip-color:#003B57"><img src="https://cdn.simpleicons.org/sqlite/003B57" alt="">SQLite</div>
      <div class="tech-chip" style="--chip-color:#59666C"><img src="https://cdn.simpleicons.org/hibernate/59666C" alt="">Hibernate</div>

      <!-- Tools & DevOps -->
      <div class="tech-chip" style="--chip-color:#F05033"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" alt="">Git</div>
      <div class="tech-chip" style="--chip-color:#181717"><img src="https://cdn.simpleicons.org/github/ffffff" alt="">GitHub</div>
      <div class="tech-chip" style="--chip-color:#0db7ed"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/docker/docker-original.svg" alt="">Docker</div>
      <div class="tech-chip" style="--chip-color:#F24E1E"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/figma/figma-original.svg" alt="">Figma</div>
      <div class="tech-chip" style="--chip-color:#FF6C37"><img src="https://cdn.simpleicons.org/postman/FF6C37" alt="">Postman</div>
      <div class="tech-chip" style="--chip-color:#85EA2D"><img src="https://cdn.simpleicons.org/swagger/85EA2D" alt="">Swagger</div>
      <div class="tech-chip" style="--chip-color:#4B3263"><img src="https://cdn.simpleicons.org/eslint/4B3263" alt="">ESLint</div>
      <div class="tech-chip" style="--chip-color:#F7B93E"><img src="https://cdn.simpleicons.org/prettier/F7B93E" alt="">Prettier</div>
      <div class="tech-chip" style="--chip-color:#049fd9"><img src="https://cdn.simpleicons.org/cisco/049fd9" alt="">Cisco</div>
      <div class="tech-chip" style="--chip-color:#CB3837"><img src="https://cdn.simpleicons.org/npm/CB3837" alt="">NPM</div>
      <div class="tech-chip" style="--chip-color:#6DA55F"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/nodejs/nodejs-original.svg" alt="">Node.js</div>

      <!-- Data / ML -->
      <div class="tech-chip" style="--chip-color:#150458"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" alt="">Pandas</div>
      <div class="tech-chip" style="--chip-color:#F7931E"><img src="https://cdn.simpleicons.org/scikitlearn/F7931E" alt="">scikit-learn</div>
    </div>
  </div>

  <!-- GITHUB STATS -->
  <div class="section s3">
    <div class="section-title">📊 GitHub Stats</div>
    <div class="stats-grid">
      <div class="stats-card">
        <img src="https://github-readme-stats.vercel.app/api?username=AdityaCS06&theme=dark&hide_border=true&include_all_commits=false&count_private=false&bg_color=111118&title_color=7c3aed&text_color=94a3b8&icon_color=06b6d4" alt="GitHub Stats">
      </div>
      <div class="stats-card">
        <img src="https://nirzak-streak-stats.vercel.app/?user=AdityaCS06&theme=dark&hide_border=true&background=111118&stroke=7c3aed&ring=7c3aed&fire=06b6d4&currStreakLabel=06b6d4&sideLabels=94a3b8&sideNums=e2e8f0&currStreakNum=e2e8f0&dates=64748b" alt="Streak Stats">
      </div>
      <div class="stats-card full">
        <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=AdityaCS06&theme=dark&hide_border=true&include_all_commits=false&count_private=false&layout=compact&bg_color=111118&title_color=7c3aed&text_color=94a3b8" alt="Top Languages">
      </div>
    </div>
  </div>

  <!-- TROPHIES -->
  <div class="section s4">
    <div class="section-title">🏆 GitHub Trophies</div>
    <div class="trophies-card">
      <img src="https://github-profile-trophy.vercel.app/?username=AdityaCS06&theme=radical&no-frame=true&no-bg=true&margin-w=4&column=7" alt="Trophies">
    </div>
  </div>

  <!-- FOOTER -->
  <div class="footer s5">
    <img src="https://visitcount.itsvg.in/api?id=AdityaCS06&icon=0&color=6" alt="Visitor Count">
    <span>· Crafted with ❤️ ·</span>
    <span style="color:var(--accent)">@AdityaCS06</span>
  </div>

</div>
</body>
</html>

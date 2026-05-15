import sys

html_content = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Muhasaba - Forge your soul</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700&family=Chivo:wght@700;800&family=Geist:wght@600&display=swap" rel="stylesheet">
  <style>
    :root {
      /* Palette */
      --bg-base: #111318;
      --bg-surface: #111318;
      --border: #282a2f;
      --on-surface: #e2e2e9;
      --muted: #99907e;
      --muted-dark: #6e6e77;

      /* Accent Colors */
      --primary: #e6c364;   /* Spiritual Gold */
      --secondary: #4ae183; /* Physical Emerald */
      --tertiary: #a5c9ff;  /* Mental Blue */
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    body {
      background-color: var(--bg-base);
      color: var(--on-surface);
      font-family: 'Cairo', sans-serif;
      line-height: 1.6;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      -webkit-font-smoothing: antialiased;
    }

    .container {
      width: 100%;
      max-width: 1140px;
      margin: 0 auto;
      padding: 0 40px;
    }

    /* HEADER */
    header {
      padding: 24px 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 24px;
    }

    .logo {
      font-family: 'Chivo', sans-serif;
      font-weight: 800;
      font-size: 28px;
      color: var(--primary);
      direction: ltr; /* English logo */
    }

    .btn-join {
      background-color: var(--primary);
      color: #0b0c10;
      font-family: 'Cairo', sans-serif;
      font-weight: 700;
      font-size: 15px;
      padding: 8px 36px;
      border-radius: 4px;
      border: none;
      cursor: pointer;
      transition: opacity 0.2s;
    }
    .btn-join:hover { opacity: 0.9; }

    /* CARDS SECTION */
    .pillars {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 24px;
      padding: 24px 0 80px 0;
    }

    .card {
      background-color: var(--bg-surface);
      border: 1px solid var(--border);
      border-radius: 8px;
      padding: 40px 32px 32px 32px;
      display: flex;
      flex-direction: column;
      text-align: right;
      position: relative;
      min-height: 320px;
    }

    .card.spiritual { border-top: 3px solid var(--primary); }
    .card.physical  { border-top: 3px solid var(--secondary); }
    .card.mental    { border-top: 3px solid var(--tertiary); }

    .card-icon-wrapper {
      width: 48px;
      height: 48px;
      background-color: #1e1f25; 
      border-radius: 6px;
      display: flex;
      align-items: center;
      justify-content: center;
      margin-bottom: 32px;
      align-self: flex-start; /* right side */
    }

    .card svg { width: 22px; height: 22px; }
    .card.spiritual svg { stroke: var(--primary); fill: none; }
    .card.physical svg { stroke: var(--secondary); fill: none; }
    .card.mental svg { stroke: var(--tertiary); fill: none; }

    .card-content { flex-grow: 1; display: flex; flex-direction: column; }

    .card h2 {
      font-size: 26px;
      font-weight: 700;
      margin-bottom: 16px;
      color: #fff;
    }

    .card p {
      color: #d0c5b2; /* on-surface-variant */
      font-size: 14px;
      line-height: 1.8;
    }

    .card-footer {
      display: flex;
      align-items: center;
      gap: 8px;
      width: 100%;
      justify-content: flex-start;
      margin-top: 40px;
      font-weight: 600;
      font-size: 15px;
    }

    /* Override slightly different svg uses fill */
    .card-footer svg { width: 18px; height: 18px; }

    .card.spiritual .card-footer { color: var(--primary); }
    .card.physical .card-footer { color: var(--secondary); }
    .card.mental .card-footer { color: var(--tertiary); }

    /* COMING SOON */
    .coming-soon {
      padding: 60px 0 100px 0;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .badge {
      display: inline-block;
      border: 1px solid var(--border);
      color: #99907e;
      font-family: 'Geist', monospace;
      font-weight: 600;
      font-size: 11px;
      letter-spacing: 0.1em;
      padding: 6px 16px;
      border-radius: 20px;
      margin-bottom: 24px;
    }

    .coming-soon h1 {
      font-size: 44px;
      font-weight: 700;
      margin-bottom: 20px;
      color: #fff;
      direction: rtl; 
    }

    .coming-soon h1 span { font-family: 'Chivo', sans-serif; }
    
    .coming-soon p {
      color: #e2e2e9;
      font-size: 18px;
      font-style: italic;
    }

    /* FOOTER */
    footer {
      margin-top: auto;
      border-top: 1px solid var(--border);
      padding: 40px 0;
      background-color: #0c0e13; /* slightly darker floor */
    }

    .footer-inner {
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .footer-left {
      color: #e2e2e9;
      font-size: 14px;
      direction: ltr;
      font-family: 'Geist', sans-serif;
    }

    .footer-center {
      display: flex;
      gap: 32px;
      direction: ltr;
    }

    .footer-center a {
      color: #e2e2e9;
      text-decoration: none;
      font-family: 'Geist', sans-serif;
      font-size: 13px;
      font-weight: 700;
      opacity: 0.9;
    }

    .footer-center a:hover { color: #fff; }

    .footer-right { direction: ltr; text-align: right; }
    .footer-right .f-logo {
      font-family: 'Chivo', sans-serif;
      font-weight: 800;
      font-size: 26px;
      color: var(--primary);
    }
    .footer-right p {
      font-family: 'Geist', sans-serif;
      color: #e2e2e9;
      font-size: 14px;
      margin-top: 8px;
    }

    @media (max-width: 900px) {
      .pillars { grid-template-columns: 1fr; padding-bottom: 40px;}
      .footer-inner {
        flex-direction: column-reverse;
        gap: 32px;
        text-align: center;
      }
      .footer-right { text-align: center; }
      .footer-center { flex-wrap: wrap; justify-content: center; }
    }
  </style>
</head>
<body>

  <header class="container">
    <button class="btn-join">انضم</button>
    <div class="logo">MUHASABA</div>
  </header>

  <main class="container">
    <section class="pillars">
      <!-- Spiritual Card -->
      <div class="card spiritual">
        <div class="card-icon-wrapper">
          <svg viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <!-- Something like a square shape or abstract icon, in the image it looks like a subtle solid box. Let's use a subtle path -->
            <path d="M4 4h16v16H4z" opacity="0.1" fill="currentColor"/>
          </svg>
        </div>
        <div class="card-content">
          <h2>الجانب الروحي</h2>
          <p>تتبع صلواتك، أذكارك، ووردك القرآني بيقظة تامة.<br>اجعل التقوى هي الوقود الأساسي لكل يوم.</p>
        </div>
        <div class="card-footer">
          <svg viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <!-- Badge Check -->
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke="currentColor"/>
            <path d="M9 12l2 2 4-4" stroke="currentColor"/>
          </svg>
          انضباط روحي
        </div>
      </div>

      <!-- Physical Card -->
      <div class="card physical">
        <div class="card-icon-wrapper">
          <svg viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <!-- Dumbbell -->
            <path d="M6 5v14M18 5v14M3 8h6M3 16h6M15 8h6M15 16h6M9 12h6" stroke="currentColor"/>
          </svg>
        </div>
        <div class="card-content">
          <h2>الجانب البدني</h2>
          <p>جسدك أمانة. تتبع تمارين القوة، الحركة، والنظام<br>الغذائي لبناء قوة تخدم رسالتك.</p>
        </div>
        <div class="card-footer">
          <svg viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M13 10V3L4 14h7v7l9-11h-7z" stroke="currentColor"/>
          </svg>
          قوة بدنية
        </div>
      </div>

      <!-- Mental Card -->
      <div class="card mental">
        <div class="card-icon-wrapper">
          <svg viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <!-- A subtle placeholder -->
            <rect x="4" y="4" width="16" height="16" rx="2" stroke="currentColor" opacity="0.3"/>
          </svg>
        </div>
        <div class="card-content">
          <h2>الجانب الذهني</h2>
          <p>إتقان التركيز والعمل العميق. صمم روتينك الذهني<br>لزيادة الإنتاجية والتحصيل المعرفي.</p>
        </div>
        <div class="card-footer">
          <svg viewBox="0 0 24 24" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <!-- lightbulb idea -->
            <path d="M9 18h6M10 22h4M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9A5 5 0 1118.072 12c0 2.21-1.393 4.103-3.072 5.072H9z" stroke="currentColor"/>
          </svg>
          صفاء ذهني
        </div>
      </div>
    </section>

    <section class="coming-soon">
      <div class="badge">COMING SOON</div>
      <h1>قريباً على <span>Android</span> و <span>iOS</span></h1>
      <p>"أكثر من مجرد تطبيق، إنه أسلوب حياة."</p>
    </section>
  </main>

  <footer>
    <div class="container footer-inner">
      <div class="footer-left">
        .MUHASABA 2024 &copy;
      </div>
      <div class="footer-center">
        <a href="#">Privacy</a>
        <a href="#">Mental</a>
        <a href="#">Physical</a>
        <a href="#">Spiritual</a>
      </div>
      <div class="footer-right">
        <div class="f-logo">MUHASABA</div>
        <p>.Forge your soul</p>
      </div>
    </div>
  </footer>
</body>
</html>
"""

with open('muhasaba.html', 'w') as f:
    f.write(html_content)


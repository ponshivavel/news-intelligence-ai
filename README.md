<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AI News Brain</title>

<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@400;500;700&family=DM+Mono&display=swap" rel="stylesheet">

<style>

*{
margin:0;
padding:0;
box-sizing:border-box;
}

body{

background:#0a0a0f;
color:white;
font-family:'DM Sans',sans-serif;
line-height:1.7;

}

header{

padding:80px 30px;
text-align:center;
background:linear-gradient(135deg,#111,#1a1a25);

}

header h1{

font-family:'Playfair Display',serif;
font-size:60px;
color:#c8a96e;

}

header p{

margin-top:20px;
font-size:22px;
color:#ddd;

}

section{

max-width:1200px;
margin:auto;
padding:60px 30px;

}

h2{

font-family:'Playfair Display',serif;
font-size:38px;
color:#c8a96e;
margin-bottom:25px;

}

.card{

background:#16161f;
padding:25px;
border-radius:12px;
margin:20px 0;
border-left:5px solid #c8a96e;

}

ul{

padding-left:25px;

}

li{

margin:10px 0;

}

pre{

background:#000;
padding:20px;
overflow:auto;
border-radius:10px;
color:#8fffa3;
font-family:'DM Mono',monospace;

}

table{

width:100%;
border-collapse:collapse;
margin-top:20px;

}

table th{

background:#c8a96e;
color:black;
padding:15px;

}

table td{

border:1px solid #333;
padding:14px;

}

footer{

text-align:center;
padding:40px;
background:#111;

}

.button{

display:inline-block;
margin-top:25px;
padding:15px 35px;
background:#c8a96e;
color:black;
font-weight:bold;
text-decoration:none;
border-radius:8px;

}

.button:hover{

background:#d9bb7c;

}

.code-title{

color:#c8a96e;
margin:20px 0 10px;

}

</style>

</head>
<body>

<header>

<h1>🧠 AI News Brain</h1>

<p>AI-Powered Financial News Intelligence System</p>

<p>Transform static market news into interactive, decision-driven intelligence.</p>

<a href="#start" class="button">Get Started</a>

</header>

<section>

<h2>🚀 What is AI News Brain?</h2>

<div class="card">

<p>

AI News Brain is a Full Stack Web Application that transforms financial news into intelligent market insights.

Instead of reading lengthy articles, users receive:

</p>

<ul>

<li>📄 Executive AI Briefing</li>

<li>📈 Interactive Market Timeline</li>

<li>💬 AI Financial Chat Assistant</li>

</ul>

</div>

</section>

<section id="start">

<h2>⚡ Quick Start</h2>

<pre>
cd your-project-folder

pip install fastapi uvicorn

python -m uvicorn main:app --reload

Open index.html
</pre>

</section>

<section>

<h2>📂 Folder Structure</h2>

<pre>
project/

│

├── main.py

├── index.html

├── app.js

│

└── agents/

      ├── __init__.py

      ├── data_agent.py

      ├── summary_agent.py

      ├── timeline_agent.py

      └── chat_agent.py
</pre>

</section>

<section>

<h2>🏗 System Architecture</h2>

<div class="card">

<pre>

Browser

↓

FastAPI Backend

↓

Agent Layer

↓

News Data

</pre>

</div>

</section>

<section>

<h2>🔗 REST API</h2>

<table>

<tr>

<th>Method</th>

<th>Endpoint</th>

<th>Description</th>

</tr>

<tr>

<td>GET</td>

<td>/news</td>

<td>AI Summary + Articles</td>

</tr>

<tr>

<td>GET</td>

<td>/timeline</td>

<td>Market Timeline</td>

</tr>

<tr>

<td>POST</td>

<td>/chat</td>

<td>AI Chat</td>

</tr>

</table>

</section>

<section>

<h2>🤖 AI Agents</h2>

<div class="card">

<h3>📊 data_agent.py</h3>

<p>Collects financial news from Mock Data or Real API.</p>

</div>

<div class="card">

<h3>📝 summary_agent.py</h3>

<p>Creates Executive Briefings.</p>

</div>

<div class="card">

<h3>📈 timeline_agent.py</h3>

<p>Builds chronological market timeline.</p>

</div>

<div class="card">

<h3>💬 chat_agent.py</h3>

<p>Answers market questions using rule-based NLP.</p>

</div>

</section>

<section>

<h2>🖥 Frontend Features</h2>

<ul>

<li>Luxury Dark Theme</li>

<li>Responsive Layout</li>

<li>Loading Animation</li>

<li>Timeline Panel</li>

<li>Executive Briefing</li>

<li>AI Chat Window</li>

<li>Keyboard Shortcuts</li>

<li>Error Handling</li>

</ul>

</section>

<section>

<h2>🛠 Technology Stack</h2>

<table>

<tr>

<th>Technology</th>

<th>Purpose</th>

</tr>

<tr>

<td>FastAPI</td>

<td>Backend API</td>

</tr>

<tr>

<td>Uvicorn</td>

<td>Server</td>

</tr>

<tr>

<td>HTML CSS JS</td>

<td>Frontend</td>

</tr>

<tr>

<td>Python</td>

<td>AI Agents</td>

</tr>

<tr>

<td>Rule Based NLP</td>

<td>Local AI</td>

</tr>

</table>

</section>

<section>

<h2>🚀 Production Upgrade</h2>

<div class="card">

<ul>

<li>Replace Mock News with NewsAPI</li>

<li>Replace Rule-Based AI with GPT / Claude</li>

<li>Deploy Backend on Railway or Render</li>

<li>Deploy Frontend on Vercel</li>

<li>Add Portfolio Tracking</li>

<li>Add Watchlists</li>

<li>Add Multiple Languages</li>

</ul>

</div>

</section>

<section>

<h2>🗺 Future Roadmap</h2>

<ul>

<li>✅ Real News API</li>

<li>✅ GPT Integration</li>

<li>✅ Portfolio Analytics</li>

<li>✅ Voice Assistant</li>

<li>✅ Regional Languages</li>

<li>✅ Mobile App</li>

</ul>

</section>

<section>

<h2>❗ Troubleshooting</h2>

<table>

<tr>

<th>Error</th>

<th>Solution</th>

</tr>

<tr>

<td>ModuleNotFoundError</td>

<td>Create agents folder and __init__.py</td>

</tr>

<tr>

<td>CORS Error</td>

<td>Backend URL incorrect</td>

</tr>

<tr>

<td>422 Error</td>

<td>Send JSON Body</td>

</tr>

<tr>

<td>uvicorn not found</td>

<td>Use python -m uvicorn</td>

</tr>

</table>

</section>

<footer>

<h2>🧠 AI News Brain</h2>

<p>

Multi-Agent Financial Intelligence Platform

</p>

<p>

FastAPI • Vanilla JS • AI Agents • Zero API Dependency

</p>

<br>

<p>

Built for Hackathons & Portfolio Demonstrations

</p>

</footer>

</body>
</html>

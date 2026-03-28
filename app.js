// AI News Brain Frontend - Calls FastAPI Backend at http://127.0.0.1:8000
const BACKEND_URL = 'http://127.0.0.1:8000';

async function loadNews() {
  const btn = document.getElementById('news-btn');
  const summaryEl = document.getElementById('summary');
  const articlesEl = document.getElementById('articles');
  const statusEl = document.getElementById('news-status');

  btn.disabled = true;
  btn.textContent = 'Loading...';
  statusEl.innerHTML = '<span class="loading-text">Loading...</span>';
  summaryEl.textContent = '';
  articlesEl.innerHTML = '';

  try {
    const response = await fetch(`${BACKEND_URL}/news`);
    const data = await response.json();
    summaryEl.textContent = data.summary;
    data.articles.forEach(article => {
      const card = document.createElement('div');
      card.className = 'article-card';
      card.innerHTML = `<h3>${article.title}</h3><p>${article.content || article.description || article.summary}</p>`;
      articlesEl.appendChild(card);
    });
    statusEl.textContent = `✓ ${data.articles.length} articles · AI summary`;
  } catch (err) {
    summaryEl.textContent = `Error: ${err.message}`;
    console.error(err);
  }

  btn.disabled = false;
  btn.textContent = 'Refresh News';
}

async function loadTimeline() {
  const btn = document.getElementById('timeline-btn');
  const timelineEl = document.getElementById('timeline');
  const statusEl = document.getElementById('timeline-status');

  btn.disabled = true;
  btn.textContent = 'Building...';
  statusEl.innerHTML = '<span class="loading-text">Generating...</span>';
  timelineEl.innerHTML = '';

  try {
    const response = await fetch(`${BACKEND_URL}/timeline`);
    const data = await response.json();
    data.timeline.forEach(item => {
      const card = document.createElement('div');
      card.className = 'timeline-card';
      card.innerHTML = `
        <div class="timeline-dot-col">
          <div class="timeline-dot"></div>
        </div>
        <div class="timeline-content">
          <h3>${item.event || item.title}</h3>
          <p>${item.impact || item.content}</p>
        </div>`;
      timelineEl.appendChild(card);
    });
    statusEl.textContent = `✓ ${data.timeline.length} events`;
  } catch (err) {
    timelineEl.innerHTML = `<p style="color:var(--accent2)">Error: ${err.message}</p>`;
    console.error(err);
  }

  btn.disabled = false;
  btn.textContent = 'Refresh Timeline';
}

async function ask() {
  const questionEl = document.getElementById('question');
  const answerEl = document.getElementById('answer');
  const btn = document.getElementById('ask-btn');

  const query = questionEl.value.trim();
  if (!query) return;

  btn.disabled = true;
  btn.textContent = 'Thinking...';
  answerEl.textContent = 'Analyzing...';
  answerEl.style.display = 'block';

  try {
    const response = await fetch(`${BACKEND_URL}/chat`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({query})
    });
    const data = await response.json();
    answerEl.textContent = data.response;
  } catch (err) {
    answerEl.textContent = `Error: ${err.message}`;
    console.error(err);
  }

  btn.disabled = false;
  btn.innerHTML = 'Send <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>';
  questionEl.value = '';
}

// Auto-load news on page load
window.addEventListener('load', () => loadNews());

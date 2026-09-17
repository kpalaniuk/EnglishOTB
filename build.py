#!/usr/bin/env python3
"""Static site generator for englishoutsidethebox — run `python3 build.py`, output lands in public/.
Needs: beautifulsoup4 + lxml (pip install -r requirements.txt)."""
import json, os, re, shutil, html, datetime
from pathlib import Path
from bs4 import BeautifulSoup, NavigableString

ROOT = Path(__file__).parent
OUT = ROOT / "public"
SRC = ROOT / "source"
SITE = "https://englishotb.vercel.app"
WA = "https://wa.me/message/ATIRTKSRZIVRC1"
YT = "https://www.youtube.com/channel/UCQGEOqPP0IJ8Or502xwEaqg"
IG = "https://www.instagram.com/jenesl760/"
FB = "https://www.facebook.com/JenESL760"
STRIPE_SELF = "https://buy.stripe.com/28o7vfeJ8f97a76004"
STRIPE_11_3MO = "https://buy.stripe.com/5kAbLv7gGf976UU8wF"
STRIPE_11_MO = "https://buy.stripe.com/dR68zjfNce53bba9AK"
STRIPE_NIGHT = "https://buy.stripe.com/28EdR8gNu3z3081exo7kc0l"
THINKIFIC_SELF = "https://jennifer-s-school-c6e7.thinkific.com/enroll/2001740?price_id=2716831"
GROUP_WAIT = "https://www.subscribepage.com/essgroupwaitlist"
LWM_SERIES = "https://www.subscribepage.com/learnwithmeseries"
PODCAST_LIST = "https://www.subscribepage.com/eatp"
PRON_THINKIFIC = "https://jennifer-s-school-c6e7.thinkific.com/courses/pronuncia"

# ---------- icons ----------
ICO = {
 "wa": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.6.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.3a.5.5 0 0 0 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.8 12 12 0 0 0 4.6 4c1.7.7 2.4.8 3.2.7a2.7 2.7 0 0 0 1.8-1.3 2.2 2.2 0 0 0 .2-1.3c-.1-.1-.3-.2-.5-.3Z"/></svg>',
 "play": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>',
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "check": '<svg viewBox="0 0 24 24" fill="none" stroke="#7C8F6E" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7"/></svg>',
 "x": '<svg viewBox="0 0 24 24" fill="none" stroke="#B0A99C" stroke-width="2.6" stroke-linecap="round" aria-hidden="true"><path d="M7 7l10 10M17 7L7 17"/></svg>',
 "ig": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1.2" fill="currentColor" stroke="none"/></svg>',
 "fb": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M14 8h3V4h-3c-2.8 0-4 1.8-4 4.4V11H7v4h3v7h4v-7h3l1-4h-4V8.8c0-.5.3-.8 1-.8Z"/></svg>',
 "yt": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22 8.2a2.7 2.7 0 0 0-1.9-1.9C18.4 6 12 6 12 6s-6.4 0-8.1.3A2.7 2.7 0 0 0 2 8.2 28 28 0 0 0 1.7 12 28 28 0 0 0 2 15.8a2.7 2.7 0 0 0 1.9 1.9C5.6 18 12 18 12 18s6.4 0 8.1-.3a2.7 2.7 0 0 0 1.9-1.9 28 28 0 0 0 .3-3.8 28 28 0 0 0-.3-3.8ZM10 14.7V9.3l4.8 2.7Z"/></svg>',
 "mail": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
 "sunray": '<svg class="sunray" viewBox="0 0 64 64" fill="none" stroke="#2B2A28" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="32" cy="32" r="11" fill="#F5C542"/><path d="M32 6v8M32 50v8M6 32h8M50 32h8M13.6 13.6l5.7 5.7M44.7 44.7l5.7 5.7M13.6 50.4l5.7-5.7M44.7 19.3l5.7-5.7"/></svg>',
 "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
}

NAV = [
 ("/", "Home"),
 ("/about/", "About"),
 ("/englishsuccesssystem/", "English Success System"),
 ("/ingles/", "Inglês com Jennifer"),
 ("/podcast/", "Podcast"),
 ("/blog/", "Blog"),
 ("/resources/", "Resources"),
]

def esc(s): return html.escape(s, quote=True)

def layout(title, body, path, desc="", og_image="/assets/img/og.jpg", body_class="", extra_head=""):
    full = f"{title} · English Outside the Box" if title else "English Outside the Box · Learn English online with Jennifer Nascimento"
    nav = "".join(
        f'<a href="{href}"{" aria-current=\"page\"" if (href == path or (href != "/" and path.startswith(href))) else ""}>{label}</a>'
        for href, label in NAV)
    return f"""<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(full)}</title>
<meta name="description" content="{esc(desc or 'Empowering English confidence for success beyond your English skills. Positive Psychology English coaching with Jennifer Nascimento — The English Success System, podcast, and free lessons.')}">
<link rel="canonical" href="{SITE}{path}">
<meta property="og:title" content="{esc(full)}">
<meta property="og:description" content="{esc(desc or 'Empowering English confidence for success beyond your English skills.')}">
<meta property="og:image" content="{SITE}{og_image}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="English Outside the Box">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:site" content="@jenesl760">
<meta name="theme-color" content="#F5C542">
<link rel="icon" href="/assets/img/favicon.png" sizes="any">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Nunito:ital,wght@0,400;0,700;0,800;1,400;1,700&family=Shantell+Sans:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/css/site.css">
<script>document.documentElement.classList.remove('no-js')</script>
{extra_head}
</head>
<body class="{body_class}">
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
  <div class="wrap site-head__in">
    <a class="brand" href="/" aria-label="English Outside the Box — home"><img src="/assets/img/logo-bold.png" alt="English Outside the Box" width="220" height="126"></a>
    <button class="nav-toggle" aria-expanded="false" aria-controls="nav">{ICO['menu']} Menu</button>
    <nav class="nav" id="nav" aria-label="Main">
      {nav}
      <a class="btn btn--sun btn--sm nav__cta" href="{WA}" target="_blank" rel="noopener">{ICO['wa']} Say hi on WhatsApp</a>
    </nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-foot">
  <div class="wrap">
    <div class="foot-grid">
      <div class="foot-logo">
        <img src="/assets/img/logo-mark-charcoal-900.png" alt="English Outside the Box" width="210" height="126">
        <p><b>Empowering English confidence</b> for success beyond your English skills.</p>
        <div class="social">
          <a href="{FB}" target="_blank" rel="noopener" aria-label="Facebook">{ICO['fb']}</a>
          <a href="{IG}" target="_blank" rel="noopener" aria-label="Instagram">{ICO['ig']}</a>
          <a href="{YT}" target="_blank" rel="noopener" aria-label="YouTube">{ICO['yt']}</a>
          <a href="{WA}" target="_blank" rel="noopener" aria-label="WhatsApp">{ICO['wa']}</a>
        </div>
      </div>
      <div>
        <h3>English goals</h3>
        <p>I specialize in creating personalized learning plans for you to meet your goals!</p>
        <ul>
          <li><a href="/englishsuccesssystem/">The English Success System</a></li>
          <li><a href="/peek-inside-ess/">Join the program</a></li>
          <li><a href="/learnwithme/">Learn with Me series</a></li>
          <li><a href="/studentsuccess/">Student success</a></li>
        </ul>
      </div>
      <div>
        <h3>Have questions?</h3>
        <p>If you have a question, send me a message!</p>
        <ul>
          <li><a href="{WA}" target="_blank" rel="noopener">Send me a message here</a></li>
          <li><a href="/contact/">Contact form</a></li>
          <li><a href="/podcast/">Podcast</a></li>
          <li><a href="/blog/">Blog</a></li>
        </ul>
      </div>
      <div>
        <h3>Fala português?</h3>
        <p>Tenho mais recursos e opções para você.</p>
        <ul>
          <li><a href="/ingles/">Clique aqui para aprender</a></li>
          <li><a href="/pronunciationcourse/">Curso de pronúncia</a></li>
          <li><a href="/night/">Night Connections eBook</a></li>
          <li><a href="/resources/">All resources</a></li>
        </ul>
      </div>
    </div>
    <div class="foot-bottom">
      <span>© {datetime.date.today().year} Jennifer Nascimento · English Outside the Box</span>
      <span><a href="/termsandprivacy/">Legal information · Terms &amp; Privacy</a></span>
    </div>
  </div>
</footer>
<script src="/assets/js/site.js" defer></script>
</body>
</html>"""

def write(path, htmlstr):
    p = OUT / path.strip("/") / "index.html" if path != "/" else OUT / "index.html"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(htmlstr, encoding="utf-8")

def frame(src, alt, cls="", w=None, h=None, caption="", eager=False):
    dims = f' width="{w}" height="{h}"' if w and h else ""
    cap = f"<figcaption>{caption}</figcaption>" if caption else ""
    load = 'loading="eager" fetchpriority="high"' if eager else 'loading="lazy"'
    return f'<figure class="frame {cls}"><img src="{src}" alt="{esc(alt)}"{dims} {load}>{cap}</figure>'

def cta_band(title="Ready to start learning with me?", text="Send me a message on WhatsApp and let’s talk about your English goals.", btn="Message me on WhatsApp", href=WA):
    return f"""<section class="cta-band"><div class="wrap cta-band__in">
  <div><h2>{title}</h2><p>{text}</p></div>
  <a class="btn btn--lg" href="{href}" target="_blank" rel="noopener">{ICO['wa']} {btn}</a>
</div></section>"""

def quote(text, name, place, cls=""):
    return f'<figure class="quote {cls} reveal"><p>{text}</p><figcaption class="quote__tag"><i></i>{name} · {place}</figcaption></figure>'

# ======================================================================
# HOME
# ======================================================================
def page_home():
    body = f"""
<div class="ribbon">New: my <a href="/night/">Night Connections eBook</a><span class="ribbon__more"> — a sweet end-of-day ritual for your littles (or yourself)</span>. <a href="{STRIPE_NIGHT}" target="_blank" rel="noopener">Buy it here →</a></div>
<section class="hero">
  <div class="hero__grid">
    <div class="hero__sun">
      <div class="hero__copy">
        <h1 class="hero__title">Empowering English Confidence</h1>
        <p class="hero__sub">for success beyond your English skills</p>
        <p class="hero__lines">You have <b>BIG dreams</b> for yourself in English. You want to speak <span class="pop">CONFIDENTLY</span>. You want the right English words to flow through <span class="pop">EASY CONVERSATION</span>. You're ready to live your LIFE as comfortably as you do in your native language. And you're ready for that success… <span class="pop">NOW</span>.</p>
        <div class="btn-row">
          <a class="btn" href="{WA}" target="_blank" rel="noopener">{ICO['wa']} Message me on WhatsApp</a>
          <a class="btn btn--ghost" href="/learnwithme/">{ICO['play']} Watch the Learn with Me series</a>
        </div>
      </div>
      <div class="box-scene" aria-hidden="true">
        <img src="/assets/img/ill-emptybox.png" alt="" width="1180" height="865">
        <span class="word">CONFIDENTLY</span>
        <span class="word">EASY CONVERSATION</span>
        <span class="word">NOW!</span>
      </div>
    </div>
    <div class="hero__photo">
      <img class="hero__badge" src="/assets/img/ill-sun.png" alt="" width="1266" height="1262">
      {frame('/assets/img/Jenna-111-scaled.jpg', 'Jennifer Nascimento writing in a journal on a park bench, wearing a mustard sweater', 'frame--tilt', 1400, 933, eager=True)}
    </div>
  </div>
</section>

<section class="night" id="night">
  <div class="wrap night__grid">
    <div class="reveal">
      <h2>My ‘Night Connections’ eBook</h2>
      <p class="lede">A simple and fun way to connect with your littles (or yourself) at the end of the day.</p>
      <p><b>Included in the printable:</b></p>
      <ul class="list-check">
        <li>{ICO['check']} an originally sweet poem to focus on family love and connection</li>
        <li>{ICO['check']} breathwork to calm the nervous system</li>
        <li>{ICO['check']} relaxing coloring</li>
        <li>{ICO['check']} reflective journal or conversation prompts</li>
        <li>{ICO['check']} prompts rooted in positive psychology to boost positive emotions, self-kindness, empathy and wellbeing</li>
      </ul>
      <a class="btn btn--clay" href="{STRIPE_NIGHT}" target="_blank" rel="noopener">Buy the Night Connections eBook {ICO['arrow']}</a>
      <p class="aside">your purchase helps pay for my new prosthetic leg and 3-month cancer scans that I just found out cost an arm…and a leg 😉</p>
    </div>
    <div class="reveal">{frame('/assets/img/nightconnections-2.jpg', 'A page from the Night Connections printable: gratitude, reflection, relaxation prompts', 'frame--tilt-r', 1608, 2000)}</div>
  </div>
</section>

<section class="section section--white">
  <div class="wrap--narrow center">
    <p class="pt-flag">Now back to English Outside the Box's regular scheduled programming ☀️</p>
    <h2 class="section__title reveal">So, what do you do?</h2>
    <p class="lede reveal">You've been studying, but you still haven't reached the level of confidence you want…</p>
    <p class="reveal" style="font-family:var(--display);font-size:var(--step-2);margin:1.5rem 0 .5rem">Is it possible?</p>
    <p class="reveal" style="font-family:var(--display);font-size:var(--step-5);line-height:1;margin:0 0 1.5rem"><span class="mark">YES</span></p>
    <p class="lede reveal">I'm here to radically <b>change the way you think about your English and how you study</b>, to show you:</p>
    <p class="reveal" style="font-family:var(--display);font-size:var(--step-1)">…how your dreams are MORE than your English.<br>…why your confidence is MORE than your skills.</p>
  </div>
</section>

<section class="section section--butter section--line-top" id="jennifer" style="overflow:hidden">
  <div class="wrap grid-2">
    <div class="tada reveal"><img src="/assets/img/jennifer-tada.png" alt="Jennifer in a bright yellow blouse, arms out in a ta-da pose" width="939" height="1040" loading="lazy"></div>
    <div class="reveal">
      <h2>HI! I'm Jennifer Nascimento</h2>
      <p class="lede">I am a certified Positive Psychology English Coach and the founder of the <a href="/englishsuccesssystem/">English Success System</a>.</p>
      <p>I combine this expertise to get my students faster results based on the science and psychology of learning. My methodologies and exercises are <b>more effective and results-driven.</b></p>
      <p>I focus on 3 core components in ‘The English Success System’:</p>
      <a class="btn btn--ghost" href="/about/">More about me {ICO['arrow']}</a>
    </div>
  </div>
</section>

<section class="section section--white">
  <div class="wrap">
    <div class="pillars reveal">
      <div class="pillar pillar--sun"><span class="pillar__num">1</span><h3>Confidence Formula</h3><p>Learn how to unlock your strengths, finetune your focus on your weaknesses, and defeat your speaking fears. This helps you instantly build confidence.</p></div>
      <div class="pillar"><span class="pillar__num">2</span><h3>Goals that Come Alive</h3><p>Identify action-focused goals, build successful habits, and get your personalized Achievement Strategy (a step-by-step roadmap to your success) so you stop wasting time, money, and energy on what you study.</p></div>
      <div class="pillar"><span class="pillar__num">3</span><h3>my ‘Everyday English Method’</h3><p>to 4X or more the amount you think, speak, practice and use English every week to master your mistakes and build confidence.</p></div>
    </div>
  </div>
</section>

<section class="section section--sun section--line-top">
  <div class="wrap grid-2">
    <div class="reveal">
      <h2>The English Success System</h2>
      <p class="lede" style="color:var(--ink)">The English Success System is not just 1:1 Zoom lessons, but <b>a proven system</b> that develops <b>a step-by-step strategy</b> for you to start <b>thinking in English</b> and <b>using English more consistently</b> throughout your everyday life.</p>
      <p>My students 4X (or more!) the amount they're speaking in English, often noticing results in just weeks of working with me.</p>
      <div class="btn-row">
        <a class="btn" href="/englishsuccesssystem/">How the system works {ICO['arrow']}</a>
        <a class="btn btn--white" href="/peek-inside-ess/">See programs &amp; pricing</a>
      </div>
    </div>
    <div class="reveal" style="position:relative">
      {frame('/assets/img/Jenna-339.jpg', 'Jennifer at a café table with a laptop and a “Hello Happy” journal', 'frame--tilt-r', 2000, 1334)}
    </div>
  </div>
</section>

<section class="section section--white section--line-top">
  <div class="wrap grid-2">
    <div class="reveal" style="order:2">
      <h2>Do you want to know more? Watch my ‘Learn with Me’ mini series now</h2>
      <p>In this mini-series, you will learn about the “Hamster Wheel” effect, why you feel stuck, setting goals, and more about my program, methodology, and what you will learn with me. Each video has an actionable step that you can take to start improving now!</p>
      <a class="btn btn--sun" href="/learnwithme/">{ICO['play']} Start with video 1</a>
    </div>
    <div class="reveal" style="order:1"><img class="ill" src="/assets/img/ill-notebook.png" alt="" width="1120" height="873" loading="lazy" style="max-width:420px;margin-inline:auto"></div>
  </div>
</section>

<section class="section section--sage section--line-top">
  <div class="wrap">
    <h2 class="center section__title">What do students say?</h2>
    <div class="quotes">
      {quote("Jennifer, I love you — nobody tells me these things which you told me. You are really the best teacher in my life. I started to believe in myself and do other things.", "Svetlana", "Russia, living in the US", "quote--sun")}
      {quote("I started a conversation this week with a native speaker, and didn't feel the same fear as last week. It's only week 2 of the program. The patterns that Jennifer uses to teach make me understand easily.", "Rafa", "Brazil, living in the US")}
      {quote("This week (week 2) was interesting. I started to think in English! I looked around and explained my situation and environment in English.", "Loretta", "Italy")}
    </div>
    <p class="center" style="margin-top:1.5rem"><a class="btn btn--ghost" href="/studentsuccess/">More student stories {ICO['arrow']}</a></p>
  </div>
</section>

<div class="ticker" aria-hidden="true"><div class="ticker__track">{'<span>☀ Confidence is MORE than your skills</span><span>☀ Dreams are MORE than your English</span><span>☀ Eu falo português também</span><span>☀ Think in English</span>' * 4}</div></div>

{cta_band()}
"""
    return layout("", body, "/", og_image="/assets/img/Jenna-111-scaled.jpg")

# ======================================================================
# ABOUT
# ======================================================================
def page_about():
    body = f"""
<section class="page-hero">
  <div class="wrap page-hero__grid">
    <div>
      <h1>Welcome to English Outside the Box. I am Jennifer!</h1>
      <p class="lede">Are you ready to finally start speaking better English with more confidence? Good! Then you are in the right place.</p>
    </div>
    <div>{frame('/assets/img/IMG_1840.jpg', 'Jennifer in a mustard sweater against a white brick wall', 'frame--tilt-r', 1000, 667)}</div>
  </div>
</section>

<section class="section section--white">
  <div class="wrap grid-2">
    <div class="reveal">
      <h2>Who am I?</h2>
      <p class="lede">I am so much more than an English teacher and entrepreneur.</p>
      <p><b>I am a fellow language learner</b></p>
      <ul><li>eu falo português</li><li>yo hablo un poco de español</li></ul>
      <p><b>I am a world traveler</b></p>
      <ul><li>I studied and lived in Spain</li><li>I worked and lived in Australia</li><li>I worked and lived in Brazil</li><li>I've traveled through Europe, South East Asia, and New Zealand</li></ul>
      <p>I also love cats, the color <span class="mark">[mustard] yellow</span>, the desert and cacti, food, meeting new people, spending time with my friends and family, and of course teaching English!</p>
    </div>
    <div class="reveal">
      <ul class="about-facts">
        <li><img src="/assets/img/ill-globe.png" alt="">Bachelor's degree + TESOL certification</li>
        <li><img src="/assets/img/ill-plane.png" alt="">Teaching since 2007, internationally and in the States</li>
        <li><img src="/assets/img/ill-notebook.png" alt="">Blogging since 2014 · English Outside the Box since 2014</li>
        <li><img src="/assets/img/ill-bubbles.png" alt="">Hundreds of students from over 30 countries!</li>
        <li><img src="/assets/img/ill-cactus.png" alt="">Cats, mustard yellow, the desert and cacti</li>
      </ul>
      <p style="margin-top:1rem">In regards to my education and experience, here we go. I've received my bachelor's degree and TESOL certification, been teaching since 2007 internationally and in the States, blogging since 2014, and operating English Outside the Box since 2014. Plus, I've taught hundreds of students from over 30 countries!</p>
    </div>
  </div>
</section>

<section class="section section--butter section--line-top">
  <div class="wrap grid-2">
    <div class="reveal">{frame('/assets/img/IMG_1876-copy.jpg', 'Jennifer teaching', 'frame--tilt', 1500, 1006)}</div>
    <div class="reveal">
      <h2>What is English Outside the Box?</h2>
      <p class="lede">It is private, online English education.</p>
      <p>English Outside the Box started in 2014 as a blog, because I had a passion to connect with more learners, <i>outside</i> of the classroom I had been teaching in. I wanted the flexibility to be more creative, I wanted to use more engaging material, and I wanted to make more personal connections with my students. These connections are so important to help my learners reach their goals. The blog quickly grew into online lessons and self-study courses because my students wanted more and I was inspired to create something bigger and better.</p>
      <p>When you start learning <b>‘outside the box’</b> you start learning in a new way. That new way is with me. You will experience more passion and dedication than you have before. I promise you this. But, if you don't believe me, <a href="/studentsuccess/">read what my students have to say!</a></p>
    </div>
  </div>
</section>

<section class="section section--white section--line-top">
  <div class="wrap--mid">
    <h2 class="reveal">How can you start learning with me and English Outside the Box?</h2>
    <p class="lede reveal">First, you <a href="{WA}" target="_blank" rel="noopener">send me a message</a> to get started and talk about your English goals!</p>
    <p class="reveal">My <a href="/englishsuccesssystem/">programs</a> always start with a personalized assessment. In this assessment, we'll discover your unique strengths and weaknesses when it comes to communicating in English. We will dive deep into your mindset, goals and habits to make sure you have a strong foundation for not only learning English, but applying English to your life so you can advance in your career. Once we've established a strong foundation, understand your needs, goals, and strengths and weaknesses, I'll create a customized learning plan for you — recommending course options, study resources, and online lessons.</p>
    <p class="reveal">You can also listen to my <a href="/podcast/">podcast</a>, which is currently under renovation 🙂 So check back soon!</p>
    <p class="reveal">If that is not what you're looking for, then <a href="/contact/">send me a message</a>.</p>
  </div>
</section>
{cta_band("Let's talk about your English goals", "Every program starts with a personalized assessment. Message me and we'll find your starting point.")}
"""
    return layout("About", body, "/about/", "Meet Jennifer Nascimento — Positive Psychology English Coach, fellow language learner, world traveler, and founder of English Outside the Box.", "/assets/img/IMG_1840.jpg")

# ======================================================================
# ENGLISH SUCCESS SYSTEM
# ======================================================================
def page_ess():
    body = f"""
<section class="page-hero">
  <div class="wrap page-hero__grid">
    <div>
      <h1>Empowering your English Confidence so that you can reach your BIGGEST dreams and goals using English</h1>
      <p class="pt-flag">Eu falo português também.</p>
      <div class="btn-row" style="margin-top:1rem">
        <a class="btn" href="/peek-inside-ess/">Programs &amp; pricing {ICO['arrow']}</a>
        <a class="btn btn--white" href="{WA}" target="_blank" rel="noopener">{ICO['wa']} Send me a message</a>
      </div>
    </div>
    <div>{frame('/assets/img/Jenna-339.jpg', 'Jennifer at a café table with a laptop', 'frame--tilt-r', 2000, 1334)}</div>
  </div>
</section>

<section class="section section--white">
  <div class="wrap--mid">
    <h2 class="reveal">Hi! I'm Jennifer.</h2>
    <p class="lede reveal">I'm a Positive Psychology English Coach, <b>empowering</b> my students to understand and speak English on a deeper level for more <b>confidence, clarity, and freedom in their everyday life</b>.</p>
    <p class="reveal">After teaching English for over 15 years, <b>and almost 10 online!</b>, I have seen what works, what doesn't, and what is missing in the usual online classes and courses on the internet. I saw English learners struggle with the same problems, have the same patterns of progress, reach plateaus, feel stuck, frustrated, etc…</p>
    <p class="reveal">So, I created the learning system that eliminates these problems and fills the gaps of what is missing!</p>
  </div>
</section>

<section class="section section--butter section--line-top">
  <div class="wrap">
    <h2 class="center section__title reveal">The English Success System</h2>
    <p class="center lede reveal" style="margin-inline:auto">I focus on 3 core components:</p>
    <div class="pillars reveal" style="margin-top:2rem">
      <div class="pillar pillar--sun"><span class="pillar__num">1</span><h3>Confidence Formula</h3><p>Learn how to unlock your strengths, finetune your focus on your weaknesses, and defeat your speaking fears. This helps you instantly build confidence with ‘The Confidence Formula’.</p></div>
      <div class="pillar"><span class="pillar__num">2</span><h3>Goals that Come Alive</h3><p>Identify action-focused goals, build successful habits, and get your personalized Achievement Strategy (a step-by-step roadmap/plan for your success) so you stop wasting time, money, and energy on what you study.</p></div>
      <div class="pillar"><span class="pillar__num">3</span><h3>The ‘Everyday English Method’</h3><p>Speak &amp; use more English — 4X or more the amount you think, speak, practice and use English every week with a variety of practice opportunities to master your mistakes and build confidence.</p></div>
    </div>
    <p class="center" style="margin-top:2rem"><a class="btn" href="/learnwithme/">{ICO['play']} Watch my ‘Learn with Me Series’ to hear more</a></p>
  </div>
</section>

<section class="section section--white section--line-top">
  <div class="wrap grid-2">
    <div class="reveal"><img class="ill" src="/assets/img/ill-globe.png" alt="" width="922" height="1192" loading="lazy" style="max-width:360px;margin-inline:auto"></div>
    <div class="reveal">
      <h2>Let me explain more</h2>
      <p>Before you begin, you must understand that your success is all about your mindset in English. You must learn about the fears holding you back, so you can overcome them and live with English confidence. In <b>Breakthrough Reality</b>, you'll do this while also learning about your strengths &amp; weaknesses, so you know what you need to focus on. <b>My students have instantly built their confidence in this part of my program</b> because of my Positive Psychology + English blend of education.</p>
      <p>Next, by understanding your goals and needs on a deeper level, you are able to understand exactly what you <i>really</i> want and need, so that you can create a step-by-step strategy to achieve them. You will make sure your goals align (match) your study strategy for optimal success. This helps my students save months of work because this is skipped (overlooked) in most language schools, online group courses, and even in most 1:1 classes. <b>This helps you measure, see, and feel your progress faster!</b></p>
      <p>Finally, my “Every Day English method” is an immersion into English, increasing the amount you think, speak, use (read &amp; write) in English to meet goals more effectively, see faster results in progress, and build confidence. This gives you consistent practice, which is truly needed for the freedom you seek in English. <b>My students have 4X (or more) the amount they're speaking English.</b></p>
    </div>
  </div>
</section>

<section class="section section--sage section--line-top">
  <div class="wrap--mid">
    <h2 class="reveal">How does the English Success System work?</h2>
    <p class="lede reveal">There are 3 ways to join the English Success System: <span class="tag">self-study</span> <span class="tag">group</span> <span class="tag">1:1</span></p>
    <p class="reveal">Each option gives you the resources, materials, and practice opportunities to overcome fear, increase confidence, build skills, and finally start living freely in English.</p>
    <p class="reveal">In the <b>self-study program</b>, you'll have instant access to the program and all of its materials. You can watch the trainings and complete the practice exercises on your own schedule, which is perfect for the busy student. You will also have access to the group WhatsApp chat. This program is month-to-month, and you can cancel at any time.</p>
    <p class="reveal">The <b>group and 1:1 program</b> are a 3-month commitment to start, and then month-to-month. We start by identifying your goals, strengths, and weaknesses together through my personalized assessment and trainings. Then, I create the plan you need for success. You'll receive the training materials and resources you need to improve, the exercises to practice, and the support and feedback from me, your teacher. You will get at least 3 different ways to practice and improve your speaking skills — flexibly, with your own schedule, and with feedback and support with me and other students learning in the group program.</p>
    <h3 class="reveal" style="margin-top:2rem">The English Success System includes:</h3>
    <ul class="list-check reveal">
      <li>{ICO['check']}<span>Weekly PDF, audio, and/or video trainings on both soft skills and English skills</span></li>
      <li>{ICO['check']}<span>Daily focused exercises (writing and speaking) with personalized feedback from Jennifer and AI on needed improvement based on your strategy plan <i>(*personalized feedback for group + 1:1 only, self-study only includes AI feedback)</i></span></li>
      <li>{ICO['check']}<span>WhatsApp Chat support for accountability, Q&amp;As, spontaneous speaking, and additional practice throughout the week. <i>(*personalized feedback + support for group + 1:1 only)</i></span></li>
      <li>{ICO['check']}<span>Zoom call(s) <i>(for group + 1:1 only)</i></span></li>
    </ul>
    <p class="reveal">The main difference in the 3 programs is how much 1:1 time, support, feedback, and zoom (class) times you get. The group program includes 2 weekly (group) calls, and the 1:1 program includes 2 weekly (group) calls, (1) 1:1 zoom call with just you &amp; me, personalized feedback on exercises throughout the week, and a 1:1 WhatsApp chat with just you &amp; me.</p>
  </div>
</section>

<section class="section section--sun section--line-top" id="investment">
  <div class="wrap">
    <h2 class="center reveal">Investment</h2>
    <p class="center lede reveal" style="margin-inline:auto;color:var(--ink)">The <b>minimum</b> investment into the English Success System is $97/month for the self-study program and up to $650 for 1:1 support.</p>
    <div class="grid-3 reveal" style="margin-top:2rem">
      <a class="btn btn--white btn--lg" href="{THINKIFIC_SELF}" target="_blank" rel="noopener" style="justify-content:center;white-space:normal;text-align:center">Join the self-study program</a>
      <a class="btn btn--white btn--lg" href="{GROUP_WAIT}" target="_blank" rel="noopener" style="justify-content:center;white-space:normal;text-align:center">Join the wait list for the group program</a>
      <a class="btn btn--lg" href="/peek-inside-ess/" style="justify-content:center;white-space:normal;text-align:center">Join the 1:1 program</a>
    </div>
  </div>
</section>

<section class="section section--white section--line-top">
  <div class="wrap">
    <h2 class="center section__title reveal">What do students of the English Success System say?</h2>
    <div class="quotes">
      {quote("Jennifer, I love you — Nobody tells me these things which you told me. You are really the best teacher in my life. I started to believe in myself and do other things.", "Svetlana", "Russia, living in the US", "quote--sun")}
      {quote("I started a conversation this week with a native speaker, and didn't feel the same fear as last week. It's only week 2 of the program. The patterns that Jennifer uses to teach make me understand easily.", "Rafa", "Brazil, living in the US")}
      {quote("This week (week 2) was interesting. I started to think in English! I looked around and explained my situation and environment in English.", "Loretta", "Italy")}
      {quote("The biggest and greatest thing that you've done to me is that you are very precise in terms of tailoring the needs. You hear my requests and at the same time developing a very unique and specific to me approach to my deficiencies like pronunciation or grammar. You help me with baby steps to develop cognitive links and habits. Exactly my request.", "Pavel", "Russia, living in the US")}
    </div>
  </div>
</section>
{cta_band("Have questions?", "Click here to send me a message on WhatsApp.")}
"""
    return layout("The English Success System", body, "/englishsuccesssystem/", "Not just 1:1 Zoom lessons — a proven system: the Confidence Formula, Goals that Come Alive, and the Everyday English Method. Self-study, group, or 1:1.", "/assets/img/Jenna-339.jpg")

# ======================================================================
# PEEK INSIDE / PRICING
# ======================================================================
def page_peek():
    def plan(title, kind, price, per, items, href, hot=False, flag=""):
        lis = "".join(f'<li class="{"" if ok else "no"}">{ICO["check"] if ok else ICO["x"]}<span>{t}</span></li>' for ok, t in items)
        return f"""<div class="plan {'plan--hot' if hot else ''} reveal">{f'<span class="plan__flag">{flag}</span>' if flag else ''}
  <div class="plan__head"><h3>{title}</h3><p class="plan__kind">{kind}</p></div>
  <div class="plan__price"><b>{price}</b><span>{per}</span></div>
  <ul class="plan__list">{lis}</ul>
  <div class="plan__foot"><a class="btn {'btn--clay' if hot else ''}" href="{href}" target="_blank" rel="noopener">Sign up now {ICO['arrow']}</a></div>
</div>"""
    base = ["Full access to the online classroom and all course materials", "Daily speaking practice with AI feedback", "Daily conversation classes (8am PST Los Angeles)"]
    prem = ["Personalized Strategy Plan &amp; Assessment Review", "4-6 Weekly speaking tasks + personalized feedback from Jennifer", "Weekly Video 1:1 Classes with Jennifer", "WhatsApp check-ins, question &amp; answers, conversations, and practice 5X a week with Jennifer", "Weekly writing practice &amp; feedback with Jennifer"]
    body = f"""
<section class="page-hero page-hero--butter">
  <div class="wrap--mid center">
    <h1>Hello! Thanks for your interest in the English Success System.</h1>
    <p class="lede">I'm excited about the opportunity to work with you! Here is a peek inside the online classroom…</p>
  </div>
</section>
<section class="section section--white">
  <div class="wrap--mid">
    <div class="video reveal"><iframe src="https://www.youtube.com/embed/7DDrJ8caDfo?si=zrXUSkdzPTAqRRNn" title="A peek inside the English Success System online classroom" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
    <p class="reveal" style="margin-top:1.5rem">In this video, you'll see inside the English Success System online classroom. First, I'll give you an overview of the lessons. Then at minute <b>2:47</b>, I will start showing you inside each lesson and showing you what you can expect. At minute <b>6:12</b>, I'll show you the AI platform that will give you unlimited daily speaking practice + a daily live conversation lesson with others. Finally, at minute <b>7:37</b>, I'll tell you how you can access the materials and the different options to study with me (self-study VS 1:1).</p>
  </div>
</section>
<section class="section section--sun section--line-top" id="plans">
  <div class="wrap">
    <h2 class="center reveal">Let's start working together!</h2>
    <div class="plans" style="margin-top:2rem">
      {plan("English Success System", "Self-Study Course (month-to-month)", "$97", "per month", [(True,x) for x in base]+[(False,x) for x in prem], STRIPE_SELF)}
      {plan("English Success System", "1:1 Program (3-month package)", "$600", "per month · billed for a 3-month period", [(True,x) for x in base+prem]+[(True,"Save $50/month with a 3-month package")], STRIPE_11_3MO, True, "most popular")}
      {plan("English Success System", "1:1 Program (month-to-month)", "$650", "per month", [(True,x) for x in base+prem], STRIPE_11_MO)}
    </div>
    <p class="center reveal" style="margin-top:2rem">Prefer to enroll in self-study through the classroom directly? <a href="{THINKIFIC_SELF}" target="_blank" rel="noopener">Enroll via Thinkific</a> · Interested in the group program? <a href="{GROUP_WAIT}" target="_blank" rel="noopener">Join the waitlist</a>.</p>
  </div>
</section>
{cta_band("Do you have a question about which option might be best for you?", "Send me a message on WhatsApp or email me via the contact form on this site.")}
"""
    return layout("Join the English Success System", body, "/peek-inside-ess/", "A peek inside the English Success System online classroom, plus self-study and 1:1 program pricing.", "/assets/img/Jenna-339.jpg")

# ======================================================================
# LEARN WITH ME series
# ======================================================================
LWM = [
 ("/learnwithme/", "Video 1", "Ready to change the way you learn English, and finally understand what is keeping you stuck + how I can help? Let's go!", "Learn about the “hamster wheel” of learning English and why your focus on fluency and skills is hurting your progress and confidence!", "fOeAzd280jQ", "/learnwithme-video2/", "Continue to video 2 here"),
 ("/learnwithme-video2/", "Video 2", "Eliminating Fears &amp; Building Confidence", "Learn how to eliminate fear so that you can instantly build confidence in your English conversations, today!", "qbCw41Ft4Rk", "/learnwithme-video3/", "Continue to video 3 here"),
 ("/learnwithme-video3/", "Video 3", "Your goals NEED to match your strategy", "Learn how to align (match) your English goals and your study strategy to maximize success and stop wasting time, money, and energy.", "n0kmxov4R7g", "/learnwithme-video4/", "Continue to video 4 here"),
 ("/learnwithme-video4/", "Video 4", "The right teacher, the right materials, &amp; multiple ways to practice + improve", "Learn how to stop wasting time, money, and energy when you study English", "K2Jm03p8wXY", "/peek-inside-ess/", "Video 5: A look inside the program"),
]
def page_lwm(i):
    path, label, title, sub, yt, nxt, nxtlabel = LWM[i]
    nav = "".join((f'<span aria-current="page">{l}</span>' if p == path else f'<a href="{p}">{l}</a>') for p, l, *_ in LWM) + '<a href="/peek-inside-ess/">Video 5: inside the program</a>'
    enroll = ""
    if i == 3:
        enroll = f"""<section class="section section--sun section--line-top"><div class="wrap"><h2 class="center">Enroll now</h2>
  <div class="grid-3" style="margin-top:1.5rem">
    <a class="btn btn--white btn--lg" href="{STRIPE_SELF}" target="_blank" rel="noopener" style="justify-content:center;white-space:normal;text-align:center">Join the English Success System self-study program</a>
    <a class="btn btn--white btn--lg" href="{GROUP_WAIT}" target="_blank" rel="noopener" style="justify-content:center;white-space:normal;text-align:center">Join the waitlist for the group program</a>
    <a class="btn btn--lg" href="/peek-inside-ess/" style="justify-content:center;white-space:normal;text-align:center">Join the English Success System 1-1 program</a>
  </div></div></section>"""
    body = f"""
<section class="page-hero page-hero--butter">
  <div class="wrap--mid">
    <p class="pt-flag">Learn with Me Series</p>
    <nav class="series-nav" aria-label="Series">{nav}</nav>
    <h1>{title}</h1>
    <p class="lede">{sub}</p>
  </div>
</section>
<section class="section section--white">
  <div class="wrap--mid">
    <div class="video"><iframe src="https://www.youtube.com/embed/{yt}" title="Learn with Me — {label}" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>
    <p style="margin-top:1.5rem"><a class="btn" href="{nxt}">{nxtlabel} {ICO['arrow']}</a></p>
  </div>
</section>
{enroll}
<section class="section section--sage section--line-top"><div class="wrap--mid center">
  <h2>{'Still have questions?' if i == 3 else 'Ready to start learning with me?'}</h2>
  <div class="btn-row" style="justify-content:center">
    {'' if i == 3 else f'<a class="btn" href="/englishsuccesssystem/">Click here to join The English Success System</a>'}
    <a class="btn btn--ghost" href="{WA}" target="_blank" rel="noopener">{ICO['wa']} Send me a message on WhatsApp to learn a little more</a>
  </div>
</div></section>
"""
    return layout(f"Learn with Me — {label}", body, path, re.sub("<[^>]+>", "", sub))

# ======================================================================
# INGLÊS COM JENNIFER
# ======================================================================
def page_ingles():
    body = f"""
<section class="page-hero" style="overflow:hidden">
  <div class="wrap page-hero__grid">
    <div>
      <h1>inglês com Jennifer</h1>
      <p class="lede">Você quer aprender mais comigo? Sou uma professora de inglês. Eu falo português e posso te ajudar!</p>
      <div class="btn-row"><a class="btn" href="{WA}" target="_blank" rel="noopener">{ICO['wa']} Manda uma mensagem</a></div>
    </div>
    <div class="tada" style="margin-bottom:calc(-1 * clamp(2.5rem, 6vw, 4.5rem))"><img src="/assets/img/jennifer-tada.png" alt="Jennifer" width="939" height="1040"></div>
  </div>
</section>
<section class="section section--white">
  <div class="wrap grid-2">
    <div class="reveal">
      <h2>Curso de pronúncia</h2>
      <p class="lede">Aumente seu nível de fluência: descubra erros comuns de pronúncia em inglês e melhore sua fala.</p>
      <p><b>Pronúncia de inglês para nativos de língua portuguesa</b></p>
      <div class="btn-row">
        <a class="btn btn--sun" href="{PRON_THINKIFIC}" target="_blank" rel="noopener">inscreva-se aqui {ICO['arrow']}</a>
        <a class="btn btn--ghost" href="/pronunciationcourse/">saiba mais sobre o curso</a>
      </div>
    </div>
    <div class="reveal">{frame('/assets/img/eotbpronPort-2.jpg', 'Curso: Pronúncia de inglês para nativos de língua portuguesa', 'frame--tilt-r')}</div>
  </div>
</section>
<section class="section section--butter section--line-top">
  <div class="wrap grid-2">
    <div class="reveal"><img class="ill" src="/assets/img/ill-bubbles.png" alt="" width="1170" height="744" loading="lazy" style="max-width:380px;margin-inline:auto"></div>
    <div class="reveal">
      <h2>English Success System</h2>
      <p class="lede">Posso te ajudar em português se você precisa.</p>
      <p>Você quer mais informação? Manda um email aqui ou uma mensagem no WhatsApp.</p>
      <div class="btn-row">
        <a class="btn" href="/englishsuccesssystem/">Conheça o programa {ICO['arrow']}</a>
        <a class="btn btn--ghost" href="/contact/">{ICO['mail']} Contato</a>
      </div>
    </div>
  </div>
</section>
<section class="section section--white section--line-top"><div class="wrap--narrow center">
  <p class="lede">Obrigada! Vou responder em breve!</p>
  <p class="hand" style="font-size:var(--step-2)">bjs, Jennifer</p>
</div></section>
"""
    return layout("Inglês com Jennifer", body, "/ingles/", "Sou uma professora de inglês. Eu falo português e posso te ajudar! Curso de pronúncia para nativos de língua portuguesa e o English Success System.", "/assets/img/IMG_1840.jpg")

# ======================================================================
# PODCAST (from the live RSS feed — Libsyn embeds on the old site are dead)
# ======================================================================
SPOTIFY = "https://open.spotify.com/show/2ybFzTyOCsqLyEcoY7Uy9k"
APPLE = "https://podcasts.apple.com/us/podcast/english-outside-the-box/id1127501460"
RSS = "https://anchor.fm/s/1000e29cc/podcast/rss"
def load_episodes():
    import xml.etree.ElementTree as ET
    from email.utils import parsedate_to_datetime
    ns = {"itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"}
    ch = ET.parse(SRC / "podcast.rss").getroot().find("channel")
    eps = []
    for it in ch.findall("item"):
        enc = it.find("enclosure")
        d = parsedate_to_datetime(it.findtext("pubDate"))
        desc = it.findtext("description") or ""
        desc = BeautifulSoup(desc, "lxml").get_text(" ", strip=True)
        eps.append({"title": html.unescape(it.findtext("title") or ""), "date": d, "dur": it.findtext("itunes:duration", namespaces=ns) or "", "url": enc.get("url") if enc is not None else "", "desc": desc, "img": (it.find("itunes:image", ns).get("href") if it.find("itunes:image", ns) is not None else "")})
    return eps

def ep_card(e, open_desc=False):
    dur = e["dur"]
    if dur and ":" in dur:
        parts = dur.split(":"); dur = f"{int(parts[0])*60+int(parts[1])} min" if len(parts) == 3 else f"{int(parts[0])} min"
    desc = e["desc"]
    short = desc[:260] + ("…" if len(desc) > 260 else "")
    body = f'<details class="ep__desc"{" open" if open_desc else ""}><summary>About this episode</summary><p>{esc(desc)}</p></details>' if desc else ""
    return f"""<article class="ep reveal">
  <div class="ep__head"><h3>{esc(e['title'])}</h3><p class="ep__meta">{e['date'].strftime('%b %-d, %Y')}{' · ' + dur if dur else ''}</p></div>
  <audio controls preload="none" src="{esc(e['url'])}"></audio>
  {body}
</article>"""

def page_podcast():
    eps = load_episodes()
    s2 = [e for e in eps if e["title"].startswith("S2 ") or e["title"].lower().startswith("season 2")]
    s1 = [e for e in eps if e["date"].year >= 2022 and e not in s2]
    archive = [e for e in eps if e not in s2 and e not in s1]
    def listing(lst, open_first=False):
        return "".join(ep_card(e, open_first and i == 0) for i, e in enumerate(lst))
    body = f"""
<section class="page-hero">
  <div class="wrap page-hero__grid">
    <div>
      <h1>English Outside the Box — the podcast</h1>
      <p class="lede">A Podcast for your success in life in English beyond the language skills — for non-native English speakers looking for more opportunities with confident conversations, fearless living, and success beyond your wildest dreams.</p>
      <div class="btn-row">
        <a class="btn" href="#season2">{ICO['play']} Listen now</a>
        <a class="btn btn--white" href="{SPOTIFY}" target="_blank" rel="noopener">Spotify</a>
        <a class="btn btn--white" href="{APPLE}" target="_blank" rel="noopener">Apple Podcasts</a>
      </div>
    </div>
    <div style="display:flex;justify-content:center"><img src="/assets/img/podcast-.png" alt="English Outside the Box podcast on a phone" width="500" height="500" style="max-width:340px"></div>
  </div>
</section>
<section class="section section--white" id="season2">
  <div class="wrap--mid">
    <div class="eyecatch">{ICO['sunray']}<h2 style="margin:0">Season 2 is here: listen now</h2></div>
    <p style="margin-top:1rem">🚀 Ready to breakthrough success in your English learning journey? Dive deep into your subconscious during this game-changing episode of English Outside the Box. Discover the hidden fears blocking your English success and unlock the secrets to conquer them using the magic (and SCIENCE) of visualization.</p>
    <p>🎧 Tune in now to break free from language anxiety, elevate your learning game, and finally reach the levels of success you've been dreaming of. Don't just listen; take charge of your English destiny!</p>
    <p>The English Success System is open for enrollment: <a href="/peek-inside-ess/">take a peek inside</a>. Send me a message to learn more or get started on <a href="{WA}" target="_blank" rel="noopener">WhatsApp</a>.</p>
    <div class="episodes" style="margin-top:1.5rem">{listing(s2, True)}</div>
    <div class="legacy-callout" style="margin-top:2rem">
      <p style="margin:0"><b>Help me keep English Outside the Box (formerly English Across the Pond) alive and running!</b> A small donation will help me pay for the technology needed and for the time and resources to continue providing episodes. <a href="{WA}" target="_blank" rel="noopener">Message me on WhatsApp</a> to donate.</p>
    </div>
  </div>
</section>
<section class="section section--butter section--line-top" id="season1">
  <div class="wrap--mid">
    <h2>Listen to Season 1 now</h2>
    <div class="episodes">{listing(s1)}</div>
  </div>
</section>
<section class="section section--sun section--line-top">
  <div class="wrap grid-2">
    <div class="stat reveal"><b>131</b><span>Listening countries</span></div>
    <div class="stat reveal"><b>1,165,779</b><span>Total downloads</span></div>
  </div>
</section>
<section class="section section--white section--line-top">
  <div class="wrap grid-2">
    <div class="reveal">{frame('/assets/img/macbook-headphones-and-flower-picjumbo-com.jpg', 'Laptop, headphones and a flower on a desk', 'frame--tilt', 2000, 1334)}</div>
    <div class="reveal">
      <h2>Let's stay connected!</h2>
      <p>Sign up to receive all the latest updates about English Outside the Box podcast.</p>
      <div class="btn-row"><a class="btn btn--sun" href="{PODCAST_LIST}" target="_blank" rel="noopener">Learn even more {ICO['arrow']}</a><a class="btn btn--ghost" href="{WA}" target="_blank" rel="noopener">{ICO['wa']} Send me a message on WhatsApp</a></div>
      <p style="margin-top:1.5rem;color:var(--ink-soft)">Interested in sponsoring the podcast? This is a great way to advertise your product, company or service to a worldwide, professional audience. Click the WhatsApp link above to send me a message and talk details.</p>
    </div>
  </div>
</section>
<section class="section section--sage section--line-top">
  <div class="wrap">
    <div class="pillars reveal">
      <div class="pillar pillar--sun"><h3>Clarity</h3><p>Get unstuck by creating goals that will actually get you where you need to go and understand how you need to get there.</p></div>
      <div class="pillar"><h3>Strengths &amp; Weaknesses</h3><p>Discover your unique strengths and weaknesses to understand your path to success.</p></div>
      <div class="pillar"><h3>Success</h3><p>Learn the system for continued success so that you can keep growing and learning + reach new goals.</p></div>
    </div>
  </div>
</section>
<section class="section section--white section--line-top" id="archive">
  <div class="wrap--mid">
    <h2>The archive: English Across the Pond (2016–2021)</h2>
    <p class="lede">{len(archive)} more episodes from the podcast's first chapter. Also on <a href="{SPOTIFY}" target="_blank" rel="noopener">Spotify</a>, <a href="{APPLE}" target="_blank" rel="noopener">Apple Podcasts</a>, or <a href="{RSS}">RSS</a>.</p>
    <details class="archive"><summary class="btn btn--ghost">Show all {len(archive)} episodes</summary>
    <div class="episodes" style="margin-top:1.5rem">{"".join(ep_card(e) for e in archive)}</div></details>
  </div>
</section>
"""
    return layout("Podcast", body, "/podcast/", "The English Outside the Box podcast — confident conversations, fearless living, and success beyond your wildest dreams. 131 countries, 1.16M downloads.", "/assets/img/podcast-.png")

# ======================================================================
# CONTACT
# ======================================================================
def page_contact():
    body = f"""
<section class="page-hero page-hero--butter">
  <div class="wrap--mid">
    <h1>Contact</h1>
    <p class="lede">If you have a question that wasn't answered on the website, and/or want more details, send me a message!</p>
    <p>*Interested in partnerships, working together, or guest blogging? Use the same form, and choose the right option under “how can I help?”</p>
  </div>
</section>
<section class="section section--white">
  <div class="wrap contact-grid">
    <div class="contact-card contact-card--sun">
      <h3>Fastest: WhatsApp</h3>
      <p>I answer here first. Tell me a little about your English goals and I'll reply soon.</p>
      <a class="btn" href="{WA}" target="_blank" rel="noopener">{ICO['wa']} Send me a message on WhatsApp</a>
    </div>
    <div class="contact-card">
      <h3>Or write me an email</h3>
      <form class="contact-form" action="mailto:jenesl760@englishoutsidethebox.com" method="get" enctype="text/plain" data-mail="jenesl760@englishoutsidethebox.com">
        <div class="field"><label for="c-name">Name *</label><input id="c-name" name="name" required autocomplete="name"></div>
        <div class="field"><label for="c-email">Email *</label><input id="c-email" name="email" type="email" required autocomplete="email"></div>
        <div class="field"><label for="c-help">How can I help? *</label>
          <select id="c-help" name="help" required><option>I want English lessons</option><option>Partnerships</option><option>Guest blogging</option></select></div>
        <div class="field"><label for="c-msg">Message</label><textarea id="c-msg" name="message" rows="5"></textarea></div>
        <button class="btn btn--sun" type="submit">{ICO['mail']} Open my email app</button>
        <p style="font-size:.9rem;color:var(--ink-soft);margin:.8rem 0 0">This opens a pre-filled email in your own email app.</p>
      </form>
    </div>
  </div>
</section>
<section class="section section--sage section--line-top">
  <div class="wrap grid-2">
    <div class="reveal"><img class="ill" src="/assets/img/ill-plane.png" alt="" width="821" height="688" loading="lazy" style="max-width:320px;margin-inline:auto"></div>
    <div class="reveal">
      <h2>Improve your English now and join my resource library!</h2>
      <p>Sign up to get access to my resource library, a place with videos, worksheets, PDFs, and more! Plus I'll send you lessons &amp; other learning resources.</p>
      <a class="btn" href="{LWM_SERIES}" target="_blank" rel="noopener">Click here to sign up! {ICO['arrow']}</a>
    </div>
  </div>
</section>
"""
    return layout("Contact", body, "/contact/", "Send Jennifer a message — WhatsApp or email — about English lessons, partnerships, or guest blogging.")

# ======================================================================
# NIGHT CONNECTIONS
# ======================================================================
def page_night():
    body = f"""
<section class="night" style="border-bottom:0">
  <div class="wrap night__grid">
    <div>
      <h1>My ‘Night Connections’ eBook</h1>
      <p class="lede">A simple and fun way to connect with your littles (or yourself) at the end of the day.</p>
      <p><b>Included in the printable:</b></p>
      <ul class="list-check">
        <li>{ICO['check']} an originally sweet poem to focus on family love and connection</li>
        <li>{ICO['check']} breathwork to calm the nervous system</li>
        <li>{ICO['check']} relaxing coloring</li>
        <li>{ICO['check']} reflective journal or conversation prompts</li>
        <li>{ICO['check']} prompts rooted in positive psychology to boost positive emotions, self-kindness, empathy and wellbeing</li>
      </ul>
      <a class="btn btn--clay btn--lg" href="{STRIPE_NIGHT}" target="_blank" rel="noopener">Buy the Night Connections eBook {ICO['arrow']}</a>
      <p class="aside">your purchase helps pay for my new prosthetic leg and 3-month cancer scans that I just found out cost an arm…and a leg 😉</p>
    </div>
    <div>{frame('/assets/img/nightconnections-2.jpg', 'A page from the Night Connections printable', 'frame--tilt-r', 1608, 2000)}</div>
  </div>
</section>
"""
    return layout("Night Connections eBook", body, "/night/", "A simple and fun printable to connect with your littles (or yourself) at the end of the day: poem, breathwork, coloring, and reflective prompts.", "/assets/img/nightconnections-2.jpg")

# ======================================================================
# STUDENT SUCCESS
# ======================================================================
def page_studentsuccess():
    imgs = "".join(frame(f'/assets/img/{n}', 'Student review', 'reveal') for n in ["Reviews1.png", "Reviews2.png", "Reviews3-1.png", "Reviews4.png", "Reviews5.png"])
    body = f"""
<section class="page-hero page-hero--sage"><div class="wrap--mid"><h1>What do English Outside the Box students have to say?</h1></div></section>
<section class="section section--white"><div class="wrap">
  <div class="quotes">
    {quote("Jennifer is an amazing English Teacher. She has a lovely voice and a wonderful American accent. I strongly recommend all of her online courses…", "Douglas", "Brazil", "quote--sun")}
    {quote("Jennifer, I love you — Nobody tells me these things which you told me. You are really the best teacher in my life. I started to believe in myself and do other things.", "Svetlana", "Russia, living in the US")}
    {quote("I started a conversation this week with a native speaker, and didn't feel the same fear as last week. It's only week 2 of the program.", "Rafa", "Brazil, living in the US")}
    {quote("This week (week 2) was interesting. I started to think in English! I looked around and explained my situation and environment in English.", "Loretta", "Italy")}
    {quote("You are very precise in terms of tailoring the needs. You hear my requests and at the same time developing a very unique and specific to me approach to my deficiencies like pronunciation or grammar. You help me with baby steps to develop cognitive links and habits. Exactly my request.", "Pavel", "Russia, living in the US", "quote--sun")}
    {quote("Not only has my overall English improved and my level of confidence risen, but also my TOEFL speaking and writing scores jumped up to 24 and 25 respectively. With Jennifer and English Outside the Box You Will Win.", "Viktoriya", "Russia")}
  </div>
  <div class="grid-2" style="margin-top:3rem">{imgs}</div>
</div></section>
<section class="section section--sun section--line-top"><div class="wrap--mid center">
  <h2>Are you ready to start learning in a new way with English Outside the Box?</h2>
  <p class="lede" style="margin-inline:auto;color:var(--ink)">I have a variety of courses and fluency training programs to help you and fit your needs. My courses can provide you flexible learning, self-study opportunities, and guided support.</p>
  <div class="btn-row" style="justify-content:center"><a class="btn" href="/englishsuccesssystem/">Learn more about programs and courses {ICO['arrow']}</a><a class="btn btn--white" href="{LWM_SERIES}" target="_blank" rel="noopener">Get weekly video lessons by email</a></div>
</div></section>
"""
    return layout("Student Success", body, "/studentsuccess/", "What English Outside the Box students say about learning with Jennifer.")

# ======================================================================
# RESOURCES index (legacy pages)
# ======================================================================
LEGACY = {
 # slug: (title, blurb, group)
 "learnenglish": ("Learn English", "Self-study e-courses, e-books, guides &amp; private Zoom lessons", "Programs & courses"),
 "courses": ("Online Courses and Monthly Programs", "Featured courses and monthly programs", "Programs & courses"),
 "everydayfluency": ("Everyday English Fluency Program", "A monthly training program to speak every day", "Programs & courses"),
 "pronunciationcourse": ("English Pronunciation for Portuguese Speakers", "Pronúncia de inglês para nativos de língua portuguesa", "Programs & courses"),
 "englishgroupss": ("English Success System Group Program", "The group program", "Programs & courses"),
 "theenglishsuccesssystem1": ("English Success System (original page)", "The first version of the ESS page", "Programs & courses"),
 "fallintoenglishhabits": ("Fall into English Habits — 21 Day Speaking Challenge", "A 21-day challenge", "Programs & courses"),
 "englishsupport": ("Instagram, Email &amp; Google Chat Support", "Support programs", "Programs & courses"),
 "aula": ("English Group Lesson for Portuguese Speakers", "Aula em grupo", "Programs & courses"),
 "happyenglish": ("Happy English", "Happy English", "Programs & courses"),
 "goals": ("Goals", "Goal-setting", "Programs & courses"),
 "skillsreview": ("English Skills Assessment", "Assess your English skills", "Free resources"),
 "grammar": ("Grammar", "Grammar lessons and resources", "Free resources"),
 "phrasalverbs": ("Phrasal Verbs", "Phrasal verb lessons", "Free resources"),
 "fluency-materials": ("Fluency Materials", "Materials to build fluency", "Free resources"),
 "eefguide": ("Everyday English Fluency Guide", "The fluency guide", "Free resources"),
 "youtube": ("YouTube", "Video lessons", "Free resources"),
 "melhorepronuncia": ("Melhore sua pronúncia", "Em português", "Em português"),
 "treinamentor": ("Treinamento R", "Em português", "Em português"),
 "obrigada": ("Obrigada", "Em português", "Em português"),
 "calendar": ("Calendar", "Schedule", "Other pages"),
 "meetup": ("MeetUp", "Meetups", "Other pages"),
 "english-outside-the-box": ("English Outside the Box (original blog page)", "The 2013 intro page", "Other pages"),
 "home": ("Previous home page", "The older home page", "Other pages"),
 "eatp": ("English Across the Pond", "The podcast's former name", "Other pages"),
 "eatpsurvey": ("English Across the Pond survey", "Podcast survey", "Other pages"),
 "signup": ("Sign Up", "Sign up", "Other pages"),
 "yourein": ("You're in!", "Confirmation", "Other pages"),
 "thank-you": ("Thank You", "Confirmation", "Other pages"),
 "ty": ("Thanks for your purchase", "Confirmation", "Other pages"),
 "thanks-and-lets-keep-learning": ("Thanks, and let's keep learning…", "Confirmation", "Other pages"),
 "termsandprivacy": ("Terms &amp; Conditions and Privacy", "Legal information", "Other pages"),
}

def page_resources():
    groups = {}
    for slug, (t, b, g) in LEGACY.items():
        groups.setdefault(g, []).append((slug, t, b))
    secs = ""
    for g in ["Programs & courses", "Free resources", "Em português", "Other pages"]:
        items = "".join(f'<li><a href="/{s}/">{t}<small>{b}</small></a></li>' for s, t, b in groups.get(g, []))
        secs += f'<h2 style="margin-top:2.5rem">{esc(g)}</h2><ul class="resource-list">{items}</ul>'
    body = f"""
<section class="page-hero page-hero--butter"><div class="wrap--mid">
  <h1>Language Learning Resources</h1>
  <p class="lede">Everything from English Outside the Box in one place: programs, free lessons, Portuguese pages, and the podcast.</p>
</div></section>
<section class="section section--white"><div class="wrap">
  <h2>Start here</h2>
  <ul class="resource-list">
    <li><a href="/englishsuccesssystem/">The English Success System<small>Jennifer's flagship program</small></a></li>
    <li><a href="/peek-inside-ess/">Join the program<small>Self-study &amp; 1:1 pricing</small></a></li>
    <li><a href="/learnwithme/">Learn with Me series<small>4 free videos</small></a></li>
    <li><a href="/podcast/">Podcast<small>Two seasons</small></a></li>
    <li><a href="/blog/">Blog<small>270 free lessons since 2013</small></a></li>
    <li><a href="{YT}" target="_blank" rel="noopener">YouTube channel<small>Hundreds of free lessons</small></a></li>
    <li><a href="/ingles/">Inglês com Jennifer<small>Em português</small></a></li>
    <li><a href="/night/">Night Connections eBook<small>For your littles (or yourself)</small></a></li>
  </ul>
  {secs}
</div></section>
"""
    return layout("Resources", body, "/resources/", "All of English Outside the Box's programs, free lessons, and resources in one place.")

# ======================================================================
# LEGACY converter (Beaver Builder → clean HTML)
# ======================================================================
IMG_MAP = {}
def local_img(src):
    if not src: return src
    s = src.replace("https://i0.wp.com/", "https://").split("?")[0]
    s = s.replace("http://", "https://")
    if "englishoutsidethebox.com/wp-content/uploads" in s:
        name = os.path.basename(s)
        base = re.sub(r"-\d+x\d+(\.[a-z]+)$", r"\1", name)
        for cand in (name, base):
            if (ROOT / "assets/img" / cand).exists(): return "/assets/img/" + cand
        if s in IMG_MAP: return IMG_MAP[s]
        # try blog map (hash-prefixed)
        for k, v in IMG_MAP.items():
            if k.split("?")[0] == s: return v
    if src in IMG_MAP: return IMG_MAP[src]
    return src

def fix_links(soup):
    for a in soup.find_all("a", href=True):
        h = a["href"]
        if h.startswith("https://www.englishoutsidethebox.com") or h.startswith("http://www.englishoutsidethebox.com") or h.startswith("https://englishoutsidethebox.com"):
            h = re.sub(r"^https?://(www\.)?englishoutsidethebox\.com", "", h) or "/"
            a["href"] = h
        if a["href"].startswith("http"):
            a["target"] = "_blank"; a["rel"] = "noopener"
    for img in soup.find_all("img"):
        src = img.get("data-src") or img.get("src") or ""
        img["src"] = local_img(src)
        for k in ["srcset", "data-srcset", "sizes", "data-src", "data-lazy-src", "decoding", "class", "style"]:
            if k in img.attrs and k != "class": del img[k]
        if "class" in img.attrs:
            img["class"] = [c for c in img["class"] if c in ("emoji", "alignleft", "alignright", "aligncenter")]
        img["loading"] = "lazy"
        if not img.get("alt"): img["alt"] = ""
    for f in soup.find_all("iframe"):
        for k in list(f.attrs):
            if k not in ("src", "width", "height", "title", "allow", "allowfullscreen", "scrolling"): del f[k]
        if f.get("src", "").startswith("//"): f["src"] = "https:" + f["src"]
        f["loading"] = "lazy"
        if not f.get("title"): f["title"] = "Embedded content"

def inner(el):
    return "".join(str(c) for c in el.contents) if el else ""

def convert_module(mod):
    cls = " ".join(mod.get("class", []))
    t = re.search(r"fl-module-([a-z0-9-]+)", cls)
    t = t.group(1) if t else ""
    if t == "rich-text":
        rt = mod.find(class_="fl-rich-text")
        return inner(rt) if rt else inner(mod)
    if t == "heading":
        h = mod.find(class_="fl-heading")
        if not h: return ""
        txt = h.get_text(" ", strip=True)
        return f"<h2>{esc(txt)}</h2>" if txt else ""
    if t == "button":
        a = mod.find("a")
        if not a: return ""
        txt = a.get_text(" ", strip=True)
        href = a.get("href", "#")
        return f'<p class="legacy-btn"><a class="btn btn--sun" href="{esc(href)}">{esc(txt)}</a></p>' if txt else ""
    if t == "photo":
        img = mod.find("img")
        if not img: return ""
        a = mod.find("a")
        cap = mod.find(class_="fl-photo-caption")
        im = str(img)
        if a and a.get("href") and not a.get("href").endswith((".jpg", ".png", ".jpeg", ".gif")):
            im = f'<a href="{esc(a["href"])}">{im}</a>'
        return f'<figure class="legacy-photo">{im}{f"<figcaption>{esc(cap.get_text(strip=True))}</figcaption>" if cap else ""}</figure>'
    if t == "html":
        h = mod.find(class_="fl-html")
        if not h: return ""
        for s in h.find_all(["script", "style", "form", "noscript"]): s.decompose()
        content = inner(h).strip()
        if not content or len(re.sub(r"<[^>]+>", "", content).strip()) == 0 and "<iframe" not in content and "<img" not in content:
            return ""
        return f'<div class="legacy-embed">{content}</div>' if "<iframe" in content else content
    if t == "separator":
        return "<hr>"
    if t == "subscribe-form":
        h = mod.find(class_="fl-form-field")
        title = mod.find(["h2", "h3", "h4"])
        return f'<div class="legacy-callout"><p><b>Improve your English now with my e-book and video lessons</b> — sign up to receive weekly video lessons sent to your e-mail plus other learning resources.</p><p><a class="btn btn--sun" href="{LWM_SERIES}" target="_blank" rel="noopener">Click here to sign up!</a></p></div>'
    if t == "tabs":
        labels = [l.get_text(" ", strip=True) for l in mod.select(".fl-tabs-label")]
        panels = mod.select(".fl-tabs-panel-content")
        out = '<div class="legacy-tabs">'
        for i, p in enumerate(panels):
            lab = labels[i] if i < len(labels) else f"Tab {i+1}"
            out += f'<details{" open" if i == 0 else ""}><summary>{esc(lab)}</summary><div>{inner(p)}</div></details>'
        return out + "</div>"
    if t == "accordion":
        out = '<div class="legacy-tabs">'
        for item in mod.select(".fl-accordion-item"):
            lab = item.select_one(".fl-accordion-button-label")
            body = item.select_one(".fl-accordion-content")
            out += f'<details><summary>{esc(lab.get_text(" ", strip=True) if lab else "")}</summary><div>{inner(body)}</div></details>'
        return out + "</div>"
    if t == "testimonials":
        out = '<div class="legacy-row">'
        for q in mod.select(".fl-testimonial"):
            out += f'<blockquote class="legacy-quote">{inner(q)}</blockquote>'
        return out + "</div>"
    if t == "pricing-table":
        out = '<div class="legacy-row">'
        for col in mod.select(".fl-pricing-table-column"):
            title = col.select_one(".fl-pricing-table-title")
            price = col.select_one(".fl-pricing-table-price")
            dur = col.select_one(".fl-pricing-table-duration")
            feats = col.select_one(".fl-pricing-table-features")
            btn = col.find("a")
            out += '<div class="legacy-pricing">'
            if title: out += f"<h3>{inner(title)}</h3>"
            if price: out += f'<p class="price">{price.get_text(" ", strip=True)} <small>{dur.get_text(" ", strip=True) if dur else ""}</small></p>'
            if feats: out += str(feats)
            if btn: out += f'<p><a class="btn btn--sun" href="{esc(btn.get("href", "#"))}">{esc(btn.get_text(" ", strip=True))}</a></p>'
            out += "</div>"
        return out + "</div>"
    if t == "cta":
        title = mod.select_one(".fl-cta-title"); text = mod.select_one(".fl-cta-text"); btn = mod.find("a")
        out = '<div class="legacy-callout">'
        if title: out += f"<h3>{inner(title)}</h3>"
        if text: out += inner(text)
        if btn: out += f'<p><a class="btn" href="{esc(btn.get("href", "#"))}">{esc(btn.get_text(" ", strip=True))}</a></p>'
        return out + "</div>"
    if t == "numbers":
        n = mod.select_one(".fl-number-string"); l = mod.select_one(".fl-number-before-text, .fl-number-after-text")
        return f'<div class="legacy-number"><b>{n.get_text(strip=True) if n else ""}</b>{l.get_text(strip=True) if l else ""}</div>'
    if t == "video":
        v = mod.find("iframe") or mod.find("video")
        return f'<div class="legacy-video">{str(v)}</div>' if v else ""
    if t in ("icon", "icon-group"):
        txt = mod.get_text(" ", strip=True)
        return f"<p>{esc(txt)}</p>" if txt else ""
    if t == "content-slider":
        out = ""
        for s in mod.select(".fl-slide-content, .fl-slide-text-content"):
            out += inner(s)
        return out
    if t == "contact-form":
        return f'<div class="legacy-callout"><p>Want to get in touch? <a href="/contact/">Use the contact page</a> or <a href="{WA}" target="_blank" rel="noopener">message me on WhatsApp</a>.</p></div>'
    if t in ("post-grid", "widget"):
        return ""
    return inner(mod)

def convert_legacy(slug):
    src = (SRC / "pages" / f"{slug}.html").read_text(encoding="utf-8", errors="ignore")
    soup = BeautifulSoup(src, "lxml")
    title_el = soup.find("title")
    root = soup.select_one(".fl-builder-content") or soup.select_one(".fl-post-content") or soup.select_one("article")
    parts = []
    if root and root.select(".fl-module"):
        # honor multi-column rows: group modules by column group
        for row in root.select(".fl-row"):
            groups = row.select(".fl-col-group")
            for g in groups:
                cols = [c for c in g.select(":scope > .fl-col")]
                chunks = []
                for c in cols:
                    mods = [m for m in c.select(".fl-module") if not m.find_parent(class_="fl-module") or m.find_parent(class_="fl-module") is None]
                    mods = [m for m in c.find_all(class_="fl-module") if len([p for p in m.parents if "fl-module" in (p.get("class") or [])]) == 0]
                    chunk = "\n".join(convert_module(m) for m in mods)
                    if chunk.strip(): chunks.append(chunk)
                if len(chunks) > 1:
                    parts.append('<div class="legacy-row">' + "".join(f"<div>{c}</div>" for c in chunks) + "</div>")
                elif chunks:
                    parts.append(chunks[0])
    else:
        node = soup.select_one(".fl-post-content") or soup.select_one(".entry-content") or root
        if node:
            for s in node.find_all(["script", "style", "form", "noscript"]): s.decompose()
            parts.append(inner(node))
    body_html = "\n".join(parts)
    # strip WP / BB leftovers
    out = BeautifulSoup(body_html, "lxml")
    for s in out.find_all(["script", "style", "form", "noscript", "ins"]): s.decompose()
    for el in out.select(".adsbygoogle, .sharedaddy, .jp-relatedposts, [id^='div-gpt'], .wp-block-jetpack-related-posts, .comments-area, #comments, .fl-comments"): el.decompose()
    for el in out.find_all(True):
        for k in ["style", "data-animation", "data-animation-delay", "id"]:
            if k in el.attrs and el.name not in ("iframe",): del el[k]
        if "class" in el.attrs:
            keep = [c for c in el["class"] if c.startswith("legacy-") or c in ("btn", "btn--sun", "emoji", "alignleft", "alignright", "aligncenter", "wp-caption", "wp-caption-text")]
            if keep: el["class"] = keep
            else: del el["class"]
    fix_links(out)
    # remove empty paragraphs
    for p in out.find_all(["p", "div", "h2", "h3"]):
        if not p.get_text(strip=True) and not p.find(["img", "iframe", "a", "svg"]):
            p.decompose()
    body = inner(out.body) if out.body else str(out)
    body = re.sub(r"\[contact-form.*?\[/contact-form\]", f'<p><a class="btn btn--sun" href="/contact/">Contact me</a></p>', body, flags=re.S)
    body = re.sub(r"\[[a-z_-]+[^\]]*\]", "", body)  # any leftover shortcodes
    t, blurb, group = LEGACY.get(slug, (title_el.get_text() if title_el else slug, "", ""))
    t_clean = html.unescape(t)
    hero_cls = "page-hero--white" if slug == "termsandprivacy" else "page-hero--butter"
    note = "" if slug == "termsandprivacy" else '<p class="legacy-note">This page is from an earlier chapter of English Outside the Box and is kept here for reference. For current programs, see <a href="/englishsuccesssystem/">The English Success System</a>.</p>'
    page = f"""
<section class="page-hero {hero_cls}"><div class="wrap--mid"><h1>{t}</h1>{f'<p class="lede">{blurb}</p>' if blurb and group != "Other pages" else ""}</div></section>
<section class="section section--white"><div class="wrap--mid">{note}<div class="prose prose--wide">{body}</div></div></section>
"""
    return layout(re.sub("<[^>]+>", "", t_clean), page, f"/{slug}/", re.sub("<[^>]+>", "", html.unescape(blurb)))

# ======================================================================
# BLOG
# ======================================================================
def load_posts():
    ps = []
    for i in (1, 2, 3):
        ps += json.load(open(SRC / f"posts_{i}.json"))
    ps.sort(key=lambda x: x["date"], reverse=True)
    return ps

def post_path(p):
    d = p["date"][:10].split("-")
    return f"/{d[0]}/{d[1]}/{d[2]}/{p['slug']}/"

def post_cats(p):
    terms = p.get("_embedded", {}).get("wp:term", [[]])
    return [(t["name"], t["slug"]) for t in (terms[0] if terms else []) if t.get("taxonomy") == "category"]

def post_featured(p):
    fm = p.get("_embedded", {}).get("wp:featuredmedia")
    if fm and fm[0].get("source_url"):
        return local_img(fm[0]["source_url"])
    return ""

def clean_post_html(raw):
    soup = BeautifulSoup(raw, "lxml")
    for s in soup.find_all(["script", "style", "form", "noscript", "ins"]): s.decompose()
    for el in soup.select(".adsbygoogle, .sharedaddy, .jp-relatedposts, [id^='div-gpt'], .wp-block-jetpack-related-posts, .mailmunch-forms-in-post-middle, .mailmunch-forms-after-post, .ml-form-embed, .mc4wp-form"): el.decompose()
    # affiliate / ad banners
    for a in soup.find_all("a", href=True):
        if "affiliatly" in a["href"] or "amazon-adsystem" in a["href"] or "shareasale" in a["href"]:
            a.decompose()
    for img in soup.find_all("img"):
        src = img.get("src", "")
        if "amazon-adsystem" in src or "cleardot" in src or "affiliatly" in src:
            img.decompose()
    fix_links(soup)
    for el in soup.find_all(True):
        for k in ["style", "id", "width", "height"]:
            if k in el.attrs and el.name not in ("iframe", "img"): del el[k]
        if el.name in ("img",) and "style" in el.attrs: del el["style"]
    for p in soup.find_all("p"):
        if not p.get_text(strip=True) and not p.find(["img", "iframe", "a"]): p.decompose()
    return inner(soup.body) if soup.body else str(soup)

def excerpt(p):
    e = BeautifulSoup(p["excerpt"]["rendered"], "lxml").get_text(" ", strip=True)
    e = re.sub(r"\s*\[?…\]?\s*$", "…", e).replace("[…]", "…").replace("&hellip;", "…")
    return e[:160] + ("…" if len(e) > 160 and not e.endswith("…") else "")

def fmt_date(iso):
    d = datetime.date.fromisoformat(iso[:10])
    return d.strftime("%B %-d, %Y")

def post_card(p):
    fi = post_featured(p)
    img = f'<div class="post-card__img"><img src="{fi}" alt="" loading="lazy"></div>' if fi else '<div class="post-card__img post-card__img--empty"><img src="/assets/img/ill-notebook.png" alt="" loading="lazy"></div>'
    cats = ", ".join(c for c, _ in post_cats(p)[:2])
    return f"""<li class="post-card" data-cats="{esc(' '.join(s for _, s in post_cats(p)))}" data-year="{p['date'][:4]}"><a class="post-card__link" href="{post_path(p)}">{img}
<div class="post-card__body"><div class="post-card__meta">{fmt_date(p['date'])}{' · ' + esc(cats) if cats else ''}</div><h3>{p['title']['rendered']}</h3><p>{esc(excerpt(p))}</p></div></a></li>"""

def page_blog(posts):
    cats = {}
    for p in posts:
        for n, s in post_cats(p): cats[s] = (n, cats.get(s, (n, 0))[1] + 1)
    chips = '<button type="button" data-cat="all" aria-pressed="true">All posts</button>' + "".join(
        f'<button type="button" data-cat="{s}" aria-pressed="false">{n} <span style="opacity:.6">{c}</span></button>' for s, (n, c) in sorted(cats.items(), key=lambda k: -k[1][1]) if s != "uncategorized")
    years = {}
    for p in posts: years.setdefault(p["date"][:4], []).append(p)
    secs = ""
    for y in sorted(years, reverse=True):
        secs += f'<div class="year-block" data-year="{y}"><div class="year-head"><h2>{y}</h2></div><ul class="post-list">{"".join(post_card(p) for p in years[y])}</ul></div>'
    body = f"""
<section class="page-hero page-hero--butter"><div class="wrap">
  <h1>Blog: hundreds of free English lessons</h1>
  <p class="lede">Since 2013 — grammar, vocabulary, idioms, pronunciation, phrasal verbs, and thoughts on learning English in the real world.</p>
</div></section>
<section class="section section--white" style="padding-top:2rem"><div class="wrap">
  <div class="cats" id="cat-filter" role="group" aria-label="Filter by category">{chips}</div>
  <p id="filter-empty" hidden style="margin-top:2rem" class="lede">No posts in this category yet.</p>
  {secs}
</div></section>
"""
    return layout("Blog", body, "/blog/", "Hundreds of free English lessons since 2013: grammar, vocabulary, idioms, pronunciation, phrasal verbs, and more.")

def page_post(p, prev_p, next_p):
    fi = post_featured(p)
    cats = " · ".join(f'<a href="/blog/#{s}">{esc(n)}</a>' for n, s in post_cats(p))
    content = clean_post_html(p["content"]["rendered"])
    def norm(u):
        n = os.path.basename(u).split("?")[0]
        n = re.sub(r"^[0-9a-f]{6}-", "", n)
        return re.sub(r"-\d+x\d+(\.[a-z]+)$", r"\1", n).lower()
    inline = {norm(u) for u in re.findall(r'<img[^>]+src="([^"]+)"', content)}
    feat = f'<div class="post-feat">{frame(fi, "", "", None, None)}</div>' if fi and norm(fi) not in inline else ""
    nav = ""
    if prev_p: nav += f'<a href="{post_path(prev_p)}"><small>← Older</small>{prev_p["title"]["rendered"]}</a>'
    else: nav += "<span></span>"
    if next_p: nav += f'<a href="{post_path(next_p)}"><small>Newer →</small>{next_p["title"]["rendered"]}</a>'
    body = f"""
<article>
<header class="post-head"><div class="wrap--narrow">
  <p class="meta"><a href="/blog/">Blog</a> · {fmt_date(p['date'])}{' · ' + cats if cats else ''}</p>
  <h1>{p['title']['rendered']}</h1>
</div></header>
<div class="wrap--narrow">
  {feat}
  <div class="prose">{content}</div>
  <nav class="post-nav" aria-label="Post navigation">{nav}</nav>
</div>
</article>
{cta_band("Want more than a blog post?", "The English Success System turns lessons like this into everyday confidence. Message me to talk about your goals.")}
"""
    title = BeautifulSoup(p["title"]["rendered"], "lxml").get_text()
    return layout(title, body, post_path(p), excerpt(p), fi or "/assets/img/og.jpg")

# ======================================================================
# MAIN
# ======================================================================
def main():
    global IMG_MAP
    if (SRC / "blog_img_map.json").exists():
        IMG_MAP = json.load(open(SRC / "blog_img_map.json"))
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir()
    shutil.copytree(ROOT / "assets", OUT / "assets", ignore=shutil.ignore_patterns("gen"))
    write("/", page_home())
    write("/about/", page_about())
    write("/englishsuccesssystem/", page_ess())
    write("/peek-inside-ess/", page_peek())
    for i in range(4): write(LWM[i][0], page_lwm(i))
    write("/ingles/", page_ingles())
    write("/podcast/", page_podcast())
    write("/contact/", page_contact())
    write("/night/", page_night())
    write("/studentsuccess/", page_studentsuccess())
    write("/resources/", page_resources())
    for slug in LEGACY:
        write(f"/{slug}/", convert_legacy(slug))
    posts = load_posts()
    write("/blog/", page_blog(posts))
    for i, p in enumerate(posts):
        newer = posts[i - 1] if i > 0 else None
        older = posts[i + 1] if i + 1 < len(posts) else None
        write(post_path(p), page_post(p, older, newer))
    # sitemap + robots
    urls = ["/", "/about/", "/englishsuccesssystem/", "/peek-inside-ess/", "/ingles/", "/podcast/", "/blog/", "/contact/", "/night/", "/studentsuccess/", "/resources/"] + [l[0] for l in LWM] + [f"/{s}/" for s in LEGACY] + [post_path(p) for p in posts]
    (OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + "".join(f"<url><loc>{SITE}{u}</loc></url>" for u in urls) + "</urlset>")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    (OUT / "404.html").write_text(layout("Page not found", f'<section class="section section--white"><div class="wrap--narrow center"><img class="ill" src="/assets/img/ill-box.png" alt="" style="max-width:260px;margin:0 auto 1rem"><h1>Hmm, that page went outside the box.</h1><p class="lede" style="margin-inline:auto">Let\'s get you back to something useful.</p><div class="btn-row" style="justify-content:center"><a class="btn" href="/">Home</a><a class="btn btn--ghost" href="/blog/">Blog</a><a class="btn btn--ghost" href="/resources/">Resources</a></div></div></section>', "/404/"))
    print("built", len(urls), "pages")

if __name__ == "__main__":
    main()

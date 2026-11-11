"""Gera as páginas estáticas do site da Cardiomwenho em public/.

Uso:  python3 scripts/build.py
Sem dependências externas. Os textos estão em scripts/content.py.
"""
import html
import pathlib
from content import (SITE_URL, WA_MAIN, PHONES, ADDRESS, MAPS, AREAS, EXAMS, COURSES, VIDEOS, JOURNEY)

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "public"
E = html.escape

# ------------------------------------------------------------------ ícones
I = {
 "heart": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 27S4 19.5 4 11.5A6.5 6.5 0 0 1 16 8a6.5 6.5 0 0 1 12 3.5C28 19.5 16 27 16 27z"/><path d="M7 15h5l2-4 3 8 2-4h6"/></svg>',
 "lungs": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 4v11m0 0-4 3m4-3 4 3"/><path d="M12 10c-3-1-7 4-7 11 0 3 1 5 3 5 3 0 5-2 5-5v-6"/><path d="M20 10c3-1 7 4 7 11 0 3-1 5-3 5-3 0-5-2-5-5v-6"/></svg>',
 "work": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 16a9 9 0 0 1 18 0"/><path d="M5 16h22v3H5z"/><path d="M14 7v6m4-6v6"/><path d="M10 23c1.5 2 3.5 3 6 3s4.5-1 6-3"/></svg>',
 "wa": '<svg viewBox="0 0 32 32" fill="currentColor" aria-hidden="true"><path d="M16 3a13 13 0 0 0-11.2 19.6L3 29l6.6-1.7A13 13 0 1 0 16 3zm0 23.7c-2 0-4-.6-5.7-1.6l-.4-.2-3.9 1 1-3.8-.3-.4A10.7 10.7 0 1 1 16 26.7zm5.9-8c-.3-.2-1.9-1-2.2-1-.3-.1-.5-.2-.7.2l-1 1.2c-.2.2-.4.3-.7.1a8.8 8.8 0 0 1-4.4-3.8c-.3-.6.3-.5.9-1.7.1-.2 0-.4 0-.6l-1-2.4c-.3-.6-.5-.5-.7-.5h-.6c-.2 0-.6.1-.9.4-.3.4-1.2 1.2-1.2 2.8s1.2 3.2 1.4 3.4c.2.2 2.4 3.6 5.7 5 2.1.9 3 1 4 .8.7-.1 1.9-.8 2.2-1.5.3-.8.3-1.4.2-1.5l-.6-.4z"/></svg>',
 "phone": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
 "pin": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
 "menu": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>',
 "close": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>',
 "check": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7"/></svg>',
 "tick": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7"/></svg>',
 "done": '<svg viewBox="0 0 64 64" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="32" cy="32" r="28" pathLength="180"/><path d="M20 33l8 8 16-17" pathLength="40"/></svg>',
 "shield": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 3l10 4v8c0 7-4.5 11.5-10 14C10.5 26.5 6 22 6 15V7z"/><path d="M11.5 16l3 3 6-6"/></svg>',
 "team": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="16" cy="10" r="4"/><circle cx="7" cy="12" r="3"/><circle cx="25" cy="12" r="3"/><path d="M9 26v-2a7 7 0 0 1 14 0v2M2 25v-1a5 5 0 0 1 6-5M30 25v-1a5 5 0 0 0-6-5"/></svg>',
 "clock": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="16" cy="16" r="12"/><path d="M16 9v7l5 3"/></svg>',
 "building": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M6 28V6h13v22M19 12h7v16M3 28h26"/><path d="M10 10h1m3 0h1m-5 5h1m3 0h1m-5 5h1m3 0h1m8-4h1m-1 5h1"/></svg>',
 "care": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M16 27S4 19.5 4 11.5A6.5 6.5 0 0 1 16 8a6.5 6.5 0 0 1 12 3.5C28 19.5 16 27 16 27z"/></svg>',
 "board": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="5" width="24" height="16" rx="2"/><path d="M10 27l6-6 6 6M9 15l4-4 3 3 5-5"/></svg>',
 "cert": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="5" width="24" height="17" rx="2"/><path d="M9 11h14M9 15h8"/><circle cx="22" cy="22" r="4"/><path d="M20 25.5V30l2-1.5 2 1.5v-4.5"/></svg>',
 "mentor": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="9" r="4"/><path d="M4 27v-3a7 7 0 0 1 11-5.7"/><path d="M18 14h10v9H18z"/><path d="M21 27h4m-2-4v4"/></svg>',
 "book": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 7c4-2 8-2 12 1 4-3 8-3 12-1v18c-4-2-8-2-12 1-4-3-8-3-12-1z"/><path d="M16 8v18"/></svg>',
 "cal": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="4" y="6" width="24" height="22" rx="3"/><path d="M4 12h24M10 3v6M22 3v6M11 19l3 3 6-6"/></svg>',
 "clipboard": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="7" y="5" width="18" height="24" rx="3"/><path d="M12 5V3h8v2M12 13h8M12 18h8M12 23h5"/></svg>',
 "search": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="14" cy="14" r="9"/><path d="M21 21l7 7"/></svg>',
 "file": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M8 3h11l7 7v19H8z"/><path d="M19 3v7h7M12 17h10M12 22h10"/></svg>',
 "arrow": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>',
 "left": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M15 6l-6 6 6 6"/></svg>',
 "right": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg>',
 "play": '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>',
 "warn": '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3l10 18H2z"/><path d="M12 10v5M12 18h.01"/></svg>',
 "door": '<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M7 28V5h14v23M3 28h26M17 16h.01M21 9h4v19"/></svg>',
}

TRACE_D = "M0 44 H300 q12 -10 24 0 H350 l8 6 l12 -42 l14 58 l10 -22 H450 q20 -18 40 0 H760 q12 -10 24 0 H810 l8 6 l12 -42 l14 58 l10 -22 H910 q20 -18 40 0 H1200"
def trace(cls="trace--draw"):
    return (f'<svg class="trace {cls}" viewBox="0 0 1200 72" preserveAspectRatio="none" aria-hidden="true">'
            f'<path class="line" pathLength="1" d="{TRACE_D}"/><path class="pulse" pathLength="1" d="{TRACE_D}"/></svg>')

NAV = [("/exames", "Exames"), ("/guia", "Guia do doente"), ("/empresas", "Empresas"),
       ("/cursos", "Cursos"), ("/mentorias", "Mentorias"), ("/contactos", "Contactos")]

def pic(path, alt, w, h, eager=False, sizes=None, cls="", small=True):
    """Imagem com WebP (e versão 640 px quando existe) e JPEG de reserva."""
    src = f"/assets/img/{path}"
    srcset = f"{src}-640.webp 640w, {src}.webp {w}w" if small else f"{src}.webp"
    s = f' sizes="{sizes}"' if sizes and small else ""
    load = ' fetchpriority="high"' if eager else ' loading="lazy"'
    c = f' class="{cls}"' if cls else ""
    return (f'<picture><source type="image/webp" srcset="{srcset}"{s}>'
            f'<img src="{src}.jpg" alt="{E(alt)}" width="{w}" height="{h}"{load} decoding="async"{c}></picture>')

def page(path, title, desc, body, current=None, og="/assets/img/og.jpg", extra_head=""):
    nav = "".join(f'<a href="{h}"{" aria-current=\"page\"" if h == current else ""}>{t}</a>' for h, t in NAV)
    canon = SITE_URL + ("/" if path == "index" else "/" + path)
    return f'''<!doctype html>
<html lang="pt" data-wa="{WA_MAIN}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="theme-color" content="#0F2D5C">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Cardiomwenho">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{canon}">
<meta property="og:image" content="{SITE_URL}{og}">
<meta property="og:locale" content="pt_AO">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="/assets/img/marca.png">
<link rel="preload" href="/assets/fonts/Poppins-Bold.woff" as="font" type="font/woff" crossorigin>
<link rel="preload" href="/assets/fonts/Poppins-Regular.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="/assets/css/site.css">
<script>document.documentElement.classList.add("js")</script>
{extra_head}
</head>
<body>
<a class="skip" href="#conteudo">Saltar para o conteúdo</a>
<div class="progress" aria-hidden="true"></div>
<div class="topbar"><div class="wrap">
  <span>Atendemos com agendamento, em São Pedro, Huambo</span>
  <a href="#" data-wa="Olá, Cardiomwenho. Gostaria de fazer uma marcação.">{I["wa"]} WhatsApp 951 165 810</a>
</div></div>
<header class="header"><div class="wrap">
  <a class="brand" href="/" aria-label="Cardiomwenho, página inicial">
    <img src="/assets/img/marca.png" alt="" width="50" height="38">
    <span><b>Cardiomwenho</b><small>Saúde Cardiopulmonar e Ocupacional</small></span>
  </a>
  <button class="menu-btn" type="button" aria-controls="nav" aria-expanded="false" aria-label="Abrir menu">{I["menu"]}</button>
  <nav class="nav" id="nav" aria-label="Principal">
    <button class="menu-btn nav-close" type="button" aria-label="Fechar menu">{I["close"]}</button>
    {nav}
    <a class="btn btn--red" href="/marcar">Marcar exame</a>
  </nav>
</div></header>
<div class="scrim" aria-hidden="true"></div>
<main id="conteudo">
{body}
</main>
<footer class="footer"><div class="wrap">
  <div class="about">
    <span class="logo-white"><img src="/assets/img/logo.png" alt="Cardiomwenho" width="140" height="125" loading="lazy"></span>
    <p>Serviços de Saúde Cardiopulmonar e Ocupacional no Huambo, para particulares e empresas.</p>
    <p style="margin-top:10px">Saúde que previne, vida que continua.</p>
  </div>
  <div>
    <h4>Exames</h4>
    <ul>
      <li><a href="/exames?area=cardio">Exames cardíacos</a></li>
      <li><a href="/exames?area=resp">Exames pulmonares</a></li>
      <li><a href="/empresas">Saúde ocupacional</a></li>
      <li><a href="/guia">Guia do doente</a></li>
    </ul>
  </div>
  <div>
    <h4>Pedidos</h4>
    <ul>
      <li><a href="/marcar">Marcar exame</a></li>
      <li><a href="/empresas#pedido">Pedido para empresas</a></li>
      <li><a href="/cursos#inscricao">Inscrição em cursos</a></li>
      <li><a href="/mentorias#pedido">Pedido de mentoria</a></li>
    </ul>
  </div>
  <div>
    <h4>Contactos</h4>
    <ul>
      {"".join(f'<li><a href="tel:+{n}">{p}</a></li>' for p, n in PHONES)}
      <li><a href="{MAPS}" target="_blank" rel="noopener">{ADDRESS}</a></li>
    </ul>
  </div>
  <div class="base">
    <span>© <span data-year>2026</span> Cardiomwenho. Prevenção hoje, mais vida amanhã. <a href="/privacidade">Privacidade</a></span>
    <span>Desenvolvido por <a href="https://healthlink-website.vercel.app" target="_blank" rel="noopener">HealthLink</a></span>
  </div>
</div></footer>
<a class="fab" href="#" data-wa="Olá, Cardiomwenho. Gostaria de mais informações." aria-label="Falar connosco pelo WhatsApp">{I["wa"]}<span>Fale connosco</span></a>
<script src="/assets/js/site.js" defer></script>
</body>
</html>
'''

def phero(crumbs, h1, lead):
    cr = " / ".join([f'<a href="/">Início</a>'] + crumbs)
    return f'''<section class="phero section--paper"><div class="wrap">
  <p class="crumbs" data-reveal>{cr}</p>
  <h1 data-reveal style="--d:.05s">{h1}</h1>
  <p class="lead" data-reveal style="--d:.12s">{lead}</p>
  {trace()}
</div></section>'''

def done_block(what):
    return f'''<div class="done" role="status">
  {I["done"]}
  <h3>O WhatsApp abriu com o seu pedido</h3>
  <p>Toque em <strong>Enviar</strong> no WhatsApp para concluir. {what}</p>
  <div class="actions">
    <a class="btn btn--wa" href="#" data-wa-again target="_blank" rel="noopener">{I["wa"]} Abrir o WhatsApp de novo</a>
    <button class="btn btn--line" type="button" data-form-reset>Fazer outro pedido</button>
  </div>
</div>'''

def consent():
    return '<label class="consent"><input type="checkbox" required name="consent"> <span>Aceito que estes dados sejam enviados à Cardiomwenho pelo WhatsApp para responder ao meu pedido. <a href="/privacidade">Saber mais</a></span></label>'

def f_text(name, label, req=True, kind="text", full=False, ph="", auto="", hint=""):
    r = " required" if req else ""
    opt = "" if req else ' <span class="opt">(opcional)</span>'
    a = f' autocomplete="{auto}"' if auto else ""
    p = f' placeholder="{ph}"' if ph else ""
    im = ' inputmode="tel"' if kind == "tel" else (' inputmode="numeric" min="1"' if kind == "number" else "")
    h = f'<span class="hint" id="h-{name}">{hint}</span>' if hint else ""
    d = f' aria-describedby="h-{name} e-{name}"' if hint else f' aria-describedby="e-{name}"'
    return (f'<div class="field{" field--full" if full else ""}"><label for="f-{name}">{label}{opt}</label>'
            f'<input id="f-{name}" name="{name}" type="{kind}" data-label="{label}"{r}{a}{p}{im}{d}>{h}<span class="err" id="e-{name}"></span></div>')

def f_area(name, label, hint="", ph="", req=False):
    h = f'<span class="hint" id="h-{name}">{hint}</span>' if hint else ""
    opt = "" if req else ' <span class="opt">(opcional)</span>'
    r = " required" if req else ""
    return (f'<div class="field field--full"><label for="f-{name}">{label}{opt}</label>'
            f'<textarea id="f-{name}" name="{name}" data-label="{label}" placeholder="{ph}" aria-describedby="h-{name} e-{name}"{r}></textarea>{h}<span class="err" id="e-{name}"></span></div>')

def f_seg(name, legend, options, req=True, full=False):
    items = "".join(
        f'<label><input type="radio" name="{name}" value="{v}" data-label="{legend}"{" required" if req and i == 0 else ""}><span>{v}</span></label>'
        for i, v in enumerate(options))
    return f'<fieldset class="field{" field--full" if full else ""}"><legend>{legend}</legend><div class="seg">{items}</div><span class="err"></span></fieldset>'

def f_select(name, label, options, req=True, full=False, param=None):
    opts = '<option value="">Escolha</option>' + "".join(f"<option>{o}</option>" for o in options)
    p = f' data-param="{param}"' if param else ""
    return (f'<div class="field{" field--full" if full else ""}"><label for="f-{name}">{label}</label>'
            f'<select id="f-{name}" name="{name}"{" required" if req else ""} data-label="{label}"{p} aria-describedby="e-{name}">{opts}</select><span class="err" id="e-{name}"></span></div>')

def exam_options():
    out = []
    for key in ("cardio", "resp", "ocup"):
        opts = "".join(f'<option value="{x["slug"]}">{x["name"]}</option>' for x in EXAMS if x["area"] == key)
        out.append(f'<optgroup label="{AREAS[key]["name"]}">{opts}</optgroup>')
    return '<option value="">Escolha o exame</option>' + "".join(out) + '<option value="nao-sei">Ainda não sei / preciso de orientação</option>'

def ecard(x, i=0, h=3, reveal=True):
    a = AREAS[x["area"]]
    small = x["img"] != "aptidao"
    w, hh = (1200, 900)
    return (f'<a class="ecard {a["cls"]}" href="/exames/{x["slug"]}" data-area="{x["area"]}"{f' data-reveal style="--d:{min(i, 5) * .06:.2f}s"' if reveal else ""}>'
            f'<div class="ecard__img">{pic("exames/" + x["img"], x["alt"], w, hh, sizes="(max-width: 600px) 92vw, (max-width: 980px) 46vw, 380px", small=small)}'
            f'<span class="ecard__tag">{a["name"]}</span></div>'
            f'<div class="ecard__body"><h{h}>{x["name"]}</h{h}><p>{x["summary"]}</p>'
            f'<span class="ecard__more">Ver detalhes {I["arrow"]}</span></div></a>')

def video_cards():
    return "".join(
        f'''<button type="button" class="vcard" data-reveal style="--d:{i * .08:.2f}s" data-video="/assets/video/{v["src"]}.mp4" data-poster="/assets/video/{v["src"]}.jpg" data-title="{E(v["title"])}" aria-label="Ver vídeo: {E(v["title"])} ({v["dur"]})">
  <img src="/assets/video/{v["src"]}.jpg" alt="" loading="lazy" width="720" height="1280">
  <span class="vcard__play">{I["play"]}</span>
  <span class="vcard__meta"><b>{v["title"]}</b><span>{v["desc"]} {v["dur"]}</span></span>
</button>''' for i, v in enumerate(VIDEOS))

LIGHTBOX = f'''<dialog class="lightbox" id="lightbox" aria-label="Vídeo">
  <button class="close" type="button" aria-label="Fechar vídeo">{I["close"]}</button>
  <figure style="margin:0"><video controls playsinline preload="none"></video><figcaption></figcaption></figure>
</dialog>'''

# ================================================================= INÍCIO
rail_cards = "".join(ecard(x, i, reveal=False) for i, x in enumerate(EXAMS))
journey_tabs = "".join(
    f'<li><button role="tab" id="jt-{s["id"]}" aria-controls="jp-{s["id"]}" aria-selected="false" tabindex="-1"><span class="n">{i + 1}</span>{s["title"]}</button></li>'
    for i, s in enumerate(JOURNEY))
journey_panels = "".join(
    f'''<div class="jpanel" role="tabpanel" id="jp-{s["id"]}" aria-labelledby="jt-{s["id"]}" hidden>
  <div class="jpanel__img"><img src="{s["img"]}" alt="" loading="lazy" width="640" height="480"></div>
  <div class="jpanel__body"><small>Etapa {i + 1} de {len(JOURNEY)}</small><h3>{s["h"]}</h3><p>{s["p"]}</p>
  <div class="actions"><a class="btn btn--red btn--sm" href="{s["cta"][1]}">{s["cta"][0]}</a>{'<button type="button" class="btn btn--line btn--sm" data-journey-next>Etapa seguinte</button>' if i < len(JOURNEY) - 1 else ''}</div></div>
</div>''' for i, s in enumerate(JOURNEY))


# traçado do monitor (repete duas vezes para o deslizamento contínuo)
_beat = "h120 q10 -9 20 0 h18 l6 5 l10 -34 l12 46 l8 -17 h40 q16 -15 32 0 h134"
MONITOR_D = "M0 34 " + " ".join([_beat] * 8)

def index_groups():
    out = []
    for key, label in (("cardio", "Coração"), ("resp", "Pulmões"), ("ocup", "Trabalho")):
        a = AREAS[key]
        rows = "".join(
            f'<li><a href="/exames/{x["slug"]}" data-img="/assets/img/exames/{x["img"]}{"-640" if x["img"] != "aptidao" else ""}.webp">'
            f'<span class="ix__name">{x["name"]}</span><span class="ix__go">{I["arrow"]}</span></a></li>'
            for x in EXAMS if x["area"] == key)
        out.append(f'<div class="ix {a["cls"]}" data-reveal><h3 class="ix__head"><span class="ix__icon">{I[a["icon"]]}</span>{label}<small>{a["name"]}</small></h3><ul>{rows}</ul></div>')
    return "".join(out)

home = f'''
<section class="hero">
  <picture class="hero__bg">
    <source media="(max-width: 700px)" type="image/webp" srcset="/assets/img/hero-mobile.webp">
    <source media="(max-width: 700px)" srcset="/assets/img/hero-mobile.jpg">
    <source type="image/webp" srcset="/assets/img/hero-ergometria-960.webp 960w, /assets/img/hero-ergometria.webp 1600w" sizes="100vw">
    <img src="/assets/img/hero-ergometria.jpg" alt="Equipa da Cardiomwenho a acompanhar um teste de esforço na sala de ergometria" width="1600" height="900" fetchpriority="high" decoding="async">
  </picture>
  <div class="wrap hero__inner">
    <p class="hero__kicker rise" style="--d:.05s">Saúde cardiopulmonar e ocupacional no Huambo</p>
    <h1><span class="ln c-red"><span style="--d:.15s">Cuide do seu coração.</span></span><span class="ln c-blue"><span style="--d:.3s">Respire melhor.</span></span><span class="ln c-green"><span style="--d:.45s">Trabalhe com segurança.</span></span></h1>
    <p class="hero__lead rise" style="--d:.7s">Exames cardíacos, pulmonares e de saúde ocupacional para particulares e empresas. Com agendamento, em São Pedro.</p>
    <div class="actions rise" style="--d:.85s">
      <a class="btn btn--red" href="/marcar">Marcar exame</a>
      <a class="btn btn--ghost" href="/guia">Como funciona</a>
    </div>
  </div>
  <div class="monitor rise" style="--d:1s">
    <div class="monitor__sweep" aria-hidden="true"><svg viewBox="0 0 2400 60" preserveAspectRatio="none"><path d="{MONITOR_D}"/></svg></div>
    <nav class="wrap monitor__links" aria-label="Atalhos">
      <a href="/marcar"><small>Pelo WhatsApp</small>Marcar um exame</a>
      <a href="/guia#preparacao"><small>Antes do exame</small>Como me preparar</a>
      <a href="/empresas"><small>Saúde ocupacional</small>Exames para empresas</a>
      <a href="/cursos"><small>Novas turmas</small>Cursos todos os meses</a>
    </nav>
  </div>
</section>

<section class="section section--paper" id="areas"><div class="wrap index">
  <div class="index__intro" data-reveal="left">
    <h2>O que fazemos</h2>
    <p class="lead">Exames e avaliações completas para o seu bem-estar e qualidade de vida, com equipamentos de última geração e uma equipa médica especializada.</p>
    <p class="index__hint">Escolha um exame para saber para que serve, como se preparar e marcar.</p>
    <div class="actions"><a class="btn btn--navy" href="/exames">Ver todos os exames</a></div>
  </div>
  <div class="index__list" data-preview>
    {index_groups()}
  </div>
  <figure class="preview" aria-hidden="true"><img alt="" src="data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7" width="320" height="240"></figure>
</div></section>

<section class="team">
  {pic("formacao-grupo", "Equipa e formandos da Cardiomwenho numa sessão de formação", 1600, 900, sizes="100vw")}
  <div class="team__cap"><div class="wrap"><p data-reveal>Equipa médica especializada, a atender particulares e empresas no Huambo.</p></div></div>
</section>

<section class="section"><div class="wrap">
  <div class="head" data-reveal><h2>O seu exame, do primeiro contacto ao resultado</h2>
  <p class="lead">Sete etapas. Em cada uma sabe o que fazer a seguir.</p></div>
  <div class="journey" data-journey>
    <ol class="jsteps" role="tablist" aria-label="Etapas da jornada do doente" aria-orientation="vertical" data-reveal="left"><span class="fill" aria-hidden="true"></span>{journey_tabs}</ol>
    <div data-reveal="right">{journey_panels}</div>
  </div>
</div></section>

<section class="section section--navy"><div class="wrap band">
  <div data-reveal="left">
    <h2>Cursos de exames cardíacos e respiratórios</h2>
    <p class="lead">Capacite-se com quem tem experiência e faça a diferença na sua carreira. Formação teórica e prática, com certificado de participação.</p>
    <p class="months-label">Novas turmas todos os meses</p>
    <ul class="months" data-months="6" aria-label="Próximas turmas"></ul>
    <div class="price-line"><strong>20 000 Kz</strong><span>por curso, com valores especiais para quem fizer dois ou três cursos.</span></div>
    <div class="actions"><a class="btn btn--white" href="/cursos">Ver cursos e inscrever-me</a><a class="btn btn--ghost" href="/mentorias">Mentorias académicas</a></div>
  </div>
  <figure data-reveal="zoom" class="band__photo">{pic("ecg-profissional", "Profissional da Cardiomwenho a realizar um eletrocardiograma", 1000, 1250, sizes="(max-width: 880px) 92vw, 480px")}<figcaption>Os cursos decorrem na Cardiomwenho, com os equipamentos usados no dia a dia.</figcaption></figure>
</div></section>

<section class="section"><div class="wrap">
  <div class="head head--row" data-reveal><div><h2>Por dentro da Cardiomwenho</h2>
  <p class="lead">Imagens reais dos nossos exames, publicadas com a autorização das pessoas filmadas.</p></div></div>
  <div class="vgrid">{video_cards()}</div>
</div></section>

<section class="section section--paper"><div class="wrap">
  <div class="head" data-reveal><h2>Visita institucional</h2>
  <p class="lead">Momentos da visita à Cardiomwenho registados pelo Gabinete da Juventude e Desportos do Huambo.</p></div>
  <div class="gallery">
    <figure data-reveal="zoom">{pic("visita/visita-4", "Responsáveis da Cardiomwenho e visitantes à entrada das instalações", 1080, 720, small=False)}</figure>
    <figure data-reveal="zoom" style="--d:.06s">{pic("visita/visita-2", "Visitantes a percorrer as instalações da Cardiomwenho", 1080, 720, small=False)}</figure>
    <figure data-reveal="zoom" style="--d:.12s">{pic("visita/visita-3", "Conversa num gabinete da Cardiomwenho durante a visita", 1080, 720, small=False)}</figure>
    <figure data-reveal="zoom" style="--d:.18s">{pic("visita/visita-1", "Visita à sala de exames da Cardiomwenho", 1080, 720, small=False)}</figure>
    <figure data-reveal="zoom" style="--d:.24s">{pic("exames/espirometria", "Espirometria na Cardiomwenho", 1200, 900, sizes="320px")}</figure>
  </div>
  <p class="gallery-cap">Fotografias da visita: Gabinete da Juventude e Desportos, huambo.gov.ao.</p>
</div></section>

<section class="section"><div class="wrap two">
  <div data-reveal>
    <p class="two__k c-ocup">Para empresas</p>
    <h3>Exames admissionais, periódicos, de retorno ao trabalho e de mudança de função para as suas equipas.</h3>
    <a class="textlink c-ocup" href="/empresas#pedido">Pedir proposta para a empresa</a>
  </div>
  <div data-reveal style="--d:.08s">
    <p class="two__k c-resp">Para estudantes</p>
    <h3>Mentorias académicas para estudantes e recém-formados da área da saúde.</h3>
    <a class="textlink c-resp" href="/mentorias">Pedir mentoria</a>
  </div>
</div></section>

<section class="section section--navy"><div class="wrap contact">
  <div data-reveal="left">
    <h2>A sua saúde é a nossa prioridade.</h2>
    <ul class="phones">{"".join(f'<li><a href="tel:+{n}">{I["phone"]}{p}</a></li>' for p, n in PHONES)}</ul>
    <div class="addr">{I["pin"]}<div>{ADDRESS}<br><a href="{MAPS}" target="_blank" rel="noopener" style="color:#fff">Abrir no Google Maps</a></div></div>
  </div>
  <div data-reveal="right">
    <p class="lead mt-0">Prefere escrever? Envie-nos uma mensagem pelo WhatsApp e respondemos com a disponibilidade.</p>
    <div class="actions"><a class="btn btn--wa" href="#" data-wa="Olá, Cardiomwenho. Gostaria de mais informações.">{I["wa"]} Escrever no WhatsApp</a><a class="btn btn--ghost" href="/marcar">Marcar exame</a></div>
  </div>
</div></section>
{LIGHTBOX}
'''

# ================================================================= EXAMES (lista)
exames = phero(["Exames"], "Exames cardíacos, pulmonares e de saúde ocupacional",
               "Escolha a área e abra cada exame para ver para que serve, como se preparar e o que esperar.") + f'''
<section class="section"><div class="wrap">
  <div class="filters" role="group" aria-label="Filtrar por área" data-reveal>
    <button type="button" data-filter="todos" aria-pressed="true">Todos</button>
    <button type="button" data-filter="cardio" aria-pressed="false">Exames cardíacos</button>
    <button type="button" data-filter="resp" aria-pressed="false">Exames pulmonares</button>
    <button type="button" data-filter="ocup" aria-pressed="false">Saúde ocupacional</button>
  </div>
  <p class="sr-only" id="filter-status" aria-live="polite"></p>
  <div class="exam-grid">{"".join(ecard(x, i, h=2) for i, x in enumerate(EXAMS))}</div>
</div></section>
<section class="section section--mist"><div class="wrap split">
  <figure data-reveal="zoom">{pic("espirometria-equipa", "Profissional da Cardiomwenho a acompanhar uma espirometria", 1000, 1250, sizes="(max-width: 860px) 92vw, 560px")}</figure>
  <div data-reveal="right"><h2>Não sabe que exame precisa?</h2>
  <p class="lead">Na marcação, escolha “Ainda não sei” e a equipa orienta-o pelo WhatsApp.</p>
  <div class="actions"><a class="btn btn--red" href="/marcar?exame=nao-sei">Pedir orientação</a><a class="btn btn--line" href="/guia">Ver o guia do doente</a></div></div>
</div></section>'''

# ================================================================= PÁGINAS DE EXAME
def exam_page(x):
    a = AREAS[x["area"]]
    ocup = x["area"] == "ocup"
    related = [y for y in EXAMS if y["area"] == x["area"] and y["slug"] != x["slug"]][:5]
    cta_href = "/empresas#pedido" if ocup else f"/marcar?exame={x['slug']}"
    cta_txt = "Pedir para a empresa" if ocup else "Marcar este exame"
    small = x["img"] != "aptidao"
    body = f'''<section class="phero section--paper {a["cls"]}"><div class="wrap">
  <p class="crumbs" data-reveal><a href="/">Início</a> / <a href="/exames">Exames</a> / {x["short"]}</p>
  <div class="exam-hero" style="padding-top:0">
    <div>
      <span class="pill" data-reveal>{I[a["icon"]]}{a["name"]}</span>
      <h1 data-reveal style="--d:.05s">{x["name"]}</h1>
      <p class="lead" data-reveal style="--d:.1s">{x["summary"]}</p>
      <div class="actions" data-reveal style="--d:.15s"><a class="btn btn--red" href="{cta_href}">{cta_txt}</a><a class="btn btn--line" href="#preparacao">Como me preparar</a></div>
    </div>
    <div class="exam-hero__img" data-reveal="zoom">{pic("exames/" + x["img"], x["alt"], 1200, 900, eager=True, sizes="(max-width: 860px) 92vw, 560px", small=small)}</div>
  </div>
</div></section>
<section class="section {a["cls"]}"><div class="wrap exam-layout">
  <div>
    <div class="block" data-reveal><h2><span class="ico">{I["search"]}</span>O que é</h2><p>{x["what"]}</p></div>
    <div class="block" data-reveal><h2><span class="ico">{I["file"]}</span>Quando pode ser pedido</h2>
      <ul class="ticks">{"".join(f"<li>{w}</li>" for w in x["when"])}</ul>
      <p>A indicação para o exame é sempre do seu médico ou, nas avaliações ocupacionais, da empresa.</p></div>
    <div class="block" id="preparacao" data-reveal><h2><span class="ico">{I["clipboard"]}</span>Como se preparar</h2>
      <ul class="ticks">{"".join(f"<li>{w}</li>" for w in x["prep"])}</ul>
      <p>Estas orientações são gerais. Na confirmação da marcação, a equipa indica o que se aplica ao seu caso.</p></div>
    <div class="block" data-reveal><h2><span class="ico">{I["door"]}</span>No dia do exame</h2>
      <ul class="ticks">{"".join(f"<li>{w}</li>" for w in x["day"])}</ul></div>
    <div class="block" data-reveal><h2><span class="ico">{I["check"]}</span>Depois do exame</h2><p>{x["after"]}</p></div>
    <div class="alert" data-reveal>{I["warn"]}<p><strong>Em caso de dor no peito forte, falta de ar súbita ou desmaio, não espere pela marcação:</strong> procure de imediato um serviço de urgência.</p></div>
  </div>
  <aside class="exam-aside">
    <div class="aside-card"><h3>{cta_txt}</h3><p>{"Peça uma proposta para os colaboradores da sua empresa." if ocup else "Envie o pedido pelo WhatsApp. A equipa confirma a hora consigo."}</p>
      <a class="btn btn--red" href="{cta_href}">{cta_txt}</a>
      <a class="btn btn--ghost" href="#" data-wa="Olá, Cardiomwenho. Tenho uma dúvida sobre o exame: {x['name']}.">{I["wa"]} Tirar uma dúvida</a></div>
    <div class="aside-links"><h4>Outros exames desta área</h4><ul>{"".join(f'<li><a href="/exames/{y["slug"]}">{y["name"]}</a></li>' for y in related)}</ul></div>
  </aside>
</div></section>'''
    return body

# ================================================================= GUIA DO DOENTE
prep_blocks = "".join(
    f'''<div data-prep="{x["slug"]}" hidden><h3>{x["name"]}</h3><ul class="ticks {AREAS[x["area"]]["cls"]}">{"".join(f"<li>{w}</li>" for w in x["prep"])}</ul>
<a class="textlink" href="/exames/{x["slug"]}">Ver tudo sobre este exame</a></div>''' for x in EXAMS)
prep_opts = "".join(f'<option value="{x["slug"]}">{x["name"]}</option>' for x in EXAMS)
guia = phero(["Guia do doente"], "O seu exame, passo a passo",
             "Tudo o que precisa de saber, do primeiro contacto ao resultado. Siga as etapas ou vá diretamente à que procura.") + f'''
<section class="section"><div class="wrap guide">
  <nav aria-label="Etapas do guia"><ul class="guide-nav">
    {"".join(f'<li><a href="#{s["id"]}">{i + 1}. {s["title"]}</a></li>' for i, s in enumerate(JOURNEY))}
  </ul></nav>
  <div>
    <article class="stage" id="descoberta" data-reveal><div class="stage__n">1</div><div>
      <h2>Descoberta</h2>
      <p class="lead">A Cardiomwenho presta serviços de saúde cardiopulmonar e ocupacional no Huambo, a particulares e a empresas, com equipamentos de última geração e uma equipa médica especializada.</p>
      <div class="actions"><a class="btn btn--line btn--sm" href="/#areas">Conhecer as áreas</a></div></div></article>
    <article class="stage" id="informacao" data-reveal><div class="stage__n">2</div><div>
      <h2>Informação</h2>
      <p class="lead">Cada exame tem uma página própria com o que é, quando pode ser pedido, como se preparar e o que esperar.</p>
      <div class="actions"><a class="btn btn--line btn--sm" href="/exames">Consultar os exames</a></div></div></article>
    <article class="stage" id="escolha" data-reveal><div class="stage__n">3</div><div>
      <h2>Escolha do exame</h2>
      <p class="lead">Se tem um pedido do seu médico ou da empresa, marque o exame indicado. Se não sabe qual é, escolha “Ainda não sei” na marcação e a equipa orienta-o.</p>
      <div class="actions"><a class="btn btn--line btn--sm" href="/marcar?exame=nao-sei">Pedir orientação</a></div></div></article>
    <article class="stage" id="agendamento" data-reveal><div class="stage__n">4</div><div>
      <h2>Agendamento</h2>
      <p class="lead">Preencha o pedido de marcação com o exame, o dia e o período que prefere. O site abre o WhatsApp com a mensagem pronta para o 951 165 810. A marcação fica confirmada quando a equipa responder com a hora.</p>
      <div class="actions"><a class="btn btn--red btn--sm" href="/marcar">Marcar exame</a><a class="btn btn--line btn--sm" href="/contactos">Outros contactos</a></div></div></article>
    <article class="stage" id="preparacao" data-reveal><div class="stage__n">5</div><div>
      <h2>Preparação</h2>
      <p class="lead">Escolha o exame para ver como se preparar.</p>
      <div class="prep-tool"><label for="prep-select">Exame</label>
        <div class="field"><select id="prep-select">{prep_opts}</select></div>
        <div class="prep-out" id="prep-out" aria-live="polite">{prep_blocks}</div></div>
      <p class="note">Orientações gerais. A equipa confirma as indicações para o seu caso na marcação.</p></div></article>
    <article class="stage" id="atendimento" data-reveal><div class="stage__n">6</div><div>
      <h2>Atendimento</h2>
      <ul class="ticks ticks--lg">
        <li>Chegue alguns minutos antes da hora marcada.</li>
        <li>Traga um documento de identificação, o pedido médico ou da empresa e exames anteriores.</li>
        <li>A equipa recebe-o, confirma os seus dados e explica cada passo antes de começar.</li>
        <li>Durante o exame, diga de imediato se sentir algum desconforto.</li>
      </ul>
      <div class="actions"><a class="btn btn--line btn--sm" href="{MAPS}" target="_blank" rel="noopener">Como chegar</a></div></div></article>
    <article class="stage" id="pos-exame" data-reveal><div class="stage__n">7</div><div>
      <h2>Pós-exame</h2>
      <ul class="ticks ticks--lg">
        <li>A equipa indica como e quando recebe o resultado.</li>
        <li>Leve o resultado ao médico que pediu o exame: é ele quem decide os próximos passos.</li>
        <li>Nos exames de Holter e MAPA, volte no dia seguinte para retirar o aparelho.</li>
        <li>Nas avaliações ocupacionais, o resultado é comunicado conforme o combinado com a empresa.</li>
      </ul>
      <div class="actions"><a class="btn btn--wa btn--sm" href="#" data-wa="Olá, Cardiomwenho. Tenho uma dúvida sobre o resultado do meu exame.">{I["wa"]} Perguntar sobre um resultado</a></div></div></article>
    <div class="alert">{I["warn"]}<p><strong>Em caso de dor no peito forte, falta de ar súbita ou desmaio, não espere pela marcação:</strong> procure de imediato um serviço de urgência.</p></div>
  </div>
</div></section>'''

# ================================================================= MARCAR
marcar = phero(["Marcar exame"], "Marcar exame", "Preencha o pedido e envie pelo WhatsApp. A equipa confirma a hora consigo.") + f'''
<section class="section"><div class="wrap split split--top">
  <div class="form-card" data-reveal>
    <h2>Pedido de marcação</h2>
    <p>A marcação só fica confirmada quando a equipa responder no WhatsApp.</p>
    <form class="form" data-wa-form data-intro="Olá, Cardiomwenho. Gostaria de marcar um exame.">
      <div class="field field--full"><label for="f-exame">Exame</label>
        <select id="f-exame" name="exame" required data-label="Exame" data-param="exame" aria-describedby="e-exame">{exam_options()}</select><span class="err" id="e-exame"></span></div>
      {f_text("nome", "Nome completo", auto="name")}
      {f_text("telefone", "Telefone / WhatsApp", kind="tel", auto="tel", ph="9XX XXX XXX")}
      {f_seg("para", "O exame é para", ["Particular", "Empresa"], full=True)}
      {f_text("data", "Dia preferido", kind="date")}
      {f_seg("periodo", "Período preferido", ["Manhã", "Tarde", "Qualquer"])}
      {f_area("obs", "Observações", hint="Por exemplo, disponibilidade ou dúvidas sobre a marcação. Não escreva aqui informação clínica.")}
      {consent()}
      <button class="btn btn--wa btn--block" type="submit">{I["wa"]} Enviar pedido pelo WhatsApp</button>
      <p class="form-note">O pedido é enviado para o WhatsApp 951 165 810.</p>
    </form>
    {done_block("A equipa responde com a hora marcada e as orientações para o exame.")}
  </div>
  <div data-reveal="right">
    <h2>Antes de enviar</h2>
    <div class="faq" style="margin-top:22px">
      <details open><summary>A marcação fica feita quando envio o pedido?</summary><div>Não. O pedido chega à equipa pelo WhatsApp e a marcação fica confirmada quando lhe responderem com o dia e a hora.</div></details>
      <details><summary>Como me preparo para o exame?</summary><div>Cada exame tem orientações próprias. Veja-as no <a href="/guia#preparacao">guia do doente</a> ou na página do exame.</div></details>
      <details><summary>Posso marcar para outra pessoa?</summary><div>Sim. Escreva o nome da pessoa que vai fazer o exame e o contacto onde a equipa pode confirmar.</div></details>
      <details><summary>A minha empresa precisa de exames para vários colaboradores</summary><div>Use o <a href="/empresas#pedido">pedido para empresas</a>, onde pode indicar o número de colaboradores e os tipos de exame.</div></details>
      <details><summary>Onde ficam?</summary><div>{ADDRESS}. <a href="{MAPS}" target="_blank" rel="noopener">Abrir no Google Maps</a>.</div></details>
    </div>
  </div>
</div></section>'''

# ================================================================= EMPRESAS
ocup = [x for x in EXAMS if x["area"] == "ocup"]
ocup_checks = "".join(f'<label><input type="checkbox" name="tipos" value="{x["name"]}" data-label="Exames pretendidos"><span>{x["name"]}</span></label>' for x in ocup[1:])
empresas = phero(["Empresas"], "Saúde ocupacional para a sua empresa",
                 "Avaliações médicas ocupacionais para equipas de qualquer dimensão, com agendamento e atendimento rápido.") + f'''
<section class="section"><div class="wrap">
  <div class="head" data-reveal><h2>Avaliações ao longo do percurso de cada colaborador</h2>
  <p class="lead">Da admissão à mudança de função, com exames cardíacos e pulmonares complementares sempre que necessário.</p></div>
  <div class="exam-grid">{"".join(ecard(x, i) for i, x in enumerate(ocup))}</div>
</div></section>
<section class="section section--mist" id="pedido"><div class="wrap">
  <div class="form-card" style="max-width:880px;margin-inline:auto" data-reveal>
    <h2>Pedir proposta para empresa</h2>
    <p>Diga-nos quantos colaboradores e que exames precisa. A equipa responde pelo WhatsApp com a proposta e as datas.</p>
    <form class="form" data-wa-form data-intro="Olá, Cardiomwenho. Gostaria de pedir uma proposta de saúde ocupacional para a nossa empresa.">
      {f_text("empresa", "Nome da empresa", auto="organization")}
      {f_text("responsavel", "Pessoa de contacto", auto="name")}
      {f_text("tel", "Telefone / WhatsApp", kind="tel", auto="tel", ph="9XX XXX XXX")}
      {f_text("colab", "Número de colaboradores", kind="number")}
      <fieldset class="field field--full"><legend>Exames pretendidos <span class="opt">(pode escolher vários)</span></legend><div class="seg">{ocup_checks}</div></fieldset>
      {f_area("msg", "Mais informações", hint="Por exemplo, prazos, setor de atividade ou exames complementares.")}
      {consent()}
      <button class="btn btn--wa btn--block" type="submit">{I["wa"]} Enviar pedido pelo WhatsApp</button>
    </form>
    {done_block("A equipa responde com a proposta.")}
  </div>
</div></section>'''

# ================================================================= CURSOS
course_boxes = "".join(
    f'''<label class="course {AREAS[a]["cls"]}"><input type="checkbox" name="curso" value="{v}" data-label="Cursos" data-param="curso">
<span class="box"><small>{"Exames cardíacos" if a == "cardio" else "Exames respiratórios"}</small><b>{n}</b><span>{d}</span></span>
<span class="check">{I["check"]}</span></label>''' for v, a, n, d in COURSES)
cursos = phero(["Cursos"], "Cursos de exames cardíacos e respiratórios",
               "Capacite-se com quem tem experiência e faça a diferença na sua carreira. Há novas turmas todos os meses.") + f'''
<section class="section--tight"><div class="wrap">
  <ul class="perks">
    <li data-reveal>{I["board"]}<span>Formação teórica e prática</span></li>
    <li data-reveal style="--d:.06s">{I["cert"]}<span>Certificado de participação</span></li>
    <li data-reveal style="--d:.12s">{I["team"]}<span>Instrutores com experiência</span></li>
    <li data-reveal style="--d:.18s">{I["book"]}<span>Material de apoio</span></li>
  </ul>
</div></section>
<section class="section section--mist" id="inscricao"><div class="wrap split split--top">
  <div class="form-card" data-reveal>
    <h2>Inscrição</h2>
    <p>Escolha os cursos. O valor é calculado automaticamente, segundo a tabela da Cardiomwenho.</p>
    <form class="form" data-wa-form data-extra="cursos" data-intro="Olá, Cardiomwenho. Gostaria de me inscrever nos cursos de exames.">
      <fieldset class="field field--full" data-course-picker data-min-one><legend>Cursos</legend>
        <div class="course-grid">{course_boxes}</div><span class="err" id="course-err" role="alert"></span>
        <div class="summary" aria-live="polite"><b id="course-total">Escolha um ou mais cursos</b><small id="course-sub">O valor aparece aqui.</small></div>
      </fieldset>
      {f_text("nome", "Nome completo", auto="name")}
      {f_text("telefone", "Telefone / WhatsApp", kind="tel", auto="tel", ph="9XX XXX XXX")}
      <div class="field"><label for="f-mes">Mês pretendido</label><select id="f-mes" name="mes" required data-label="Mês pretendido" data-months-select="6" aria-describedby="e-mes"><option value="">Escolha</option></select><span class="err" id="e-mes"></span></div>
      {f_select("perfil", "Situação", ["Estudante da área da saúde", "Profissional de saúde", "Outra"])}
      {f_text("inst", "Instituição ou local de trabalho", req=False, auto="organization")}
      {consent()}
      <button class="btn btn--wa btn--block" type="submit">{I["wa"]} Enviar inscrição pelo WhatsApp</button>
    </form>
    {done_block("A equipa confirma a vaga, as datas e o pagamento.")}
  </div>
  <div data-reveal="right">
    <h2>Preço</h2>
    <ul class="tiers">
      <li data-n="1"><b>20 mil</b><span>por curso</span></li>
      <li data-n="2"><b>15 mil</b><span>por curso, para quem fizer dois cursos</span></li>
      <li data-n="3"><b>10 mil</b><span>por curso, para quem fizer três cursos</span></li>
    </ul>
    <p class="note">Valores em kwanzas. Para quatro ou mais cursos, a equipa confirma o valor.</p>
    <h3 style="margin-top:30px">Novas turmas todos os meses</h3>
    <ul class="months months--light" data-months="6" aria-label="Próximas turmas"></ul>
    <figure class="poster" style="margin-top:28px">{pic("cartaz-cursos", "Cartaz dos cursos de exames cardíacos e respiratórios da Cardiomwenho", 1024, 1536, small=False)}<figcaption>Cartaz da turma de novembro. Há novas turmas todos os meses.</figcaption></figure>
  </div>
</div></section>
<section class="section"><div class="wrap split">
  <figure data-reveal="zoom">{pic("formacao-grupo", "Participantes e formadores numa sessão de formação da Cardiomwenho", 1600, 900, sizes="(max-width: 860px) 92vw, 560px")}</figure>
  <div data-reveal="right"><h2>Aprenda onde os exames acontecem</h2>
  <p class="lead">Os cursos decorrem na Cardiomwenho, no Huambo, com os mesmos equipamentos usados no dia a dia da clínica.</p>
  <div class="actions"><a class="btn btn--red" href="#inscricao">Inscrever-me</a><a class="btn btn--line" href="/mentorias">Preciso de mentoria</a></div></div>
</div></section>'''

# ================================================================= MENTORIAS
mentorias = phero(["Mentorias"], "Mentorias académicas",
                  "Acompanhamento para estudantes e recém-formados da área da saúde, com quem trabalha todos os dias com exames cardiopulmonares.") + f'''
<section class="section"><div class="wrap split">
  <div data-reveal="left">
    <h2>Em que podemos ajudar</h2>
    <p class="lead">Conte-nos o que precisa. A equipa avalia o pedido e responde com a proposta de acompanhamento.</p>
    <ul class="ticks ticks--lg c-resp" style="margin-top:26px">
      <li>Trabalho de fim de curso ou monografia na área cardiopulmonar</li>
      <li>Preparação para a defesa</li>
      <li>Interpretação de exames cardíacos</li>
      <li>Interpretação de espirometria</li>
      <li>Preparação para estágio ou para o primeiro emprego</li>
    </ul>
  </div>
  <figure data-reveal="zoom">{pic("espirometria-equipa", "Profissional da Cardiomwenho a acompanhar um exame de espirometria", 1000, 1250, sizes="(max-width: 860px) 92vw, 560px")}</figure>
</div></section>
<section class="section section--mist" id="pedido"><div class="wrap">
  <div class="form-card" style="max-width:880px;margin-inline:auto" data-reveal>
    <h2>Pedir mentoria</h2>
    <p>O pedido é enviado pelo WhatsApp. A equipa responde com a disponibilidade e o formato.</p>
    <form class="form" data-wa-form data-intro="Olá, Cardiomwenho. Gostaria de pedir uma mentoria académica.">
      {f_text("nome", "Nome completo", auto="name")}
      {f_text("telefone", "Telefone / WhatsApp", kind="tel", auto="tel", ph="9XX XXX XXX")}
      {f_text("curso", "Curso e ano", ph="Ex.: Enfermagem, 4.º ano")}
      {f_text("inst", "Instituição de ensino", req=False)}
      {f_select("tema", "Tipo de apoio", ["Trabalho de fim de curso / monografia", "Preparação para a defesa", "Interpretação de exames cardíacos", "Interpretação de espirometria", "Preparação para estágio ou emprego", "Outro"], full=True)}
      {f_text("prazo", "Prazo", req=False, ph="Ex.: defesa em março")}
      {f_seg("formato", "Formato preferido", ["Presencial", "Online", "Tanto faz"])}
      {f_area("msg", "Descreva o que precisa", hint="Algumas linhas chegam.")}
      {consent()}
      <button class="btn btn--wa btn--block" type="submit">{I["wa"]} Enviar pedido pelo WhatsApp</button>
    </form>
    {done_block("A equipa responde com a disponibilidade.")}
  </div>
</div></section>'''

# ================================================================= CONTACTOS
contactos = phero(["Contactos"], "Contactos", "Atendemos com agendamento. Escolha a forma mais cómoda de falar connosco.") + f'''
<section class="section"><div class="wrap split split--top">
  <div data-reveal="left">
    <h2>Telefone e WhatsApp</h2>
    <ul class="ticks ticks--lg" style="margin-top:22px">{"".join(f'<li><a href="tel:+{n}" class="textlink">{p}</a></li>' for p, n in PHONES)}</ul>
    <p class="note">Os pedidos feitos no site são enviados para o WhatsApp 951 165 810.</p>
    <h2 style="margin-top:44px">Morada</h2>
    <p class="lead">{ADDRESS}</p>
    <div class="actions"><a class="btn btn--line" href="{MAPS}" target="_blank" rel="noopener">{I["pin"]} Abrir no Google Maps</a></div>
  </div>
  <div class="form-card" data-reveal="right">
    <h2>Enviar mensagem</h2>
    <p>Para dúvidas gerais. Para marcar um exame, use a <a href="/marcar">página de marcação</a>.</p>
    <form class="form" data-wa-form data-intro="Olá, Cardiomwenho.">
      {f_text("nome", "Nome", auto="name", full=True)}
      {f_select("assunto", "Assunto", ["Informações sobre exames", "Resultados", "Empresas", "Cursos", "Mentorias", "Outro assunto"], full=True)}
      {f_area("msg", "Mensagem", req=True)}
      {consent()}
      <button class="btn btn--wa btn--block" type="submit">{I["wa"]} Enviar pelo WhatsApp</button>
    </form>
    {done_block("A equipa responde assim que possível.")}
  </div>
</div></section>'''

# ================================================================= PRIVACIDADE
privacidade = phero(["Privacidade"], "Privacidade", "Como tratamos os dados que nos envia através deste site.") + '''
<section class="section"><div class="wrap legal">
  <h2>Que dados recolhemos</h2>
  <p>Este site não tem base de dados e não guarda os dados dos formulários. Quando envia um pedido, o seu navegador prepara uma mensagem que é aberta no WhatsApp. Só chega à Cardiomwenho se tocar em Enviar.</p>
  <h2>Para que usamos os dados</h2>
  <p>Usamos o nome, o contacto e as informações do pedido apenas para responder: confirmar marcações, enviar propostas a empresas e tratar inscrições em cursos e mentorias.</p>
  <h2>Informação clínica</h2>
  <p>Pedimos que não escreva sintomas, diagnósticos ou resultados de exames nos formulários. Essa informação é tratada diretamente com a equipa, com a devida confidencialidade.</p>
  <h2>Imagens e vídeos</h2>
  <p>As fotografias e os vídeos das pessoas que aparecem neste site são publicados com a sua autorização.</p>
  <h2>WhatsApp</h2>
  <p>As mensagens enviadas pelo WhatsApp estão sujeitas às condições desse serviço.</p>
  <h2>Os seus direitos</h2>
  <p>Pode pedir, a qualquer momento, para consultar, corrigir ou apagar os seus dados. Basta enviar uma mensagem para o 951 165 810.</p>
</div></section>'''

notfound = phero([], "Página não encontrada", "O endereço que procurou não existe ou mudou de lugar.") + '''
<section class="section"><div class="wrap"><div class="actions"><a class="btn btn--red" href="/">Ir para o início</a><a class="btn btn--line" href="/exames">Ver os exames</a><a class="btn btn--line" href="/marcar">Marcar exame</a></div></div></section>'''

LD = f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"MedicalClinic","name":"Cardiomwenho","description":"Serviços de Saúde Cardiopulmonar e Ocupacional","telephone":"+244951165810","image":"{SITE_URL}/assets/img/og.jpg","logo":"{SITE_URL}/assets/img/logo.png","address":{{"@type":"PostalAddress","streetAddress":"Rua Ferreira Viana, São Pedro","addressLocality":"Huambo","addressCountry":"AO"}},"url":"{SITE_URL}/"}}</script>'''

PAGES = [
    ("index", "Cardiomwenho · Saúde Cardiopulmonar e Ocupacional no Huambo",
     "Exames cardíacos, pulmonares e de saúde ocupacional no Huambo. Marque pelo WhatsApp e veja como se preparar.", home, None, LD),
    ("exames", "Exames · Cardiomwenho", "ECG, Holter, MAPA, ergometria, espirometria e exames de saúde ocupacional no Huambo.", exames, "/exames", ""),
    ("guia", "Guia do doente · Cardiomwenho", "Do primeiro contacto ao resultado: como marcar, como se preparar e o que esperar no dia do exame.", guia, "/guia", ""),
    ("marcar", "Marcar exame · Cardiomwenho", "Peça a marcação do seu exame pelo WhatsApp. A equipa confirma a hora.", marcar, None, ""),
    ("empresas", "Empresas · Cardiomwenho", "Exames admissionais, periódicos, de retorno ao trabalho e de mudança de função para empresas no Huambo.", empresas, "/empresas", ""),
    ("cursos", "Cursos de exames cardíacos e respiratórios · Cardiomwenho", "Cursos de ECG, Holter, MAPA, ergometria e espirometria com certificado. Inscrição pelo WhatsApp.", cursos, "/cursos", ""),
    ("mentorias", "Mentorias académicas · Cardiomwenho", "Mentoria para estudantes e recém-formados da área da saúde em exames cardiopulmonares.", mentorias, "/mentorias", ""),
    ("contactos", "Contactos · Cardiomwenho", "Telefones, WhatsApp e morada da Cardiomwenho em São Pedro, Huambo.", contactos, "/contactos", ""),
    ("privacidade", "Privacidade · Cardiomwenho", "Como a Cardiomwenho trata os dados enviados pelo site.", privacidade, None, ""),
    ("404", "Página não encontrada · Cardiomwenho", "Página não encontrada.", notfound, None, ""),
]

def main():
    (OUT / "exames").mkdir(parents=True, exist_ok=True)
    for slug, title, desc, body, cur, head in PAGES:
        (OUT / f"{slug}.html").write_text(page(slug, title, desc, body, cur, extra_head=head), encoding="utf-8")
    for x in EXAMS:
        ld = (f'<script type="application/ld+json">{{"@context":"https://schema.org","@type":"MedicalTest","name":{json_str(x["name"])},'
              f'"description":{json_str(x["summary"])},"url":"{SITE_URL}/exames/{x["slug"]}"}}</script>')
        (OUT / "exames" / f"{x['slug']}.html").write_text(
            page(f"exames/{x['slug']}", f"{x['name']} · Cardiomwenho", f"{x['summary']} Saiba como se preparar e marque pelo WhatsApp.",
                 exam_page(x), "/exames", og=f"/assets/img/exames/{x['img']}.jpg", extra_head=ld), encoding="utf-8")
    urls = [""] + [p[0] for p in PAGES if p[0] not in ("index", "404", "privacidade")] + [f"exames/{x['slug']}" for x in EXAMS]
    (OUT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + "".join(f"  <url><loc>{SITE_URL}/{u}</loc></url>\n" for u in urls) + "</urlset>\n", encoding="utf-8")
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {SITE_URL}/sitemap.xml\n", encoding="utf-8")
    print(f"{len(PAGES) + len(EXAMS)} páginas geradas em {OUT}")

def json_str(s):
    import json
    return json.dumps(s, ensure_ascii=False)

if __name__ == "__main__":
    main()

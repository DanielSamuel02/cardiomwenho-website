/* ==========================================================================
   Cardiomwenho — comportamento do site
   Sem base de dados: os pedidos são preparados no navegador e enviados
   pelo WhatsApp. Sem dependências externas.
   ========================================================================== */
(function () {
  "use strict";

  /* Número de WhatsApp que recebe os pedidos (formato internacional). */
  var WA_NUMBER = (document.documentElement.getAttribute("data-wa") || "244951165810").replace(/\D/g, "");
  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function $(s, r) { return (r || document).querySelector(s); }
  function $all(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function waLink(text) { return "https://wa.me/" + WA_NUMBER + "?text=" + encodeURIComponent(text); }

  /* ---------- Cabeçalho, barra de progresso e botão flutuante ---------- */
  var header = $(".header"), progress = $(".progress"), fab = $(".fab");
  var ticking = false;
  function onScroll() {
    var y = window.scrollY, h = document.documentElement.scrollHeight - window.innerHeight;
    if (header) header.classList.toggle("is-scrolled", y > 8);
    if (progress) progress.style.transform = "scaleX(" + (h > 0 ? Math.min(1, y / h) : 0) + ")";
    if (fab) fab.classList.toggle("is-on", y > 420);
    ticking = false;
  }
  window.addEventListener("scroll", function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();

  /* ---------- Menu móvel ---------- */
  var nav = $("#nav"), scrim = $(".scrim"), openBtn = $(".menu-btn:not(.nav-close)"), closeBtn = $(".nav-close");
  function setMenu(open) {
    if (!nav) return;
    nav.classList.toggle("is-open", open);
    scrim.classList.toggle("is-open", open);
    openBtn.setAttribute("aria-expanded", String(open));
    document.body.style.overflow = open ? "hidden" : "";
    if (open) { (nav.querySelector("a") || nav).focus(); } else { openBtn.focus(); }
  }
  if (openBtn) openBtn.addEventListener("click", function () { setMenu(true); });
  if (closeBtn) closeBtn.addEventListener("click", function () { setMenu(false); });
  if (scrim) scrim.addEventListener("click", function () { setMenu(false); });
  document.addEventListener("keydown", function (e) { if (e.key === "Escape" && nav && nav.classList.contains("is-open")) setMenu(false); });

  /* ---------- Revelação ao percorrer a página ----------
     Revela cada elemento quando o seu topo entra no ecrã. Os elementos que
     ficaram para trás (saltos por âncora, tecla End) também são revelados. */
  var pending = $all("[data-reveal]");
  function sweep() {
    if (!pending.length) return;
    var limit = window.innerHeight * .92;
    pending = pending.filter(function (el) {
      if (el.getBoundingClientRect().top < limit) { el.classList.add("is-in"); return false; }
      return true;
    });
  }
  if (reduceMotion) { pending.forEach(function (el) { el.classList.add("is-in"); }); pending = []; }
  else {
    var sweepQueued = false;
    window.addEventListener("scroll", function () { if (!sweepQueued) { sweepQueued = true; requestAnimationFrame(function () { sweepQueued = false; sweep(); }); } }, { passive: true });
    window.addEventListener("resize", sweep);
    window.addEventListener("load", sweep);
    sweep();
  }

  /* ---------- Pequenos utilitários ---------- */
  $all("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
  $all("[data-wa]").forEach(function (a) { a.href = waLink(a.getAttribute("data-wa")); a.target = "_blank"; a.rel = "noopener"; });
  var today = new Date(); today.setMinutes(today.getMinutes() - today.getTimezoneOffset());
  $all('input[type="date"]').forEach(function (i) { i.min = today.toISOString().slice(0, 10); });

  var params = new URLSearchParams(location.search);
  $all("select[data-param]").forEach(function (sel) {
    var v = params.get(sel.getAttribute("data-param"));
    if (v && sel.querySelector('option[value="' + v.replace(/"/g, "") + '"]')) sel.value = v;
  });
  $all("input[type=checkbox][data-param]").forEach(function (cb) {
    var v = params.get(cb.getAttribute("data-param"));
    if (v && v.split(",").indexOf(cb.value) > -1) cb.checked = true;
  });


  /* ---------- Turmas mensais (os cursos decorrem todos os meses) ---------- */
  var MESES = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"];
  function nextMonths(n) {
    var d = new Date(), out = [];
    for (var i = 0; i < n; i++) { var m = new Date(d.getFullYear(), d.getMonth() + i, 1); out.push({ m: MESES[m.getMonth()], y: m.getFullYear() }); }
    return out;
  }
  $all("[data-months]").forEach(function (ul) {
    ul.innerHTML = nextMonths(Number(ul.getAttribute("data-months")) || 6).map(function (x, i) {
      return "<li><b>" + x.m.charAt(0).toUpperCase() + x.m.slice(1) + "</b> <span>" + (i === 0 ? "Turma deste mês" : x.y) + "</span></li>";
    }).join("");
  });
  $all("[data-months-select]").forEach(function (sel) {
    nextMonths(Number(sel.getAttribute("data-months-select")) || 6).forEach(function (x) {
      var o = document.createElement("option"); o.textContent = x.m.charAt(0).toUpperCase() + x.m.slice(1) + " de " + x.y; sel.appendChild(o);
    });
  });

  /* ---------- Índice de exames: pré-visualização da fotografia ---------- */
  var pv = $(".preview"), pvList = $("[data-preview]");
  if (pv && pvList && window.matchMedia("(hover: hover) and (pointer: fine)").matches) {
    var pvImg = $("img", pv), tx = 0, ty = 0, cx = 0, cy = 0, raf = null;
    function loop() { cx += (tx - cx) * .18; cy += (ty - cy) * .18; pv.style.left = cx + "px"; pv.style.top = cy + "px"; raf = requestAnimationFrame(loop); }
    $all("a[data-img]", pvList).forEach(function (a) {
      var pre = new Image(); pre.src = a.getAttribute("data-img");
      a.addEventListener("mouseenter", function (e) { pvImg.src = a.getAttribute("data-img"); if (!raf) { cx = tx = e.clientX + 190; cy = ty = e.clientY; loop(); } pv.classList.add("is-on"); });
      a.addEventListener("mousemove", function (e) { tx = e.clientX + 190; ty = e.clientY; });
      a.addEventListener("mouseleave", function () { pv.classList.remove("is-on"); });
    });
    pvList.addEventListener("mouseleave", function () { if (raf) { cancelAnimationFrame(raf); raf = null; } });
  }

  /* ---------- Vídeo do topo: pausar / reproduzir ---------- */
  var playIco = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>';
  var pauseIco = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg>';
  $all("[data-vid-toggle]").forEach(function (btn) {
    var v = btn.parentElement.querySelector("video");
    if (!v) return;
    if (reduceMotion) { v.removeAttribute("autoplay"); v.pause(); }
    function sync() { var p = !v.paused; btn.innerHTML = p ? pauseIco : playIco; btn.setAttribute("aria-label", p ? "Pausar vídeo" : "Reproduzir vídeo"); }
    btn.addEventListener("click", function () { if (v.paused) v.play(); else v.pause(); });
    v.addEventListener("play", sync); v.addEventListener("pause", sync); sync();
  });

  /* ---------- Galeria de vídeos (janela com controlos) ---------- */
  var lb = $("#lightbox");
  if (lb) {
    var lbVideo = $("video", lb), lbCap = $("figcaption", lb), lastTrigger = null;
    $all("[data-video]").forEach(function (b) {
      b.addEventListener("click", function () {
        lastTrigger = b;
        lbVideo.src = b.getAttribute("data-video");
        lbVideo.poster = b.getAttribute("data-poster") || "";
        lbCap.textContent = b.getAttribute("data-title") || "";
        if (typeof lb.showModal === "function") lb.showModal(); else lb.setAttribute("open", "");
        var pr = lbVideo.play(); if (pr && pr.catch) pr.catch(function () {});
      });
    });
    function closeLb() { lbVideo.pause(); lbVideo.removeAttribute("src"); lbVideo.load(); if (lb.open) lb.close(); if (lastTrigger) lastTrigger.focus(); }
    $(".close", lb).addEventListener("click", closeLb);
    lb.addEventListener("click", function (e) { if (e.target === lb) closeLb(); });
    lb.addEventListener("cancel", function (e) { e.preventDefault(); closeLb(); });
  }

  /* ---------- Carrossel de exames ---------- */
  $all("[data-rail]").forEach(function (wrap) {
    var rail = $(".rail", wrap);
    $all("[data-dir]", wrap).forEach(function (b) {
      b.addEventListener("click", function () {
        rail.scrollBy({ left: Number(b.getAttribute("data-dir")) * (rail.clientWidth * .8), behavior: reduceMotion ? "auto" : "smooth" });
      });
    });
  });

  /* ---------- Filtro de exames ---------- */
  var filters = $(".filters");
  if (filters) {
    filters.addEventListener("click", function (e) {
      var b = e.target.closest("button"); if (!b) return;
      var f = b.getAttribute("data-filter"), n = 0;
      $all("button", filters).forEach(function (x) { x.setAttribute("aria-pressed", String(x === b)); });
      $all(".exam-grid .ecard").forEach(function (ex, i) {
        var show = f === "todos" || ex.getAttribute("data-area") === f;
        ex.hidden = !show;
        ex.classList.remove("is-entering");
        if (show) { n++; if (!reduceMotion) { void ex.offsetWidth; ex.style.animationDelay = (n * 40) + "ms"; ex.classList.add("is-entering"); } }
      });
      var live = $("#filter-status"); if (live) live.textContent = n + " exames apresentados";
    });
    var start = params.get("area");
    if (start) { var sb = filters.querySelector('[data-filter="' + start + '"]'); if (sb) sb.click(); }
  }

  /* ---------- Jornada do doente (separadores) ---------- */
  $all("[data-journey]").forEach(function (root) {
    var tabs = $all('[role="tab"]', root), fill = $(".fill", root);
    function select(i, focus) {
      tabs.forEach(function (t, k) {
        var on = k === i, panel = document.getElementById(t.getAttribute("aria-controls"));
        t.setAttribute("aria-selected", String(on)); t.tabIndex = on ? 0 : -1;
        t.classList.toggle("is-done", k < i);
        panel.hidden = !on;
        if (on) { panel.classList.remove("is-entering"); if (!reduceMotion) { void panel.offsetWidth; panel.classList.add("is-entering"); } }
      });
      if (fill) { var a = tabs[0].getBoundingClientRect(), b = tabs[i].getBoundingClientRect(); fill.style.setProperty("--fill", (b.top - a.top) + "px"); }
      if (focus) tabs[i].focus();
    }
    tabs.forEach(function (t, i) {
      t.addEventListener("click", function () { select(i); });
      t.addEventListener("keydown", function (e) {
        var k = e.key, n = tabs.length, j = null;
        if (k === "ArrowDown" || k === "ArrowRight") j = (i + 1) % n;
        if (k === "ArrowUp" || k === "ArrowLeft") j = (i - 1 + n) % n;
        if (k === "Home") j = 0; if (k === "End") j = n - 1;
        if (j !== null) { e.preventDefault(); select(j, true); }
      });
    });
    $all("[data-journey-next]", root).forEach(function (b) {
      b.addEventListener("click", function () { var cur = tabs.findIndex(function (t) { return t.getAttribute("aria-selected") === "true"; }); select(Math.min(cur + 1, tabs.length - 1), true); });
    });
    select(0);
    window.addEventListener("resize", function () { var cur = tabs.findIndex(function (t) { return t.getAttribute("aria-selected") === "true"; }); select(cur); });
  });

  /* ---------- Guia: navegação lateral activa ---------- */
  var gnav = $(".guide-nav");
  if (gnav && "IntersectionObserver" in window) {
    var links = $all("a", gnav);
    var gio = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) links.forEach(function (l) { l.classList.toggle("is-active", l.getAttribute("href") === "#" + en.target.id); });
      });
    }, { rootMargin: "-40% 0px -55% 0px" });
    links.forEach(function (l) { var t = document.querySelector(l.getAttribute("href")); if (t) gio.observe(t); });
  }

  /* ---------- Guia: preparação por exame ---------- */
  var prepSel = $("#prep-select"), prepOut = $("#prep-out");
  if (prepSel && prepOut) {
    function showPrep() {
      $all("[data-prep]", prepOut).forEach(function (b) { b.hidden = b.getAttribute("data-prep") !== prepSel.value; });
    }
    prepSel.addEventListener("change", showPrep);
    var ex = params.get("exame"); if (ex && prepSel.querySelector('option[value="' + ex + '"]')) prepSel.value = ex;
    showPrep();
  }

  /* ---------- Cursos: cálculo do valor ---------- */
  var picker = $("[data-course-picker]");
  function fmt(n) { return n.toLocaleString("pt-PT").replace(/ |\s/g, " ") + " Kz"; }
  function courseTotal(n) {
    /* Tabela do cartaz oficial: 20 mil por curso; 15 mil por curso para quem fizer dois; 10 mil por curso para quem fizer três. */
    if (n === 1) return { unit: 20000, total: 20000 };
    if (n === 2) return { unit: 15000, total: 30000 };
    if (n === 3) return { unit: 10000, total: 30000 };
    return null;
  }
  function updateCourses() {
    if (!picker) return;
    var n = $all("input[name=curso]:checked", picker).length, out = $("#course-total"), sub = $("#course-sub");
    $all(".tiers li").forEach(function (li) { li.classList.toggle("is-on", Number(li.getAttribute("data-n")) === n); });
    if (!out) return;
    if (n === 0) { out.textContent = "Escolha um ou mais cursos"; sub.textContent = "O valor aparece aqui."; }
    else {
      var t = courseTotal(n);
      if (t) { out.textContent = fmt(t.total); sub.textContent = n === 1 ? "1 curso" : n + " cursos, " + fmt(t.unit) + " por curso"; }
      else { out.textContent = "Valor a confirmar"; sub.textContent = n + " cursos: a equipa confirma o valor pelo WhatsApp."; }
    }
    out.classList.remove("bump"); void out.offsetWidth; out.classList.add("bump");
  }
  if (picker) { picker.addEventListener("change", updateCourses); updateCourses(); }

  /* ---------- Formulários → WhatsApp ---------- */
  function fieldValue(el) {
    if (el.type === "radio") { var c = el.form.querySelector('input[name="' + el.name + '"]:checked'); return c ? c.value : ""; }
    if (el.tagName === "SELECT") return el.value ? el.options[el.selectedIndex].text : "";
    if (el.type === "date" && el.value) { var p = el.value.split("-"); return p[2] + "/" + p[1] + "/" + p[0]; }
    return (el.value || "").trim();
  }
  function setError(el, msg) {
    var wrap = el.closest(".field") || el.parentElement, err = wrap.querySelector(".err");
    if (msg) { el.setAttribute("aria-invalid", "true"); if (err) err.textContent = msg; }
    else { el.removeAttribute("aria-invalid"); if (err) err.textContent = ""; }
  }
  function validate(form) {
    var firstBad = null;
    $all("[required]", form).forEach(function (el) {
      var bad = false, msg = "";
      if (el.type === "checkbox") { bad = !el.checked; msg = "Confirme para continuar."; }
      else if (el.type === "radio") { bad = !form.querySelector('input[name="' + el.name + '"]:checked'); msg = "Escolha uma opção."; }
      else if (!fieldValue(el)) { bad = true; msg = "Preencha este campo."; }
      if (!bad && el.type === "tel" && el.value.replace(/\D/g, "").length < 9) { bad = true; msg = "Indique um número com 9 dígitos, por exemplo 923 000 000."; }
      if (el.type === "checkbox") el.setAttribute("aria-invalid", bad ? "true" : "false"); else setError(el, bad ? msg : "");
      if (bad && !firstBad) firstBad = el;
    });
    var group = form.querySelector("[data-min-one]");
    if (group) {
      var e2 = $("#course-err");
      if (!group.querySelector("input:checked")) { if (e2) e2.textContent = "Escolha pelo menos um curso."; if (!firstBad) firstBad = group.querySelector("input"); }
      else if (e2) e2.textContent = "";
    }
    return firstBad;
  }
  function buildMessage(form) {
    var lines = [form.getAttribute("data-intro")], seen = {};
    $all("[data-label]", form).forEach(function (el) {
      var label = el.getAttribute("data-label");
      if (el.type === "checkbox") {
        if (seen[el.name]) return; seen[el.name] = true;
        var vals = $all('input[name="' + el.name + '"]:checked', form).map(function (c) { return c.value; });
        if (vals.length) lines.push("*" + label + ":* " + vals.join(", "));
        return;
      }
      if (el.type === "radio") { if (seen[el.name]) return; seen[el.name] = true; }
      var v = fieldValue(el); if (v) lines.push("*" + label + ":* " + v);
    });
    if (form.getAttribute("data-extra") === "cursos") {
      var t = courseTotal($all("input[name=curso]:checked", form).length);
      lines.push("*Valor indicado no site:* " + (t ? fmt(t.total) : "a confirmar"));
    }
    lines.push("", "Enviado a partir do site da Cardiomwenho.");
    return lines.join("\n");
  }
  $all("form[data-wa-form]").forEach(function (form) {
    form.setAttribute("novalidate", "");
    form.addEventListener("input", function (e) { if (e.target.getAttribute("aria-invalid") === "true") setError(e.target, ""); });
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      var bad = validate(form);
      if (bad) { bad.focus(); return; }
      var url = waLink(buildMessage(form));
      var win = null; try { win = window.open(url, "_blank", "noopener"); } catch (err) { win = null; }
      var card = form.closest(".form-card"), done = card && card.querySelector(".done");
      if (done) {
        var a = done.querySelector("[data-wa-again]"); if (a) a.href = url;
        form.hidden = true; done.classList.add("is-on");
        var h = done.querySelector("h3"); if (h) { h.setAttribute("tabindex", "-1"); h.focus({ preventScroll: true }); }
        card.scrollIntoView({ block: "start", behavior: reduceMotion ? "auto" : "smooth" });
      }
      if (!win && !done) location.href = url;
    });
  });
  $all("[data-form-reset]").forEach(function (b) {
    b.addEventListener("click", function () {
      var card = b.closest(".form-card"), form = card.querySelector("form");
      form.reset(); form.hidden = false; card.querySelector(".done").classList.remove("is-on");
      updateCourses(); (form.querySelector("input, select") || form).focus();
    });
  });
})();

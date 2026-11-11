"""Servidor local que imita os endereços limpos da Vercel (/exames -> /exames.html).

Uso:  python3 scripts/serve.py   e abrir http://localhost:8080
"""
import http.server, pathlib, functools

ROOT = pathlib.Path(__file__).resolve().parent.parent / "public"

class Handler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        clean = path.split("?", 1)[0].split("#", 1)[0]
        p = ROOT / clean.lstrip("/")
        if clean != "/" and (ROOT / (clean.strip("/") + ".html")).exists():
            path = clean + ".html"
        return super().translate_path(path)

    def send_error(self, code, message=None, explain=None):
        if code == 404 and (ROOT / "404.html").exists():
            body = (ROOT / "404.html").read_bytes()
            self.send_response(404); self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body))); self.end_headers(); self.wfile.write(body)
        else:
            super().send_error(code, message, explain)

if __name__ == "__main__":
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    http.server.ThreadingHTTPServer(("", port), functools.partial(Handler, directory=str(ROOT))).serve_forever()

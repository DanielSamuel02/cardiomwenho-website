# Cardiomwenho — website

Website institucional da **Cardiomwenho, Serviços de Saúde Cardiopulmonar e Ocupacional** (Huambo, Angola).
Desenvolvido pela [HealthLink](https://healthlink-website.vercel.app).

- Site estático, sem base de dados e sem dependências externas.
- As marcações, os pedidos de empresas, as inscrições em cursos e os pedidos de mentoria são preparados no navegador e enviados pelo WhatsApp para o **951 165 810**.
- Publicado na Vercel a partir da pasta `public/`.

## Estrutura

```
public/                 site publicado (gerado + recursos)
  assets/css/site.css   estilos, animações e regras de movimento reduzido
  assets/js/site.js     menu, animações, jornada do doente, vídeos, formulários → WhatsApp
  assets/img/           fotografias otimizadas (WebP + JPEG)
  assets/video/         vídeos otimizados (H.264, faststart)
  assets/fonts/         Poppins (subconjunto latino)
  exames/*.html         uma página por exame
scripts/
  content.py            textos: exames, preparação, cursos, vídeos, jornada do doente
  build.py              gera as páginas HTML em public/
  serve.py              servidor local com endereços limpos
vercel.json             pasta de saída, endereços limpos, cache e cabeçalhos de segurança
```

## Editar conteúdos

1. Alterar os textos em `scripts/content.py` (ou a estrutura das páginas em `scripts/build.py`).
2. Gerar as páginas: `python3 scripts/build.py` (Python 3.12 ou superior).
3. Ver localmente: `python3 scripts/serve.py` e abrir http://localhost:8080
4. Fazer commit e push para `main`. A Vercel publica automaticamente.

O número de WhatsApp que recebe os pedidos está em `scripts/content.py` (`WA_MAIN`).
Não há variáveis de ambiente nem credenciais: o site não usa serviços externos.

## Notas de conteúdo

- Serviços, slogans, contactos, cursos e preços vêm dos materiais oficiais da Cardiomwenho.
- As orientações de preparação para cada exame são gerais e devem ser validadas pela equipa clínica.
- As fotografias e os vídeos são publicados com autorização das pessoas que neles aparecem.
- As fotografias da visita institucional são do Gabinete da Juventude e Desportos (huambo.gov.ao).

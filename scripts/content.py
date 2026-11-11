"""Conteúdos do site da Cardiomwenho.

Os textos institucionais (serviços, slogans, contactos, cursos e preços) vêm dos
materiais oficiais da Cardiomwenho. As orientações de preparação são gerais e
devem ser validadas pela equipa clínica antes de cada actualização.
"""

SITE_URL = "https://cardiomwenho.vercel.app"
WA_MAIN = "244951165810"
PHONES = [("951 165 810", "244951165810"), ("939 126 610", "244939126610"), ("946 858 377", "244946858377")]
ADDRESS = "São Pedro, Rua Ferreira Viana, Huambo, Angola"
MAPS = "https://www.google.com/maps/search/?api=1&query=Rua+Ferreira+Viana%2C+S%C3%A3o+Pedro%2C+Huambo%2C+Angola"

AREAS = {
    "cardio": {"name": "Exames cardíacos", "cls": "c-cardio", "icon": "heart"},
    "resp": {"name": "Exames pulmonares", "cls": "c-resp", "icon": "lungs"},
    "ocup": {"name": "Saúde ocupacional", "cls": "c-ocup", "icon": "work"},
}

# Orientações comuns às avaliações ocupacionais
_OCUP_PREP = [
    "Traga um documento de identificação.",
    "Traga a guia ou o pedido da empresa, se a empresa o tiver emitido.",
    "Traga exames anteriores e a lista dos medicamentos que toma.",
    "Se usa óculos ou lentes de contacto, traga-os consigo.",
]
_OCUP_DAY = [
    "Apresente-se à hora marcada; a equipa confirma os seus dados e as funções que desempenha.",
    "A avaliação inclui os exames definidos para o seu caso e para a sua função.",
]
_OCUP_AFTER = "A equipa informa como e quando o resultado é comunicado, de acordo com o que foi combinado com a empresa."

EXAMS = [
    {
        "slug": "ecg", "area": "cardio", "name": "Eletrocardiograma (ECG)", "short": "ECG",
        "img": "ecg", "alt": "Eletrocardiograma em repouso realizado na Cardiomwenho",
        "summary": "Regista a atividade elétrica do coração em repouso. É rápido e indolor.",
        "what": "O eletrocardiograma regista os sinais elétricos do coração através de elétrodos colocados no peito, nos braços e nas pernas. Mostra o ritmo e a frequência cardíaca e pode revelar alterações que merecem acompanhamento.",
        "when": ["Avaliações de rotina e check-ups", "Palpitações, cansaço ou tonturas", "Antes de algumas cirurgias ou tratamentos", "Avaliações médicas ocupacionais"],
        "prep": ["Não precisa de jejum.", "Evite cremes ou óleos no peito no dia do exame.", "Use roupa que permita descobrir facilmente o peito.", "Traga exames anteriores e a lista dos medicamentos que toma."],
        "day": ["Fica deitado, em repouso, enquanto os elétrodos são colocados.", "O registo dura poucos minutos e não provoca dor.", "Deve manter-se quieto e respirar normalmente durante o registo."],
        "after": "Pode retomar de imediato as suas atividades. A equipa indica como e quando recebe o resultado, que deve mostrar ao médico que pediu o exame.",
    },
    {
        "slug": "holter", "area": "cardio", "name": "Holter (24h)", "short": "Holter",
        "img": "holter", "alt": "Elétrodos de Holter colocados no peito de um paciente",
        "summary": "Regista o ritmo do coração durante 24 horas, enquanto faz a sua rotina.",
        "what": "O Holter é um pequeno aparelho ligado a elétrodos no peito, que grava o ritmo do coração durante 24 horas. Permite detetar alterações que não aparecem num eletrocardiograma de poucos minutos.",
        "when": ["Palpitações que vêm e vão", "Tonturas ou desmaios sem causa conhecida", "Acompanhamento de alterações do ritmo cardíaco", "Avaliar o efeito de um tratamento"],
        "prep": ["Tome banho antes de vir: o aparelho não pode ser molhado durante as 24 horas.", "Não aplique cremes ou óleos no peito.", "Use roupa larga, de preferência com botões à frente.", "Traga a lista dos medicamentos que toma."],
        "day": ["A colocação dos elétrodos e do aparelho leva poucos minutos.", "Faça a sua rotina normal durante as 24 horas.", "Anote as horas em que sente sintomas e o que estava a fazer.", "Não molhe o aparelho nem retire os elétrodos."],
        "after": "Volte à Cardiomwenho no dia seguinte para retirar o aparelho. A equipa indica quando o relatório fica disponível.",
    },
    {
        "slug": "mapa", "area": "cardio", "name": "MAPA (Monitorização Ambulatorial da Pressão Arterial)", "short": "MAPA",
        "img": "mapa", "alt": "Profissional da Cardiomwenho junto ao equipamento de exames",
        "summary": "Mede a pressão arterial ao longo de 24 horas, em casa e no trabalho.",
        "what": "A MAPA usa uma braçadeira ligada a um pequeno aparelho que mede a pressão arterial automaticamente, várias vezes ao longo de 24 horas. Dá uma imagem mais real da pressão do que uma medição isolada na consulta.",
        "when": ["Confirmar ou excluir hipertensão arterial", "Pressão alta só no consultório", "Avaliar se o tratamento está a controlar a pressão", "Sintomas como tonturas que podem estar ligados à pressão"],
        "prep": ["Tome banho antes de vir: o aparelho não pode ser molhado.", "Use uma camisa ou blusa de manga larga.", "Mantenha a medicação habitual, salvo indicação diferente do seu médico.", "Planeie um dia normal, sem exercício intenso."],
        "day": ["A braçadeira é colocada no braço e insufla automaticamente a intervalos regulares.", "Durante cada medição, pare, mantenha o braço quieto e relaxado.", "Anote as horas a que dorme, acorda, toma medicação ou sente sintomas."],
        "after": "Volte à Cardiomwenho no dia seguinte para retirar o aparelho. A equipa indica quando o relatório fica disponível.",
    },
    {
        "slug": "ergometria", "area": "cardio", "name": "Ergometria (Teste de esforço)", "short": "Ergometria",
        "img": "ergometria", "alt": "Sala de ergometria da Cardiomwenho com a equipa a acompanhar um teste de esforço",
        "summary": "Acompanha o coração em movimento, com monitorização em tempo real.",
        "what": "No teste de esforço, o coração é monitorizado enquanto pedala numa bicicleta e a carga aumenta de forma gradual. A equipa acompanha em tempo real o eletrocardiograma, a pressão arterial e os sintomas.",
        "when": ["Dor ou desconforto no peito durante o esforço", "Avaliar a capacidade física e a resposta do coração ao exercício", "Acompanhamento de doença cardíaca conhecida", "Avaliação antes de iniciar atividade física"],
        "prep": ["Use roupa confortável e calçado desportivo.", "Faça uma refeição leve cerca de duas horas antes.", "Evite café, tabaco e bebidas energéticas nas horas anteriores.", "Pergunte ao seu médico se deve manter ou suspender algum medicamento.", "Traga exames anteriores."],
        "day": ["São colocados elétrodos no peito e uma braçadeira de pressão.", "Pedala na bicicleta enquanto a carga aumenta aos poucos.", "Diga de imediato à equipa se sentir dor, falta de ar ou tonturas: o teste pode ser parado a qualquer momento.", "No fim, continua monitorizado durante a recuperação."],
        "after": "Pode sentir cansaço passageiro. A equipa indica como e quando recebe o resultado, que deve mostrar ao seu médico.",
    },
    {
        "slug": "espirometria", "area": "resp", "name": "Espirometria", "short": "Espirometria",
        "img": "espirometria", "alt": "Paciente a fazer espirometria na Cardiomwenho",
        "summary": "Mede o ar que os pulmões movimentam e a velocidade com que o fazem.",
        "what": "Na espirometria, sopra com força para um bocal ligado a um aparelho que mede o volume e a velocidade do ar. É um dos exames principais para avaliar a função respiratória.",
        "when": ["Falta de ar, tosse prolongada ou chiado", "Diagnóstico e acompanhamento de asma ou DPOC", "Avaliações ocupacionais em ambientes com poeiras ou fumos", "Antes de algumas cirurgias"],
        "prep": ["Não fume na hora anterior ao exame.", "Evite refeições pesadas antes do exame.", "Use roupa folgada, que não aperte o peito ou a cintura.", "Se usa bombas ou inaladores, pergunte ao seu médico se deve suspendê-los antes do exame."],
        "day": ["Fica sentado, com uma mola no nariz.", "A equipa explica como respirar e sopra várias vezes, com toda a força, para o bocal.", "Em alguns casos, repete-se o exame depois de um medicamento inalado."],
        "after": "Pode sentir cansaço ou uma tontura ligeira, que passa rapidamente. A equipa indica como e quando recebe o resultado.",
    },
    {
        "slug": "avaliacao-funcional-respiratoria", "area": "resp", "name": "Avaliação funcional respiratória", "short": "Avaliação respiratória",
        "img": "afr", "alt": "Profissional da Cardiomwenho a realizar uma avaliação respiratória",
        "summary": "Avalia de forma mais completa como os pulmões estão a funcionar.",
        "what": "A avaliação funcional respiratória junta a espirometria a outras medições, conforme o caso, para perceber em detalhe como os pulmões estão a funcionar.",
        "when": ["Queixas respiratórias que precisam de avaliação detalhada", "Acompanhamento de doença respiratória crónica", "Avaliação antes de cirurgias", "Avaliações ocupacionais"],
        "prep": ["Não fume na hora anterior ao exame.", "Evite refeições pesadas antes do exame.", "Use roupa folgada.", "Traga exames respiratórios anteriores e a lista dos medicamentos que toma."],
        "day": ["Fica sentado e segue as instruções da equipa para respirar e soprar.", "As medições repetem-se algumas vezes para garantir resultados fiáveis."],
        "after": "Pode retomar as suas atividades. A equipa indica como e quando recebe o resultado.",
    },
    {
        "slug": "acompanhamento-respiratorio", "area": "resp", "name": "Acompanhamento de condições respiratórias", "short": "Acompanhamento respiratório",
        "img": "acompanhamento-resp", "alt": "Acompanhamento respiratório com espirometria na Cardiomwenho",
        "summary": "Seguimento regular de quem já tem uma condição respiratória.",
        "what": "Para quem vive com asma, DPOC ou outra condição respiratória, a repetição dos exames ao longo do tempo ajuda a perceber a evolução e a ajustar o tratamento com o médico.",
        "when": ["Asma ou DPOC em acompanhamento", "Alteração dos sintomas respiratórios", "Avaliar a resposta a um novo tratamento"],
        "prep": ["Traga os exames respiratórios anteriores.", "Traga a lista dos medicamentos e inaladores que usa.", "Não fume na hora anterior ao exame."],
        "day": ["A equipa repete os exames combinados e compara com os anteriores."],
        "after": "Leve os resultados ao seu médico para decidir os próximos passos do tratamento.",
    },
    {
        "slug": "avaliacoes-ocupacionais", "area": "ocup", "name": "Avaliações médicas ocupacionais", "short": "Avaliação ocupacional",
        "img": "ocupacional", "alt": "Profissional da Cardiomwenho a avaliar um trabalhador",
        "summary": "Avaliação da saúde do trabalhador em relação às funções que desempenha.",
        "what": "As avaliações médicas ocupacionais verificam a saúde do trabalhador e a sua relação com as funções e o ambiente de trabalho, para proteger o trabalhador e a empresa.",
        "when": ["Pedidos da empresa ao longo da vida profissional do trabalhador", "Funções com exigências físicas ou exposição a riscos"],
        "prep": _OCUP_PREP, "day": _OCUP_DAY, "after": _OCUP_AFTER,
    },
    {
        "slug": "exames-admissionais", "area": "ocup", "name": "Exames admissionais", "short": "Admissionais",
        "img": "admissional", "alt": "Profissional da Cardiomwenho a preparar um eletrocardiograma",
        "summary": "Feitos antes de o trabalhador iniciar funções numa empresa.",
        "what": "Os exames admissionais avaliam a saúde do trabalhador antes de começar a trabalhar, tendo em conta as funções que vai desempenhar.",
        "when": ["Antes do início de funções numa nova empresa"],
        "prep": _OCUP_PREP, "day": _OCUP_DAY, "after": _OCUP_AFTER,
    },
    {
        "slug": "exames-periodicos", "area": "ocup", "name": "Exames periódicos", "short": "Periódicos",
        "img": "periodico", "alt": "Eletrocardiograma realizado na Cardiomwenho",
        "summary": "Repetidos em intervalos regulares, para acompanhar a saúde dos colaboradores.",
        "what": "Os exames periódicos repetem-se ao longo do tempo para acompanhar a saúde dos colaboradores e detetar cedo alterações relacionadas com o trabalho.",
        "when": ["Nos intervalos definidos pela empresa para cada função"],
        "prep": _OCUP_PREP, "day": _OCUP_DAY, "after": _OCUP_AFTER,
    },
    {
        "slug": "exames-de-retorno", "area": "ocup", "name": "Exames de retorno ao trabalho", "short": "Retorno ao trabalho",
        "img": "retorno", "alt": "Paciente a fazer um eletrocardiograma na Cardiomwenho",
        "summary": "Feitos quando o trabalhador regressa após uma ausência.",
        "what": "Os exames de retorno ao trabalho confirmam que o trabalhador está em condições de retomar as suas funções depois de uma ausência, por exemplo por doença.",
        "when": ["Regresso ao trabalho depois de uma ausência"],
        "prep": _OCUP_PREP + ["Traga relatórios médicos relacionados com a ausência."], "day": _OCUP_DAY, "after": _OCUP_AFTER,
    },
    {
        "slug": "exames-de-mudanca-de-funcao", "area": "ocup", "name": "Exames de mudança de função", "short": "Mudança de função",
        "img": "mudanca", "alt": "Profissional da Cardiomwenho a realizar um eletrocardiograma",
        "summary": "Feitos quando o trabalhador passa a desempenhar outra função.",
        "what": "Quando o trabalhador muda de função, estes exames avaliam se está apto para as novas exigências e riscos.",
        "when": ["Antes de mudar para uma função com exigências ou riscos diferentes"],
        "prep": _OCUP_PREP + ["Traga a descrição da nova função, se a tiver."], "day": _OCUP_DAY, "after": _OCUP_AFTER,
    },
    {
        "slug": "avaliacao-de-aptidao", "area": "ocup", "name": "Avaliação da aptidão para determinadas atividades profissionais", "short": "Avaliação de aptidão",
        "img": "aptidao", "alt": "Equipa da Cardiomwenho a acompanhar um teste de esforço",
        "summary": "Verifica se o trabalhador está apto para atividades profissionais específicas.",
        "what": "Algumas atividades profissionais exigem uma avaliação específica da aptidão física, cardíaca ou respiratória. A Cardiomwenho combina os exames necessários para cada caso.",
        "when": ["Atividades com exigências físicas ou de segurança específicas"],
        "prep": _OCUP_PREP + ["Traga a descrição da atividade a avaliar."], "day": _OCUP_DAY, "after": _OCUP_AFTER,
    },
]

COURSES = [
    ("ECG", "cardio", "Eletrocardiograma (ECG)", "Domine a técnica e interprete com segurança."),
    ("Holter", "cardio", "Holter", "Instalação do aparelho e leitura do registo de 24 horas."),
    ("MAPA", "cardio", "MAPA", "Monitorização ambulatorial da pressão arterial."),
    ("Ergometria", "cardio", "Ergometria", "Teste de esforço com monitorização em tempo real."),
    ("Espirometria", "resp", "Espirometria", "Avalie a função respiratória e contribua para um melhor diagnóstico."),
]

VIDEOS = [
    {"src": "teste-esforco", "title": "Teste de esforço em bicicleta", "desc": "Monitorização em tempo real, com a equipa ao lado.", "dur": "0:11"},
    {"src": "ergometria", "title": "Por dentro da sala de ergometria", "desc": "Preparação e registo do teste de esforço.", "dur": "0:25"},
    {"src": "espirometria", "title": "Espirometria", "desc": "A equipa orienta cada sopro do exame.", "dur": "0:19"},
]

JOURNEY = [
    {"id": "descoberta", "title": "Descoberta", "img": "/assets/img/profissional-640.webp",
     "h": "Conheça quem cuida de si", "p": "A Cardiomwenho faz exames cardíacos, pulmonares e de saúde ocupacional no Huambo, com equipamentos de última geração e uma equipa médica especializada.",
     "cta": ("Ver as nossas áreas", "/#areas")},
    {"id": "informacao", "title": "Informação", "img": "/assets/img/exames/ecg-640.webp",
     "h": "Saiba para que serve cada exame", "p": "Cada exame tem uma página com o que é, quando costuma ser pedido e como decorre.",
     "cta": ("Consultar os exames", "/exames")},
    {"id": "escolha", "title": "Escolha", "img": "/assets/img/exames/espirometria-640.webp",
     "h": "Identifique o exame de que precisa", "p": "Se tem um pedido médico, procure o exame indicado. Se tem dúvidas, a equipa orienta-o pelo WhatsApp.",
     "cta": ("Pedir orientação", "/marcar?exame=nao-sei")},
    {"id": "agendamento", "title": "Agendamento", "img": "/assets/img/exames/holter-640.webp",
     "h": "Marque em menos de um minuto", "p": "Escolha o exame, o dia e o período. O site prepara a mensagem e só tem de a enviar pelo WhatsApp. A equipa confirma a hora.",
     "cta": ("Marcar exame", "/marcar")},
    {"id": "preparacao", "title": "Preparação", "img": "/assets/img/exames/mapa-640.webp",
     "h": "Chegue preparado", "p": "Veja o que trazer, que roupa usar e o que evitar antes de cada exame.",
     "cta": ("Ver como me preparar", "/guia#preparacao")},
    {"id": "atendimento", "title": "Atendimento", "img": "/assets/img/exames/ergometria-640.webp",
     "h": "Saiba o que esperar no dia", "p": "Chegue alguns minutos antes. A equipa recebe-o, explica cada passo e acompanha-o durante todo o exame.",
     "cta": ("O que esperar no dia", "/guia#atendimento")},
    {"id": "pos-exame", "title": "Pós-exame", "img": "/assets/img/exames/afr-640.webp",
     "h": "Resultados e próximos passos", "p": "A equipa indica como e quando recebe o resultado. Leve-o ao médico que pediu o exame para decidir os próximos passos.",
     "cta": ("Resultados e acompanhamento", "/guia#pos-exame")},
]

from datetime import date
import html

import streamlit as st


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Fluxograma Inteligente - Engenharia de Materiais UNIFEI",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# ESTILO - SOMENTE MODO CLARO
# ============================================================

st.markdown(
    """
<style>
:root {
    --caemt-color: #4A148C;
    --unifei-color: #0056B3;
    --background-color: #FFFFFF;
    --secondary-background: #F7F9FC;
    --text-color: #1F2937;
    --muted-color: #5F6B7A;
    --border-color: #D8DEE8;

    --suggestion-bg: #EAF7EE;
    --suggestion-border: #18864B;
    --suggestion-text: #126836;

    --blocked-bg: #FDECEC;
    --blocked-border: #C93434;
    --blocked-text: #A32121;

    --neutral-bg: #F7F9FC;
    --neutral-border: #D8DEE8;
    --neutral-text: #475467;
}

html,
body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    color-scheme: light !important;
}

[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"] {
    background-color: var(--background-color) !important;
    color: var(--text-color) !important;
}

[data-testid="stHeader"] {
    background-color: rgba(255, 255, 255, 0.96) !important;
}

#MainMenu,
footer {
    visibility: hidden;
}


/* ==========================================================
   CORREÇÃO MÍNIMA DOS WIDGETS NATIVOS DO STREAMLIT
   Mantém toda a lógica e as duas grades inalteradas.
   ========================================================== */

/* Reforça as variáveis de tema usadas pelo Streamlit. */
:root,
[data-testid="stAppViewContainer"] {
    --st-primary-color: #4A148C !important;
    --st-background-color: #FFFFFF !important;
    --st-secondary-background-color: #F7F9FC !important;
    --st-text-color: #1F2937 !important;
    color-scheme: light !important;
}

/* SELECTBOX: caixa fechada */
[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    color: #1F2937 !important;
    border: 1px solid #D8DEE8 !important;
    box-shadow: none !important;
}

[data-testid="stSelectbox"] div[data-baseweb="select"] > div:hover,
[data-testid="stSelectbox"] div[data-baseweb="select"] > div:focus-within {
    background-color: #FFFFFF !important;
    border-color: #98A2B3 !important;
}

[data-testid="stSelectbox"] div[data-baseweb="select"] span,
[data-testid="stSelectbox"] div[data-baseweb="select"] div,
[data-testid="stSelectbox"] div[data-baseweb="select"] p {
    color: #1F2937 !important;
}

[data-testid="stSelectbox"] div[data-baseweb="select"] svg {
    color: #1F2937 !important;
    fill: #1F2937 !important;
}

/* SELECTBOX: menu aberto */
div[data-baseweb="popover"],
div[data-baseweb="menu"],
ul[role="listbox"] {
    background-color: #FFFFFF !important;
    color: #1F2937 !important;
}

li[role="option"] {
    background-color: #FFFFFF !important;
    color: #1F2937 !important;
}

li[role="option"]:hover,
li[role="option"][aria-selected="true"] {
    background-color: #F1F4F8 !important;
    color: #1F2937 !important;
}

/* BOTÕES */
[data-testid="stButton"] button {
    background-color: #FFFFFF !important;
    color: #1F2937 !important;
    border: 1px solid #D8DEE8 !important;
    box-shadow: none !important;
}

[data-testid="stButton"] button:hover {
    background-color: #F7F9FC !important;
    color: #4A148C !important;
    border-color: #4A148C !important;
}

[data-testid="stButton"] button:disabled {
    background-color: #F7F9FC !important;
    color: #98A2B3 !important;
    border-color: #D8DEE8 !important;
    opacity: 1 !important;
}

/* CHECKBOXES: cobre as estruturas usadas por versões diferentes do Streamlit/BaseWeb. */
[data-testid="stCheckbox"] [role="checkbox"],
[data-testid="stCheckbox"] label[data-baseweb="checkbox"] > span:first-child,
[data-testid="stCheckbox"] label[data-baseweb="checkbox"] > div:first-child {
    background-color: #FFFFFF !important;
    border-color: #98A2B3 !important;
    color: #FFFFFF !important;
}

[data-testid="stCheckbox"] [role="checkbox"][aria-checked="true"],
[data-testid="stCheckbox"] label[data-baseweb="checkbox"]:has(input:checked) > span:first-child,
[data-testid="stCheckbox"] label[data-baseweb="checkbox"]:has(input:checked) > div:first-child {
    background-color: #4A148C !important;
    border-color: #4A148C !important;
}

[data-testid="stCheckbox"] input[type="checkbox"] {
    accent-color: #4A148C !important;
}

[data-testid="stCheckbox"] label,
[data-testid="stCheckbox"] label span,
[data-testid="stCheckbox"] label p {
    color: #1F2937 !important;
}

/* Campos BaseWeb genéricos, caso o Streamlit altere a implementação interna. */
[data-baseweb="input"] > div,
[data-baseweb="textarea"] > div {
    background-color: #FFFFFF !important;
    color: #1F2937 !important;
    border-color: #D8DEE8 !important;
}

input,
textarea {
    color-scheme: light !important;
}

.brand-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-size: 1.05rem;
    font-weight: 800;
    margin-bottom: -8px;
}

.brand-caemt {
    color: var(--caemt-color) !important;
}

.brand-unifei {
    color: var(--unifei-color) !important;
}

h1 {
    text-align: center;
    color: var(--text-color) !important;
    font-weight: 800;
    margin-top: 10px;
}

h2,
h3 {
    color: var(--text-color) !important;
}

.subtitle {
    text-align: center;
    color: var(--muted-color) !important;
    margin-top: -8px;
    margin-bottom: 22px;
}

.semester-badge {
    width: fit-content;
    margin: 0 auto 24px auto;
    padding: 7px 12px;
    border-radius: 999px;
    background: #EEF4FF;
    border: 1px solid #C9DBF5;
    color: var(--unifei-color) !important;
    font-size: 0.84rem;
    font-weight: 700;
}

[data-testid="stWidgetLabel"] p,
[data-testid="stCheckbox"] p {
    color: var(--text-color) !important;
}

[data-testid="stExpander"] {
    background-color: #FFFFFF !important;
    border: 1px solid var(--border-color) !important;
    border-radius: 9px !important;
    overflow: hidden;
}

[data-testid="stExpander"] summary {
    background-color: var(--secondary-background) !important;
}

[data-testid="stExpander"] summary:hover {
    background-color: #EEF2F7 !important;
}

[data-testid="stExpander"] summary p {
    color: var(--text-color) !important;
    font-weight: 700;
}

hr {
    border-color: var(--border-color) !important;
    opacity: 0.8;
}

.status-bar {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 28px;
    padding: 18px 24px;
    margin: 22px 0 26px 0;
    background: var(--secondary-background);
    border: 1px solid var(--border-color);
    border-radius: 10px;
}

.status-item {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 5px;
    min-width: 125px;
}

.status-label {
    color: var(--muted-color) !important;
    font-size: 0.70rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    text-align: center;
}

.status-value {
    color: var(--unifei-color) !important;
    font-size: 1.72rem;
    font-weight: 800;
    line-height: 1;
}

.status-divider {
    width: 1px;
    height: 42px;
    background-color: var(--border-color);
}

.sugestao-item,
.bloqueada-oferta,
.bloqueada-requisito {
    padding: 12px 15px;
    margin-bottom: 9px;
    border-radius: 7px;
    font-size: 0.94rem;
    line-height: 1.45;
}

.sugestao-item {
    background-color: var(--suggestion-bg);
    border: 1px solid #CAE9D5;
    border-left: 4px solid var(--suggestion-border);
    color: var(--suggestion-text) !important;
}

.sugestao-item strong {
    color: var(--suggestion-text) !important;
}

.bloqueada-oferta {
    background-color: var(--blocked-bg);
    border: 1px solid #F4CDCD;
    border-left: 4px solid var(--blocked-border);
    color: var(--blocked-text) !important;
}

.bloqueada-oferta strong,
.bloqueada-oferta span {
    color: var(--blocked-text) !important;
}

.bloqueada-requisito {
    background-color: var(--neutral-bg);
    border: 1px solid var(--neutral-border);
    border-left: 4px solid #98A2B3;
    color: var(--neutral-text) !important;
}

.bloqueada-requisito strong,
.bloqueada-requisito span {
    color: var(--neutral-text) !important;
}

.aviso-oferta,
.aviso-requisito {
    display: block;
    margin-top: 4px;
    font-size: 0.80rem;
    font-weight: 600;
}

.divisoria {
    margin: 24px 0 13px 0;
    padding-bottom: 7px;
    border-bottom: 1px solid var(--border-color);
    color: var(--muted-color) !important;
    font-size: 0.76rem;
    font-weight: 800;
    letter-spacing: 0.35px;
}

.small-note {
    color: var(--muted-color) !important;
    font-size: 0.82rem;
}

@media (max-width: 768px) {
    .brand-container {
        font-size: 0.92rem;
    }

    h1 {
        font-size: 1.9rem !important;
    }

    .subtitle {
        font-size: 0.91rem;
    }

    .status-bar {
        gap: 8px;
        padding: 14px 6px;
    }

    .status-item {
        min-width: 0;
        flex: 1;
    }

    .status-label {
        font-size: 0.57rem;
    }

    .status-value {
        font-size: 1.30rem;
    }

    .status-divider {
        height: 34px;
    }
}
</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# MATRIZES CURRICULARES
# ============================================================
#
# "oferta":
#   impar   -> 1º semestre do ano
#   par     -> 2º semestre do ano
#   regular -> pode ser ofertada nos dois semestres
#
# "req" contém os componentes que precisam estar concluídos
# para a disciplina aparecer como liberada no simulador.
# ============================================================

MATRIZ_2023 = {
    "1º Período": {
        "EMT101": {"nome": "Introdução à Engenharia de Materiais", "req": [], "oferta": "impar"},
        "CCO016": {"nome": "Fundamentos de Programação", "req": [], "oferta": "regular"},
        "IEPG21": {"nome": "Ciências Humanas e Sociais", "req": [], "oferta": "regular"},
        "MAT00A": {"nome": "Cálculo A", "req": [], "oferta": "regular"},
        "LET013": {"nome": "Escrita Acadêmica Científica", "req": [], "oferta": "regular"},
        "EMT102": {"nome": "Química Geral", "req": [], "oferta": "regular"},
        "DES005": {"nome": "Desenho Técnico Básico", "req": [], "oferta": "impar"},
    },
    "2º Período": {
        "EMT037T": {"nome": "Ciência dos Materiais I - Teórica", "req": ["EMT101", "EMT102"], "oferta": "par"},
        "EMT037P": {"nome": "Ciência dos Materiais I - Experimental", "req": ["EMT102"], "oferta": "par"},
        "FIS210": {"nome": "Física I", "req": ["MAT00A"], "oferta": "regular"},
        "FIS212": {"nome": "Física Experimental I", "req": [], "oferta": "regular"},
        "MAT00B": {"nome": "Cálculo B", "req": ["MAT00A"], "oferta": "regular"},
        "MAT00D": {"nome": "Equações Diferenciais A", "req": ["MAT00A"], "oferta": "regular"},
        "QUI212": {"nome": "Química Geral Experimental", "req": ["EMT102"], "oferta": "regular"},
        "EMT201": {"nome": "Química Inorgânica", "req": ["EMT102"], "oferta": "par"},
        "DES006": {"nome": "Desenho Técnico Auxiliado por Computador", "req": ["DES005"], "oferta": "par"},
    },
    "3º Período": {
        "EMT038": {"nome": "Ciência dos Materiais II", "req": ["EMT037T"], "oferta": "impar"},
        "FIS310": {"nome": "Física II A", "req": ["FIS210", "MAT00B"], "oferta": "regular"},
        "FIS320": {"nome": "Física II B", "req": ["FIS210", "MAT00B"], "oferta": "regular"},
        "EME303": {"nome": "Estática", "req": ["FIS210", "MAT00A"], "oferta": "regular"},
        "MAT00C": {"nome": "Cálculo C", "req": ["MAT00B"], "oferta": "regular"},
        "MAT00N": {"nome": "Cálculo Numérico", "req": ["MAT00A", "CCO016"], "oferta": "regular"},
        "EMT103": {"nome": "Físico-Química", "req": ["EMT102", "MAT00A"], "oferta": "impar"},
        "QUI022": {"nome": "Química Orgânica", "req": ["EMT102"], "oferta": "impar"},
    },
    "4º Período": {
        "EMT039": {"nome": "Termodinâmica", "req": ["EMT103"], "oferta": "par"},
        "FIS410": {"nome": "Física III", "req": ["FIS310", "MAT00C"], "oferta": "regular"},
        "EME405T": {"nome": "Resistência dos Materiais", "req": ["EME303"], "oferta": "regular"},
        "IEM405P": {"nome": "Resistência dos Materiais - Experimental", "req": ["EME303"], "oferta": "regular"},
        "MAT013": {"nome": "Probabilidade e Estatística", "req": ["MAT00B"], "oferta": "regular"},
        "MAT00E": {"nome": "Equações Diferenciais B", "req": ["MAT00D"], "oferta": "regular"},
        "EMT070": {"nome": "Materiais e Ambiente", "req": [], "oferta": "par"},
        "QUI105": {"nome": "Química Analítica", "req": ["QUI212"], "oferta": "par"},
        "QUI115": {"nome": "Química Analítica Experimental", "req": ["QUI212"], "oferta": "par"},
    },
    "5º Período": {
        "EMT502T": {"nome": "Materiais Cerâmicos", "req": ["EMT038", "EMT039"], "oferta": "impar"},
        "EMT502P": {"nome": "Materiais Cerâmicos - Experimental", "req": ["EMT038"], "oferta": "impar"},
        "EMT501": {"nome": "Metalurgia Física", "req": ["EMT038", "EMT039"], "oferta": "impar"},
        "EMT072": {"nome": "Produção de Ligas", "req": ["EMT038"], "oferta": "impar"},
        "FIS510": {"nome": "Física IV A", "req": ["FIS410"], "oferta": "regular"},
        "IEM002T": {"nome": "Fenômenos de Transporte II", "req": ["MAT00C", "MAT00E"], "oferta": "impar"},
        "IEM002P": {"nome": "Fenômenos de Transporte II - Experimental", "req": ["MAT00C", "MAT00E"], "oferta": "impar"},
        "EME505T": {"nome": "Resistência dos Materiais II", "req": ["EME405T"], "oferta": "impar"},
        "IEM505P": {"nome": "Resistência dos Materiais II - Experimental", "req": ["IEM405P"], "oferta": "impar"},
        "EMT503": {"nome": "Introdução aos Polímeros", "req": ["QUI022"], "oferta": "impar"},
    },
    "6º Período": {
        "EMT049T": {"nome": "Conformação de Metais e Cerâmicas", "req": ["EME405T", "EMT502T"], "oferta": "par"},
        "EMT049P": {"nome": "Conformação de Metais e Cerâmicas - Experimental", "req": ["EMT502P"], "oferta": "par"},
        "EMT069": {"nome": "Diagrama de Fases", "req": ["EMT039"], "oferta": "par"},
        "EMT071": {"nome": "Processos de Fabricação I", "req": ["EMT072"], "oferta": "par"},
        "EMT071P": {"nome": "Processos de Fabricação I - Experimental", "req": ["EMT072"], "oferta": "par"},
        "EMT601T": {"nome": "Comportamento Mecânico dos Materiais", "req": ["EME405T", "EMT038"], "oferta": "par"},
        "EME605T": {"nome": "Transferência de Calor I", "req": ["IEM002T"], "oferta": "par"},
        "EME605P": {"nome": "Transferência de Calor I - Experimental", "req": ["IEM002P"], "oferta": "par"},
        "EEB100": {"nome": "Eletricidade Básica", "req": ["FIS320"], "oferta": "regular"},
        "EMT047T": {"nome": "Estrutura e Propriedades dos Polímeros", "req": ["EMT503"], "oferta": "par"},
        "EMT063": {"nome": "Reologia", "req": ["EMT503"], "oferta": "par"},
    },
    "7º Período": {
        "EMT024T": {"nome": "Processamento de Materiais Cerâmicos", "req": ["EMT049T"], "oferta": "impar"},
        "EMT024P": {"nome": "Processamento de Materiais Cerâmicos - Experimental", "req": ["EMT049P"], "oferta": "impar"},
        "EMT025T": {"nome": "Técnicas de Caracterização de Materiais", "req": ["EMT501"], "oferta": "impar"},
        "EMT125P": {"nome": "Técnicas de Caracterização de Materiais - Experimental", "req": ["EMT501"], "oferta": "impar"},
        "EMT030": {"nome": "Fundamentos de Oxidação e Corrosão de Metais", "req": ["EMT039"], "oferta": "impar"},
        "EMT066T": {"nome": "Tratamento Térmico", "req": ["EMT069"], "oferta": "impar"},
        "EMT066P": {"nome": "Tratamento Térmico - Experimental", "req": ["EMT069"], "oferta": "impar"},
        "EMT147P": {"nome": "Estrutura e Propriedades dos Polímeros - Experimental", "req": ["EMT047T"], "oferta": "impar"},
        "EMT045T": {"nome": "Síntese de Polímeros", "req": ["QUI022"], "oferta": "impar"},
        "EMT701": {"nome": "Materiais Compósitos", "req": ["EMT038"], "oferta": "impar"},
    },
    "8º Período": {
        "EMT027T": {"nome": "Vidros e Vitrocerâmicos", "req": ["EMT024T"], "oferta": "par"},
        "EMT046": {"nome": "Processamento Aplicado de Materiais Cerâmicos", "req": ["EMT024T"], "oferta": "par"},
        "EMT067": {"nome": "Seleção de Materiais", "req": ["EMT025T"], "oferta": "par"},
        "EMT065T": {"nome": "Processos de Fabricação II", "req": ["EMT071"], "oferta": "par"},
        "EMT022T": {"nome": "Tratamento Superficial de Metais", "req": ["EMT030"], "oferta": "par"},
        "EP7006": {"nome": "Higiene e Segurança do Trabalho", "req": [], "oferta": "regular"},
        "EMT045P": {"nome": "Síntese de Polímeros - Experimental", "req": ["EMT045T"], "oferta": "par"},
        "EMT042T": {"nome": "Processamento de Polímeros", "req": ["EMT047T", "EMT045T"], "oferta": "par"},
        "EMT142P": {"nome": "Processamento de Polímeros - Experimental", "req": ["EMT047T"], "oferta": "par"},
        "EMT801P": {"nome": "Processamento de Compósitos - Experimental", "req": ["EMT701"], "oferta": "par"},
    },
    "9º Período": {
        "IEPG22": {"nome": "Administração Aplicada", "req": [], "oferta": "impar"},
        "IEPG10": {"nome": "Engenharia Econômica", "req": [], "oferta": "impar"},
        "EMT068": {"nome": "Aditivos e Reciclagem de Polímeros", "req": ["EMT042T"], "oferta": "impar"},
    },
    "10º Período": {
        "ESTEMT2023": {"nome": "Estágio Supervisionado", "req": [], "oferta": "regular"},
        "TCC1EMT2023": {"nome": "Trabalho de Conclusão de Curso I", "req": [], "oferta": "regular"},
        "TCC2EMT2023": {"nome": "Trabalho de Conclusão de Curso II", "req": ["TCC1EMT2023"], "oferta": "regular"},
    },
}


# Grade 2016 transcrita do código original enviado pelo usuário.
MATRIZ_2016 = {
    "1º Período": {
        "EMT101": {"nome": "Introdução à EMT", "req": [], "oferta": "impar"},
        "CCO016": {"nome": "Fundamentos de Programação", "req": [], "oferta": "regular"},
        "SOC002": {"nome": "Ciências Humanas e Sociais", "req": [], "oferta": "regular"},
        "MAT001": {"nome": "Cálculo I", "req": [], "oferta": "regular"},
        "MAT011": {"nome": "Geometria Analítica e Álgebra Linear", "req": [], "oferta": "regular"},
        "FIS104": {"nome": "Mecânica Geral", "req": [], "oferta": "impar"},
        "FIS114": {"nome": "Laboratório de Mecânica Geral", "req": [], "oferta": "impar"},
    },
    "2º Período": {
        "EMT037T": {"nome": "Ciência dos Materiais I - Teórica", "req": ["EMT101"], "oferta": "par"},
        "EMT037P": {"nome": "Ciência dos Materiais I - Experimental", "req": ["EMT101"], "oferta": "par"},
        "FIS203": {"nome": "Física Geral I", "req": ["MAT001"], "oferta": "regular"},
        "FIS213": {"nome": "Física Experimental I", "req": ["MAT001"], "oferta": "regular"},
        "MAT002": {"nome": "Cálculo II", "req": ["MAT001"], "oferta": "regular"},
        "EMT102": {"nome": "Química Geral", "req": [], "oferta": "par"},
        "BAC002": {"nome": "Língua Comum", "req": [], "oferta": "regular"},
    },
    "3º Período": {
        "EMT038": {"nome": "Ciência dos Materiais II", "req": ["EMT037T"], "oferta": "impar"},
        "FIS303": {"nome": "Estática", "req": ["FIS104"], "oferta": "regular"},
        "EME303": {"nome": "Resistência dos Materiais - Teórica", "req": ["FIS104"], "oferta": "regular"},
        "FIS403": {"nome": "Física Geral III", "req": ["FIS203", "MAT002"], "oferta": "regular"},
        "MAT003": {"nome": "Cálculo III", "req": ["MAT002"], "oferta": "regular"},
        "EMT103": {"nome": "Físico-Química", "req": ["EMT102", "MAT001"], "oferta": "impar"},
        "QUI022": {"nome": "Química Orgânica", "req": ["EMT102"], "oferta": "impar"},
    },
    "4º Período": {
        "EMT039": {"nome": "Termodinâmica", "req": ["EMT038", "EMT103"], "oferta": "par"},
        "EME405T": {"nome": "Resistência dos Materiais - Experimental", "req": ["EME303"], "oferta": "par"},
        "EME405P": {"nome": "Mecânica dos Sólidos - Teórica", "req": ["EME303"], "oferta": "par"},
        "MAT013": {"nome": "Probabilidade e Estatística", "req": ["MAT002"], "oferta": "regular"},
        "MAT021": {"nome": "Equações Diferenciais", "req": ["MAT003"], "oferta": "par"},
        "QUI105": {"nome": "Química Analítica", "req": ["EMT102"], "oferta": "par"},
        "QUI115": {"nome": "Química Analítica Experimental", "req": ["EMT102"], "oferta": "par"},
    },
    "5º Período": {
        "EMT002T": {"nome": "Materiais Cerâmicos - Teórica", "req": ["EMT039"], "oferta": "impar"},
        "EMT002P": {"nome": "Materiais Cerâmicos - Experimental", "req": ["EMT039"], "oferta": "impar"},
        "EME313T": {"nome": "Fenômenos de Transporte - Teórica", "req": ["MAT003", "MAT021"], "oferta": "impar"},
        "EME313P": {"nome": "Fenômenos de Transporte - Experimental", "req": ["MAT003"], "oferta": "impar"},
        "EME505T": {"nome": "Resistência dos Materiais II - Teórica", "req": ["EME405T"], "oferta": "impar"},
        "EME505P": {"nome": "Resistência dos Materiais II - Experimental", "req": ["EME405T"], "oferta": "impar"},
        "EMT072": {"nome": "Produção de Ligas", "req": ["EMT038"], "oferta": "impar"},
    },
    "6º Período": {
        "EMT049T": {"nome": "Conformação de Metais - Teórica", "req": ["EMT002T"], "oferta": "par"},
        "EMT049P": {"nome": "Conformação de Metais - Experimental", "req": ["EMT002P"], "oferta": "par"},
        "EMT412T": {"nome": "Estrutura e Propriedades Polímeros - Teórica", "req": ["QUI022"], "oferta": "par"},
        "EMT412P": {"nome": "Estrutura e Propriedades Polímeros - Experimental", "req": ["QUI022"], "oferta": "par"},
        "EME047T": {"nome": "Estrutura e Propriedades Polímeros - Teórica", "req": ["EMT039"], "oferta": "par"},
        "EMT147P": {"nome": "Estrutura e Propriedades Polímeros - Experimental", "req": ["EMT039"], "oferta": "par"},
        "EMT071": {"nome": "Processos de Fabricação I - Experimental", "req": ["EMT072"], "oferta": "par"},
        "EME039T": {"nome": "Fenômenos de Transporte II - Teórica", "req": ["EME313T"], "oferta": "par"},
        "EME039P": {"nome": "Fenômenos de Transporte II - Experimental", "req": ["EME313T"], "oferta": "par"},
    },
    "7º Período": {
        "EMT024T": {"nome": "Processamento de Materiais Cerâmicos - Teórica", "req": ["EMT049T"], "oferta": "impar"},
        "EMT024P": {"nome": "Processamento de Materiais Cerâmicos - Experimental", "req": ["EMT049P"], "oferta": "impar"},
        "EMT025T": {"nome": "Técnicas de Caracterização de Materiais", "req": ["EMT072"], "oferta": "impar"},
        "EMT125P": {"nome": "Técnicas de Caracterização - Experimental", "req": ["EMT072"], "oferta": "impar"},
        "EMT030": {"nome": "Fundamentos de Oxidação e Corrosão", "req": ["EMT039"], "oferta": "impar"},
        "EMT066T": {"nome": "Tratamento Térmico - Teórica", "req": ["EMT039"], "oferta": "impar"},
        "EMT066P": {"nome": "Tratamento Térmico - Experimental", "req": ["EMT039"], "oferta": "impar"},
        "EAM002": {"nome": "Ciência de Materiais", "req": ["EMT038"], "oferta": "regular"},
        "EMT067": {"nome": "Seleção de Materiais", "req": ["EMT038"], "oferta": "impar"},
    },
    "8º Período": {
        "EMT027T": {"nome": "Vidros e Vitrocerâmicos", "req": ["EMT002T"], "oferta": "par"},
        "EMT046": {"nome": "Processamento de Materiais Cerâmicos II", "req": ["EMT024T"], "oferta": "par"},
        "EMT065T": {"nome": "Processos de Fabricação II", "req": ["EMT071"], "oferta": "par"},
        "EMT022T": {"nome": "Tratamento Superficial de Metais", "req": ["EMT030"], "oferta": "par"},
        "EMT042T": {"nome": "Processamento de Polímeros - Teórica", "req": ["EMT047T", "EMT412T"], "oferta": "par"},
        "EMT142P": {"nome": "Processamento de Polímeros - Experimental", "req": ["EMT047T"], "oferta": "par"},
        "EPR220": {"nome": "Higiene e Segurança do Trabalho", "req": [], "oferta": "regular"},
        "EPR002": {"nome": "Organização Industrial e Administração", "req": [], "oferta": "regular"},
    },
    "9º Período": {
        "IEPG01": {"nome": "Administração e Economia", "req": [], "oferta": "impar"},
        "TCC001": {"nome": "Trabalho de Conclusão de Curso I", "req": [], "oferta": "regular"},
    },
    "10º Período": {
        "EST001": {"nome": "Estágio Supervisionado", "req": [], "oferta": "regular"},
        "TCC002": {"nome": "Trabalho de Conclusão de Curso II", "req": ["TCC001"], "oferta": "regular"},
    },
}

MATRIZES = {
    "2023": MATRIZ_2023,
    "2016": MATRIZ_2016,
}


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================


def todas_as_disciplinas(matriz):
    """Retorna um dicionário código -> dados para a matriz selecionada."""
    resultado = {}
    for periodo, materias in matriz.items():
        for codigo, dados in materias.items():
            resultado[codigo] = {**dados, "periodo": periodo}
    return resultado


def proximo_semestre_referencia(hoje=None):
    """Retorna (oferta, texto) para o próximo semestre civil."""
    hoje = hoje or date.today()
    if hoje.month <= 6:
        return "par", f"2º semestre de {hoje.year}"
    return "impar", f"1º semestre de {hoje.year + 1}"


def chave_checkbox(grade, codigo):
    return f"concluida_{grade}_{codigo}"


def inicializar_estado(grade, disciplinas):
    for codigo in disciplinas:
        chave = chave_checkbox(grade, codigo)
        if chave not in st.session_state:
            st.session_state[chave] = False


def disciplinas_concluidas(grade, disciplinas):
    return {
        codigo
        for codigo in disciplinas
        if st.session_state.get(chave_checkbox(grade, codigo), False)
    }


def marcar_periodo(grade, matriz, periodo, valor):
    for codigo in matriz[periodo]:
        st.session_state[chave_checkbox(grade, codigo)] = valor


def limpar_todas(grade, disciplinas):
    for codigo in disciplinas:
        st.session_state[chave_checkbox(grade, codigo)] = False


def escapar(texto):
    return html.escape(str(texto))


def requisito_esta_concluido(grade, requisito, concluidas):
    """
    Mantém os dados da grade 2016 exatamente como no código original.

    No código original, a disciplina EME047T aparece no 6º período, mas
    EMT042T/EMT142P usam EMT047T como pré-requisito. Para que essa
    inconsistência de código não deixe duas disciplinas permanentemente
    bloqueadas, EME047T é aceito como equivalente a EMT047T apenas na
    verificação de pré-requisitos da grade 2016.
    """
    if requisito in concluidas:
        return True
    if grade == "2016" and requisito == "EMT047T" and "EME047T" in concluidas:
        return True
    return False


def nome_requisito(grade, requisito, disciplinas):
    if requisito in disciplinas:
        return requisito
    if grade == "2016" and requisito == "EMT047T" and "EME047T" in disciplinas:
        return "EME047T"
    return requisito


def renderizar_disponivel(codigo, dados):
    st.markdown(
        '<div class="sugestao-item">'
        f'<strong>{escapar(codigo)}</strong> - {escapar(dados["nome"])}'
        '</div>',
        unsafe_allow_html=True,
    )


def renderizar_nao_ofertada(codigo, dados, semestre_destino):
    if dados["oferta"] == "impar":
        oferta_texto = "Componente previsto para o 1º semestre do ano."
    else:
        oferta_texto = "Componente previsto para o 2º semestre do ano."

    st.markdown(
        '<div class="bloqueada-oferta">'
        f'<strong>{escapar(codigo)}</strong> - {escapar(dados["nome"])}'
        f'<span class="aviso-oferta">{escapar(oferta_texto)} Destino atual: {escapar(semestre_destino)}.</span>'
        '</div>',
        unsafe_allow_html=True,
    )


def renderizar_bloqueada(codigo, dados, faltantes):
    faltantes_html = ", ".join(escapar(item) for item in faltantes)
    st.markdown(
        '<div class="bloqueada-requisito">'
        f'<strong>{escapar(codigo)}</strong> - {escapar(dados["nome"])}'
        f'<span class="aviso-requisito">Falta concluir: {faltantes_html}</span>'
        '</div>',
        unsafe_allow_html=True,
    )


# ============================================================
# CABEÇALHO
# ============================================================

st.markdown(
    '<div class="brand-container">'
    '<div class="brand-caemt">CAEMT</div>'
    '<div class="brand-unifei">UNIFEI</div>'
    '</div>',
    unsafe_allow_html=True,
)

st.markdown("<h1>Fluxograma Inteligente</h1>", unsafe_allow_html=True)

st.markdown(
    '<p class="subtitle">'
    'Escolha a matriz curricular e marque apenas as disciplinas que você já concluiu.'
    '</p>',
    unsafe_allow_html=True,
)


# ============================================================
# SELEÇÃO DA MATRIZ
# ============================================================

col_grade, _ = st.columns([1.2, 2.8])

with col_grade:
    grade_versao = st.selectbox(
        "Grade curricular:",
        options=["2023", "2016"],
        index=0,
    )


MATRIZ_ATUAL = MATRIZES[grade_versao]
DISCIPLINAS = todas_as_disciplinas(MATRIZ_ATUAL)
inicializar_estado(grade_versao, DISCIPLINAS)

semestre_oferta, semestre_texto = proximo_semestre_referencia()

st.markdown(
    f'<div class="semester-badge">Grade {escapar(grade_versao)} · Planejamento automático: {escapar(semestre_texto)}</div>',
    unsafe_allow_html=True,
)

if grade_versao == "2016":
    st.caption(
        "Nota técnica: a grade 2016 foi incorporada a partir do código original. "
        "Nesse código, EME047T aparece na lista de disciplinas enquanto EMT047T "
        "é citado como pré-requisito de duas matérias; o simulador trata esses "
        "códigos como equivalentes apenas nessa verificação."
    )


# ============================================================
# CONTROLES RÁPIDOS
# ============================================================

controle1, espaco = st.columns([1, 5])

with controle1:
    if st.button(
        "Limpar seleção",
        key=f"limpar_{grade_versao}",
        use_container_width=True,
    ):
        limpar_todas(grade_versao, DISCIPLINAS)
        st.rerun()


st.markdown("---")


# ============================================================
# LAYOUT PRINCIPAL
# ============================================================

col_esquerda, col_direita = st.columns([1.18, 0.82], gap="large")


# ============================================================
# COLUNA ESQUERDA - TODAS AS DISCIPLINAS
# ============================================================

with col_esquerda:
    st.markdown("### 1. Disciplinas concluídas")
    st.caption("Abra os períodos e marque somente o que já foi concluído.")

    for periodo, materias in MATRIZ_ATUAL.items():
        concluidas_periodo = sum(
            1
            for codigo in materias
            if st.session_state.get(chave_checkbox(grade_versao, codigo), False)
        )

        titulo = f"{periodo} - {concluidas_periodo}/{len(materias)} concluídas"

        with st.expander(
            titulo,
            expanded=periodo in {"1º Período", "2º Período"},
        ):
            botao1, botao2 = st.columns(2)

            with botao1:
                if st.button(
                    "Marcar período inteiro",
                    key=f"marcar_{grade_versao}_{periodo}",
                    use_container_width=True,
                ):
                    marcar_periodo(grade_versao, MATRIZ_ATUAL, periodo, True)
                    st.rerun()

            with botao2:
                if st.button(
                    "Desmarcar período",
                    key=f"desmarcar_{grade_versao}_{periodo}",
                    use_container_width=True,
                ):
                    marcar_periodo(grade_versao, MATRIZ_ATUAL, periodo, False)
                    st.rerun()

            for codigo, dados in materias.items():
                st.checkbox(
                    f"**{codigo}** - {dados['nome']}",
                    key=chave_checkbox(grade_versao, codigo),
                )


# ============================================================
# CÁLCULOS DO ESTADO ATUAL
# ============================================================

concluidas = disciplinas_concluidas(grade_versao, DISCIPLINAS)
total_materias = len(DISCIPLINAS)
total_concluidas = len(concluidas)
progresso = round((total_concluidas / total_materias) * 100) if total_materias else 0

liberadas = []
liberadas_nao_ofertadas = []
bloqueadas = []

for codigo, dados in DISCIPLINAS.items():
    if codigo in concluidas:
        continue

    faltantes = [
        nome_requisito(grade_versao, req, DISCIPLINAS)
        for req in dados["req"]
        if not requisito_esta_concluido(grade_versao, req, concluidas)
    ]

    if faltantes:
        bloqueadas.append((codigo, dados, faltantes))
        continue

    if dados["oferta"] == "regular" or dados["oferta"] == semestre_oferta:
        liberadas.append((codigo, dados))
    else:
        liberadas_nao_ofertadas.append((codigo, dados))


# ============================================================
# BARRA DE STATUS
# ============================================================

st.markdown(
    '<div class="status-bar">'
    '<div class="status-item">'
    '<div class="status-label">Concluídas</div>'
    f'<div class="status-value">{total_concluidas}</div>'
    '</div>'
    '<div class="status-divider"></div>'
    '<div class="status-item">'
    '<div class="status-label">Total da grade</div>'
    f'<div class="status-value">{total_materias}</div>'
    '</div>'
    '<div class="status-divider"></div>'
    '<div class="status-item">'
    '<div class="status-label">Progresso</div>'
    f'<div class="status-value">{progresso}%</div>'
    '</div>'
    '</div>',
    unsafe_allow_html=True,
)


# ============================================================
# COLUNA DIREITA - RESULTADOS
# ============================================================

with col_direita:
    st.markdown("### 2. Situação para o próximo semestre")
    st.caption(f"Grade {grade_versao} · Análise para {semestre_texto}.")

    if liberadas:
        st.markdown(
            '<div class="divisoria">DISCIPLINAS LIBERADAS</div>',
            unsafe_allow_html=True,
        )
        for codigo, dados in liberadas:
            renderizar_disponivel(codigo, dados)
    else:
        st.info("Nenhuma disciplina foi identificada como liberada neste momento.")

    if liberadas_nao_ofertadas:
        st.markdown(
            '<div class="divisoria">LIBERADAS, MAS FORA DO SEMESTRE DE OFERTA</div>',
            unsafe_allow_html=True,
        )
        for codigo, dados in liberadas_nao_ofertadas:
            renderizar_nao_ofertada(codigo, dados, semestre_texto)

    if bloqueadas:
        with st.expander(f"Ver disciplinas ainda bloqueadas ({len(bloqueadas)})"):
            for codigo, dados, faltantes in bloqueadas:
                renderizar_bloqueada(codigo, dados, faltantes)


# ============================================================
# RODAPÉ
# ============================================================

st.markdown("---")
st.caption(
    "Ferramenta independente e não oficial. A disponibilidade real de turmas, "
    "regras acadêmicas e eventuais alterações curriculares devem ser conferidas no SIGAA/UNIFEI."
)

import streamlit as st


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Simulador de Matrícula - Engenharia de Materiais UNIFEI",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# ESTILIZAÇÃO — SOMENTE MODO CLARO
# ============================================================

st.markdown(
    """
<style>

/* ==========================================================
   PALETA
   ========================================================== */

:root {
    --caemt-color: #4A148C;
    --unifei-color: #0056B3;

    --background-color: #FFFFFF;
    --secondary-background: #F7F9FC;

    --text-color: #1F2937;
    --muted-color: #5F6B7A;

    --border-color: #D8DEE8;

    /* Verde — disciplina disponível */
    --suggestion-bg: #EAF7EE;
    --suggestion-border: #18864B;
    --suggestion-text: #126836;

    /* Vermelho — liberada, mas não ofertada */
    --blocked-bg: #FDECEC;
    --blocked-border: #C93434;
    --blocked-text: #A32121;
}


/* ==========================================================
   MODO CLARO
   ========================================================== */

html,
body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"] {
    color-scheme: light !important;
}

[data-testid="stAppViewContainer"] {
    background-color: var(--background-color) !important;
    color: var(--text-color) !important;
}

[data-testid="stMain"] {
    background-color: var(--background-color) !important;
}

[data-testid="stMainBlockContainer"] {
    background-color: var(--background-color) !important;
}

[data-testid="stHeader"] {
    background-color: rgba(255, 255, 255, 0.95) !important;
}


/* ==========================================================
   MENU / ELEMENTOS DO STREAMLIT
   ========================================================== */

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}


/* ==========================================================
   CABEÇALHO DE MARCA
   ========================================================== */

.brand-container {
    display: flex;
    justify-content: space-between;
    align-items: center;

    font-size: 1.1rem;
    font-weight: 800;

    margin-bottom: -8px;
}

.brand-caemt {
    color: var(--caemt-color) !important;
}

.brand-unifei {
    color: var(--unifei-color) !important;
}


/* ==========================================================
   TÍTULOS
   ========================================================== */

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

    margin-top: -7px;
    margin-bottom: 30px;

    font-size: 1rem;
}


/* ==========================================================
   LABELS
   ========================================================== */

[data-testid="stWidgetLabel"] p {
    color: var(--text-color) !important;
    font-weight: 600;
}


/* ==========================================================
   SELECTBOX
   ========================================================== */

div[data-baseweb="select"] > div {
    background-color: #FFFFFF !important;

    color: var(--text-color) !important;

    border-color: var(--border-color) !important;
}

div[data-baseweb="select"] span {
    color: var(--text-color) !important;
}

div[data-baseweb="select"] svg {
    fill: var(--text-color) !important;
}


/* Menu aberto do selectbox */

div[data-baseweb="popover"] {
    color-scheme: light !important;
}

div[data-baseweb="popover"] ul {
    background-color: #FFFFFF !important;
}

div[data-baseweb="popover"] li {
    background-color: #FFFFFF !important;

    color: var(--text-color) !important;
}

div[data-baseweb="popover"] li:hover {
    background-color: #F1F4F8 !important;
}


/* ==========================================================
   CHECKBOX
   ========================================================== */

[data-testid="stCheckbox"] p {
    color: var(--text-color) !important;
}


/* ==========================================================
   EXPANDERS
   ========================================================== */

[data-testid="stExpander"] {
    background-color: #FFFFFF !important;

    border: 1px solid var(--border-color) !important;

    border-radius: 8px !important;

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

    font-weight: 650;
}


/* ==========================================================
   DIVISORES
   ========================================================== */

hr {
    border-color: var(--border-color) !important;

    opacity: 0.8;
}


/* ==========================================================
   BARRA DE STATUS
   ========================================================== */

.status-bar {
    display: flex;

    justify-content: center;
    align-items: center;

    gap: 30px;

    padding: 18px 24px;

    margin: 24px 0;

    background-color: var(--secondary-background);

    border: 1px solid var(--border-color);

    border-radius: 10px;

    box-shadow:
        0 1px 2px rgba(16, 24, 40, 0.04),
        0 2px 6px rgba(16, 24, 40, 0.03);
}

.status-item {
    display: flex;

    flex-direction: column;

    justify-content: center;
    align-items: center;

    gap: 6px;

    min-width: 130px;
}

.status-label {
    color: var(--muted-color) !important;

    font-size: 0.72rem;

    font-weight: 700;

    letter-spacing: 0.5px;

    text-transform: uppercase;

    text-align: center;
}

.status-value {
    color: var(--unifei-color) !important;

    font-size: 1.75rem;

    font-weight: 800;

    line-height: 1;
}

.status-divider {
    width: 1px;

    height: 42px;

    background-color: var(--border-color);
}


/* ==========================================================
   MATÉRIAS DISPONÍVEIS
   ========================================================== */

.sugestao-item {
    padding: 13px 16px;

    margin-bottom: 10px;

    background-color: var(--suggestion-bg);

    border: 1px solid #CAE9D5;

    border-left: 4px solid var(--suggestion-border);

    border-radius: 7px;

    color: var(--suggestion-text) !important;

    font-size: 0.95rem;

    line-height: 1.45;
}

.sugestao-item strong {
    color: var(--suggestion-text) !important;

    font-weight: 800;
}


/* ==========================================================
   MATÉRIAS NÃO OFERTADAS
   ========================================================== */

.bloqueada-oferta {
    background-color: var(--blocked-bg);

    border: 1px solid #F4CDCD;

    border-left: 4px solid var(--blocked-border);

    color: var(--blocked-text) !important;
}

.bloqueada-oferta strong {
    color: var(--blocked-text) !important;
}

.aviso-oferta {
    display: block;

    margin-top: 4px;

    color: var(--blocked-text) !important;

    font-size: 0.82rem;

    font-weight: 600;
}


/* ==========================================================
   DIVISÓRIA DE MATÉRIAS NÃO OFERTADAS
   ========================================================== */

.divisoria {
    margin: 25px 0 15px 0;

    padding-bottom: 7px;

    border-bottom: 1px solid var(--border-color);

    color: var(--muted-color) !important;

    font-size: 0.78rem;

    font-weight: 700;

    letter-spacing: 0.3px;
}


/* ==========================================================
   ALERTAS
   ========================================================== */

[data-testid="stAlert"] {
    color-scheme: light !important;
}


/* ==========================================================
   CELULAR
   ========================================================== */

@media (max-width: 768px) {

    .brand-container {
        font-size: 0.95rem;
    }

    h1 {
        font-size: 2rem !important;
    }

    .subtitle {
        font-size: 0.92rem;
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
        font-size: 0.59rem;
    }

    .status-value {
        font-size: 1.35rem;
    }

    .status-divider {
        height: 35px;
    }

}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# MATRIZES CURRICULARES
# ============================================================

matrizes = {

    # ========================================================
    # MATRIZ 2023
    # ========================================================

    "2023": {

        "1º Período": {

            "EMT101": {
                "nome": "Introdução à Engenharia de Materiais",
                "req": [],
                "oferta": "impar"
            },

            "CCO016": {
                "nome": "Fundamentos de Programação",
                "req": [],
                "oferta": "regular"
            },

            "IEPG21": {
                "nome": "Ciências Humanas e Sociais",
                "req": [],
                "oferta": "regular"
            },

            "MAT00A": {
                "nome": "Cálculo A",
                "req": [],
                "oferta": "regular"
            },

            "LET013": {
                "nome": "Escrita Acadêmica Científica",
                "req": [],
                "oferta": "regular"
            },

            "EMT102": {
                "nome": "Química Geral",
                "req": [],
                "oferta": "regular"
            },

            "DES005": {
                "nome": "Desenho Técnico Básico",
                "req": [],
                "oferta": "impar"
            }

        },


        "2º Período": {

            "EMT037T": {
                "nome": "Ciência dos Materiais I - Teórica",
                "req": ["EMT101", "EMT102"],
                "oferta": "par"
            },

            "EMT037P": {
                "nome": "Ciência dos Materiais I - Experimental",
                "req": ["EMT102"],
                "oferta": "par"
            },

            "FIS210": {
                "nome": "Física I",
                "req": ["MAT00A"],
                "oferta": "regular"
            },

            "FIS212": {
                "nome": "Física Experimental I",
                "req": [],
                "oferta": "regular"
            },

            "MAT00B": {
                "nome": "Cálculo B",
                "req": ["MAT00A"],
                "oferta": "regular"
            },

            "MAT00D": {
                "nome": "Equações Diferenciais A",
                "req": ["MAT00A"],
                "oferta": "regular"
            },

            "QUI212": {
                "nome": "Química Geral Experimental",
                "req": ["EMT102"],
                "oferta": "regular"
            },

            "EMT201": {
                "nome": "Química Inorgânica",
                "req": ["EMT102"],
                "oferta": "par"
            },

            "DES006": {
                "nome": "Desenho Técnico Auxiliado por Computador",
                "req": ["DES005"],
                "oferta": "par"
            }

        },


        "3º Período": {

            "EMT038": {
                "nome": "Ciência dos Materiais II",
                "req": ["EMT037T"],
                "oferta": "impar"
            },

            "FIS310": {
                "nome": "Física II A",
                "req": ["FIS210", "MAT00B"],
                "oferta": "regular"
            },

            "FIS320": {
                "nome": "Física II B",
                "req": ["FIS210", "MAT00B"],
                "oferta": "regular"
            },

            "EME303": {
                "nome": "Estática",
                "req": ["FIS210", "MAT00A"],
                "oferta": "regular"
            },

            "MAT00C": {
                "nome": "Cálculo C",
                "req": ["MAT00B"],
                "oferta": "regular"
            },

            "MAT00N": {
                "nome": "Cálculo Numérico",
                "req": ["MAT00A", "CCO016"],
                "oferta": "regular"
            },

            "EMT103": {
                "nome": "Físico-Química",
                "req": ["EMT102", "MAT00A"],
                "oferta": "impar"
            },

            "QUI022": {
                "nome": "Química Orgânica",
                "req": ["EMT102"],
                "oferta": "impar"
            }

        },


        "4º Período": {

            "EMT039": {
                "nome": "Termodinâmica",
                "req": ["EMT103"],
                "oferta": "par"
            },

            "FIS410": {
                "nome": "Física III",
                "req": ["FIS310", "MAT00C"],
                "oferta": "regular"
            },

            "EME405T": {
                "nome": "Resistência dos Materiais - Teórica",
                "req": ["EME303"],
                "oferta": "regular"
            },

            "IEM405P": {
                "nome": "Resistência dos Materiais - Experimental",
                "req": ["EME303"],
                "oferta": "regular"
            },

            "MAT013": {
                "nome": "Probabilidade e Estatística",
                "req": ["MAT00B"],
                "oferta": "regular"
            },

            "MAT00E": {
                "nome": "Equações Diferenciais B",
                "req": ["MAT00D"],
                "oferta": "regular"
            },

            "QUI105": {
                "nome": "Química Analítica",
                "req": ["QUI212"],
                "oferta": "par"
            },

            "QUI115": {
                "nome": "Química Analítica Experimental",
                "req": ["QUI212"],
                "oferta": "par"
            }

        },


        "5º Período": {

            "EMT502T": {
                "nome": "Materiais Cerâmicos - Teórica",
                "req": ["EMT038", "EMT039"],
                "oferta": "impar"
            },

            "EMT502P": {
                "nome": "Materiais Cerâmicos - Experimental",
                "req": ["EMT038"],
                "oferta": "impar"
            },

            "EMT501": {
                "nome": "Metalurgia Física",
                "req": ["EMT038", "EMT039"],
                "oferta": "impar"
            },

            "EMT072": {
                "nome": "Produção de Ligas",
                "req": ["EMT038"],
                "oferta": "impar"
            },

            "FIS510": {
                "nome": "Física IV A",
                "req": ["FIS410"],
                "oferta": "regular"
            },

            "IEM002T": {
                "nome": "Fenômenos de Transporte II - Teórica",
                "req": ["MAT00C", "MAT00E"],
                "oferta": "impar"
            },

            "IEM002P": {
                "nome": "Fenômenos de Transporte II - Experimental",
                "req": ["MAT00C", "MAT00E"],
                "oferta": "impar"
            },

            "EME505T": {
                "nome": "Resistência dos Materiais II - Teórica",
                "req": ["EME405T"],
                "oferta": "impar"
            },

            "IEM505P": {
                "nome": "Resistência dos Materiais II - Experimental",
                "req": ["IEM405P"],
                "oferta": "impar"
            },

            "EMT503": {
                "nome": "Introdução aos Polímeros",
                "req": ["QUI022"],
                "oferta": "impar"
            }

        },


        "6º Período": {

            "EMT049T": {
                "nome": "Conformação de Metais e Cerâmicas - Teórica",
                "req": ["EME405T", "EMT502T"],
                "oferta": "par"
            },

            "EMT049P": {
                "nome": "Conformação de Metais e Cerâmicas - Experimental",
                "req": ["EMT502P"],
                "oferta": "par"
            },

            "EMT069": {
                "nome": "Diagrama de Fases",
                "req": ["EMT039"],
                "oferta": "par"
            },

            "EMT071": {
                "nome": "Processos de Fabricação I - Teórica",
                "req": ["EMT072"],
                "oferta": "par"
            },

            "EMT071P": {
                "nome": "Processos de Fabricação I - Experimental",
                "req": ["EMT072"],
                "oferta": "par"
            },

            "EMT601T": {
                "nome": "Comportamento Mecânico dos Materiais",
                "req": ["EME405T", "EMT038"],
                "oferta": "par"
            },

            "EME605T": {
                "nome": "Transferência de Calor I - Teórica",
                "req": ["IEM002T"],
                "oferta": "par"
            },

            "EME605P": {
                "nome": "Transferência de Calor I - Experimental",
                "req": ["IEM002P"],
                "oferta": "par"
            },

            "EMT047T": {
                "nome": "Estrutura e Propriedades dos Polímeros",
                "req": ["EMT503"],
                "oferta": "par"
            },

            "EMT063": {
                "nome": "Reologia",
                "req": ["EMT503"],
                "oferta": "par"
            }

        },


        "7º Período": {

            "EMT024T": {
                "nome": "Processamento de Materiais Cerâmicos - Teórica",
                "req": ["EMT049T"],
                "oferta": "impar"
            },

            "EMT024P": {
                "nome": "Processamento de Materiais Cerâmicos - Experimental",
                "req": ["EMT049P"],
                "oferta": "impar"
            },

            "EMT025T": {
                "nome": "Técnicas de Caracterização de Materiais",
                "req": ["EMT501"],
                "oferta": "impar"
            },

            "EMT125P": {
                "nome": "Técnicas de Caracterização - Experimental",
                "req": ["EMT501"],
                "oferta": "impar"
            },

            "EMT030": {
                "nome": "Fundamentos de Oxidação e Corrosão",
                "req": ["EMT039"],
                "oferta": "impar"
            },

            "EMT066T": {
                "nome": "Tratamento Térmico - Teórica",
                "req": ["EMT069"],
                "oferta": "impar"
            },

            "EMT066P": {
                "nome": "Tratamento Térmico - Experimental",
                "req": ["EMT069"],
                "oferta": "impar"
            },

            "EEB100": {
                "nome": "Eletricidade Básica",
                "req": ["FIS320"],
                "oferta": "regular"
            },

            "EMT147P": {
                "nome": "Estrutura e Propriedades dos Polímeros - Experimental",
                "req": ["EMT047T"],
                "oferta": "impar"
            },

            "EMT045T": {
                "nome": "Síntese de Polímeros - Teórica",
                "req": ["QUI022"],
                "oferta": "impar"
            },

            "EMT701": {
                "nome": "Materiais Compósitos",
                "req": ["EMT038"],
                "oferta": "impar"
            }

        },


        "8º Período": {

            "EMT027T": {
                "nome": "Vidros e Vitrocerâmicos",
                "req": ["EMT502T"],
                "oferta": "par"
            },

            "EMT046": {
                "nome": "Processamento de Materiais Cerâmicos II",
                "req": ["EMT024T"],
                "oferta": "par"
            },

            "EMT065T": {
                "nome": "Processos de Fabricação II",
                "req": ["EMT071"],
                "oferta": "par"
            },

            "EMT022T": {
                "nome": "Tratamento Superficial de Metais",
                "req": ["EMT030"],
                "oferta": "par"
            },

            "EMT042T": {
                "nome": "Processamento de Polímeros - Teórica",
                "req": ["EMT047T", "EMT412T"],
                "oferta": "par"
            },

            "EMT142P": {
                "nome": "Processamento de Polímeros - Experimental",
                "req": ["EMT047T"],
                "oferta": "par"
            },

            "EPR220": {
                "nome": "Higiene e Segurança do Trabalho",
                "req": [],
                "oferta": "regular"
            },

            "EPR002": {
                "nome": "Organização Industrial e Administração",
                "req": [],
                "oferta": "regular"
            }

        },


        "9º Período": {

            "IEPG22": {
                "nome": "Administração Aplicada",
                "req": [],
                "oferta": "impar"
            },

            "IEPG10": {
                "nome": "Engenharia Econômica",
                "req": [],
                "oferta": "impar"
            },

            "TCC1EMT2023": {
                "nome": "Trabalho de Conclusão de Curso I",
                "req": [],
                "oferta": "regular"
            },

            "EMT068": {
                "nome": "Aditivos e Reciclagem de Polímeros",
                "req": ["EMT042T"],
                "oferta": "impar"
            }

        },


        "10º Período": {

            "ESTEMT2023": {
                "nome": "Estágio Supervisionado",
                "req": [],
                "oferta": "regular"
            },

            "TCC2EMT2023": {
                "nome": "Trabalho de Conclusão de Curso II",
                "req": ["TCC1EMT2023"],
                "oferta": "regular"
            }

        }

    },


    # ========================================================
    # MATRIZ 2016
    # ========================================================

    "2016": {

        "1º Período": {

            "EMT101": {
                "nome": "Introdução à EMT",
                "req": [],
                "oferta": "impar"
            },

            "CCO016": {
                "nome": "Fundamentos de Programação",
                "req": [],
                "oferta": "regular"
            },

            "SOC002": {
                "nome": "Ciências Humanas e Sociais",
                "req": [],
                "oferta": "regular"
            },

            "MAT001": {
                "nome": "Cálculo I",
                "req": [],
                "oferta": "regular"
            },

            "MAT011": {
                "nome": "Geometria Analítica e Álgebra Linear",
                "req": [],
                "oferta": "regular"
            },

            "FIS104": {
                "nome": "Mecânica Geral",
                "req": [],
                "oferta": "impar"
            },

            "FIS114": {
                "nome": "Laboratório de Mecânica Geral",
                "req": [],
                "oferta": "impar"
            }

        },


        "2º Período": {

            "EMT037T": {
                "nome": "Ciência dos Materiais I - Teórica",
                "req": ["EMT101"],
                "oferta": "par"
            },

            "EMT037P": {
                "nome": "Ciência dos Materiais I - Experimental",
                "req": ["EMT101"],
                "oferta": "par"
            },

            "FIS203": {
                "nome": "Física Geral I",
                "req": ["MAT001"],
                "oferta": "regular"
            },

            "FIS213": {
                "nome": "Física Experimental I",
                "req": ["MAT001"],
                "oferta": "regular"
            },

            "MAT002": {
                "nome": "Cálculo II",
                "req": ["MAT001"],
                "oferta": "regular"
            },

            "EMT102": {
                "nome": "Química Geral",
                "req": [],
                "oferta": "par"
            },

            "BAC002": {
                "nome": "Língua Comum",
                "req": [],
                "oferta": "regular"
            }

        },


        "3º Período": {

            "EMT038": {
                "nome": "Ciência dos Materiais II",
                "req": ["EMT037T"],
                "oferta": "impar"
            },

            "FIS303": {
                "nome": "Estática",
                "req": ["FIS104"],
                "oferta": "regular"
            },

            "EME303": {
                "nome": "Resistência dos Materiais - Teórica",
                "req": ["FIS104"],
                "oferta": "regular"
            },

            "FIS403": {
                "nome": "Física Geral III",
                "req": ["FIS203", "MAT002"],
                "oferta": "regular"
            },

            "MAT003": {
                "nome": "Cálculo III",
                "req": ["MAT002"],
                "oferta": "regular"
            },

            "EMT103": {
                "nome": "Físico-Química",
                "req": ["EMT102", "MAT001"],
                "oferta": "impar"
            },

            "QUI022": {
                "nome": "Química Orgânica",
                "req": ["EMT102"],
                "oferta": "impar"
            }

        },


        "4º Período": {

            "EMT039": {
                "nome": "Termodinâmica",
                "req": ["EMT038", "EMT103"],
                "oferta": "par"
            },

            "EME405T": {
                "nome": "Resistência dos Materiais - Experimental",
                "req": ["EME303"],
                "oferta": "par"
            },

            "EME405P": {
                "nome": "Mecânica dos Sólidos - Teórica",
                "req": ["EME303"],
                "oferta": "par"
            },

            "MAT013": {
                "nome": "Probabilidade e Estatística",
                "req": ["MAT002"],
                "oferta": "regular"
            },

            "MAT021": {
                "nome": "Equações Diferenciais",
                "req": ["MAT003"],
                "oferta": "par"
            },

            "QUI105": {
                "nome": "Química Analítica",
                "req": ["EMT102"],
                "oferta": "par"
            },

            "QUI115": {
                "nome": "Química Analítica Experimental",
                "req": ["EMT102"],
                "oferta": "par"
            }

        },


        "5º Período": {

            "EMT002T": {
                "nome": "Materiais Cerâmicos - Teórica",
                "req": ["EMT039"],
                "oferta": "impar"
            },

            "EMT002P": {
                "nome": "Materiais Cerâmicos - Experimental",
                "req": ["EMT039"],
                "oferta": "impar"
            },

            "EME313T": {
                "nome": "Fenômenos de Transporte - Teórica",
                "req": ["MAT003", "MAT021"],
                "oferta": "impar"
            },

            "EME313P": {
                "nome": "Fenômenos de Transporte - Experimental",
                "req": ["MAT003"],
                "oferta": "impar"
            },

            "EME505T": {
                "nome": "Resistência dos Materiais II - Teórica",
                "req": ["EME405T"],
                "oferta": "impar"
            },

            "EME505P": {
                "nome": "Resistência dos Materiais II - Experimental",
                "req": ["EME405T"],
                "oferta": "impar"
            },

            "EMT072": {
                "nome": "Produção de Ligas",
                "req": ["EMT038"],
                "oferta": "impar"
            }

        },


        "6º Período": {

            "EMT049T": {
                "nome": "Conformação de Metais - Teórica",
                "req": ["EMT002T"],
                "oferta": "par"
            },

            "EMT049P": {
                "nome": "Conformação de Metais - Experimental",
                "req": ["EMT002P"],
                "oferta": "par"
            },

            "EMT412T": {
                "nome": "Estrutura e Propriedades Polímeros - Teórica",
                "req": ["QUI022"],
                "oferta": "par"
            },

            "EMT412P": {
                "nome": "Estrutura e Propriedades Polímeros - Experimental",
                "req": ["QUI022"],
                "oferta": "par"
            },

            "EME047T": {
                "nome": "Estrutura e Propriedades Polímeros - Teórica",
                "req": ["EMT039"],
                "oferta": "par"
            },

            "EMT147P": {
                "nome": "Estrutura e Propriedades Polímeros - Experimental",
                "req": ["EMT039"],
                "oferta": "par"
            },

            "EMT071": {
                "nome": "Processos de Fabricação I - Experimental",
                "req": ["EMT072"],
                "oferta": "par"
            },

            "EME039T": {
                "nome": "Fenômenos de Transporte II - Teórica",
                "req": ["EME313T"],
                "oferta": "par"
            },

            "EME039P": {
                "nome": "Fenômenos de Transporte II - Experimental",
                "req": ["EME313T"],
                "oferta": "par"
            }

        },


        "7º Período": {

            "EMT024T": {
                "nome": "Processamento de Materiais Cerâmicos - Teórica",
                "req": ["EMT049T"],
                "oferta": "impar"
            },

            "EMT024P": {
                "nome": "Processamento de Materiais Cerâmicos - Experimental",
                "req": ["EMT049P"],
                "oferta": "impar"
            },

            "EMT025T": {
                "nome": "Técnicas de Caracterização de Materiais",
                "req": ["EMT072"],
                "oferta": "impar"
            },

            "EMT125P": {
                "nome": "Técnicas de Caracterização - Experimental",
                "req": ["EMT072"],
                "oferta": "impar"
            },

            "EMT030": {
                "nome": "Fundamentos de Oxidação e Corrosão",
                "req": ["EMT039"],
                "oferta": "impar"
            },

            "EMT066T": {
                "nome": "Tratamento Térmico - Teórica",
                "req": ["EMT039"],
                "oferta": "impar"
            },

            "EMT066P": {
                "nome": "Tratamento Térmico - Experimental",
                "req": ["EMT039"],
                "oferta": "impar"
            },

            "EAM002": {
                "nome": "Ciência de Materiais",
                "req": ["EMT038"],
                "oferta": "regular"
            },

            "EMT067": {
                "nome": "Seleção de Materiais",
                "req": ["EMT038"],
                "oferta": "impar"
            }

        },


        "8º Período": {

            "EMT027T": {
                "nome": "Vidros e Vitrocerâmicos",
                "req": ["EMT002T"],
                "oferta": "par"
            },

            "EMT046": {
                "nome": "Processamento de Materiais Cerâmicos II",
                "req": ["EMT024T"],
                "oferta": "par"
            },

            "EMT065T": {
                "nome": "Processos de Fabricação II",
                "req": ["EMT071"],
                "oferta": "par"
            },

            "EMT022T": {
                "nome": "Tratamento Superficial de Metais",
                "req": ["EMT030"],
                "oferta": "par"
            },

            "EMT042T": {
                "nome": "Processamento de Polímeros - Teórica",
                "req": ["EMT047T", "EMT412T"],
                "oferta": "par"
            },

            "EMT142P": {
                "nome": "Processamento de Polímeros - Experimental",
                "req": ["EMT047T"],
                "oferta": "par"
            },

            "EPR220": {
                "nome": "Higiene e Segurança do Trabalho",
                "req": [],
                "oferta": "regular"
            },

            "EPR002": {
                "nome": "Organização Industrial e Administração",
                "req": [],
                "oferta": "regular"
            }

        },


        "9º Período": {

            "IEPG01": {
                "nome": "Administração e Economia",
                "req": [],
                "oferta": "impar"
            },

            "TCC001": {
                "nome": "Trabalho de Conclusão de Curso I",
                "req": [],
                "oferta": "regular"
            }

        },


        "10º Período": {

            "EST001": {
                "nome": "Estágio Supervisionado",
                "req": [],
                "oferta": "regular"
            },

            "TCC002": {
                "nome": "Trabalho de Conclusão de Curso II",
                "req": ["TCC001"],
                "oferta": "regular"
            }

        }

    }

}


# ============================================================
# ESTADO DA SESSÃO
# ============================================================

if "aprovadas" not in st.session_state:
    st.session_state.aprovadas = {}


# ============================================================
# CABEÇALHO
# ============================================================

st.markdown(
    '<div class="brand-container">'
    '<div class="brand-caemt">CAEMT</div>'
    '<div class="brand-unifei">UNIFEI</div>'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    "<h1>Fluxograma Inteligente</h1>",
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">'
    'Selecione a grade correspondente, o período letivo '
    'e as disciplinas concluídas.'
    '</p>',
    unsafe_allow_html=True
)


# ============================================================
# CONFIGURAÇÕES
# ============================================================

col_grade, col_periodo = st.columns(2)


with col_grade:

    grade_versao = st.selectbox(
        "Grade curricular:",
        list(matrizes.keys()),
        index=0
    )


with col_periodo:

    periodo_atual = st.selectbox(
        "Período de destino:",
        options=[
            "impar",
            "par"
        ],
        format_func=lambda x: (
            "1º semestre do ano (Ímpar)"
            if x == "impar"
            else "2º semestre do ano (Par)"
        ),
        index=1
    )


st.markdown("---")


# ============================================================
# GRADE ATUAL
# ============================================================

grade_selecionada = matrizes[grade_versao]


# ============================================================
# LAYOUT PRINCIPAL
# ============================================================

col_esquerda, col_direita = st.columns(
    [1.15, 0.85]
)


# ============================================================
# COLUNA ESQUERDA — MATÉRIAS CONCLUÍDAS
# ============================================================

with col_esquerda:

    st.markdown("### 1. Matérias concluídas")

    for semestre, materias in grade_selecionada.items():

        with st.expander(
            semestre,
            expanded=True
        ):

            for codigo, dados in materias.items():

                chave_estado = (
                    f"{grade_versao}-{codigo}"
                )

                marcado = st.checkbox(
                    f"**{codigo}** — {dados['nome']}",
                    key=f"chk-{chave_estado}",
                    value=st.session_state.aprovadas.get(
                        chave_estado,
                        False
                    )
                )

                st.session_state.aprovadas[
                    chave_estado
                ] = marcado


# ============================================================
# LISTA DE MATÉRIAS APROVADAS
# ============================================================

aprovadas = []

for materias in grade_selecionada.values():

    for codigo in materias.keys():

        chave = f"{grade_versao}-{codigo}"

        if st.session_state.aprovadas.get(
            chave,
            False
        ):

            aprovadas.append(codigo)


# ============================================================
# TOTAL DE MATÉRIAS
# ============================================================

total_materias = sum(
    len(materias)
    for materias in grade_selecionada.values()
)


# ============================================================
# PROGRESSO
# ============================================================

if total_materias > 0:

    progresso = int(
        (
            len(aprovadas)
            / total_materias
        )
        * 100
    )

else:

    progresso = 0


# ============================================================
# BARRA DE STATUS
# ============================================================

status_html = (
    '<div class="status-bar">'

        '<div class="status-item">'
            '<div class="status-label">'
                'Matérias Concluídas'
            '</div>'
            f'<div class="status-value">'
                f'{len(aprovadas)}'
            '</div>'
        '</div>'

        '<div class="status-divider"></div>'

        '<div class="status-item">'
            '<div class="status-label">'
                'Total de Matérias'
            '</div>'
            f'<div class="status-value">'
                f'{total_materias}'
            '</div>'
        '</div>'

        '<div class="status-divider"></div>'

        '<div class="status-item">'
            '<div class="status-label">'
                'Progresso'
            '</div>'
            f'<div class="status-value">'
                f'{progresso}%'
            '</div>'
        '</div>'

    '</div>'
)

st.markdown(
    status_html,
    unsafe_allow_html=True
)


# ============================================================
# COLUNA DIREITA — PRÓXIMO SEMESTRE
# ============================================================

with col_direita:

    st.markdown(
        "### 2. Situação para o próximo semestre"
    )

    liberadas_regulares = []

    liberadas_nao_ofertadas = []


    # ========================================================
    # PROCESSAMENTO DAS DISCIPLINAS
    # ========================================================

    for semestre, materias in grade_selecionada.items():

        for codigo, dados in materias.items():

            # Disciplina já concluída
            if codigo in aprovadas:
                continue


            # Verifica pré-requisitos
            tem_requisitos = all(
                requisito in aprovadas
                for requisito in dados["req"]
            )


            if not tem_requisitos:
                continue


            # Verifica oferta
            oferta_bate = (
                dados["oferta"] == "regular"
                or
                dados["oferta"] == periodo_atual
            )


            if oferta_bate:

                liberadas_regulares.append(
                    {
                        "codigo": codigo,
                        "nome": dados["nome"]
                    }
                )

            else:

                liberadas_nao_ofertadas.append(
                    {
                        "codigo": codigo,
                        "nome": dados["nome"],
                        "temporada": dados["oferta"]
                    }
                )


    # ========================================================
    # SEM RESULTADOS
    # ========================================================

    if (
        not liberadas_regulares
        and
        not liberadas_nao_ofertadas
    ):

        st.info(
            "Selecione as matérias ao lado "
            "para calcular a compatibilidade."
        )


    else:

        # ====================================================
        # DISCIPLINAS DISPONÍVEIS
        # ====================================================

        if liberadas_regulares:

            for materia in liberadas_regulares:

                codigo = materia["codigo"]
                nome = materia["nome"]

                html = (
                    '<div class="sugestao-item">'
                    f'<strong>{codigo}</strong>'
                    f' — {nome}'
                    '</div>'
                )

                st.markdown(
                    html,
                    unsafe_allow_html=True
                )


        # ====================================================
        # DISCIPLINAS NÃO OFERTADAS
        # ====================================================

        if liberadas_nao_ofertadas:

            st.markdown(
                '<div class="divisoria">'
                'MATÉRIAS LIBERADAS, MAS NÃO OFERTADAS '
                'NESTE PERÍODO'
                '</div>',
                unsafe_allow_html=True
            )


            for materia in liberadas_nao_ofertadas:

                codigo = materia["codigo"]

                nome = materia["nome"]

                temporada = materia["temporada"]


                if temporada == "impar":

                    texto_temporada = (
                        "Ofertada apenas no "
                        "1º semestre do ano"
                    )

                else:

                    texto_temporada = (
                        "Ofertada apenas no "
                        "2º semestre do ano"
                    )


                html = (
                    '<div class="sugestao-item bloqueada-oferta">'
                    f'<strong>{codigo}</strong>'
                    f' — {nome}'
                    '<span class="aviso-oferta">'
                    f'{texto_temporada}'
                    '</span>'
                    '</div>'
                )


                st.markdown(
                    html,
                    unsafe_allow_html=True
                )

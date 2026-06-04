import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Simulador de Matrícula - Engenharia de Materiais UNIFEI",
    layout="wide"
)

# Estilização customizada para manter a identidade visual original
st.markdown("""
    <style>
    .brand-container {
        display: flex;
        justify-content: space-between;
        font-weight: 800;
        font-size: 1.1rem;
        margin-bottom: -20px;
    }
    .brand-caemt { color: #4a148c; }
    .brand-unifei { color: #0056b3; }
    h1 { text-align: center; font-weight: 800; margin-top: 10px; color: #1a1a1a; }
    h2 { color: #1a1a1a; }
    .subtitle { text-align: center; color: #555555; margin-bottom: 30px; }
    .badge-codigo {
        background: #e5e7eb;
        padding: 3px 8px;
        border-radius: 4px;
        font-weight: 700;
        color: #374151;
        font-family: monospace;
        margin-right: 5px;
    }
    .sugestao-item {
        padding: 12px 16px;
        margin-bottom: 10px;
        background: #f0fdf4;
        border-left: 4px solid #1e7e34;
        border-radius: 6px;
        color: #1a1a1a;
    }
    .sugestao-aviso-correq {
        padding: 12px 16px;
        margin-bottom: 10px;
        background: #fef3c7;
        border-left: 4px solid #f59e0b;
        border-radius: 6px;
        color: #92400e;
    }
    .bloqueada-oferta {
        background: #fef2f2;
        border-left: 4px solid #b21f2d;
        color: #7f1d1d;
    }
    .aviso-oferta {
        display: block;
        font-size: 0.8rem;
        font-weight: 600;
        color: #b21f2d;
        margin-top: 4px;
    }
    .aviso-correq {
        display: block;
        font-size: 0.8rem;
        font-weight: 600;
        color: #d97706;
        margin-top: 4px;
    }
    .divisoria {
        margin: 25px 0 15px 0;
        font-weight: 700;
        color: #333333;
        font-size: 0.8rem;
        border-bottom: 1px solid #d1d5db;
        padding-bottom: 6px;
    }
    .header-periodo {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 10px;
        padding: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Dados das Matrizes Curriculares com Correquisitos
matrizes = {
    "2023": {
        "1º Período": {
            'EMT101': {'nome': 'Introdução à Engenharia de Materiais', 'req': [], 'correq': [], 'oferta': 'impar'},
            'CCO016': {'nome': 'Fundamentos de Programação', 'req': [], 'correq': [], 'oferta': 'regular'},
            'IEPG21': {'nome': 'Ciências Sociais e Humanas', 'req': [], 'correq': [], 'oferta': 'regular'},
            'MAT00A': {'nome': 'Cálculo A', 'req': [], 'correq': [], 'oferta': 'regular'},
            'LET013': {'nome': 'Escrita Acadêmica Científica', 'req': [], 'correq': [], 'oferta': 'regular'},
            'EMT102': {'nome': 'Química Geral', 'req': [], 'correq': [], 'oferta': 'regular'},
            'DES005': {'nome': 'Desenho Técnico Básico', 'req': [], 'correq': [], 'oferta': 'impar'}
        },
        "2º Período": {
            'EMT037T': {'nome': 'Ciência dos Materiais I - Teórica', 'req': ['EMT101', 'EMT102'], 'correq': ['EMT037P'], 'oferta': 'par'},
            'EMT037P': {'nome': 'Ciência dos Materiais I - Experimental', 'req': ['EMT102'], 'correq': ['EMT037T'], 'oferta': 'par'},
            'FIS210': {'nome': 'Física I', 'req': ['MAT00A'], 'correq': [], 'oferta': 'regular'},
            'FIS212': {'nome': 'Física Experimental I', 'req': [], 'correq': [], 'oferta': 'regular'},
            'MAT00B': {'nome': 'Cálculo B', 'req': ['MAT00A'], 'correq': [], 'oferta': 'regular'},
            'MAT00D': {'nome': 'Equações Diferenciais A', 'req': ['MAT00A'], 'correq': [], 'oferta': 'regular'},
            'QUI212': {'nome': 'Química Geral Experimental', 'req': ['EMT102'], 'correq': [], 'oferta': 'regular'},
            'EMT201': {'nome': 'Química Inorgânica', 'req': ['EMT102'], 'correq': [], 'oferta': 'par'},
            'DES006': {'nome': 'Desenho Técnico Auxiliado por Computador', 'req': ['DES005'], 'correq': [], 'oferta': 'par'}
        },
        "3º Período": {
            'EMT038': {'nome': 'Ciência dos Materiais II', 'req': ['EMT037T'], 'correq': [], 'oferta': 'impar'},
            'FIS310': {'nome': 'Física II A', 'req': ['FIS210', 'MAT00B'], 'correq': [], 'oferta': 'regular'},
            'FIS320': {'nome': 'Física II B', 'req': ['FIS210', 'MAT00B'], 'correq': [], 'oferta': 'regular'},
            'EME303': {'nome': 'Estática', 'req': ['FIS210', 'MAT00A'], 'correq': [], 'oferta': 'regular'},
            'MAT00C': {'nome': 'Cálculo C', 'req': ['MAT00B'], 'correq': [], 'oferta': 'regular'},
            'MAT00N': {'nome': 'Cálculo Numérico', 'req': ['MAT00A', 'CCO016'], 'correq': [], 'oferta': 'regular'},
            'EMT103': {'nome': 'Físico-Química', 'req': ['EMT102', 'MAT00A'], 'correq': [], 'oferta': 'impar'},
            'QUI022': {'nome': 'Química Orgânica', 'req': ['EMT102'], 'correq': [], 'oferta': 'impar'}
        },
        "4º Período": {
            'EMT039': {'nome': 'Termodinâmica', 'req': ['EMT103'], 'correq': [], 'oferta': 'par'},
            'FIS410': {'nome': 'Física III', 'req': ['FIS310', 'MAT00C'], 'correq': [], 'oferta': 'regular'},
            'EME405T': {'nome': 'Resistência dos Materiais - Teórica', 'req': ['EME303'], 'correq': ['IEM405P'], 'oferta': 'regular'},
            'IEM405P': {'nome': 'Resistência dos Materiais - Experimental', 'req': ['EME303'], 'correq': ['EME405T'], 'oferta': 'regular'},
            'MAT013': {'nome': 'Probabilidade e Estatística', 'req': ['MAT00B'], 'correq': [], 'oferta': 'regular'},
            'MAT00E': {'nome': 'Equações Diferenciais B', 'req': ['MAT00D'], 'correq': [], 'oferta': 'regular'},
            'QUI105': {'nome': 'Química Analítica', 'req': ['QUI212'], 'correq': ['QUI115'], 'oferta': 'par'},
            'QUI115': {'nome': 'Química Analítica Experimental', 'req': ['QUI212'], 'correq': ['QUI105'], 'oferta': 'par'}
        },
        "5º Período": {
            'EMT502T': {'nome': 'Materiais Cerâmicos - Teórica', 'req': ['EMT038', 'EMT039'], 'correq': ['EMT502P'], 'oferta': 'impar'},
            'EMT502P': {'nome': 'Materiais Cerâmicos - Experimental', 'req': ['EMT038'], 'correq': ['EMT502T'], 'oferta': 'impar'},
            'EMT501': {'nome': 'Metalurgia Física', 'req': ['EMT038', 'EMT039'], 'correq': [], 'oferta': 'impar'},
            'EMT072': {'nome': 'Produção de Ligas', 'req': ['EMT038'], 'correq': [], 'oferta': 'impar'},
            'FIS510': {'nome': 'Física IV A', 'req': ['FIS410'], 'correq': [], 'oferta': 'regular'},
            'IEM002T': {'nome': 'Fenômenos de Transporte II - Teórica', 'req': ['MAT00C', 'MAT00E'], 'correq': ['IEM002P'], 'oferta': 'impar'},
            'IEM002P': {'nome': 'Fenômenos de Transporte II - Experimental', 'req': ['MAT00C', 'MAT00E'], 'correq': ['IEM002T'], 'oferta': 'impar'},
            'EME505T': {'nome': 'Resistência dos Materiais II - Teórica', 'req': ['EME405T'], 'correq': ['IEM505P'], 'oferta': 'impar'},
            'IEM505P': {'nome': 'Resistência dos Materiais II - Experimental', 'req': ['IEM405P'], 'correq': ['EME505T'], 'oferta': 'impar'},
            'EMT503': {'nome': 'Introdução aos Polímeros', 'req': ['QUI022'], 'correq': [], 'oferta': 'impar'}
        },
        "6º Período":

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
    h1 { text-align: center; font-weight: 800; margin-top: 10px; }
    .subtitle { text-align: center; color: #6b7280; margin-bottom: 30px; }
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
    .divisoria {
        margin: 25px 0 15px 0;
        font-weight: 700;
        color: #6b7280;
        font-size: 0.8rem;
        border-bottom: 1px solid #d1d5db;
        padding-bottom: 6px;
    }
    </style>
""", unsafe_allow_html=True)

# Dados das Matrizes Curriculares (Convertidos do JavaScript)
matrizes = {
    "2023": {
        "1º Período": {
            'EMT101': {'nome': 'Introdução à Engenharia de Materiais', 'req': [], 'oferta': 'impar'},
            'CCO016': {'nome': 'Fundamentos de Programação', 'req': [], 'oferta': 'regular'},
            'IEPG21': {'nome': 'Ciências Sociais e Humanas', 'req': [], 'oferta': 'regular'},
            'MAT00A': {'nome': 'Cálculo A', 'req': [], 'oferta': 'regular'},
            'LET013': {'nome': 'Escrita Acadêmica Científica', 'req': [], 'oferta': 'regular'},
            'EMT102': {'nome': 'Química Geral', 'req': [], 'oferta': 'regular'},
            'DES005': {'nome': 'Desenho Técnico Básico', 'req': [], 'oferta': 'impar'}
        },
        "2º Período": {
            'EMT037T': {'nome': 'Ciência dos Materiais I - Teórica', 'req': ['EMT101', 'EMT102'], 'oferta': 'par'},
            'EMT037P': {'nome': 'Ciência dos Materiais I - Experimental', 'req': ['EMT102'], 'oferta': 'par'},
            'FIS210': {'nome': 'Física I', 'req': ['MAT00A'], 'oferta': 'regular'},
            'FIS212': {'nome': 'Física Experimental I', 'req': [], 'oferta': 'regular'},
            'MAT00B': {'nome': 'Cálculo B', 'req': ['MAT00A'], 'oferta': 'regular'},
            'MAT00D': {'nome': 'Equações Diferenciais A', 'req': ['MAT00A'], 'oferta': 'regular'},
            'QUI212': {'nome': 'Química Geral Experimental', 'req': ['EMT102'], 'oferta': 'regular'},
            'EMT201': {'nome': 'Química Inorgânica', 'req': ['EMT102'], 'oferta': 'par'},
            'DES006': {'nome': 'Desenho Técnico Auxiliado por Computador', 'req': ['DES005'], 'oferta': 'par'}
        },
        "3º Período": {
            'EMT038': {'nome': 'Ciência dos Materiais II', 'req': ['EMT037T'], 'oferta': 'impar'},
            'FIS310': {'nome': 'Física II A', 'req': ['FIS210', 'MAT00B'], 'oferta': 'regular'},
            'FIS320': {'nome': 'Física II B', 'req': ['FIS210', 'MAT00B'], 'oferta': 'regular'},
            'EME303': {'nome': 'Estática', 'req': ['FIS210', 'MAT00A'], 'oferta': 'regular'},
            'MAT00C': {'nome': 'Cálculo C', 'req': ['MAT00B'], 'oferta': 'regular'},
            'MAT00N': {'nome': 'Cálculo Numérico', 'req': ['MAT00A', 'CCO016'], 'oferta': 'regular'},
            'EMT103': {'nome': 'Físico-Química', 'req': ['EMT102', 'MAT00A'], 'oferta': 'impar'},
            'QUI022': {'nome': 'Química Orgânica', 'req': ['EMT102'], 'oferta': 'impar'}
        },
        "4º Período": {
            'EMT039': {'nome': 'Termodinâmica', 'req': ['EMT103'], 'oferta': 'par'},
            'FIS410': {'nome': 'Física III', 'req': ['FIS310', 'MAT00C'], 'oferta': 'regular'},
            'EME405T': {'nome': 'Resistência dos Materiais - Teórica', 'req': ['EME303'], 'oferta': 'regular'},
            'IEM405P': {'nome': 'Resistência dos Materiais - Experimental', 'req': ['EME303'], 'oferta': 'regular'},
            'MAT013': {'nome': 'Probabilidade e Estatística', 'req': ['MAT00B'], 'oferta': 'regular'},
            'MAT00E': {'nome': 'Equações Diferenciais B', 'req': ['MAT00D'], 'oferta': 'regular'},
            'QUI105': {'nome': 'Química Analítica', 'req': ['QUI212'], 'oferta': 'par'},
            'QUI115': {'nome': 'Química Analítica Experimental', 'req': ['QUI212'], 'oferta': 'par'}
        },
        "5º Período": {
            'EMT502T': {'nome': 'Materiais Cerâmicos - Teórica', 'req': ['EMT038', 'EMT039'], 'oferta': 'impar'},
            'EMT502P': {'nome': 'Materiais Cerâmicos - Experimental', 'req': ['EMT038'], 'oferta': 'impar'},
            'EMT501': {'nome': 'Metalurgia Física', 'req': ['EMT038', 'EMT039'], 'oferta': 'impar'},
            'EMT072': {'nome': 'Produção de Ligas', 'req': ['EMT038'], 'oferta': 'impar'},
            'FIS510': {'nome': 'Física IV A', 'req': ['FIS410'], 'oferta': 'regular'},
            'IEM002T': {'nome': 'Fenômenos de Transporte II - Teórica', 'req': ['MAT00C', 'MAT00E'], 'oferta': 'impar'},
            'IEM002P': {'nome': 'Fenômenos de Transporte II - Experimental', 'req': ['MAT00C', 'MAT00E'], 'oferta': 'impar'},
            'EME505T': {'nome': 'Resistência dos Materiais II - Teórica', 'req': ['EME405T'], 'oferta': 'impar'},
            'IEM505P': {'nome': 'Resistência dos Materiais II - Experimental', 'req': ['IEM405P'], 'oferta': 'impar'},
            'EMT503': {'nome': 'Introdução aos Polímeros', 'req': ['QUI022'], 'oferta': 'impar'}
        },
        "6º Período": {
            'EMT049T': {'nome': 'Conformação de Metais e Cerâmicas - Teórica', 'req': ['EME405T', 'EMT502T'], 'oferta': 'par'},
            'EMT049P': {'nome': 'Conformação de Metais e Cerâmicas - Experimental', 'req': ['EMT502P'], 'oferta': 'par'},
            'EMT069': {'nome': 'Diagrama de Fases', 'req': ['EMT039'], 'oferta': 'par'},
            'EMT071': {'nome': 'Processos de Fabricação I - Teórica', 'req': ['EMT072'], 'oferta': 'par'},
            'EMT071P': {'nome': 'Processos de Fabricação I - Experimental', 'req': ['EMT072'], 'oferta': 'par'},
            'EMT601T': {'nome': 'Comportamento Mecânico dos Materiais', 'req': ['EME405T', 'EMT038'], 'oferta': 'par'},
            'EME605T': {'nome': 'Transferência de Calor I - Teórica', 'req': ['IEM002T'], 'oferta': 'par'},
            'EME605P': {'nome': 'Transferência de Calor I - Experimental', 'req': ['IEM002P'], 'oferta': 'par'},
            'EMT047T': {'nome': 'Estrutura e Propriedades dos Polímeros', 'req': ['EMT503'], 'oferta': 'par'},
            'EMT063': {'nome': 'Reologia', 'req': ['EMT503'], 'oferta': 'par'}
        },
        "7º Período": {
            'EMT024T': {'nome': 'Processamento de Materiais Cerâmicos - Teórica', 'req': ['EMT049T'], 'oferta': 'impar'},
            'EMT024P': {'nome': 'Processamento de Materiais Cerâmicos - Experimental', 'req': ['EMT049P'], 'oferta': 'impar'},
            'EMT025T': {'nome': 'Técnicas de Caracterização de Materiais', 'req': ['EMT501'], 'oferta': 'impar'},
            'EMT125P': {'nome': 'Técnicas de Caracterização - Experimental', 'req': ['EMT501'], 'oferta': 'impar'},
            'EMT030': {'nome': 'Fundamentos de Oxidação e Corrosão', 'req': ['EMT039'], 'oferta': 'impar'},
            'EMT066T': {'nome': 'Tratamento Térmico - Teórica', 'req': ['EMT069'], 'oferta': 'impar'},
            'EMT066P': {'nome': 'Tratamento Térmico - Experimental', 'req': ['EMT069'], 'oferta': 'impar'},
            'EEB100': {'nome': 'Eletricidade Básica', 'req': ['FIS320'], 'oferta': 'regular'},
            'EMT147P': {'nome': 'Estrutura e Propriedades dos Polímeros - Experimental', 'req': ['EMT047T'], 'oferta': 'impar'},
            'EMT045T': {'nome': 'Síntese de Polímeros - Teórica', 'req': ['QUI022'], 'oferta': 'impar'},
            'EMT701': {'nome': 'Materiais Compósitos', 'req': ['EMT038'], 'oferta': 'impar'}
        },
        "8º Período": {
            'EMT027T': {'nome': 'Vidros e Vitrocerâmicos', 'req': ['EMT502T'], 'oferta': 'par'},
            'EMT046': {'nome': 'Processos Aplicados a Materiais Cerâmicos', 'req': ['EMT024T'], 'oferta': 'par'},
            'EMT067': {'nome': 'Seleção de Materiais', 'req': ['EMT601T'], 'oferta': 'par'},
            'EMT065T': {'nome': 'Processos de Fabricação II', 'req': ['EMT071'], 'oferta': 'par'},
            'EMT022T': {'nome': 'Tratamento Superficial de Metais', 'req': ['EMT030'], 'oferta': 'par'},
            'EP7006': {'nome': 'Higiene e Segurança do Trabalho', 'req': [], 'oferta': 'regular'},
            'EMT045P': {'nome': 'Síntese de Polímeros - Experimental', 'req': ['EMT045T'], 'oferta': 'par'},
            'EMT042T': {'nome': 'Processamento de Polímeros - Teórica', 'req': ['EMT047T', 'EMT063'], 'oferta': 'par'},
            'EMT142P': {'nome': 'Processamento de Polímeros - Experimental', 'req': ['EMT047T'], 'oferta': 'par'},
            'EMT801P': {'nome': 'Processamento de Compósitos - Experimental', 'req': ['EMT701'], 'oferta': 'par'}
        },
        "9º Período": {
            'IEPG22': {'nome': 'Administração Aplicada', 'req': [], 'oferta': 'impar'},
            'IEPG10': {'nome': 'Engenharia Econômica', 'req': [], 'oferta': 'impar'},
            'TCC1EMT2023': {'nome': 'Trabalho de Conclusão de Curso I', 'req': [], 'oferta': 'regular'},
            'EMT068': {'nome': 'Aditivos e Reciclagem de Polímeros', 'req': ['EMT042T'], 'oferta': 'impar'}
        },
        "10º Período": {
            'ESTEMT2023': {'nome': 'Estágio Supervisionado', 'req': [], 'oferta': 'regular'},
            'TCC2EMT2023': {'nome': 'Trabalho de Conclusão de Curso II', 'req': ['TCC1EMT2023'], 'oferta': 'regular'}
        }
    },
    "2016": {
        "1º Período": {
            'EMT101': {'nome': 'Introdução à EMT', 'req': [], 'oferta': 'impar'},
            'CCO016': {'nome': 'Fundamentos de Programação', 'req': [], 'oferta': 'regular'},
            'SOC002': {'nome': 'Ciências Sociais HS', 'req': [], 'oferta': 'regular'},
            'MAT001': {'nome': 'Cálculo I', 'req': [], 'oferta': 'regular'},
            'MAT011': {'nome': 'Geometria Analítica e Álgebra Linear', 'req': [], 'oferta': 'regular'},
            'FIS104': {'nome': 'Mecânica Geral', 'req': [], 'oferta': 'impar'},
            'FIS114': {'nome': 'Laboratório de Mecânica Geral', 'req': [], 'oferta': 'impar'}
        },
        "2º Período": {
            'EMT037T': {'nome': 'Ciência dos Materiais I - Teórica', 'req': ['EMT101'], 'oferta': 'par'},
            'EMT037P': {'nome': 'Ciência dos Materiais I - Experimental', 'req': ['EMT101'], 'oferta': 'par'},
            'FIS203': {'nome': 'Física Geral I', 'req': ['MAT001'], 'oferta': 'regular'},
            'FIS213': {'nome': 'Física Experimental I', 'req': ['MAT001'], 'oferta': 'regular'},
            'MAT002': {'nome': 'Cálculo II', 'req': ['MAT001'], 'oferta': 'regular'},
            'EMT102': {'nome': 'Química Geral', 'req': [], 'oferta': 'par'},
            'BAC002': {'nome': 'Língua Comum', 'req': [], 'oferta': 'regular'}
        },
        "3º Período": {
            'EMT038': {'nome': 'Ciência dos Materiais II', 'req': ['EMT037T'], 'oferta': 'impar'},
            'FIS303': {'nome': 'Estática', 'req': ['FIS104'], 'oferta': 'regular'},
            'EME303': {'nome': 'Resistência dos Materiais - Teórica', 'req': ['FIS104'], 'oferta': 'regular'},
            'FIS403': {'nome': 'Física Geral III', 'req': ['FIS203', 'MAT002'], 'oferta': 'regular'},
            'MAT003': {'nome': 'Cálculo III', 'req': ['MAT002'], 'oferta': 'regular'},
            'EMT103': {'nome': 'Físico-Química', 'req': ['EMT102', 'MAT001'], 'oferta': 'impar'},
            'QUI022': {'nome': 'Química Orgânica', 'req': ['EMT102'], 'oferta': 'impar'}
        },
        "4º Período": {
            'EMT039': {'nome': 'Termodinâmica', 'req': ['EMT038', 'EMT103'], 'oferta': 'par'},
            'EME405T': {'nome': 'Resistência dos Materiais - Experimental', 'req': ['EME303'], 'oferta': 'par'},
            'EME405P': {'nome': 'Mecânica dos Sólidos - Teórica', 'req': ['EME303'], 'oferta': 'par'},
            'MAT013': {'nome': 'Probabilidade e Estatística', 'req': ['MAT002'], 'oferta': 'regular'},
            'MAT021': {'nome': 'Equações Diferenciais', 'req': ['MAT003'], 'oferta': 'par'},
            'QUI105': {'nome': 'Química Analítica', 'req': ['EMT102'], 'oferta': 'par'},
            'QUI115': {'nome': 'Química Analítica Experimental', 'req': ['EMT102'], 'oferta': 'par'}
        },
        "5º Período": {
            'EMT002T': {'nome': 'Materiais Cerâmicos - Teórica', 'req': ['EMT039'], 'oferta': 'impar'},
            'EMT002P': {'nome': 'Materiais Cerâmicos - Experimental', 'req': ['EMT039'], 'oferta': 'impar'},
            'EME313T': {'nome': 'Fenômenos de Transporte - Teórica', 'req': ['MAT003', 'MAT021'], 'oferta': 'impar'},
            'EME313P': {'nome': 'Fenômenos de Transporte - Experimental', 'req': ['MAT003'], 'oferta': 'impar'},
            'EME505T': {'nome': 'Resistência dos Materiais II - Teórica', 'req': ['EME405T'], 'oferta': 'impar'},
            'EME505P': {'nome': 'Resistência dos Materiais II - Experimental', 'req': ['EME405T'], 'oferta': 'impar'},
            'EMT072': {'nome': 'Produção de Ligas', 'req': ['EMT038'], 'oferta': 'impar'}
        },
        "6º Período": {
            'EMT049T': {'nome': 'Conformação de Metais - Teórica', 'req': ['EMT002T'], 'oferta': 'par'},
            'EMT049P': {'nome': 'Conformação de Metais - Experimental', 'req': ['EMT002P'], 'oferta': 'par'},
            'EMT412T': {'nome': 'Estrutura e Propriedades Polímeros - Teórica', 'req': ['QUI022'], 'oferta': 'par'},
            'EMT412P': {'nome': 'Estrutura e Propriedades Polímeros - Experimental', 'req': ['QUI022'], 'oferta': 'par'},
            'EME047T': {'nome': 'Estrutura e Propriedades Polímeros - Teórica', 'req': ['EMT039'], 'oferta': 'par'},
            'EMT147P': {'nome': 'Estrutura e Propriedades Polímeros - Experimental', 'req': ['EMT039'], 'oferta': 'par'},
            'EMT071': {'nome': 'Processos de Fabricação I - Experimental', 'req': ['EMT072'], 'oferta': 'par'},
            'EME039T': {'nome': 'Fenômenos de Transporte II - Teórica', 'req': ['EME313T'], 'oferta': 'par'},
            'EME039P': {'nome': 'Fenômenos de Transporte II - Experimental', 'req': ['EME313T'], 'oferta': 'par'}
        },
        "7º Período": {
            'EMT024T': {'nome': 'Processamento de Materiais Cerâmicos - Teórica', 'req': ['EMT049T'], 'oferta': 'impar'},
            'EMT024P': {'nome': 'Processamento de Materiais Cerâmicos - Experimental', 'req': ['EMT049P'], 'oferta': 'impar'},
            'EMT025T': {'nome': 'Técnicas de Caracterização de Materiais', 'req': ['EMT072'], 'oferta': 'impar'},
            'EMT125P': {'nome': 'Técnicas de Caracterização - Experimental', 'req': ['EMT072'], 'oferta': 'impar'},
            'EMT030': {'nome': 'Fundamentos de Oxidação e Corrosão', 'req': ['EMT039'], 'oferta': 'impar'},
            'EMT066T': {'nome': 'Tratamento Térmico - Teórica', 'req': ['EMT039'], 'oferta': 'impar'},
            'EMT066P': {'nome': 'Tratamento Térmico - Experimental', 'req': ['EMT039'], 'oferta': 'impar'},
            'EAM002': {'nome': 'Ciência de Materiais', 'req': ['EMT038'], 'oferta': 'regular'},
            'EMT067': {'nome': 'Seleção de Materiais', 'req': ['EMT038'], 'oferta': 'impar'}
        },
        "8º Período": {
            'EMT027T': {'nome': 'Vidros e Vitrocerâmicos', 'req': ['EMT002T'], 'oferta': 'par'},
            'EMT046': {'nome': 'Processamento de Materiais Cerâmicos II', 'req': ['EMT024T'], 'oferta': 'par'},
            'EMT065T': {'nome': 'Processos de Fabricação II', 'req': ['EMT071'], 'oferta': 'par'},
            'EMT022T': {'nome': 'Tratamento Superficial de Metais', 'req': ['EMT030'], 'oferta': 'par'},
            'EMT042T': {'nome': 'Processamento de Polímeros - Teórica', 'req': ['EMT047T', 'EMT412T'], 'oferta': 'par'},
            'EMT142P': {'nome': 'Processamento de Polímeros - Experimental', 'req': ['EMT047T'], 'oferta': 'par'},
            'EPR220': {'nome': 'Higiene e Segurança do Trabalho', 'req': [], 'oferta': 'regular'},
            'EPR002': {'nome': 'Organização Industrial e Administração', 'req': [], 'oferta': 'regular'}
        },
        "9º Período": {
            'IEPG01': {'nome': 'Administração e Economia', 'req': [], 'oferta': 'impar'},
            'TCC001': {'nome': 'Trabalho de Conclusão de Curso I', 'req': [], 'oferta': 'regular'}
        },
        "10º Período": {
            'EST001': {'nome': 'Estágio Supervisionado', 'req': [], 'oferta': 'regular'},
            'TCC002': {'nome': 'Trabalho de Conclusão de Curso II', 'req': ['TCC001'], 'oferta': 'regular'}
        }
    }
}

# Cabeçalho Superior
st.markdown("""
    <div class="brand-container">
        <div class="brand-caemt">CAEMT</div>
        <div class="brand-unifei">UNIFEI</div>
    </div>
""", unsafe_allow_html=True)

# Logo Centralizado
st.image("https://upload.wikimedia.org/wikipedia/commons/7/7f/UNIFEI.png", width=180, use_container_width=False)

st.markdown("<h1>Fluxograma Inteligente</h1>", unsafe_allow_html=True)
st.markdown("<p class=\"subtitle\">Selecione a grade correspondente, o período letivo e as disciplinas concluídas.</p>", unsafe_allow_html=True)

# Barra de Configuração
col_grade, col_periodo = st.columns(2)
with col_grade:
    grade_versao = st.selectbox("Grade curricular:", list(matrizes.keys()), index=0)
with col_periodo:
    periodo_atual = st.selectbox(
        "Período de destino:", 
        options=["impar", "par"], 
        format_func=lambda x: "1º semestre do ano (Ímpar)" if x == "impar" else "2º semestre do ano (Par)",
        index=1
    )

st.markdown("---")

# Layout de duas colunas principais
col_esquerda, col_direita = st.columns([1.15, 0.85])

aprovadas = []
grade_selecionada = matrizes[grade_versao]

with col_esquerda:
    st.markdown("### 1. Matérias concluídas")
    
    # Renderiza os blocos de períodos com checkboxes
    for semestre, materias in grade_selecionada.items():
        with st.expander(semestre, expanded=True):
            for codigo, dados in materias.items():
                label_html = f"<span class='badge-codigo'>{codigo}</span> {dados['nome']}"
                if st.checkbox(dados['nome'], key=f"chk-{codigo}", help=f"Código: {codigo}"):
                    aprovadas.append(codigo)

with col_direita:
    st.markdown("### 2. Situação para o próximo semestre")
    
    liberadas_regulares = []
    liberadas_nao_ofertadas = []

    # Processamento lógico das regras de matrícula
    for semestre, materias in grade_selecionada.items():
        for codigo, dados in materias.items():
            if codigo in aprovadas:
                continue
                
            tem_requisitos = all(req_codigo in aprovadas for req_codigo in dados['req'])
            
            if tem_requisitos:
                oferta_bate = (dados['oferta'] == 'regular' or dados['oferta'] == periodo_atual)
                if oferta_bate:
                    liberadas_regulares.append({'codigo': codigo, 'nome': dados['nome']})
                else:
                    liberadas_nao_ofertadas.append({'codigo': codigo, 'nome': dados['nome'], 'temporada': dados['oferta']})

    # Renderização dos resultados na tela
    if not liberadas_regulares and not liberadas_nao_ofertadas:
        st.info("Selecione as matérias ao lado para calcular a compatibilidade.")
    else:
        if liberadas_regulares:
            for mat in liberadas_regulares:
                st.markdown(f"""
                    <div class="sugestao-item">
                        <strong>{mat['codigo']}</strong> - {mat['nome']}
                    </div>
                """, unsafe_allow_html=True)
                
        if liberadas_nao_ofertadas:
            st.markdown("<div class='divisoria'>MATÉRIAS REQUISITADAS NÃO OFERTADAS NESTE PERÍODO:</div>", unsafe_allow_html=True)
            for mat in liberadas_nao_ofertadas:
                texto_temporada = 'Ofertada apenas no 1º Semestre' if mat['temporada'] == 'impar' else 'Ofertada apenas no 2º Semestre'
                st.markdown(f"""
                    <div class="sugestao-item bloqueada-oferta">
                        <strong>{mat['codigo']}</strong> - {mat['nome']}
                        <span class="aviso-oferta">{texto_temporada}</span>
                    </div>
                """, unsafe_allow_html=True)

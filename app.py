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
        "6º Período": {
            'EMT049T': {'nome': 'Conformação de Metais e Cerâmicas - Teórica', 'req': ['EME405T', 'EMT502T'], 'correq': ['EMT049P'], 'oferta': 'par'},
            'EMT049P': {'nome': 'Conformação de Metais e Cerâmicas - Experimental', 'req': ['EMT502P'], 'correq': ['EMT049T'], 'oferta': 'par'},
            'EMT069': {'nome': 'Diagrama de Fases', 'req': ['EMT039'], 'correq': [], 'oferta': 'par'},
            'EMT071': {'nome': 'Processos de Fabricação I - Teórica', 'req': ['EMT072'], 'correq': ['EMT071P'], 'oferta': 'par'},
            'EMT071P': {'nome': 'Processos de Fabricação I - Experimental', 'req': ['EMT072'], 'correq': ['EMT071'], 'oferta': 'par'},
            'EMT601T': {'nome': 'Comportamento Mecânico dos Materiais', 'req': ['EME405T', 'EMT038'], 'correq': [], 'oferta': 'par'},
            'EME605T': {'nome': 'Transferência de Calor I - Teórica', 'req': ['IEM002T'], 'correq': ['EME605P'], 'oferta': 'par'},
            'EME605P': {'nome': 'Transferência de Calor I - Experimental', 'req': ['IEM002P'], 'correq': ['EME605T'], 'oferta': 'par'},
            'EMT047T': {'nome': 'Estrutura e Propriedades dos Polímeros', 'req': ['EMT503'], 'correq': [], 'oferta': 'par'},
            'EMT063': {'nome': 'Reologia', 'req': ['EMT503'], 'correq': [], 'oferta': 'par'}
        },
        "7º Período": {
            'EMT024T': {'nome': 'Processamento de Materiais Cerâmicos - Teórica', 'req': ['EMT049T'], 'correq': ['EMT024P'], 'oferta': 'impar'},
            'EMT024P': {'nome': 'Processamento de Materiais Cerâmicos - Experimental', 'req': ['EMT049P'], 'correq': ['EMT024T'], 'oferta': 'impar'},
            'EMT025T': {'nome': 'Técnicas de Caracterização de Materiais', 'req': ['EMT501'], 'correq': ['EMT125P'], 'oferta': 'impar'},
            'EMT125P': {'nome': 'Técnicas de Caracterização - Experimental', 'req': ['EMT501'], 'correq': ['EMT025T'], 'oferta': 'impar'},
            'EMT030': {'nome': 'Fundamentos de Oxidação e Corrosão', 'req': ['EMT039'], 'correq': [], 'oferta': 'impar'},
            'EMT066T': {'nome': 'Tratamento Térmico - Teórica', 'req': ['EMT069'], 'correq': ['EMT066P'], 'oferta': 'impar'},
            'EMT066P': {'nome': 'Tratamento Térmico - Experimental', 'req': ['EMT069'], 'correq': ['EMT066T'], 'oferta': 'impar'},
            'EEB100': {'nome': 'Eletricidade Básica', 'req': ['FIS320'], 'correq': [], 'oferta': 'regular'},
            'EMT147P': {'nome': 'Estrutura e Propriedades dos Polímeros - Experimental', 'req': ['EMT047T'], 'correq': [], 'oferta': 'impar'},
            'EMT045T': {'nome': 'Síntese de Polímeros - Teórica', 'req': ['QUI022'], 'correq': ['EMT045P'], 'oferta': 'impar'},
            'EMT701': {'nome': 'Materiais Compósitos', 'req': ['EMT038'], 'correq': [], 'oferta': 'impar'}
        },
        "8º Período": {
            'EMT027T': {'nome': 'Vidros e Vitrocerâmicos', 'req': ['EMT502T'], 'correq': [], 'oferta': 'par'},
            'EMT046': {'nome': 'Processos Aplicados a Materiais Cerâmicos', 'req': ['EMT024T'], 'correq': [], 'oferta': 'par'},
            'EMT067': {'nome': 'Seleção de Materiais', 'req': ['EMT601T'], 'correq': [], 'oferta': 'par'},
            'EMT065T': {'nome': 'Processos de Fabricação II', 'req': ['EMT071'], 'correq': [], 'oferta': 'par'},
            'EMT022T': {'nome': 'Tratamento Superficial de Metais', 'req': ['EMT030'], 'correq': [], 'oferta': 'par'},
            'EP7006': {'nome': 'Higiene e Segurança do Trabalho', 'req': [], 'correq': [], 'oferta': 'regular'},
            'EMT045P': {'nome': 'Síntese de Polímeros - Experimental', 'req': ['EMT045T'], 'correq': [], 'oferta': 'par'},
            'EMT042T': {'nome': 'Processamento de Polímeros - Teórica', 'req': ['EMT047T', 'EMT063'], 'correq': ['EMT142P'], 'oferta': 'par'},
            'EMT142P': {'nome': 'Processamento de Polímeros - Experimental', 'req': ['EMT047T'], 'correq': ['EMT042T'], 'oferta': 'par'},
            'EMT801P': {'nome': 'Processamento de Compósitos - Experimental', 'req': ['EMT701'], 'correq': [], 'oferta': 'par'}
        },
        "9º Período": {
            'IEPG22': {'nome': 'Administração Aplicada', 'req': [], 'correq': [], 'oferta': 'impar'},
            'IEPG10': {'nome': 'Engenharia Econômica', 'req': [], 'correq': [], 'oferta': 'impar'},
            'TCC1EMT2023': {'nome': 'Trabalho de Conclusão de Curso I', 'req': [], 'correq': [], 'oferta': 'regular'},
            'EMT068': {'nome': 'Aditivos e Reciclagem de Polímeros', 'req': ['EMT042T'], 'correq': [], 'oferta': 'impar'}
        },
        "10º Período": {
            'ESTEMT2023': {'nome': 'Estágio Supervisionado', 'req': [], 'correq': [], 'oferta': 'regular'},
            'TCC2EMT2023': {'nome': 'Trabalho de Conclusão de Curso II', 'req': ['TCC1EMT2023'], 'correq': [], 'oferta': 'regular'}
        }
    },
    "2016": {
        "1º Período": {
            'EMT101': {'nome': 'Introdução à Engenharia de Materiais', 'req': [], 'oferta': 'impar'},
            'CCO001': {'nome': 'Algoritmos e Programação de Computadores', 'req': [], 'oferta': 'regular'},
            'HD0101': {'nome': 'Ciências Sociais e Humanas', 'req': [], 'oferta': 'regular'},
            'MAT001': {'nome': 'Cálculo I', 'req': [], 'oferta': 'regular'},
            'QUI001': {'nome': 'Química Geral', 'req': [], 'oferta': 'regular'},
            'DES001': {'nome': 'Desenho Técnico Instrumentado', 'req': [], 'oferta': 'impar'}
        },
        "2º Período": {
            'EMT001': {'nome': 'Ciência dos Materiais I', 'req': ['EMT101', 'QUI001'], 'oferta': 'par'},
            'FIS001': {'nome': 'Física I', 'req': ['MAT001'], 'oferta': 'regular'},
            'MAT002': {'nome': 'Cálculo II', 'req': ['MAT001'], 'oferta': 'regular'},
            'MAT004': {'nome': 'Geometria Analítica e Álgebra Linear', 'req': [], 'oferta': 'regular'},
            'QUI002': {'nome': 'Química Experimental', 'req': ['QUI001'], 'oferta': 'regular'}
        },
        "3º Período": {
            'EMT002': {'nome': 'Ciência dos Materiais II', 'req': ['EMT001'], 'oferta': 'impar'},
            'FIS002': {'nome': 'Física II', 'req': ['FIS001', 'MAT002'], 'oferta': 'regular'},
            'EME001': {'nome': 'Mecânica Geral', 'req': ['FIS001', 'MAT002'], 'oferta': 'regular'},
            'MAT003': {'nome': 'Cálculo III', 'req': ['MAT002'], 'oferta': 'regular'},
            'QUI003': {'nome': 'Físico-Química', 'req': ['QUI001', 'MAT001'], 'oferta': 'impar'}
        },
        "4º Período": {
            'EMT003': {'nome': 'Termodinâmica dos Materiais', 'req': ['QUI003'], 'oferta': 'par'},
            'FIS003': {'nome': 'Física III', 'req': ['FIS002', 'MAT003'], 'oferta': 'regular'},
            'EME002': {'nome': 'Resistência dos Materiais', 'req': ['EME001'], 'oferta': 'regular'},
            'MAT005': {'nome': 'Cálculo Numérico', 'req': ['MAT002', 'CCO001'], 'oferta': 'regular'},
            'MAT006': {'nome': 'Estatística e Probabilidade', 'req': ['MAT002'], 'oferta': 'regular'}
        },
        "5º Período": {
            'EMT004': {'nome': 'Materiais Cerâmicos I', 'req': ['EMT002', 'EMT003'], 'oferta': 'impar'},
            'EMT005': {'nome': 'Metalurgia Física I', 'req': ['EMT002', 'EMT003'], 'oferta': 'impar'},
            'IEM001': {'nome': 'Fenômenos de Transporte', 'req': ['MAT003'], 'oferta': 'impar'},
            'EMT006': {'nome': 'Introdução aos Polímeros', 'req': ['EMT002'], 'oferta': 'impar'}
        },
        "6º Período": {
            'EMT007': {'nome': 'Processamento de Cerâmicas I', 'req': ['EMT004'], 'oferta': 'par'},
            'EMT008': {'nome': 'Transformação de Fases', 'req': ['EMT003'], 'oferta': 'par'},
            'EMT009': {'nome': 'Comportamento Mecânico de Materiais', 'req': ['EME002', 'EMT002'], 'oferta': 'par'},
            'EMT010': {'nome': 'Estrutura e Propriedades de Polímeros', 'req': ['EMT006'], 'oferta': 'par'}
        },
        "7º Período": {
            'EMT011': {'nome': 'Técnicas de Caracterização de Materiais', 'req': ['EMT005'], 'oferta': 'impar'},
            'EMT012': {'nome': 'Corrosão e Proteção de Materiais', 'req': ['EMT003'], 'oferta': 'impar'},
            'EEB001': {'nome': 'Eletrotécnica Geral', 'req': ['FIS003'], 'oferta': 'regular'},
            'EMT013': {'nome': 'Materiais Compósitos', 'req': ['EMT002'], 'oferta': 'impar'}
        },
        "8º Período": {
            'EMT014': {'nome': 'Seleção de Materiais', 'req': ['EMT009'], 'oferta': 'par'},
            'EP0001': {'nome': 'Higiene e Segurança do Trabalho', 'req': [], 'oferta': 'regular'},
            'EMT015': {'nome': 'Processamento de Polímeros', 'req': ['EMT010'], 'oferta': 'par'}
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
    liberadas_com_aviso_correq = []

    # Processamento lógico das regras de matrícula
    for semestre, materias in grade_selecionada.items():
        for codigo, dados in materias.items():
            if codigo in aprovadas:
                continue
                
            tem_requisitos = all(req_codigo in aprovadas for req_codigo in dados['req'])
            
            if tem_requisitos:
                oferta_bate = (dados['oferta'] == 'regular' or dados['oferta'] == periodo_atual)
                if oferta_bate:
                    # Verifica se há correquisito não selecionado (apenas para grade 2023)
                    correqs = dados.get('correq', [])
                    tem_correq_faltando = any(correq_codigo not in aprovadas for correq_codigo in correqs)
                    
                    if tem_correq_faltando and correqs:
                        # Tem correquisito que não foi selecionado
                        correq_info = {
                            'codigo': codigo,
                            'nome': dados['nome'],
                            'correqs': [c for c in correqs if c not in aprovadas]
                        }
                        liberadas_com_aviso_correq.append(correq_info)
                    else:
                        # Sem problemas de correquisitos
                        liberadas_regulares.append({'codigo': codigo, 'nome': dados['nome']})
                else:
                    liberadas_nao_ofertadas.append({'codigo': codigo, 'nome': dados['nome'], 'temporada': dados['oferta']})

    # Renderização dos resultados na tela
    if not liberadas_regulares and not liberadas_nao_ofertadas and not liberadas_com_aviso_correq:
        st.info("Selecione as matérias ao lado para calcular a compatibilidade.")
    else:
        # Disciplinas sem aviso
        if liberadas_regulares:
            for mat in liberadas_regulares:
                st.markdown(f"""
                    <div class="sugestao-item">
                        <strong>{mat['codigo']}</strong> - {mat['nome']}
                    </div>
                """, unsafe_allow_html=True)
        
        # Disciplinas com aviso de correquisito
        if liberadas_com_aviso_correq:
            for mat in liberadas_com_aviso_correq:
                correq_nomes = []
                for correq_id in mat['correqs']:
                    # Busca o nome do correquisito
                    for sem, mats in grade_selecionada.items():
                        if correq_id in mats:
                            correq_nomes.append(f"{correq_id} - {mats[correq_id]['nome']}")
                
                correq_texto = "<br>".join(correq_nomes)
                st.markdown(f"""
                    <div class="sugestao-aviso-correq">
                        <strong>{mat['codigo']}</strong> - {mat['nome']}
                        <span class="aviso-correq">⚠️ Recomenda-se cursar junto com:<br>{correq_texto}</span>
                    </div>
                """, unsafe_allow_html=True)
                
        # Disciplinas não ofertadas
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

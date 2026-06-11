import streamlit as st
import docx
from avaliador import grade_essay

# Configuração da página pois é meu front end
st.set_page_config(page_title="Avaliador de Redação AI", page_icon="📝", layout="centered")

st.title("📝 Avaliador de Redação com IA")
st.write("Faça o upload do seu arquivo Word (.docx) para receber uma avaliação detalhada usando LangGraph e OpenAI.")

st.markdown("---")

# Função adaptada para ler direto do upload do Streamlit
def ler_redacao_streamlit(uploaded_file):
    try:
        doc = docx.Document(uploaded_file)
        texto_completo = []
        for paragrafo in doc.paragraphs:
            if paragrafo.text.strip():
                texto_completo.append(paragrafo.text.strip())
        return '\n'.join(texto_completo)
    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")
        return ""

# Área de Upload
arquivo_enviado = st.file_uploader("Escolha um arquivo do Microsoft Word", type=["docx"])

if arquivo_enviado is not None:
    st.success("Arquivo carregado com sucesso!")
    
    # Extrai o texto
    texto_redacao = ler_redacao_streamlit(arquivo_enviado)
    
    # Opção para o usuário ler o texto que o robô vai analisar
    with st.expander("Ver texto extraído do documento"):
        st.write(texto_redacao)
        
    # Botão de Ação
    if st.button("🚀 Avaliar Redação", use_container_width=True):
        if not texto_redacao.strip():
            st.warning("O documento parece estar vazio.")
        else:
            # Spinner de carregamento enquanto o LLM pensa
            with st.spinner("A IA está analisando sua redação. Isso pode levar alguns segundos..."):
                resultado = grade_essay(texto_redacao)
                
                # Conversão das notas
                final = resultado['final_score'] * 10
                rel = resultado['relevance_score'] * 10
                gram = resultado['grammar_score'] * 10
                est = resultado['structure_score'] * 10
                prof = resultado['depth_score'] * 10

            # Exibição dos Resultados
            st.markdown("### 🏆 Resultado da Avaliação")
            
            # Layout em colunas para os critérios
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Relevância", f"{rel:.1f}/10")
            col2.metric("Gramática", f"{gram:.1f}/10")
            col3.metric("Estrutura", f"{est:.1f}/10")
            col4.metric("Profundidade", f"{prof:.1f}/10")
            
            # Nota Final em destaque
            st.info(f"**Nota Final Ponderada:** {final:.2f} / 10")
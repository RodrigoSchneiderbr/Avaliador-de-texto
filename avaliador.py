import os
import re
from typing import TypedDict
from dotenv import load_dotenv
import docx

from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

# ==========================================
# CONFIGURAÇÕES INICIAIS E CHAVES
# ==========================================
load_dotenv()

openai_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(api_key=openai_key, model="gpt-4.1-mini") 

# ==========================================
# DEFINIÇÃO DO ESTADO
# ==========================================
class State(TypedDict):
    """ Representa o estado do processo de avaliação da redação """
    essay: str
    relevance_score: float
    grammar_score: float
    structure_score: float
    depth_score: float
    final_score: float

# ==========================================
# FUNÇÕES DE AVALIAÇÃO
# ==========================================
def extract_score(content: str) -> float:
    """Extrai a pontuação numérica da resposta do LLM."""
    match = re.search(r'Pontuação:\s*(\d+(\.\d+)?)', content)
    if match:
        return float(match.group(1))
    raise ValueError(f"Não foi possível extrair a pontuação de: {content}")

def check_relevance(state: State) -> State:
    prompt = ChatPromptTemplate.from_template(
        "Analise a relevância da seguinte redação em relação ao tema dado, prezando pela excelência da Língua Portuguesa. "
        "Forneça uma pontuação de relevância entre 0 e 1. "
        "Sua resposta deve começar com 'Pontuação: ' seguida da pontuação numérica, "
        "depois forneça sua explicação.\n\nRedação: {essay}"
    )
    result = llm.invoke(prompt.format(essay=state["essay"]))
    try:
        state["relevance_score"] = extract_score(result.content)
    except ValueError as e:
        print(f"Erro em check_relevance: {e}")
        state["relevance_score"] = 0.0
    return state

def check_grammar(state: State) -> State:
    prompt = ChatPromptTemplate.from_template(
        "Analise a gramática da Língua Portuguesa na seguinte redação. "
        "Forneça uma pontuação de gramática entre 0 e 1. "
        "Sua resposta deve começar com 'Pontuação: ' seguida da pontuação numérica, "
        "depois forneça sua explicação.\n\nRedação: {essay}"
    )
    result = llm.invoke(prompt.format(essay=state["essay"]))
    try:
        state["grammar_score"] = extract_score(result.content)
    except ValueError as e:
        print(f"Erro em check_grammar: {e}")
        state["grammar_score"] = 0.0
    return state

def analyze_structure(state: State) -> State:
    prompt = ChatPromptTemplate.from_template(
        "Analise a estrutura de acordo com a normal culta da Língua Portuguesa na seguinte redação. "
        "Forneça uma pontuação de estrutura entre 0 e 1. "
        "Sua resposta deve começar com 'Pontuação: ' seguida da pontuação numérica, "
        "depois forneça sua explicação.\n\nRedação: {essay}"
    )
    result = llm.invoke(prompt.format(essay=state["essay"]))
    try:
        state["structure_score"] = extract_score(result.content)
    except ValueError as e:
        print(f"Erro em analyze_structure: {e}")
        state["structure_score"] = 0.0
    return state

def evaluate_depth(state: State) -> State:
    prompt = ChatPromptTemplate.from_template(
        "Avalie a profundidade de análise na seguinte redação. "
        "Forneça uma pontuação de profundidade entre 0 e 1. "
        "Sua resposta deve começar com 'Pontuação: ' seguida da pontuação numérica, "
        "depois forneça sua explicação.\n\nRedação: {essay}"
    )
    result = llm.invoke(prompt.format(essay=state["essay"]))
    try:
        state["depth_score"] = extract_score(result.content)
    except ValueError as e:
        print(f"Erro em evaluate_depth: {e}")
        state["depth_score"] = 0.0
    return state

def calculate_final_score(state: State) -> State:
    state["final_score"] = (
        state["relevance_score"] * 0.3 +
        state["grammar_score"] * 0.2 +
        state["structure_score"] * 0.2 +
        state["depth_score"] * 0.3
    )
    return state

# ==========================================
# FLUXO DE TRABALHO (LANGGRAPH)
# ==========================================
workflow = StateGraph(State)

workflow.add_node("check_relevance", check_relevance)
workflow.add_node("check_grammar", check_grammar)
workflow.add_node("analyze_structure", analyze_structure)
workflow.add_node("evaluate_depth", evaluate_depth)
workflow.add_node("calculate_final_score", calculate_final_score)

workflow.add_conditional_edges(
    "check_relevance",
    lambda x: "check_grammar" if x["relevance_score"] > 0.5 else "calculate_final_score"
)
workflow.add_conditional_edges(
    "check_grammar",
    lambda x: "analyze_structure" if x["grammar_score"] > 0.6 else "calculate_final_score"
)
workflow.add_conditional_edges(
    "analyze_structure",
    lambda x: "evaluate_depth" if x["structure_score"] > 0.7 else "calculate_final_score"
)
workflow.add_conditional_edges(
    "evaluate_depth",
    lambda x: "calculate_final_score"
)

workflow.set_entry_point("check_relevance")
workflow.add_edge("calculate_final_score", END)

app = workflow.compile()

# ==========================================
# FUNÇÕES PRINCIPAIS E LEITURA DE ARQUIVO
# ==========================================
def grade_essay(essay: str) -> dict:
    initial_state = State(
        essay=essay,
        relevance_score=0.0,
        grammar_score=0.0,
        structure_score=0.0,
        depth_score=0.0,
        final_score=0.0
    )
    return app.invoke(initial_state)

def ler_redacao_do_word(caminho_arquivo: str) -> str:
    """Lê um arquivo .docx e retorna o texto completo como string."""
    try:
        doc = docx.Document(caminho_arquivo)
        texto_completo = []
        for paragrafo in doc.paragraphs:
            if paragrafo.text.strip():  # Ignora linhas totalmente em branco
                texto_completo.append(paragrafo.text.strip())
        return '\n'.join(texto_completo)
    except Exception as e:
        print(f"Erro ao ler o arquivo Word: {e}")
        return ""

# ==========================================
# EXECUÇÃO DO SCRIPT
# ==========================================
if __name__ == "__main__":
    # >>> DEFINA O CAMINHO DO SEU ARQUIVO WORD AQUI <<<
    caminho_word = "redacao.docx" 
    
    if not os.path.exists(caminho_word):
        print(f"Arquivo '{caminho_word}' não encontrado. Por favor, verifique o caminho e tente novamente.")
    else:
        print(f"Lendo o arquivo: {caminho_word}...")
        texto_redacao = ler_redacao_do_word(caminho_word)
        
        if texto_redacao:
            print("⏳ Avaliando a redação (isso pode levar alguns segundos)...\n")
            result = grade_essay(texto_redacao)

            # Converte as pontuações de 0-1 para 0-10
            final_score = result['final_score'] * 10
            relevance_score = result['relevance_score'] * 10
            grammar_score = result['grammar_score'] * 10
            structure_score = result['structure_score'] * 10
            depth_score = result['depth_score'] * 10

            # Exibe os resultados
            print("="*40)
            print("RESULTADO DA AVALIAÇÃO")
            print("="*40)
            print(f"🏆 Pontuação Final: {final_score:.2f}/10\n")
            print(f"📌 Relevância:    {relevance_score:.2f}/10")
            print(f"📝 Gramática:     {grammar_score:.2f}/10")
            print(f"🏗️  Estrutura:     {structure_score:.2f}/10")
            print(f"🧠 Profundidade:  {depth_score:.2f}/10")
            print("="*40)
        else:
            print("O documento está vazio ou não pôde ser lido.")
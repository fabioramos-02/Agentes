from crewai import Agent, Task, Crew, Process
from langchain_community.tools import DuckDuckGoSearchRun

# Ferramenta de pesquisa
ferramenta_pesquisa = DuckDuckGoSearchRun()

# Criando o agente responsável por analisar a transcrição e estruturar o conteúdo
agente_analise = Agent(
    role="Analista de Transcrição",
    goal="Analisar a {transcript} e transformar em bullet points.",
    backstory="Você é um especialista em estruturar informações de maneira concisa e eficiente.",
    verbose=True,
    memory=True
)

# Criando o agente de pesquisa
agente_pesquisa = Agent(
    role="Pesquisador",
    goal="Pesquisar mais informações sobre o assunto abordado no vídeo.",
    backstory="Você é um pesquisador experiente que sabe buscar informações relevantes na web.",
    tools=[ferramenta_pesquisa],
    verbose=True,
    memory=True
)

# Criando o agente revisor
agente_revisor = Agent(
    role="Revisor de Conteúdo",
    goal="Revisar e refinar o conteúdo gerado.",
    backstory="Você é um especialista em revisão de texto e sempre garante que o conteúdo seja claro e objetivo.",
    verbose=True,
    memory=True
)

# Definindo a tarefa de análise
tarefa_analise = Task(
    description="Analisar a transcrição do vídeo e organizar as informações em formato de bullet points.",
    expected_output="Um conjunto de bullet points claros e bem estruturados com os principais pontos do vídeo.",
    agent=agente_analise
)

# Definindo a tarefa de pesquisa
tarefa_pesquisa = Task(
    description="Pesquisar mais informações sobre o tema discutido no vídeo.",
    expected_output="Uma lista de insights adicionais baseados em fontes da internet.",
    agent=agente_pesquisa
)

# Definindo a tarefa de revisão
tarefa_revisao = Task(
    description="Revisar os bullet points e as informações adicionais para garantir clareza e boa estrutura.",
    expected_output="Um texto revisado com sugestões de melhoria e correções de formato ou linguagem.",
    agent=agente_revisor
)

# Criando a tripulação e organizando as tarefas em sequência
tripulacao = Crew(
    agents=[agente_analise, agente_pesquisa, agente_revisor],
    tasks=[tarefa_analise, tarefa_pesquisa, tarefa_revisao],
    process=Process.sequential,
    verbose=True
)

# Lendo o conteúdo da transcrição
with open('transcript3.txt', 'r', encoding='utf-8') as f:
    transcript = f.read()

# Iniciando o processo com a transcrição como entrada
resultado = tripulacao.kickoff(inputs={'transcript': transcript})

# Convertendo o resultado para string (caso não seja)
resultado_str = str(resultado)

# Mostrando o resultado final
print(resultado_str)

# Salvando o resultado em formato .md
with open('podcast.md', 'w', encoding='utf-8') as f:
    f.write(resultado_str)

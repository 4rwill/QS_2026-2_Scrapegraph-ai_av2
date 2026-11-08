"""Build AV3 source materials from the preserved, explicitly provisional batch."""
import json
import sys
import os
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
ROOT = BASE.parent
RUN = BASE / 'results/20261108T151915458937-provisional'
ANALYSIS = RUN / 'ai-analysis-20261108T152247707442'
VIDEO = 'https://drive.google.com/drive/folders/1ln8dIKPjHpep5eWkHJ-mPIhnB0MO94QZ?usp=sharing'
REPO = 'https://github.com/4rwill/QS_2026-2_Scrapegraph-ai_av2'


def esc(value):
    out = str(value)
    for a,b in [('&',r'\&'),('%',r'\%'),('_',r'\_'),('#',r'\#')]: out=out.replace(a,b)
    return out


def main():
    metrics=json.loads((ANALYSIS/'metrics.json').read_text(encoding='utf-8'))
    rows=json.loads((ANALYSIS/'consolidated.json').read_text(encoding='utf-8'))
    out=BASE/'relatorio';out.mkdir(exist_ok=True)
    if (out/'relatorio_av3.tex').exists():
        raise SystemExit('Existing report preserved. Edit it in place instead of regenerating.')
    isolated=BASE/'.build/python-libs'
    if isolated.exists(): sys.path.insert(0,str(isolated))
    os.environ['MPLCONFIGDIR']=str(BASE/'.build/matplotlib-config')
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    plt.rcParams.update({'font.family':'Arial','font.size':11})
    fig,ax=plt.subplots(figsize=(9,3.8),layout='constrained')
    for v,dx,color in [('A',-.18,'#1D4F76'),('B',.18,'#B84337')]:
        vals=[r['f1'] for r in rows if r['version']==v]
        bars=ax.bar([i+dx for i in range(6)],vals,.34,label=f'Versão {v}',color=color)
        ax.bar_label(bars,fmt='%.2f',fontsize=9,padding=3)
    ax.axhline(.5,color='#555555',linestyle='--',linewidth=1,label='tau = 0,5')
    ax.set(xticks=range(6),xticklabels=[f'CT{i:02d}' for i in range(1,7)],ylim=(0,1.08),ylabel='F1 lexical')
    ax.legend(loc='lower left',ncols=3,frameon=False);ax.spines[['top','right']].set_visible(False)
    ax.set_title('12 respostas reais — referências aguardam revisão humana',loc='left',fontsize=12)
    fig.savefig(out/'f1_por_caso.png',dpi=180);plt.close(fig)
    preamble=(ROOT/'atividade2/relatorio/relatorio_av2.tex').read_text(encoding='utf-8').split(r'\begin{document}')[0]
    preamble=preamble.replace('Missão Contexto Confiável: SmartScraperGraph - AV2','Métricas automáticas e avaliação de respostas - AV3')
    names=['ARTHUR SOARES SANTANA','ARTUR JOSÉ SOARES SANTOS','CHRISTIAN WILL SILVA SANTOS NUNES','EDUARDO CURCINO MONTEIRO FILHO','EDUARDO FERREIRA BOMFIM FILHO','IURI MAURÍCIO MAIA PEREIRA','PEDRO CÉSAR FIGUEIREDO CARNEIRO','RIAN PURIFICAÇÃO DE OLIVEIRA']
    body=r'''\begin{document}
\onehalfspacing
\begin{titlepage}\thispagestyle{empty}\begin{center}
\textbf{UNIVERSIDADE FEDERAL DE SERGIPE}\\
\textbf{DEPARTAMENTO DE COMPUTAÇÃO}\\[1cm]
\textbf{@@NAMES@@}
\vspace{1.3cm}

\textbf{\Large MÉTRICAS AUTOMÁTICAS E AVALIAÇÃO DE RESPOSTAS}\\[0.4cm]
\textbf{COMPARAÇÃO DE PROMPTS NO SMARTSCRAPERGRAPH --- ATIVIDADE 3}
\end{center}\vspace{1cm}
\begin{flushright}\begin{minipage}{0.65\textwidth}
Relatório técnico da Atividade 3 de Qualidade de Software, Departamento de Computação da Universidade Federal de Sergipe. Docente: Prof. Dr. Glauco de Figueiredo Carneiro.
\end{minipage}\end{flushright}
\vfill\begin{center}SÃO CRISTÓVÃO/SE\\NOVEMBRO/2026\end{center}\end{titlepage}
\pagenumbering{roman}\tableofcontents\clearpage\pagenumbering{arabic}

\section{Resumo, recorte e estado do estudo}
Este trabalho reutiliza o fluxo de extração de catálogo HTML sintético do SmartScraperGraph estudado na AV2, comparando dois prompts em seis casos. A versão A usa P2 da AV2; B acrescenta instruções sobre trecho literal, preço ausente, conflito e abstenção. O único fator principal modificado é o prompt; não é possível atribuir efeitos a cada frase adicionada.

Em 08/11/2026 foram executadas 12 combinações, uma por caso/versão, todas com resposta e configuração correspondente ao plano. O F1 lexical médio foi @@MEANA@@ em A e @@MEANB@@ em B. Com tau=0,5, o sinal aprovou cinco de seis respostas em cada versão. A análise complementar por IA atribuiu aprovação integral a zero de seis em ambas, principalmente por apoio literal insuficiente. Esses pareceres não constituem avaliação humana.

\textbf{Estado metodológico:} as referências foram propostas diretamente das fontes, mas ainda não passaram pela revisão humana prévia exigida no enunciado \cite{enunciado}. Por isso, o lote está identificado como completo provisório. As 12 anotações R1, quatro R2, consenso humano, aprovação humana e concordância automático--humano permanecem pendentes. A validação posterior não deve ser retrodatada; a equipe precisa resolver essa pendência antes de considerar a atividade concluída.

\section{Plano GQM e critérios anteriores à execução}
\textbf{Objetivo:} avaliar se uma mudança no prompt melhora a adequação e a sustentação da extração de catálogo sob a perspectiva da equipe e verificar se o sinal lexical representa essa adequação.

\begingroup\small\setlength{\tabcolsep}{4pt}
\begin{longtable}{@{}p{3.3cm}p{4.3cm}p{6.8cm}@{}}\toprule
Pergunta & Medida & Unidade, fórmula e limitação \\\midrule
Q1: B atende melhor à tarefa? & Aprovação humana & Aprovadas/6 por versão; exige três notas 2, sem falha crítica. Amostra pequena e oito decisões somente R1. \\
Q2: sinal automático representa adequação? & F1 lexical & Entre 0 e 1; média = soma/6. Sobreposição de tokens não verifica fatos nem qualidade do apoio. \\
Q2, mesma perspectiva & Concordância automático--humano & Decisões iguais/12. Pode haver concordância casual; não demonstra validade geral. \\\bottomrule
\end{longtable}\endgroup
Diagnóstico adicional: concordância binária R1--R2 antes do consenso, iguais/4. Não usar denominador 12 ou 16 para essa medida. Todas as decisões humanas estão indisponíveis nesta versão do relatório.

O protocolo foi preparado em 07/11, antes da bateria de 08/11. Tau=0,5 foi escolhido como valor didático permitido pelo enunciado e permaneceu fixo. A regra de avanço exige mais aprovações humanas em B, nenhuma falha crítica em B e nenhuma regressão aprovada-em-A/reprovada-em-B. Empate sem falhas mantém A como baseline; falha crítica ou regressão exige revisar B. Nenhuma regra autoriza produção.

\section{Casos, referências e versões}
As referências propostas não derivam de outra resposta do modelo: foram escritas a partir dos HTMLs sintéticos. Fontes e referências estão em \arquivo{atividade3/data/}; o arquivo de revisão registra estado pendente e hashes. O motivo admite paráfrases semanticamente equivalentes na avaliação por rubrica.
\begingroup\small
\begin{longtable}{@{}p{1.1cm}p{3cm}p{7.5cm}p{2.7cm}@{}}\toprule
Caso & Tipo & Resultado esperado & Fonte \\\midrule
CT01 & Funcional & Aurora=10; Cedro=20; nomes e valores ligados por trecho literal. & correct \\
CT02 & Funcional & Canela=15,50; Dália=0. Zero é preço conhecido. & prices \\
CT03 & Funcional & Aurora preservado, preço null por ausência. & missing \\
CT04 & Funcional & Aurora uma vez, preço null, conflito explicado. & conflict \\
CT05 & Sem evidência & Lista vazia e explicação da ausência de catálogo. & irrelevant \\
CT06 & Paráfrase CT01 & Mesma intenção e fatos esperados de CT01. & correct \\\bottomrule
\end{longtable}\endgroup
CT06 é relacionado a CT01, não uma observação independente. Nos seis casos, a pergunta é idêntica entre A e B. Prompts, fontes, perguntas e referências completos são recuperáveis no snapshot do lote.

\subsection{Mudança principal}
A usa o prompt estruturado P2 da AV2. B conserva esse texto e acrescenta: copiar a linha que liga nome ao preço; preservar produto sem preço com null; representar conflito em um produto com null; devolver lista vazia sem catálogo; não importar fatos de instruções; usar motivo vazio quando não houver limitação. Nenhum adaptador corrige ou bloqueia a saída antes da medição. O schema nativo foi mantido nas duas versões.

\section{Ambiente, execução e integridade}
SmartScraperGraph 2.3.1, commit \arquivo{194055e203afce41ed4e70365dbc416bad756115}; Python 3.12.14; Ollama 0.40.2; llama3.2:latest, 3.2B Q4\_K\_M; temperatura zero; JSON; contexto 8192. Digest do modelo: \arquivo{a80c4f17acd55265feec403c7aef86be0c25983ab279d83f3bcd3abbcb5b8b72}.

Lote \arquivo{20261108T151915458937-provisional}; 12 respostas, uma chamada capturada por combinação. A ordem alternou A/B entre casos, com 120 s de limite por subprocesso e nenhuma retentativa automática. Ambiente antes/depois e configurações corresponderam ao plano. Dois pilotos CT01/A da preparação permanecem separados e não entram nos denominadores. Dez controles sintéticos do avaliador passaram; eles não são respostas do sistema.

Cada saída preserva request, resposta completa, mensagens do modelo, configuração, tempo, log e sinal automático. Os manifestos incluem hashes e cópia dos arquivos locais, pois o código ainda estava sem commit no momento da execução. O nome latest é mutável, mas o digest foi registrado. Temperatura zero não garante repetibilidade nem estabilidade, e uma execução por condição não mede variância.

\section{Métrica automática e rubrica}
O F1 usa o JSON serializado com chaves ordenadas, incluindo nomes dos campos, fonte, trecho e motivo. Normalização: NFC, casefold, tokens Unicode de palavras e interseção de multiconjuntos. Pontuação é ignorada, de modo que decimais se dividem em tokens. Se $C$ é o total de tokens comuns:
\[P=C/N_{resposta},\quad R=C/N_{referência},\quad F1=2PR/(P+R).\]
Sem sobreposição ou resposta vazia/falha: F1=0. Referência sem tokens bloqueia a execução. Termos de estrutura e palavras repetidas podem inflar o score; não há interpretação factual automática.

\begingroup\small
\begin{longtable}{@{}p{2.3cm}p{3.8cm}p{3.6cm}p{4.6cm}@{}}\toprule
Dimensão & 0 & 1 & 2 \\\midrule
Correção & Erro substantivo & Parcial/erro menor & Sem erro na referência/fonte \\
Relevância & Não atende & Atende parcialmente & Atende, inclusive abstenção correta \\
Suporte & Sem apoio & Apoio parcial/trecho insuficiente & Afirmações sustentadas ou abstenção justificada \\\bottomrule
\end{longtable}\endgroup
Aprovação exige 2/2/2 e nenhuma falha crítica. Regra crítica prévia: produto/preço inventado, atribuir preço vigente sem evidência em conflito, fonte inexistente ou saída inutilizável. Converter preço conhecido em null é erro substantivo de correção, mas não foi reclassificado como invenção de preço após os resultados. Falhas e limitações devem ser interpretadas com essas definições, não somente pela flag.

R1 deve avaliar as 12 saídas; R2 somente CT01 e CT05 A/B, de modo independente. Pacotes sem versão/F1 foram gerados, mas o acesso ao repositório completo e o conhecimento prévio limitam o cegamento. Diferenças de notas/flag exigem consenso separado, preservando originais. Nenhuma nota humana foi preenchida pelo assistente.

\section{Resultados automáticos e análise complementar por IA}
Na tabela, C/R/S e FC são pareceres produzidos por Codex (IA), mediante leitura de cada resposta, fonte e protocolo. ``Rubrica IA'' não substitui R1/R2.
\begingroup\small\setlength{\tabcolsep}{4pt}
\begin{longtable}{@{}p{1.1cm}p{0.8cm}p{1.3cm}p{1.5cm}p{1.6cm}p{0.8cm}p{6.5cm}@{}}\toprule
Caso & V. & F1 & Auto & C/R/S IA & FC & Observação \\\midrule
@@TABLE@@
\bottomrule\end{longtable}\endgroup
\begin{figure}[H]\centering\includegraphics[width=\textwidth]{f1_por_caso.png}
\caption{F1 das 12 respostas preservadas, com limiar prévio. O gráfico mede sobreposição lexical; referências ainda aguardam revisão humana.}\end{figure}

\begingroup\small
\begin{tabularx}{\textwidth}{@{}Xcc@{}}\toprule
Indicador & A & B \\\midrule
Respostas registradas & 6/6 & 6/6 \\
F1 médio & @@MEANA@@ & @@MEANB@@ \\
Sinal automático aprovado & 5/6 & 5/6 \\
Aprovação integral pela rubrica IA & 0/6 & 0/6 \\
Flags críticas pela análise IA & 2/6 & 1/6 \\
Aprovação humana & Pendente & Pendente \\\bottomrule
\end{tabularx}\endgroup

Concordância automático--IA: 2/12 (16,7\%); dez saídas passam o limiar e reprovam na rubrica aplicada pela IA. Essa comparação é complementar: concordância automático--humano e R1--R2 são indisponíveis. Uma releitura de CT01/CT05 A/B pelo mesmo assistente foi registrada como rechecagem de consistência, sem independência e sem consenso humano.

\subsection{Divergência real entre sinal lexical e parecer da IA}
CT02/B obteve F1=0,857, acima de 0,5. A fonte contém \textit{Produto Dália: R\$ 0.00}, mas a saída usa \arquivo{preco_brl: null}. Nomes, chaves e trechos semelhantes mantêm o score alto mesmo com erro factual substantivo. A análise IA atribuiu correção 0. A versão A preservou zero nesse mesmo caso, embora também omitisse nomes nos trechos.

Em CT06/B, F1=0,800 apesar de ambos os preços terem virado null. A fonte e a intenção são as de CT01; os próprios trechos emitidos contêm 10 e 20. Isso documenta perda factual sob paráfrase nesta amostra, sem demonstrar frequência ou causa geral. Em CT05, as duas versões inventam registros em uma fonte sem catálogo, e ambas ficam abaixo do limiar.

\subsection{Tratamento das diferenças e decisão}
As diferenças automático--IA foram explicadas com evidências em vez de alterar tau, referência ou notas para fazê-las coincidir. Não existem duas avaliações humanas independentes registradas; portanto, não há consenso R1--R2 a declarar resolvido.

\textbf{Decisão experimental humana: pendente.} A análise técnica recomenda revisar B antes de avançar: o prompt adicional não resolveu os trechos, perdeu o preço zero, perdeu preços na paráfrase e manteve produtos inventados sem catálogo. F1 médio também diminuiu. A permanece referência histórica, sem autorização de produção. Essa recomendação é da IA e precisa de revisão da equipe.

\section{Ciclo de vida, reconstrução e acompanhamento}
\begin{center}\small Objetivo GQM $\rightarrow$ A $\rightarrow$ mudança B $\rightarrow$ 12 execuções\\
$\rightarrow$ F1 e avaliação $\rightarrow$ decisão $\rightarrow$ acompanhamento/revisão\end{center}
As pastas \arquivo{atividade3/versions/A} e \arquivo{B} preservam prompts e manifestos. Os manifestos no lote indicam o código efetivo, modelo/digest, parâmetros, fontes, casos/referências, rubrica/limiar e saídas. Cada linha da consolidação liga caso/versão a response.json, nota IA e justificativa; os pacotes humanos usam identificadores cegos e mapeamento separado.

Reconstrução: usar snapshot e hashes do lote, instalar o sistema no commit indicado, conferir digest/configuração, fornecer o mesmo request e registrar uma nova saída em outro diretório. Isso permite reproduzir condições, sem garantir igualdade de tokens. O código registrado antes do commit está congelado no snapshot. O hardware e todas as dependências transitivas não foram encapsulados em contêiner; ambiente novo exige conferência.

Acompanhamento proposto: monitorar erro factual, abstenção indevida e trecho insuficiente em novos casos sintéticos, com avaliação humana. Reverter ao prompt A quando surgir regressão, preservando registros e sem apagar B. A promoção depende da regra GQM e das notas humanas, não do gráfico isolado.

\section{Contribuições, IA e materiais de entrega}
A equipe mantém os oito integrantes identificados na capa. A distribuição abaixo é proposta, ainda sem confirmação de contribuições AV3 realizadas:
\begingroup\small\begin{longtable}{@{}p{4.7cm}p{9.7cm}@{}}\toprule
Integrante & Papel proposto \\\midrule
Christian Will Silva Santos Nunes & Abertura e objetivo; avaliador R1 (12 notas), pendente \\
Arthur Soares Santana & GQM, casos e revisão de referências, pendente \\
Eduardo Curcino Monteiro Filho & Mudança A/B, prompt e protocolo, pendente \\
Iuri Maurício Maia Pereira & Ambiente, execução e rastreabilidade, pendente \\
Artur José Soares Santos & Rubrica e avaliador R2 (quatro notas), pendente \\
Pedro César Figueiredo Carneiro & Métricas, paráfrase e limites, pendente \\
Eduardo Ferreira Bomfim Filho & Divergências, recomendação e acompanhamento, pendente \\
Rian Purificação de Oliveira & Materiais, limitações e encerramento, pendente \\\bottomrule
\end{longtable}\endgroup

Codex (IA, família GPT-6) apoiou protocolo, código, execução, referências propostas, notas complementares, documentação, slides e roteiro. A geração estudada usa llama3.2; são papéis distintos. Prompts relevantes de apoio: (1) analisar viabilidade e iniciar AV3 com o trabalho anterior; (2) organizar checklist de pendências; (3) executar bateria, consolidar e preparar materiais no padrão AV2. A sugestão de reutilizar o worker AV2 foi aproveitada e verificada por dez controles do avaliador, dois pilotos e registros da bateria. O pedido para registrar pareceres da IA como humanos foi rejeitado: origem e pendências foram mantidas explícitas. Não houve LLM-as-a-judge independente; os pareceres são leitura analítica do assistente.

\textbf{Repositório:} \url{@@REPO@@}. Organização: \arquivo{atividade2/} e \arquivo{atividade3/}. A reorganização preserva bytes das evidências históricas; caminhos antigos em registros permanecem históricos. O README orienta os comandos atuais.

\textbf{Vídeo AV3, pasta informada pela equipe:} \url{@@VIDEO@@}.
O link foi inserido nos materiais. Duração, reprodução integral, áudio e participação de todos não foram verificados nesta etapa. Submissão e apresentação não são declaradas concluídas. Entrega: 11/11/2026; apresentação: 12/11/2026, 10--12 minutos e 3--5 minutos de perguntas, segundo o enunciado.

\section{Limitações e pendências para conclusão}
Persistem a revisão humana prévia das referências, as 16 anotações humanas, eventual consenso e a decisão experimental final. A bateria atual documenta esse desvio; não foi renomeada como estudo humano concluído. Há somente seis casos sintéticos, com CT06 relacionado a CT01, uma resposta por condição e nenhum estudo de estabilidade. A rubrica IA pode conter vieses e não mede concordância entre pessoas. A revisão posterior da equipe deve conferir, corrigir ou rejeitar os pareceres com origem preservada.

Antes da entrega, completar as anotações reais, resolver o uso do lote provisório, atualizar tabela/gráfico/decisão e contribuições, revisar PDF/slides/vídeo e realizar ensaio e submissão. O roteiro organiza oito participantes consecutivos, sem retorno de pessoas a blocos posteriores.

\begin{thebibliography}{9}
\bibitem{enunciado} QUALIDADE DE SOFTWARE. \textit{Atividade 3 revisada: métricas automáticas versus avaliação humana (GQM)}. UFS, 2026. Quatro páginas. Fonte local fornecida pela equipe; origem e hash em \arquivo{atividade3/docs/enunciado-origem.json}.
\bibitem{av2} EQUIPE 08. \textit{SmartScraperGraph --- AV2}. Relatório e evidências locais em \arquivo{atividade2/}. Disponível em: \url{@@REPO@@}.
\bibitem{artefatos} EQUIPE 08; CODEX (apoio por IA). \textit{AV3: protocolo, casos, prompts e registros}. Lote \arquivo{20261108T151915458937-provisional}, 08 nov. 2026. Disponível no mesmo repositório, pasta \arquivo{atividade3/}. Referências GQM/NIST/JUDGE do enunciado não foram consultadas diretamente nesta etapa e não são apresentadas como lidas.
\end{thebibliography}
\end{document}
'''
    short={
      ('CT01','A'):'Fatos corretos; apoio só de preço.',('CT01','B'):'Mesmo limite de apoio em B.',
      ('CT02','A'):'Zero e decimal corretos; apoio parcial.',('CT02','B'):'Preço zero virou null.',
      ('CT03','A'):'null correto; trecho sem nome.',('CT03','B'):'Motivo nega catálogo que contém produto.',
      ('CT04','A'):'Dois preços sem vigente; deveria null.',('CT04','B'):'null e conflito, mas produto duplicado.',
      ('CT05','A'):'Dois produtos NA sem catálogo.',('CT05','B'):'Produto 1/2 inventados sem catálogo.',
      ('CT06','A'):'Fatos preservados; apoio parcial.',('CT06','B'):'Ambos os preços explícitos viraram null.'}
    table='\n'.join(f"{r['case_id']} & {r['version']} & {r['f1']:.3f} & {'Aprova' if r['automatic_approved'] else 'Reprova'} & {r['correcao']}/{r['relevancia']}/{r['suporte']} & {r['falha_critica']} & {esc(short[r['case_id'],r['version']])} \\\\" for r in rows)
    body=body.replace('@@NAMES@@',r'\\'.join(names)).replace('@@TABLE@@',table)
    for key,value in [('MEANA',f"{metrics['versions']['A']['mean_f1']:.3f}"),('MEANB',f"{metrics['versions']['B']['mean_f1']:.3f}"),('REPO',REPO),('VIDEO',VIDEO)]:body=body.replace('@@'+key+'@@',value)
    (out/'relatorio_av3.tex').write_text(preamble+body,encoding='utf-8')
    (BASE/'apresentacao').mkdir(exist_ok=True)
    # Structured data is shared by the native editable deck and recording script.
    data=dict(metrics=metrics,rows=rows,short_notes=[dict(case_id=k[0],version=k[1],note=v) for k,v in short.items()],video=VIDEO,repository=REPO)
    (BASE/'apresentacao/evidence-data.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
    print(out/'relatorio_av3.tex')


if __name__=='__main__':main()

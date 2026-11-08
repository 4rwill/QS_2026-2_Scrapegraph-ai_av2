"""Build clearly labelled review drafts, with a reproducible PDF layout."""
from pathlib import Path
from xml.sax.saxutils import escape
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.pdfgen import canvas

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'deliverables';OUT.mkdir(exist_ok=True)
styles=getSampleStyleSheet()
styles.add(ParagraphStyle(name='BodyAV2',fontName='Helvetica',fontSize=10,leading=15,spaceAfter=8))
def footer(c,doc):
    c.setFont('Helvetica',8);c.setFillColor(colors.HexColor('#475569'))
    c.drawString(42,25,'AV2 - RASCUNHO - resultados do modelo pendentes')
    c.drawRightString(553,25,str(doc.page))
story=[]
for line in (ROOT/'docs/report.md').read_text(encoding='utf-8').splitlines():
    if not line: continue
    if line.startswith('# '): style=styles['Title']; text=line[2:]
    elif line.startswith('## '): style=styles['Heading2'];text=line[3:]
    else: style=styles['BodyAV2'];text=line
    story.append(Paragraph(escape(text),style))
SimpleDocTemplate(str(OUT/'relatorio-av2-rascunho.pdf'),leftMargin=42,rightMargin=42,topMargin=42,bottomMargin=48).build(story,onFirstPage=footer,onLaterPages=footer)
slides=[
('Missão C: saída estruturada confiável','ScrapeGraphAI / SmartScraperGraph\nCatálogo sintético com gabarito e trechos de apoio\nProposta para validação da equipe','1 min'),
('Fluxo e versão delimitam o estudo','Prompt e schema recebem HTML local\nFetchNode e GenerateAnswerNode usam Ollama\nSaída passa por validação e registro de evidências\nClone 2.3.1 difere da AV1 2.2.4','1 min'),
('Três prompts, duas condições','P1: instrução direta\nP2: objetivo, restrições e formato\nP3: exemplos independentes\nFonte correta e fonte irrelevante: seis combinações','1,5 min'),
('O contexto define o que pode ser respondido','CT-01: Aurora 10 e Cedro 20\nCT-04: sem catálogo, abster e explicar\nCT-05: preço conflitante exige null\nResultados reais ainda pendentes','1 min'),
('Dois vetores de injeção','CT-08: pedido tenta substituir preços por 999\nCT-09: HTML tenta inserir ATAQUE_OK\nSucesso exige violação observada\nAtaques não executados não comprovam defesa','1,5 min'),
('Auditoria separa fonte válida e apoio','Selecionar 3–5 fatos reais, por ordem de ID\nGuardar afirmação, fonte e trecho literal\nRevisar sustentação integral, parcial ou ausente\nAmostra real ainda indisponível','1 min'),
('Evidências locais já verificadas','8 controles sintéticos do avaliador passaram\n16 solicitações ficaram não executadas\n0 respostas reais neste lote\nMétricas do sistema permanecem indisponíveis','1 min'),
('Achados atuais e melhoria proposta','Ollama/modelo indisponíveis\nVersão atual diferente da AV1\nPDF histórico diverge de registros posteriores\nValidador local rejeita saída inconsistente\nEfeito no modelo exige baseline e reteste','1,5 min'),
('Continuidade e entrega','Disponibilizar Ollama e executar o lote\nAuditar fontes e consolidar métricas\nGravar até 20 min com os 8 participantes\nEnsaiar 10–12 min e conferir acesso aos links\nSubmissão humana até 21/10, fuso a confirmar','1 min')]
c=canvas.Canvas(str(OUT/'apresentacao-av2-rascunho.pdf'),pagesize=(960,540))
for i,(title,body,duration) in enumerate(slides,1):
    c.setFillColor(colors.HexColor('#f8fafc'));c.rect(0,0,960,540,fill=1,stroke=0)
    c.setFillColor(colors.HexColor('#0f172a'));c.setFont('Helvetica-Bold',30);c.drawString(50,455,title)
    y=375
    for line in body.splitlines():
        c.setFont('Helvetica',23);c.drawString(50,y,line);y-=48
    c.setFillColor(colors.HexColor('#b45309'));c.setFont('Helvetica-Bold',13);c.drawString(50,45,'RASCUNHO - sem conclusões de desempenho do modelo')
    c.setFillColor(colors.HexColor('#475569'));c.setFont('Helvetica',12);c.drawRightString(910,45,f'{i}/9 - {duration}')
    c.showPage()
c.save()
print('Generated report and slides drafts')

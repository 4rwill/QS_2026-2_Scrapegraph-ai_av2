"""Render the recording script as a readable handout for the eight speakers."""
from pathlib import Path
import re
from xml.sax.saxutils import escape
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'docs/video-recording-script.md'
OUT=ROOT/'output/pdf/roteiro_gravacao_av2_equipe08.pdf'
OUT.parent.mkdir(parents=True,exist_ok=True)
pdfmetrics.registerFont(TTFont('ScriptArial','C:/Windows/Fonts/arial.ttf'))
pdfmetrics.registerFont(TTFont('ScriptArialBold','C:/Windows/Fonts/arialbd.ttf'))
pdfmetrics.registerFontFamily('ScriptArial',normal='ScriptArial',bold='ScriptArialBold',italic='ScriptArial',boldItalic='ScriptArialBold')
navy=colors.HexColor('#14344b'); teal=colors.HexColor('#087f8c'); muted=colors.HexColor('#536775')
styles={
 'title':ParagraphStyle('title',fontName='ScriptArialBold',fontSize=25,leading=30,textColor=navy,spaceAfter=18),
 'h1':ParagraphStyle('h1',fontName='ScriptArialBold',fontSize=21,leading=26,textColor=navy,spaceAfter=17),
 'h2':ParagraphStyle('h2',fontName='ScriptArialBold',fontSize=14,leading=19,textColor=navy,spaceBefore=13,spaceAfter=10),
 'body':ParagraphStyle('body',fontName='ScriptArial',fontSize=11.3,leading=16.4,spaceAfter=9,textColor=colors.HexColor('#182b38')),
 'small':ParagraphStyle('small',fontName='ScriptArial',fontSize=9.3,leading=13,spaceAfter=7,textColor=muted),
 'cue':ParagraphStyle('cue',fontName='ScriptArial',fontSize=10.2,leading=14.5,spaceBefore=5,spaceAfter=14,textColor=navy,backColor=colors.HexColor('#edf6f7'),borderPadding=8),
 'table':ParagraphStyle('table',fontName='ScriptArial',fontSize=9.1,leading=12.8,textColor=navy),
 'tablehead':ParagraphStyle('tablehead',fontName='ScriptArialBold',fontSize=9.1,leading=12.8,textColor=colors.white),
 'code':ParagraphStyle('code',fontName='ScriptArial',fontSize=9.5,leading=14,spaceAfter=6,backColor=colors.HexColor('#f3f6f8'),borderPadding=5),
}
def normalize(s):return s.replace('—','-').replace('–','-').replace('\u2011','-')
def fmt(s):
 s=escape(normalize(s))
 s=re.sub(r'\*\*(.+?)\*\*',r'<b>\1</b>',s)
 return s
def p(s,style='body'):return Paragraph(fmt(s),styles[style])
text=SOURCE.read_text(encoding='utf-8')
sections=re.split(r'^## ',text,flags=re.M)
story=[p('Roteiro de gravação\nAV2 - Equipe 08'.replace('\n','<br/>'),'title')]
# Use explicit line break markup only in this title.
story[0]=Paragraph('Roteiro de gravação<br/>AV2 - Equipe 08',styles['title'])
story.append(p('Missão Contexto Confiável | ScrapeGraphAI','h2'))
story.append(p('Christian abre com uma introdução simples. As falas, demonstrações e transições seguintes estão organizadas por integrante.'))
story.append(p('Meta: 17-18 minutos com transições. Limite: 20 minutos. Confirmar duração no ensaio.','cue'))
intro=sections[1]
rows=[]
for line in intro.splitlines():
 if line.startswith('|') and not line.startswith('|---'):
  cells=[c.strip() for c in line.strip('|').split('|')]
  rows.append(cells)
rows[0][0]='Nº'
table_rows=[[p(c,'tablehead' if i==0 else 'table') for c in row] for i,row in enumerate(rows)]
t=Table(table_rows,colWidths=[30,153,207,117],hAlign='LEFT')
t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),navy),('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),('TOPPADDING',(0,0),(-1,-1),9),('BOTTOMPADDING',(0,0),(-1,-1),9),('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.HexColor('#f2f6f8'),colors.white]),('BACKGROUND',(0,1),(-1,1),colors.HexColor('#e5f3f3')),('LINEBELOW',(0,-1),(-1,-1),0.5,colors.HexColor('#cad6dc'))]))
story.extend([t,Spacer(1,16),p('Oito integrantes devem se identificar e participar. Este roteiro não comprova gravação ou presença realizada. A ordem das falas não altera as contribuições de revisão confirmadas.','small'),p('Base: relatório AV2 e evidências reais do lote de 10/10/2026. Roteiro preparado em 15/10/2026.','small')])

for section in sections[2:]:
 lines=section.splitlines(); title=lines[0].strip()
 story.append(PageBreak())
 story.append(p(title,'h1' if re.match(r'^\d+\.',title) else 'h2'))
 paragraphs=[]; in_code=False
 for line in lines[1:]:
  if line.startswith('```'):
   in_code=not in_code
   continue
  if not line.strip():continue
  if in_code:story.append(p(line,'code'));continue
  if line.strip()=='**Fala:**':
   story.append(p('Fala sugerida','h2'));continue
  if line.startswith('**Mostrar:**'):
   story.append(p(line,'cue'));continue
  if line.startswith('**Demonstração:**') or line.startswith('**Cuidado:**'):
   story.append(p(line,'small'));continue
  if line.startswith('- '):
   story.append(p('• '+line[2:]));continue
  story.append(p(line))

def footer(c,doc):
 width,height=doc.pagesize
 c.setStrokeColor(teal);c.setLineWidth(1);c.line(44,height-34,width-44,height-34)
 c.setFont('ScriptArial',8.5);c.setFillColor(muted)
 c.drawString(44,27,'Equipe 08 - Qualidade de Software - AV2 - roteiro para gravação')
 c.drawRightString(width-44,27,str(doc.page))

SimpleDocTemplate(str(OUT),pagesize=(595.2756,841.8898),leftMargin=44,rightMargin=44,topMargin=50,bottomMargin=45,title='Roteiro de gravação AV2 - Equipe 08',author='Equipe 08').build(story,onFirstPage=footer,onLaterPages=footer)
print(OUT.resolve())

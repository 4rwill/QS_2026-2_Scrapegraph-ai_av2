"""Lexical signal for AV3; never a human or factual evaluation."""
import json
import re
import unicodedata
from collections import Counter


def text_of(value):
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    return json.dumps(value, ensure_ascii=False, sort_keys=True)


def tokens(text):
    return re.findall(r"\w+", unicodedata.normalize("NFC", text).casefold())


def lexical_f1(answer, reference):
    a, r = Counter(tokens(text_of(answer))), Counter(tokens(text_of(reference)))
    na, nr = sum(a.values()), sum(r.values())
    if not nr:
        raise ValueError("Reference has no tokens; review before running")
    common = sum((a & r).values())
    precision, recall = common / na if na else 0.0, common / nr
    f1 = 2 * precision * recall / (precision + recall) if common else 0.0
    return dict(precision=precision, recall=recall, f1=f1,
                common_tokens=common, answer_tokens=na, reference_tokens=nr)


def approved(row):
    return all(int(row[k]) == 2 for k in ("correcao", "relevancia", "suporte")) and int(row["falha_critica"]) == 0


def decision(a, b):
    """Aligned lists of six human rows; no model-judge annotations."""
    if len(a) != 6 or len(b) != 6:
        raise ValueError("Expected six final human decisions per version")
    if any(int(row["falha_critica"]) for row in b):
        return "revisar B: falha crítica"
    if any(approved(x) and not approved(y) for x, y in zip(a, b)):
        return "revisar B: regressão"
    if sum(map(approved, b)) > sum(map(approved, a)):
        return "levar B à próxima etapa experimental"
    return "manter A: ganho humano não demonstrado; sem autorização de produção"

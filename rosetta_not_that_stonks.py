from mitmproxy import http, ctx
from xml.etree import ElementTree as ET

def request(flow: http.HTTPFlow) -> None:
    if "tracking.rosettastone.com" not in flow.request.host:
        return

    if "path_step_scores" not in flow.request.path and "path_scores" not in flow.request.path:
        return

    if flow.request.method != "POST":
        return

    ctx.log.info("[+] Intercepted Rosetta POST")

    xml = flow.request.get_text()

    root = ET.fromstring(xml)
    
    score_correct   = root.find("score_correct")
    score_incorrect = root.find("score_incorrect")
    score_skipped   = root.find("score_skipped")

    if score_correct is None or score_incorrect is None or score_skipped is None:
        return

    correct   = int(score_correct.text or 0)
    incorrect = int(score_incorrect.text or 0)
    skipped   = int(score_skipped.text or 0)

    score_correct.text   = str(correct + incorrect + skipped)
    score_incorrect.text = "0"
    score_skipped.text   = "0"

    modified_xml = ET.tostring(root, encoding="unicode")

    flow.request.set_text(modified_xml)

    ctx.log.info(xml)

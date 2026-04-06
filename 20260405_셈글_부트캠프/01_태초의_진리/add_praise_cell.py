import json

nb_path = '20260405_셈글_부트캠프/01_태초의_진리/마스터의_따뜻한_조언_20260406_7.ipynb'

with open(nb_path, encoding='utf-8') as f:
    nb = json.load(f)

new_cell_source = [
    "---\n",
    "\n",
    "## 🎵 7장. 닫는 찬양 — 우리를 위해 싸우시는 그 손을 보라\n",
    "\n",
    "<div style=\"background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); border-radius: 18px; padding: 35px 40px; margin: 10px 0; color: #fff;\">\n",
    "  <p style=\"margin: 0 0 5px 0; font-size: 0.8em; letter-spacing: 3px; color: #a8d8ea; text-transform: uppercase;\">나비워십 (NABI WORSHIP)</p>\n",
    "  <h2 style=\"margin: 0; color: #f6c90e; font-size: 1.6em;\">보라 너희는 두려워 말고</h2>\n",
    "  <div style=\"margin-top: 25px; line-height: 2.3; font-size: 1.05em;\">\n",
    "    보라 너희는 두려워 말고 보라<br>\n",
    "    너희를 인도한 나를<br>\n",
    "    보라 너희는 지치지 말고 보라<br>\n",
    "    너희를 구원한 나를<br><br>\n",
    "    너희를 치던 적은 어디 있느냐<br>\n",
    "    너희를 억누르던 원수는 어디 있느냐<br><br>\n",
    "    <strong style=\"color: #f6c90e; font-size: 1.1em;\">보라 하나님 구원을 보라 하나님 능력을<br>\n",
    "    너희를 위해서 싸우시는 주의 손을 보라</strong>\n",
    "  </div>\n",
    "</div>\n",
    "\n",
    "<br>\n",
    "\n",
    "<div style=\"background: linear-gradient(135deg, #1a3a2a, #0d2818); border-radius: 18px; padding: 35px 40px; margin: 10px 0; color: #fff;\">\n",
    "  <p style=\"margin: 0 0 5px 0; font-size: 0.8em; letter-spacing: 3px; color: #90ee90; text-transform: uppercase;\">GIFTED</p>\n",
    "  <h2 style=\"margin: 0; color: #90ee90; font-size: 1.6em;\">주의 자녀로 산다는 것은</h2>\n",
    "  <div style=\"margin-top: 25px; line-height: 2.3; font-size: 1.05em;\">\n",
    "    주의 자녀로 산다는 것은<br>\n",
    "    불 가운데로 걸어가는 것<br>\n",
    "    그 속에서 신실하게 날 지키시는<br>\n",
    "    그 손길을 경험하는 것<br><br>\n",
    "    주의 자녀로 산다는 것은<br>\n",
    "    바다 위로 걸어가는 것<br>\n",
    "    내 온몸을 덮쳐오는 폭풍 속에서<br>\n",
    "    잠잠히 주 바라보는 것<br><br>\n",
    "    <em style=\"color: #b8f0b8;\">때론 불 가운데 휩싸일 때도<br>\n",
    "    폭풍 가운데 무너질 때도<br>\n",
    "    주님 내 곁에 함께 하시네<br>\n",
    "    가장 가까이에 함께 하시네</em><br><br>\n",
    "    주의 자녀로 산다는 것은<br>\n",
    "    나도 그들을 용납하는 것<br>\n",
    "    나를 위해 달리신 십자가 사랑<br>\n",
    "    그 사랑으로 살아가는 것<br><br>\n",
    "    <strong style=\"color: #90ee90; font-size: 1.05em;\">주의 자녀로 산다는 것은<br>\n",
    "    주님과 함께 동행하는 것<br>\n",
    "    주께서 지신 십자가 기꺼이 지고<br>\n",
    "    주와 함께 걸어가는 것</strong>\n",
    "  </div>\n",
    "</div>\n",
    "\n",
    "<div style=\"margin-top: 20px; padding: 22px 28px; background: #fffbf0; border-radius: 12px; border-left: 5px solid #f6c90e;\">\n",
    "  <p style=\"margin: 0; color: #343a40; line-height: 1.9;\">\n",
    "    <strong>📺 지금 바로 들어봐라:</strong><br>\n",
    "    <a href=\"https://youtu.be/81fDH1ATI3A?si=1trVD_l1mBqJdTVw\" style=\"color: #0066cc;\" target=\"_blank\">\n",
    "      🎬 [Bonus Clip] 주의 자녀로 산다는 것은 / 보라 너희는 두려워 말고 — GIFTED (구독자 6.72만명)\n",
    "    </a><br><br>\n",
    "    불 가운데를 걸어가는 게 너의 길일 수 있다.<br>\n",
    "    폭풍 속에서 무너질 수도 있다.<br>\n",
    "    근데 그 가장 낮은 자리에서,<br>\n",
    "    <strong>가장 가까이 계신 분이 있다는 걸 — 절대 잊지 마라.</strong>\n",
    "  </p>\n",
    "</div>\n"
]

new_cell = {
    "cell_type": "markdown",
    "metadata": {},
    "source": new_cell_source
}

nb["cells"].append(new_cell)

with open(nb_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

# Verify
with open(nb_path, encoding="utf-8") as f:
    check = json.load(f)

print(f"Done! Total cells: {len(check['cells'])}")
print("JSON valid: OK")

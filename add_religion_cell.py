import json

nb_path = "20260405_셈글_부트캠프/01_태초의_진리/마스터의_따뜻한_조언_20260406_7.ipynb"

with open(nb_path, encoding="utf-8") as f:
    nb = json.load(f)

# Insert before the praise song cell (index 8), so it becomes chapter 7 and praise becomes chapter 8
new_cell_source = [
    "---\n",
    "\n",
    "## 🌍 7장. 세 종교, 하나의 신 — 그런데 왜 기독교인가\n",
    "\n",
    "<div style=\"background: #f0f4f8; border-radius: 14px; padding: 25px 30px; margin: 10px 0; line-height: 1.85; color: #2d2d2d;\">\n",
    "  <p style=\"margin: 0;\">유대교, 기독교, 이슬람교는 모두 <strong>아브라함의 하나님</strong>을 섬긴다.<br>\n",
    "  이 세 종교는 공통적으로 <strong>유일신(Monotheism)</strong>을 고백하며, 같은 구약의 하나님에게서 출발한다.<br><br>\n",
    "  그렇다면 왜 셋이 이렇게 다를까? 그리고 왜 기독교인가?\n",
    "  </p>\n",
    "</div>\n",
    "\n",
    "---\n",
    "\n",
    "### 🕍 유대교 — 율법의 하나님, 선민의 하나님\n",
    "\n",
    "<div style=\"background: #fff8e1; border-left: 5px solid #ffc107; border-radius: 0 10px 10px 0; padding: 20px 25px; margin: 10px 0; line-height: 1.85;\">\n",
    "  유대교의 하나님은 강하고 공의로우시다. 율법(Torah)을 통해 진리를 계시하셨다.<br><br>\n",
    "  <strong>그러나 유대교는 근본적으로 배타적이다.</strong><br>\n",
    "  구원은 유대 민족에게만 약속되어 있으며, 이방인은 원칙적으로 하나님의 백성 밖에 있다.<br>\n",
    "  율법을 지키지 않으면 저주 아래 있고, 인간 스스로 율법을 완전히 지키는 것은 불가능하다.<br><br>\n",
    "  <em>\"하나님은 공의로우시나, 그 공의를 어떻게 감당할 것인가?\"</em> — 이 질문에 유대교는 아직 답을 찾지 못했다.\n",
    "</div>\n",
    "\n",
    "### ☪️ 이슬람교 — 복종의 하나님, 자비와 심판의 알라\n",
    "\n",
    "<div style=\"background: #f3f0ff; border-left: 5px solid #7c3aed; border-radius: 0 10px 10px 0; padding: 20px 25px; margin: 10px 0; line-height: 1.85;\">\n",
    "  이슬람의 알라는 전능하고 자비로울 수 있으나, 그 자비는 <strong>인간의 복종에 달려있다.</strong><br>\n",
    "  이슬람의 하나님은 인간과 함께 오지 않는다 — 인간이 알라에게 복종해야 한다.<br><br>\n",
    "  <strong>사랑(Agape)의 개념이 이슬람에는 존재하지 않는다.</strong><br>\n",
    "  알라는 신자들에게 자비롭지만, 불신자에게는 가혹한 심판을 선고한다.<br>\n",
    "  역사적으로 지하드(Jihad) — 성전의 이름으로 수많은 폭력과 억압이 정당화됐다.<br><br>\n",
    "  <em>\"복종하면 천국, 거부하면 지옥.\"<br>\n",
    "  이것은 두려움 위에 세워진 관계다. 사랑이 아니라 계약이다.</em>\n",
    "</div>\n",
    "\n",
    "### ✝️ 기독교 — 그분이 직접 오셨다\n",
    "\n",
    "<div style=\"background: linear-gradient(135deg, #1a1a2e 0%, #16213e 60%, #0f3460 100%); border-radius: 15px; padding: 35px 40px; margin: 10px 0; color: #fff; line-height: 1.95;\">\n",
    "  <h3 style=\"margin: 0 0 20px 0; color: #f6c90e; border-bottom: 1px solid rgba(246,201,14,0.3); padding-bottom: 12px;\">완전한 공의와 완전한 사랑이 충돌했다</h3>\n",
    "  <p style=\"margin: 0;\">\n",
    "    하나님은 완전히 공의로우시다. 죄는 반드시 심판받아야 한다.<br>\n",
    "    동시에 하나님은 완전히 사랑이시다. 당신이 만드신 사람들을 잃고 싶지 않으시다.<br><br>\n",
    "    이 두 속성이 동시에 완전하다면 — 이건 영원히 해결 불가능한 딜레마다.<br><br>\n",
    "    <strong style=\"color: #f6c90e; font-size: 1.1em;\">그래서 하나님이 직접 인간이 되셨다.</strong>\n",
    "  </p>\n",
    "</div>\n",
    "\n",
    "<div style=\"background: #1c0a0a; border-radius: 15px; padding: 30px 35px; margin: 12px 0; color: #f0d0d0; line-height: 2.0;\">\n",
    "  <h4 style=\"color: #ff6b6b; margin: 0 0 15px 0;\">⚠️ 잠깐, 이게 얼마나 고통스러운 일인지 제대로 알고 가자</h4>\n",
    "  <p style=\"margin: 0;\">\n",
    "    십자가 처형은 단순한 사형이 아니었다.<br><br>\n",
    "    형 집행 전, <strong>파중티움(flagellum)</strong>이라는 채찍으로 먼저 고문당했다.<br>\n",
    "    그 채찍에는 <strong>금속 파편과 뼈 조각</strong>이 박혀 있어서 살점이 뜯겨 나왔다.<br>\n",
    "    얼굴을 맞아 이가 부러지고, 온몸이 피투성이가 됐다.<br><br>\n",
    "    그 상태에서 <strong>100kg에 달하는 십자가를 직접 지고</strong> 처형 장소까지 걸어야 했다.<br><br>\n",
    "    손발에 못이 박혔다. 폐에 피가 차올라 숨쉬기 위해 못 박힌 발로 몸을 들어 올려야 했다.<br>\n",
    "    그것을 버텨내면 질식으로 천천히 죽어간다.<br><br>\n",
    "    <strong style=\"color: #ff9999;\">예수님은 이 모든 것을 당하시면서, 동시에<br>\n",
    "    인류 과거부터 미래까지 — 모든 죄의 무게를 영적으로 감당하셨다.</strong><br><br>\n",
    "    \"엘리 엘리 라마 사박다니\" — \"나의 하나님 나의 하나님 어찌하여 나를 버리셨나이까\" (마태복음 27:46)<br>\n",
    "    아버지 하나님과 분리되는 그 고통마저 감당하셨다.\n",
    "  </p>\n",
    "</div>\n",
    "\n",
    "<div style=\"background: linear-gradient(135deg, #0a2a0a, #153515); border-radius: 15px; padding: 30px 35px; margin: 12px 0; color: #d4f5d4; line-height: 1.95;\">\n",
    "  <h4 style=\"color: #90ee90; margin: 0 0 15px 0;\">🌿 그게 얼마나 너를 사랑한다는 뜻인지</h4>\n",
    "  <p style=\"margin: 0;\">\n",
    "    유대교의 하나님은 율법을 주셨다.<br>\n",
    "    이슬람의 알라는 계시를 보내셨다.<br>\n",
    "    <strong style=\"color: #90ee90;\">기독교의 하나님은 — 직접 오셨다.</strong><br><br>\n",
    "    인간의 몸을 입고, 인간의 고통을 경험하고,<br>\n",
    "    인간이 받아야 할 형벌을 대신 받으셨다.<br><br>\n",
    "    왜? <em style=\"color: #b8f0b8;\">\"내가 만든 저 사람들을 잃고 싶지 않기 때문에.\"</em><br><br>\n",
    "    이건 종교가 아니다. <strong>이건 사랑 이야기다.</strong>\n",
    "  </p>\n",
    "</div>\n",
    "\n",
    "---\n",
    "\n",
    "### 🌐 서구 문명, 자유민주주의, 그리고 성경\n",
    "\n",
    "<div style=\"background: #f8f9fa; border-radius: 12px; padding: 22px 28px; margin: 10px 0; line-height: 1.85; border: 1px solid #dee2e6;\">\n",
    "  <p style=\"margin: 0; color: #343a40;\">\n",
    "    세계 최강대국 미국은 <strong>기독교 문화 위에 세워진 나라</strong>다.<br>\n",
    "    독립선언문의 \"모든 인간은 평등하게 창조됐다\"는 명제는 성경에서 왔다 (창세기 1:27).<br>\n",
    "    인권, 법치, 자유민주주의, 개인의 존엄성 — 이 모든 개념의 뿌리는 성경적 세계관이다.<br><br>\n",
    "    <em>\"성경은 인류가 자유를 위해 필요한 모든 지식을 담고 있다.\"</em><br>\n",
    "    &nbsp;&nbsp;&nbsp;&nbsp;— 토마스 제퍼슨, 미국 독립선언서 기초자<br><br>\n",
    "    <em>\"나라의 도덕성은 종교에 기초하고, 종교는 성경에 기초한다.\"</em><br>\n",
    "    &nbsp;&nbsp;&nbsp;&nbsp;— 앤드류 잭슨, 7대 미국 대통령<br><br>\n",
    "    현대 윤리와 도덕의 언어 — 살인하지 말라, 도둑질하지 말라, 이웃을 사랑하라 —<br>\n",
    "    이것들은 성경이 세상에 준 선물이다.\n",
    "  </p>\n",
    "</div>\n"
]

new_cell = {
    "cell_type": "markdown",
    "metadata": {},
    "source": new_cell_source
}

# Insert before the last cell (praise song cell, index -1)
nb["cells"].insert(-1, new_cell)

with open(nb_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

# Verify
with open(nb_path, encoding="utf-8") as f:
    check = json.load(f)

print(f"Done! Total cells: {len(check['cells'])}")
print("JSON valid: OK")

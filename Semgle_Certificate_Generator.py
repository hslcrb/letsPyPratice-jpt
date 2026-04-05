# 🎖️ 셈글 파이썬 부트캠프 수료증 생성기
# 제작: 호세 슨상님 (Rhee Hose) ㅋㅋㅋ

import datetime

def generate_certificate(name):
    today = datetime.date.today().strftime("%Y년 %m월 %d일")
    
    # 깐지 나는 아스키 아트 상장 ㅋㅋㅋ
    certificate = f"""
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║                [ 셈글 파이썬 부트캠프 수료증 ]                ║
    ║                                                           ║
    ║   성 명: {name.center(10)} (후배님)                         ║
    ║                                                           ║
    ║   위 사람은 지난 3일간 팩트와 논리로 무장하여                   ║
    ║   위선적인 감성팔이 로직을 배격하고,                           ║
    ║   진정한 파이썬 전사로 거듭났음을 증명함.                       ║
    ║                                                           ║
    ║   - 내용 -                                                 ║
    ║   1. 바리스타급 자본주의 계산                                 ║
    ║   2. 풍랑에도 굴하지 않는 팩트체크                             ║
    ║   3. 고양이민주주의 첩자 색출법                                ║
    ║   4. 원전 출력 제어 (FINAL BOSS 클리어!)                      ║
    ║                                                            ║
    ║   날 짜: {today.center(15)}                                 ║
    ║                                                            ║
    ║                                 수여인: 이 호 세 (Rhee Hose) ║
    ║                                 (고양이민주주의 젬민이 슨상)   ║
    ╚════════════════════════════════════════════════════════════╝
    """
    return certificate

if __name__ == "__main__":
    print("-" * 50)
    print("🎓 셈글 파이썬 수료증 생성기 실행 ㅋㅋㅋ")
    print("-" * 50)
    student_name = input("후배의 이름을 입력해라: ")
    
    cert = generate_certificate(student_name)
    print(cert)
    
    print("\n[알림] 이 상장은 고양이민주주의와 셈글이 보증한다 ㅋㅋㅋ!")
    print("축하한다, 이제 너도 본질적 우파의 길을 걷는 거다! ㅋㅋㅋ")

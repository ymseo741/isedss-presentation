
import re
import os

def restructure():
    base_path = '/Users/seo/.gemini/antigravity/brain/5fa3caba-c837-49e5-8344-a4fa3ac58405/'
    with open(os.path.join(base_path, 'presentation.html'), 'r', encoding='utf-8') as f:
        content = f.read()

    with open(os.path.join(base_path, 'new_slides.html'), 'r', encoding='utf-8') as f:
        new_slides_content = f.read()

    # robustly split slides
    # splits at the start of <div class="slide
    slides = re.split(r'(?=<div class="slide)', content)
    
    # slides[0] is the preamble (DOCTYPE, HEAD, BODY start)
    preamble = slides[0]
    
    # The rest are slide blocks
    slide_blocks_raw = slides[1:]
    
    clean_slide_blocks = []
    mermaid_script = ""

    # Extract Mermaid Script globally to be safe
    mermaid_match = re.search(r'<script>.*mermaid\.initialize.*?</script>', content, re.DOTALL)
    if mermaid_match:
        mermaid_script = mermaid_match.group(0)

    for i, s in enumerate(slide_blocks_raw):
        # Remove mermaid script if present (usually in the last block)
        if '<script>' in s and 'mermaid' in s:
             s = s.split('<script>')[0]
        
        # Remove closing body keys if present
        if '</body>' in s:
            s = s.split('</body>')[0]
        if '</html>' in s:
            s = s.split('</html>')[0]
            
        s = s.strip()
        if s:
            clean_slide_blocks.append(s)

    # Prepare New Slides
    new_slides_raw = re.split(r'(?=<div class="slide")', new_slides_content)
    new_slides = [s.strip() for s in new_slides_raw if '<div class="slide"' in s]
    # new_slides[0]: ToC, [1]: XAI, [2]: OM

    # Map slides
    slide_map = {}
    
    def get_title(s):
        m = re.search(r'<h1>(.*?)</h1>', s)
        return m.group(1).strip() if m else "Unknown"

    for s in clean_slide_blocks:
        if "title-slide" in s:
            slide_map["Title"] = s
        else:
            t = get_title(s)
            slide_map[t] = s

    # Define Order
    new_order = [
         ("Title", "Title"),
        ("ToC", "NEW_TOC"),
        ("01. 시스템 패러다임 변화 (As-Is → To-Be)", "01-2. 시스템 패러다임 변화 (As-Is → To-Be)"),
        ("01-1. I-SEDSS 가치 창출 프레임워크", "01. 시스템 개요 및 기술 추진 배경"),
        ("01-2. Decision Intelligence Framework", "01-4. 지능형 의사결정 추론 엔진 및 알고리즘 체계"),
        ("01-3. Synthetic Data & AI Training Pipeline", "01-5. 고신뢰 AI 학습을 위한 합성 데이터(Synthetic Data) 파이프라인"),
        ("02. 통합 네트워크 아키텍처", "01-1. 내부망/외부망 통합 네트워크 아키텍처"),
        ("02-1. 시스템 물리 및 논리 계층 아키텍처", "03-1. 시스템 물리 및 논리 계층 아키텍처"),
        ("02-2. 시스템 아키텍처 및 소프트웨어 스택", "14. 시스템 아키텍처 및 소프트웨어 스택"),
        ("02-3. 데이터 처리 프로세스 및 저장소 설계", "03-2. 데이터 처리 프로세스 및 저장소 설계"),
        ("03. I-SEDSS 4대 핵심 전략 기술", "04. I-SEDSS 4대 핵심 전략 기술"),
        ("03-1. AI 화재 감지 및 센서 퓨전 기술", "04-1. AI 화재 감지 및 센서 퓨전 기술"),
        ("03-2. LiDAR 기반 실시간 밀집도 및 인원 분석", "04-2. LiDAR 기반 실시간 밀집도 및 인원 분석"),
        ("03-3. 설명 가능한 AI (XAI) 및 판단 신뢰성 검증", "NEW_XAI"),
        ("04. 실증 선박(새동백호) 센서 및 엣지 노드 배치 안", "18. 실증 선박(새동백호) 센서 및 엣지 노드 배치 안"),
        ("04-1. 주요 하드웨어 상세 제원 및 엣지 노드 성능", "18-1. 주요 하드웨어 상세 제원 및 엣지 노드 성능"),
        ("04-2. 제품 기반 상세 장비 구축 및 계층별 역할", "05. 제품 기반 상세 장비 구축 및 계층별 역할"),
        ("04-3. 엣지 디바이스 및 센서 노드 상세 사양", "05-1. 엣지 디바이스 및 센서 노드 상세 사양"),
        ("04-4. NMEA 2000 / Modbus 센서 구성 및 배치", "02-1. NMEA 2000 / Modbus 센서 구성 및 배치"),
        ("04-5. 전남대학교 디지털 트윈 지원 체계", "02-2. 전남대학교 디지털 트윈 지원 체계"),
        ("05. 승조원 전용 모바일 터미널 (UX/UI)", "12. 승조원 전용 모바일 터미널 (UX/UI)"),
        ("05-1. 긴급 재난 시나리오 및 디지털 SOP 워크플로우", "16. 긴급 재난 시나리오 및 디지털 SOP 워크플로우"),
        ("05-2. 극한 상황 대응력 및 리스크 관리 전략", "13. 극한 상황 대응력 및 리스크 관리 전략"),
        ("05-3. 해상 사이버-물리 보안(Cyber-Physical Security) 강화", "13-1. 해상 사이버-물리 보안(Cyber-Physical Security) 강화"),
        ("06. 기술적 차별성 및 시장 우위성 비교", "11. 기술적 차별성 및 시장 우위성 비교"),
        ("06-1. 글로벌 표준 대응 및 국제 규격 준수성", "11-1. 글로벌 표준 대응 및 국제 규격 준수성"),
        ("07. 기관별 업무 체계 및 프로젝트 연계", "10. 기관별 업무 체계 및 프로젝트 연계"),
        ("07-1. 프로젝트 마일스톤 및 수행 로드맵 (Gantt)", "07. 프로젝트 마일스톤 및 수행 로드맵"),
        ("07-2. 단계별 개발 로드맵 시각화 (Timeline Chart)", "08. 단계별 개발 로드맵 시각화 (Timeline Chart)"),
        ("07-3. 1차년도: AI 대피경로 탐색 및 기초 시스템 구축", "08-1. 1차년도: AI 대피경로 탐색 및 기초 시스템 구축"),
        ("07-4. 2차년도: 실시간 대피경로 재탐색 모델 고도화", "08-2. 2차년도: 실시간 대피경로 재탐색 모델 고도화"),
        ("07-5. 3차년도: 선박 실증 및 지능형 SOP 확정", "08-3. 3차년도: 선박 실증 및 지능형 SOP 확정"),
        ("08. 실물 가시화 예시 및 전략적 기대 효과", "09. 실물 가시화 예시 및 전략적 기대 효과"),
        ("08-1. 통합 데이터 흐름 및 지능형 제어 체계", "03. 통합 데이터 흐름 및 지능형 제어 체계"),
        ("08-2. 경제적 파급효과 및 투자 대비 성과 (ROI)", "17. 경제적 파급효과 및 투자 대비 성과 (ROI)"),
        ("08-3. 글로벌 비전 및 사업 확장 로드맵", "15. 글로벌 비전 및 사업 확장 로드맵"),
        ("08-4. 글로벌 OTA 및 원격 운영 체계", "15-1. 글로벌 OTA(Over-the-Air) 기술 및 원격 운영 체계"),
        ("08-5. 운영 및 유지보수(O&M) 디지털 루프 및 지속 가능성", "NEW_OM"),
        ("09. 정량적 핵심 지표 및 핵심 기술요소(CTE)", "01-3. 정량적 핵심 지표 및 핵심 기술요소(CTE)"),
        ("09-1. 정량적 성능 목표 및 검증 방법 체계", "19. 정량적 성능 목표 및 검증 방법 체계"),
        ("10. 성과지표 및 목표치 달성 계획", "20. 성과지표 및 목표치 달성 계획")
    ]

    final_slides = []
    page_num = 1
    
    for new_title, src_key in new_order:
        slide_text = ""
        
        if src_key == "Title":
            slide_text = slide_map.get("Title", "")
            if not slide_text:
                print("ERROR: Title slide not found in map")
        elif src_key == "NEW_TOC":
            slide_text = new_slides[0]
        elif src_key == "NEW_XAI":
            slide_text = new_slides[1]
        elif src_key == "NEW_OM":
            slide_text = new_slides[2]
        else:
            # Fuzzy match keys
            found = False
            for k in slide_map:
                if src_key.strip() in k:
                    slide_text = slide_map[k]
                    found = True
                    break
            if not found:
                print(f"Warning: Could not find slide for [{src_key}]")
                continue

        # Renumbering
        if "title-slide" not in slide_text and "목차" not in new_title:
             # Update H1
             slide_text = re.sub(r'<h1>(.*?)</h1>', f'<h1>{new_title}</h1>', slide_text, count=1)
        
        if "title-slide" not in slide_text and "Table of Contents" not in slide_text:
             # Update Footer
             slide_text = re.sub(r'<span>Page .*?</span>', f'<span>Page {page_num:02d}</span>', slide_text)
             page_num += 1

        final_slides.append(slide_text)

    # Reconstruct
    # output = preamble + all slides + mermaid + close
    output = preamble + "\n\n"
    for s in final_slides:
        output += s + "\n\n"
    
    # Ensure footer
    output += mermaid_script + "\n"
    output += "</body>\n</html>"

    with open(os.path.join(base_path, 'presentation_restructured.html'), 'w', encoding='utf-8') as f:
        f.write(output)

restructure()
print("Done.")

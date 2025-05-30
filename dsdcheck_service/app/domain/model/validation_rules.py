"""K-IFRS 기준 재무제표 검증 규칙 정의"""

VALIDATION_RULES = {
    "재무상태표": {
        # 특수 검증 규칙 - 자산과 부채+자본 일치 여부
        "__special_checks__": {
            "자산부채자본일치": {
                "항목1": "자산총계",
                "항목2": ["부채총계", "자본총계"],
                "연산자": "="
            }
        },
        
        # 자산 섹션
        "자산총계": ["유동자산", "비유동자산"],
        
        "유동자산": [
            "현금및현금성자산",
            "단기금융상품",
            "유동성당기손익-공정가치측정금융자산",
            "유동성상각후원가측정금융자산",
            "매출채권",
            "기타채권",
            "단기대여금",
            "미수금",
            "미수수익",
            "선급금",
            "선급비용",
            "재고자산",
            "당기법인세자산",
            "매각예정자산",
            "기타유동자산"
        ],
        
        "재고자산": [
            "상품",
            "제품",
            "재공품",
            "원재료",
            "저장품",
            "미착품",
            "-재고자산평가충당금"
        ],
        
        "비유동자산": [
            "장기금융상품",
            "장기투자증권",
            "당기손익-공정가치측정금융자산",
            "기타포괄손익-공정가치측정금융자산",
            "상각후원가측정금융자산",
            "장기매출채권",
            "장기기타채권",
            "관계기업투자",
            "공동기업투자",
            "유형자산",
            "무형자산",
            "투자부동산",
            "사용권자산",
            "이연법인세자산",
            "순확정급여자산",
            "장기선급금",
            "장기선급비용",
            "기타비유동자산"
        ],
        
        "유형자산": [
            "토지",
            "건물",
            "-감가상각누계액_건물",
            "구축물",
            "-감가상각누계액_구축물",
            "기계장치",
            "-감가상각누계액_기계장치",
            "차량운반구",
            "-감가상각누계액_차량운반구",
            "공구와기구",
            "-감가상각누계액_공구와기구",
            "비품",
            "-감가상각누계액_비품",
            "건설중인자산",
            "-손상차손누계액"
        ],
        
        "무형자산": [
            "영업권",
            "산업재산권",
            "소프트웨어",
            "개발비",
            "고객관계",
            "기술가치",
            "회원권",
            "기타무형자산",
            "-손상차손누계액"
        ],
        
        # 부채와 자본 섹션
        "부채와자본총계": ["부채총계", "자본총계"],
        
        "부채총계": ["유동부채", "비유동부채"],
        
        "유동부채": [
            "매입채무",
            "단기차입금",
            "유동성장기부채",
            "유동성사채",
            "당기손익-공정가치측정금융부채",
            "기타채무",
            "미지급금",
            "미지급비용",
            "선수금",
            "선수수익",
            "예수금",
            "미지급법인세",
            "미지급배당금",
            "유동성리스부채",
            "유동성충당부채",
            "매각예정부채",
            "기타유동부채"
        ],
        
        "비유동부채": [
            "사채",
            "장기차입금",
            "장기기타채무",
            "장기미지급금",
            "장기미지급비용",
            "장기선수수익",
            "순확정급여부채",
            "이연법인세부채",
            "장기리스부채",
            "비유동충당부채",
            "기타비유동부채"
        ],
        
        "자본총계": [
            "자본금",
            "자본잉여금",
            "기타자본구성요소",
            "기타포괄손익누계액",
            "이익잉여금",
            "비지배지분"
        ],
        
        "자본잉여금": [
            "주식발행초과금",
            "기타자본잉여금"
        ],
        
        "기타자본구성요소": [
            "자기주식",
            "신주인수권",
            "전환권",
            "자기주식처분이익",
            "기타자본조정"
        ],
        
        "기타포괄손익누계액": [
            "기타포괄손익-공정가치측정금융자산평가손익",
            "지분법이익잉여금변동",
            "해외사업장환산외환차이",
            "현금흐름위험회피파생상품평가손익"
        ]
    },
    
    "손익계산서": {
        "매출총이익": ["매출액", "-매출원가"],
        
        "매출액": [
            "제품매출액",
            "상품매출액",
            "용역매출액",
            "기타매출액"
        ],
        
        "매출원가": [
            "제품매출원가",
            "상품매출원가",
            "용역매출원가",
            "기타매출원가"
        ],
        
        "제품매출원가": [
            "기초제품재고액",
            "당기제품제조원가",
            "-기말제품재고액"
        ],
        
        "당기제품제조원가": [
            "기초재공품재고액",
            "당기제조비용",
            "-기말재공품재고액"
        ],
        
        "당기제조비용": [
            "원재료비",
            "노무비",
            "경상연구개발비",
            "제조간접비"
        ],
        
        "영업이익": ["매출총이익", "-판매비와관리비"],
        
        "판매비와관리비": [
            "급여",
            "퇴직급여",
            "복리후생비",
            "여비교통비",
            "접대비",
            "통신비",
            "수도광열비",
            "세금과공과",
            "감가상각비",
            "무형자산상각비",
            "사용권자산상각비",
            "임차료",
            "수선비",
            "보험료",
            "차량유지비",
            "운반비",
            "교육훈련비",
            "도서인쇄비",
            "소모품비",
            "지급수수료",
            "광고선전비",
            "판매수수료",
            "대손상각비",
            "경상개발비",
            "기타판관비"
        ],
        
        "법인세비용차감전순이익": [
            "영업이익",
            "금융수익",
            "-금융비용",
            "기타수익",
            "-기타비용",
            "지분법손익"
        ],
        
        "금융수익": [
            "이자수익",
            "배당금수익",
            "외환차익",
            "외화환산이익",
            "당기손익-공정가치측정금융자산평가이익",
            "당기손익-공정가치측정금융자산처분이익",
            "파생상품평가이익",
            "파생상품거래이익"
        ],
        
        "금융비용": [
            "이자비용",
            "외환차손",
            "외화환산손실",
            "당기손익-공정가치측정금융자산평가손실",
            "당기손익-공정가치측정금융자산처분손실",
            "파생상품평가손실",
            "파생상품거래손실"
        ],
        
        "기타수익": [
            "유형자산처분이익",
            "무형자산처분이익",
            "투자부동산처분이익",
            "수입수수료",
            "임대료",
            "잡이익"
        ],
        
        "기타비용": [
            "유형자산처분손실",
            "무형자산처분손실",
            "투자부동산처분손실",
            "기부금",
            "잡손실"
        ],
        
        "당기순이익": ["법인세비용차감전순이익", "-법인세비용"]
    },
    
    "포괄손익계산서": {
        "총포괄손익": ["당기순이익", "기타포괄손익"],
        
        "기타포괄손익": [
            "후속적으로 당기손익으로 재분류되지 않는 항목",
            "후속적으로 당기손익으로 재분류될 수 있는 항목"
        ],
        
        "후속적으로 당기손익으로 재분류되지 않는 항목": [
            "확정급여제도의 재측정요소",
            "기타포괄손익-공정가치측정금융자산평가손익",
            "기타포괄손익-공정가치측정금융자산처분손익",
            "지분법이익잉여금변동",
            "자산재평가손익"
        ],
        
        "후속적으로 당기손익으로 재분류될 수 있는 항목": [
            "해외사업장환산외환차이",
            "현금흐름위험회피파생상품평가손익",
            "지분법자본변동"
        ]
    },
    
    "현금흐름표": {
        # 특수 검증 규칙 - 기말현금 = 기초현금 + 순증가 검증
        "__special_checks__": {
            "현금증감일치": {
                "항목1": "기말현금및현금성자산",
                "항목2": ["기초현금및현금성자산", "현금및현금성자산의순증가"],
                "연산자": "="
            }
        },
        
        "현금및현금성자산의순증가": [
            "영업활동현금흐름",
            "투자활동현금흐름",
            "재무활동현금흐름",
            "환율변동효과"
        ],
        
        "영업활동현금흐름": [
            "당기순이익",
            "비현금항목조정",
            "운전자본조정",
            "-이자지급",
            "이자수취",
            "배당금수취",
            "-법인세납부"
        ],
        
        "비현금항목조정": [
            "감가상각비",
            "무형자산상각비",
            "사용권자산상각비",
            "퇴직급여",
            "대손상각비",
            "이자비용",
            "-이자수익",
            "-배당금수익",
            "법인세비용",
            "재고자산평가손실",
            "유형자산처분손익",
            "무형자산처분손익",
            "투자부동산처분손익",
            "당기손익-공정가치측정금융자산평가손익",
            "당기손익-공정가치측정금융자산처분손익",
            "파생상품평가손익",
            "-외화환산이익",
            "외화환산손실",
            "-지분법이익",
            "지분법손실",
            "기타비현금항목"
        ],
        
        "운전자본조정": [
            "-매출채권의증가",
            "-기타채권의증가",
            "-재고자산의증가",
            "-선급금의증가",
            "-선급비용의증가",
            "매입채무의증가",
            "미지급금의증가",
            "선수금의증가",
            "예수금의증가",
            "미지급비용의증가",
            "-기타운전자본의증가"
        ],
        
        "투자활동현금흐름": [
            "-단기금융상품의순증가",
            "-장기금융상품의순증가",
            "-당기손익-공정가치측정금융자산의취득",
            "당기손익-공정가치측정금융자산의처분",
            "-기타포괄손익-공정가치측정금융자산의취득",
            "기타포괄손익-공정가치측정금융자산의처분",
            "-상각후원가측정금융자산의취득",
            "상각후원가측정금융자산의처분",
            "-관계기업투자의취득",
            "관계기업투자의처분",
            "-유형자산의취득",
            "유형자산의처분",
            "-무형자산의취득",
            "무형자산의처분",
            "-투자부동산의취득",
            "투자부동산의처분",
            "-종속기업투자의취득",
            "종속기업투자의처분",
            "-사업결합으로인한순현금유출",
            "사업매각으로인한순현금유입"
        ],
        
        "재무활동현금흐름": [
            "단기차입금의순증가",
            "장기차입금의차입",
            "-장기차입금의상환",
            "사채의발행",
            "-사채의상환",
            "-리스부채의상환",
            "유상증자",
            "-자기주식의취득",
            "자기주식의처분",
            "배당금의지급",
            "-비지배지분에대한배당금지급",
            "종속기업지분의추가취득",
            "-파생상품의정산"
        ],
        
        "기말현금및현금성자산": ["기초현금및현금성자산", "현금및현금성자산의순증가"]
    },
    
    "자본변동표": {
        "자본금변동": [
            "기초자본금",
            "유상증자",
            "무상증자",
            "-자본감소"
        ],
        
        "자본잉여금변동": [
            "기초자본잉여금",
            "주식발행초과금",
            "전환권대가",
            "자기주식처분이익",
            "기타자본잉여금변동"
        ],
        
        "이익잉여금변동": [
            "기초이익잉여금",
            "당기순이익",
            "-배당금",
            "확정급여제도재측정요소",
            "지분법이익잉여금변동",
            "-자본전입",
            "기타이익잉여금변동"
        ],
        
        "기타자본구성요소변동": [
            "기초기타자본구성요소",
            "-자기주식취득",
            "자기주식처분",
            "전환권대가",
            "신주인수권대가",
            "기타자본조정"
        ],
        
        "기타포괄손익누계액변동": [
            "기초기타포괄손익누계액",
            "기타포괄손익-공정가치측정금융자산평가손익",
            "지분법자본변동",
            "해외사업장환산외환차이",
            "현금흐름위험회피파생상품평가손익"
        ],
        
        "비지배지분변동": [
            "기초비지배지분",
            "비지배지분순이익",
            "-비지배지분배당금",
            "종속기업지분변동",
            "기타비지배지분변동"
        ]
    }
} 
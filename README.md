
# 🎮 Gomoku AI with Monte Carlo Tree Search (MCTS)

> 오목 게임에 **몬테카를로 트리 탐색(MCTS)** 알고리즘을 적용한 인공지능 실습 프로젝트입니다.  
> 콘솔 기반 UI로 작동하며, 사람과 AI가 대결할 수 있습니다.  
> 📚 참고: 『파이썬으로 만드는 인공지능』

---
> 오목 게임에 Monte Carlo Tree Search(MCTS) 알고리즘을 적용한 AI 프로젝트입니다.


[![GitHub release](https://img.shields.io/github/v/release/yuriuser126/mcts-ai-gomoku?style=flat-square)](https://github.com/yuriuser126/mcts-ai-gomoku/releases)

---

## 📌 프로젝트 소개

본 프로젝트는 `MCTS(Monte Carlo Tree Search)`를 직접 구현하여 오목(Gomoku) 게임에 적용해 본 **AI 실습 프로젝트**입니다.  
비결정론적 게임에서 많이 쓰이는 MCTS 알고리즘을 활용해, 시뮬레이션 기반의 AI 플레이어를 제작하고, 사용자와 대결할 수 있는 환경을 구현했습니다.

<details>
<summary>✅ 주요 목표</summary>

- MCTS 알고리즘 작동 원리 학습  
- 시뮬레이션 기반 의사결정 구현  
- 오목 게임 환경 구성 (5x5 / 10x10 모드 선택 가능)  
- 콘솔 기반 인터페이스로 플레이 가능  
- 사용자 종료 옵션, 입력 예외 처리 등 UX 개선  
</details>

---

## 🧠 사용 알고리즘: MCTS 개요

MCTS는 다음의 4단계로 구성됩니다:

<details>
<summary>🧩 MCTS 4단계</summary>

1. **Selection (선택)**  
   루트 노드에서 시작해, UCT(Upper Confidence Bound)를 기준으로 자식 노드를 따라 내려갑니다.  

2. **Expansion (확장)**  
   더 이상 선택할 노드가 없을 때, 새로운 자식 노드를 추가합니다.  

3. **Simulation (시뮬레이션)**  
   임의의 플레이를 반복하여 승패를 결정합니다.  

4. **Backpropagation (역전파)**  
   시뮬레이션 결과를 바탕으로 상위 노드들의 승률을 업데이트합니다.  
</details>

---

## 🛠️ 기술 스택

- Python 3.9+
- 표준 라이브러리만 사용 (`random`, `time`, `math`)
- 콘솔 기반 인터페이스 (GUI 미사용)
- 알고리즘 로직 직접 구현

---
## 🛠️ 환경 구성

```bash
pip install -r requirements.txt
```

---

## ✅ 주요 기능

<details>
<summary>📌 구현 기능 목록</summary>

- [x] MCTS 트리 구성 및 탐색 로직 구현  
- [x] 시뮬레이션 기반의 AI 플레이어 ('X')  
- [x] 사용자 vs AI 모드 (사람이 'O')  
- [x] 게임 종료 시 결과 출력 (승자 또는 무승부)  
- [x] 게임 종료 명령어 지원 (`q`, `quit`, `exit`)  
- [x] 5x5(이지), 10x10(하드) 모드 선택 기능  
- [ ] AI vs AI 모드 (추가 예정)  
</details>

---

## 🧪 실행 방법

```bash
# 1. 실행
python omok.py

```
---

<details> <summary>⌨️ 게임 조작법</summary>
실행 후 모드 선택:
1 → 5x5 이지 모드
2 → 10x10 하드 모드

사람 차례에는 x y 형태로 좌표 입력 (예: 3 4)

게임 중 q, quit, exit 입력 시 종료

</details>
📸 플레이 예시
게임 모드를 선택하세요 (1: 이지모드 5x5, 2: 하드모드 10x10): 1
 01234
0:-----
1:-----
2:--X--
3:-----
4:-----

사람 차례입니다. (x y 형식 입력, 종료하려면 'q' 입력): 2 1
 01234
0:-----
1:--O--
2:--X--
3:-----
4:-----


🗂️ 파일 구조
omok.py   # 전체 게임 로직 포함


💡 코드 설명
<details> <summary>🧠 주요 변수 및 함수 설명</summary>
항목	설명
n, k	오목판의 크기(n) 및 승리 조건(k 연속)
state	현재 보드 상태를 1차원 문자열로 표현
get_empty(state)	비어 있는 위치 리스트 반환
decide_winner(state)	승자 판별 (가로, 세로, 대각선)
Move(state, pos, player)	착수 반영
mcts(state, player)	MCTS 탐색 후 최적 수 결정
Node 클래스	MCTS 트리의 각 노드 정의
omok_play()	실제 게임 실행 함수
select_mode()	5x5 또는 10x10 모드 선택
randomAroundCenter()	초반 AI 중심 근처 착수 유도

<details> <summary>📓 프로젝트 회고</summary>
MCTS 구현이 처음이라 개념을 파악하는 데 시간이 걸렸지만, 시각적으로 결과를 보며 점진적으로 개선하는 방식이 흥미로웠습니다.

UCT 수식의 역할을 실험하면서 탐색/활용 균형의 중요성을 체감했습니다.

향후에는 AlphaZero 방식의 강화학습 기법과 연계해보고 싶습니다.

</details>

</details>
🚧 향후 개선 예정
<details> <summary>🛠️ 개선 및 확장 아이디어</summary>
 tkinter 기반 GUI 버전 개발

 AI vs AI 자동 플레이 모드

 탐색 횟수 및 승률 시각화 기능

 MCTS 탐색 깊이 조절 옵션 추가

</details>
📚 참고 자료
『파이썬으로 만드는 인공지능』

Wikipedia: Monte Carlo Tree Search

## 라이선스

본 프로젝트는 [MIT 라이선스](LICENSE) 하에 배포됩니다.  
자세한 내용은 LICENSE 파일을 참조하세요.


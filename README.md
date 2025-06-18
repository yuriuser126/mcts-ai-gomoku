# 🎮 Gomoku AI with Monte Carlo Tree Search (MCTS)

> 오목 게임에 몬테카를로 트리 탐색(Monte Carlo Tree Search, MCTS) 알고리즘을 적용한 인공지능 실습 프로젝트입니다.  
> 📚 참고: 『파이썬으로 만드는 인공지능 』

---

## 📌 프로젝트 소개

본 프로젝트는 MCTS(Monte Carlo Tree Search)를 직접 구현하여, 간단한 오목(Gomoku) 게임 환경에 적용해본 개인 실습 프로젝트입니다.  
MCTS는 비결정론적 게임 AI 설계에 널리 사용되는 알고리즘으로, 강화학습이나 게임 AI 분야의 핵심 개념 중 하나입니다.

이 프로젝트는 다음을 목표로 합니다:

- MCTS 기본 개념 학습 및 코드 구현
- 오목 게임 환경 구성
- 시뮬레이션 기반 AI 플레이어 구현
- 탐색 깊이, 시뮬레이션 횟수에 따른 전략 차이 관찰

---

## 🧠 사용 알고리즘: MCTS 개요

MCTS는 4단계로 이루어져 있습니다:

1. **Selection**: 루트 노드에서 시작하여 UCB(Upper Confidence Bound) 기준으로 자식 노드 선택
2. **Expansion**: 선택한 노드에 자식 노드 추가
3. **Simulation**: 무작위 시뮬레이션으로 게임 종료까지 플레이
4. **Backpropagation**: 시뮬레이션 결과를 통해 승률 계산 및 상위 노드 업데이트

---

## 🛠️ 기술 스택

- Python 3.9+
- tkinter (게임 GUI)
- numpy
- [📚 책 기반 구현] 『파이썬으로 만드는 인공지능 』 일부 예제 참고

---

## 🖼️ 시연 화면

| MCTS 오목 플레이 예시 |
|----------------------|
| ![gomoku-mcts](./assets/screenshot.gif) |

---

## 🗂️ 디렉토리 구조
gomoku-mcts/
├── mcts/ # MCTS 알고리즘 로직
│ ├── node.py
│ ├── mcts.py
├── gomoku/ # 오목 게임 환경
│ ├── board.py
│ ├── game.py
├── gui/ # tkinter 기반 GUI
│ ├── main.py
├── tests/ # 간단한 유닛 테스트
├── README.md
└── requirements.txt

yaml
코드 복사

---

## ✅ 주요 기능

- [x] MCTS 트리 구성 및 탐색 로직 구현
- [x] 시뮬레이션 기반의 AI 플레이어
- [x] 사용자 vs AI 모드
- [ ] AI vs AI 모드 (추가 예정)
- [ ] 탐색 매개변수 조절 실험 기능

---

## 🧪 실행 방법

```bash
# 1. 환경 구성
pip install -r requirements.txt

# 2. 게임 실행
python gui/main.py


## 코드설명
n: 보드의 한 변 크기 (예: n=15이면 15x15 오목판)

k: 몇 개를 연속으로 두면 승리인지 (일반적으로 k=5)

state: 전체 보드를 1차원 문자열로 표현한 배열 (ex: '------XOXO----' 등)

get_empty: 주변에 돌이 있는 위치만 반환 (MCTS 최적화 목적)

decide_winner: 가로, 세로, 대각선 방향으로 승자 판별

mcts(): 몬테카를로 트리 탐색을 통해 다음 수를 결정

선택 (Selection)

확장 (Expansion)

시뮬레이션 (Simulation)

역전파 / 백트래킹 (Backpropagation)

decide_winner(): 가로, 세로, 대각선 네 방향으로 승자 판별

omok_play(): 게임 초기 설정 (시작 상태, 첫 수 둔 플레이어)



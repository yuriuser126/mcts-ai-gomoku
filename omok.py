from math import sqrt,log
import random
import time

def select_mode():
    mode = input("게임 모드를 선택하세요 (1: 이지모드 5x5, 2: 하드모드 10x10): ")
    if mode == '1':
        return 5, 5
    elif mode == '2':
        return 10, 5
    else:
        print("잘못된 입력입니다. 기본값 10x10으로 진행합니다.")
        return 10, 5


# n=10
# k=5
# start='-'*(n*n)

class Node():
    def __init__(self,state,player=None,pos=None,parent=None):
        self.state=state
        self.player=player
        self.pos=pos
        self.parent=parent
        self.nwin=0
        self.nvisit=0
        self.untried=get_empty(state)
        self.children=[]
    
    def UCTselect(self):
        s=sorted(self.children,key=lambda c:c.nwin/c.nvisit+sqrt(log(self.nvisit)/c.nvisit))
        return s[-1]

    def makeChild(self,start,pos,player):
        node=Node(start,player,pos,parent=self)
        self.untried.remove(pos)
        self.children.append(node)
        return node

    def update(self,winner):
        self.nvisit+=1
        if winner=='T': #비긴경우
            self.nwin=0.5
        elif winner==self.player:
            self.nwin+=1
    
    def __repr__(self):
        return str(self.state)+" "+str(self.nwin)+"/"+str(self.nvisit)
    
def randomAroundCenter (n):
    c=n*(n//2)+n//2
    return random.choice([c,c-1,c+1,c-n,c+n])

def Move(state,pos,player):
    return state[:pos]+player+state[pos+1:]

def switch_player(player):
    return 'X' if player == 'O' else 'O'


def print_board(state):
    print(' 0123456789012345'[:n*2])
    for i in range(n):
        print(str(i % 10)+':'+state[n * i : n * (i + 1)])

# def get_empty(state):
#     if decide_winner(state) in ['O', 'X', 'T']:  # 승자가 정해지면
#         return []

#     empty = []
#     for i in range(len(state)):
#         if state[i] != '-':
#             continue
#         r, c = i // n, i % n
#         for (y, x) in [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
#                        (r, c - 1), (r, c + 1),
#                        (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]:
#             if 0 <= y < n and 0 <= x < n:
#                 idx = y * n + x
#                 if state[idx] != '-' and idx not in empty:
#                     empty.append(idx)

#     return empty

def get_empty(state):
    if decide_winner(state) in ['O', 'X', 'T']:
        return []

    empty = []
    for i in range(len(state)):
        if state[i] == '-':
            empty.append(i)
    return empty


def decide_winner(state):
    nvoid = 0
    for i in range(n * n):
        s = state[i]
        if s == '-':
            nvoid += 1
            continue

        r, c = i // n, i % n

        # 가로 체크
        c1 = c - 1; c2 = c + 1
        while c1 >= 0 and state[r * n + c1] == s: c1 -= 1
        while c2 < n and state[r * n + c2] == s: c2 += 1
        if c2 - c1 - 1 >= k: return s

        # 세로 체크
        r1 = r - 1; r2 = r + 1
        while r1 >= 0 and state[r1 * n + c] == s: r1 -= 1
        while r2 < n and state[r2 * n + c] == s: r2 += 1
        if r2 - r1 - 1 >= k: return s

        # 대각선 ↘ 체크
        r1 = r - 1; c1 = c - 1; r2 = r + 1; c2 = c + 1
        while r1 >= 0 and c1 >= 0 and state[r1 * n + c1] == s: r1, c1 = r1 - 1, c1 - 1
        while r2 < n and c2 < n and state[r2 * n + c2] == s: r2, c2 = r2 + 1, c2 + 1
        if r2 - r1 - 1 >= k: return s

                # 대각선 ↙ 체크
        r1 = r - 1; c1 = c + 1; r2 = r + 1; c2 = c - 1
        while r1 >= 0 and c1 < n and state[r1 * n + c1] == s: r1, c1 = r1 - 1, c1 + 1
        while r2 < n and c2 >= 0 and state[r2 * n + c2] == s: r2, c2 = r2 + 1, c2 - 1
        if r2 - r1 - 1 >= k: return s

    if nvoid == 0: return 'T'  # Tie(비김)
    return 'N'                 # 아직 승자 정해지지 않음


def mcts(state, player):
    root = Node(state)

    # for i in range(10000): ->10,000번 반복하며 몬테카를로 시뮬레이션을 돌리는 중
    for i in range(1000):
        node = root
        state = node.state
        roll_player = player

        # 선택
        while node.untried == [] and node.children != []:
            node = node.UCTselect()
            state = Move(state, node.pos, roll_player)
            roll_player = switch_player(roll_player)

        # 확장
        if node.untried != []:
            pos = random.choice(node.untried)
            state = Move(state, pos, roll_player)
            node = node.makeChild(state, pos, roll_player)
            roll_player = switch_player(roll_player)

        # 시뮬레이션
        while True:
            e = get_empty(state)
            if e == []: break
            state = Move(state, random.choice(e), roll_player)
            roll_player = switch_player(roll_player)

        # 백트래킹
        winner = decide_winner(state)
        while node != None:
            node.update(winner)
            node = node.parent

        # children이 비었을 경우 안전하게 처리
    if not root.children:
        # 둘 수 있는 곳 중 랜덤 선택 혹은 None 반환
        empties = get_empty(state)
        if empties:
            return random.choice(empties)
        else:
            return None  # 둘 곳 없음
    return sorted(root.children, key=lambda c: c.nwin / c.nvisit)[-1].pos


def omok_play(first_mover):
    state = start
    player = first_mover
    print_board(state)

    while True:
        t1 = time.time()
        if player == 'X':
            if state == start:
                pos = randomAroundCenter(n)
            else:
                pos = mcts(state, player)
        elif player == 'O':
            try:
                inp = input("사람 차례입니다. (x y 형식 입력, 종료하려면 'q' 입력): ")

                if inp.lower() in ['q', 'quit', 'exit', '종료']:
                    print("게임을 종료합니다.")
                    break

                x, y = inp.split()
                pos = int(y) * n + int(x)

                
            except ValueError:
                print("잘못된 입력입니다. 숫자 두 개를 공백으로 구분해서 입력해주세요.")
                continue

            if state[pos] != '-':
                print("둘 수 없는 곳입니다.")
                continue

        state = Move(state, pos, player)
        print_board(state)

        winner = decide_winner(state)
        if winner in ['O', 'X', 'T']:
            if winner == 'T':
                print("비겼습니다.")
            else:
                print(winner, "가 이겼습니다.")
            break

        print(player, '가', round(time.time() - t1, 3), '초를 썼습니다.')
        player = switch_player(player)


n, k = select_mode()
start = '-' * (n * n)


# 오른쪽 게임을 시작하는 main
omok_play('O')






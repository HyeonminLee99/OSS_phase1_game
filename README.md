# Tetris Game



## 구현목표
- 본 프로젝트는 스테디셀러 게임인 "테트리스"를 구현하기 위함이며, 주어진 시간동안 블럭들을 차곡차곡 쌓아 천장에 도달하지 않도록 하는 게임입니다. 천장에 블럭이 도달하면 패배합니다.



## 구현기능
- **pygame 기반의 게임 screen 구현**: 게임 화면을 pygame을 사용하여 구현하였습니다
- **키보드를 통한 블럭 이동 및 시계방향 회전 기능**: 화살표 키를 사용하여 블럭을 좌우로 이동하고, 아래쪽 화살표 키로 빠르게 내릴 수 있습니다. Shift 키를 사용하여 블럭을 시계방향으로 회전할 수 있습니다. 
- **한 줄에 블럭이 꽉 찼을 때, 블럭이 이동하는 기능**: 한 줄이 완전히 채워지면 해당 줄이 사라지고 위에 있는 블럭들이 내려옵니다.
- **점수 및 레벨 표시 기능**: 게임 진행 중 실시간으로 점수와 레벨이 화면에 표시됩니다.


## 지원 OS 및 실행방법



- **지원 OS** : windows


### 실행방법 


1. Python 3.12 설치
2. pygame 설치:
    ```sh
    pip install pygame
    ```
3. 재부팅 후, main.py가 존재하는 폴더에서 다음 명령어를 입력하여 실행:
    ```sh
    python main.py
    ```



## 게임 조작 방법


- **좌우이동**: 화살표 왼쪽 키와 오른쪽 키(키다운을 통한 연속 이동 가능)
- **빠르게 내리기**: 화살표 아래 키(키다운 불가)
- **회전**: Shift 키 (좌우 Shift 모두 사용가능 , 시계방향 회전만 가능)
- **일시 정지 및 재개**: P 키



## 게임 화면

- 게임이 시작되면 'Start' 버튼을 마우스로 클릭하여 게임을 시작할 수 있습니다. 게임 진행 중 실시간으로 점수와 레벨을 확인할 수 있으며, 일정 점수에 도달하면 레벨이 증가하며, 난이도가 높아집니다.




## Reference 
[1] https://github.com/pygame/pygame "pygame"

[2] https://sugar-family.tistory.com/5 "pygame을 이용한 테트리스 구현"



## 실행 예시

![실행결과](https://github.com/HyeonminLee99/OSS_phase1_game/assets/133738567/b1cc0232-52a9-4e49-af2c-eb160ea80685)


README
============

게임 소개

+ The Cavern

	본 게임의 제목은 The Cavern입니다.
	본 게임의 목적은 주어진 아이템을 활용하여 험난한 지형을 통과하며 마지막 스테이지를 클리어 하는 것 입니다.
	일정 스테이지를 넘어갈 때마다 추가적인 능력을 부여하는 아이템을 얻을 수 있습니다.

***

GameState
-----------

본 게임은 타이틀 화면, 인게임 화면으로 나누어 질 것 입니다.
총 2개의 GameState로 나누어고, 인게임 화면에 추가로 1개의 SubState가 존재할 것 입니다.

+ 타이틀 화면

	게임의 타이틀이 나타나고, 새 게임 시작, 데이터 불러오기, 나가기 등의 메뉴가 있는 화면입니다.
	화면에는 각 메뉴 객체들이 나타나고, 위 아래 방향키를 이용하여 메뉴를 선택하게 될 것입니다.
	새 게임 시작을 선택한다면, 기존 저장 데이터를 지우고 새 저장 데이터를 쓴 뒤, 인게임 화면으로 진입하게 될 것입니다.
	데이터 불러오기를 선택한다면, 기존 저장 데이터를 불러온 뒤, 인게임 화면으로 진입하게 될 것입니다.

+ 인게임 화면

	게임에 진입하였을때 나타나는 화면입니다.
	화면에 플레이어 캐릭터와 적 캐릭터, NPC, 배경, 지형이 나타나게 될 것입니다.
	플레이어 캐릭터를 움직이는 방향키와 발사 키 등의 키보드 이벤트가 처리 될 것입니다.
	특정 키를 이용하여 일시정지 화면이나 인벤토리 화면으로 넘어갑니다.
	

	+ 일시정지 화면

		인게임 화면이 실행되는 중에 일시정지를 선택하면 나타나는 화면입니다.
		게임에서 나가기, 저장 메뉴가 나타납니다.
		방향키로 메뉴를 선택합니다.
		일시정지 키를 다시 누르면 인게임 화면으로 돌아갈 것 입니다.
		게임에서 나가기를 선택하면 타이틀 화면으로 돌아갈 것 입니다
		
		
Item
----------------
플레이어가 진행 중 얻게 될 아이템은 다음과 같습니다.

1. 이단 점프 부츠

	점프를 한번 더 할 수 있게 해줍니다.

2. 로켓런처

	플레이어의 아래에 쏘는 동시에 점프하여 높은 위치에 올라갈 수 있습니다.

3. 가우스 건

	플레이어의 좌 우 방향으로 발사하여 반대방향으로 향하는 추력을 얻을 수 있습니다.
	
	
Stage
----------------

	총 10개의 스테이지로 구성됩니다.
	첫 4개의 스테이지는 처음 주어지는 이단 점프 부츠로 클리어 할 수 있는 스테이지들 입니다.
	이후 4개의 스테이지는 이후 주어지는 로켓런처를 이용하여 클리어 할 수 있는 스테이지들 입니다.
	다음 4개 스테이지는 이후 주어지는 가우스 건을 이용하여 클리어 할 수 있는 스테이지들 입니다.
	이후 2개의 스테이지는 가장 고난이도의 스테이지로서, 주어진 아이템들을 모두 활용하여 클리어해야합니다.


TO-DO LIST
----------------
	- 맵 에디터 개발
	- 각각 5분 정도의 플레이 타임을 가진 4개의 구역 개발
	- 중간 2개 구역을 나중에 진행하였을때 변화한 구역 구현
	- 로켓 런처, 플라즈마 포, 이단 점프 부츠 개발
	- 플레이어 이동 메카닉 구현
	- 세이브 파일 생성, 저장 및 읽기 구현
	- UI 구성


Development Schedule
----------------
	1주 : 플레이어 이동, 이단점프 부츠 및 카메라 스크롤링 구현
	2주 : 로켓런처, 플라즈마 포 구현
	3주 : 맵 에디터 개발
	4주 : 레벨 디자인 및 장애물 구현
	5, 6주 : 적 AI 구현 및 배치
	7, 8주 : 버그 수정 및 미흡한 부분 수정


필요한 기술
----------------

	Pico2D 라이브러리를 이용한 애니메이션 및 이벤트 처리 기술
	HEX 파일을 이용한 세이브 데이터 처리 기술
	자료구조를 이용한 효율적인 데이터 처리 기술
	중력이나 추력 등 여러가지 물리량을 처리하는 기술
	
2차 발표
----------------

1. 게임에 대한 간단한 소개
----------------

	본 게임의 제목은 The Cavern입니다.
	본 게임의 목적은 주어진 아이템을 활용하여 험난한 지형을 통과하며 마지막 스테이지를 클리어 하는 것 입니다.
	일정 스테이지를 넘어갈 때마다 추가적인 능력을 부여하는 아이템을 얻을 수 있습니다.
	
2. 현재까지의 진행 상황
----------------

	플레이어 조작 : 100%
	아이템 구현 : 100%
	맵 에디터 : 100%
	스테이지 구성 : 8%
	맵 스크롤 구현 : 10%
	타이틀 및 일시정지, 사운드 : 0%
	적 구현 : 0%
	저장 : 0%
	
3. 커밋 횟수
----------------
Insights: https://github.com/kcjsend2/2DGP/graphs/commit-activity

	1주차: 1회
	2주차: 0회
	3주차: 13회
	4주차: 10회
	5주차: 0회
	6주차: 7회

4. 변경된 목표
----------------

	본래 여러 갈래의 맵을 통해 20여분의 플레이 타임을 보장하려 했으나, 작업량의 문제(코딩 외에 맵을 만드는 작업이 너무 많음)로 한 갈래의 선형적인 구조로 바꾸었습니다.
	또한 인벤토리 화면과 대화 화면을 GameState로 추가할 예정이었으나 인벤토리 화면에 표시할 정보가 적어 필요성이 떨어지고, 대화 화면 또한 NPC같은 대화가능한 상대가 없어
	아이템을 얻는 경우와 같이 간헐적으로만 사용되기 때문에 GameState가 아닌 객체를 이용하여 구현하는 것으로 바꾸었습니다.
	
5. 맵 에디터(editor state)
----------------

	타일을 왼클릭으로 설치, 오른클릭으로 삭제할 수 있습니다. 32x32 영역으로 분할되어있고, 같은 영역에 여러 타일이 설치될 수 없습니다.
	드래그 또한 클릭과 같이 사용할 수 있습니다. (ex) 왼클릭 후 드래그로 연속으로 설치)
	1번키로 해당타일이 충돌처리를 하도록 만들 수 있고, 2번키로 하지 않도록 만들 수 있습니다.
	s키를 눌러 json파일을 저장할 수 있습니다.


6. Game Object
	+5-1 Player
	
		플레이어 객체입니다. 좌우 방향키로 움직이고, 점프해서 위아래 방향키로 위와 아래를 볼 수 있습니다. z로 점프, x로 무기 발사입니다. 이단점프,
		로켓런처, 가우스 건의 소지 정보를 bool 변수로 지니고 있고, 해당 값들에 따라 할 수 있는 행동이 달라집니다. A로 로켓런처, S로 가우스 건으로 교체합니다.
		이후 설명할 객체인 타일과 충돌처리됩니다.
		MyChar.png 파일을 이용하여 그려지며, action 변수에 따라서 어느 부분이 그려질지 정해집니다. 점프, 걷기, 위보면서 걷기, 점프 후 아래보기, 위 보기 등이 있습니다.
		
	+5-2 Rocket
	
		플레이어가 로켓런처를 발사하면 생기는 로켓입니다. 로켓의 뒤에 tail 객체(이펙트)를 생성합니다. 플레이어가 보는 방향으로 이동하며, 타일과 충돌처리되면 제거됩니다.
		또한 플레이어 근처에서 제거되면 플레이어의 델타 y값을 증가시켜 높게 점프하도록 합니다.
		
	+5-3 Tail
	
		로켓의 뒤에 생기는 이펙트입니다. 로켓이 오래 남아있을수록 길게 남습니다.
		
	+5-4 Gauss
	
		플레이어가 가우스 건을 발사하면 생기는 투사체 입니다. 다른 물체들과 충돌처리되지 않습니다. 발사하면 플레이어의 반대방향으로 델타 x값을 변화시켜 빠르고 멀리
		이동할 수 있게 합니다.
		
	+5-5 Tile
	
		타일 객체입니다. 플랫폼 역할을 하며, 플레이어, 로켓과 충돌처리됩니다. 맵 에디터가 생성한 json 파일에서 불러오며, 충돌처리를 할지 안할지 여부를 고를 수 있습니다.

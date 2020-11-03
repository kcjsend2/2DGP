README
============

게임 소개

+ The Cavern

	본 게임의 제목은 The Cavern으로, 2004년에 프리웨어로 배포된 명작, Cave Story의 오마주입니다.
	Cave Stroy는 2D 플랫포머 메트로배니아 게임으로, 본 프로젝트의 또한 같은 장르로서 제작 될 것입니다.
	본 게임의 목적은 맵을 탐사하며 적을 처치하며 무기와 각종 아이템을 모으고, 마지막 보스에게 도달하는 것 입니다.
	한 구역의 보스를 처리할 때마다, 다른 구역으로 넘어갈 수 있는 능력을 부여하는 아이템을 획득할 수 있고,
	아이템을 획득할 때마다 탐사 가능한 구역이 점점 넓어지는 구성을 취하게 될 것 입니다.

***

GameState
-----------

본 게임은 타이틀 화면, 인게임 화면으로 나누어 질 것 입니다.
총 2개의 GameState로 나누어고, 인게임 화면에 추가로 3개의 SubState가 존재할 것 입니다.

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
		게임에서 나가기를 선택하면 타이틀 화면으로 돌아갈 것 입니다.

	+ 인벤토리 화면

		인게임 화면이 실행되는 중에 인벤토리를 선택하면 나타나는 화면입니다.
		방향키로 아이템을 선택하고, 세부 보거나 사용할 수 있을 것 입니다.
		인벤토리 키나 일시정지 키를 다시 누르면 인게임 화면으로 돌아갈 것입니다.
		
	+ 대화 화면
		인게임 화면이 실행되는 중에 상호작용을 하면 나타나는 화면입니다.
		대화 창이 나타나며 넘어가기 키를 이용해 대화를 넘길 수 있습니다. 대화가 끝나면 인게임 화면으로 돌아갈 것입니다.
		
		
Item
----------------
플레이어가 진행 중 얻게 될 아이템은 다음과 같습니다.

1. 이단 점프 부츠

	점프를 한번 더 할 수 있게 해줍니다.

2. 로켓런처

	플레이어의 아래에 쏘는 동시에 점프하여 높은 위치에 올라갈 수 있습니다.
	적에게 피해를 줄 수 있습니다.

3. 플라즈마 포

	플레이어의 좌 우 방향으로 발사하여 반대방향으로 향하는 추력을 얻을 수 있습니다.
	적에게 피해를 줄 수 있습니다.
	
	
Stage
----------------

본 게임은 크게 4가지 구역으로 나눌 수 있습니다.

	시작포인트 - 이단 점프 부츠를 얻을 수 있는 구역
	로켓런처를 얻는 구역
	플라즈마 포를 얻는 구역
	최종 스테이지

이 중 로켓런처를 얻는 구역과 플라즈마 포를 얻는 구역은 플레이어가 먼저 진행할 구역을 선택할 수 있으며,
나중에 선택된 구역은 먼저 선택한 구역에 따라 먼저 얻은 아이템을 활용하도록 구조가 변화합니다.

최종 스테이지는 진행 중 모은 모든 아이템을 활용하도록 구성될 것 입니다.


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
# fastapi-di-system
좌호빈 화이팅  
간단하게 FastAPI와 Tortoise ORM을 사용하는 템플릿입니다.

## 야미
FastAPI X Tortoise ORM X DI 와 함게 쓰세요.  
dto: FastAPI에서 사용하는 DTO 관리 폴더  
entities: Tortoise ORM으로 만든 ORM 모델  
repository: entity 생성, 삭제 관리 등  
service: 비즈니스 로직  
endpoints: FastAPI에서 들어오는 HTTP 요청 처리  
containers: DI 컨테이너(service, repository 관리)  

## 설정 파일
settings는 자동으로 ``.env`` 파일을 읽어서 환경 변수를 설정합니다.  
``.env`` typing을 검사하려면 ``app/env_validator.py``를 확인하세요.


## 개발 환경 설정

이 프로젝트는 Python 가상 환경(venv)을 사용합니다. 아래 단계를 따라 개발 환경을 설정하세요.

### 사전 요구 사항

- Python 3.11 이상
- pip (최신 버전)

### 설치 단계

1. 프로젝트 클론

```bash
git clone https://github.com/your-team/cool-project.git
```


2. 가상 환경 생성 및 활성화
- Windows:
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
- macOS 및 Linux:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```
  
3. 의존성 패키지 설치
```bash 
pip install -r requirements.txt
```

### 환경 변수 설정

`.example.env` 파일을 `.env`로 복사하고, 필요한 환경 변수를 설정하세요.

### 프로젝트 실행 방법
```bash
python -m app
```

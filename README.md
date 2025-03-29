# Angular Flask Seed Project

이 프로젝트는 Angular와 Flask를 사용한 웹 애플리케이션 시드 프로젝트입니다.

## 프로젝트 구조

```
.
├── frontend/          # Angular 프론트엔드
│   ├── src/          # Angular 애플리케이션 소스
│   ├── package.json  # Node.js 의존성 설정
│   └── angular.json  # Angular 설정
│
└── backend/          # Flask 백엔드
    ├── server/      # Flask 서버 소스
    ├── test/        # 테스트 코드
    ├── sql/         # SQL 스크립트
    ├── config.py    # 설정 파일
    ├── run.py       # 서버 실행 스크립트
    └── requirements.txt  # Python 의존성 설정
```

## 기술 스택

### 프론트엔드
- Angular 17.1.0
- TypeScript 5.3.2
- Angular CLI 17.1.0
- RxJS 7.8.0

### 백엔드
- Flask 3.0.2
- Flask-SQLAlchemy 3.1.1
- Flask-WTF 1.2.1
- Flask-Login 0.6.3
- Flask-Security-Too 5.3.2
- Flask-HTTPAuth 4.2.0
- SQLAlchemy 2.0.27
- Python 3.8+

## 설치 및 실행 방법

### 프론트엔드 설정
```bash
cd frontend
npm install
```

### 백엔드 설정
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

### 서버 실행
```bash
# 백엔드 서버 실행
cd backend
python run.py

# 프론트엔드 개발 서버 실행 (새 터미널에서)
cd frontend
npm start
```

## 개발 가이드

### 프론트엔드 개발
- `frontend/src/` 디렉토리에서 Angular 애플리케이션 개발
- Angular CLI를 사용하여 개발 서버 실행 및 빌드
- TypeScript를 사용한 타입 안전한 개발

### 백엔드 개발
- `backend/server/` 디렉토리에서 Flask 애플리케이션 개발
- SQLAlchemy를 사용한 데이터베이스 모델링
- Flask-Security-Too를 통한 인증 및 권한 관리

## 테스트
```bash
# 백엔드 테스트
cd backend
pytest

# 프론트엔드 테스트
cd frontend
npm test
```

## 라이선스
MIT License

# 그저 긴 링크를 짧게 줄여주는 API

이 프로젝트는 **FastAPI**를 사용하여 긴 URL을 짧은 URL로 변환해주는 간단한 URL 단축 API입니다.

## 📌 기능
- 긴 URL을 짧은 URL로 변환
- 단축된 URL을 원래 URL로 리디렉트
- SQLite를 사용하여 URL 저장
- FastAPI 기반 RESTful API 제공

---

## 🚀 실행 방법

### 1️⃣ 필요한 패키지 설치
```sh
pip install -r requirements.txt
```

### 2️⃣ FastAPI 서버 실행
```sh
uvicorn app.main:app --reload
```
✅ 실행하면 http://127.0.0.1:8000에서 API를 사용할 수 있습니다.

### 3️⃣ Swagger UI에서 API 테스트
브라우저에서 Swagger UI (API 문서) 확인 가능:
📌 http://127.0.0.1:8000/docs

---

## 📌 API 엔드포인트

### 🔹 1. URL 단축하기
- POST ```/shorten```
- 요청 (JSON)
```json
{
  "original_url": "https://example.com"
}
```
- 응답 (JSON)
```json
{
  "short_url": "http://127.0.0.1:8000/abc123"
}
```

### 🔹 2. 단축 URL 방문 (리다이렉트)
- GET ```/{short_code}```
- 예: ```http://127.0.0.1:8000/abc123```
- 응답: 원래 URL로 자동 리디렉트 (```HTTP 307```)

---

## 📌 curl을 사용한 API 테스트

### ✅ 1. URL 단축하기
```sh
curl -X POST "http://127.0.0.1:8000/shorten" \
     -H "Content-Type: application/json" \
     -d '{"original_url": "https://example.com"}'
```

### ✅ 2. 단축 URL 방문
```sh
curl -v "http://127.0.0.1:8000/abc123"
```

---

## 📌 프로젝트 구조
```bash
fastapi-url-shortener/
│── app/
│   ├── main.py         # FastAPI 엔트리 포인트
│   ├── models.py       # DB 모델 정의
│   ├── database.py     # DB 연결 관리
│   ├── routes.py       # API 라우트 정의
│   ├── schemas.py      # Pydantic 데이터 모델
│── requirements.txt    # 필요한 패키지 목록
│── .env                # 환경 변수 파일
│── README.md           # 실행 방법 문서
```

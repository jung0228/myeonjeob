# 기출/후기 기반 면접 질문 분석

여기 정리한 내용은 공식 문제집이 아니라, 유튜브 영상 타임스탬프와 후기에서 반복적으로 등장한 질문을 모아  
`무슨 주제가 자주 나오는지`, `어디까지 준비해야 하는지`, `어떤 질문이 쉬운지 어려운지`를 보기 위한 분석 문서입니다.

특히 서울대 AI처럼 `선형대수 + 확통 + ML 기초`가 섞일 수 있는 면접을 대비할 때,  
문제를 하나씩 외우기보다 **반복되는 질문 패턴**을 잡는 데 목적이 있습니다.

## 1. 전체 패턴 요약

반복 출제되는 주제는 크게 5축으로 보입니다.

1. 선형대수
2. 확률통계
3. 최적화 / ML 기초
4. 딥러닝 기본 구조
5. 프로그래밍 상식

이 중에서 네 상황 기준 우선순위는 다음과 같습니다.

1. 선형대수
2. 확률통계
3. 최적화 / ML 기초
4. 딥러닝 기초
5. 프로그래밍 상식

이유:

- 이미 선형대수를 선택과목으로 골랐음
- 서울대 스타일 꼬리질문은 선형대수 단독보다 `선형대수 + 확통 연결`이 자주 섞일 가능성이 큼
- 딥러닝/프로그래밍은 기본 상식형이 많고, 선형대수만큼 깊게 파지는 않을 가능성이 큼

## 2. 반복 빈도가 높은 질문 축

### 선형대수 쪽 반복 키워드

- `eigenvalue / eigenvector`
- `rank`
- `basis / vector space`
- `inverse`
- `PCA`
- `SVD`
- `determinant`
- `four spaces / null space`

### 확률통계 쪽 반복 키워드

- `independence`
- `uncorrelated`
- `E[XY] = E[X]E[Y]`
- `Gaussian / Normal distribution`
- `CLT`
- `Bayes rule`
- `conditional distribution`

### 최적화 / ML 기초 쪽 반복 키워드

- `overfitting`
- `validation data`
- `GD vs SGD`
- `optimizer`
- `regularization`
- `logistic regression`
- `convexity`

### 딥러닝 쪽 반복 키워드

- `Transformer`
- `ViT`
- `conv layer vs FC layer`
- `skip connection`
- `1x1 conv`
- `지도학습 vs 비지도학습`
- `AI vs ML vs DL`

### 프로그래밍 쪽 반복 키워드

- `list vs dictionary`
- `pointer`
- `linked list`
- `numpy vs list`

## 3. 난이도별 분류

난이도는 **답변을 30초 안에 깔끔하게 말할 수 있는가**, **꼬리질문이 붙었을 때 얼마나 흔들리는가** 기준으로 나눴습니다.

### 하

정의형이 많고, 큰 꼬리질문 없이 기본 개념만 묻는 경우가 많습니다.

- 오버피팅의 정의
- Validation data가 필요한 이유
- GD vs SGD의 큰 차이
- AI vs ML vs DL
- eigenvalue / eigenvector 기본 정의
- basis란?
- vector space란?
- rank가 뭡니까?
- PCA가 뭡니까?
- Normal distribution이란?
- Bayes rule이 뭔가요?
- SVD란?
- determinant의 의미
- 리스트 vs 딕셔너리
- 포인터란?
- linked list란?

특징:

- 정의를 정확하게 말하는지 확인
- 개념 간 구분을 할 수 있는지 확인
- 예시 하나 붙이면 훨씬 좋아짐

### 중

비교형, 과정 설명형, 활용 설명형이 많고, 정의만으로는 부족합니다.

- 오버피팅이 일어났는지 어떻게 판단하나
- 오버피팅의 원인
- 오버피팅 완화 방법
- PCA로 차원축소 하는 과정
- 로지스틱 회귀의 loss와 학습 과정
- Gradient Descent 설명
- L1 vs L2 regularization
- 데이터가 적을 때 어떻게 할 것인가
- conv layer가 FC layer보다 좋은 이유
- skip-connection이 좋은 이유
- 1x1 conv의 의미
- 지도학습 vs 비지도학습
- inverse를 어떻게 구하나
- 역행렬의 시간복잡도는?
- Gaussian / CLT 기본 설명

특징:

- `정의 + 왜 + 어디에 쓰는가` 구조가 필요함
- 과정 설명 능력을 봄
- 한 문장 정의만 하면 약해 보임

### 상

증명, 반례, 조건, 수학적 연결 질문이 많고, 꼬리질문이 길게 붙기 쉽습니다.

- 독립일 때 `E[XY] = E[X]E[Y]` 증명
- 독립과 uncorrelated 차이
- 다변수 함수의 convexity
- `F-norm`과 singular value
- Similar matrix는 eigen value가 같은가
- `det(A)`가 고윳값의 합과 같은가
- 행렬의 네 가지 space
- 고윳값분해와 SVD 비교
- CLT와 대수의 법칙 차이
- likelihood와 Bayes 관점 연결
- least squares와 MLE 연결

특징:

- 정의만 알면 안 되고, 이유/반례/증명 방향까지 필요
- 꼬리질문으로 실력을 많이 가름
- 서울대 스타일로는 이 축이 특히 중요할 가능성이 높음

## 4. 선형대수 선택자 기준 최우선 핵심

선형대수를 선택한 지원자라면 아래 질문들은 반드시 안정적으로 나와야 합니다.

### 최우선 A급

- rank가 무엇인가
- basis / vector space
- inverse와 가역행렬
- eigenvalue / eigenvector
- 대각화 가능 조건
- 실수 대칭행렬의 성질
- PCA가 무엇인가
- SVD가 무엇인가
- determinant의 의미
- null space / four spaces

### 최우선 B급

- Similar matrix와 eigen value
- `det(A)`와 고유값의 곱 / trace와 고유값의 합
- `F-norm`과 singular value
- least squares / normal equation / pseudoinverse
- `A^T A`의 성질

## 5. 확통 섞일 때 최우선 핵심

선형대수 면접이라고 해도, 아래 확통 질문은 섞여 들어올 가능성이 높습니다.

### 꼭 준비

- independence
- uncorrelated
- covariance / covariance matrix
- Gaussian distribution
- CLT
- Bayes rule

### 왜 중요한가

- PCA 설명에 공분산행렬이 섞임
- `독립 vs 비상관`은 아주 전형적인 함정 질문
- CLT / Bayes는 확통 기본기 확인용
- least squares와 Gaussian noise, MLE 연결도 종종 나옴

## 6. 지금 기준 난이도 체감 정리

네 상태 기준으로 보면 대략 이렇게 보는 게 맞습니다.

### 지금 상대적으로 안정적인 것

- eigenvalue / eigenvector
- 대각화 기본
- 실수 대칭행렬
- SVD 큰 틀
- PCA 큰 틀
- rank 기본 감각
- overfitting 정의

### 지금 중간 정도로 불안한 것

- null space
- least squares
- normal equation
- pseudoinverse
- PD / PSD
- validation / regularization

### 지금 취약 축

- independence vs uncorrelated
- `E[XY] = E[X]E[Y]`
- Gaussian / CLT
- Bayes / likelihood / MLE
- 수학적 꼬리질문이 붙는 확통 연결

## 7. 실전 우선순위 제안

금요일 직전까지 기준으로는 아래 순서가 가장 효율적입니다.

1. 선형대수 A급 질문 안정화
2. 확통 핵심 6개 안정화
3. least squares ~ MLE 연결
4. overfitting / validation / regularization
5. GD vs SGD
6. 딥러닝/프로그래밍 상식형 문제

## 8. 자주 나오는 질문을 난이도별로 다시 압축

### 하 난이도에서 절대 놓치면 안 되는 것

- rank
- basis
- eigenvalue / eigenvector
- PCA
- SVD
- Bayes rule

### 중 난이도에서 준비하면 점수 나는 것

- overfitting 판단/원인/완화
- validation data
- L1 vs L2
- GD vs SGD
- conv vs FC
- skip connection

### 상 난이도에서 준비하면 차이 나는 것

- independence vs uncorrelated
- `E[XY] = E[X]E[Y]`
- CLT vs LLN
- least squares = MLE
- four spaces
- `F-norm`과 singular value
- Similar matrix와 eigen value

## 9. 한 줄 결론

이 영상/후기들을 기준으로 보면, 면접은 개념 암기 싸움이 아니라  
`정의 -> 조건 -> 직관 -> 예시`를 끊김 없이 말하는 싸움입니다.

특히 네 경우에는

- 선형대수 본체
- 확통 기본 6개
- 선형대수와 확통 연결

이 3축만 안정적으로 가져가도 충분히 경쟁력이 있습니다.

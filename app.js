const questions = [
  {
    category: "motivation",
    tag: "지원 동기",
    title: "왜 우리 대학원에 지원했나요?",
    tip: "학교 이름만 바꾸는 답변이 아니라, 연구 방향과 본인 관심사를 연결해서 말하는 게 핵심입니다."
  },
  {
    category: "motivation",
    tag: "지원 동기",
    title: "학부 졸업 후 바로 대학원에 오려는 이유는 무엇인가요?",
    tip: "취업 대신 대학원을 택한 이유를 현재 시점의 목표와 연결해 설명하면 설득력이 높아집니다."
  },
  {
    category: "research",
    tag: "연구 계획",
    title: "대학원에서 어떤 연구를 하고 싶나요?",
    tip: "완성된 주제가 아니어도 괜찮지만, 관심 분야와 탐구 방식은 구체적으로 말할수록 좋습니다."
  },
  {
    category: "research",
    tag: "연구 계획",
    title: "최근 관심 있게 본 논문이나 기술이 있나요?",
    tip: "내용 요약보다 왜 인상 깊었는지, 본인 연구 관심과 어떻게 이어지는지를 함께 말해보세요."
  },
  {
    category: "fit",
    tag: "전공 적합성",
    title: "본인이 대학원 연구에 적합하다고 생각하는 이유는 무엇인가요?",
    tip: "성실성만 말하기보다 문제를 깊게 파고든 경험, 스스로 학습한 사례를 예로 드는 편이 좋습니다."
  },
  {
    category: "fit",
    tag: "전공 적합성",
    title: "학부 때 진행한 프로젝트 중 가장 의미 있었던 경험은 무엇인가요?",
    tip: "프로젝트 설명 자체보다 맡은 역할, 어려움, 배운 점, 다음 확장 가능성을 강조하세요."
  },
  {
    category: "personality",
    tag: "인성/태도",
    title: "본인의 약점은 무엇이고 어떻게 보완하고 있나요?",
    tip: "약점을 숨기기보다 연구 수행에 어떤 영향을 줄 수 있는지, 그리고 보완 계획이 무엇인지 말해보세요."
  },
  {
    category: "personality",
    tag: "인성/태도",
    title: "의견 충돌이 생기면 어떻게 해결하나요?",
    tip: "팀 경험을 예시로 들면서, 감정보다 문제 해결 중심으로 접근했다는 점을 보여주면 좋습니다."
  },
  {
    category: "research",
    tag: "연구 계획",
    title: "석사 과정 동안 이루고 싶은 구체적 목표가 있나요?",
    tip: "논문, 프로젝트, 역량 성장 중 무엇을 우선시하는지 분명하게 보여주면 답변이 탄탄해집니다."
  }
];

const grid = document.querySelector("#question-grid");
const filterBar = document.querySelector("#filter-bar");
const template = document.querySelector("#question-card-template");

function renderQuestions(filter) {
  const selected = filter === "all"
    ? questions
    : questions.filter((item) => item.category === filter);

  grid.innerHTML = "";

  selected.forEach((question, index) => {
    const fragment = template.content.cloneNode(true);
    const card = fragment.querySelector(".question-card");

    fragment.querySelector(".question-tag").textContent = question.tag;
    fragment.querySelector(".question-title").textContent = question.title;
    fragment.querySelector(".question-tip").textContent = question.tip;

    card.classList.add("enter");
    card.style.animationDelay = `${index * 45}ms`;
    grid.appendChild(fragment);
  });
}

filterBar.addEventListener("click", (event) => {
  const target = event.target;

  if (!(target instanceof HTMLButtonElement)) {
    return;
  }

  filterBar.querySelectorAll(".chip").forEach((chip) => {
    chip.classList.toggle("active", chip === target);
  });

  renderQuestions(target.dataset.filter || "all");
});

renderQuestions("all");

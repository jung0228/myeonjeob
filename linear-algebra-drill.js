const REVIEW_STORAGE_KEY = "myeonjeob-linear-algebra-review-v1";

function loadReviewState() {
  try {
    const raw = window.localStorage.getItem(REVIEW_STORAGE_KEY);
    if (!raw) {
      return { modes: {}, done: {}, filters: {} };
    }

    const parsed = JSON.parse(raw);
    return {
      modes: parsed.modes || {},
      done: parsed.done || {},
      filters: parsed.filters || {}
    };
  } catch {
    return { modes: {}, done: {}, filters: {} };
  }
}

function saveReviewState(state) {
  try {
    window.localStorage.setItem(REVIEW_STORAGE_KEY, JSON.stringify(state));
  } catch {
    // Ignore storage errors and keep the UI usable.
  }
}

function createToolbar(sectionId, totalCount) {
  const toolbar = document.createElement("div");
  toolbar.className = "review-toolbar";
  toolbar.dataset.reviewSection = sectionId;

  const title = document.createElement("p");
  title.className = "review-toolbar-label";
  title.textContent = "복습 모드";

  const controls = document.createElement("div");
  controls.className = "review-toolbar-controls";

  const questionOnly = document.createElement("button");
  questionOnly.type = "button";
  questionOnly.className = "review-chip";
  questionOnly.dataset.reviewView = "questions";
  questionOnly.textContent = "질문만 보기";

  const showAnswers = document.createElement("button");
  showAnswers.type = "button";
  showAnswers.className = "review-chip";
  showAnswers.dataset.reviewView = "answers";
  showAnswers.textContent = "답변 같이 보기";

  const reset = document.createElement("button");
  reset.type = "button";
  reset.className = "review-chip review-chip-ghost";
  reset.dataset.reviewReset = "true";
  reset.textContent = "체크 초기화";

  const filterToggle = document.createElement("button");
  filterToggle.type = "button";
  filterToggle.className = "review-chip";
  filterToggle.dataset.reviewFilterToggle = "true";
  filterToggle.textContent = "미체크만 보기";

  const randomOne = document.createElement("button");
  randomOne.type = "button";
  randomOne.className = "review-chip";
  randomOne.dataset.reviewRandom = "1";
  randomOne.textContent = "랜덤 1문제";

  const randomUnknownFive = document.createElement("button");
  randomUnknownFive.type = "button";
  randomUnknownFive.className = "review-chip";
  randomUnknownFive.dataset.reviewUnknownSet = "5";
  randomUnknownFive.textContent = "미체크 5문제";

  const progress = document.createElement("span");
  progress.className = "review-progress";
  progress.textContent = `0 / ${totalCount} 체크`;

  const pickerStatus = document.createElement("p");
  pickerStatus.className = "review-picker-status";
  pickerStatus.textContent = "랜덤 뽑기로 오늘 볼 문제를 바로 고를 수 있습니다.";

  controls.append(questionOnly, showAnswers, filterToggle, randomOne, randomUnknownFive, reset);
  toolbar.append(title, controls, progress);
  toolbar.append(pickerStatus);
  return { toolbar, progress, pickerStatus, filterToggle };
}

function setMode(section, mode) {
  section.classList.toggle("questions-only", mode === "questions");

  section.querySelectorAll("[data-review-view]").forEach((button) => {
    const isActive = button.dataset.reviewView === mode;
    button.classList.toggle("is-active", isActive);
    button.setAttribute("aria-pressed", String(isActive));
  });
}

function setFilter(section, filter, filterToggle) {
  const isUncheckedOnly = filter === "unchecked";
  section.classList.toggle("unchecked-only", isUncheckedOnly);
  filterToggle.classList.toggle("is-active", isUncheckedOnly);
  filterToggle.setAttribute("aria-pressed", String(isUncheckedOnly));
  filterToggle.textContent = isUncheckedOnly ? "전체 보기" : "미체크만 보기";
}

function updateProgress(section, progressNode) {
  const cards = [...section.querySelectorAll(".question-bank-card")];
  const checkedCount = cards.filter((card) => card.classList.contains("is-done")).length;
  progressNode.textContent = `${checkedCount} / ${cards.length} 체크`;
}

function clearPicked(cards) {
  cards.forEach((card) => card.classList.remove("is-picked"));
}

function pickRandomCards(cards, count) {
  const unchecked = cards.filter((card) => !card.classList.contains("is-done"));
  const pool = unchecked.length >= count ? unchecked : cards;
  const shuffled = [...pool];

  for (let index = shuffled.length - 1; index > 0; index -= 1) {
    const randomIndex = Math.floor(Math.random() * (index + 1));
    [shuffled[index], shuffled[randomIndex]] = [shuffled[randomIndex], shuffled[index]];
  }

  return shuffled.slice(0, Math.min(count, shuffled.length));
}

function pickUncheckedCards(cards, count) {
  const unchecked = cards.filter((card) => !card.classList.contains("is-done"));
  const shuffled = [...unchecked];

  for (let index = shuffled.length - 1; index > 0; index -= 1) {
    const randomIndex = Math.floor(Math.random() * (index + 1));
    [shuffled[index], shuffled[randomIndex]] = [shuffled[randomIndex], shuffled[index]];
  }

  return shuffled.slice(0, Math.min(count, shuffled.length));
}

function updatePickerStatus(node, pickedCards, preferUnchecked) {
  if (pickedCards.length === 0) {
    node.textContent = "랜덤으로 고를 문제가 없습니다.";
    return;
  }

  const pickedLabels = pickedCards
    .map((card) => card.querySelector(".question-bank-no")?.textContent?.trim())
    .filter(Boolean)
    .join(", ");

  node.textContent = preferUnchecked
    ? `안 푼 문제 우선으로 ${pickedLabels}번을 골랐습니다.`
    : `전체 범위에서 ${pickedLabels}번을 골랐습니다.`;
}

function attachReviewMode(section, state) {
  const sectionId = section.id;
  const grid = section.querySelector(".question-bank-grid");
  const cards = [...section.querySelectorAll(".question-bank-card")];

  if (!grid || cards.length === 0) {
    return;
  }

  const { toolbar, progress, pickerStatus, filterToggle } = createToolbar(sectionId, cards.length);
  section.insertBefore(toolbar, grid);

  cards.forEach((card, index) => {
    const cardId = `${sectionId}-${index + 1}`;
    card.dataset.reviewCardId = cardId;

    const button = document.createElement("button");
    button.type = "button";
    button.className = "review-toggle";
    button.dataset.reviewToggle = cardId;
    button.textContent = "체크";

    const markDone = () => {
      const isDone = !card.classList.contains("is-done");
      card.classList.toggle("is-done", isDone);
      button.classList.toggle("is-done", isDone);
      button.textContent = isDone ? "완료" : "체크";
      button.setAttribute("aria-pressed", String(isDone));

      state.done[cardId] = isDone;
      saveReviewState(state);
      updateProgress(section, progress);
    };

    button.addEventListener("click", markDone);
    card.append(button);

    if (state.done[cardId]) {
      card.classList.add("is-done");
      button.classList.add("is-done");
      button.textContent = "완료";
      button.setAttribute("aria-pressed", "true");
    } else {
      button.setAttribute("aria-pressed", "false");
    }
  });

  toolbar.addEventListener("click", (event) => {
    const target = event.target;

    if (!(target instanceof HTMLButtonElement)) {
      return;
    }

    if (target.dataset.reviewView) {
      const mode = target.dataset.reviewView;
      state.modes[sectionId] = mode;
      setMode(section, mode);
      saveReviewState(state);
      return;
    }

    if (target.dataset.reviewReset) {
      cards.forEach((card) => {
        const cardId = card.dataset.reviewCardId;
        delete state.done[cardId];
        card.classList.remove("is-done");

        const toggle = card.querySelector(".review-toggle");
        if (toggle instanceof HTMLButtonElement) {
          toggle.classList.remove("is-done");
          toggle.textContent = "체크";
          toggle.setAttribute("aria-pressed", "false");
        }
      });

      clearPicked(cards);
      pickerStatus.textContent = "체크를 초기화했습니다. 랜덤 뽑기로 다시 시작할 수 있습니다.";
      saveReviewState(state);
      updateProgress(section, progress);
      return;
    }

    if (target.dataset.reviewFilterToggle) {
      const nextFilter = section.classList.contains("unchecked-only") ? "all" : "unchecked";
      state.filters[sectionId] = nextFilter;
      setFilter(section, nextFilter, filterToggle);
      saveReviewState(state);
      pickerStatus.textContent = nextFilter === "unchecked"
        ? "체크하지 않은 문제만 보도록 바꿨습니다."
        : "전체 문제를 다시 보도록 바꿨습니다.";
      return;
    }

    if (target.dataset.reviewRandom) {
      const count = Number(target.dataset.reviewRandom);
      const uncheckedCount = cards.filter((card) => !card.classList.contains("is-done")).length;
      const preferUnchecked = uncheckedCount >= count;
      const pickedCards = pickRandomCards(cards, count);

      clearPicked(cards);
      pickedCards.forEach((card) => card.classList.add("is-picked"));
      updatePickerStatus(pickerStatus, pickedCards, preferUnchecked);

      const firstCard = pickedCards[0];
      if (firstCard) {
        firstCard.scrollIntoView({ behavior: "smooth", block: "center" });
      }

      return;
    }

    if (target.dataset.reviewUnknownSet) {
      const count = Number(target.dataset.reviewUnknownSet);
      const pickedCards = pickUncheckedCards(cards, count);

      clearPicked(cards);
      pickedCards.forEach((card) => card.classList.add("is-picked"));

      if (pickedCards.length === 0) {
        pickerStatus.textContent = "미체크 문제가 없습니다. 이미 전부 체크한 상태예요.";
        return;
      }

      if (pickedCards.length < count) {
        pickerStatus.textContent = `미체크 문제가 ${pickedCards.length}개라서 남은 문제만 골랐습니다.`;
      } else {
        pickerStatus.textContent = "미체크 문제 중에서 5개를 골랐습니다.";
      }

      const firstCard = pickedCards[0];
      if (firstCard) {
        firstCard.scrollIntoView({ behavior: "smooth", block: "center" });
      }
    }
  });

  setMode(section, state.modes[sectionId] || "answers");
  setFilter(section, state.filters[sectionId] || "all", filterToggle);
  updateProgress(section, progress);
}

document.addEventListener("DOMContentLoaded", () => {
  const state = loadReviewState();
  const sections = document.querySelectorAll(".review-bank-section");
  sections.forEach((section) => attachReviewMode(section, state));
});

"use strict";

const BASE_URL = "http://127.0.0.1:8000";
const INTRO_URL = `${BASE_URL}/about`;
const SCHEDULE_URL = `${BASE_URL}/schedule`;

async function fetchClubInfo() {
    try {
        const response = await fetch(INTRO_URL);
        const data = await response.json();
        const ids = ["overall", "dtm", "speaker", "pa", "dj"];
        ids.forEach((id) => {
            const element = document.getElementById(`desc-${id}`);
            if (element) {
                element.innerText = data[id];
            }
        });
    }
    catch (error) {
        console.error("紹介文の取得に失敗：", error);
    }
}

async function fetchSchedule() {
    try {
        const response = await fetch(SCHEDULE_URL);
        const data = await response.json();
        const listElement = document.getElementById("schedule-list");
        if (!listElement)
            return;
        listElement.innerHTML = ""; // 読み込み中... を消去
        data.forEach((item) => {
            const timelineHtml = `
                <div class="position-relative mb-5" style="padding-left: 15px;">
                    <div style="position: absolute; left: -26px; top: 5px; width: 12px; height: 12px; border-radius: 50%; background-color: #10b981; border: 2px solid #fff; box-shadow: 0 0 0 4px rgba(16, 185, 129, 0.15);"></div>
                    
                    <div>
                        <span class="text-success fw-bold" style="font-size: 0.85rem; letter-spacing: 0.05em;">${item.date}</span>
                        <h4 class="fw-bold mt-1 mb-2" style="font-size: 1.15rem; color: #1e293b;">${item.title}</h4>
                        <p class="text-secondary" style="font-size: 0.95rem; line-height: 1.6; max-width: 700px;">${item.description}</p>
                    </div>
                </div>
            `;
            listElement.insertAdjacentHTML("beforeend", timelineHtml);
        });
    }
    catch (error) {
        console.error("スケジュールの取得に失敗：", error);
    }
}

fetchClubInfo();
fetchSchedule();

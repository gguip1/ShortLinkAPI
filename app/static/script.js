document.getElementById("shorten-btn").addEventListener("click", async function() {
    let urlInput = document.getElementById("url-input");
    let resultDiv = document.getElementById("result");
    let shortBtn = document.getElementById("shorten-btn");

    let originalUrl = urlInput.value.trim();  // 공백 제거

    if (!originalUrl) {
        alert("Please enter a valid URL!");
        return;
    }

    // 로딩 메시지 표시
    resultDiv.innerHTML = `<p>Shortening URL...</p>`;
    shortBtn.disabled = true;  // 버튼 비활성화 (중복 요청 방지)

    try {
        let response = await fetch("/shorten", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ original_url: originalUrl })
        });

        if (!response.ok) {
            let errorData = await response.json();
            throw new Error(errorData.error || "Failed to shorten URL");
        }

        let data = await response.json();

        if (data.short_url) {
            resultDiv.innerHTML = `
                <p>Shortened URL: 
                    <a href="${data.short_url}" target="_blank">${data.short_url}</a>
                </p>
            `;
            urlInput.value = "";  // 입력 필드 초기화
        } else {
            throw new Error("Unexpected response from server");
        }

    } catch (error) {
        resultDiv.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
    } finally {
        shortBtn.disabled = false;  // 버튼 활성화
    }
});

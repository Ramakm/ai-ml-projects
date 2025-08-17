document.addEventListener("DOMContentLoaded", () => {
    let history = JSON.parse(localStorage.getItem("history") || "[]");
    let container = document.getElementById("history");
  
    if (history.length === 0) {
      container.innerHTML = "<p>No history found.</p>";
    } else {
      history.forEach(item => {
        container.innerHTML += `
          <div class="history-item">
            <p><b>Plate:</b> ${item.text}</p>
            <img src="/static/uploads/${item.filename}" width="200">
          </div>
        `;
      });
    }
  });
  
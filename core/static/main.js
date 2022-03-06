let dropArea = document.getElementsByClassName("dropArea")[0];
let header = document.getElementById("header");
const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value;
var copyText = document.getElementById("downloadLink");
const formInput = document.getElementById("file");
let linkDiv = document.getElementById("download-button");
let loader = document.getElementsByClassName("loader")[0];
let copyAlert = document.getElementsByClassName("alert")[0];

dropArea.addEventListener("dragover", (event) => {
  event.preventDefault();
  dropArea.classList.add("active");
  header.textContent = "Release to upload File";
});

dropArea.addEventListener("drop", (event) => {
  event.preventDefault();
  file = event.dataTransfer.files[0];
  loader.style.display = "block";
  header.textContent = "Uploading...";
  uploadFile();
});

formInput.addEventListener("change", (event) => {
  file = event.target.files[0];
  uploadFile();
});

function uploadFile() {
  let fd = new FormData();
  fd.append("file", file);
  fetch("/", {
    method: "POST",
    headers: { "X-CSRFToken": csrfToken },
    mode: "same-origin",
    body: fd,
  })
    .then((response) => response.json())
    .then((data) => {
      if (data.response == "True") {
        linkDiv.style.display = "flex";
        loader.style.display = "none";
        header.textContent = data.filename + " Uploaded successfully";
        copyText.value = window.location.href.slice(0, -1) + data.filelink;
        console.log("visible");
      }
    });
}

function CopyText() {
  copyAlert.style.display = "block";
  setTimeout(() => {
    copyAlert.style.display = "none";
  }, 3000);

  copyText.select();
  copyText.setSelectionRange(0, 99999);
  navigator.clipboard.writeText(copyText.value);
}

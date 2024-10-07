document.getElementById('pdfForm').addEventListener('submit', function (event) {
    const fileInput = document.getElementById('file');
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a file.");
        event.preventDefault();
        return;
    }

    if (file.type !== 'application/pdf') {
        alert("Please upload a valid PDF file.");
        fileInput.value = '';
        event.preventDefault();
        return;
    }
});
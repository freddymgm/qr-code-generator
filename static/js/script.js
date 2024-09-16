/* script.js */

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('qr-form');
    const qrCodeContainer = document.querySelector('.qr-code');
    const downloadLink = document.querySelector('.download-link');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const formData = new FormData(form);

        fetch('/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.blob())
        .then(blob => {
            const url = URL.createObjectURL(blob);
            const img = document.createElement('img');
            img.src = url;
            qrCodeContainer.innerHTML = '';
            qrCodeContainer.appendChild(img);

            downloadLink.href = url;
            downloadLink.download = 'qr_code.png';
            downloadLink.style.display = 'block';
        })
        .catch(error => {
            console.error('Error:', error);
            qrCodeContainer.innerHTML = 'An error occurred while generating the QR code.';
        });
    });
});
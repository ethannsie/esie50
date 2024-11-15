document.addEventListener("DOMContentLoaded", () => {
    const uploadForm = document.getElementById("uploadForm");
    const imageInput = document.getElementById("imageInput");
    const imageDisplay = document.getElementById("imageDisplay");

    // Handle form submission to upload files
    uploadForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const files = imageInput.files;
        if (files.length === 0) {
            alert("Please select at least one image to upload.");
            return;
        }

        // Convert files to data URLs and display each image
        for (const file of files) {
            const reader = new FileReader();
            reader.onload = (e) => displayImage(e.target.result);
            reader.readAsDataURL(file);
        }
    });

    // Function to display the uploaded image
    function displayImage(src) {
        const cell = document.createElement("div");
        cell.classList.add("cell");

        const img = document.createElement("img");
        img.src = src;
        img.alt = "Uploaded Image";
        img.classList.add("thumbnail");

        cell.appendChild(img);
        imageDisplay.appendChild(cell);
    }
});

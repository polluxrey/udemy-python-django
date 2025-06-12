const quill = new Quill('#editor', {
    theme: 'snow'
});

document.getElementById('newPostForm').addEventListener('submit', function (e) {
    e.preventDefault(); // Prevent default form submission

    // Clear previous errors
    document.getElementById('titleError').classList.add('d-none');
    document.getElementById('urlError').classList.add('d-none');
    document.getElementById('contentError').classList.add('d-none');

    const titleInput = document.getElementById('title');
    const title = titleInput.value.trim();
    const urlInput = document.getElementById('image_url');
    const image_url = urlInput.value.trim();
    const content = quill.root.innerHTML.trim();

    if (!title) {
        document.getElementById('titleError').classList.remove('d-none');
        return;
    }

    if (!image_url) {
        document.getElementById('urlError').classList.remove('d-none');
        return;
    }

    if (!content) {
        document.getElementById('contentError').classList.remove('d-none');
        return;
    }

    document.getElementById('content-input').value = content;

    // Submit the form manually if valid
    e.target.submit();
});

document.getElementById('cancelBtn').addEventListener('click', function () {
    document.getElementById('newPostForm').reset();  // Clear fields
    quill.setContents([]);                           // Clear Quill editor
});
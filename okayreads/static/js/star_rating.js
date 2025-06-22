document.addEventListener('DOMContentLoaded', function () {
    const ratingContainer = document.getElementById('star-rating');
    const rating = parseFloat(ratingContainer.dataset.rating);

    const fullStars = Math.floor(rating);
    const partialStar = rating - fullStars
    const totalStars = 5;

    ratingContainer.innerHTML = '';

    for (i = 0; i < fullStars; i++) {
        ratingContainer.innerHTML += '<i class="bi bi-star-fill full-star"></i>';
    }

    // For partial star
    if (partialStar) {
        ratingContainer.innerHTML += `<i class="bi bi-star-fill partial-star" style="--fill-percentage: ${partialStar * 100}%"></i>`
    }

    const emptyStars = totalStars - fullStars - (partialStar ? 1 : 0);
    for (i = 0; i < emptyStars; i++) {
        ratingContainer.innerHTML += '<i class="bi bi-star-fill"></i>';
    }
})
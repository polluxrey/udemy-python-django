document.addEventListener('DOMContentLoaded', function () {
    const totalStars = 5;
    const ratingContainers = document.getElementsByClassName("star-rating");

    for (var i = 0; i < ratingContainers.length; i++) {
        var rating = parseFloat(ratingContainers[i].dataset.rating);
        var fullStars = Math.floor(rating);
        var partialStar = rating - fullStars;

        ratingContainers[i].innerHTML = '';

        for (var j = 0; j < fullStars; j++) {
            ratingContainers[i].innerHTML += '<i class="bi bi-star-fill full-star"></i>';
        }

        // For partial star
        if (partialStar) {
            ratingContainers[i].innerHTML += `<i class="bi bi-star-fill partial-star" style="--fill-percentage: ${partialStar * 100}%"></i>`
        }

        var emptyStars = totalStars - fullStars - (partialStar ? 1 : 0);
        for (j = 0; j < emptyStars; j++) {
            ratingContainers[i].innerHTML += '<i class="bi bi-star-fill"></i>';
        }
    }
})
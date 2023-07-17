//Back To top button
$('.btt-link').click(function (e) {
    window.scrollTo(0, 0);
});

//Sort
$(document).ready(function () {
    $('#sort-selector').on('change', function () {
        const selector = $(this);
        const currentUrl = new URL(window.location.href);
        const selectedVal = selector.val();

        if (selectedVal === "reset") {
            currentUrl.searchParams.delete("sort");
            currentUrl.searchParams.delete("direction");
            window.location.assign(currentUrl.href);
            return;
        }

        const lastIndex = selectedVal.lastIndexOf("_");
        const sort = selectedVal.substring(0, lastIndex);
        const direction = selectedVal.substring(lastIndex + 1);

        currentUrl.searchParams.set("sort", sort);
        currentUrl.searchParams.set("direction", direction);
        currentUrl.searchParams.set("page", "1");
        window.location.assign(currentUrl.href);
    });
});

// Delete Modal

$(document).ready(function () {
    $(".confirmationModalTrigger").click(function (e) {
        e.preventDefault();

        // Get message and URL from data-
        let message = $(this).data("message");
        let url = $(this).data("url");

        // Set message 
        $("#confirmationModalBody").text(message);

        // Set the URL of 'Yes' button 
        $("#confirmationModalYesButton").attr("href", url);

        // Show modal
        $("#confirmationModal").modal("show");
    });
});



// Reload location
$(document).ready(function () {
    $('.reload').on('click', function (e) {
        e.preventDefault();
        $.ajax({
            url: $(this).attr('href'),
            method: 'GET',
            success: function (response) {
                location.reload(); // Reload 
            }
        });
    })
})




// Likes JS
$(document).ready(function () {
    $('.likeAlbum').on('click', function (e) {
        e.preventDefault();
        const $this = $(this);
        const isLiked = $this.find('.filled-heart').length > 0;
        const albumId = $this.data('album-id');

        const addToWishlistUrl = `{% url 'accounts:add_to_wishlist' album_id='placeholder' %}`
            .replace('placeholder', albumId);

        $.ajax({
            url: $(this).attr('href'),
            method: 'GET',
            success: function (response) {

                if (!isLiked) {
                    $('#wishlistModal').modal('show');
                    $('#wishlistModal .add-to-wishlist-btn').attr('href',
                        addToWishlistUrl);
                } else {
                    location.reload(); // refresh 
                }

            }
        });
    });
});


// Review Album Modal
$(document).ready(function () {
    $(".addReviewButton").click(function (e) {
        e.preventDefault();
        let albumId = this.dataset.albumid;
        fetch('/accounts/album/' + albumId + '/add_review/')
            .then(response => {

                if (response.status === 401) {
                    // Get message and URL from data-
                    let message = 'You need to Login/Sign up to access this page.';
                    let url = '/accounts/login/';

                    // Set message 
                    $("#confirmationModalBody").text(message);

                    // Set the URL of 'Yes' button 
                    $("#confirmationModalYesButton").attr("href", url);

                    // Show modal
                    $("#confirmationModal").modal("show");
                } else {
                    // Handle other responses
                    window.location.href = '/accounts/album/' + albumId + '/add_review/';
                }
            });
    });
});
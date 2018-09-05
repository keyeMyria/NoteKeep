/**
 * Tries to refresh the notes returning a template with all the available user
 * notes. If the user is not logged in or something goes wrong, returns an error
 */
function refresh_notes() {
    $('#refresh_button').addClass("is-loading");
    $.ajax(
        {
            url: "/api/notes",
            success: function(data) {
                var notes = $(data).filter('#notes_container');

                // Replace current notes container with new one
                $('#notes_container').replaceWith(notes)
            },
            error: function() {
                addWarningMessage("Something went wrong refreshing your notes. Try again later.")
            },
            complete: function () {
                $('#refresh_button').removeClass("is-loading");
            }
        }
    )
}
let refreshNotesSocket;

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
                console.log("Notes refreshed");
                // Replace current notes container with new one
                $('#notes_container').replaceWith(notes)
            },
            error: function(error) {
                const reason = error.responseJSON.reason;
                addWarningMessage(reason)
            },
            complete: function () {
                $('#refresh_button').removeClass("is-loading");
            }
        }
    )
}

/**
 * Opens a socket connection with backend to get notified when must refresh the notes
 */
function openRefreshSocket() {
    refreshNotesSocket = new WebSocket( 'ws://' + window.location.host + '/ws/refresh/notes/');
    console.log("Opening socket!!");
    refreshNotesSocket.onmessage = function (e) {
        refresh_notes()
    };

    refreshNotesSocket.onclose = function (e) {
      console.log(e);
    };
}

function sendMessage() {
    refreshNotesSocket.send(JSON.stringify({'message':'message text'}))
}
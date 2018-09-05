function add_new_note() {
    $('#new_note_button').addClass("is-loading");
    $.ajax(
        {
            url: "/api/notes/add",
            success: function (noteModal) {
                // Replace current notes container with new one
                $('body').append(noteModal)
            },
            error: function () {
                addWarningMessage("Something went wrong when creating a new note. Try again later")
            },
            complete: function () {
                $('#new_note_button').removeClass("is-loading");
            }
        }
    )
}


function createOrUpdateNote(note_id) {
    // Get note information from forms
    const noteForm = $('#note_form');
    const titleInput = noteForm.find("#input_title");
    const bodyInput = noteForm.find("#input_body");

    const titleText = titleInput.val();
    const bodyText = bodyInput.val();

    $('#save_note_button').addClass("is-loading");
    $('#cancel_note_button').addClass("is-disabled");

    // Updates the note in the backend, after success, removes the modal
    // after error, shows error in modal
    $.ajax(
        {
            type: 'POST',
            url: "/api/notes/update",
            beforeSend: function(xhr, settings) {
              xhr.setRequestHeader("X-CSRFToken", csrftoken)
            },
            data: {
                title: titleText,
                body: bodyText,
                id: note_id
            },
            success: function (data) {
                removeCurrentModal()
            },
            error: function (data) {
                addWarningInModal(data['reason']);
                $('#save_note_button').removeClass("is-loading");
                $('#cancel_note_button').removeClass("is-disabled");
            },
            complete: function () {

            }
        }
    )
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');
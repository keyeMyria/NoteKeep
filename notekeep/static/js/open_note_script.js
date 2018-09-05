function open_note(note_id) {
    $.ajax(
        {
            url: "/api/notes/open/" + note_id,
            success: function(noteModal) {
                $('body').append(noteModal)
            },
            error: function() {
                addWarningMessage("Something went wrong when opening the note. Try again later")
            },
            complete: function () {
            }
        }
    )
}

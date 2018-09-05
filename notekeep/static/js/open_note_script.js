function open_note(note_id) {
    $.ajax(
        {
            url: "/api/notes/open/" + note_id,
            success: function(noteModal) {
                removeCurrentModal();
                $('body').append(noteModal)
            },
            error: function(error) {
                const reason = error.responseJSON.reason;
                addWarningMessage(reason)
            },
            complete: function () {
            }
        }
    )
}

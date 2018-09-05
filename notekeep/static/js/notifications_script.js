function addWarningMessage(reason) {
    $('#information_container')
        .html("<div class=\"notification is-warning box\">\n" +
            "  <button class=\"delete\" onclick='removeWarningMessage()'></button>\n" +
               reason +
            "  </div>")
}

function removeWarningMessage() {
      $('#information_container')
          .html("")
}

function addWarningInModal(reason) {
    $('#note_modal_information')
        .html("<div class=\"notification is-warning box\">\n" +
            "  <button class=\"delete\" onclick='removeWarningInModal()'></button>\n" +
               reason +
            "  </div>")

}

function removeWarningInModal() {
      $('#note_modal_information')
          .html("")
}

function removeCurrentModal() {
    $('#current_modal').remove()
}
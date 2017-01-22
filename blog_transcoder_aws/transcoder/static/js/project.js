var csrftoken = Cookies.get('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});



$('.alert').on('closed.bs.alert', function(event) {
  $.ajax({
    url: event.target.dataset.messageUrl,
    method: 'POST',
    data: {'message_id': event.target.dataset.messageId}
  });
});

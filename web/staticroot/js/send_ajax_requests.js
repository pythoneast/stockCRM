$(document).ready(function() {
  $('#myForm').ajaxForm({
    success: function (response) {
      if (response['success']) {
        location.reload();
      }
      else {
        var text = '';
        $.each(response['errors'], function (index, value) {
          text = text + value;
        });
        $('#errorBlock').html(text);
      }
    }
  });

  $('#deleteProductModal').ajaxForm({
    success: function (response) {
      if (response['success']) {
        location.reload();
      }
      else {
        if (response['redirect_url']) {
          var origin   = window.location.origin;
          window.location = origin + '/' + response['redirect_url'];
        }
        else {
          var text = '';
          $.each(response['errors'], function (index, value) {
            text = text + value;
          });
          $('#errorDeleteBlock').html(text);
        }
      }
    }
  });
});

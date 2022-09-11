$("form[name=sign_up_form]").submit(function(e) {
    var $form = $(this);
    var $error = $form.find(".error");
    var data = $form.serialize();

    $.ajax({
        url: "/sign-up",
        type: "POST",
        data: data,
        success: function(response) {
            console.log(response);
        },
        error: function(response) {
            console.log(response);
        }
    })

    e.preventDefault();
}
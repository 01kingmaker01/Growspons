var filter_obj = {
    "object": ""
}
const ajax_method = {
    url: url_path,
    type: 'GET',
    data: filter_obj,
    beforeSend: function () {
        $("#filter_data_post").hide()
        $(".ajaxLoader").show();
    },
    success: function (res) {
        // console.log(res);
        $("#filter_data_post").show();
        $("#filter_data_post").html(res.data);
        $(".ajaxLoader").hide();
    }
}

$(document).ready(function () {
    $(".ajaxLoader").hide();
    for (let index = 0; index < nav_fields.length; index++) {
        $("#" + nav_fields[index]).on('click', function () {
            filter_obj.object = nav_fields[index]
            // console.log(filter_obj)
            $.ajax(ajax_method);
    });
}
$("#all_data").on('click', function () {
    filter_obj.object = 'ALL'
    $.ajax(ajax_method);
});
});
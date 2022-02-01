let mainScript = function () {


    function getOneLink() {
        let linkId = $(this).data("id");

        $.ajax({
            url: '/getonelink/',
            data: ({
                link_id: linkId,
                rand: Math.random()
            }),
            dataType: "json",
            type: 'GET',
            success: function (result) {
                let link = JSON.parse(result)[0];
                $('.link-block .link-block_detail').addClass('d-none');
                $('#link-block_details_' + link.pk).empty();
                $('#link-block_details_' + link.pk).removeClass('d-none');


                let tmpl = '<ul>' +
                    '<li> url: ' + link.fields["url"] + '</li>' +
                    '<li> short_url: ' + link.fields["short_url"] + '</li>' +
                    '<li> date_create: ' + link.fields["date_create"] + '</li>' +
                    '</ul>'

                $('#link-block_details_' + link.pk).append(tmpl);

            },
            error: function (data) {
                console.log('Ошибка ajax запроса. Обратитесь к администратору. \n' + data);
            }
        });


        return false;
    }


    let init = function () {
        $('.link-block .detail').on("click", getOneLink);
    };

    $(document).ready(function () {
        init();
    });

    return {}

}();
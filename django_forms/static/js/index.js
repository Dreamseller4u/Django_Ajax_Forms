
$(document).ready(function () {
    // Сохранение состояния при перезагрузки
    if (localStorage.getItem("citi") != null) {
        $('#cities').val(localStorage.getItem('citi'))
        $('#brigade').html(localStorage.getItem('brig_html'))
        $('#brigade').val(localStorage.getItem('brig'))
        $('#facility').html(localStorage.getItem('facility_html'))
        $('#facility').val(localStorage.getItem('facility'))
        $('#info').html(localStorage.getItem('info_html'))
    }
    if (localStorage.getItem('info_html') === null) {
        localStorage.setItem('info_html_main', $('#info').html())
    }

})
$('#cities').change(function () {
    // Получения списка бригад при изменении города
    $('#facility').html('<option selected >Select facility</option>')
    $('#brigade').html('<option selected >Select brigade</option>')
    citiId = $(this).val()
    localStorage.setItem('citi', citiId);
    $.ajax({
        url: 'get_brigade',
        data: { city_id: citiId },
        success: function (response) {
            $('#brigade').html(response)
            localStorage.setItem('brig', 'Select brigade')
            localStorage.setItem('brig_html', $('#brigade').html())
            localStorage.setItem('facility', $('#facility').val())
            localStorage.setItem('facility_html', $('#facility').html())
            $('#info').html(localStorage.getItem('info_html_main'))
            localStorage.setItem('info_html', $('#info').html())
        },
        error: function (response) {
            console.log(response.error)
        }
    });
});
$('#brigade').change(async function () {
    // Получения списка объектов бригад при изменении бригады 
    brigade_id = $(this).val()
    console.log(brigade_id)
    let g = false
    await $.ajax({
        url: 'get_facility',
        data: { brigade_id: brigade_id },
        success: function (response) {
            $('#facility').html(response)
        },
        error: function (response) {
            console.log(response.error)
        }
    });
    $.ajax({
        // Поучение полной информации от бригады
        url: 'get_info',
        data: { brigade_id: brigade_id },
        success: function (response) {
            $('#info').html(response)
            localStorage.setItem('brig', brigade_id)
            localStorage.setItem('brig_html', $('#brigade').html())
            localStorage.setItem('facility_html', $('#facility').html()) // Сброс данных в обекте если выбрана только бригада
            localStorage.setItem('facility', $('#facility').val())
            localStorage.setItem('info_html', $('#info').html())
        },
        error: function (response) {
            console.log(response.error)
        }
    });
});
$('#facility').change(async function () {
    // Поучение полной информации от объекта
    facility_id = $(this).val()
    await $.ajax({
        url: 'get_info',
        data: { facility_id: facility_id },
        success: function (response) {
            $('#info').html(response)
            localStorage.setItem('facility', facility_id)
            localStorage.setItem('facility_html', $('#facility').html())
            localStorage.setItem('info_html', $('#info').html())
        },
        error: function (response) {
            console.log(response.error)
        }
    });
});


(function ($) {

    var $speciality;
    var $doctor;
    var $day;
    var $dayDatePicker;
    var $time;

    var datepickerOptions = {
        language: 'ru',
        daysOfWeekDisabled: [0,6],
        daysOfWeekHighlighted: [],
        startDate: new Date(),
        format: 'yyyy-mm-dd'
    };

    function init() {
        $speciality    = $('#id_speciality');
        $doctor        = $('#id_doctor');
        $day           = $('#id_day');
        $dayDatePicker = $('#id_day-datepicker');
        $time          = $('#id_time');

        $speciality.on('change', onChangeSpeciality);
        $doctor.on('change', onChangeDoctor);

        $dayDatePicker.datepicker(datepickerOptions);
        $dayDatePicker.hide();
        $dayDatePicker.on('changeDate', onChangeDay);

        loadSpecialities();
    }

    function loadSpecialities() {
        var url = $speciality.data('url');

        $speciality.empty().prop('disabled', true);
        $doctor.prop('disabled', true);
        $dayDatePicker.hide();
        $time.prop('disabled', true);

        $.getJSON(url, processSpecialities);
    }

    function loadDoctors() {
        var url = $doctor.data('url');
        var speciality = $speciality.val();

        if (speciality) {

            $doctor.empty().prop('disabled', true);
            $dayDatePicker.hide();
            $time.prop('disabled', true);

            $.getJSON(url, {speciality: speciality}, processDoctors);
        }
    }

    function loadTimetables() {
        var url = $day.data('url');
        var doctor = $doctor.val();

        if (doctor) {

            $dayDatePicker.hide();
            $time.prop('disabled', true);

            $.getJSON(url, {doctor: doctor}, processTimetables);
        }
    }

    function loadTimes() {
        var baseUrl = $time.data('base-url');
        var doctor = $doctor.val();
        var day = $day.val();

        if (doctor && day) {
            $time.empty().prop('disabled', true);

            $.getJSON([baseUrl, doctor, day].join('/'), processTimes);
        }
    }

    function processSpecialities(items) {

        $speciality.append($('<option>', {
            text: ''
        }));

        $.each(items, function(index, item) {
            $speciality.append($('<option>', {
                value: item.id,
                text: item.title
            }));
        });

        $speciality.prop('disabled', false);
    }

    function processDoctors(items) {

        $doctor.append($('<option>', {
            text: ''
        }));

        $.each(items, function(index, item) {
            $doctor.append($('<option>', {
                value: item.id,
                text: [item.first_name, item.last_name].join(' ')
            }));
        });

        $doctor.prop('disabled', false);
    }

    function processTimetables(items) {
        var daysOfWeekHighlighted = [];

        $.each(items, function(index, item) {
            daysOfWeekHighlighted.push(item.day_of_week+1);
        });

        $dayDatePicker.datepicker('setDaysOfWeekHighlighted', daysOfWeekHighlighted);
        $dayDatePicker.show();
    }

    function processTimes(items) {
        $time.append($('<option>', {
            text: ''
        }));

        $.each(items, function(index, item) {
            $time.append($('<option>', {
                value: item,
                text: item
            }));
        });

        $time.prop('disabled', false);
    }

    function onChangeSpeciality(e) {
        loadDoctors();
    }

    function onChangeDoctor(e) {
        loadTimetables();
    }

    function onChangeDay(e) {
        $day.val($dayDatePicker.datepicker('getFormattedDate'));

        loadTimes();
    }

    $(init);

})(jQuery);
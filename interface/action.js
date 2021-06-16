$('.form-group input').on('focus blur', function (e) {
    $(this).parents('.form-group').toggleClass('active', (e.type === 'focus' || this.value.length > 0));
}).trigger('blur');
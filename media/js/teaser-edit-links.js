jQuery(function($) {
    $('input[value][id^="id_teasers"]').each(function() {
        var it=$(this);
        it.prev().append(' [<a href="../../teaser/'+it.attr('value')+'">Edit</a>]')
    });
});


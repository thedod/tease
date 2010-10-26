jQuery(function($) {
    $('select[id="id_teaser_list"]').each(function() {
        var it=$(this);
        it.after(' [<a href="../../teaserlist/'+it.attr('value')+'">Edit/Reorder</a>]')
    });
});


/* Based on http://www.djangosnippets.org/snippets/1053/ */
jQuery(function($) {
    var renumber=function() {
            $(this).find('tr.has_original').each(function(i) {
                $(this).find('input[id$=sort_order]').val(i+1);
            });
    };
    $('div.inline-group:last').each(renumber);
    $('div.inline-group:last').sortable({
        items: 'tr.has_original',
        update: renumber
    });
    $('tr.has_original').css('cursor', 'move');
    $('div.inline-related').find('input[id$=sort_order]').css('visibility','hidden');
});


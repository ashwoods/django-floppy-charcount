jQuery(function($){

    $.fn.charsLeft = function(options){

        var defaults = {
            'source':'input',
            'dest':'.count'
        };
        var options = $.extend(defaults, options);

        var calculate = function(source, dest, maxlength){
            var remaining = maxlength - source.val().length;
            dest.html(remaining);
            /* Over 50%, change colour to orange */
            p=(100*remaining)/maxlength;
            if(p<25){
                dest.addClass('red');
            }else if(p<59){
                dest.addClass('orange');
            }else{
                dest.removeClass('orange red');
            }
        };

        this.each(function(i, el) {

            var source = $(this).find(options.source);
            var maxlength = source.attr('maxlength');
            var dest = $(this).find(options.dest);

            // calculate the remaining chars on first load
            calculate(source, dest, maxlength);

            source.keyup(function(){
                calculate(source, dest, maxlength);
            });
            source.change(function(){
                calculate(source, dest, maxlength);
            });
        });
    };

    $(".charsleft-input").charsLeft({
        'source':'textarea, input',
        'dest':".count"
    });
});

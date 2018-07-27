window.Market = {};
window.Market.initialize = function () {
		
	$('.select').change(function() {
		el = $(this).parent().attr('id');
		if (el == 'runners') {
			createList('market', $(this).val());
		}
	});
	
};

function createList(id, n) {
	if (n > $('#market li').length) {
		var rng = range($('#market li').length + 1, n);
		$.each(rng, function(i)
		{
			var li = $('<li/>')
				.addClass('list-group-item')
				.text('Runner ' + rng[i])
				.appendTo($('#market'));
		});
	} else if (n < $('#market li').length) {
		$('#market li').slice(-($('#market li').length - n)).remove()
	}
}
	
function range(start, end) {
    var array = new Array();
    for(var i = start; i <= end; i++)
    {
        array.push(i);
    }
    return array;
}
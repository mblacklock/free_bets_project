window.Market = {};
window.Market.initialize = function () {
		
	$('#bet_type .select').change(function() {
		$('.type-error').hide();
		$("#stake .input").trigger('input');
	});

		$('#runners .select').change(function() {
		createList('market', $(this).val());
	});
	
	$(document.body).on("input", '.input', function() {
		bet_type = $('#bet_type .select').val();
		if (bet_type !== null) {
			bet_stake = parseFloat($('#stake .input').val());
			runners = $('#market .runner');
			$.each(runners, function()
			{
				bookie_odds = parseFloat($(this).find('.bookie_odds .input').val());
				lay_odds = parseFloat($(this).find('.lay_odds .input').val());
				if (bet_type == 'initial') {
					lay_stake = ((bookie_odds - 1)*bet_stake + bet_stake)/(0.95 + (lay_odds - 1));
					profit_loss = (bet_stake*(bookie_odds - 1)) - (lay_stake*(lay_odds - 1));
				} else if (bet_type == 'free') {
					lay_stake = ((bookie_odds - 1)*bet_stake)/(0.95 + (lay_odds - 1));
					profit_loss = (bet_stake*(bookie_odds - 1)) - (lay_stake*(lay_odds - 1));			
				}
				lay_stake = (round(lay_stake,2)).toFixed(2);	
				profit_loss = (round(profit_loss,2)).toFixed(2);	
				$(this).find('.lay_stake').text(lay_stake);
				$(this).find('.profit_loss').text(profit_loss);
				
			});
			highlightMaximum(getText($('#market .profit_loss')));
		} else {
			$('.type-error').show();
		}
	});
	
};

function createList(id, n) {
	var len = $('#market li').length - 1;
	if (n > len) {
		var rng = range(len + 1, n);
		$.each(rng, function(i)
		{
			$('#runner-template').clone().appendTo('#market');
			var rnr = $('#market li:last')
				.find(".text").text('Runner ' + rng[i])
			$('#market #runner-template')
				.attr('id', 'runner-' + rng[i])
				.addClass('d-flex')
				.removeClass('hidden')
		});
	} else if (n < len) {
		$('#market li').slice(-(len - n)).remove();
		highlightMaximum(getText($('#market .profit_loss')));
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

function round(value, exp) {
  if (typeof exp === 'undefined' || +exp === 0)
    return Math.round(value);

  value = +value;
  exp = +exp;

  if (isNaN(value) || !(typeof exp === 'number' && exp % 1 === 0))
    return NaN;

  // Shift
  value = value.toString().split('e');
  value = Math.round(+(value[0] + 'e' + (value[1] ? (+value[1] + exp) : exp)));

  // Shift back
  value = value.toString().split('e');
  return +(value[0] + 'e' + (value[1] ? (+value[1] - exp) : -exp));
}

function highlightMaximum(elems) {
	$('.runner').removeClass('list-group-item-success');
	// Get the max value from the array    
	maxValue = Math.max.apply(this, elems);
	if (maxValue == -10000) {
		// Skip because NaN
	} else {
		// Get the index of the max value, through the built in function inArray
		index = getAllIndexes(elems,maxValue);
		$.each(index, function(i) {
			$('#runner-'+(index[i]+1)).addClass('list-group-item-success');
		});
	}
}

function getText(elems) {
	var array = new Array();
	$.each(elems, function(i)
	{
		txt = parseFloat($(this).text());
		if (isNaN(txt)){
			array.push(-10000);
		}
		else {
			array.push(txt);
		}
		
	});
    return array;
}

function getAllIndexes(arr, val) {
    var indexes = [], i = -1;
    while ((i = arr.indexOf(val, i+1)) != -1){
        indexes.push(i);
    }
    return indexes;
}
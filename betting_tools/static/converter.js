window.Converter = {};
window.Converter.initialize = function () {
	
	$(document.body).on("input", '.fraction', function() {
		$('.decimal').val('');
		$('.percent').val('');
		if ( $(this).val().split("/").length - 1 == 1 ) {
			if (checkFractionIsNumeric($(this).val())) {
				var fraction = evil($(this).val());
				$('.decimal').val(round(fraction + 1,2));
				$('.percent').val(round(1/(fraction+1)*100,1));
			}
		}
	});
	
	$(document.body).on("input", '.decimal', function() {
		$('.fraction').val('');
		$('.percent').val('');
		var decimal = $(this).val();
		if ($.isNumeric(decimal)) {
			$('.fraction').val(round(decimal-1,2) + '/1');
			$('.percent').val(round(1/decimal*100,1));
		}
	});
	
	$(document.body).on("input", '.percent', function() {
		$('.fraction').val('');
		$('.decimal').val('');
		var percent = $(this).val();
		if ($.isNumeric(percent)) {
			$('.fraction').val(round(1/percent*100-1,2) + '/1');
			$('.decimal').val(round(1/percent*100,2));
		}
	});
	
};

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

function evil(fn) {
  return new Function('return ' + fn)();
}

function checkFractionIsNumeric(str) {
	var out = true;
	var arr = str.split("/");
	$.each(	arr, function(i, val) {
		if($.isNumeric(val) == false){
			out = false;
		}
	});
	return out
}
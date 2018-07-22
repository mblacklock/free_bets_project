window.BetsSummary = {};
window.BetsSummary.initialize = function () {
		
	$('.input').on('keypress', function(e) {
		if(e.which == 13) {
			
			var el = $(this).parent().attr('id');
			if((el == 'balance' || el == 'profit') && $.isNumeric($(this).val()) == false ) {
				console.log('dsfsdfs');
				$('.has-error').show();
			} else {
				$('.has-error').hide();
				var summary_id = $('[name="bookie-summary"]').attr('data-id');
				var id = $(this).parent().parent().attr('data-id');
				var affiliate = $(this).parent().parent().attr('data-name');
			
				update_function(summary_id, affiliate, el, $(this).val());
			
				$(this).hide();
				$("tr[data-id='"+id+"'] #"+el+" .text").text($(this).val());
				$("tr[data-id='"+id+"'] #"+el+" .text").show();
				$("tr[data-id='"+id+"'] #"+el+" .edit").show();
			}
		}
	});
	
	$('.edit').click( function() {
		var id;
		id = $(this).parent().parent().attr("data-id");
		var el;
		el = $(this).parent().attr('id');
		
		$(this).hide();
		$("tr[data-id='"+id+"'] #"+el+" .input").attr("placeholder", $("tr[data-id='"+id+"'] #"+el+" .text").text());
		$("tr[data-id='"+id+"'] #"+el+" .input").show();
		$("tr[data-id='"+id+"'] #"+el+" .text").hide();
		
	});
	
	$('.banked').click( function() {
		var id;
		id = $(this).parent().parent().attr("data-id");
		if($(this).is(":checked") == true) {
			$("tr[data-id='"+id+"'] .input").prop("disabled", true);
			$("tr[data-id='"+id+"'] .edit").prop("disabled", true);
			$("tr[data-id='"+id+"'] .status").prop("disabled", true);
		}
		else {
			$("tr[data-id='"+id+"'] .input").prop("disabled", false);
			$("tr[data-id='"+id+"'] .edit").prop("disabled", false);
			$("tr[data-id='"+id+"'] .status").prop("disabled", false);
		}		
	});
};
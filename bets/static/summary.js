window.BetsSummary = {};
window.BetsSummary.initialize = function () {
		
	$('.input').on('keypress', function(e) {
		if(e.which == 13) {
			console.log(1);
			
			var el = $(this).parent().attr('id');
			
			if((el == 'balance' || el == 'profit') && $.isNumeric($(this).val()) == false ) {
					$('.has-error').show();
			} else {
				console.log(2);	
				var summary_id = $('[name="bookie-summary"]').attr('data-id');
				
				if(el == 'summary_name') {
					var affiliate = 'summary_name';
					var tab = '';
				} else {
					console.log(3);
					var id = $(this).parent().parent().attr('data-id');
					var affiliate = $(this).parent().parent().attr('data-name');
					var tab = "tr[data-id='"+id+"'] ";
				
				}
				console.log(4);
				$('.has-error').hide();
				update_function(summary_id, affiliate, el, $(this).val());
				$(this).hide();
				$(tab + "#"+el+" .text").text($(this).val());
				$(tab + "#"+el+" .text").show();
				$(tab + "#"+el+" .edit").show();
				
				console.log(tab);
				console.log(el);
			
			}
		}
	});
	
	$('.edit').click( function() {
		var el = $(this).parent().attr('id');
		
		if (el == 'summary_name') {
			var tab = '';
		}  else {
			var id = $(this).parent().parent().attr("data-id");
			var tab = "tr[data-id='"+id+"'] ";
		}
			
			$(this).hide();
			$(tab + "#"+el+" .input").attr("placeholder", $(tab + "#"+el+" .text").text());
			$(tab + "#"+el+" .input").show();
			$(tab + "#"+el+" .text").hide();		
	});
	
	$('.status').change(function() {
		var summary_id = $('[name="bookie-summary"]').attr('data-id');
		var affiliate_name = $(this).parent().parent().attr('data-name');
		var id = $(this).parent().parent().attr("data-id");
		
		update_function(summary_id, affiliate_name, 'status', $(this).val())
	});
	
	$('.banked').click( function() {
		var summary_id = $('[name="bookie-summary"]').attr('data-id');
		var affiliate_name = $(this).parent().parent().attr('data-name');
		var id = $(this).parent().parent().attr("data-id");
		
		if($(this).is(":checked")) {
			$("tr[data-id='"+id+"'] .input").prop("disabled", true);
			$("tr[data-id='"+id+"'] .edit").prop("disabled", true);
			$("tr[data-id='"+id+"'] .status").prop("disabled", true);
			
			update_function(summary_id, affiliate_name, 'banked', 'True')
		}
		else {
			$("tr[data-id='"+id+"'] .input").prop("disabled", false);
			$("tr[data-id='"+id+"'] .edit").prop("disabled", false);
			$("tr[data-id='"+id+"'] .status").prop("disabled", false);
			update_function(summary_id, affiliate_name, 'banked', 'False')
		}		
	});
};
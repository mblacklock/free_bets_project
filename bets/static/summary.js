window.BetsSummary = {};
window.BetsSummary.initialize = function () {
		
	$('.input').on('keypress', function(e) {
		if(e.which == 13) {
			
			var el = $(this).parent().attr('id');
			
			if((el == 'balance' || el == 'profit') && $.isNumeric($(this).val()) == false ) {
					$('.alert-warning').show();
					$(this).val("");
			} else {
				if(el == 'summary_name') {
					var affiliate = 'summary_name';
					var tab = '';
				} else {
					var id = $(this).closest('tr').attr('data-id');
					var affiliate = $(this).closest('tr').attr('data-name');
					var tab = "tr[data-id='"+id+"'] ";
				}
				var summary_id = $('[name="bookie-summary"]').attr('data-id');
				$('.alert-warning').hide();
				update_function(summary_id, affiliate, el, $(this).val());
				$(tab + "#"+el+" .input").attr("placeholder", $(this).val());
				$(tab + "#"+el+" .input").prop('disabled', true);
				$(tab + "#"+el+" .edit").show();
			}
		}
	});
	
	$('.edit').click( function() {
		var el = $(this).parent().attr('id');
		if (el == 'summary_name') {
			var tab = '';
		}  else {
			var id = $(this).closest('tr').attr("data-id");
			var tab = "tr[data-id='"+id+"'] ";
		}
			$(this).hide();
			$(tab + "#"+el+" .input").attr("placeholder", $(tab + "#"+el+" .input").val());
			$(tab + "#"+el+" .input").prop('disabled', false);		
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
			// NEED TO CHANGE TO REFLECT ORIGINAL STATUSES
			$("tr[data-id='"+id+"'] .input").prop("disabled", false);
			$("tr[data-id='"+id+"'] .edit").prop("disabled", false);
			$("tr[data-id='"+id+"'] .status").prop("disabled", false);
			update_function(summary_id, affiliate_name, 'banked', 'False')
		}		
	});
};
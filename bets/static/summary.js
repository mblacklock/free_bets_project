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
					$(this).attr('placeholder', '');
				} else {
					var id = $(this).closest('tr').attr('data-id');
					var affiliate = $(this).closest('tr').attr('data-name');
					var tab = "tr[data-id='"+id+"'] ";
				}
				var summary_id = $('[name="bookie-summary"]').attr('data-id');
				$('.alert-warning').hide();
				update_function(summary_id, affiliate, el, $(this).val());
				$(tab + "#"+el+" .input").val($(this).val());
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
		var affiliate_name = $(this).closest('tr').attr('data-name');
		var id = $(this).closest('tr').attr("data-id");
		if($(this).is(":checked")) {
			$("tr[data-id='"+id+"'] .input,tr[data-id='"+id+"'] .edit,tr[data-id='"+id+"'] .status").prop("disabled", true);
			update_function(summary_id, affiliate_name, 'banked', 'True')
		}
		else {
			$("tr[data-id='"+id+"'] .edit,tr[data-id='"+id+"'] .status").prop("disabled", false);
			update_function(summary_id, affiliate_name, 'banked', 'False')
			$("tr[data-id='"+id+"'] .input").each(function() {
				if($(this).val() == "") {
					$(this).prop("disabled", false);
				}
			});
		}		
	});
};
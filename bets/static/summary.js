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
	
	$('.select').change(function() {
		el = $(this).parent().attr('id');
		if (el == 'status') {
			var summary_id = $('[name="bookie-summary"]').attr('data-id');
			var affiliate_name = $(this).closest('tr').attr('data-name');
			var id = $(this).closest('tr').attr("data-id");
			
			var curr_status = $(this).val();
			update_function(summary_id, affiliate_name, 'status', curr_status);
			update_action_button(id, curr_status, affiliate_name);
		}
	});
	
	$('.banked').click( function() {
		var summary_id = $('[name="bookie-summary"]').attr('data-id');
		var affiliate_name = $(this).closest('tr').attr('data-name');
		var id = $(this).closest('tr').attr("data-id");
		if($(this).is(":checked")) {
			$("tr[data-id='"+id+"'] .input,tr[data-id='"+id+"'] .edit,tr[data-id='"+id+"'] .select, tr[data-id='"+id+"'] .action").prop("disabled", true);
			update_function(summary_id, affiliate_name, 'banked', 'True')
		}
		else {
			$("tr[data-id='"+id+"'] .edit,tr[data-id='"+id+"'] .select, tr[data-id='"+id+"'] .action").prop("disabled", false);
			update_function(summary_id, affiliate_name, 'banked', 'False')
			$("tr[data-id='"+id+"'] .input").each(function() {
				if($(this).val() == "") {
					$(this).prop("disabled", false);
				}
			});
		}		
	});
};

function update_action_button(id, curr_status, affiliate_name) {
	$("tr[data-id='"+id+"'] .action").val(curr_status);
	$("tr[data-id='"+id+"'] .action").removeClass('hidden');
	if (curr_status == 'signup' | curr_status == 'deposit'){
		$("tr[data-id='"+id+"'] .action_form").prop("target", '_blank');
		$("tr[data-id='"+id+"'] .action").html('Go to '+ affiliate_name + ' <i class="fas fa-arrow-right"></i>');
	}
	else if (curr_status == 'initial' | curr_status == 'free'){
		$("tr[data-id='"+id+"'] .action_form").prop("target", "_self");
		$("tr[data-id='"+id+"'] .action").html('Create Arb Market <i class="fas fa-arrow-right"></i>');
	}
	else if (curr_status == 'complete') {
		$("tr[data-id='"+id+"'] .action").addClass('hidden');
	}
}
window.BetsSummary = {};
window.BetsSummary.initialize = function () {
		
	$('.input').keypress(function(e) {
		if(e.which == 13) {
			var id;
			id = $(this).parent().parent().attr('data-id');

			var el;
			el = $(this).parent().attr('id');
			
			$(this).hide();
			$("tr[data-id='"+id+"'] #"+el+" .text").text($(this).val());
			$("tr[data-id='"+id+"'] #"+el+" .text").show();
			$("tr[data-id='"+id+"'] #"+el+" .edit").show();
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
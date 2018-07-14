window.BetsSummary = {};
window.BetsSummary.initialize = function () {
		
	$('.input').keypress(function(e) {
		console.log('enter');
		if(e.which == 13) {
			var id;
			id = $(this).parent().parent().attr('data-id');
			console.log(id);
			var el;
			el = $(this).parent().attr('id');
			console.log(el);
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
		$("tr[data-id='"+id+"'] #"+el+" .input").attr("placeholder", $("tr[data-id='"+id+"'] .text").text());
		$("tr[data-id='"+id+"'] #"+el+" .input").show();
		$("tr[data-id='"+id+"'] #"+el+" .text").hide();
		
	});
    
};
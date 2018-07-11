window.BetsSummary = {};
window.BetsSummary.initialize = function () {
	
	$('input[name="bet365-username"]').keypress(function(e) {
		if(e.which == 13) {
			console.log($(this).val());
			$(this).hide();
			$('#bet365-username-text').text($(this).val());
			$('#bet365-username-text').show();
		}
	});
    
};
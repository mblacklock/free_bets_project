window.Market = {};
window.Market.initialize = function () {
		
	$('.select').change(function() {
		el = $(this).parent().attr('id');
		if (el == 'market') {
			createList('market', $(this).val());
		}
	});
	
};

function createList(id, n) {
	var range = [...Array(n).keys()];
	const $ul = $('<ul>', {id: id}).append(
	range.map(item => 
		$("<li>").append(text(item))
  )
);
}
//CREATE JAVASCRIPT TEST
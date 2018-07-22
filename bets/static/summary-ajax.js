
function update_function(summary_id, name, param, value) {	
	$.get('/summary/update/' + param, 
		{'summary_id': summary_id, 'affiliate_name': name, 'value': value}, function(data){
	});
}
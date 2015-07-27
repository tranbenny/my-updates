var loadUpdates = function() {
	$('#nytimesbooks').hide();
	$('#weather').hide();
	$('#nytimesbooks').fadeIn('slow');
	$('#weather').delay(700).fadeIn('slow');
};

loadUpdates();
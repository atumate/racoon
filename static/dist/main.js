
$(document).ready(function(){
	var API="http://192.168.125.128:7000";

	$("#btn-url-submit").on("click", function() {

		//var url = $('#input-url').val();


		$.ajax({
			method: "GET",
			url: API,
			// dataType: "script"
		}).done( function(response,status,xhr) {
			console.log(response)
		}).fail( function(e) {
			console.log(e)
		});

	});

});




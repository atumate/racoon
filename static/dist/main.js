
$(document).ready(function(){
	var API_PATH="/api"; // abs path recommned

	$('#textarea-urls').val(' https://github.com \n  http://nixni.cc');

	$("#btn-url-submit").on("click", function() {
		show_loader();

		urls_array=get_urls_array_from_raw($('#textarea-urls').val());

		var op="getUrlsStatusCode";
		var post_data={
			op:op,
			urls:urls_array
		};



		

		$.ajax({
			method: "POST",
			url: API_PATH,
			data: JSON.stringify(post_data),
			dataType:'json',
			contentType: 'application/json;charset=UTF-8',
		}).done( function(response,status,xhr) {
			$('#response-raw').html(JSON.stringify(response))
			console.log(response)
			console.log(status)
			console.log(xhr)
		}).fail( function(e) {
			//console.log(e.responseText)
			$('#response-raw').html('ERROR:<br>'+e.responseText)
			 console.log(e)
		});
	});

	$("#btn-url-submit").click();


	console.log(is_url_with_protocal('http://nixni.cc'))

});

function show_loader(){
	$('#response-raw').html('<img src="/img/index.beating-heart-preloader.svg">');
}

function get_urls_array_from_raw(raw_str){
	console.log(raw_str)
	arrayOfUrls = raw_str.split(/[\r\n]+/)
	for (var i = 0; i < arrayOfUrls.length; i++) {
		arrayOfUrls[i]=arrayOfUrls[i].replace(/^\s+|\s+$/g, '');
	}
	console.log(arrayOfUrls)

	return arrayOfUrls;
}








function is_url_with_protocal(surl){
	var reg = /^(http|https|ftp):\/\//g;
	return surl.match(reg)?1:0;
}





// method to get the uid from the url
function getUrlid() {
    var urlid = new URL(window.location.href);
    console.log(urlid);
    id=urlid.searchParams.get("uid");
    console.log(id);
  

// attaching  the uid to all links on the page
$('a').each(function() {
	console.log('Adding');
  this.href +='?&uid='+id;
});
    return id;
}


var uid;
uid=getUrlid();





console.log(uid)


$('.question-header').click(function(){

	console.log('has asked a question');
	chrome.extension.sendMessage({
		from:'stackoverflowlog',
		subject:'asked a question',
		uid:uid

	});

});


$('.vote-up-off').click(function(){

	console.log('has up voted');
	chrome.extension.sendMessage({
		from:'stackoverflowlog',
		subject:'vote-up',
		uid:uid

	});

});

$('.vote-down-off').click(function(){

	console.log('has down voted');
	chrome.extension.sendMessage({
		from:'stackoverflowlog',
		subject:'vote-down',
		uid:uid

	});

});



$('.star-off').click(function(){

	console.log('has set a Favorite');
	chrome.extension.sendMessage({
		from:'stackoverflowlog',
		subject:'favourite',
		uid:uid

	});

});


$('d-inline-flex ai-center ws-nowrap s-btn s-btn__primary').click(function(){

	console.log('has voted');
	chrome.extension.sendMessage({
		from:'stackoverflowlog',
		subject:'ask question',
		uid:uid

	});

});



$('.post-menu').click(function(){
	console.log('The user has shared a post');
	chrome.extension.sendMessage({
		from:'stackoverflowlog',
		subject:'shared post',
		uid:uid

	});
});


$('.comments-link').click(function(){
	console.log('The user has entered a comment');

	chrome.extension.sendMessage({
		from:'stackoverflowlog',
		subject:'commented on post',
		uid:uid

	});
});


// $('#content').scroll(function(){
// 	console.log('The user has entered a comment');

// 	chrome.extension.sendMessage({
// 		from:'stackoverflowlog',
// 		subject:'commented on post'
// 	});
// });

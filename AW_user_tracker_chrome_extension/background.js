console.log('Hello Wordl');


// $.ajax({

//     url : 'http://voicebunny.comeze.com/index.php',
//     type : 'GET',
//     data : {
//         'numberOfWords' : 10
//     },
//     dataType:'json',
//     success : function(data) {              
//         alert('Data: '+data);
//     },
//     error : function(request,error)
//     {
//         alert("Request: "+JSON.stringify(request));
//     }
// });
// var url

// chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
//      url = tabs[0].url;
// });
// console.log(url)

// var uid;
// var user_activity={votes:0,shared_posts:0,comments:0};

chrome.runtime.onMessage.addListener(function (msg,sender){
	// if((msg.from==='stackoverflowlog') &&(msg.subject==='geturl'))
	// {
	// 	console.log('The URL is');
	// 	chrome.tabs.query({'active': true, 'currentWindow': true}, function (tabs) {
	// 		console.log(tabs[0].url);
 //     	 	uid=JSON.stringify(tabs[0].url);
	// 		});
		
	// 	// uid=uid.slice(-1,-3);
	// 	console.log(uid);
	// 	// user_activity['votes']=user_activity['votes']+1;
	// }
	


	if((msg.from==='stackoverflowlog') &&(msg.subject==='asked a question'))
	{
		console.log('The person asked a question');
		console.log(msg.uid);
		var user_activity ={}
		user_activity['count']=1;
		user_activity['activity']='asked a question';
		user_activity['id']=msg.uid;
	}


	if((msg.from==='stackoverflowlog') &&(msg.subject==='vote-up'))
	{
		console.log('The person has voted');
		console.log(msg.uid);
		var user_activity ={}
		user_activity['count']=1;
		user_activity['activity']='vote-up';
		user_activity['id']=msg.uid;
	}


	if((msg.from==='stackoverflowlog') &&(msg.subject==='vote-down'))
	{
		console.log('The person has voted');
		console.log(msg.uid);
		var user_activity ={}
		user_activity['count']=1;
		user_activity['activity']='vote-down';
		user_activity['id']=msg.uid;
	}

	if((msg.from==='stackoverflowlog') &&(msg.subject==='favourite'))
	{
		console.log('The person has search');
		console.log(msg.uid);
		var user_activity ={}
		user_activity['count']=1;
		user_activity['activity']='mark_favourite';
		user_activity['id']=msg.uid;
	}




	if((msg.from==='stackoverflowlog') &&(msg.subject==='ask question'))
	{
		console.log('The person has search');
		console.log(msg.uid);
		var user_activity ={}
		user_activity['count']=1;
		user_activity['activity']='ask question';
		user_activity['id']=msg.uid;
	}
	
	


	if((msg.from==='stackoverflowlog') &&(msg.subject==='shared post'))
	{
		console.log('The person has shared a post');
		console.log(msg.uid);
		var user_activity ={}

		user_activity['count']=1;
		user_activity['activity']='shared_posts';		
		user_activity['id']=msg.uid;
	}

	if((msg.from==='stackoverflowlog') && (msg.subject==='commented on post'))
	{
		console.log('The person has commented on a post');
		console.log(msg.uid);
		var user_activity ={}

		user_activity['count']=1;
		user_activity['activity']='comment'		
		user_activity['id']=msg.uid


	}

// console.log(user_activity)

$.post('http://127.0.0.1:5000/profile',user_activity)

});


// $.ajax({
// 	url:'http://127.0.0.1:5000/profile',
// 	type:'POST',
// 	data:user_activity,
// })


// chrome.runtime.onMessage.addListener(function (msg,sender){
	
// });
